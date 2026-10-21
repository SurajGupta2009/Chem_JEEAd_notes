"""Fonts, palette, markup parsing and text layout for the PDF pages.

One TextWriter is kept per colour for the whole page: PyMuPDF's TextWriter
takes a single colour, but batching one per colour keeps the page fast and
the colours exact (changing .color between appends is not reliable).
"""
from __future__ import annotations

import os
import re

import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(os.path.dirname(HERE), "assets", "fonts")

NAVY = (0.0863, 0.1451, 0.3020)
TEAL = (0.0392, 0.4196, 0.3843)
RED = (0.7020, 0.1490, 0.1176)
GOLD = (0.7216, 0.5255, 0.0431)
GRID = (0.8824, 0.9059, 0.9451)
INK = (0.0706, 0.1216, 0.2118)
PAPER = (1, 1, 1)
MARK = (1.0, 0.945, 0.686)
BOX = (0.976, 0.965, 0.890)
REDBOX = (0.992, 0.925, 0.914)
TEALBOX = (0.918, 0.957, 0.953)

_FILES = {
    "kalam": "kalam-latin-400-normal.ttf",
    "kalam-b": "kalam-latin-700-normal.ttf",
    "caveat": "caveat-latin-700-normal.ttf",
    "serif": "DejaVuSerif.ttf",
    "serif-b": "DejaVuSerif-Bold.ttf",
}
_FONTS = {}


def font(key):
    if key not in _FONTS:
        p = os.path.join(FONT_DIR, _FILES[key])
        f = pymupdf.Font(fontfile=p)
        _FONTS[key] = f
    return _FONTS[key]


def width(text, key, size):
    return font(key).text_length(text, fontsize=size)


# characters that Kalam lacks or draws poorly -> DejaVu Serif
_SERIF_CHARS = set(
    "\u03b1\u03b2\u03b3\u03b4\u03b5\u03b6\u03b7\u03b8\u03b9\u03ba\u03bb\u03bc\u03bd\u03be"
    "\u03c0\u03c1\u03c3\u03c4\u03c5\u03c6\u03c7\u03c8\u03c9\u0393\u0394\u0398\u039b\u039e"
    "\u03a0\u03a3\u03a6\u03a8\u03a9\u2192\u2190\u2194\u21cc\u21d2\u2260\u2264\u2265\u2248"
    "\u2212\u00b1\u00d7\u00f7\u221a\u221e\u2220\u2225\u22a5\u2020\u2021\u25b3\u2261\u2262"
    "\u222b\u2202\u2206\u03bc\u00b0\u2032\u2033\u2081\u2082\u2083\u2084"
)

_DIGITS = "\u2080\u2081\u2082\u2083\u2084\u2085\u2086\u2087\u2088\u2089"


def route(ch, key):
    """Pick the font that has this glyph, keeping the hand where possible."""
    if ch in _SERIF_CHARS:
        return "serif" if key != "kalam-b" else "serif-b"
    if key.startswith("serif"):
        return key
    return key


def glyph_runs(text, key):
    out = []
    for ch in text:
        k = route(ch, key)
        if out and out[-1][0] == k:
            out[-1] = (k, out[-1][1] + ch)
        else:
            out.append((k, ch))
    return out


# ---------------------------------------------------------------------------
# markup -> spans
# ---------------------------------------------------------------------------
TAG = re.compile(r"(<[^>]+>|\$[^$]+\$)")


class Span:
    __slots__ = ("text", "kind", "script", "color", "mark")

    def __init__(self, text, kind="kalam", script=0, color=None, mark=False):
        self.text = text
        self.kind = kind
        self.script = script
        self.color = color
        self.mark = mark

    def size(self, base):
        return base * {0: 1.0, 1: 0.60, -1: 0.64}[self.script]

    def dy(self, base):                      # PDF y grows downwards
        if self.script == 1:
            return -0.36 * base
        if self.script == -1:
            return 0.20 * base
        return 0.0


