#!/usr/bin/env python3
"""Quote every Mermaid node / edge / subgraph label in the notes (rulebook R20).

Unquoted labels are the single biggest source of "diagram does not render"
bugs: Mermaid's flowchart grammar silently mis-reads brackets, commas,
parens, `|`, `-` and Unicode look-alikes inside a bare label, and a bad
label aborts the *whole* diagram.

This script is purely syntactic and idempotent:

  A[O2]          ->  A["O2"]
  A(O2)          ->  A("O2")
  A>no lone pair] ->  A>"no lone pair"]
  A -->|yes| B   ->  A -->|"yes"| B
  A -- lifts --> B ->  A -- "lifts" --> B
  subgraph CN    ->  subgraph "CN"

It never touches already-quoted labels, so it is safe to re-run.

Usage:  python3 scripts/quote_mermaid_labels.py [--check]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FENCE = re.compile(r"^\s*```\s*(\w+)?\s*$")
# lines that are grammar, not content
DIRECTIVE = re.compile(
    r"^\s*(%%|classDef|class |style |linkStyle|click |direction|end\b|flowchart|graph\b|"
    r"flowchart-|subgraph\s|$)"
)

SUBGRAPH = re.compile(r"^(\s*subgraph\s+)(\S.*?)\s*$")
EDGE_LABEL = re.compile(r"(\|[^|\n]*\|)")          # A -->|text| B
# A *dash* label is `A -- text --> B`: the left arrow has no head and is
# detached from its node, the right arrow has one.  That asymmetry is what
# separates a real label from a plain chain such as `A --> B --> C`, so the
# pattern anchors on a node character before the space and forbids arrows
# inside the label.
_LEFT = r"(?:-{2,}(?!>)|-\.-|={2,}(?!>)|-{2,}o|-{2,}x)"
_RIGHT = r"(?:-+>|\.-+>|={2,}>|-+o>|-+x>)"
DASH_LABEL = re.compile(
    r"(?<=[A-Za-z0-9_\]\)])\s+(" + _LEFT + r")\s+(?P<lab>(?:(?!-+>)[^<>|])+?)"
    r"\s+(" + _RIGHT + r")\s+(?=[A-Za-z_])")


def quote(text: str) -> str:
    if not text.strip():
        return text
    if text.startswith('"'):
        return text
    return '"' + text.replace('"', "#quot;") + '"'


def fix_pairs(line: str) -> str:
    """Quote the inside of every outermost [..] / (..) shape, then skip inside it."""
    out, i, n = [], 0, len(line)
    while i < n:
        ch = line[i]
        if ch == '"':                      # already-quoted region: copy through
            j = i + 1
            while j < n and line[j] != '"':
                j += 1
            out.append(line[i:j + 1])
            i = j + 1
            continue
        if ch in "[({":
            closer = {"[": "]", "(": ")", "{": "}"}[ch]
            depth, j = 0, i
            while j < n:
                if line[j] == '"':
                    j += 1
                    while j < n and line[j] != '"':
                        j += 1
                elif line[j] in "[({":
                    depth += 1
                elif line[j] in "])}":
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            if j >= n or line[j] != closer:      # unbalanced - leave alone
                out.append(ch)
                i += 1
                continue
        elif ch in "])}":
            out.append(ch)
            i += 1
            continue
        else:
            out.append(ch)
            i += 1
            continue
        inner = line[i + 1:j]
        out.append(ch + quote(inner) + closer)
        i = j + 1
    return "".join(out)


def fix_line(line: str) -> str:
    m = SUBGRAPH.match(line)
    if m:
        # `subgraph id[Title]` keeps its id and quotes only the title
        inner = re.match(r"([A-Za-z_][A-Za-z0-9_]*)\[(.*)\]", m.group(2))
        if inner:
            return f"{m.group(1)}{inner.group(1)}[{quote(inner.group(2))}]"
        return m.group(1) + quote(m.group(2))
    if DIRECTIVE.match(line):
        return line
    new = fix_pairs(line)
    new = EDGE_LABEL.sub(lambda m: "|" + quote(m.group(1)[1:-1]) + "|", new)
    new = DASH_LABEL.sub(
        lambda m: f" {m.group(1)} {quote(m.group('lab'))} {m.group(3)} ", new)
    return new


def main() -> int:
    check = "--check" in sys.argv
    changed_files = 0
    changed_lines = 0
    for path in sorted(ROOT.glob("*/*/notes.md")):
        src = path.read_text(encoding="utf-8")
        out, in_block, dirty = [], False, False
        for line in src.split("\n"):
            m = FENCE.match(line)
            if m:
                in_block = (m.group(1) or "").lower() == "mermaid"
                out.append(line)
                continue
            if in_block:
                new = fix_line(line)
                if new != line:
                    dirty = True
                    changed_lines += 1
                out.append(new)
            else:
                out.append(line)
        if dirty:
            changed_files += 1
            if not check:
                path.write_text("\n".join(out), encoding="utf-8")
    print(f"{changed_files} file(s), {changed_lines} line(s) "
          f"{'would change' if check else 'rewritten'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
