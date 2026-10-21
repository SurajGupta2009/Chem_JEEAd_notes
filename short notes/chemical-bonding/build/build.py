"""Build the complete Chemical Bonding short notes PDF (24 sheets = 24 pages)."""
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

    pdf_out = os.path.join(ROOT, "pdf", "chemical-bonding-complete.pdf")
    os.makedirs(os.path.join(ROOT, "pdf"), exist_ok=True)

    part_label = "Chemical Bonding & Molecular Structure"
    part_short = "Chemical Bonding · JEE Main + Advanced"
    running = "Chemical Bonding"
    meta_title = "Chemical Bonding & Molecular Structure — Complete Explanatory Short Notes"

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
