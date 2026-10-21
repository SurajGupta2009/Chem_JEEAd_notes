"""Vector chemistry sketches drawn straight onto the PDF page (no raster).

Each figure is composed on a design canvas measured in points (538 wide,
height = 538 * aspect) and scaled uniformly into the box the layout engine
hands over, so bond angles and label sizes stay right at any width.
"""
from __future__ import annotations

import math

from textkit import GOLD, NAVY, RED, TEAL, draw_text, glyph_runs, width


class Pen:
    def __init__(self, page, x, y_top, w, h, W0=538.0, H0=140.0):
        self.p = page
        self.k = min(w / W0, h / H0)
        self.ox = x + (w - W0 * self.k) / 2.0
        self.oy = y_top + (h - H0 * self.k) / 2.0
        self.fs = 8.7
        self.lw = max(0.85, min(1.2, 0.95 * self.k + 0.1))

    def P(self, px, py):
        return (self.ox + px * self.k, self.oy + py * self.k)

    def line(self, a, b, color=NAVY, width=None, dash=None):
        self.p.draw_line(self.P(*a), self.P(*b), color=color,
                         width=self.lw if width is None else width, dashes=dash)

    def poly(self, pts, color=NAVY, width=None, fill=None, close=False):
        P = [self.P(*q) for q in pts]
        if fill is not None:
            self.p.draw_polyline(P, color=color, fill=fill, width=0.2, closePath=close)
        else:
            self.p.draw_polyline(P, color=color,
                                 width=self.lw if width is None else width,
                                 closePath=close)

    def bond(self, a, b, order=1, stereo=None, color=NAVY, g1=0.0, g2=0.0):
        (x1, y1), (x2, y2) = a, b
        dx, dy = x2 - x1, y2 - y1
        n = math.hypot(dx, dy) or 1.0
        ux, uy = dx / n, dy / n
        x1, y1 = x1 + ux * g1, y1 + uy * g1
        x2, y2 = x2 - ux * g2, y2 - uy * g2
        if stereo == "wedge":
            px, py = -uy * 2.4, ux * 2.4
            self.poly([(x1, y1), (x2 + px, y2 + py), (x2 - px, y2 - py)],
                      fill=color, color=color, close=True)
            return
        if stereo == "hash":
            px, py = -uy * 3.2, ux * 3.2
            for i in range(1, 7):
                t = i / 6.6
                cx, cy = x1 + (x2 - x1) * t, y1 + (y2 - y1) * t
                f = 0.30 + 0.70 * t
                self.line((cx - px * f, cy - py * f), (cx + px * f, cy + py * f), color=color)
            return
        if order == 2:
            px, py = -uy * 2.3, ux * 2.3
            self.line((x1 + px, y1 + py), (x2 + px, y2 + py), color=color)
            self.line((x1 - px, y1 - py), (x2 - px, y2 - py), color=color)
            return
        if order == 3:
            px, py = -uy * 2.4, ux * 2.4
            self.line((x1 + px, y1 + py), (x2 + px, y2 + py), color=color)
            self.line(a, b, color=color)
            self.line((x1 - px, y1 - py), (x2 - px, y2 - py), color=color)
            return
        self.line((x1, y1), (x2, y2), color=color)

    def dash(self, a, b, color=TEAL, pattern="[2.4 2.2] 0"):
        self.line(a, b, color=color, dash=pattern)

    def circle(self, c, r, fill=None, stroke=NAVY):
        self.p.draw_circle(self.P(*c), r * self.k, color=stroke, fill=fill, width=self.lw)

    def arrow(self, a, b, color=NAVY, head=6.0):
        p1, p2 = self.P(*a), self.P(*b)
        self.p.draw_line(p1, p2, color=color, width=self.lw)
        dx, dy = p2[0] - p1[0], p2[1] - p1[1]
        n = math.hypot(dx, dy) or 1.0
        ux, uy = dx / n, dy / n
        px, py = -uy * head * 0.42, ux * head * 0.42
        tri = [p2, (p2[0] - ux * head + px, p2[1] - uy * head + py),
               (p2[0] - ux * head - px, p2[1] - uy * head - py)]
        self.p.draw_polyline(tri, color=color, fill=color, closePath=True, width=0.2)

    # text with ~sub~ and ^sup^ -------------------------------------------------
    def _runs(self, s):
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

    def text(self, x, y, s, size=None, color=NAVY, align="c", kind="kalam-b"):
        size = self.fs if size is None else size
        parts = []
        for txt, mode in self._runs(s):
            sz = size * (1.0 if mode == 0 else 0.64)
            dy = 0.0 if mode == 0 else (0.20 * size if mode == -1 else -0.40 * size)
            for k, t in glyph_runs(txt, kind):
                parts.append((k, t, sz, dy))
        total = sum(width(t, k, sz) for k, t, sz, _ in parts)
        cx = x
        if align == "c":
            cx -= total / 2
        elif align == "r":
            cx -= total
        bx, by = self.P(cx, y)
        for k, t, sz, dy in parts:
            draw_text(self.p, bx, by + dy * self.k, t, k, sz, color)
            bx += width(t, k, sz)

    def atom(self, x, y, s, **kw):
        self.text(x, y, s, **kw)


