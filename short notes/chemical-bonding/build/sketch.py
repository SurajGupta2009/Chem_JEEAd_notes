"""Vector chemistry sketches drawn straight onto the PDF page (no raster).

Each figure is composed on a design canvas measured in points (538 wide,
height = 538 * aspect) and scaled uniformly into the box the layout engine
hands over, so bond angles and label sizes stay right at any width.
"""
from __future__ import annotations

import math

from textkit import GOLD, NAVY, RED, TEAL, PAPER, draw_text, glyph_runs, width


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

    def bond(self, a, b, order=1, stereo=None, color=NAVY, g1=0.0, g2=0.0, width=None):
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

    def circle(self, c, r, fill=None, color=None, stroke=NAVY, close=False):
        if color is not None: stroke = color
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

# ===========================================================================
# p-Block Specific Figures & Chemical Structures
# ===========================================================================

def fig_diborane(page, x, y, w, h):
    """Diborane B2H6 3c-2e bridge (banana bonds) structure."""
    g = Pen(page, x, y, w, h, 538, 140)
    # Terminal B-H bonds
    # Left B at (190, 70), Right B at (348, 70)
    g.circle((190, 70), 10, color=TEAL, fill=PAPER, close=True)
    g.text(190, 74, "B", color=TEAL, size=9.5)
    g.circle((348, 70), 10, color=TEAL, fill=PAPER, close=True)
    g.text(348, 74, "B", color=TEAL, size=9.5)

    # Terminal H bonds (left)
    g.bond((180, 65), (130, 35))
    g.text(122, 33, "Ht", color=NAVY, size=8.5)
    g.bond((180, 75), (130, 105))
    g.text(122, 110, "Ht", color=NAVY, size=8.5)

    # Terminal H bonds (right)
    g.bond((358, 65), (408, 35))
    g.text(416, 33, "Ht", color=NAVY, size=8.5)
    g.bond((358, 75), (408, 105))
    g.text(416, 110, "Ht", color=NAVY, size=8.5)

    # Bridge H top (269, 25) and bottom (269, 115)
    g.circle((269, 25), 8, color=RED, fill=PAPER)
    g.text(269, 28, "Hb", color=RED, size=8.5)
    g.circle((269, 115), 8, color=RED, fill=PAPER)
    g.text(269, 118, "Hb", color=RED, size=8.5)

    # Banana bonds (curved arc / line to bridges)
    g.line((195, 62), (262, 28), color=RED, width=1.5)
    g.line((276, 28), (343, 62), color=RED, width=1.5)
    g.line((195, 78), (262, 112), color=RED, width=1.5)
    g.line((276, 112), (343, 78), color=RED, width=1.5)

    # Annotation
    g.text(269, 68, "3c-2e bridge (banana bond)", color=RED, size=7.8)
    g.text(269, 80, "B-Hb: 133 pm, B-Ht: 119 pm", color=NAVY, size=7.2)
    g.text(269, 92, "Hb-B-Hb: 97 deg, Ht-B-Ht: 121 deg", color=NAVY, size=7.2)


