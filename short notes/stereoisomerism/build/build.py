"""Build the Stereoisomerism chapter PDFs from content/*.py.

    python3 build/build.py                 # both parts
    python3 build/build.py --part JEE      # Part I only
    python3 build/build.py --pages 20-30   # only sheets in that page range
"""
from __future__ import annotations

import argparse
import importlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, ROOT)

import pagelib  # noqa: E402

PARTS = [
    ("JEE", "Part I", "jee", "jee_", "J"),
    ("EXT", "Part II", "extensions", "ext_", "X"),
]

LABELS = {
    "JEE": ("Part I \u00b7 JEE Main + Advanced core", "JEE Main + Advanced"),
    "EXT": ("Part II \u00b7 JEE Advanced extensions", "JEE Advanced extensions"),
}


def load_sheets(prefix):
    sheets = []
    for i in range(1, 10):
        mod = f"content.{prefix}{i}"
        try:
            m = importlib.import_module(mod)
        except ModuleNotFoundError:
            break
        # copy: renumber() below rewrites ids and appends EXTRA blocks, and
        # this function is called more than once per process (verify, package)
        sheets.extend(dict(sh, blocks=list(sh["blocks"])) for sh in m.SHEETS)
    return sheets


def renumber(sheets, part):
    from content.extra_blocks import EXTRA
    for i, sh in enumerate(sheets, 1):
        old = sh["id"]
        sh["id"] = f"{'J' if part == 'JEE' else 'X'}-{i:02d}"
        extra = EXTRA.get(old) or EXTRA.get(sh["id"])
        if extra:
            sh["blocks"] = list(sh["blocks"]) + list(extra)
    return sheets


def build(part_filter=None, page_range=None):
    for key, label, folder, prefix, letter in PARTS:
        if part_filter and key != part_filter:
            continue
        sheets = renumber(load_sheets(prefix), key)
        if not sheets:
            raise SystemExit(f"no sheets imported for {key} (check content/{prefix}1.py)")
        if page_range:
            lo, hi = page_range
            sheets = [s for s in sheets if lo <= int(s["id"].split("-")[1]) <= hi]
        if not sheets:
            raise SystemExit("page range selected no sheets")
        part_label, running = LABELS[key]
        out = os.path.join(ROOT, "pdf",
                           "stereoisomerism-jee.pdf" if key == "JEE"
                           else "stereoisomerism-extensions.pdf")
        n, info = pagelib.build_pdf(sheets, out, part_label, part_label, running,
                                    f"Stereoisomerism \u2014 {label}")
        print(f"{key}: {len(sheets)} sheets, {n} pages -> {out}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--part", choices=["JEE", "EXT"])
    ap.add_argument("--pages", help="LO-HI sheet number range")
    a = ap.parse_args()
    rng = None
    if a.pages:
        lo, hi = a.pages.split("-")
        rng = (int(lo), int(hi))
    build(a.part, rng)


if __name__ == "__main__":
    main()
