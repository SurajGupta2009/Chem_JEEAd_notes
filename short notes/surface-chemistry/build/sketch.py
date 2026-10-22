"""Custom vector chemical diagrams and physical schematics for Surface Chemistry short notes."""
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

    def text(self, x, y, txt, font="kalam-bold", size=7.5, color=NAVY, align="center"):
        import fitz
        ox = len(txt) * size * 0.25 if align == "center" else (len(txt) * size * 0.5 if align == "right" else 0)
        pt = fitz.Point(self.tx(x) - ox, self.ty(y))
        self.p.insert_text(pt, txt, fontsize=size, color=color)


def fig_adsorption_residual(page, x, y, w, h):
    """Residual surface forces vs bulk forces causing adsorption."""
    g = Pen(page, x, y, w, h, 538, 120)
    g.rect((5, 5, 528, 110), fill=LIGHT_BG, color=TEAL, width=1.0)

    # Bulk solid adsorbent box
    g.rect((40, 45, 200, 60), fill=(0.90, 0.93, 0.96), color=NAVY, width=1.2)
    g.text(140, 95, "Adsorbent (Solid Bulk)", color=NAVY, size=7.0)

    # Bulk particle (balanced forces)
    g.circle((90, 75), 9, fill=(0.75, 0.85, 0.95), color=NAVY, width=1.0)
    for dx, dy in [(0, -16), (0, 16), (-16, 0), (16, 0), (-11, -11), (11, 11), (-11, 11), (11, -11)]:
        g.line((90, 75), (90 + dx, 75 + dy), color=TEAL, width=0.8)
    g.text(90, 60, "Bulk: Net Force = 0", color=TEAL, size=5.5)

    # Surface particle (unbalanced inward/tangential residual forces)
    g.circle((180, 45), 9, fill=(1.0, 0.85, 0.75), color=RED, width=1.2)
    # Downward inward pull
    g.line((180, 45), (180, 70), color=RED, width=1.5)
    g.line((180, 45), (160, 60), color=RED, width=1.2)
    g.line((180, 45), (200, 60), color=RED, width=1.2)
    g.line((180, 45), (155, 45), color=NAVY, width=1.0)
    g.line((180, 45), (205, 45), color=NAVY, width=1.0)
    g.text(180, 32, "Unbalanced Residual Forces!", color=RED, size=6.0)

    # Incoming adsorbate gas molecules
    for ax, ay in [(150, 15), (180, 18), (210, 12), (130, 22), (230, 20)]:
        g.circle((ax, ay), 3.5, fill=PAPER, color=TEAL)
        g.line((ax, ay), (ax, ay + 8), color=TEAL, width=0.8) # velocity vector downwards

    # Right explanatory panel
    g.rect((255, 12, 270, 96), fill=PAPER, color=TEAL, width=1.0)
    g.text(390, 24, "Why Adsorption Occurs (NCERT §5.1.2)", color=TEAL, size=7.2)
    g.text(390, 36, "• Surface particles experience an inward net pull,", color=NAVY, size=6.2)
    g.text(390, 45, "  creating **Residual Surface Valence / Free Energy**.", color=NAVY, size=6.2)
    g.text(390, 56, "• Adsorption satisfies these residual forces:", color=TEAL, size=6.0)
    g.text(390, 66, "  Surface energy decreases → ΔH is ALWAYS NEGATIVE!", color=RED, size=6.2)
    g.text(390, 76, "• Gas molecules lose translational freedom: ΔS < 0.", color=NAVY, size=6.0)
    g.text(390, 86, "• For spontaneity (ΔG = ΔH − TΔS < 0):", color=NAVY, size=6.0)
    g.text(390, 97, "  |ΔH| MUST EXCEED |TΔS|! Exothermic in all cases.", color=RED, size=6.2)


