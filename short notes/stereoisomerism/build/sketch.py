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
        s = (s.replace("**", "")
              .replace("-->", "\u2192").replace("->", "\u2192")
              .replace("<===>", "\u21cc").replace("===>", "\u2192").replace("<===", "\u2190"))
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
# Visual Enhancements: Stereoisomerism New Chemical Figures
# ===========================================================================

def fig_sawhorse(page, x, y, w, h):
    """Sawhorse projection comparison: Staggered vs Eclipsed."""
    g = Pen(page, x, y, w, h, 538, 140)
    # Staggered (left, C1=(120, 100), C2=(200, 45))
    g.bond((120, 100), (200, 45), color=NAVY, order=1)
    # C1 bonds (pointing down, left-up, right-up)
    g.bond((120, 100), (120, 130)); g.text(120, 137, "H", color=NAVY, size=7.8)
    g.bond((120, 100), (80, 85)); g.text(72, 85, "H", color=NAVY, size=7.8)
    g.bond((120, 100), (155, 115)); g.text(163, 118, "H", color=NAVY, size=7.8)
    # C2 bonds (staggered: pointing up, left-down, right-down)
    g.bond((200, 45), (200, 15)); g.text(200, 10, "H", color=NAVY, size=7.8)
    g.bond((200, 45), (165, 30)); g.text(157, 30, "H", color=NAVY, size=7.8)
    g.bond((200, 45), (240, 60)); g.text(248, 62, "H", color=NAVY, size=7.8)
    g.text(160, 135, "Staggered Sawhorse (anti 180°)", color=TEAL, size=8.0)

    # Eclipsed (right, C1=(340, 100), C2=(420, 45))
    g.bond((340, 100), (420, 45), color=NAVY, order=1)
    # C1 bonds (pointing up, left, right)
    g.bond((340, 100), (340, 130)); g.text(340, 137, "H", color=NAVY, size=7.8)
    g.bond((340, 100), (300, 85)); g.text(292, 85, "H", color=NAVY, size=7.8)
    g.bond((340, 100), (375, 115)); g.text(383, 118, "H", color=NAVY, size=7.8)
    # C2 bonds (parallel/eclipsed)
    g.bond((420, 45), (420, 75)); g.text(420, 82, "H", color=NAVY, size=7.8)
    g.bond((420, 45), (380, 30)); g.text(372, 30, "H", color=NAVY, size=7.8)
    g.bond((420, 45), (455, 60)); g.text(463, 62, "H", color=NAVY, size=7.8)
    g.text(380, 135, "Eclipsed Sawhorse (syn 0°)", color=RED, size=8.0)


def fig_biphenyl(page, x, y, w, h):
    """Substituted Biphenyl with restricted rotation (Atropisomerism)."""
    g = Pen(page, x, y, w, h, 538, 140)
    # Left ring (vertical plane, drawn as vertical ellipse / hexagon)
    # Center (180, 70)
    pts1 = [(150, 70), (165, 45), (195, 45), (210, 70), (195, 95), (165, 95)]
    for i in range(6):
        g.bond(pts1[i], pts1[(i+1)%6])
    # Inner double bonds
    g.circle((180, 70), 12, stroke=NAVY)

    # Central pivot C-C single bond
    g.bond((210, 70), (270, 70), color=NAVY, order=1)

    # Right ring (perpendicular horizontal plane)
    pts2 = [(270, 70), (295, 58), (325, 58), (345, 70), (325, 82), (295, 82)]
    for i in range(6):
        g.bond(pts2[i], pts2[(i+1)%6])
    g.circle((310, 70), 8, stroke=NAVY)

    # Bulky ortho substituents on left ring
    g.bond((165, 45), (150, 25)); g.text(140, 22, "NO2", color=RED, size=8.0)
    g.bond((165, 95), (150, 115)); g.text(140, 120, "COOH", color=TEAL, size=8.0)

    # Bulky ortho substituents on right ring
    g.bond((295, 58), (295, 30)); g.text(295, 24, "COOH", color=TEAL, size=8.0)
    g.bond((295, 82), (295, 110)); g.text(295, 118, "NO2", color=RED, size=8.0)

    # Annotations
    g.text(440, 50, "Orthogonal Rings", color=TEAL, size=8.5)
    g.text(440, 65, "Steric clash prevents", color=NAVY, size=7.5)
    g.text(440, 77, "planar rotation (barrier", color=NAVY, size=7.5)
    g.text(440, 89, "> 100 kJ/mol). Chiral!", color=RED, size=8.0)


