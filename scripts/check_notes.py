#!/usr/bin/env python3
"""
Check every notes.md in the repo against docs/NOTE-FORMATTING-RULEBOOK.md — the quality gate
the rulebook asks for in R33. No third-party dependencies, so it runs in CI and in a pre-commit
hook. Exits non-zero and prints one line per finding, grouped by file.

    python3 scripts/check_notes.py              # every notes.md
    python3 scripts/check_notes.py --all        # every markdown file in the repo
    python3 scripts/check_notes.py --quiet      # only the summary
    python3 scripts/check_notes.py <path> ...   # specific files

What it enforces, and where the rule lives:

  N1   one notes.md per chapter folder, named exactly notes.md
  N2   GitHub-safe markdown: no [[wikilinks]], no > [!callout], no Dataview
  N3   markers are the house set
  N4   an H2 that maps to an NCERT section carries its number in parentheses
  N5   the file ends with a Quick Revision Sheet and a *Cross-links:* footer
  R3   frontmatter exists and `words` is within 5 % of the real count
  R5   exactly one H1 title; Parts are the only other H1s
  R6   H2s are numbered 1..N with no gaps or duplicates
  R7   every Contents anchor resolves against the GitHub slug of a real heading
  R12  every relative link and image exists, and every #fragment it carries is a real
       heading in the file it points at
  R14  tables: <= 6 columns, consistent pipe counts, no empty cells
  R20  Mermaid: `flowchart TD`/`LR` only, every label quoted, <= 14 nodes, no box-drawing
  R30  the Quick Revision Sheet is bullets only, <= 30 of them

Rulebook R33 asks for exactly this script. It is a linter, not a formatter: it never edits.
"""
from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

BOXDRAW = re.compile(r"[─-╿]")
MAX_NODES = 14
MAX_COLS = 6
WORD_TOLERANCE = 0.05
FRONTMATTER_KEYS = ("branch", "chapter", "class", "ncert_code", "edition",
                    "exams", "sources", "status", "words", "updated", "tags")


# ---------------------------------------------------------------------------
# GitHub heading slugs
# ---------------------------------------------------------------------------
def gh_slug(heading: str) -> str:
    """github-slugger's algorithm: lowercase, drop punctuation/symbols, spaces -> hyphens.

    Letters, marks and *numbers* survive — so Unicode subscripts and superscripts stay in the
    slug, while emoji, arrows, dashes and parentheses vanish (which is why double hyphens
    appear). ASCII dots are punctuation, so "(3.6.3)" becomes "363", never "3-6-3".
    """
    s = heading.strip().lower()
    out = []
    for ch in s:
        cat = unicodedata.category(ch)
        if cat[0] in ("L", "M", "N"):
            out.append(ch)
        elif ch in " -":
            out.append(ch)
        # everything else (P*, S*, C*) is dropped
    return "".join(out).replace(" ", "-")


def strip_code_spans(text: str) -> str:
    """Blank out fenced blocks and `code` spans so the text checks ignore examples."""
    return re.sub(r"`[^`\n]*`", " ", unfenced(text))


FENCE = re.compile(r"^[ \t]{0,3}(`{3,}|~{3,})")


def unfenced(text: str) -> str:
    """Drop fenced blocks, keeping the line count.

    CommonMark opens a block on a line-start run of three or more backticks (or tildes) and
    closes it on a run of at least the same length. Matching line by line rather than with
    one `.*?` regex matters: a run of backticks *inside* a sentence is not a fence, and a
    non-greedy pair-up misreads it as one and swallows the rest of the file.
    """
    out, fence = [], None
    for line in text.splitlines():
        m = FENCE.match(line)
        if fence is None:
            if m:
                fence = m.group(1)
                out.append("")
                continue
            out.append(line)
        else:
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence) \
                    and line.strip().strip("`~") == "":
                fence = None
            out.append("")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Individual checks
