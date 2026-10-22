"""Custom vector chemical diagrams and physical schematics for d- and f-Block Elements."""
from __future__ import annotations

import math

# Color palette matching short notes style
NAVY = (0.05, 0.16, 0.28)
TEAL = (0.0, 0.47, 0.42)
GOLD = (0.85, 0.55, 0.13)
RED = (0.75, 0.15, 0.15)
GRAY = (0.55, 0.60, 0.65)
LIGHT_BG = (0.95, 0.97, 0.98)
PAPER = (1.0, 1.0, 1.0)


class Pen:
    def __init__(self, page, x, y, w, h, vx=538, vy=110):
        self.p = page
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vx = vx
        self.vy = vy
        self.sx = w / vx
        self.sy = h / vy

    def tx(self, px):
        return self.x + px * self.sx

    def ty(self, py):
        return self.y + py * self.sy

    def line(self, p1, p2, color=NAVY, width=1.0, dashes=None):
        import fitz
        p1_t = fitz.Point(self.tx(p1[0]), self.ty(p1[1]))
        p2_t = fitz.Point(self.tx(p2[0]), self.ty(p2[1]))
        if dashes:
            self.p.draw_line(p1_t, p2_t, color=color, width=width, dashes=dashes)
        else:
            self.p.draw_line(p1_t, p2_t, color=color, width=width)

    def rect(self, r, fill=None, color=NAVY, width=1.0):
        import fitz
        r_t = fitz.Rect(self.tx(r[0]), self.ty(r[1]), self.tx(r[0] + r[2]), self.ty(r[1] + r[3]))
        self.p.draw_rect(r_t, fill=fill, color=color, width=width)

    def circle(self, c, r, fill=None, color=NAVY, width=1.0):
        import fitz
        c_t = fitz.Point(self.tx(c[0]), self.ty(c[1]))
        self.p.draw_circle(c_t, r * self.sx, fill=fill, color=color, width=width)

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

    def text(self, x, y, txt, font="kalam-bold", size=7.5, color=NAVY, align="center"):
        from textkit import draw_text, glyph_runs, width
        s = (txt.replace("**", "")
                .replace("-->", "→").replace("->", "→")
                .replace("<===>", "⇌").replace("===>", "→").replace("<===", "←"))
        parts = []
        for t, mode in self._runs(s):
            sz = size * (1.0 if mode == 0 else 0.64)
            dy = 0.0 if mode == 0 else (0.20 * size if mode == -1 else -0.40 * size)
            for k, seg in glyph_runs(t, "kalam-b"):
                parts.append((k, seg, sz, dy))
        total = sum(width(seg, k, sz) for k, seg, sz, _ in parts)
        cx = self.tx(x)
        if align == "center":
            cx -= total / 2
        elif align == "right":
            cx -= total
        by = self.ty(y)
        for k, seg, sz, dy in parts:
            draw_text(self.p, cx, by + dy * self.sy, seg, k, sz, color)
            cx += width(seg, k, sz)


