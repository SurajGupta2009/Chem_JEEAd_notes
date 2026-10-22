"""Custom vector chemical diagrams and physical schematics for Coordination Compounds."""
from __future__ import annotations

import math

# Semantic Palette matching short notes guidelines
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


def fig_werner_structures(page, x, y, w, h):
    """Werner's Theory: Primary (dashed/ionizable) vs Secondary (solid/coordinate) valencies."""
    g = Pen(page, x, y, w, h, 538, 120)
    g.rect((5, 5, 528, 110), fill=LIGHT_BG, color=TEAL, width=1.0)

    # Left: [Co(NH3)6]Cl3 (Yellow)
    g.circle((80, 52), 14, fill=PAPER, color=GOLD, width=1.5)
    g.text(80, 55, "Co^3+^", color=GOLD, size=8.0)
    # 6 solid lines for NH3 (Secondary valency = 6)
    pts_oct = [(50, 30), (110, 30), (45, 52), (115, 52), (50, 74), (110, 74)]
    for ox, oy in pts_oct:
        g.line((80, 52), (ox, oy), color=TEAL, width=1.2)
        g.text(ox, oy+2, "NH~3~", color=TEAL, size=5.8)
    # 3 dashed lines outside for 3 Cl- (Primary valency = 3, ionizable)
    pts_cl = [(30, 20), (130, 20), (80, 95)]
    for cx, cy in pts_cl:
        g.line((80, 52), (cx, cy), color=RED, width=1.0, dashes=[3, 2])
        g.text(cx, cy+2, "Cl^−^", color=RED, size=6.2)
    g.text(80, 105, "[Co(NH~3~)~6~]Cl~3~: 3 AgCl ppt", color=NAVY, size=6.5)

    # Middle: [Co(NH3)5Cl]Cl2 (Purple)
    g.circle((230, 52), 14, fill=PAPER, color=RED, width=1.5)
    g.text(230, 55, "Co^3+^", color=RED, size=8.0)
    pts_oct2 = [(200, 30), (260, 30), (195, 52), (265, 52), (200, 74)]
    for ox, oy in pts_oct2:
        g.line((230, 52), (ox, oy), color=TEAL, width=1.2)
        g.text(ox, oy+2, "NH~3~", color=TEAL, size=5.8)
    # One dual-nature Cl (solid + dashed = dual character!)
    g.line((230, 52), (260, 74), color=TEAL, width=1.5)
    g.line((230, 52), (260, 74), color=RED, width=1.0, dashes=[3, 2])
    g.text(262, 76, "Cl^−^*", color=RED, size=6.2)
    # 2 pure primary Cl- outside
    g.line((230, 52), (180, 20), color=RED, width=1.0, dashes=[3, 2]); g.text(180, 22, "Cl^−^", color=RED, size=6.2)
    g.line((230, 52), (230, 95), color=RED, width=1.0, dashes=[3, 2]); g.text(230, 97, "Cl^−^", color=RED, size=6.2)
    g.text(230, 105, "[Co(NH~3~)~5~Cl]Cl~2~: 2 AgCl ppt", color=NAVY, size=6.5)

    # Right Explanatory Box
    g.rect((325, 12, 200, 96), fill=PAPER, color=TEAL, width=1.0)
    g.text(425, 22, "Werner's Postulates (NCERT §9.1)", color=TEAL, size=7.2)
    g.text(425, 34, "• **Primary Valency (Oxidation State):**", color=RED, size=6.2)
    g.text(425, 44, "  Ionizable, non-directional; satisfied ONLY", color=NAVY, size=5.8)
    g.text(425, 53, "  by negative ions (dashed lines).", color=NAVY, size=5.8)
    g.text(425, 64, "• **Secondary Valency (Coordination Number):**", color=TEAL, size=6.2)
    g.text(425, 74, "  Non-ionizable, directional in space (solid lines);", color=NAVY, size=5.8)
    g.text(425, 83, "  determines stereochemistry / geometry!", color=NAVY, size=5.8)
    g.text(425, 94, "• Dual Ligand (Cl*): Satisfies BOTH primary &", color=GOLD, size=5.8)
    g.text(425, 103, "  secondary valency → non-ionizable in solution!", color=RED, size=5.5)