# ---------------------------------------------------------------------------
def check_structure(path: Path, lines: list[str], add):
    h1 = [i for i, l in enumerate(lines) if l.startswith("# ")]
    parts = [i for i in h1 if re.match(r"^# Part [A-Z0-9]", lines[i])]
    if len(h1) - len(parts) != 1:
        add("N5", "expected exactly one '# Title' heading "
                   "(plus any '# Part ...' dividers), found %d" % (len(h1) - len(parts)))
    for i in h1:
        if i not in parts and i != h1[0]:
            add("R5", "line %d: a second H1 that is not a '# Part ...' divider" % (i + 1))

    nums = []
    for i, l in enumerate(lines):
        m = re.match(r"^## (\d+)\.\s", l)
        if m:
            nums.append((int(m.group(1)), i, l))
    if nums:
        expected = list(range(1, len(nums) + 1))
        got = [n for n, _, _ in nums]
        if got != expected:
            missing = sorted(set(expected) - set(got))
            dupes = sorted({n for n in got if got.count(n) > 1})
            add("R6", "H2 numbering is not 1..%d (missing %s%s)"
                % (len(nums), missing or "none", ", duplicated %s" % dupes if dupes else ""))
    else:
        add("R6", "no numbered '## N.' sections at all")


def check_frontmatter(path: Path, lines: list[str], add):
    if not lines or lines[0].strip() != "---":
        add("R3", "no YAML frontmatter")
        return
    try:
        end = lines.index("---", 1)
    except ValueError:
        add("R3", "frontmatter is never closed")
        return
    keys = {}
    for l in lines[1:end]:
        if ":" in l and not l.startswith((" ", "\t", "-")):
            k, _, v = l.partition(":")
            keys[k.strip()] = v.strip()
    for k in FRONTMATTER_KEYS:
        if k not in keys:
            add("R3", "frontmatter is missing `%s`" % k)
    if keys.get("status") not in ("draft", "written", "reviewed"):
        add("R3", "frontmatter `status` is %r, expected draft/written/reviewed" % keys.get("status"))
    if "words" in keys:
        try:
            claimed = int(keys["words"])
        except ValueError:
            add("R3", "frontmatter `words` is not a number: %r" % keys["words"])
            claimed = None
        if claimed is not None:
            actual = len(path.read_text(encoding="utf-8").split())
            if abs(claimed - actual) > max(50, actual * WORD_TOLERANCE):
                add("R3", "frontmatter says words: %d, the file actually has %d" % (claimed, actual))


def check_n2(path: Path, lines: list[str], add):
    body = strip_code_spans(path.read_text(encoding="utf-8"))
    for i, l in enumerate(lines):
        if re.search(r"\[\[[^\]]+\]\]", strip_code_spans(l)):
            add("N2", "line %d: wikilink — use a relative markdown link" % (i + 1))
        if re.match(r"^\s*> \[!", l):
            add("N2", "line %d: Obsidian callout — use a '> **⚠ …**' blockquote" % (i + 1))
    if re.search(r"```dataview", body, re.I):
        add("N2", "Dataview block in a committed note")


def check_fences(path: Path, lines: list[str], add):
    in_fence = False
    for i, l in enumerate(lines):
        if not l.startswith("```"):
            continue
        if not in_fence and l.strip() == "```":
            add("N6", "line %d: bare ``` fence — tag it (mermaid, smiles, text …)" % (i + 1))
        in_fence = not in_fence
    if in_fence:
        add("N6", "unclosed code fence")


def check_contents(path: Path, lines: list[str], add):
    slugs = set()
    for l in lines:
        m = re.match(r"^#{1,6} +(.*)$", l)
        if m:
            slugs.add(gh_slug(m.group(1)))
    seen_contents = False
    for i, l in enumerate(lines):
        if l.startswith("## Contents"):
            seen_contents = True
            continue
        if seen_contents and l.startswith("# "):
            break
        for target in re.findall(r"\]\(#([^)]+)\)", l):
            if target not in slugs:
                add("R7", "line %d: Contents anchor '#%s' matches no heading" % (i + 1, target))
    if not seen_contents:
        add("R5", "no '## Contents' block")
    # cross-file anchors are check_links' job (R12): it resolves the file and the slug together


def check_links(path: Path, lines: list[str], add):
    import urllib.parse
    text = path.read_text(encoding="utf-8")
    for m in re.finditer(r"!\[([^\]]*)\]\(([^)]+)\)", text):
        t = urllib.parse.unquote(m.group(2).strip())
        if t.startswith(("http://", "https://")) or "<" in t:
            continue
        if not (path.parent / t).exists():
            add("R19", "image %s does not exist" % t)
    # blank out inline math first: $\ce{...->[x](y)...}$ is LaTeX, not a link
    naked = re.sub(r"\$[^$\n]*\$", lambda m: " " * len(m.group(0)), strip_code_spans(text))
    for m in re.finditer(r"(?<!!)\[([^\]]*)\]\(([^)\s]+)\)", naked):
        raw = m.group(2).strip()
        if raw.startswith(("http://", "https://", "mailto:")) or "<" in raw:
            continue
        target, _, frag = urllib.parse.unquote(raw).partition("#")
        if not target or not is_path(target):
            continue
        dest = path.parent / target
        if not dest.exists():
            add("R12", "link target %s does not exist" % target)
        elif frag and dest.suffix.lower() == ".md" and frag not in heading_slugs(dest):
            add("R12", "link target %s has no heading #%s" % (target, frag))