def preprocess(markup):
    s = markup.replace("\n", " ").replace("&nbsp;", "\u00a0")
    for a, b in (("\u2010", "-"), ("\u2011", "-"), ("\u2013", "-"), ("\u2014", "\u2014")):
        s = s.replace(a, b)

    # Convert ASCII chemical reaction arrows to unicode arrows
    s = s.replace("<===>", "\u21cc").replace("<===", "\u2190").replace("===>", "\u2192").replace("->", "\u2192")

    # Fix unbracketed superscripts like ^3+, ^2+, ^+, ^- into proper ^3+^, ^2+^, ^+^, ^-^
    s = re.sub(r"\^([0-9]*[+-])(?!\^)", r"^\1^", s)

    # Auto-subscript chemical formulas containing digits if not already subscripted
    def _sub_formula(m):
        raw = m.group(0)
        if "~" in raw or "$" in raw or "^" in raw:
            return raw
        # Avoid years (e.g. 2026), element groups (e.g. G13), temperatures (e.g. 300K)
        if raw.startswith("G") and raw[1:].isdigit():
            return raw
        # Convert digits after letters or closing parens into subscripts: B2H6 -> B~2~H~6~
        return re.sub(r"([A-Za-z\)])(\d+)", r"\1~\2~", raw)

    chem_pat = re.compile(r"\b(?:[A-Z][a-z]?(?:\d+|(?:\([A-Za-z0-9_]+\)\d*))+[A-Za-z0-9_()·+-]*)\b")
    s = chem_pat.sub(_sub_formula, s)
    return s


def parse(markup):
    """**bold** *italic* ~sub~ ^sup^ $math$ <mark>..</mark>."""
    s = preprocess(markup)
    spans = []
    bold = italic = mark = math = False
    for chunk in TAG.split(s):
        if not chunk:
            continue
        if chunk.startswith("<mark"):
            mark = True
            continue
        if chunk == "</mark>":
            mark = False
            continue
        if chunk.startswith("<"):
            continue
        if chunk.startswith("$") and chunk.endswith("$") and len(chunk) > 2:
            for txt, mode in _scripts(chunk[1:-1]):
                spans.append(Span(txt, "serif", mode, None, mark))
            continue
        i = 0
        buf = ""
        while i < len(chunk):
            c = chunk[i]
            if chunk.startswith("**", i):
                if buf:
                    spans.append(_span(buf, bold, italic, mark))
                    buf = ""
                bold = not bold
                i += 2
                continue
            if c == "*":
                if buf:
                    spans.append(_span(buf, bold, italic, mark))
                    buf = ""
                italic = not italic
                i += 1
                continue
            if c in "~^":
                if buf:
                    spans.append(_span(buf, bold, italic, mark))
                    buf = ""
                j = chunk.find(c, i + 1)
                if j < 0:
                    buf += c
                    i += 1
                    continue
                spans.append(Span(chunk[i + 1:j], "kalam-b" if bold else "kalam",
                                   -1 if c == "~" else 1, None, mark))
                i = j + 1
                continue
            buf += c
            i += 1
        if buf:
            spans.append(_span(buf, bold, italic, mark))
    return [s for s in spans if s.text]


def _scripts(s):
    """Split on ~sub~ / ^sup^ so equations can carry real sub/superscripts."""
    out, buf, mode = [], "", 0
    for ch in s:
        if ch in "~^":
            if buf:
                out.append((buf, mode))
                buf = ""
            mode = 0 if mode else (-1 if ch == "~" else 1)
        else:
            buf += ch
    if buf:
        out.append((buf, mode))
    return out


def _span(text, bold, italic, mark):
    if bold:
        return Span(text, "kalam-b", 0, None, mark)
    if italic:
        # Caveat has no true italic; a lighter hand reads as emphasis
        return Span(text, "kalam", 0, None, mark)
    return Span(text, "kalam", 0, None, mark)


# ---------------------------------------------------------------------------
# text writer (one per colour, per page)
# ---------------------------------------------------------------------------
_TW = {}


def begin_text(page):
    global _TW
    _TW = {}
    return _TW


def end_text(page):
    global _TW
    for tw in _TW.values():
        tw.write_text(page)
    _TW = {}