def fig_lanthanoid_contraction(page, x, y, w, h):
    """Atomic Radii curve showing 3d -> 4d increase, and 4d ~ 5d overlap due to Lanthanoid Contraction."""
    g = Pen(page, x, y, w, h, 538, 120)
    g.rect((5, 5, 528, 110), fill=LIGHT_BG, color=TEAL, width=1.0)

    # Plot axes
    g.line((50, 95), (280, 95), color=NAVY, width=1.2) # X: Group (3 to 12)
    g.line((50, 15), (50, 95), color=NAVY, width=1.2)  # Y: Metallic Radius (pm)
    g.text(45, 12, "Radius (pm)", color=NAVY, size=6.5)
    g.text(160, 103, "Transition Group → (Sc/Ti/V to Zn/Cd/Hg)", color=NAVY, size=6.0)

    # Y ticks: 130 to 180 pm
    g.text(45, 80, "130", color=GRAY, size=5.5)
    g.text(45, 50, "155", color=GRAY, size=5.5)
    g.text(45, 25, "180", color=GRAY, size=5.5)

    # 3d series curve (lowest)
    pts_3d = [(55, 35), (80, 65), (110, 75), (140, 80), (170, 82), (200, 82), (230, 80), (260, 75)]
    for i in range(len(pts_3d)-1):
        g.line(pts_3d[i], pts_3d[i+1], color=NAVY, width=1.2)
    g.text(265, 78, "3d Series (Sc→Zn)", color=NAVY, size=5.5)

    # 4d series curve (higher)
    pts_4d = [(55, 20), (80, 45), (110, 55), (140, 60), (170, 62), (200, 62), (230, 60), (260, 56)]
    for i in range(len(pts_4d)-1):
        g.line(pts_4d[i], pts_4d[i+1], color=TEAL, width=1.5)
    g.text(265, 48, "4d (Y→Cd)", color=TEAL, size=5.5)

    # 5d series curve (IDENTICAL/OVERLAPPING WITH 4d due to 4f contraction!)
    pts_5d = [(55, 18), (80, 46), (110, 56), (140, 61), (170, 62), (200, 62), (230, 59), (260, 54)]
    for i in range(len(pts_5d)-1):
        g.line(pts_5d[i], pts_5d[i+1], color=RED, width=1.2, dashes=[3, 2])
    g.text(265, 60, "5d (La→Hg)", color=RED, size=5.5)

    # Highlight twin pairs
    g.circle((80, 45.5), 4, fill=PAPER, color=GOLD)
    g.text(80, 38, "Zr(160) ≈ Hf(159)!", color=GOLD, size=6.0)
    g.circle((110, 55.5), 4, fill=PAPER, color=GOLD)
    g.text(110, 48, "Nb ≈ Ta (146 pm)", color=GOLD, size=6.0)

    # Right explanatory box
    g.rect((300, 12, 225, 96), fill=PAPER, color=TEAL, width=1.0)
    g.text(412, 22, "Lanthanoid Contraction (NCERT §8.3.2)", color=TEAL, size=7.2)
    g.text(412, 34, "• **Poor Shielding of 4f Electrons:**", color=NAVY, size=6.2)
    g.text(412, 44, "  Intervening 14 Ce-Lu electrons have diffuse", color=NAVY, size=5.8)
    g.text(412, 53, "  shapes → shielding order: s > p > d > f (worst!).", color=NAVY, size=5.8)
    g.text(412, 64, "• **Z~eff~ Skyrockets:**", color=RED, size=6.2)
    g.text(412, 74, "  Net nuclear pull pulls valence 5d/6s inwards,", color=NAVY, size=5.8)
    g.text(412, 83, "  cancelling expected shell expansion from 4d to 5d!", color=NAVY, size=5.8)
    g.text(412, 94, "• **Consequences:** Zr/Hf, Nb/Ta, Mo/W have", color=TEAL, size=5.8)
    g.text(412, 103, "  identical radii, identical chemistry & high density!", color=RED, size=5.5)