def fig_cft_octahedral(page, x, y, w, h):
    """Crystal Field Splitting in Octahedral vs Tetrahedral Complexes."""
    g = Pen(page, x, y, w, h, 538, 120)
    g.rect((5, 5, 528, 110), fill=LIGHT_BG, color=TEAL, width=1.0)

    # Left: Octahedral Field Splitting
    g.text(120, 16, "Octahedral Field (Δ_o)", color=TEAL, size=7.5)
    # Free ion 5 degenerate orbitals
    for i in range(5):
        g.rect((20 + i*10, 55, 8, 12), fill=PAPER, color=GRAY, width=1.0)
    g.text(45, 75, "Free M^n+^ (d^x^)", color=GRAY, size=5.5)

    # Average spherical field
    for i in range(5):
        g.rect((80 + i*10, 45, 8, 12), fill=PAPER, color=NAVY, width=1.0)
    g.text(105, 65, "Barycentre (Spherical)", color=NAVY, size=5.5)

    # Splitting into eg (top 2) and t2g (bottom 3)
    # eg (top): +0.6 Δ_o
    g.rect((170, 25, 10, 12), fill=PAPER, color=RED, width=1.2)
    g.rect((185, 25, 10, 12), fill=PAPER, color=RED, width=1.2)
    g.text(182, 20, "e~g~ (d~x²−y²~, d~z²~)", color=RED, size=6.0)
    g.text(182, 42, "+0.6 Δ_o (+3/5)", color=RED, size=5.5)

    # t2g (bottom): -0.4 Δ_o
    g.rect((160, 68, 10, 12), fill=PAPER, color=TEAL, width=1.2)
    g.rect((175, 68, 10, 12), fill=PAPER, color=TEAL, width=1.2)
    g.rect((190, 68, 10, 12), fill=PAPER, color=TEAL, width=1.2)
    g.text(180, 88, "t~2g~ (d~xy~, d~yz~, d~zx~)", color=TEAL, size=6.0)
    g.text(180, 97, "−0.4 Δ_o (−2/5)", color=TEAL, size=5.5)

    # Energy arrow Δ_o
    g.line((215, 25), (215, 80), color=GOLD, width=1.5)
    g.text(225, 53, "Δ_o", color=GOLD, size=8.0)

    # Center: Tetrahedral Field Splitting
    g.text(320, 16, "Tetrahedral Field (Δ~t~)", color=RED, size=7.5)
    # Inverted: e (bottom 2) and t2 (top 3)
    g.rect((280, 30, 10, 12), fill=PAPER, color=TEAL, width=1.2)
    g.rect((295, 30, 10, 12), fill=PAPER, color=TEAL, width=1.2)
    g.rect((310, 30, 10, 12), fill=PAPER, color=TEAL, width=1.2)
    g.text(300, 24, "t~2~ (+0.4 Δ~t~)", color=TEAL, size=5.8)

    g.rect((290, 72, 10, 12), fill=PAPER, color=RED, width=1.2)
    g.rect((305, 72, 10, 12), fill=PAPER, color=RED, width=1.2)
    g.text(302, 92, "e (−0.6 Δ~t~)", color=RED, size=5.8)

    # Right Explanatory Box
    g.rect((350, 12, 175, 96), fill=PAPER, color=TEAL, width=1.0)
    g.text(437, 22, "CFT Governing Principles", color=TEAL, size=6.8)
    g.text(437, 34, "• **Octahedral Field (Oh):** Ligands approach", color=NAVY, size=5.5)
    g.text(437, 43, "  along axes (x, y, z) → axial orbitals (e~g~)", color=NAVY, size=5.5)
    g.text(437, 52, "  experience maximal repulsion and rise!", color=RED, size=5.5)
    g.text(437, 63, "• **Tetrahedral Field (Td):** Ligands approach", color=NAVY, size=5.5)
    g.text(437, 72, "  between axes → t~2~ rises, e falls.", color=NAVY, size=5.5)
    g.text(437, 83, "• **The 4/9 Relation:** **Δ~t~ = (4/9) Δ_o**!", color=GOLD, size=6.5)
    g.text(437, 93, "  Because Δ~t~ is small, pairing energy P > Δ~t~:", color=NAVY, size=5.5)
    g.text(437, 102, "  **ALL Td complexes are HIGH SPIN!**", color=RED, size=5.8)