def fig_borax_anion(page, x, y, w, h):
    """Borax anion [B4O5(OH)4]2- ring structure."""
    g = Pen(page, x, y, w, h, 538, 150)
    # 2 sp2 Borons (trigonal), 2 sp3 Borons (tetrahedral)
    # Ring vertices: B1(200, 45), O1(269, 35), B2(338, 45), O2(370, 75),
    # B3(338, 105), O3(269, 115), B4(200, 105), O4(168, 75), bridge O5(269, 75)
    pts_B = [(200, 45), (338, 45), (338, 105), (200, 105)]
    pts_O = [(269, 35), (370, 75), (269, 115), (168, 75)]

    # Draw Ring bonds
    g.bond((200, 45), (269, 35)); g.bond((269, 35), (338, 45))
    g.bond((338, 45), (370, 75)); g.bond((370, 75), (338, 105))
    g.bond((338, 105), (269, 115)); g.bond((269, 115), (200, 105))
    g.bond((200, 105), (168, 75)); g.bond((168, 75), (200, 45))

    # Cross bridge oxygen between B4 and B2 (or B1 and B3)
    g.bond((200, 45), (269, 75), color=RED); g.bond((269, 75), (338, 105), color=RED)

    # Labels
    g.circle((269, 75), 7, fill=PAPER, color=RED); g.text(269, 78, "O", color=RED, size=8.0)
    for p in pts_O:
        g.circle(p, 6, fill=PAPER, color=NAVY); g.text(p[0], p[1]+3, "O", color=NAVY, size=7.5)
    for i, p in enumerate(pts_B):
        is_sp3 = (i in (0, 2))
        c = RED if is_sp3 else TEAL
        g.circle(p, 8, fill=PAPER, color=c)
        g.text(p[0], p[1]+3, "B-", color=RED, size=8.0) if is_sp3 else g.text(p[0], p[1]+3, "B", color=TEAL, size=8.0)
        # OH groups
        dx = -25 if p[0] < 269 else 25
        dy = -15 if p[1] < 75 else 15
        g.bond(p, (p[0]+dx, p[1]+dy))
        g.text(p[0]+dx+ (6 if dx>0 else -6), p[1]+dy+3, "OH", size=7.2)

    g.text(269, 138, "[B4O5(OH)4]2- : Two sp2 B (planar) + Two sp3 B- (tetrahedral) + 5 B-O-B bridges", color=NAVY, size=7.8)


def fig_silicate_types(page, x, y, w, h):
    """Silicate structural units: Ortho, Pyro, Cyclic, Chain."""
    g = Pen(page, x, y, w, h, 538, 140)
    # (a) Ortho SiO4 4-
    g.poly([(80, 40), (45, 95), (115, 95)], color=TEAL, fill=PAPER, close=True)
    g.circle((80, 75), 4, fill=RED, color=RED) # Si inside
    g.text(80, 115, "Orthosilicate", color=TEAL, size=8.0)
    g.text(80, 128, "SiO4 4- (0 shared O)", color=NAVY, size=7.2)

    # (b) Pyro Si2O7 6-
    g.poly([(200, 40), (165, 95), (235, 95)], color=TEAL, fill=PAPER, close=True)
    g.poly([(270, 40), (235, 95), (305, 95)], color=TEAL, fill=PAPER, close=True)
    g.circle((235, 95), 4, fill=RED, color=RED) # shared O
    g.text(235, 115, "Pyrosilicate", color=TEAL, size=8.0)
    g.text(235, 128, "Si2O7 6- (1 shared O)", color=NAVY, size=7.2)

    # (c) Cyclic / Ring (Si3O9 6-)
    g.poly([(430, 30), (395, 75), (465, 75)], color=TEAL, fill=PAPER, close=True)
    g.poly([(395, 75), (360, 115), (430, 115)], color=TEAL, fill=PAPER, close=True)
    g.poly([(465, 75), (430, 115), (500, 115)], color=TEAL, fill=PAPER, close=True)
    g.text(430, 128, "Cyclic (Si3O9 6-) / Chain (SiO3 2-)n : 2 shared O/tetrahedron", color=NAVY, size=7.5)


