"""Verification suite for the Surface Chemistry short notes."""
from __future__ import annotations

import glob
import os
import sys
import zipfile

import fitz
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

def run_checks():
    errors = []
    passes = 0

    def check(cond, msg):
        nonlocal passes
        if cond:
            passes += 1
            print(f"  [PASS] {msg}")
        else:
            errors.append(msg)
            print(f"  [FAIL] {msg}")

    print("--- 1. Checking Key Deliverables Existence ---")
    check(os.path.exists(os.path.join(ROOT, "pdf", "surface-chemistry-complete.pdf")), "surface-chemistry-complete.pdf exists")
    check(os.path.exists(os.path.join(ROOT, "downloads", "surface-chemistry-complete-png.zip")), "surface-chemistry-complete-png.zip exists")
    check(os.path.exists(os.path.join(ROOT, "index.html")), "index.html gallery exists")

    print("\n--- 2. Checking PDF Page Count and Bookmarks ---")
    pdf_path = os.path.join(ROOT, "pdf", "surface-chemistry-complete.pdf")
    doc = fitz.open(pdf_path)
    check(len(doc) == 18, f"PDF has exactly 18 pages (found {len(doc)})")
    toc = doc.get_toc()
    check(len(toc) == 18, f"PDF has exactly 18 bookmarks (found {len(toc)})")

    # Verify A4 geometry (595.28 x 841.89 pt)
    page1 = doc[0]
    rect = page1.rect
    check(abs(rect.width - 595.28) < 1.0 and abs(rect.height - 841.89) < 1.0, f"PDF page is A4 portrait: {rect.width:.1f} x {rect.height:.1f} pt")
    doc.close()

    print("\n--- 3. Checking PNG Sheets (Dimensions & Count) ---")
    pngs = sorted(glob.glob(os.path.join(ROOT, "png", "*.png")))
    check(len(pngs) == 18, f"Exactly 18 PNG sheets generated (found {len(pngs)})")
    if pngs:
        with Image.open(pngs[0]) as im:
            check(im.size == (2480, 3508), f"PNG dimensions are exactly 2480x3508 px (found {im.size})")

    print("\n--- 4. Checking Thumbnails ---")
    thumbs = sorted(glob.glob(os.path.join(ROOT, "thumbs", "*.jpg")))
    check(len(thumbs) == 18, f"Exactly 18 thumbnails generated (found {len(thumbs)})")

    print("\n--- 5. Checking ZIP Archive Integrity ---")
    zip_path = os.path.join(ROOT, "downloads", "surface-chemistry-complete-png.zip")
    with zipfile.ZipFile(zip_path, "r") as zf:
        namelist = zf.namelist()
        check("surface-chemistry-complete.pdf" in namelist, "ZIP includes surface-chemistry-complete.pdf")
        png_entries = [n for n in namelist if n.endswith(".png")]
        check(len(png_entries) == 18, f"ZIP includes all 18 PNGs (found {len(png_entries)})")
        test_res = zf.testzip()
        check(test_res is None, "ZIP archive passes CRC integrity check")

    print(f"\nSummary: {passes} checks passed, {len(errors)} failed.")
    if errors:
        sys.exit(1)

if __name__ == "__main__":
    run_checks()