# ---------------------------------------------------------------------------
# figures
# ---------------------------------------------------------------------------
def fig_condition(page, x, y, w, h):
    g = Pen(page, x, y, w, h, 538, 108)
    c1, c2 = (150, 62), (214, 62)
    g.bond(c1, c2, order=2)
    g.bond(c1, (112, 36)); g.bond(c1, (112, 88))
    g.bond(c2, (252, 36)); g.bond(c2, (252, 88))
    g.text(106, 39, "a", align="r"); g.text(106, 91, "b", align="r")
    g.text(258, 39, "x", align="l"); g.text(258, 91, "y", align="l")
    g.text(300, 42, "the \u03c0 bond stops rotation", color=TEAL, align="l")
    g.text(300, 62, "a \u2260 b  and  x \u2260 y", color=RED, align="l")
    g.text(300, 82, "\u2192 geometrical isomers (E/Z)", align="l")


def fig_butene(page, x, y, w, h):
    g = Pen(page, x, y, w, h, 538, 140)
    for cx, rt, rb, lab in [(140, "CH~3~", "H", "cis-but-2-ene"),
                            (398, "H", "CH~3~", "trans-but-2-ene")]:
        c1, c2 = (cx - 27, 84), (cx + 27, 84)
        g.bond(c1, c2, order=2)
        g.bond(c1, (cx - 51, 60)); g.bond(c1, (cx - 51, 108))
        g.bond(c2, (cx + 51, 60)); g.bond(c2, (cx + 51, 108))
        g.text(cx - 53, 56, "CH~3~", align="r")
        g.text(cx - 53, 112, "H", align="r")
        g.text(cx + 53, 56, rt, align="l")
        g.text(cx + 53, 112, rb, align="l")
        g.text(cx, 134, lab, color=TEAL)
    g.text(140, 22, "\u03bc \u2260 0 (bond moments add)", color=TEAL, size=8.0)
    g.text(398, 22, "\u03bc = 0 (moments cancel)", color=TEAL, size=8.0)


def fig_oxime(page, x, y, w, h):
    g = Pen(page, x, y, w, h, 538, 140)
    for cx, oh_down, lab in [(150, True, "syn  (OH with CH~3~)"),
                             (390, False, "anti  (OH opposite CH~3~)")]:
        c, n = (cx - 30, 90), (cx + 30, 90)
        g.bond(c, n, order=2, g1=8, g2=10)
        g.text(cx + 30, 80, "N")
        g.bond(c, (cx - 60, 118)); g.bond(c, (cx - 60, 62))
        g.text(cx - 62, 122, "CH~3~", align="r")
        g.text(cx - 62, 58, "H", align="r")
        oy = 118 if oh_down else 62
        g.bond(n, (cx + 62, oy))
        g.text(cx + 64, oy + 4, "OH", align="l")
        ly = 70 if oh_down else 110
        g.circle((cx + 44, ly), 1.1, fill=NAVY, stroke=NAVY)
        g.circle((cx + 49, ly), 1.1, fill=NAVY, stroke=NAVY)
        g.text(cx, 26, lab, color=TEAL, size=8.2)