def fig_p4_allotropes(page, x, y, w, h):
    """White P4 tetrahedral vs Red P polymeric chain."""
    g = Pen(page, x, y, w, h, 538, 130)
    # White P4 tetrahedron at left
    pts = [(120, 30), (70, 95), (170, 95), (120, 75)]
    g.bond(pts[0], pts[1]); g.bond(pts[0], pts[2]); g.bond(pts[0], pts[3])
    g.bond(pts[1], pts[2]); g.bond(pts[1], pts[3]); g.bond(pts[2], pts[3])
    for p in pts:
        g.circle(p, 5, fill=PAPER, color=RED); g.text(p[0], p[1]+3, "P", color=RED, size=7.5)
    g.text(120, 112, "White P4 (discrete)", color=RED, size=8.0)
    g.text(120, 124, "Bond angle 60 deg (high strain)", color=NAVY, size=7.0)

    # Red P chain at right
    for offset in (280, 370, 460):
        p1 = (offset, 45); p2 = (offset-30, 85); p3 = (offset+30, 85); p4 = (offset, 70)
        g.bond(p1, p2); g.bond(p1, p3); g.bond(p1, p4); g.bond(p2, p4); g.bond(p3, p4)
        for p in (p1, p2, p3, p4):
            g.circle(p, 4, fill=PAPER, color=TEAL); g.text(p[0], p[1]+2, "P", color=TEAL, size=6.5)
    g.bond((280+30, 85), (370-30, 85), color=RED, width=1.5)
    g.bond((370+30, 85), (460-30, 85), color=RED, width=1.5)
    g.text(370, 112, "Red Phosphorus (polymeric chain of P4 units)", color=TEAL, size=8.0)
    g.text(370, 124, "Opened P-P bridge link, non-toxic, insoluble, inert", color=NAVY, size=7.0)


def fig_p4o10_cage(page, x, y, w, h):
    """P4O6 and P4O10 Adamantane-like cage structures."""
    g = Pen(page, x, y, w, h, 538, 140)
    # 4 P atoms at tetrahedral vertices (180, 35), (120, 95), (240, 95), (180, 75)
    # Bridging O on all 6 edges, terminal =O on all 4 P in P4O10
    g.text(180, 15, "P4O6 (6 P-O-P bridges)", color=TEAL, size=8.0)
    pts_P = [(180, 35), (120, 95), (240, 95), (180, 75)]
    for i in range(4):
        for j in range(i+1, 4):
            g.bond(pts_P[i], pts_P[j], color=NAVY)
    for p in pts_P:
        g.circle(p, 6, fill=PAPER, color=TEAL); g.text(p[0], p[1]+3, "P", color=TEAL, size=7.5)

    g.text(380, 15, "P4O10 (6 bridges + 4 terminal P=O)", color=RED, size=8.0)
    pts_P2 = [(380, 35), (320, 95), (440, 95), (380, 75)]
    for i in range(4):
        for j in range(i+1, 4):
            g.bond(pts_P2[i], pts_P2[j], color=NAVY)
    for p in pts_P2:
        g.circle(p, 6, fill=PAPER, color=RED); g.text(p[0], p[1]+3, "P", color=RED, size=7.5)
        # terminal O
        dy = -15 if p[1]<50 else 15
        g.bond(p, (p[0], p[1]+dy), color=RED, width=1.5)
        g.text(p[0], p[1]+dy+(3 if dy>0 else -2), "=O", color=RED, size=7.0)
    g.text(269, 130, "Each P in P4O10 is sp3 tetrahedral; 16 total P-O bonds (6 bridging P-O-P + 4 P=O)", color=NAVY, size=7.5)


def fig_sulfur_crown(page, x, y, w, h):
    """S8 Puckered Crown Ring Structure."""
    g = Pen(page, x, y, w, h, 538, 130)
    # Crown ring 8 vertices: 4 top, 4 bottom
    top_pts = [(170, 45), (230, 45), (310, 45), (370, 45)]
    bot_pts = [(140, 85), (200, 85), (280, 85), (340, 85)]
    order = [bot_pts[0], top_pts[0], bot_pts[1], top_pts[1], bot_pts[2], top_pts[2], bot_pts[3], top_pts[3]]
    for i in range(8):
        g.bond(order[i], order[(i+1)%8], color=GOLD, width=1.5)
    for p in order:
        g.circle(p, 6, fill=PAPER, color=GOLD); g.text(p[0], p[1]+3, "S", color=NAVY, size=7.5)
    g.text(269, 110, "S8 Crown Ring (D4d symmetry)", color=TEAL, size=8.5)
    g.text(269, 122, "S-S bond length = 204 pm, S-S-S bond angle = 107 deg", color=NAVY, size=7.5)