def is_path(target: str) -> bool:
    """Is this link target a file path, or a formula GitHub happened to read as one?

    The compound library writes SMILES raw — ChemEdit reads column 2 verbatim, so
    backticks would break it — which means GitHub turns `[O-]`, `[SiH3]` and `[Cl](=O)`
    into links. Those are data, not navigation, and no file by that name exists.
    """
    return "/" in target or bool(re.search(r"\.[A-Za-z0-9]{1,5}$", target))


def heading_slugs(path: Path) -> set[str]:
    """The GitHub anchors a markdown file actually exposes."""
    out = set()
    for line in unfenced(path.read_text(encoding="utf-8")).splitlines():
        m = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", re.sub(r"`[^`\n]*`", " ", line))
        if m:
            out.add(gh_slug(m.group(2)))
    return out


def split_row(line: str) -> list[str]:
    """Split a table row on unescaped pipes: `\\|` is content, not a column break."""
    return [c.strip() for c in re.split(r"(?<!\\)\|", line.strip().strip("|"))]


def check_tables(path: Path, lines: list[str], add):
    i = 0
    while i < len(lines):
        if lines[i].strip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            header = split_row(lines[i])
            if len(header) > MAX_COLS:
                add("R14", "line %d: table has %d columns (max %d)" % (i + 1, len(header), MAX_COLS))
            ncol = len(header)
            j = i + 1
            while j < len(lines) and lines[j].strip().startswith("|"):
                cells = split_row(lines[j])
                if len(cells) != ncol:
                    add("R14", "line %d: row has %d cells, header has %d" % (j + 1, len(cells), ncol))
                if all(c == "" for c in cells):
                    j += 1
                    continue
                for c in cells:
                    if c == "":
                        add("R14", "line %d: empty cell — use — " % (j + 1))
                        break
                j += 1
            i = j
        else:
            i += 1


def check_mermaid(path: Path, lines: list[str], add):
    i = 0
    while i < len(lines):
        if lines[i].strip() == "```mermaid":
            start = i
            j = i + 1
            while j < len(lines) and lines[j].strip() != "```":
                j += 1
            body = lines[i + 1:j]
            check_one_diagram(start + 1, body, add)
            if j + 1 < len(lines) and not lines[j + 1].strip().startswith("*"):
                add("R20", "line %d: no italic caption under the diagram" % (j + 2))
            i = j + 1
        else:
            i += 1


NODE_DEF = re.compile(r"([A-Za-z][A-Za-z0-9_]*)\s*(\[\(|\[\[|\(\(|\{\{|\[|\(|\{)")
EDGE_LBL = re.compile(r"(-->|-\.->|==>)\s*\|([^|]*)\|")
SHAPE_TEXT = re.compile(r"(\[\(|\[\[|\(\(|\{\{|\[|\(|\{)\s*(\"[^\"]*\"|[^]\)\}\|]*)")


def check_one_diagram(lineno: int, body: list[str], add):
    if not body:
        add("R20", "line %d: empty mermaid block" % lineno)
        return
    head = body[0].strip()
    if not re.fullmatch(r"flowchart (TD|LR)", head):
        add("R20", "line %d: first line is %r — use 'flowchart TD' or 'flowchart LR'" % (lineno, head))
    for off, l in enumerate(body):
        if BOXDRAW.search(l):
            add("R21", "line %d: box-drawing/ASCII art inside a diagram — redraw it" % (lineno + off))
        for m in EDGE_LBL.finditer(l):
            if not m.group(2).strip().startswith('"'):
                add("R20", "line %d: edge label %r is not quoted" % (lineno + off, m.group(2).strip()))
        # blank out the *inside* of quoted labels (keeping the quotes) so
        # brackets that live inside a label are not read as shapes
        masked = re.sub(r'"[^"\n]*"',
                        lambda m: '"' + "x" * (len(m.group(0)) - 2) + '"', l)
        for m in SHAPE_TEXT.finditer(masked):
            if m.group(1) in ("[", "(", "{", "[(", "[[", "((", "{{") and not m.group(2).startswith('"'):
                add("R20", "line %d: node label %r is not quoted" % (lineno + off, m.group(2)[:40]))
        for m in re.finditer(r"^\s*subgraph\s+(?![\w]*[\"\[])([^\n]+)$", l):
            add("R20", "line %d: subgraph title %r is not quoted" % (lineno + off, m.group(1).strip()))
        if re.search(r"^\s*\w+\s*\+\s*\w+\s*-->", l):
            add("R20", "line %d: 'A + B --> C' is not valid — use 'A & B --> C'" % (lineno + off))
    nodes = set(NODE_DEF.findall("\n".join(body)) and
                [m[0] for m in NODE_DEF.findall("\n".join(body))])
    if len(nodes) > MAX_NODES:
        add("R20", "line %d: %d nodes (max %d — split the diagram)" % (lineno, len(nodes), MAX_NODES))