def draw_text(page, x, y, text, key, size, color):
    if not _TW:
        begin_text(page)
    ck = tuple(round(c, 3) for c in color)
    tw = _TW.get(ck)
    if tw is None:
        tw = pymupdf.TextWriter(page.rect)
        tw.color = ck
        _TW[ck] = tw
    tw.append((x, y), text, font=font(key), fontsize=size)


# ---------------------------------------------------------------------------
# Rich: wraps parsed markup into lines and draws them
# ---------------------------------------------------------------------------
class Word:
    __slots__ = ("pieces", "w", "space")

    def __init__(self, pieces, space=False):
        self.pieces = pieces          # [(kind, text, size, dy, color, mark)]
        self.w = sum(width(t, k, s) for k, t, s, dy, col, mk in pieces)
        self.space = space


class Rich:
    def __init__(self, markup, size=11.15, leading=15.15, color=NAVY,
                 align="left", space_before=0.0, space_after=3.2, indent=0.0,
                 first_indent=0.0, pad=0.0, base="kalam"):
        self.markup = markup
        self.spans = parse(markup) if isinstance(markup, str) else markup
        self.size = size
        self.leading = leading
        self.color = color
        self.align = align
        self.space_before = space_before
        self.space_after = space_after
        self.indent = indent
        self.first_indent = first_indent
        self.pad = pad
        self.base = base
        self.lines = []

    # -- layout -------------------------------------------------------
    def _words(self):
        out = []
        for sp in self.spans:
            chunks = re.split(r"(\s+)", sp.text)
            for ch in chunks:
                if not ch:
                    continue
                if ch.isspace():
                    if out:
                        out[-1].space = True
                    continue
                kind = sp.kind
                if self.base != "kalam" and kind == "kalam":
                    kind = self.base
                elif self.base != "kalam" and kind == "kalam-b":
                    kind = "serif-b"
                out.append(Word([(kind, ch, sp.size(self.size), sp.dy(self.size),
                                 sp.color or self.color, sp.mark)]))
        return out

    def layout(self, w):
        words = self._words()
        if not words:
            self.lines = []
            self.h = self.space_before + self.space_after
            return self.h
        lines, cur, curw = [], [], 0.0
        avail = w - 2 * self.pad - self.indent - self.first_indent
        for word in words:
            add = word.w + (width(" ", "kalam", self.size) if cur else 0.0)
            if cur and curw + add > avail:
                lines.append((cur, curw))
                cur, curw = [], 0.0
                add = word.w
                avail = w - 2 * self.pad - self.indent
            cur.append(word)
            curw += add
        if cur:
            lines.append((cur, curw))
        self.lines = lines
        self.w = w
        self.h = self.space_before + len(lines) * self.leading + self.space_after
        return self.h

    # -- draw ---------------------------------------------------------
    def draw(self, page, x, y, ruled=True):
        space = width(" ", "kalam", self.size)
        top = y + self.space_before
        for i, (words, curw) in enumerate(self.lines):
            base = top + (i + 1) * self.leading - 0.28 * self.leading
            ind = self.indent + (self.first_indent if i == 0 else 0)
            if self.align == "center":
                cx = x + (self.w - 2 * self.pad - curw) / 2
            elif self.align == "right":
                cx = x + self.w - self.pad - curw
            else:
                cx = x + self.pad + ind
            for word in words:
                for kind, text, size, dy, color, mark in word.pieces:
                    if mark:
                        page.draw_rect(pymupdf.Rect(cx - 0.6, base - size * 0.95,
                                                    cx + word.w + 0.6, base + size * 0.24),
                                       color=None, fill=MARK, width=0)
                    draw_text(page, cx, base + dy, text, kind, size, color)
                    cx += width(text, kind, size)
                if word.space:
                    cx += space
        return top + len(self.lines) * self.leading


def text_height(markup, w, size=11.15, leading=15.15, indent=0.0, pad=0.0):
    r = Rich(markup, size=size, leading=leading, indent=indent, pad=pad)
    return r.layout(w)
