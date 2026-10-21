"""Ink coverage and last-used band per page.

    python3 checks/page_report.py pdf/stereoisomerism-jee.pdf
"""
import sys

import pymupdf


def main(path):
    doc = pymupdf.open(path)
    print(f"{path}: {len(doc)} pages")
    for i, page in enumerate(doc, 1):
        pix = page.get_pixmap(dpi=40, colorspace=pymupdf.csGRAY)
        w, h = pix.width, pix.height
        rows = []
        for y in range(h):
            dark = 0
            for x in range(w):
                if pix.pixel(x, y)[0] < 235:
                    dark += 1
            rows.append(dark)
        ink = sum(rows) / (w * h)
        top, bot = int(h * 0.080), int(h * 0.949)
        last = top
        for y in range(top, bot):
            if rows[y] > 3:
                last = y
        band = min(10, int((last - top) / (bot - top) * 10) + 1)
        step = (bot - top) / 10.0
        bars = "".join("#" if sum(rows[int(top + step * b):int(top + step * (b + 1))]) > 0 else "." for b in range(10))
        print(f"  p{i:02d}  ink={ink:.3f}  last_band={band}/10  bands={bars}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "pdf/stereoisomerism-jee.pdf")