def fig_azo(page, x, y, w, h):
    g = Pen(page, x, y, w, h, 538, 130)
    for cx, trans, lab in [(150, False, "cis (syn): both Ph on one side"),
                           (390, True, "trans (anti): Ph opposite")]:
        n1, n2 = (cx - 22, 76), (cx + 22, 76)
        g.bond(n1, n2, order=2, g1=8, g2=8)
        g.text(cx - 22, 68, "N"); g.text(cx + 22, 68, "N")
        g.bond(n1, (cx - 56, 50)); g.text(cx - 60, 47, "Ph", align="r")
        g.bond(n2, (cx + 56, 102 if trans else 50))
        g.text(cx + 60, 105 if trans else 47, "Ph", align="l")
        g.text(cx, 20, lab, color=TEAL, size=8.1)


def fig_ring_updown(page, x, y, w, h):
    g = Pen(page, x, y, w, h, 538, 183)
    for cx, trans, lab in [(150, False, "cis: \u03c3 present \u2192 achiral"),
                           (390, True, "trans: no \u03c3 \u2192 enantiomers")]:
        apex, left, right = (cx, 52), (cx - 56, 140), (cx + 56, 140)
        g.bond(apex, left); g.bond(apex, right); g.bond(left, right)
        g.bond(apex, (cx, 22), stereo="wedge")
        g.text(cx, 15, "CH~3~")
        g.bond(right, (cx + 56, 110), stereo=("hash" if trans else "wedge"))
        g.text(cx + 58, 106, "CH~3~", align="l")
        g.text(cx, 166, lab, color=TEAL, size=8.1)


def fig_cumulene(page, x, y, w, h):
    g = Pen(page, x, y, w, h, 538, 161)
    c1, c2, c3 = (78, 82), (126, 82), (174, 82)
    g.bond(c1, c2, order=2, g1=6, g2=4)
    g.bond(c2, c3, order=2, g1=4, g2=6)
    g.text(c2[0], c2[1] - 10, "C", size=7.6)
    g.bond(c1, (52, 56)); g.bond(c1, (52, 108))
    g.text(48, 54, "a", align="r"); g.text(48, 112, "b", align="r")
    g.bond(c3, (200, 56), stereo="wedge")
    g.bond(c3, (200, 108), stereo="hash")
    g.text(205, 54, "x", align="l"); g.text(205, 112, "y", align="l")
    px, py = 400, 82
    g.dash((px, py - 44), (px, py + 44), color=GOLD)
    g.text(px + 4, py - 48, "plane of a, b", color=GOLD, align="l", size=8.0)
    g.dash((px - 58, py), (px + 58, py), color=TEAL)
    g.text(px - 62, py + 4, "plane of x, y", color=TEAL, align="r", size=8.0)
    g.text(px, py + 60, "\u22a5", color=RED, size=10)
    g.text(126, 146, "left pair in the page plane; x, y are wedge/hash, so their plane is \u22a5 to it",
           color=TEAL, size=7.9)


def fig_chiral_carbon(page, x, y, w, h):
    g = Pen(page, x, y, w, h, 538, 183)

    def centre(cx, mirror):
        cy = 96
        g.text(cx, cy + 3, "C")
        g.bond((cx, cy), (cx, cy - 34), g1=9)
        g.bond((cx, cy), (cx, cy + 34), g1=9)
        g.text(cx, cy - 40, "H"); g.text(cx, cy + 52, "F")
        ls, rs = ("wedge", "hash") if mirror else ("hash", "wedge")
        g.bond((cx, cy), (cx - 42, cy - 18), stereo=ls, g1=10)
        g.bond((cx, cy), (cx + 42, cy - 18), stereo=rs, g1=10)
        g.text(cx - 46, cy - 26, "Br" if not mirror else "Cl", align="r")
        g.text(cx + 46, cy - 26, "Cl" if not mirror else "Br", align="l")

    centre(150, False); centre(390, True)
    g.dash((270, 34), (270, 156))
    g.text(274, 40, "\u03c3", color=TEAL, align="l")
    g.text(150, 176, "one enantiomer", color=TEAL)
    g.text(390, 176, "mirror image", color=RED)


def _rect(g, x1, y1, x2, y2):
    import pymupdf
    a, b = g.P(x1, y1), g.P(x2, y2)
    return pymupdf.Rect(a[0], a[1], b[0], b[1])