def fig_isotherms(page, x, y, w, h):
    """Freundlich and Langmuir Adsorption Isotherms with pressure regions."""
    g = Pen(page, x, y, w, h, 538, 120)
    g.rect((5, 5, 528, 110), fill=LIGHT_BG, color=TEAL, width=1.0)

    # Freundlich Isotherm Plot on Left
    g.line((40, 95), (220, 95), color=NAVY, width=1.2) # X: Pressure p
    g.line((40, 15), (40, 95), color=NAVY, width=1.2)  # Y: x/m
    g.text(35, 12, "x/m", color=NAVY, size=6.5)
    g.text(130, 103, "Pressure p →", color=NAVY, size=6.2)

    # Curve: Low P linear, intermediate fractional, high P saturation
    pts = [(40, 95), (70, 70), (100, 50), (140, 38), (180, 32), (215, 32)]
    for i in range(len(pts)-1):
        g.line(pts[i], pts[i+1], color=TEAL, width=1.5)

    # Three regions labelled
    g.line((70, 95), (70, 70), color=GRAY, width=0.8, dashes=[2, 2])
    g.line((160, 95), (160, 35), color=GRAY, width=0.8, dashes=[2, 2])
    g.text(55, 60, "x/m ∝ p^1^", color=NAVY, size=5.5)
    g.text(115, 42, "x/m = k p^1/n^", color=TEAL, size=6.2)
    g.text(190, 26, "Saturation: x/m ∝ p^0^", color=RED, size=5.5)

    # Logarithmic Freundlich Plot in Middle
    g.line((245, 95), (370, 95), color=NAVY, width=1.2)
    g.line((245, 20), (245, 95), color=NAVY, width=1.2)
    g.text(245, 15, "log(x/m)", color=NAVY, size=6.0)
    g.text(310, 103, "log p →", color=NAVY, size=6.0)
    # Straight line: y = mx + c
    g.line((245, 75), (360, 35), color=GOLD, width=1.5)
    # Intercept
    g.line((242, 75), (248, 75), color=RED, width=1.2)
    g.text(270, 78, "Intercept = log k", color=RED, size=5.5)
    g.text(325, 48, "Slope = 1/n", color=GOLD, size=6.0)
    g.text(325, 58, "(0 ≤ 1/n ≤ 1)", color=NAVY, size=5.5)

    # Right Rules Panel
    g.rect((385, 12, 140, 96), fill=PAPER, color=TEAL, width=1.0)
    g.text(455, 22, "Freundlich Laws (NCERT)", color=TEAL, size=6.8)
    g.text(455, 34, "• x/m = k p^1/n^  (n > 1)", color=NAVY, size=6.0)
    g.text(455, 45, "• log(x/m) = log k + (1/n)log p", color=NAVY, size=5.5)
    g.text(455, 56, "• 1/n = 0: x/m = const (indep of p)", color=GRAY, size=5.2)
    g.text(455, 66, "• 1/n = 1: x/m ∝ p (linear)", color=GRAY, size=5.2)
    g.text(455, 78, "• Fails at high pressure!", color=RED, size=6.0)
    g.text(455, 88, "• Langmuir: θ = Kp/(1+Kp)", color=TEAL, size=5.8)
    g.text(455, 98, "  Accounts for monolayer sat.", color=NAVY, size=5.2)


def fig_catalysis_cycle(page, x, y, w, h):
    """5-Step Modern Adsorption Theory of Heterogeneous Catalysis."""
    g = Pen(page, x, y, w, h, 538, 120)
    g.rect((5, 5, 528, 110), fill=LIGHT_BG, color=TEAL, width=1.0)

    # Step 1: Diffusion
    g.rect((15, 20, 95, 75), fill=PAPER, color=NAVY, width=1.0)
    g.text(62, 30, "1. DIFFUSION", color=TEAL, size=7.0)
    g.text(62, 44, "Reactants A + B", color=NAVY, size=6.0)
    g.text(62, 54, "diffuse to catalyst", color=NAVY, size=5.5)
    g.text(62, 64, "external surface.", color=NAVY, size=5.5)
    g.line((50, 75), (75, 85), color=GOLD, width=1.5)

    g.line((110, 57), (120, 57), color=TEAL, width=1.5)

    # Step 2: Chemisorption
    g.rect((120, 20, 95, 75), fill=PAPER, color=TEAL, width=1.0)
    g.text(167, 30, "2. ADSORPTION", color=TEAL, size=7.0)
    g.text(167, 44, "A and B chemisorb", color=NAVY, size=5.8)
    g.text(167, 54, "onto active sites via", color=NAVY, size=5.5)
    g.text(167, 64, "chemical bonds.", color=NAVY, size=5.5)
    g.text(167, 78, "Lowers E_a!", color=RED, size=6.5)

    g.line((215, 57), (225, 57), color=TEAL, width=1.5)

    # Step 3: Chemical Reaction (Complex)
    g.rect((225, 20, 95, 75), fill=PAPER, color=RED, width=1.0)
    g.text(272, 30, "3. REACTION", color=RED, size=7.0)
    g.text(272, 44, "Formation of", color=NAVY, size=6.0)
    g.text(272, 54, "activated complex:", color=NAVY, size=5.5)
    g.text(272, 64, "[A—B—Catalyst]‡", color=RED, size=6.0)
    g.text(272, 78, "Bonds rearrange.", color=NAVY, size=5.5)

    g.line((320, 57), (330, 57), color=TEAL, width=1.5)

    # Step 4: Desorption
    g.rect((330, 20, 95, 75), fill=PAPER, color=GOLD, width=1.0)
    g.text(377, 30, "4. DESORPTION", color=GOLD, size=7.0)
    g.text(377, 44, "Product P desorbs", color=NAVY, size=5.8)
    g.text(377, 54, "from active site,", color=NAVY, size=5.5)
    g.text(377, 64, "freeing the site for", color=NAVY, size=5.5)
    g.text(377, 78, "next cycle!", color=TEAL, size=6.2)

    g.line((425, 57), (435, 57), color=TEAL, width=1.5)

    # Step 5: Product Diffusion
    g.rect((435, 20, 90, 75), fill=PAPER, color=NAVY, width=1.0)
    g.text(480, 30, "5. DIFFUSION", color=TEAL, size=7.0)
    g.text(480, 44, "Product P diffuses", color=NAVY, size=5.8)
    g.text(480, 54, "away into bulk.", color=NAVY, size=5.5)
    g.text(480, 68, "Catalyst mass &", color=GRAY, size=5.2)
    g.text(480, 78, "composition UNCHANGED", color=TEAL, size=5.0)

    g.text(269, 105, "NCERT §5.2.2: Activity (catalyst accelerates rate by 10^10^) vs Selectivity (directs reaction to yield specific products, e.g. CO+H2).", color=GRAY, size=5.8)