def fig_electrode_potentials(page, x, y, w, h):
    """Thermochemical Cycle for E°(M2+/M) and the anomalous peaks of Cr, Mn, Cu, Zn."""
    g = Pen(page, x, y, w, h, 538, 120)
    g.rect((5, 5, 528, 110), fill=LIGHT_BG, color=TEAL, width=1.0)

    # Thermochemical Born-Haber-like cycle on Left
    g.rect((20, 20, 65, 30), fill=PAPER, color=NAVY, width=1.0)
    g.text(52, 37, "M(s)", color=NAVY, size=7.5)

    g.line((85, 35), (145, 35), color=RED, width=1.2) # Sublimation
    g.text(115, 28, "Δ_sub H° (>0)", color=RED, size=5.8)

    g.rect((145, 20, 65, 30), fill=PAPER, color=NAVY, width=1.0)
    g.text(177, 37, "M(g)", color=NAVY, size=7.5)

    g.line((177, 50), (177, 75), color=GOLD, width=1.2) # Ionization
    g.text(210, 62, "IE~1~ + IE~2~ (>0)", color=GOLD, size=5.8)

    g.rect((145, 75, 65, 30), fill=PAPER, color=NAVY, width=1.0)
    g.text(177, 92, "M^2+^(g)", color=NAVY, size=7.5)

    g.line((145, 90), (85, 90), color=TEAL, width=1.2) # Hydration
    g.text(115, 84, "Δ_hyd H° (<0)", color=TEAL, size=5.8)

    g.rect((20, 75, 65, 30), fill=PAPER, color=TEAL, width=1.0)
    g.text(52, 92, "M^2+^(aq)", color=TEAL, size=7.5)

    # Direct diagonal arrow for E°
    g.line((52, 50), (52, 75), color=NAVY, width=1.5)
    g.text(32, 63, "E°~red~", color=NAVY, size=6.5)

    # Right: Four Anomalous JEE Traps
    g.rect((255, 12, 270, 96), fill=PAPER, color=TEAL, width=1.0)
    g.text(390, 22, "E°(M^2+^/M) Anomalies Explained (NCERT §8.3.5)", color=TEAL, size=7.0)
    g.text(390, 34, "1. **Cu is POSITIVE (+0.34 V):**", color=RED, size=6.2)
    g.text(390, 44, "   High atomisation energy + high (IE~1~+IE~2~) is NOT", color=NAVY, size=5.5)
    g.text(390, 52, "   compensated by hydration enthalpy! Cu cannot displace H~2~.", color=NAVY, size=5.5)
    g.text(390, 63, "2. **Mn is More Negative (−1.18 V):**", color=TEAL, size=6.2)
    g.text(390, 72, "   Half-filled d^5^ stability makes Mn^2+^ extremely stable!", color=NAVY, size=5.5)
    g.text(390, 82, "3. **Zn is More Negative (−0.76 V):**", color=GOLD, size=6.2)
    g.text(390, 91, "   Completely filled d^10^ stability in Zn^2+^.", color=NAVY, size=5.5)
    g.text(390, 101, "4. **E°(M^3+^/M^2+^):** Fe = +0.77 V (d^5^ stable); Mn = +1.57 V (d^4^ to d^5^).", color=NAVY, size=5.2)


def fig_chromate_dichromate(page, x, y, w, h):
    """Structures of Chromate CrO4(2-) (tetrahedral) and Dichromate Cr2O7(2-) (bridged oxo dimer)."""
    g = Pen(page, x, y, w, h, 538, 120)
    g.rect((5, 5, 528, 110), fill=LIGHT_BG, color=TEAL, width=1.0)

    # Left: Yellow Chromate CrO4(2-)
    g.circle((90, 55), 14, fill=PAPER, color=GOLD, width=1.5)
    g.text(90, 58, "Cr", color=GOLD, size=9.0)
    # 4 Oxygens tetrahedral
    pts_cro4 = [(65, 30), (115, 30), (65, 80), (115, 80)]
    for ox, oy in pts_cro4:
        g.circle((ox, oy), 8, fill=PAPER, color=RED)
        g.text(ox, oy+2.5, "O", color=RED, size=6.5)
        g.line((90, 55), (ox, oy), color=GOLD, width=1.2)
    g.text(90, 100, "Chromate [CrO~4~]^2−^", color=GOLD, size=7.2)
    g.text(90, 110, "Yellow, T~d~ symmetry, all Cr-O 166 pm", color=NAVY, size=5.8)

    # Equilibrium Arrow in Center
    g.line((145, 52), (185, 52), color=RED, width=1.5)
    g.line((185, 58), (145, 58), color=GOLD, width=1.5)
    g.text(165, 45, "+ 2 H^+^ (pH < 7)", color=RED, size=6.0)
    g.text(165, 68, "+ 2 OH^−^ (pH > 7)", color=GOLD, size=6.0)

    # Right: Orange Dichromate Cr2O7(2-)
    # Left Cr
    g.circle((230, 55), 12, fill=PAPER, color=RED, width=1.5); g.text(230, 58, "Cr", color=RED, size=8.0)
    # Right Cr
    g.circle((310, 55), 12, fill=PAPER, color=RED, width=1.5); g.text(310, 58, "Cr", color=RED, size=8.0)
    # Bridging Oxygen
    g.circle((270, 42), 8, fill=PAPER, color=TEAL, width=1.2); g.text(270, 44.5, "O", color=TEAL, size=6.5)
    g.line((230, 55), (270, 42), color=NAVY, width=1.2)
    g.line((310, 55), (270, 42), color=NAVY, width=1.2)
    g.text(270, 28, "126° (Cr-O-Cr bridge)", color=TEAL, size=5.8)
    g.text(270, 36, "179 pm (Longer!)", color=GRAY, size=5.2)

    # Terminal Oxygens (3 on each Cr, 163 pm)
    pts_term = [(205, 40), (215, 75), (245, 75), (335, 40), (325, 75), (295, 75)]
    for tx, ty in pts_term:
        g.circle((tx, ty), 6.5, fill=PAPER, color=RED)
        g.text(tx, ty+2.0, "O", color=RED, size=5.5)
        # Bond to parent Cr
        pcr = (230, 55) if tx < 270 else (310, 55)
        g.line(pcr, (tx, ty), color=RED, width=1.0)

    g.text(270, 100, "Dichromate [Cr~2~O~7~]^2−^", color=RED, size=7.2)
    g.text(270, 110, "Orange, 6 terminal Cr-O (163 pm) + 2 bridge (179 pm)", color=NAVY, size=5.8)

    # Extreme Right Key Takeaway Box
    g.rect((370, 12, 155, 96), fill=PAPER, color=TEAL, width=1.0)
    g.text(447, 24, "Acid-Base Switch (NCERT)", color=TEAL, size=6.8)
    g.text(447, 36, "2 CrO~4~^2−^ + 2 H^+^ ⇌ Cr~2~O~7~^2−^ + H~2~O", color=RED, size=5.2)
    g.text(447, 48, "• Acidic medium: ORANGE Cr~2~O~7~^2−^", color=RED, size=5.8)
    g.text(447, 58, "• Basic medium: YELLOW CrO~4~^2−^", color=GOLD, size=5.8)
    g.text(447, 70, "• Oxidation State is +6 in BOTH!", color=NAVY, size=6.0)
    g.text(447, 80, "  NOT a redox reaction!", color=RED, size=6.0)
    g.text(447, 92, "• Diamagnetic (d^0^, no unp e^-).", color=NAVY, size=5.5)
    g.text(447, 102, "  Colour due to LMCT charge transfer!", color=TEAL, size=5.5)