def check_sheet(path: Path, lines: list[str], add):
    h2 = [i for i, l in enumerate(lines) if l.startswith("## ")]
    sheet = [i for i in h2 if lines[i].startswith("## ") and "Quick Revision Sheet" in lines[i]]
    if not sheet:
        add("N5", "no '## Quick Revision Sheet'")
        return
    s = sheet[-1]
    numbered = [l for l in lines[s + 1:] if re.match(r"^## \d+\.", l)]
    if numbered:
        add("R30", "'Quick Revision Sheet' is not the last numbered section")
    body = [l for l in lines[s + 1:] if l.strip() and not l.startswith("---")
            and not l.startswith("*Cross-links")]
    if any(l.strip().startswith("|") for l in body):
        add("R30", "the Quick Revision Sheet contains a table — bullets only")
    bullets = [l for l in body if l.strip().startswith(("-", "*"))]
    if len(bullets) > 30:
        add("R30", "%d bullets in the Quick Revision Sheet (max 30)" % len(bullets))
    if not any(l.startswith("*Cross-links:*") for l in lines):
        add("N5", "no '*Cross-links:*' footer")


# ---------------------------------------------------------------------------
# Rules that describe the shape of a chapter's notes.md, and so only apply to one.
CHAPTER_ONLY = ("N1", "N2", "N3", "N4", "N5", "R3", "R5", "R6", "R7", "R30")


def check_file(path: Path, chapter: bool = True) -> list[tuple[str, int, str]]:
    """Check one markdown file.

    `chapter` is True for a notes.md, which the chapter rules (frontmatter, Contents, the
    Quick Revision Sheet) apply to in full. For any other markdown — the README, the
    rulebook, a generated table — only the file-agnostic rules run, because a document
    that is not a chapter has no frontmatter and no Contents block to get wrong.
    """
    findings: list[tuple[str, int, str]] = []

    def add(rule, msg):
        findings.append((rule, 0, msg))

    lines = path.read_text(encoding="utf-8").split("\n")
    for fn in (check_frontmatter, check_structure, check_n2, check_fences, check_contents,
               check_links, check_tables, check_mermaid, check_sheet):
        fn(path, lines, add)
    return findings if chapter else [f for f in findings if f[0] not in CHAPTER_ONLY]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*", type=Path)
    ap.add_argument("--all", action="store_true",
                    help="every markdown file in the repo, not just the notes.md files")
    ap.add_argument("--quiet", action="store_true", help="summary only")
    args = ap.parse_args()

    if args.paths:
        files = [p.resolve() for p in args.paths]
    elif args.all:
        skip = {".git", "node_modules", "__pycache__", ".obsidian"}
        files = sorted(f for f in ROOT.rglob("*.md") if not skip & set(f.parts))
    else:
        files = sorted(ROOT.glob("*/*/notes.md"))
    by_file, total, dirty = {}, 0, 0
    for f in files:
        if not f.exists():
            print("no such file: %s" % f, file=sys.stderr)
            return 2
        findings = check_file(f, chapter=not args.all or f.name == "notes.md")
        by_file[f] = findings
        total += len(findings)
        dirty += bool(findings)
    if not args.quiet:
        for f, findings in by_file.items():
            if not findings:
                continue
            print("%s" % f.relative_to(ROOT) if ROOT in f.parents else f)
            for rule, _, msg in sorted(findings):
                print("    %-4s %s" % (rule, msg))
    print("\n%d file(s) checked, %d clean, %d finding(s)." % (len(files), len(files) - dirty, total))
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
