"""Package the Redox Reactions short notes: export PNGs, thumbnails, ZIP, and index.html."""
from __future__ import annotations

import glob
import json
import os
import zipfile

import fitz
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

def make_pngs():
    pdf_path = os.path.join(ROOT, "pdf", "redox-complete.pdf")
    out_dir = os.path.join(ROOT, "png")
    os.makedirs(out_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    print(f"Exporting {len(doc)} pages to 2480x3508 PNG at 300 DPI...")
    zoom = 300.0 / 72.0
    mat = fitz.Matrix(zoom, zoom)
    for i, page in enumerate(doc):
        pix = page.get_pixmap(matrix=mat, alpha=False)
        fn = f"RD_p{i+1:02d}.png"
        target = os.path.join(out_dir, fn)
        pix.save(target)
        with Image.open(target) as im:
            if im.size != (2480, 3508):
                im = im.resize((2480, 3508), Image.Resampling.LANCZOS)
                im.save(target, dpi=(300, 300), optimize=True)
    doc.close()
    print("PNG export complete.")

def make_thumbs():
    out_dir = os.path.join(ROOT, "thumbs")
    os.makedirs(out_dir, exist_ok=True)
    pngs = sorted(glob.glob(os.path.join(ROOT, "png", "*.png")))
    print(f"Generating {len(pngs)} thumbnails...")
    for p in pngs:
        stem = os.path.splitext(os.path.basename(p))[0]
        thumb_path = os.path.join(out_dir, f"{stem}.jpg")
        with Image.open(p) as img:
            img.thumbnail((620, 877), Image.Resampling.LANCZOS)
            img.convert("RGB").save(thumb_path, "JPEG", quality=82, optimize=True)
    print("Thumbnails complete.")

def make_zips():
    d_dir = os.path.join(ROOT, "downloads")
    os.makedirs(d_dir, exist_ok=True)
    zip_path = os.path.join(d_dir, "redox-complete-png.zip")
    print("Creating ZIP archive...")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in sorted(glob.glob(os.path.join(ROOT, "png", "*.png"))):
            zf.write(p, arcname=os.path.join("png", os.path.basename(p)))
        pdf = os.path.join(ROOT, "pdf", "redox-complete.pdf")
        if os.path.exists(pdf):
            zf.write(pdf, arcname="redox-complete.pdf")
    print(f"ZIP created: {os.path.getsize(zip_path)/1024/1024:.2f} MB")

def make_index():
    pngs = sorted(glob.glob(os.path.join(ROOT, "png", "*.png")))
    pdf_path = os.path.join(ROOT, "pdf", "redox-complete.pdf")
    doc = fitz.open(pdf_path)
    toc = doc.get_toc()
    titles = {item[2]: item[1] for item in toc}
    doc.close()

    cards = []
    for i, p in enumerate(pngs, 1):
        fn = os.path.basename(p)
        stem = os.path.splitext(fn)[0]
        thumb = f"thumbs/{stem}.jpg"
        title = titles.get(i, f"Page {i}")
        cards.append(f"""
        <div class="card">
            <a href="png/{fn}" target="_blank">
                <img src="{thumb}" alt="{title}" loading="lazy">
            </a>
            <div class="meta">
                <span class="num">Page {i:02d}</span>
                <span class="title">{title}</span>
                <a class="dl" href="png/{fn}" download>PNG 300DPI</a>
            </div>
        </div>
        """)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Redox Reactions & Equivalent Concept — Complete Explanatory Short Notes</title>
<style>
:root {{ --ink: #0f2b48; --teal: #00796b; --bg: #f8fafc; --card-bg: #ffffff; --border: #e2e8f0; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: var(--bg); color: var(--ink); margin: 0; padding: 24px; }}
header {{ max-width: 1200px; margin: 0 auto 32px; }}
h1 {{ font-size: 28px; margin: 0 0 8px; color: var(--ink); }}
.sub {{ font-size: 16px; color: #475569; margin: 0 0 16px; }}
.btn-bar {{ display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 24px; }}
.btn {{ display: inline-flex; align-items: center; padding: 10px 18px; border-radius: 6px; font-weight: 600; font-size: 14px; text-decoration: none; }}
.btn-primary {{ background: var(--teal); color: #fff; }}
.btn-secondary {{ background: #fff; color: var(--ink); border: 1px solid var(--border); }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 20px; max-width: 1400px; margin: 0 auto; }}
.card {{ background: var(--card-bg); border: 1px solid var(--border); border-radius: 8px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.05); transition: transform 0.15s ease; }}
.card:hover {{ transform: translateY(-2px); box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }}
.card img {{ width: 100%; aspect-ratio: 1 / 1.414; object-fit: cover; display: block; background: #f1f5f9; }}
.meta {{ padding: 12px; display: flex; flex-direction: column; gap: 6px; }}
.num {{ font-size: 12px; font-weight: 700; color: var(--teal); text-transform: uppercase; }}
.title {{ font-size: 13px; font-weight: 600; color: var(--ink); line-height: 1.35; }}
.dl {{ font-size: 11px; color: #64748b; text-decoration: none; margin-top: 4px; }}
.dl:hover {{ color: var(--teal); text-decoration: underline; }}
</style>
</head>
<body>
<header>
    <h1>Redox Reactions & Equivalent Concept — Complete Explanatory Short Notes</h1>
    <p class="sub">Oxidation States, Balancing, n-Factor Matrix, Equivalents, Titrations & Electrochemical Series · 19 Sheets (19 Pages)</p>
    <div class="btn-bar">
        <a class="btn btn-primary" href="pdf/redox-complete.pdf" target="_blank">Download Full PDF (19 Pages, Bookmarked)</a>
        <a class="btn btn-secondary" href="downloads/redox-complete-png.zip" download>Download High-Res PNG Archive (ZIP)</a>
        <a class="btn btn-secondary" href="README.md" target="_blank">Documentation & Syllabi</a>
        <a class="btn btn-secondary" href="PRINTING.txt" target="_blank">Printing Instructions (A4)</a>
    </div>
</header>
<main class="grid">
{''.join(cards)}
</main>
</body>
</html>
"""
    out_html = os.path.join(ROOT, "index.html")
    with open(out_html, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"index.html generated with {len(cards)} cards.")

if __name__ == "__main__":
    make_pngs()
    make_thumbs()
    make_zips()
    make_index()