def fig_polarimeter(page, x, y, w, h):
    g = Pen(page, x, y, w, h, 538, 140)
    by = 74
    g.line((14, by), (44, by))
    g.arrow((24, by - 16), (44, by - 16), color=TEAL, head=4.5)
    g.text(20, by - 24, "light", color=TEAL, size=7.8, align="l")
    g.p.draw_rect(_rect(g, 44, 56, 96, 92), color=NAVY, width=g.lw)
    g.p.draw_rect(_rect(g, 124, 62, 300, 86), color=NAVY, width=g.lw)
    g.p.draw_rect(_rect(g, 330, 56, 382, 92), color=NAVY, width=g.lw)
    g.line((96, by), (124, by)); g.line((300, by), (330, by))
    g.line((382, by), (420, by))
    g.circle((432, by), 8, stroke=NAVY); g.circle((432, by), 2.4, fill=NAVY, stroke=NAVY)
    g.text(70, 106, "polarizer", color=TEAL, size=8.0)
    g.text(212, 106, "sample tube, path l", color=TEAL, size=8.0)
    g.text(356, 106, "analyser", color=TEAL, size=8.0)
    g.text(432, 106, "eye", color=TEAL, size=8.0)
    g.text(212, 42, "rotate the analyser back to darkness \u2192 \u03b1", size=8.0)


def fig_energy_butane(page, x, y, w, h):
    g = Pen(page, x, y, w, h, 538, 161)
    x0, x1, yb, yt = 70, 470, 126, 34
    g.line((x0, yt), (x0, yb)); g.line((x0, yb), (x1, yb))
    g.text(x0 - 8, yt + 6, "E", align="r")
    g.text(x1 - 60, yb + 34, "dihedral angle \u03b8", align="r")
    pts = []
    for i in range(181):
        deg = i * 2
        e = 0.5 - 0.5 * math.cos(math.radians(3 * deg))
        pts.append((x0 + (x1 - x0) * deg / 360.0, yt + (yb - yt) * (0.28 + 0.72 * e)))
    for i in range(len(pts) - 1):
        g.line(pts[i], pts[i + 1], color=TEAL, width=g.lw * 1.25)
    for deg in (0, 120, 240, 360):
        g.text(x0 + (x1 - x0) * deg / 360.0, yb + 8, str(deg), size=7.2)
    for deg, lab in ((60, "gauche"), (180, "anti"), (300, "gauche")):
        px = x0 + (x1 - x0) * deg / 360.0
        g.circle((px, yb - 4), 2.1, fill=TEAL, stroke=TEAL)
        g.text(px, yb + 18, lab, size=7.2, color=TEAL)


def fig_fischer(page, x, y, w, h):
    g = Pen(page, x, y, w, h, 538, 183)
    cx = 130
    g.line((cx, 46), (cx, 150))
    g.line((cx - 44, 80), (cx + 44, 80))
    g.line((cx - 44, 118), (cx + 44, 118))
    g.text(cx, 40, "CHO"); g.text(cx, 162, "CH~2~OH")
    g.text(cx - 48, 84, "H", align="r"); g.text(cx + 48, 84, "OH", align="l")
    g.text(cx - 48, 122, "H", align="r"); g.text(cx + 48, 122, "OH", align="l")
    g.text(cx, 178, "Fischer: vertical back", color=TEAL, size=8.0)
    mx, my = 380, 96
    g.text(mx, my + 4, "C")
    g.bond((mx, my - 6), (mx, my - 40)); g.text(mx, my - 44, "CHO")
    g.bond((mx, my + 6), (mx, my + 40)); g.text(mx, my + 52, "CH~2~OH")
    g.bond((mx + 6, my - 2), (mx + 44, my - 14), stereo="wedge")
    g.bond((mx - 6, my - 2), (mx - 44, my - 14), stereo="hash")
    g.text(mx + 48, my - 20, "OH", align="l")
    g.text(mx - 48, my - 20, "H", align="r")
    g.text(mx, 178, "same molecule, 3-D", color=TEAL, size=8.0)