def fig_square_planar_splitting(page, x, y, w, h):
    """Crystal Field Splitting in Square Planar Complexes & Jahn-Teller Limit."""
    g = Pen(page, x, y, w, h, 538, 120)
    g.rect((5, 5, 528, 110), fill=LIGHT_BG, color=TEAL, width=1.0)

    # Progressive evolution from Octahedral -> Tetragonal (z-out) -> Square Planar
    g.text(70, 18, "Octahedral (O~h~)", color=GRAY, size=6.5)
    g.rect((60, 35, 10, 10), fill=PAPER, color=RED); g.rect((75, 35, 10, 10), fill=PAPER, color=RED)
    g.text(72, 30, "e~g~", color=RED, size=5.5)
    g.rect((55, 75, 10, 10), fill=PAPER, color=TEAL); g.rect((70, 75, 10, 10), fill=PAPER, color=TEAL); g.rect((85, 75, 10, 10), fill=PAPER, color=TEAL)
    g.text(72, 92, "t~2g~", color=TEAL, size=5.5)

    g.line((105, 55), (145, 55), color=NAVY, width=1.2)
    g.text(125, 48, "z-elongation", color=NAVY, size=5.5)

    # Square Planar (D4h): z-ligands completely removed!
    g.text(230, 16, "Square Planar (D~4h~)", color=TEAL, size=7.2)
    # Highest: d_x2-y2 (directly facing 4 in-plane ligands)
    g.rect((220, 22, 14, 10), fill=PAPER, color=RED, width=1.2)
    g.text(227, 16, "d~x²−y²~ (Extreme Repulsion!)", color=RED, size=6.0)

    # Second: d~xy~
    g.rect((220, 45, 14, 10), fill=PAPER, color=GOLD, width=1.2)
    g.text(227, 40, "d~xy~ (in-plane non-axial)", color=GOLD, size=5.8)

    # Third: d_z2 (stabilized due to absence of z-ligands)
    g.rect((220, 68, 14, 10), fill=PAPER, color=TEAL, width=1.2)
    g.text(227, 63, "d~z²~ (axial, low repulsion)", color=TEAL, size=5.8)

    # Lowest: degenerate d~xz~, d~yz~
    g.rect((212, 90, 14, 10), fill=PAPER, color=NAVY, width=1.2)
    g.rect((230, 90, 14, 10), fill=PAPER, color=NAVY, width=1.2)
    g.text(227, 105, "d~xz~, d~yz~ (strictly off-plane)", color=NAVY, size=5.8)

    # Right Explanatory Box
    g.rect((320, 12, 205, 96), fill=PAPER, color=TEAL, width=1.0)
    g.text(422, 22, "Square Planar & d^8^ Systems", color=TEAL, size=6.8)
    g.text(422, 34, "• **Energy Hierarchy in D~4h~:**", color=RED, size=6.0)
    g.text(422, 44, "  **d~x²−y²~ >> d~xy~ > d~z²~ > (d~xz~ = d~yz~)**", color=RED, size=6.0)
    g.text(422, 55, "• **Why d^8^ Metals Love Square Planar?**", color=NAVY, size=6.0)
    g.text(422, 65, "  8 electrons occupy the bottom 4 orbitals paired,", color=NAVY, size=5.5)
    g.text(422, 74, "  leaving empty the highly destabilized d~x²−y²~!", color=NAVY, size=5.5)
    g.text(422, 85, "• **Universally Square Planar:** All **4d^8^ (Pd^2+^)** and", color=TEAL, size=5.5)
    g.text(422, 94, "  **5d^8^ (Pt^2+^, Au^3+^)** complexes are square planar &", color=TEAL, size=5.5)
    g.text(422, 103, "  **DIAMAGNETIC**, even with weak-field Cl^−^ ligands!", color=RED, size=5.5)