def fig_xenon_fluorides(page, x, y, w, h):
    """XeF2, XeF4, XeF6 VSEPR geometries."""
    g = Pen(page, x, y, w, h, 538, 130)
    # XeF2: Linear (sp3d, 3 equatorial lp)
    g.circle((100, 60), 9, fill=PAPER, color=TEAL); g.text(100, 64, "Xe", color=TEAL, size=8.0)
    g.bond((100, 51), (100, 25)); g.text(100, 20, "F", color=NAVY, size=7.5)
    g.bond((100, 69), (100, 95)); g.text(100, 102, "F", color=NAVY, size=7.5)
    g.text(100, 118, "XeF2 (Linear)", color=TEAL, size=7.5)
    g.text(100, 126, "sp3d (3 lp eq)", color=NAVY, size=6.8)

    # XeF4: Square Planar (sp3d2, 2 axial lp)
    g.circle((269, 60), 9, fill=PAPER, color=TEAL); g.text(269, 64, "Xe", color=TEAL, size=8.0)
    pts = [(235, 40), (303, 40), (303, 80), (235, 80)]
    for p in pts:
        g.bond((269, 60), p); g.text(p[0], p[1]+3, "F", color=NAVY, size=7.2)
    g.text(269, 118, "XeF4 (Sq Planar)", color=TEAL, size=7.5)
    g.text(269, 126, "sp3d2 (2 lp ax)", color=NAVY, size=6.8)

    # XeF6: Distorted Octahedral (sp3d3, 1 fluxional lp)
    g.circle((440, 60), 9, fill=PAPER, color=RED); g.text(440, 64, "Xe", color=RED, size=8.0)
    pts6 = [(410, 40), (470, 40), (405, 75), (475, 75), (440, 25), (440, 95)]
    for p in pts6:
        g.bond((440, 60), p, color=RED); g.text(p[0], p[1]+3, "F", color=NAVY, size=7.0)
    g.text(440, 118, "XeF6 (Dist. Octahedral)", color=RED, size=7.5)
    g.text(440, 126, "sp3d3 (1 sterically active lp)", color=NAVY, size=6.8)


# Update REGISTRY
REGISTRY.update({
    "diborane": (fig_diborane, 0.22),
    "borax": (fig_borax_anion, 0.24),
    "silicates": (fig_silicate_types, 0.22),
    "phosphorus": (fig_p4_allotropes, 0.22),
    "p4o10": (fig_p4o10_cage, 0.23),
    "sulfur": (fig_sulfur_crown, 0.22),
    "xenon": (fig_xenon_fluorides, 0.22),
})

# ===========================================================================
# Chemical Bonding Specific Diagrams & Figures
# ===========================================================================