def fig_tartaric(page, x, y, w, h):
    g = Pen(page, x, y, w, h, 538, 215)
    for cx, tr, br, lab in [(95, True, True, "(R,R)  active"),
                            (270, False, False, "(S,S)  active"),
                            (445, True, False, "(R,S)  meso")]:
        g.line((cx, 48), (cx, 168))
        g.line((cx - 40, 78), (cx + 40, 78))
        g.line((cx - 40, 132), (cx + 40, 132))
        g.text(cx, 42, "COOH"); g.text(cx, 182, "COOH")
        g.text(cx - 44, 82, "H" if tr else "OH", align="r")
        g.text(cx + 44, 82, "OH" if tr else "H", align="l")
        g.text(cx - 44, 136, "H" if br else "OH", align="r")
        g.text(cx + 44, 136, "OH" if br else "H", align="l")
        g.text(cx, 202, lab, color=TEAL if "active" in lab else RED, size=8.1)
    g.dash((405, 105), (485, 105), color=RED)
    g.text(492, 108, "\u03c3", color=RED, size=8.4)


def fig_newman(page, x, y, w, h):
    g = Pen(page, x, y, w, h, 538, 150)

    def view(cx, cy, r, eclipsed):
        g.circle((cx, cy), r, stroke=NAVY)
        g.circle((cx, cy), 1.8, fill=NAVY, stroke=NAVY)
        for ang in (90, 210, 330):
            a = math.radians(ang)
            g.line((cx, cy), (cx + (r + 16) * math.cos(a), cy - (r + 16) * math.sin(a)))
            g.text(cx + (r + 22) * math.cos(a), cy - (r + 22) * math.sin(a) + 3, "H", size=7.6)
        for ang in ((82, 202, 322) if eclipsed else (30, 150, 270)):
            a = math.radians(ang)
            g.line((cx + r * math.cos(a), cy - r * math.sin(a)),
                   (cx + (r + 16) * math.cos(a), cy - (r + 16) * math.sin(a)))
            g.text(cx + (r + 22) * math.cos(a), cy - (r + 22) * math.sin(a) + 3, "H", size=7.6)

    view(150, 84, 34, False); view(390, 84, 34, True)
    g.text(150, 14, "staggered  (60\u00b0)", color=TEAL, size=8.2)
    g.text(390, 14, "eclipsed  (0\u00b0)", color=TEAL, size=8.2)
    g.text(150, 146, "lower energy", size=8.0)
    g.text(390, 146, "torsional strain", size=8.0)


def fig_ring_ae(page, x, y, w, h):
    g = Pen(page, x, y, w, h, 538, 183)
    pts = [(180, 62), (226, 40), (276, 62), (276, 124), (230, 146), (180, 124)]
    for i in range(6):
        g.bond(pts[i], pts[(i + 1) % 6])
    g.bond(pts[0], (180, 32)); g.text(180, 26, "a", color=RED)
    g.bond(pts[0], (150, 92)); g.text(144, 96, "e", color=TEAL, align="r")
    g.bond(pts[3], (276, 154)); g.text(276, 168, "a", color=RED)
    g.bond(pts[3], (306, 92)); g.text(312, 96, "e", color=TEAL, align="l")
    g.text(360, 66, "axial: vertical,", color=RED, size=8.0, align="l")
    g.text(360, 78, "up/down alternates", color=RED, size=8.0, align="l")
    g.text(360, 104, "equatorial: roughly radial,", color=TEAL, size=8.0, align="l")
    g.text(360, 116, "and alternates too", color=TEAL, size=8.0, align="l")


REGISTRY = {
    "condition": (fig_condition, 0.20),
    "butene": (fig_butene, 0.26),
    "oxime": (fig_oxime, 0.26),
    "azo": (fig_azo, 0.24),
    "ringupdown": (fig_ring_updown, 0.34),
    "cumulene": (fig_cumulene, 0.30),
    "chiralcarbon": (fig_chiral_carbon, 0.34),
    "polarimeter": (fig_polarimeter, 0.26),
    "butane": (fig_energy_butane, 0.30),
    "fischer": (fig_fischer, 0.34),
    "tartaric": (fig_tartaric, 0.40),
    "newman": (fig_newman, 0.28),
    "ringae": (fig_ring_ae, 0.34),
}
