"""Reproducible checks for the stereoisomerism chapter.

    python3 checks/verify.py            # all checks, exit 1 on failure
    python3 checks/verify.py --quiet

Checks (each prints PASS/FAIL with the numbers it saw):
  1  every promised file exists
  2  the two part PDFs: A4 size, page count == planner page count
  3  combined PDF: page count == sum, bookmark per sheet, Part I first
  4  PNGs: 2480x3508, nominal 300 dpi, count == PDF pages, names parse
  5  thumbs: exist for every PNG
  6  ZIPs: open, contain every PNG at the right path, no extras
  7  index.html: links to every download and every PNG
  8  page furniture: each page carries its part / sheet id / page label
  9  manuals: every table caption unique, section numbers inside 0-6
This is a structural and consistency check. It does not re-verify chemistry;
see SOURCE-AUDIT.md for what was and was not checked by hand.
"""
from __future__ import annotations

import os
import re
import sys
import zipfile

import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "build"))
sys.path.insert(0, ROOT)

import build as B          # noqa: E402
import pagelib             # noqa: E402

FAIL = []
OK = 0


def check(cond, name, detail=""):
    global OK
    if cond:
        OK += 1
        print(f"  PASS  {name}" + (f"  [{detail}]" if detail else ""))
    else:
        FAIL.append(name + (f" [{detail}]" if detail else ""))
        print(f"  FAIL  {name}" + (f"  [{detail}]" if detail else ""))


def part_pdfs():
    return [("JEE", "pdf/stereoisomerism-jee.pdf", "jee_"),
            ("EXT", "pdf/stereoisomerism-extensions.pdf", "ext_")]


def planned(prefix, key):
    sheets = B.renumber(B.load_sheets(prefix), key)
    out, page = [], 0
    for sh in sheets:
        pages, _ = pagelib.build_sheet(sh, 1, len(sheets), "x", "x", "x")
        out.append((sh["id"], sh["title"], page, len(pages)))
        page += len(pages)
    return out