def fig_born_haber(page, x, y, w, h):
    """Born-Haber Cycle for NaCl formation energy components."""
    g = Pen(page, x, y, w, h, 538, 140)
    # Energy levels / cycle boxes
    # Ground elements at bottom left: Na(s) + 1/2 Cl2(g) -> (80, 110)
    g.text(100, 115, "Na(s) + 1/2 Cl2(g)", color=NAVY, size=8.5)

    # Sublimation: Na(s) -> Na(g) (ΔH_sub = +108 kJ)
    g.arrow((100, 105), (100, 75), color=TEAL)
    g.text(60, 90, "+ΔH_sub", color=TEAL, size=7.5)
    g.text(100, 70, "Na(g) + 1/2 Cl2(g)", color=NAVY, size=8.0)

    # Ionization: Na(g) -> Na+(g) (IE = +496 kJ)
    g.arrow((100, 60), (100, 25), color=TEAL)
    g.text(60, 42, "+IE", color=TEAL, size=7.5)
    g.text(100, 20, "Na+(g) + 1/2 Cl2(g)", color=NAVY, size=8.0)

    # Bond Dissociation: 1/2 Cl2 -> Cl(g) (+1/2 ΔH_diss = +121 kJ)
    g.arrow((165, 20), (250, 20), color=TEAL)
    g.text(205, 12, "+1/2 ΔH_diss", color=TEAL, size=7.5)
    g.text(300, 20, "Na+(g) + Cl(g)", color=NAVY, size=8.0)

    # Electron Gain: Cl(g) -> Cl-(g) (ΔH_eg = -349 kJ)
    g.arrow((360, 20), (430, 45), color=RED)
    g.text(410, 28, "ΔH_eg (exothermic)", color=RED, size=7.5)
    g.text(450, 50, "Na+(g) + Cl-(g)", color=NAVY, size=8.5)

    # Lattice Energy: Na+(g) + Cl-(g) -> NaCl(s) (U = -788 kJ)
    g.arrow((450, 60), (450, 105), color=RED)
    g.text(475, 82, "U_lattice (-788 kJ)", color=RED, size=8.0)

    # Product at bottom right: NaCl(s)
    g.text(450, 115, "NaCl(s) [Lattice]", color=TEAL, size=8.5)

    # Direct formation enthalpy
    g.arrow((180, 115), (380, 115), color=NAVY)
    g.text(280, 128, "ΔH°_f = ΔH_sub + IE + 1/2 D + ΔH_eg + U_latt = -411 kJ/mol", color=NAVY, size=7.8)


def fig_fajans_polarization(page, x, y, w, h):
    """Fajans' Polarization: Cation polarizes deformable electron cloud of Anion."""
    g = Pen(page, x, y, w, h, 538, 130)
    # 1. Pure Ionic (left): spherical cation + spherical anion
    g.circle((80, 60), 12, fill=PAPER, color=TEAL)
    g.text(80, 63, "M+", color=TEAL, size=8.0)
    g.circle((140, 60), 25, fill=PAPER, color=NAVY)
    g.text(140, 63, "X-", color=NAVY, size=8.0)
    g.text(110, 105, "Pure Ionic (spherical clouds)", color=TEAL, size=7.8)

    # Transition arrow
    g.arrow((190, 60), (250, 60), color=RED)
    g.text(220, 48, "Polarization", color=RED, size=7.5)

    # 2. Polarized Covalent Character (right): tiny cation + distorted oval anion
    g.circle((310, 60), 9, fill=PAPER, color=RED)
    g.text(310, 63, "M+", color=RED, size=7.5)

    # Distorted anion cloud pulled towards cation
    g.poly([(335, 60), (350, 40), (395, 42), (405, 60), (395, 78), (350, 80)], color=RED, fill=PAPER, close=True)
    g.text(375, 63, "X- (distorted)", color=RED, size=7.8)
    g.text(350, 105, "Electron density shared -> Covalent character", color=RED, size=7.8)
    g.text(350, 118, "Lower M.P., decreased solubility in water, intense colour", color=NAVY, size=7.2)