def fig_carbonyl_synergic_bonding(page, x, y, w, h):
    """Synergic M-CO Bonding: sigma donation and pi backbonding."""
    g = Pen(page, x, y, w, h, 538, 120)
    g.rect((5, 5, 528, 110), fill=LIGHT_BG, color=TEAL, width=1.0)

    # Left: Metal center and CO ligand schematic
    g.circle((100, 55), 18, fill=PAPER, color=NAVY, width=1.5)
    g.text(100, 58, "M", color=NAVY, size=10.0)

    g.circle((180, 55), 12, fill=PAPER, color=TEAL, width=1.2)
    g.text(180, 57.5, "C", color=TEAL, size=8.0)

    g.circle((240, 55), 12, fill=PAPER, color=RED, width=1.2)
    g.text(240, 57.5, "O", color=RED, size=8.0)

    # Sigma donation: C -> M (axial)
    g.line((165, 55), (120, 55), color=TEAL, width=2.0)
    g.text(142, 47, "σ donation", color=TEAL, size=6.5)
    g.text(142, 65, "LP(C) → Vacant d(M)", color=GRAY, size=5.2)

    # Pi back-donation: M -> C (above and below)
    # Upper loop
    g.line((110, 40), (170, 40), color=RED, width=1.5, dashes=[3, 1])
    g.text(140, 32, "π back-donation (dπ → π*)", color=RED, size=6.0)
    # Lower loop
    g.line((110, 70), (170, 70), color=RED, width=1.5, dashes=[3, 1])

    # C-O triple bond
    g.line((193, 51), (227, 51), color=TEAL, width=1.2)
    g.line((193, 55), (227, 55), color=TEAL, width=1.2)
    g.line((193, 59), (227, 59), color=TEAL, width=1.2)

    # Right Explanatory Box
    g.rect((275, 12, 250, 96), fill=PAPER, color=TEAL, width=1.0)
    g.text(400, 22, "Synergic Effect in Metal Carbonyls (NCERT §9.6)", color=TEAL, size=6.8)
    g.text(400, 34, "1. **σ-Bond (C → M):** Carbon donates its lone pair", color=TEAL, size=5.8)
    g.text(400, 43, "   into an empty hybrid orbital of the metal atom.", color=NAVY, size=5.5)
    g.text(400, 54, "2. **π-Bond (M → C):** Filled metal dπ orbital donates", color=RED, size=5.8)
    g.text(400, 63, "   electron density back into empty antibonding **π* orbitals** of CO.", color=NAVY, size=5.5)
    g.text(400, 75, "3. **Synergy:** σ-donation increases electron density on M,", color=GOLD, size=5.8)
    g.text(400, 84, "   enhancing π-backdonation; π-backdonation strengthens σ-bond!", color=NAVY, size=5.5)
    g.text(400, 95, "4. **Bond Length Impact:** As negative charge on metal increases:", color=RED, size=5.5)
    g.text(400, 104, "   M-C bond strengthens (shorter), **C-O bond weakens (longer, lower ν_CO)**!", color=RED, size=5.2)