def fig_micelle_formation(page, x, y, w, h):
    """Surfactant molecule structure, surface monolayer, and spherical micelle at CMC."""
    g = Pen(page, x, y, w, h, 538, 120)
    g.rect((5, 5, 528, 110), fill=LIGHT_BG, color=TEAL, width=1.0)

    # Left: Sodium Stearate anatomy
    g.rect((15, 15, 150, 90), fill=PAPER, color=NAVY, width=1.0)
    g.text(90, 26, "Sodium Stearate (Soap)", color=TEAL, size=7.0)
    # Zig-zag hydrophobic tail
    pts_tail = [(30, 52), (40, 44), (50, 52), (60, 44), (70, 52), (80, 44), (90, 52), (100, 44), (110, 52)]
    for i in range(len(pts_tail)-1):
        g.line(pts_tail[i], pts_tail[i+1], color=NAVY, width=1.5)
    g.text(70, 65, "Hydrophobic C~17~H~35~− Tail", color=NAVY, size=5.5)
    # Polar hydrophilic head
    g.circle((122, 52), 9, fill=(0.99, 0.85, 0.85), color=RED, width=1.2)
    g.text(122, 54, "COO^−^", color=RED, size=6.0)
    g.circle((138, 45), 4, fill=PAPER, color=GOLD)
    g.text(138, 47, "Na^+^", color=GOLD, size=5.0)
    g.text(125, 75, "Hydrophilic Head", color=RED, size=5.5)

    # Middle: Below CMC (Surface Monolayer)
    g.rect((175, 15, 145, 90), fill=PAPER, color=GOLD, width=1.0)
    g.text(247, 26, "Low Conc: Below CMC", color=GOLD, size=7.0)
    g.line((185, 50), (310, 50), color=TEAL, width=1.5) # Water surface
    g.text(247, 46, "Water Surface Line", color=TEAL, size=5.2)
    # Tails in air, heads in water
    for hx in [200, 225, 250, 275, 300]:
        g.circle((hx, 56), 4.5, fill=(0.99, 0.85, 0.85), color=RED)
        g.line((hx, 56), (hx, 36), color=NAVY, width=1.2)
    g.text(247, 72, "Behaves as normal electrolyte.", color=NAVY, size=5.5)
    g.text(247, 83, "Tails project out into air;", color=GRAY, size=5.2)
    g.text(247, 93, "heads immersed in water.", color=GRAY, size=5.2)

    # Right: Spherical Micelle (Above CMC, Kraft Temp T_k)
    g.rect((330, 15, 195, 90), fill=PAPER, color=RED, width=1.0)
    g.text(427, 26, "Above CMC: Spherical Micelle", color=RED, size=7.0)
    # Central grease/oil droplet
    g.circle((427, 60), 10, fill=(1.0, 0.95, 0.7), color=GOLD, width=1.0)
    g.text(427, 62, "Oil", color=GOLD, size=6.0)
    # Radial surfactant molecules (heads outside, tails pointing in)
    for ang in range(0, 360, 30):
        rad = math.radians(ang)
        x_head = 427 + 28 * math.cos(rad)
        y_head = 60 + 28 * math.sin(rad)
        x_tail = 427 + 10 * math.cos(rad)
        y_tail = 60 + 10 * math.sin(rad)
        g.line((x_tail, y_tail), (x_head, y_head), color=NAVY, width=1.0)
        g.circle((x_head, y_head), 3.5, fill=(0.99, 0.85, 0.85), color=RED)
    g.text(427, 97, "Hydrophobic tails trap grease in center!", color=TEAL, size=5.5)