def fig_permanganate_manganate(page, x, y, w, h):
    """Structures of Permanganate MnO4(-) (purple) and Manganate MnO4(2-) (green)."""
    g = Pen(page, x, y, w, h, 538, 120)
    g.rect((5, 5, 528, 110), fill=LIGHT_BG, color=TEAL, width=1.0)

    # Left: Dark Green Manganate [MnO4]2- (paramagnetic, d1)
    g.circle((100, 52), 14, fill=PAPER, color=TEAL, width=1.5)
    g.text(100, 55, "Mn", color=TEAL, size=8.5)
    for ox, oy in [(75, 30), (125, 30), (75, 75), (125, 75)]:
        g.circle((ox, oy), 8, fill=PAPER, color=RED); g.text(ox, oy+2.5, "O", color=RED, size=6.5)
        g.line((100, 52), (ox, oy), color=TEAL, width=1.2)
    g.text(100, 95, "Manganate [MnO~4~]^2−^ (Green)", color=TEAL, size=7.2)
    g.text(100, 106, "Mn(+6), d^1^: PARAMAGNETIC (1 unp e^-)", color=NAVY, size=6.0)

    # Right: Intense Purple Permanganate [MnO4]- (diamagnetic, d0)
    g.circle((270, 52), 14, fill=PAPER, color=(0.5, 0.1, 0.5), width=1.5)
    g.text(270, 55, "Mn", color=(0.5, 0.1, 0.5), size=8.5)
    for ox, oy in [(245, 30), (295, 30), (245, 75), (295, 75)]:
        g.circle((ox, oy), 8, fill=PAPER, color=RED); g.text(ox, oy+2.5, "O", color=RED, size=6.5)
        g.line((270, 52), (ox, oy), color=(0.5, 0.1, 0.5), width=1.2)
    g.text(270, 95, "Permanganate [MnO~4~]^−^ (Deep Purple)", color=(0.5, 0.1, 0.5), size=7.2)
    g.text(270, 106, "Mn(+7), d^0^: DIAMAGNETIC (0 unp e^-)", color=NAVY, size=6.0)

    # Right Explanatory Box
    g.rect((360, 12, 165, 96), fill=PAPER, color=TEAL, width=1.0)
    g.text(442, 22, "Disproportionation & LMCT", color=TEAL, size=6.8)
    g.text(442, 34, "• **Manganate Disproportionates in Acid:**", color=RED, size=5.5)
    g.text(442, 44, "  3 MnO~4~^2−^ + 4 H^+^ →", color=NAVY, size=5.5)
    g.text(442, 53, "  2 MnO~4~^−^ (purple) + MnO~2~ (brown) + 2H~2~O", color=NAVY, size=5.0)
    g.text(442, 64, "• **Stable only in strong alkali (pH > 12)**!", color=TEAL, size=5.5)
    g.text(442, 76, "• **Why is KMnO~4~ Deep Purple?**", color=NAVY, size=6.0)
    g.text(442, 86, "  Mn(+7) is d^0^ (no d-d transition!).", color=RED, size=5.5)
    g.text(442, 95, "  Colour is due to intense **Ligand to", color=NAVY, size=5.5)
    g.text(442, 104, "  Metal Charge Transfer (LMCT)**: O^2−^ → Mn^7+^!", color=RED, size=5.5)