def fig_vsepr_shapes(page, x, y, w, h):
    """VSEPR Key Geometries: Bent (H2O), Trigonal Pyramidal (NH3), See-Saw (SF4), T-shaped (ClF3)."""
    g = Pen(page, x, y, w, h, 538, 140)
    # (a) Bent H2O at (70, 60)
    g.circle((70, 50), 9, fill=PAPER, color=TEAL); g.text(70, 53, "O", color=TEAL, size=8.0)
    g.bond((70, 50), (45, 85)); g.text(40, 90, "H", color=NAVY, size=7.5)
    g.bond((70, 50), (95, 85)); g.text(100, 90, "H", color=NAVY, size=7.5)
    # 2 lone pairs
    g.circle((60, 28), 4, color=RED); g.circle((80, 28), 4, color=RED)
    g.text(70, 110, "Bent (H2O)", color=TEAL, size=8.0)
    g.text(70, 122, "104.5° (2 lp)", color=NAVY, size=7.0)

    # (b) Trigonal Pyramidal NH3 at (190, 60)
    g.circle((190, 45), 9, fill=PAPER, color=TEAL); g.text(190, 48, "N", color=TEAL, size=8.0)
    g.circle((190, 25), 4, color=RED) # 1 lp
    g.bond((190, 45), (165, 85)); g.text(160, 90, "H", size=7.5)
    g.bond((190, 45), (190, 90)); g.text(190, 96, "H", size=7.5)
    g.bond((190, 45), (215, 85)); g.text(220, 90, "H", size=7.5)
    g.text(190, 110, "Pyramidal (NH3)", color=TEAL, size=8.0)
    g.text(190, 122, "107.8° (1 lp)", color=NAVY, size=7.0)

    # (c) See-Saw SF4 at (320, 60)
    g.circle((320, 60), 9, fill=PAPER, color=TEAL); g.text(320, 63, "S", color=TEAL, size=8.0)
    g.circle((295, 60), 4, color=RED) # eq lp
    g.bond((320, 60), (320, 20)); g.text(320, 15, "F(ax)", size=7.0)
    g.bond((320, 60), (320, 100)); g.text(320, 106, "F(ax)", size=7.0)
    g.bond((320, 60), (350, 45)); g.text(355, 45, "F(eq)", size=7.0)
    g.bond((320, 60), (350, 75)); g.text(355, 78, "F(eq)", size=7.0)
    g.text(320, 118, "See-Saw (SF4)", color=TEAL, size=8.0)
    g.text(320, 128, "sp3d (1 lp eq)", color=NAVY, size=7.0)

    # (d) T-Shaped ClF3 at (450, 60)
    g.circle((450, 60), 9, fill=PAPER, color=TEAL); g.text(450, 63, "Cl", color=TEAL, size=8.0)
    g.circle((430, 45), 4, color=RED); g.circle((430, 75), 4, color=RED) # 2 eq lp
    g.bond((450, 60), (450, 20)); g.text(450, 15, "F(ax)", size=7.0)
    g.bond((450, 60), (450, 100)); g.text(450, 106, "F(ax)", size=7.0)
    g.bond((450, 60), (485, 60)); g.text(492, 63, "F(eq)", size=7.0)
    g.text(450, 118, "T-Shaped (ClF3)", color=TEAL, size=8.0)
    g.text(450, 128, "sp3d (2 lp eq)", color=NAVY, size=7.0)


def fig_mot_o2_n2(page, x, y, w, h):
    """Molecular Orbital Energy Level Diagram: O2 vs N2 (s-p mixing crossover)."""
    g = Pen(page, x, y, w, h, 538, 140)
    # Left: N2, B2, C2 (< 14 valence electrons, s-p mixing occurs)
    g.text(140, 15, "B2, C2, N2 (≤ 14 e-): s-p mixing active", color=TEAL, size=8.2)
    # Energy levels bottom to top
    g.line((90, 110), (190, 110)); g.text(205, 112, "σ(2s)", size=7.2)
    g.line((90, 95), (190, 95)); g.text(205, 97, "σ*(2s)", size=7.2)
    # π(2px) = π(2py) LOWER than σ(2pz)
    g.line((70, 75), (120, 75), color=RED, width=1.5)
    g.line((140, 75), (190, 75), color=RED, width=1.5)
    g.text(205, 77, "π(2px) = π(2py) [LOWER]", color=RED, size=7.2)
    g.line((90, 58), (190, 58)); g.text(205, 60, "σ(2pz) [Pushed up]", size=7.2)
    g.line((70, 42), (120, 42)); g.line((140, 42), (190, 42))
    g.text(205, 44, "π*(2px) = π*(2py)", size=7.2)
    g.line((90, 28), (190, 28)); g.text(205, 30, "σ*(2pz)", size=7.2)

    # Right: O2, F2 (> 14 valence electrons, normal order)
    g.text(390, 15, "O2, F2 (> 14 e-): Normal order (no s-p mix)", color=NAVY, size=8.2)
    g.line((340, 110), (440, 110)); g.text(455, 112, "σ(2s)", size=7.2)
    g.line((340, 95), (440, 95)); g.text(455, 97, "σ*(2s)", size=7.2)
    # σ(2pz) LOWER than π(2px)=π(2py)
    g.line((340, 78), (440, 78), color=TEAL, width=1.5)
    g.text(455, 80, "σ(2pz) [LOWER]", color=TEAL, size=7.2)
    g.line((320, 62), (370, 62)); g.line((390, 62), (440, 62))
    g.text(455, 64, "π(2px) = π(2py)", size=7.2)
    g.line((320, 42), (370, 42), color=RED, width=1.5); g.line((390, 42), (440, 42), color=RED, width=1.5)
    g.text(455, 44, "π*(2px) = π*(2py) [2 unpaired in O2!]", color=RED, size=7.2)
    g.line((340, 28), (440, 28)); g.text(455, 30, "σ*(2pz)", size=7.2)