def fig_electrical_double_layer(page, x, y, w, h):
    """Helmholtz Electrical Double Layer, Stern Plane, and Zeta Potential (ζ)."""
    g = Pen(page, x, y, w, h, 538, 120)
    g.rect((5, 5, 528, 110), fill=LIGHT_BG, color=TEAL, width=1.0)

    # Colloidal particle core (e.g. AgI with preferential I- adsorption)
    g.circle((80, 58), 24, fill=(1.0, 0.98, 0.85), color=GOLD, width=1.5)
    g.text(80, 60, "AgI Core", color=GOLD, size=7.5)

    # Fixed Layer (Stern Layer) of I- ions
    for ang in range(0, 360, 36):
        rad = math.radians(ang)
        ix = 80 + 36 * math.cos(rad)
        iy = 58 + 36 * math.sin(rad)
        g.circle((ix, iy), 4, fill=(0.99, 0.85, 0.85), color=RED)
        g.text(ix, iy+1.5, "−", color=RED, size=5.5)
    g.text(80, 102, "Fixed (Stern) Layer", color=RED, size=6.0)

    # Diffuse Layer of K+ counter-ions
    for ang in [18, 54, 90, 126, 162, 198, 234, 270, 306, 342]:
        rad = math.radians(ang)
        kx = 80 + 50 * math.cos(rad)
        ky = 58 + 50 * math.sin(rad)
        g.circle((kx, ky), 3.5, fill=PAPER, color=TEAL)
        g.text(kx, ky+1.2, "+", color=TEAL, size=5.0)
    g.text(80, 112, "Mobile Diffuse Layer", color=TEAL, size=5.8)

    # Potential decay curve in center
    g.line((180, 95), (320, 95), color=NAVY, width=1.0) # Distance r
    g.line((180, 20), (180, 95), color=NAVY, width=1.0) # Potential V
    g.text(180, 15, "Potential V", color=NAVY, size=6.0)
    g.text(250, 103, "Distance from surface r →", color=NAVY, size=5.8)
    # Steep linear drop across fixed layer, then exponential decay
    g.line((180, 30), (220, 55), color=RED, width=1.5)
    pts_decay = [(220, 55), (240, 70), (270, 85), (310, 93)]
    for i in range(len(pts_decay)-1):
        g.line(pts_decay[i], pts_decay[i+1], color=TEAL, width=1.2)
    # Zeta potential marked
    g.line((220, 20), (220, 95), color=GRAY, width=0.8, dashes=[2, 2])
    g.text(220, 18, "Shear Plane", color=GRAY, size=5.5)
    g.line((218, 55), (235, 55), color=GOLD, width=1.2)
    g.text(255, 52, "Zeta Potential (ζ)", color=GOLD, size=6.5)

    # Right Rules & Formula Panel
    g.rect((335, 12, 190, 96), fill=PAPER, color=TEAL, width=1.0)
    g.text(430, 22, "Electrokinetic Properties (NCERT)", color=TEAL, size=6.8)
    g.text(430, 34, "• **Preferential Ion Adsorption:**", color=NAVY, size=6.0)
    g.text(430, 44, "  Adsorbs ion common to its lattice!", color=TEAL, size=5.8)
    g.text(430, 54, "  AgNO~3~ (excess) + KI → AgI/Ag^+^ (+ve sol)", color=NAVY, size=5.2)
    g.text(430, 64, "  KI (excess) + AgNO~3~ → AgI/I^−^ (−ve sol)", color=NAVY, size=5.2)
    g.text(430, 76, "• **Zeta Potential (ζ):**", color=GOLD, size=6.0)
    g.text(430, 86, "  Potential difference between fixed", color=NAVY, size=5.5)
    g.text(430, 96, "  layer and mobile diffuse liquid layer.", color=NAVY, size=5.5)
    g.text(430, 105, "  High |ζ| (>30 mV) prevents coagulation!", color=RED, size=5.2)


