"""A4 flow layout: blocks -> pages -> PDF -> PNG."""
from __future__ import annotations

import json
import os

import pymupdf

import sketch
from textkit import (BOX, GOLD, GRID, INK, MARK, NAVY, PAPER, RED, REDBOX, TEAL,
                     TEALBOX, Rich, begin_text, draw_text, end_text, font, parse,
                     width)

PAGE_W, PAGE_H = 595.276, 841.89
M = 28.346
BODY_W = PAGE_W - 2 * M
BODY_TOP = 68.0
BODY_BOTTOM = 799.0
FS = 11.15
LEAD = 15.15

# spacing profiles, switched by build_sheet
COMPACT = False
ROOMY = False
TIGHT = False


def sp(normal, compact, roomy):
    if TIGHT:
        # spacing-only emergency: enough to pull one stray block back a page,
        # never a change of font size
        return compact * 0.55 if compact > 4 else compact - 0.9
    if COMPACT:
        return compact
    if ROOMY:
        return roomy
    return normal


# ---------------------------------------------------------------------------
# flows
# ---------------------------------------------------------------------------
class Flow:
    before = 0.0
    after = 0.0
    h = 0.0
    stretch = 0.0        # extra space handed out when a sheet must fill its last page

    def layout(self, w):
        return self.h

    def draw(self, page, x, y):
        raise NotImplementedError


class Gap(Flow):
    def __init__(self, h=5):
        self.base_h = h
        self.h = h

    def layout(self, w):
        self.h = self.base_h + self.stretch
        return self.h


class Rule(Flow):
    def __init__(self):
        self.before = sp(9.0, 6.0, 14.0)
        self.after = sp(9.0, 6.0, 14.0)
        self.h = self.before + self.after

    def layout(self, w):
        self.h = self.before + self.after + self.stretch
        return self.h

    def draw(self, page, x, y):
        page.draw_line((x, y + self.before), (x + BODY_W, y + self.before),
                       color=GOLD, width=0.65, dashes="[2.5 2.5] 0")


class Heading(Flow):
    def __init__(self, text, level=2):
        self.text = text
        self.level = level
        self.size = 17.4 if level == 2 else 14.2
        self.before = sp(13.0, 9.0, 20.0)
        self.after = sp(5.0, 3.4, 8.0)
        self.rich = Rich(text.replace("*", ""), size=self.size,
                         leading=self.size * 1.18, color=TEAL,
                         space_before=0, space_after=0)
        self.h = None

    def layout(self, w):
        self.rich.spans = [s.__class__(s.text, "caveat", 0, None, False)
                           for s in parse(self.text)]
        self.rich.color = TEAL
        self.rich.size = self.size
        self.h = self.before + self.rich.layout(w) + self.after + 3.0 + self.stretch
        return self.h

    def draw(self, page, x, y):
        top = y + self.before
        bottom = self.rich.draw(page, x, top)
        page.draw_line((x, bottom + 1.6), (x + BODY_W, bottom + 1.6),
                       color=TEAL, width=0.8)
        page.draw_line((x, bottom + 3.0), (x + min(BODY_W, 120), bottom + 3.0),
                       color=GOLD, width=1.1)


class Para(Flow):
    def __init__(self, text, size=FS, leading=None, color=NAVY, align="left",
                 space_before=None, space_after=None, indent=0.0):
        self.rich = Rich(text, size=size,
                         leading=leading or sp(LEAD, LEAD - 0.55, LEAD + 0.75),
                         color=color, align=align,
                         space_before=sp(0, 0, 0) if space_before is None else space_before,
                         space_after=(sp(3.2, 1.9, 5.6) if space_after is None
                                      else space_after),
                         indent=indent)
        self.h = None

    def layout(self, w):
        self.h = self.rich.layout(w) + self.stretch
        return self.h

    def draw(self, page, x, y):
        self.rich.draw(page, x, y)