def fig_boat_chair(page, x, y, w, h):
    """Cyclohexane: Chair vs Boat with Flagpole Interactions."""
    g = Pen(page, x, y, w, h, 538, 140)
    # Chair at left (130, 70)
    pts_c = [(90, 65), (120, 45), (160, 60), (160, 95), (130, 115), (90, 100)]
    for i in range(6):
        g.bond(pts_c[i], pts_c[(i+1)%6])
    g.text(125, 25, "Chair Form (staggered)", color=TEAL, size=8.2)
    g.text(125, 132, "ΔG = 0 kJ/mol (Most stable)", color=NAVY, size=7.5)

    # Boat at right (370, 70)
    pts_b = [(320, 55), (350, 90), (390, 90), (420, 55), (380, 55), (360, 55)]
    # Standard boat contour: C1(330, 50), C2(360, 85), C3(400, 85), C4(430, 50), C5(390, 50), C6(370, 50)
    g.bond((330, 50), (360, 85)); g.bond((360, 85), (400, 85)); g.bond((400, 85), (430, 50))
    g.bond((430, 50), (410, 35)); g.bond((410, 35), (350, 35)); g.bond((350, 35), (330, 50))
    # Flagpole hydrogens at C1 and C4
    g.bond((350, 35), (365, 18), color=RED); g.text(368, 14, "H (flagpole)", color=RED, size=7.2)
    g.bond((410, 35), (395, 18), color=RED); g.text(392, 14, "H (flagpole)", color=RED, size=7.2)
    g.dash((368, 18), (392, 18), color=RED)
    g.text(380, 105, "Boat Form (eclipsed + flagpole clash)", color=RED, size=8.0)
    g.text(380, 118, "ΔG ≈ +29 kJ/mol (Unstable)", color=NAVY, size=7.5)


def fig_sn2_inversion(page, x, y, w, h):
    """Walden Inversion in SN2 Reaction (Umbrella Inversion)."""
    g = Pen(page, x, y, w, h, 538, 140)
    # Reactant (R) at left (100, 70)
    g.text(80, 35, "(R)-Substrate", color=NAVY, size=8.0)
    g.circle((100, 70), 5, fill=NAVY)
    g.bond((100, 70), (140, 70)); g.text(148, 73, "Br", color=RED, size=8.0)
    g.bond((100, 70), (80, 45)); g.text(72, 43, "R1", color=NAVY, size=7.5)
    g.bond((100, 70), (80, 95), stereo="wedge"); g.text(72, 100, "R2", color=NAVY, size=7.5)
    g.bond((100, 70), (60, 70), stereo="hash"); g.text(50, 73, "H", color=NAVY, size=7.5)

    # Incoming Nu- from backside
    g.arrow((180, 70), (220, 70), color=TEAL)
    g.text(200, 60, "Backside attack", color=TEAL, size=7.5)

    # Transition State (270, 70)
    g.text(270, 25, "Pentacoordinate T.S. [Nu...C...Br]", color=TEAL, size=8.0)
    g.circle((270, 70), 4, fill=NAVY)
    g.dash((235, 70), (266, 70), color=TEAL); g.text(225, 73, "OH-", color=TEAL, size=7.5)
    g.dash((274, 70), (305, 70), color=RED); g.text(312, 73, "Br-", color=RED, size=7.5)
    g.bond((270, 70), (270, 40)); g.text(270, 35, "R1", size=7.5)
    g.bond((270, 70), (255, 95), stereo="wedge"); g.text(250, 102, "R2", size=7.5)
    g.bond((270, 70), (285, 95), stereo="hash"); g.text(288, 102, "H", size=7.5)

    # Inverted Product (S) at right (440, 70)
    g.arrow((340, 70), (380, 70), color=TEAL)
    g.text(440, 35, "(S)-Inverted Product (100% Inversion)", color=RED, size=8.0)
    g.circle((440, 70), 5, fill=NAVY)
    g.bond((440, 70), (400, 70), color=TEAL); g.text(390, 73, "HO", color=TEAL, size=8.0)
    g.bond((440, 70), (460, 45)); g.text(468, 43, "R1", color=NAVY, size=7.5)
    g.bond((440, 70), (460, 95), stereo="wedge"); g.text(468, 100, "R2", color=NAVY, size=7.5)
    g.bond((440, 70), (480, 70), stereo="hash"); g.text(490, 73, "H", color=NAVY, size=7.5)


# Update REGISTRY
REGISTRY.update({
    "sawhorse": (fig_sawhorse, 0.26),
    "biphenyl": (fig_biphenyl, 0.26),
    "boatchair": (fig_boat_chair, 0.26),
    "sn2": (fig_sn2_inversion, 0.26),
})