def fig_electrophoresis_dialysis(page, x, y, w, h):
    """Electrophoresis U-Tube apparatus and Dialysis purification."""
    g = Pen(page, x, y, w, h, 538, 120)
    g.rect((5, 5, 528, 110), fill=LIGHT_BG, color=TEAL, width=1.0)

    # Left: Electrophoresis U-Tube
    g.rect((15, 12, 245, 96), fill=PAPER, color=NAVY, width=1.0)
    g.text(137, 23, "Electrophoresis (Cataphoresis)", color=NAVY, size=7.2)
    # U-tube lines
    g.line((60, 35), (60, 85), color=NAVY, width=1.5)
    g.line((60, 85), (100, 85), color=NAVY, width=1.5)
    g.line((100, 85), (100, 35), color=NAVY, width=1.5)
    g.line((75, 35), (75, 72), color=NAVY, width=1.0)
    g.line((75, 72), (85, 72), color=NAVY, width=1.0)
    g.line((85, 72), (85, 35), color=NAVY, width=1.0)
    # Electrodes
    g.rect((63, 40, 8, 8), fill=RED, color=RED, width=1.0) # Anode (+)
    g.text(67, 33, "(+)", color=RED, size=6.0)
    g.rect((93, 40, 8, 8), fill=TEAL, color=TEAL, width=1.0) # Cathode (-)
    g.text(97, 33, "(−)", color=TEAL, size=6.0)
    # Particles migrating
    for my in [55, 65, 75]:
        g.circle((67, my), 2.5, fill=RED, color=RED)
    g.text(175, 42, "• Movement of colloidal", color=NAVY, size=5.8)
    g.text(175, 52, "  particles under electric field.", color=NAVY, size=5.8)
    g.text(175, 63, "• Negative particles move to Anode (+).", color=RED, size=5.5)
    g.text(175, 73, "• Positive particles move to Cathode (−).", color=TEAL, size=5.5)
    g.text(175, 85, "• Electroosmosis: Particles prevented", color=GOLD, size=5.5)
    g.text(175, 95, "  from moving; dispersion medium moves!", color=GOLD, size=5.2)

    # Right: Dialysis & Electrodialysis
    g.rect((270, 12, 255, 96), fill=PAPER, color=TEAL, width=1.0)
    g.text(397, 23, "Colloid Purification: Dialysis", color=TEAL, size=7.2)
    # Dialysis parchment bag
    g.rect((300, 38, 45, 55), fill=(0.95, 0.98, 0.95), color=TEAL, width=1.2)
    g.text(322, 55, "Parchment", color=TEAL, size=5.0)
    g.text(322, 63, "Bag", color=TEAL, size=5.0)
    # Big colloid trapped
    g.circle((315, 75), 4, fill=GOLD, color=GOLD)
    g.circle((330, 80), 4, fill=GOLD, color=GOLD)
    # Small crystalloids diffusing out
    for cx, cy in [(355, 50), (360, 70), (355, 85)]:
        g.circle((cx, cy), 1.5, fill=RED, color=RED)
        g.line((cx-5, cy), (cx, cy), color=RED, width=0.8) # arrow out

    g.text(440, 42, "• Principle: Crystalloid ions diffuse", color=NAVY, size=5.8)
    g.text(440, 52, "  through parchment/cellophane,", color=NAVY, size=5.8)
    g.text(440, 62, "  while colloidal particles are trapped.", color=NAVY, size=5.8)
    g.text(440, 74, "• Electrodialysis: Electric field", color=RED, size=5.8)
    g.text(440, 84, "  accelerates ionic migration (10× faster!).", color=RED, size=5.5)
    g.text(440, 96, "• Ultrafiltration: Collodion impregnated paper.", color=TEAL, size=5.5)


REGISTRY = {
    "adsorption_residual": (fig_adsorption_residual, 0.22),
    "isotherms": (fig_isotherms, 0.22),
    "catalysis_cycle": (fig_catalysis_cycle, 0.22),
    "micelle_formation": (fig_micelle_formation, 0.22),
    "electrical_double_layer": (fig_electrical_double_layer, 0.22),
    "electrophoresis_dialysis": (fig_electrophoresis_dialysis, 0.22),
}
