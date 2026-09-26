#!/usr/bin/env python3
"""Render a chapter's structure table into an SVG grid + an Obsidian `smiles` block.

Implements rungs 4-5 of the structure ladder in docs/NOTE-FORMATTING-RULEBOOK.md (R18/R19):
ONE markdown table is the source of truth, and two artefacts are generated from it:

  1. `<name>.svg`  - a grid drawing (RDKit) that renders on GitHub AND in Obsidian with no
                     plugin; this is what notes.md embeds, so no reader ever hits a hole.
  2. the ```smiles block inside the same .md file, between the markers
         <!-- smiles:begin -->  and  <!-- smiles:end -->
     which the Obsidian "Chem" plugin (id `chem`) renders as live structures.

Source file format (e.g. Physical-Chemistry/05-Redox-Reactions/figures/structures.md):

    | Label | SMILES | Note |
    |---|---|---|
    | H₂SO₅ (Caro's acid) | OOS(=O)(=O)O | S +6 |

`Label` and `Note` are joined into the legend under each drawing. Rows whose SMILES cell is
empty or `—` are skipped. Any other table in the file is ignored (the first table whose
header contains "SMILES" is used).

Usage:
    python scripts/render_structures.py <path/to/structures.md> [--per-row 4] [--size 260]

Requires RDKit (`pip install rdkit`), which is NOT needed by fetch_ncert_pdfs.py and is not
a runtime dependency of the notes themselves - only of regenerating the figures.
"""
import argparse
import re
import sys
from pathlib import Path

BEGIN, END = "<!-- smiles:begin -->", "<!-- smiles:end -->"


def parse_table(md: str):
    rows, header, in_table = [], None, False
    for line in md.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            if in_table and header:
                break
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if header is None:
            if any(c.upper() == "SMILES" for c in cells):
                header, in_table = [c.upper() for c in cells], True
            continue
        if set("".join(cells)) <= set("-: "):
            continue  # delimiter row
        row = dict(zip(header, cells))
        smi = row.get("SMILES", "").strip("` ")
        if smi and smi != "—":
            rows.append((row.get("LABEL", ""), smi, row.get("NOTE", "")))
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", type=Path)
    ap.add_argument("--per-row", type=int, default=4)
    ap.add_argument("--size", type=int, default=240, help="cell size in px")
    args = ap.parse_args()

    try:
        from rdkit import Chem
        from rdkit.Chem import rdDepictor
        from rdkit.Chem.Draw import rdMolDraw2D
    except ImportError as e:
        sys.exit("RDKit drawing unavailable (%s): pip install rdkit" % e)
    rdDepictor.SetPreferCoordGen(True)  # CoordGen: textbook layouts (e.g. the CrO5 butterfly)

    md = args.source.read_text(encoding="utf-8")
    rows = parse_table(md)
    if not rows:
        sys.exit("no table with a SMILES column found in %s" % args.source)

    bad = [(l, s) for l, s, _ in rows if Chem.MolFromSmiles(s) is None]
    if bad:
        sys.exit("unparseable SMILES: %s" % bad)

    # RDKit's built-in legend font has no Unicode glyphs (subscripts, minus, fractions), so
    # each molecule is drawn WITHOUT a legend and the captions are added as real SVG <text>,
    # which every browser (GitHub, Obsidian) renders with full Unicode.
    size, cap = args.size, 46
    per = min(args.per_row, len(rows))
    nrows = -(-len(rows) // per)
    W, H = per * size, nrows * (size + cap)
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">'
             % (W, H, W, H),
             '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, H)]
    for i, (label, smi, note) in enumerate(rows):
        m = Chem.MolFromSmiles(smi)
        rdDepictor.Compute2DCoords(m)
        d = rdMolDraw2D.MolDraw2DSVG(size, size)
        o = d.drawOptions()
        o.bondLineWidth, o.padding, o.clearBackground = 2, 0.15, False
        d.DrawMolecule(m)
        d.FinishDrawing()
        body = re.sub(r"<\?xml[^>]*>\s*", "", d.GetDrawingText())
        body = re.sub(r"<rect[^>]*/>", "", body, count=1)  # drop per-cell background
        x, y = (i % per) * size, (i // per) * (size + cap)
        parts.append('<g transform="translate(%d,%d)">%s</g>' % (x, y, body))
        esc = lambda s: s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        cx = x + size / 2
        parts.append('<text x="%.1f" y="%d" font-family="Helvetica,Arial,sans-serif" font-size="15" '
                     'font-weight="bold" text-anchor="middle" fill="#111">%s</text>'
                     % (cx, y + size + 14, esc(label)))
        if note:
            parts.append('<text x="%.1f" y="%d" font-family="Helvetica,Arial,sans-serif" font-size="14" '
                         'text-anchor="middle" fill="#333">%s</text>' % (cx, y + size + 34, esc(note)))
    parts.append("</svg>")
    svg = "\n".join(parts)
    out_svg = args.source.with_suffix(".svg")
    out_svg.write_text(svg, encoding="utf-8")

    block = "%s\n```smiles\n%s\n```\n%s" % (BEGIN, "\n".join(s for _, s, _ in rows), END)
    if BEGIN in md and END in md:
        md = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), lambda _: block, md, flags=re.S)
    else:
        md = md.rstrip("\n") + "\n\n" + block + "\n"
    args.source.write_text(md, encoding="utf-8")
    print("wrote %s (%d structures) and refreshed the smiles block in %s"
          % (out_svg, len(rows), args.source))


if __name__ == "__main__":
    main()