def fig_lanthanoid_actinoid_comparison(page, x, y, w, h):
    """4f Lanthanoids vs 5f Actinoids comparison (Shielding, Oxidation states, and Radioactivity)."""
    g = Pen(page, x, y, w, h, 538, 120)
    g.rect((5, 5, 528, 110), fill=LIGHT_BG, color=TEAL, width=1.0)

    # Left: 4f Lanthanoids
    g.rect((15, 15, 245, 90), fill=PAPER, color=TEAL, width=1.0)
    g.text(137, 26, "4f Lanthanoids (Ce to Lu, Z = 58 - 71)", color=TEAL, size=7.2)
    g.text(137, 40, "• Oxidation States: Predominantly **+3** (rarely +2, +4).", color=NAVY, size=6.0)
    g.text(137, 50, "  Ce^4+^ (noble 4f^0^, oxidant); Eu^2+^ (stable 4f^7^, reductant).", color=GRAY, size=5.5)
    g.text(137, 62, "• 4f orbitals are **deeply buried inside the atom**", color=NAVY, size=6.0)
    g.text(137, 72, "  (shielded by 5s^2^ 5p^6^ electrons); do NOT participate", color=NAVY, size=5.5)
    g.text(137, 81, "  in bonding → low tendency to form complexes!", color=NAVY, size=5.5)
    g.text(137, 93, "• Radioactivity: **ONLY Promethium (Pm) is radioactive**!", color=RED, size=6.0)

    # Right: 5f Actinoids
    g.rect((275, 15, 250, 90), fill=PAPER, color=RED, width=1.0)
    g.text(400, 26, "5f Actinoids (Th to Lr, Z = 90 - 103)", color=RED, size=7.2)
    g.text(400, 40, "• Oxidation States: **Wide spectrum: +3, +4, +5, +6, +7**!", color=RED, size=6.0)
    g.text(400, 50, "  U(+6), Np(+7), Pu(+7) due to small 5f-6d-7s energy gap.", color=GRAY, size=5.5)
    g.text(400, 62, "• 5f orbitals extend further into space than 4f:", color=NAVY, size=6.0)
    g.text(400, 72, "  Less shielded → **much greater tendency to form complexes**", color=NAVY, size=5.5)
    g.text(400, 81, "  and oxo-cations (e.g. UO~2~^2+^, PuO~2~^2+^).", color=TEAL, size=5.5)
    g.text(400, 93, "• Radioactivity: **ALL actinoids are intensely radioactive**!", color=RED, size=6.0)


REGISTRY = {
    "lanthanoid_contraction": (fig_lanthanoid_contraction, 0.22),
    "electrode_potentials": (fig_electrode_potentials, 0.22),
    "chromate_dichromate": (fig_chromate_dichromate, 0.22),
    "permanganate_manganate": (fig_permanganate_manganate, 0.22),
    "lanthanoid_actinoid_comparison": (fig_lanthanoid_actinoid_comparison, 0.22),
}