def fig_isomerism_cis_trans(page, x, y, w, h):
    """Geometrical Isomerism: Cis vs Trans and Fac vs Mer."""
    g = Pen(page, x, y, w, h, 538, 120)
    g.rect((5, 5, 528, 110), fill=LIGHT_BG, color=TEAL, width=1.0)

    # Left: Cis-[Pt(NH3)2Cl2] (Cisplatin)
    g.rect((30, 20, 95, 80), fill=PAPER, color=TEAL, width=1.0)
    g.circle((77, 55), 10, fill=PAPER, color=NAVY, width=1.2); g.text(77, 57.5, "Pt", color=NAVY, size=7.0)
    # NH3 top & right
    g.line((77, 55), (55, 38), color=TEAL, width=1.2); g.text(52, 38, "Cl", color=RED, size=6.0)
    g.line((77, 55), (55, 72), color=TEAL, width=1.2); g.text(52, 72, "Cl", color=RED, size=6.0)
    g.line((77, 55), (100, 38), color=TEAL, width=1.2); g.text(102, 38, "NH~3~", color=TEAL, size=5.5)
    g.line((77, 55), (100, 72), color=TEAL, width=1.2); g.text(102, 72, "NH~3~", color=TEAL, size=5.5)
    g.text(77, 94, "**Cisplatin** (Anti-cancer active!)", color=RED, size=5.5)
    g.text(77, 102, "Dipole moment μ > 0", color=GRAY, size=5.0)

    # Center-Left: Trans-[Pt(NH3)2Cl2]
    g.rect((145, 20, 95, 80), fill=PAPER, color=GRAY, width=1.0)
    g.circle((192, 55), 10, fill=PAPER, color=NAVY, width=1.2); g.text(192, 57.5, "Pt", color=NAVY, size=7.0)
    # Trans diagonals
    g.line((192, 55), (170, 38), color=RED, width=1.2); g.text(168, 38, "Cl", color=RED, size=6.0)
    g.line((192, 55), (215, 72), color=RED, width=1.2); g.text(218, 72, "Cl", color=RED, size=6.0)
    g.line((192, 55), (215, 38), color=TEAL, width=1.2); g.text(218, 38, "NH~3~", color=TEAL, size=5.5)
    g.line((192, 55), (170, 72), color=TEAL, width=1.2); g.text(168, 72, "NH~3~", color=TEAL, size=5.5)
    g.text(192, 94, "**Trans-isomer** (Inactive)", color=NAVY, size=5.5)
    g.text(192, 102, "Centrosymmetric: μ = 0", color=GRAY, size=5.0)

    # Right: Fac vs Mer in [Ma3b3]
    g.rect((260, 15, 265, 90), fill=PAPER, color=TEAL, width=1.0)
    g.text(392, 26, "Facial (fac) vs Meridional (mer) [Ma~3~b~3~]", color=TEAL, size=7.0)
    g.text(392, 40, "• **Facial (fac-isomer):** Three identical donor atoms", color=NAVY, size=5.8)
    g.text(392, 50, "  occupy the corners of the **same octahedral triangular face**.", color=NAVY, size=5.5)
    g.text(392, 60, "  All cis to each other (90° angles). Optically INACTIVE (plane of symmetry).", color=RED, size=5.2)
    g.text(392, 73, "• **Meridional (mer-isomer):** Three donor atoms", color=NAVY, size=5.8)
    g.text(392, 83, "  span a **semi-circle / meridian** plane around the center.", color=NAVY, size=5.5)
    g.text(392, 93, "  One trans pair (180°) and two cis pairs (90°). Optically INACTIVE.", color=RED, size=5.2)


REGISTRY = {
    "werner_structures": (fig_werner_structures, 0.22),
    "cft_octahedral": (fig_cft_octahedral, 0.22),
    "square_planar_splitting": (fig_square_planar_splitting, 0.22),
    "carbonyl_synergic_bonding": (fig_carbonyl_synergic_bonding, 0.22),
    "isomerism_cis_trans": (fig_isomerism_cis_trans, 0.22),
}