def main():
    quiet = "--quiet" in sys.argv
    print("1. promised files")
    promised = [
        "index.html", "README.md", "SCOPE.md", "SOURCE-AUDIT.md", "PRINTING.txt",
        "source/NS-Sir-Stereoisomerism-Complete-Notes.md",
        "build/build.py", "build/package.py", "build/make_index.py",
        "build/pagelib.py", "build/textkit.py", "build/sketch.py",
        "checks/page_report.py", "checks/verify.py",
        "pdf/stereoisomerism-jee.pdf", "pdf/stereoisomerism-extensions.pdf",
        "pdf/stereoisomerism-complete.pdf",
        "downloads/stereoisomerism-part1-jee-png.zip",
        "downloads/stereoisomerism-part2-extensions-png.zip",
        "downloads/stereoisomerism-complete-png.zip",
    ]
    for p in promised:
        check(os.path.exists(os.path.join(ROOT, p)), p)

    print("2. part PDFs")
    total = 0
    ranges_by_part = {}
    for key, pdf, prefix in part_pdfs():
        ranges = planned(prefix, key)
        ranges_by_part[key] = ranges
        n_planned = sum(r[3] for r in ranges)
        doc = pymupdf.open(os.path.join(ROOT, pdf))
        w, h = doc[0].rect.width, doc[0].rect.height
        check(abs(w - 595.276) < 1 and abs(h - 841.89) < 1, f"{key} A4", f"{w:.1f}x{h:.1f}")
        check(len(doc) == n_planned, f"{key} page count", f"{len(doc)} vs planner {n_planned}")
        check(len(doc.get_toc()) == len(ranges), f"{key} bookmarks", f"{len(doc.get_toc())} vs {len(ranges)} sheets")
        total += n_planned
        doc.close()
        print(f"        {key}: {len(ranges)} sheets, {n_planned} pages")

    print("3. combined PDF")
    doc = pymupdf.open(os.path.join(ROOT, "pdf/stereoisomerism-complete.pdf"))
    check(len(doc) == total, "combined page count", f"{len(doc)} vs {total}")
    toc = doc.get_toc()
    top = [t for t in toc if t[0] == 1]
    check(len(top) == 2, "two top-level parts", str([t[1] for t in top]))
    check(top and top[0][1].startswith("Part I"), "Part I first", top[0][1] if top else "")
    subs = [t for t in toc if t[0] == 2]
    check(len(subs) == sum(len(r) for r in ranges_by_part.values()), "one bookmark per sheet", str(len(subs)))
    check(all(re.search(r"^\w{1,2}-\d\d \u2014 ", t[1]) for t in subs), "bookmark titles have id")
    doc.close()

    print("4. PNGs")
    png_names = {}
    for key, pdf, prefix in part_pdfs():
        folder = "jee" if key == "JEE" else "extensions"
        files = sorted(f for f in os.listdir(os.path.join(ROOT, folder)) if f.endswith(".png"))
        n_pages = sum(r[3] for r in ranges_by_part[key])
        check(len(files) == n_pages, f"{key} PNG count", f"{len(files)} vs {n_pages}")
        from PIL import Image
        bad = []
        for f in files:
            im = Image.open(os.path.join(ROOT, folder, f))
            dpi = im.info.get("dpi") or (0, 0)
            if im.size != (2480, 3508) or abs(dpi[0] - 300) > 0.01:
                bad.append((f, im.size, im.info.get("dpi")))
        check(not bad, f"{key} 2480x3508 @300dpi", f"{len(files)} files" if not bad else str(bad[:3]))
        pat = re.compile(rf"^{'JEE' if key == 'JEE' else 'EXT'}_p(\d\d)_([JX]-\d\d)_(\d)of(\d)\.png$")
        parsed = [pat.match(f) for f in files]
        check(all(parsed), f"{key} filename scheme")
        order = [int(m.group(1)) for m in parsed if m]
        check(order == sorted(order) and order == list(range(1, len(order) + 1)),
              f"{key} page numbers contiguous")
        png_names[key] = (folder, files)

    print("5. thumbs")
    tdir = os.path.join(ROOT, "thumbs")
    tn = sorted(f for f in os.listdir(tdir) if f.endswith(".jpg")) if os.path.isdir(tdir) else []
    all_pngs = {f for _k, (_f, fs) in png_names.items() for f in fs}
    want_thumbs = {os.path.splitext(f)[0] + ".jpg" for f in all_pngs}
    check(set(tn) == want_thumbs, "one thumb per PNG",
          f"{len(tn)} thumbs / {len(all_pngs)} PNGs")

    print("6. ZIPs")
    for zname, wanted in (
        ("stereoisomerism-part1-jee-png.zip", [("jee", f) for f in png_names["JEE"][1]]),
        ("stereoisomerism-part2-extensions-png.zip", [("extensions", f) for f in png_names["EXT"][1]]),
    ):
        with zipfile.ZipFile(os.path.join(ROOT, "downloads", zname)) as z:
            names = set(z.namelist())
            want = {f"{d}/{f}" for d, f in wanted}
            check(want == names, f"{zname} contents", f"{len(names)} entries")
            check(z.testzip() is None, f"{zname} integrity")
    with zipfile.ZipFile(os.path.join(ROOT, "downloads", "stereoisomerism-complete-png.zip")) as z:
        names = {n for n in z.namelist() if n.endswith(".png")}
        check(len(names) == total, "complete ZIP has all PNGs", f"{len(names)} vs {total}")
        check({"pdf/stereoisomerism-jee.pdf", "pdf/stereoisomerism-extensions.pdf"} <= set(z.namelist()),
              "complete ZIP has both PDFs")

    print("7. index.html")
    html = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    for link in ("downloads/stereoisomerism-complete-png.zip",
                 "downloads/stereoisomerism-part1-jee-png.zip",
                 "downloads/stereoisomerism-part2-extensions-png.zip",
                 "pdf/stereoisomerism-complete.pdf", "pdf/stereoisomerism-jee.pdf",
                 "pdf/stereoisomerism-extensions.pdf", "PRINTING.txt", "SCOPE.md",
                 "SOURCE-AUDIT.md"):
        check(link in html, f"index links {link}")
    missing = [f for f in all_pngs if f not in html]
    check(not missing, "index gallery covers every PNG", f"{len(all_pngs)} imgs" if not missing else str(missing[:3]))

    print("8. page furniture")
    for key, pdf, _p in part_pdfs():
        doc = pymupdf.open(os.path.join(ROOT, pdf))
        bad = []
        for i, page in enumerate(doc):
            txt = page.get_text()
            if "Part" not in txt or not re.search(r"[JX]-\d\d", txt) or "page" not in txt:
                bad.append(i + 1)
        check(not bad, f"{key} furniture on every page", f"{len(doc)} pages" if not bad else str(bad))
        doc.close()

    print("9. manuals")
    from collections import Counter
    for key, _pdf, prefix in part_pdfs():
        caps, secs = [], []
        for sh in B.renumber(B.load_sheets(prefix), key):
            for b in sh["blocks"]:
                if b[0] == "table" and len(b) > 4 and isinstance(b[4], str):
                    m = re.match(r"Table (\d)\.(\d+)[a-z]?", b[4])
                    if m:
                        caps.append((int(m.group(1)), int(m.group(2))))
                if b[0] == "h2":
                    m = re.match(r"(\d)\.(\d+)([a-z]?)", b[1])
                    if m:
                        secs.append((int(m.group(1)), int(m.group(2)), m.group(3)))
        check(not {k: v for k, v in Counter(caps).items() if v > 1},
              f"{key} unique table numbers", f"{len(caps)} tables")
        check(caps == sorted(caps), f"{key} table numbers in reading order", f"{len(caps)} tables")
        check(secs == sorted(secs), f"{key} section numbers in reading order", f"{len(secs)} sections")
        check(all(s[0] <= 6 for s in secs), f"{key} section chapters")
        if not quiet:
            print(f"        {key}: {len(secs)} numbered sections, {len(caps)} tables")

    print()
    print(f"{OK} passed, {len(FAIL)} failed")
    if FAIL:
        for f in FAIL:
            print("   -", f)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
