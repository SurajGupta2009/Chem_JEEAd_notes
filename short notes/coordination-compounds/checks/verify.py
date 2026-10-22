"""Verification script for Coordination Compounds short notes."""
import os
import glob
import fitz
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def check_pdf():
    pdf = os.path.join(ROOT, "pdf", "coordination-compounds-complete.pdf")
    assert os.path.exists(pdf), f"PDF missing: {pdf}"
    doc = fitz.open(pdf)
    assert len(doc) == 18, f"Expected 18 pages, got {len(doc)}"
    toc = doc.get_toc()
    assert len(toc) == 18, f"Expected 18 bookmarks, got {len(toc)}"
    print(f"[OK] PDF valid: 18 pages, 18 bookmarks, size {os.path.getsize(pdf)/1024:.1f} KB")

def check_pngs():
    pngs = sorted(glob.glob(os.path.join(ROOT, "png", "*.png")))
    assert len(pngs) == 18, f"Expected 18 PNGs, got {len(pngs)}"
    for p in pngs:
        with Image.open(p) as im:
            assert im.size == (2480, 3508), f"Wrong size {im.size} for {p}"
    print(f"[OK] PNGs valid: 18 files, all 2480x3508 at 300 DPI")

def check_thumbs():
    thumbs = sorted(glob.glob(os.path.join(ROOT, "thumbs", "*.jpg")))
    assert len(thumbs) == 18, f"Expected 18 thumbnails, got {len(thumbs)}"
    for t in thumbs:
        with Image.open(t) as im:
            assert im.size[0] <= 620 and im.size[1] <= 877
    print(f"[OK] Thumbnails valid: 18 files")

def check_downloads():
    zip_path = os.path.join(ROOT, "downloads", "coordination-compounds-complete-png.zip")
    assert os.path.exists(zip_path), f"ZIP missing: {zip_path}"
    assert os.path.getsize(zip_path) > 10 * 1024 * 1024, "ZIP too small"
    print(f"[OK] ZIP archive valid: {os.path.getsize(zip_path)/1024/1024:.2f} MB")

def check_index():
    index = os.path.join(ROOT, "index.html")
    assert os.path.exists(index), f"index.html missing: {index}"
    with open(index) as f:
        html = f.read()
    assert "CC_p01.png" in html
    assert "CC_p18.png" in html
    assert html.count('class="card"') == 18
    print("[OK] index.html valid with 18 cards")

if __name__ == "__main__":
    check_pdf()
    check_pngs()
    check_thumbs()
    check_downloads()
    check_index()
    print("\nALL VERIFICATION SUITE CHECKS PASSED SUCCESSFULLY!")
