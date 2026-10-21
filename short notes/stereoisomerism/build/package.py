"""Package the chapter: PNG sheets, thumbnails, ZIPs, bookmarked PDFs, index.html.

Run after ``build/build.py`` (or pass ``--build``):

    python3 build/package.py            # everything
    python3 build/package.py --no-zip   # pages + gallery only

The page -> sheet mapping is computed once here (from the same content modules
the PDF was built from) and reused by the filenames, the ZIPs, the PDF bookmarks
and index.html, so the four never disagree.
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
import zipfile

import pymupdf
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, ROOT)

import build as B          # noqa: E402
import pagelib             # noqa: E402

PARTS = [
    ("JEE", "Part I", "jee", "jee_", "J"),
    ("EXT", "Part II", "extensions", "ext_", "X"),
]
THUMB_W = 620
PDFS = {"JEE": "pdf/stereoisomerism-jee.pdf", "EXT": "pdf/stereoisomerism-extensions.pdf"}


def sheet_ranges(part_key, prefix):
    """[(sheet_id, title, first_page_index, n_pages)]"""
    sheets = B.renumber(B.load_sheets(prefix), part_key)
    out, page = [], 0
    for sh in sheets:
        pages, _ = pagelib.build_sheet(sh, 1, len(sheets), "x", "x", "x")
        out.append((sh["id"], sh["title"], page, len(pages)))
        page += len(pages)
    return out


def export_pngs(part_key, folder, prefix, pdf):
    ranges = sheet_ranges(part_key, prefix)
    expected = sum(r[3] for r in ranges)
    outdir = os.path.join(ROOT, folder)
    os.makedirs(outdir, exist_ok=True)
    for fn in os.listdir(outdir):
        if fn.endswith(".png"):
            os.remove(os.path.join(outdir, fn))
    doc = pymupdf.open(os.path.join(ROOT, pdf))
    if len(doc) != expected:
        raise SystemExit(f"{pdf}: {len(doc)} pages but the planner says {expected}")
    names = []
    for i, page in enumerate(doc):
        sid, title, first, n = next(r for r in ranges if r[2] <= i < r[2] + r[3])
        k = i - first + 1
        tag = "JEE" if part_key == "JEE" else "EXT"
        name = f"{tag}_p{i + 1:02d}_{sid}_{k}of{n}.png"
        path = os.path.join(outdir, name)
        page.get_pixmap(dpi=300, colorspace=pymupdf.csRGB, alpha=False).save(path)
        pagelib._normalise_png(path, 300, 64)
        names.append(name)
    doc.close()
    return ranges, names


def make_thumbs(pairs):
    """pairs = [(folder, name); ...] — one pass, so the second part does not
    delete the first part's thumbnails."""
    out = os.path.join(ROOT, "thumbs")
    os.makedirs(out, exist_ok=True)
    for fn in os.listdir(out):
        if fn.endswith((".png", ".jpg")):
            os.remove(os.path.join(out, fn))
    for folder, n in pairs:
        im = Image.open(os.path.join(ROOT, folder, n)).convert("RGB")
        h = round(im.height * THUMB_W / im.width)
        # JPEG thumbnails: a tenth of the size of PNG, and the gallery only needs a preview
        im.resize((THUMB_W, h), Image.LANCZOS).save(
            os.path.join(out, os.path.splitext(n)[0] + ".jpg"),
            quality=82, optimize=True, progressive=True, dpi=(72, 72))


def make_zips(all_names):
    dl = os.path.join(ROOT, "downloads")
    os.makedirs(dl, exist_ok=True)
    jee = [n for f, n in all_names if f == "jee"]
    ext = [n for f, n in all_names if f == "extensions"]
    for fname, folder, names in (
        ("stereoisomerism-part1-jee-png.zip", "jee", jee),
        ("stereoisomerism-part2-extensions-png.zip", "extensions", ext),
    ):
        with zipfile.ZipFile(os.path.join(dl, fname), "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
            for n in names:
                z.write(os.path.join(ROOT, folder, n), arcname=f"{folder}/{n}")
    with zipfile.ZipFile(os.path.join(dl, "stereoisomerism-complete-png.zip"),
                         "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for part in ("pdf/stereoisomerism-jee.pdf", "pdf/stereoisomerism-extensions.pdf"):
            z.write(os.path.join(ROOT, part), arcname=part)
        for folder, n in all_names:
            z.write(os.path.join(ROOT, folder, n), arcname=f"{folder}/{n}")


def make_combined_pdf(parts):
    """Part I first, then Part II, one bookmark per sheet."""
    doc = pymupdf.open()
    toc, offset = [], 0
    for label, _folder, pdf, ranges in parts:
        src = pymupdf.open(os.path.join(ROOT, pdf))
        doc.insert_pdf(src)
        src.close()
        toc.append([1, label, offset + 1])
        for sid, title, first, n in ranges:
            toc.append([2, f"{sid} \u2014 {title}", offset + first + 1])
        offset += sum(r[3] for r in ranges)
    doc.set_toc(toc)
    doc.set_metadata({"title": "Stereoisomerism \u2014 short notes (complete)",
                      "author": "Arena short-notes build",
                      "subject": "JEE Main + Advanced stereoisomerism, 41 sheets"})
    out = os.path.join(ROOT, "pdf/stereoisomerism-complete.pdf")
    doc.save(out, deflate=True, garbage=3)
    doc.close()
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--no-zip", action="store_true")
    a = ap.parse_args()
    if a.build:
        subprocess.check_call([sys.executable, "-u", os.path.join(HERE, "build.py")], cwd=ROOT)

    parts, all_names, summary = [], [], []
    for key, label, folder, prefix, _letter in PARTS:
        print(f"[{key}] exporting PNGs ...", flush=True)
        ranges, names = export_pngs(key, folder, prefix, PDFS[key])
        print(f"[{key}] {len(names)} PNGs / {len(ranges)} sheets", flush=True)
        parts.append((label, folder, PDFS[key], ranges))
        all_names.extend((folder, n) for n in names)
        summary.append((label, len(ranges), len(names)))

    make_thumbs([(folder, n) for folder, n in all_names])

    if not a.no_zip:
        print("writing ZIPs ...", flush=True)
        make_zips(all_names)

    print("merging the combined PDF ...", flush=True)
    make_combined_pdf(parts)

    from make_index import write_index
    n = write_index(parts, summary)
    print(f"index.html written ({n} gallery entries)")


if __name__ == "__main__":
    main()