class Bullets(Flow):
    def __init__(self, items, numbered=False, size=FS, leading=None,
                 space_after=None):
        self.items = items
        self.numbered = numbered
        self.size = size
        self.leading = leading or sp(LEAD - 0.6, LEAD - 0.7, LEAD + 0.7)
        self.space_after = sp(2.0, 1.4, 3.6) if space_after is None else space_after
        self.rich = []
        self.h = None

    def layout(self, w):
        ind = 17.0
        self.rich = []
        total = 0.0
        for it in self.items:
            r = Rich(it, size=self.size, leading=self.leading, indent=ind,
                     space_before=0, space_after=0)
            r.layout(w)
            self.rich.append(r)
            total += r.h + self.space_after
        self.h = total + self.stretch
        return self.h

    def draw(self, page, x, y):
        for i, r in enumerate(self.rich):
            if self.numbered:
                label = f"{i + 1}."
                draw_text(page, x + 1, y + self.leading - 0.28 * self.leading,
                          label, "kalam-b", self.size, TEAL)
            else:
                page.draw_circle((x + 6.2, y + self.leading * 0.62), 1.5,
                                 color=TEAL, fill=TEAL)
            y = r.draw(page, x, y) + self.space_after


class EqBlock(Flow):
    def __init__(self, lines):
        self.lines = lines if isinstance(lines, (list, tuple)) else [lines]
        self.before = sp(2.4, 1.4, 4.0)
        self.after = sp(5.0, 3.4, 8.0)
        self.rich = []
        self.h = None

    def layout(self, w):
        self.rich = []
        for ln in self.lines:
            r = Rich(ln, size=12.0, leading=17.0, color=NAVY, align="center",
                     space_before=0, space_after=0, base="serif")
            r.layout(w)
            self.rich.append(r)
        self.h = self.before + sum(r.h for r in self.rich) + self.after + self.stretch
        return self.h

    def draw(self, page, x, y):
        yy = y + self.before
        for r in self.rich:
            yy = r.draw(page, x, yy)


class Callout(Flow):
    def __init__(self, text, kind="key"):
        self.kind = kind
        self.box = {"key": BOX, "warn": REDBOX, "note": TEALBOX}[kind]
        self.edge = {"key": GOLD, "warn": RED, "note": TEAL}[kind]
        self.label = {"key": "KEY RESULT", "warn": "TRAP", "note": "NOTE"}[kind]
        self.pad = 7.0
        self.label_h = 11.6
        self.before = sp(3.4, 2.2, 6.0)
        self.after = sp(5.6, 3.8, 9.0)
        self.rich = Rich(text, size=FS, leading=sp(LEAD - 0.7, LEAD - 0.9, LEAD + 0.4),
                         color=NAVY, space_before=0, space_after=0, pad=self.pad)
        self.h = None

    def layout(self, w):
        self.w = w
        self.rich.layout(w)
        self.h = self.before + self.label_h + self.rich.h + 4.0 + self.after + self.stretch
        return self.h

    def draw(self, page, x, y):
        top = y + self.before
        bot = top + self.h - self.before - self.after
        page.draw_rect(pymupdf.Rect(x, top, x + BODY_W, bot), color=None,
                       fill=self.box, width=0)
        page.draw_line((x, top), (x, bot), color=self.edge, width=2.2)
        r = pymupdf.Rect(x, top, x + BODY_W, bot)
        page.draw_rect(r, color=self.edge, width=0.45, dashes="[2 2] 0")
        draw_text(page, x + 9, top + 9.4, self.label, "caveat", 7.6, self.edge)
        self.rich.draw(page, x, top + self.label_h)


class _Cell:
    __slots__ = ("rich", "h")

    def __init__(self, rich):
        self.rich = rich
        self.h = 0.0