def fig_h_bonding(page, x, y, w, h):
    """Hydrogen Bonding: Intermolecular (ice/H2O) vs Intramolecular (o-nitrophenol)."""
    g = Pen(page, x, y, w, h, 538, 130)
    # (a) Intermolecular in Ice (tetrahedral network) at left (130, 60)
    g.circle((130, 60), 10, fill=PAPER, color=TEAL); g.text(130, 63, "O", color=TEAL, size=8.0)
    g.bond((130, 60), (105, 40)); g.text(100, 38, "H", size=7.2)
    g.bond((130, 60), (155, 40)); g.text(160, 38, "H", size=7.2)
    # H-bond dashes
    g.dash((130, 60), (130, 100), color=RED)
    g.circle((130, 108), 8, fill=PAPER, color=TEAL); g.text(130, 111, "O", color=TEAL, size=7.0)
    g.dash((100, 38), (70, 25), color=RED)
    g.text(130, 15, "Intermolecular H-Bonding (Ice Cage)", color=TEAL, size=8.0)
    g.text(130, 125, "Density: Ice < Water (Open cage collapse at 4°C)", color=NAVY, size=7.2)

    # (b) Intramolecular in o-Nitrophenol at right (380, 60)
    # Benzene ring at (350, 60)
    pts = [(330, 60), (340, 42), (360, 42), (370, 60), (360, 78), (340, 78)]
    for i in range(6): g.bond(pts[i], pts[(i+1)%6])
    g.circle((350, 60), 8, stroke=NAVY)
    # -OH at C1
    g.bond((360, 42), (380, 30)); g.text(388, 28, "O", color=TEAL, size=7.5)
    g.bond((388, 28), (408, 30)); g.text(414, 30, "H", color=NAVY, size=7.5)
    # -NO2 at C2
    g.bond((370, 60), (395, 65)); g.text(403, 67, "N", color=RED, size=7.5)
    g.bond((403, 67), (420, 80)); g.text(426, 83, "O-", color=NAVY, size=7.2)
    g.bond((403, 67), (418, 52), order=2); g.text(425, 52, "O", color=RED, size=7.2)
    # Intramolecular chelation ring H-bond
    g.dash((414, 30), (425, 48), color=RED)
    g.text(390, 105, "Intramolecular H-Bonding (Chelation)", color=RED, size=8.0)
    g.text(390, 118, "Steam volatile, lower BP, weaker acid than p-isomer", color=NAVY, size=7.2)


# Update REGISTRY
REGISTRY.update({
    "bornhaber": (fig_born_haber, 0.26),
    "fajans": (fig_fajans_polarization, 0.24),
    "vsepr": (fig_vsepr_shapes, 0.26),
    "mot": (fig_mot_o2_n2, 0.26),
    "hbonding": (fig_h_bonding, 0.24),
})
