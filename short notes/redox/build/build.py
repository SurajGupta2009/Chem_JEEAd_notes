"""Build the complete Redox Reactions & Equivalent Concept short notes PDF (18 sheets = 18 pages)."""
from __future__ import annotations

import importlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "content"))

import pagelib

CONTENT_MODULES = [
    "part1",
    "part2",
    "part3",
]

def load_all_sheets():
    sheets = []
    for mod_name in CONTENT_MODULES:
        mod = importlib.import_module(mod_name)
        sheets.extend(dict(sh, blocks=list(sh["blocks"])) for sh in mod.SHEETS)
    return sheets

def main():
    sheets = load_all_sheets()
    print(f"Loaded {len(sheets)} sheets.")

    pdf_out = os.path.join(ROOT, "pdf", "redox-complete.pdf")
    os.makedirs(os.path.join(ROOT, "pdf"), exist_ok=True)

    part_label = "Redox Reactions & Equivalent Concept"
    part_short = "Redox Reactions · JEE Main + Advanced"
    running = "Redox Reactions"
    meta_title = "Redox Reactions & Equivalent Concept — Complete Explanatory Short Notes"

    n, info = pagelib.build_pdf(
        sheets,
        pdf_out,
        part_label,
        part_short,
        running,
        meta_title
    )
    print(f"Successfully built {len(sheets)} sheets, {n} pages -> {pdf_out}")

if __name__ == "__main__":
    main()