class TableEl(Flow):
    def __init__(self, headers, rows, widths=None, caption="", size=9.3):
        self.headers = headers
        self.rows = rows
        self.widths = widths or [1] * len(headers)
        self.caption = caption
        self.size = size
        self.before = sp(2.0, 1.2, 3.6)
        self.after = sp(4.0, 2.6, 6.4)
        self.cap = Rich(caption, size=8.5, leading=11.0, color=TEAL,
                        space_before=0, space_after=0) if caption else None
        self.h = None

    def layout(self, w):
        self.w = w
        tot = sum(self.widths)
        self.cols = [w * x / tot for x in self.widths]
        pad = 4.0
        self.head = []
        hh = 0.0
        for i, h in enumerate(self.headers):
            r = Rich(h, size=self.size, leading=self.size * 1.24, color=NAVY,
                     space_before=0, space_after=0, pad=pad)
            r.layout(self.cols[i])
            self.head.append(r)
            hh = max(hh, r.h)
        self.head_h = hh + 5.0
        self.body = []
        bh = 0.0
        for row in self.rows:
            cells = []
            rh = 0.0
            for i, c in enumerate(row):
                r = Rich(str(c), size=self.size, leading=self.size * 1.24,
                         color=NAVY, space_before=0, space_after=0, pad=pad)
                r.layout(self.cols[i])
                cells.append(r)
                rh = max(rh, r.h)
            self.body.append((cells, rh + 4.4))
            bh += rh + 4.4
        caph = 0.0
        if self.cap:
            self.cap.layout(w)
            caph = self.cap.h + 2.0
        self.h = self.before + self.head_h + bh + caph + self.after + self.stretch
        return self.h

    def draw(self, page, x, y):
        top = y + self.before
        page.draw_rect(pymupdf.Rect(x, top, x + self.w, top + self.head_h),
                       color=None, fill=(0.929, 0.945, 0.969), width=0)
        yy = top + 2.0
        for i, r in enumerate(self.head):
            r.draw(page, x + sum(self.cols[:i]), yy)
        page.draw_line((x, top + self.head_h), (x + self.w, top + self.head_h),
                       color=TEAL, width=0.9)
        yy = top + self.head_h
        for cells, rh in self.body:
            for i, r in enumerate(cells):
                r.draw(page, x + sum(self.cols[:i]), yy + 2.0)
            yy += rh
            page.draw_line((x, yy), (x + self.w, yy), color=GRID, width=0.6)
        for cx in [0] + [sum(self.cols[:i + 1]) for i in range(len(self.cols))]:
            page.draw_line((x + cx, top), (x + cx, yy), color=GRID, width=0.6)
        page.draw_line((x, top), (x + self.w, top), color=TEAL, width=0.9)
        page.draw_line((x, yy), (x + self.w, yy), color=TEAL, width=0.9)
        if self.cap:
            self.cap.draw(page, x, yy + 2.0)


class Fig(Flow):
    def __init__(self, name, caption="", aspect=None, scale=1.0):
        self.name = name
        self.caption = caption
        fn, default = sketch.REGISTRY[name]
        self.aspect = aspect or default
        self.scale = scale
        self.before = sp(2.5, 1.6, 5.0)
        self.after = sp(4.5, 2.8, 8.0)
        self.h = None

    def layout(self, w):
        self.w = w
        self.fh = w * self.aspect * self.scale
        self.cap = (Rich(self.caption, size=8.4, leading=11.0, color=TEAL,
                         align="center", space_before=0, space_after=0)
                    if self.caption else None)
        caph = (self.cap.layout(w) + 12.5) if self.cap else 0.0
        self.h = self.before + self.fh + caph + self.after + self.stretch
        return self.h

    def draw(self, page, x, y):
        top = y + self.before
        page.draw_rect(pymupdf.Rect(x, top, x + self.w, top + self.fh),
                       color=None, fill=(1, 1, 1), width=0)
        fn, _ = sketch.REGISTRY[self.name]
        fn(page, x, top, self.w, self.fh)
        if self.cap:
            self.cap.draw(page, x, top + self.fh + 2.2)


class PageBreak(Flow):
    def __init__(self):
        self.h = 0.0

    def layout(self, w):
        return 0.0


# ---------------------------------------------------------------------------
# block list -> flows
# ---------------------------------------------------------------------------
def make_flow(b):
    kind = b[0]
    if kind == "h2":
        return Heading(b[1], 2)
    if kind == "h3":
        return Heading(b[1], 3)
    if kind == "p":
        return Para(b[1])
    if kind == "lead":
        return Para(b[1], size=11.8, color=(0.055, 0.180, 0.270),
                    leading=sp(15.8, 15.4, 16.6))
    if kind == "eq":
        if isinstance(b[1], (list, tuple)):
            return EqBlock(list(b[1]))
        return EqBlock([b[1]])
    if kind == "bul":
        return Bullets(b[1])
    if kind == "num":
        return Bullets(b[1], numbered=True)
    if kind in ("key", "warn", "note"):
        return Callout(b[1], kind)
    if kind == "fig":
        return Fig(b[1], b[2] if len(b) > 2 else "",
                   b[3] if len(b) > 3 else None, b[4] if len(b) > 4 else 1.0)
    if kind == "table":
        return TableEl(b[1], b[2], b[3] if len(b) > 3 else None,
                       b[4] if len(b) > 4 else "")
    if kind == "rule":
        return Rule()
    if kind == "pagebreak":
        return PageBreak()
    if kind == "gap":
        return Gap(b[1] if len(b) > 1 else 5)
    raise ValueError(kind)


# ---------------------------------------------------------------------------
# pagination
# ---------------------------------------------------------------------------
def plan(flows):
    pages = [[]]
    y = BODY_TOP
    for i, f in enumerate(flows):
        if isinstance(f, PageBreak):
            if pages[-1]:
                pages.append([])
                y = BODY_TOP
            continue
        h = f.layout(BODY_W)
        need = h
        nxt = flows[i + 1] if i + 1 < len(flows) else None
        keep = 0.0
        if isinstance(f, Heading) and nxt is not None and not isinstance(nxt, PageBreak):
            keep = min(nxt.layout(BODY_W), 92.0)
        if y + need + keep > BODY_BOTTOM and pages[-1]:
            pages.append([])
            y = BODY_TOP
        pages[-1].append((f, y))
        y += h
    return pages


def _fill(page_items):
    if not page_items:
        return 0.0
    last = page_items[-1][0]
    y = page_items[-1][1] + last.h - last.after
    y = min(y, BODY_BOTTOM)
    return max(0.0, (y - BODY_TOP) / (BODY_BOTTOM - BODY_TOP))


# ---------------------------------------------------------------------------
# page furniture
# ---------------------------------------------------------------------------
def _fit(text, max_w, font_key="kalam", size=7.0):
    """Ellipsize at a word boundary so a header never runs under the sheet chip."""
    if width(text, font_key, size) <= max_w:
        return text
    words, out = text.split(), ""
    for w in words:
        cand = (out + " " + w).strip()
        if width(cand + " ...", font_key, size) <= max_w:
            out = cand
        else:
            break
    return (out + " ...").strip() if out else "..."


def draw_furniture(page, part_label, part_short, sid, title, sheet_idx, sheet_total,
                   page_idx, page_total, running):
    # rules
    for yy in range(72, 800, 15):
        page.draw_line((M, yy + 10.6), (PAGE_W - M, yy + 10.6), color=GRID, width=0.45)
    # header
    draw_text(page, M, 41, "Stereoisomerism", "caveat", 21.5, TEAL)
    sub = "short notes  \u00b7  " + running
    draw_text(page, M, 55.5, _fit(sub, PAGE_W - M - 182 - M, "kalam", 8.2), "kalam", 8.2, NAVY)
    page.draw_line((M, 60), (PAGE_W - M, 60), color=TEAL, width=0.9)
    page.draw_line((M, 62.2), (M + 150, 62.2), color=GOLD, width=1.2)
    # sheet chip
    chip = pymupdf.Rect(PAGE_W - M - 176, 27, PAGE_W - M, 55)
    page.draw_rect(chip, color=TEAL, width=0.7, dashes="[2 2] 0")
    draw_text(page, chip.x0 + 7, 40, part_label, "caveat", 8.0, TEAL)
    draw_text(page, chip.x1 - 7, 40, sid, "caveat", 10.5, NAVY)
    tail = f"sheet {sheet_idx} of {sheet_total}"
    room = chip.width - 14 - width(tail, "kalam", 6.9) - 8
    draw_text(page, chip.x0 + 7, 51, _fit(title, room, "kalam", 6.9), "kalam", 6.9, NAVY)
    draw_text(page, chip.x1 - 7 - width(f"sheet {sheet_idx} of {sheet_total}", "kalam", 6.9),
              51, f"sheet {sheet_idx} of {sheet_total}", "kalam", 6.9, TEAL)
    # footer
    page.draw_line((M, 806), (PAGE_W - M, 806), color=TEAL, width=0.8)
    draw_text(page, M, 817, part_short, "kalam", 8.2, TEAL)
    mid = f"sheet {sheet_idx} of {sheet_total}  \u00b7  page {page_idx} of {page_total}"
    draw_text(page, (PAGE_W - width(mid, "kalam", 8.2)) / 2, 817, mid, "kalam", 8.2, NAVY)
    right = f"stereoisomerism \u00b7 {sid}"
    draw_text(page, PAGE_W - M - width(right, "kalam", 8.2), 817, right, "kalam", 8.2, TEAL)


# ---------------------------------------------------------------------------
# build
# ---------------------------------------------------------------------------
def build_sheet(sheet, sheet_idx, sheet_total, part_label, part_short, running):
    """Choose a spacing profile for this sheet.

    Flows are rebuilt for each attempt because the profile is baked into the
    leading/spacing values when the flow objects are constructed. Font sizes are
    never changed; only the space between and inside blocks.
    """
    global COMPACT, ROOMY, TIGHT

    def attempt(compact=False, tight=False, roomy=False):
        global COMPACT, ROOMY, TIGHT
        COMPACT, ROOMY, TIGHT = compact, roomy, tight
        flows = [make_flow(b) for b in sheet["blocks"]]
        pages = plan(flows)
        COMPACT = ROOMY = TIGHT = False
        return pages, flows

    pages, flows = attempt()
    if len(pages) > 1 and _fill(pages[-1]) < 0.55:
        c_pages, c_flows = attempt(compact=True)
        if len(c_pages) < len(pages):
            pages, flows = c_pages, c_flows
        elif len(c_pages) == len(pages) and _fill(c_pages[-1]) > _fill(pages[-1]) + 0.08:
            pages, flows = c_pages, c_flows
        if len(pages) > 1 and _fill(pages[-1]) < 0.40:
            t_pages, t_flows = attempt(tight=True)
            if len(t_pages) < len(pages):
                pages, flows = t_pages, t_flows
    if len(pages) == 1:
        # sparse one-pager (also when compact/tight rescued a 2-page draft): give the sheet room to breathe, then hand out any
        # remaining slack evenly as inter-block stretch so pages end full
        if _fill(pages[0]) < 0.85:
            r_pages, r_flows = attempt(roomy=True)
            if len(r_pages) == 1:
                pages, flows = r_pages, r_flows
        items = pages[0]
        used = items[-1][1] + items[-1][0].h
        leftover = BODY_BOTTOM - used - 1.5
        if leftover > 10:
            add = leftover / max(1, len(items))
            for f, _ in items:
                f.stretch += add
            grown = plan(flows)
            if len(grown) == 1:
                pages = grown
            else:
                for f, _ in items:
                    f.stretch -= add
                pages = plan(flows)
    return pages, flows


def build_pdf(sheets, out_path, part_label, part_short, running, meta_title):
    doc = pymupdf.open()
    info = []
    total = len(sheets)
    for idx, sh in enumerate(sheets, 1):
        pages, flows = build_sheet(sh, idx, total, part_label, part_short, running)
        info.append({"id": sh["id"], "title": sh["title"], "pages": len(pages)})
        for pi, items in enumerate(pages, 1):
            page = doc.new_page(width=PAGE_W, height=PAGE_H)
            begin_text(page)
            draw_furniture(page, part_label, part_short, sh["id"], sh["title"],
                           idx, total, pi, len(pages), running)
            for f, y in items:
                f.draw(page, M, y)
            end_text(page)
    doc.set_metadata({"title": meta_title, "author": "Arena short-notes build",
                      "subject": f"{running} short notes",
                      "keywords": part_label})
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    toc = []
    pg = 0
    for sh in info:
        toc.append([1, f"{sh['id']} \u2014 {sh['title']}", pg + 1])
        pg += sh["pages"]
    doc.set_toc(toc)
    doc.save(out_path, deflate=True, garbage=3)
    n = len(doc)
    doc.close()
    with open(os.path.join(os.path.dirname(out_path), "build-info.json"), "w") as f:
        json.dump({"part": part_label, "sheets": info, "pages": n}, f, indent=1)
    return n, info


def to_pngs(pdf_path, out_dir, prefix, dpi=300, colors=64):
    os.makedirs(out_dir, exist_ok=True)
    doc = pymupdf.open(pdf_path)
    outs = []
    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=dpi, colorspace=pymupdf.csRGB, alpha=False)
        path = os.path.join(out_dir, f"{prefix}-{i + 1:02d}.png")
        pix.save(path)
        _normalise_png(path, dpi, colors)
        outs.append(path)
    doc.close()
    return outs


def _normalise_png(path, dpi, colors):
    from PIL import Image
    im = Image.open(path).convert("RGB")
    if im.size != (2480, 3508):
        im = im.resize((2480, 3508), Image.LANCZOS)
    q = im.quantize(colors=colors, method=Image.MEDIANCUT, dither=Image.FLOYDSTEINBERG)
    q.save(path, dpi=(dpi, dpi), optimize=True)


def merge(pdf_paths, out_path, title, toc):
    doc = pymupdf.open()
    offset = 0
    for p in pdf_paths:
        src = pymupdf.open(p)
        doc.insert_pdf(src)
        offset += len(src)
        src.close()
    doc.set_toc(toc)
    doc.set_metadata({"title": title, "author": "Arena short-notes build"})
    doc.save(out_path, deflate=True, garbage=3)
    doc.close()
