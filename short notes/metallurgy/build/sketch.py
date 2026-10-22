"""Custom vector chemical diagrams and flowcharts for Metallurgy short notes."""
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

    def rect(self, r, fill=None, color=NAVY, width=1.0, radius=0):
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


def fig_froth_floatation(page, x, y, w, h):
    """Froth floatation cell schematic with rotating agitator, rising bubbles, and mineral froth."""
    g = Pen(page, x, y, w, h, 538, 120)
    # Background panel
    g.rect((5, 5, 528, 110), fill=(0.97, 0.99, 1.0), color=TEAL, width=1.0, radius=4)

    # Tank body
    g.rect((80, 25, 200, 75), fill=(0.92, 0.96, 0.98), color=NAVY, width=1.5)
    # Rotating impeller / air inlet pipe
    g.line((180, 10), (180, 85), color=NAVY, width=3.0)
    g.rect((165, 80, 30, 10), fill=GOLD, color=NAVY, width=1.2) # Impeller blades
    g.text(180, 8, "Compressed Air Inflow", color=NAVY, size=6.5)

    # Froth layer at top
    g.rect((80, 25, 200, 20), fill=(0.99, 0.92, 0.8), color=GOLD, width=1.0)
    for bx, by in [(95, 35), (115, 30), (135, 38), (155, 32), (205, 35), (225, 31), (245, 36), (265, 33)]:
        g.circle((bx, by), 4, fill=(1.0, 1.0, 1.0), color=GOLD)
    g.text(140, 20, "Mineral-Rich Froth (Sulphide Ore + Pine Oil)", color=GOLD, size=6.5)

    # Rising bubbles carrying sulphide
    for bbx, bby in [(120, 65), (140, 50), (220, 60), (240, 52), (160, 68), (200, 70)]:
        g.circle((bbx, bby), 2.5, fill=PAPER, color=TEAL)
        g.circle((bbx+2, bby-1), 1.2, fill=GOLD, color=GOLD) # ore particle attached

    # Gangue sediment at bottom
    g.rect((85, 92, 190, 7), fill=(0.85, 0.85, 0.85), color=GRAY, width=0.8)
    g.text(180, 97, "Gangue Wetted by Water (Settles at bottom)", color=GRAY, size=5.8)

    # Right Explanatory Box
    g.rect((300, 15, 225, 92), fill=PAPER, color=TEAL, width=1.0, radius=3)
    g.text(412, 26, "Froth Floatation Principles (NCERT §6.2.3)", color=TEAL, size=7.5)
    g.text(412, 38, "• Frother: Pine oil / Camphor (stabilizes foam)", color=NAVY, size=6.3)
    g.text(412, 49, "• Collector: Na-Ethyl Xanthate (hydrophobic coating)", color=NAVY, size=6.3)
    g.text(412, 60, "• Stabilizer: Aniline / Cresol (surface tension)", color=NAVY, size=6.3)
    g.text(412, 71, "• Depressant: NaCN separates ZnS from PbS", color=RED, size=6.3)
    g.text(412, 82, "   Forms soluble complex: Na~2~[Zn(CN)~4~]", color=RED, size=6.0)
    g.text(412, 93, "   PbS floats unaffected into the froth!", color=TEAL, size=6.0)


def fig_bayer_process(page, x, y, w, h):
    """Bayer Process Flowchart for Leaching of Alumina from Bauxite."""
    g = Pen(page, x, y, w, h, 538, 120)
    g.rect((5, 5, 528, 110), fill=LIGHT_BG, color=TEAL, width=1.0, radius=4)

    # Step 1: Digestion
    g.rect((15, 25, 115, 65), fill=PAPER, color=NAVY, width=1.0, radius=3)
    g.text(72, 36, "1. DIGESTION", color=TEAL, size=7.5)
    g.text(72, 48, "Crushed Bauxite +", color=NAVY, size=6.2)
    g.text(72, 58, "Conc. NaOH (473-523 K)", color=NAVY, size=6.2)
    g.text(72, 68, "35-36 bar pressure", color=GRAY, size=5.8)
    g.text(72, 78, "Soluble Na[Al(OH)~4~]", color=GOLD, size=6.2)

    g.line((130, 57), (150, 57), color=TEAL, width=1.5) # Arrow

    # Step 2: Filtration & Red Mud
    g.rect((150, 25, 110, 65), fill=PAPER, color=NAVY, width=1.0, radius=3)
    g.text(205, 36, "2. FILTRATION", color=TEAL, size=7.5)
    g.text(205, 48, "Insoluble Impurities", color=RED, size=6.2)
    g.text(205, 58, "Removed as Red Mud:", color=RED, size=6.2)
    g.text(205, 68, "Fe~2~O~3~, TiO~2~, Silica", color=NAVY, size=5.8)
    g.text(205, 78, "(SiO~2~ as Na~2~SiO~3~)", color=GRAY, size=5.5)

    g.line((260, 57), (280, 57), color=TEAL, width=1.5) # Arrow

    # Step 3: Precipitation
    g.rect((280, 25, 115, 65), fill=PAPER, color=NAVY, width=1.0, radius=3)
    g.text(337, 36, "3. NEUTRALIZATION", color=TEAL, size=7.5)
    g.text(337, 48, "CO~2~ Gas Bubbled +", color=NAVY, size=6.2)
    g.text(337, 58, "Fresh Al(OH)~3~ Seeds", color=NAVY, size=6.2)
    g.text(337, 68, "Induces precipitation", color=GRAY, size=5.8)
    g.text(337, 78, "Hydrated Al~2~O~3~·xH~2~O", color=GOLD, size=6.2)

    g.line((395, 57), (415, 57), color=TEAL, width=1.5) # Arrow

    # Step 4: Calcination
    g.rect((415, 25, 110, 65), fill=PAPER, color=NAVY, width=1.0, radius=3)
    g.text(470, 36, "4. CALCINATION", color=TEAL, size=7.5)
    g.text(470, 48, "Heat to 1470 K", color=RED, size=6.5)
    g.text(470, 58, "Al~2~O~3~·xH~2~O →", color=NAVY, size=6.2)
    g.text(470, 70, "PURE ALUMINA", color=TEAL, size=7.0)
    g.text(470, 80, "Al~2~O~3~ + x H~2~O↑", color=NAVY, size=6.0)

    g.text(269, 102, "NCERT §6.2.4: Hall's Process uses Na~2~CO~3~; Serpeck's Process (for white bauxite with silica) uses Coke + N~2~ → AlN.", color=GRAY, size=6.0)


def fig_ellingham_diagram(page, x, y, w, h):
    """The Ellingham Diagram: Standard Gibbs Free Energy of Oxidation vs Temperature."""
    g = Pen(page, x, y, w, h, 538, 120)
    g.rect((5, 5, 528, 110), fill=LIGHT_BG, color=TEAL, width=1.0, radius=4)

    # Plot axes
    g.line((60, 95), (320, 95), color=NAVY, width=1.2) # X axis (T in °C or K)
    g.line((60, 15), (60, 95), color=NAVY, width=1.2)  # Y axis (ΔG° per mole of O2)
    g.text(60, 12, "ΔG° (kJ/mol O~2~)", color=NAVY, size=6.2)
    g.text(190, 103, "Temperature T (K) →", color=NAVY, size=6.2)

    # T ticks
    g.text(60, 101, "0", color=GRAY, size=5.5)
    g.text(140, 101, "700 K", color=GRAY, size=5.5)
    g.text(210, 101, "1073 K", color=RED, size=5.5)
    g.text(280, 101, "1600 K", color=GRAY, size=5.5)

    # Ellingham Lines
    # 1. 2Mg + O2 -> 2MgO (very negative, rises, kinks upward at boiling point)
    g.line((60, 90), (220, 75), color=TEAL, width=1.2)
    g.line((220, 75), (310, 55), color=TEAL, width=1.2) # kink at Mg bp
    g.text(230, 82, "2Mg + O~2~ → 2MgO (Kink at Mg bp)", color=TEAL, size=5.2)

    # 2. 4/3 Al + O2 -> 2/3 Al2O3 (above Mg below crossover)
    g.line((60, 80), (310, 50), color=GOLD, width=1.2)
    g.text(275, 46, "4/3Al + O~2~ → 2/3Al~2~O~3~", color=GOLD, size=5.2)

    # 3. 2C + O2 -> 2CO (downward sloping, ΔS > 0!)
    g.line((60, 40), (310, 85), color=RED, width=1.5)
    g.text(280, 90, "2C + O~2~ → 2CO (Slope < 0!)", color=RED, size=5.5)

    # 4. 2Fe + O2 -> 2FeO
    g.line((60, 60), (310, 35), color=NAVY, width=1.2)
    g.text(160, 50, "2Fe + O~2~ → 2FeO", color=NAVY, size=5.2)

    # Right Key Rules Panel
    g.rect((335, 12, 190, 95), fill=PAPER, color=TEAL, width=1.0, radius=3)
    g.text(430, 22, "Key Ellingham Laws (NCERT §6.3)", color=TEAL, size=7.0)
    g.text(430, 34, "1. Lower line reduces higher oxide:", color=NAVY, size=6.2)
    g.text(430, 44, "   Metal of lower curve can reduce", color=NAVY, size=5.8)
    g.text(430, 53, "   the oxide of any element above it!", color=NAVY, size=5.8)
    g.text(430, 64, "2. Crossover Point:", color=RED, size=6.2)
    g.text(430, 74, "   Above T~c~, the lower curve swaps.", color=NAVY, size=5.8)
    g.text(430, 83, "   e.g. Mg reduces Al~2~O~3~ < 1623 K;", color=GRAY, size=5.5)
    g.text(430, 92, "   Al reduces MgO > 1623 K!", color=RED, size=5.8)
    g.text(430, 102, "3. Downward 2C+O~2~→2CO cuts all oxides!", color=TEAL, size=5.8)


def fig_blast_furnace(page, x, y, w, h):
    """The Blast Furnace for Iron Extraction showing zones, chemistry, and slag formation."""
    g = Pen(page, x, y, w, h, 538, 120)
    g.rect((5, 5, 528, 110), fill=LIGHT_BG, color=TEAL, width=1.0, radius=4)

    # Blast furnace stylized profile
    pts = [(80, 15), (105, 15), (120, 55), (110, 95), (75, 95), (65, 55)]
    # Outline of stack
    g.line((80, 15), (65, 55), color=NAVY, width=1.2)
    g.line((65, 55), (75, 95), color=NAVY, width=1.2)
    g.line((75, 95), (110, 95), color=NAVY, width=1.2)
    g.line((110, 95), (120, 55), color=NAVY, width=1.2)
    g.line((120, 55), (105, 15), color=NAVY, width=1.2)
    g.line((105, 15), (80, 15), color=NAVY, width=1.2)

    # Charge in top
    g.text(92, 11, "Charge: Ore + Coke + CaCO~3~", color=GOLD, size=5.5)
    # Tuyeres at bottom
    g.line((55, 85), (75, 85), color=RED, width=2.0)
    g.line((130, 85), (110, 85), color=RED, width=2.0)
    g.text(50, 82, "Hot Air", color=RED, size=5.2)
    # Molten pig iron and slag taps
    g.text(92, 92, "Molten Iron + Slag", color=NAVY, size=5.5)

    # Zone chemistry descriptions in columns
    # Zone 1 (Top: Reduction 500 - 800 K)
    g.rect((135, 15, 125, 28), fill=PAPER, color=TEAL, width=0.8, radius=2)
    g.text(197, 23, "Top: Reduction Zone (500-800 K)", color=TEAL, size=6.2)
    g.text(197, 32, "3 Fe~2~O~3~ + CO → 2 Fe~3~O~4~ + CO~2~", color=NAVY, size=5.5)
    g.text(197, 40, "Fe~3~O~4~ + 4 CO → 3 Fe + 4 CO~2~", color=NAVY, size=5.5)

    # Zone 2 (Middle: Slag & Decomposition 900 - 1200 K)
    g.rect((135, 47, 125, 30), fill=PAPER, color=GOLD, width=0.8, radius=2)
    g.text(197, 55, "Middle: Slag Formation (900-1200 K)", color=GOLD, size=6.2)
    g.text(197, 64, "CaCO~3~ → CaO + CO~2~ (Calcination)", color=NAVY, size=5.5)
    g.text(197, 73, "CaO + SiO~2~ → CaSiO~3~ (Fusible Slag)", color=RED, size=5.5)

    # Zone 3 (Bottom: Combustion 1500 - 2200 K)
    g.rect((135, 81, 125, 27), fill=PAPER, color=RED, width=0.8, radius=2)
    g.text(197, 89, "Bottom: Combustion Zone (>1500 K)", color=RED, size=6.2)
    g.text(197, 98, "C + O~2~ → CO~2~  (Exothermic, 2170 K)", color=NAVY, size=5.5)
    g.text(197, 105, "C + CO~2~ → 2 CO (Boudouard, Endothermic)", color=NAVY, size=5.5)

    # Iron Forms Matrix Box at Right
    g.rect((270, 15, 255, 93), fill=PAPER, color=NAVY, width=1.0, radius=3)
    g.text(397, 25, "Forms of Iron — Composition & Traps", color=NAVY, size=7.2)
    g.text(397, 37, "• Pig Iron: ≈4% Carbon + S, P, Si, Mn impurities.", color=RED, size=6.2)
    g.text(397, 46, "  Tapped directly from blast furnace; hard & brittle.", color=GRAY, size=5.5)
    g.text(397, 57, "• Cast Iron: ≈3% Carbon (Pig iron remelted with scrap).", color=GOLD, size=6.2)
    g.text(397, 66, "  Extremely hard, brittle, expands upon solidification.", color=GRAY, size=5.5)
    g.text(397, 77, "• Wrought Iron: Purest commercial iron (<0.2% C).", color=TEAL, size=6.2)
    g.text(397, 86, "  Made in reverberatory furnace lined with haematite:", color=NAVY, size=5.5)
    g.text(397, 95, "  Fe~2~O~3~ + 3 C → 2 Fe + 3 CO↑ (removes carbon).", color=NAVY, size=5.5)
    g.text(397, 104, "  Malleable, ductile, tough (used for chains, anchors).", color=TEAL, size=5.5)


def fig_hall_heroult(page, x, y, w, h):
    """Hall-Héroult Electrolytic Cell for Alumina Extraction and Carbon Anode Burn."""
    g = Pen(page, x, y, w, h, 538, 120)
    g.rect((5, 5, 528, 110), fill=LIGHT_BG, color=TEAL, width=1.0, radius=4)

    # Steel tank with carbon lining (Cathode)
    g.rect((40, 25, 200, 70), fill=(0.90, 0.90, 0.90), color=NAVY, width=1.5)
    g.rect((45, 30, 190, 60), fill=(0.20, 0.20, 0.20), color=NAVY, width=1.0) # Carbon cathode lining
    g.rect((50, 35, 180, 50), fill=(0.98, 0.95, 0.88), color=GOLD, width=0.8) # Molten electrolyte bath

    # Suspended Graphite Anodes
    for ax in [80, 115, 150, 185]:
        g.rect((ax, 15, 15, 45), fill=(0.3, 0.3, 0.3), color=NAVY, width=1.0)
        g.line((ax+7, 8), (ax+7, 15), color=RED, width=1.2) # Anode busbar
    g.line((85, 8), (195, 8), color=RED, width=1.5)
    g.text(140, 5, "Graphite Anodes (+)", color=RED, size=6.5)

    # Cathode label
    g.text(140, 93, "Carbon Lining = Cathode (−)", color=NAVY, size=6.0)
    g.text(140, 78, "Molten Al settles at bottom (1220 K)", color=TEAL, size=5.5)

    # Right details panel
    g.rect((255, 12, 270, 96), fill=PAPER, color=TEAL, width=1.0, radius=3)
    g.text(390, 22, "Hall-Héroult Cell Chemistry (NCERT §6.6)", color=TEAL, size=7.2)
    g.text(390, 34, "• Electrolyte: Molten Al~2~O~3~ (5%) + Cryolite (Na~3~AlF~6~, 85%)", color=NAVY, size=6.2)
    g.text(390, 43, "  + Fluorspar (CaF~2~, 5-10%).", color=NAVY, size=6.2)
    g.text(390, 53, "• Function of Cryolite / CaF~2~: (Crucial JEE Traps!)", color=RED, size=6.2)
    g.text(390, 62, "  1. Lowers melting point from 2320 K to ≈1170 K.", color=NAVY, size=5.8)
    g.text(390, 71, "  2. Increases electrical conductivity of the melt.", color=NAVY, size=5.8)
    g.text(390, 81, "• Anode Consumption Trap:", color=RED, size=6.2)
    g.text(390, 90, "  C + 2 O^2−^ → CO~2~ + 4 e^−^  (and C + O^2−^ → CO + 2 e^−^)", color=NAVY, size=5.8)
    g.text(390, 100, "  ≈0.5 kg of Carbon anode is burnt for EVERY 1 kg of Al produced!", color=RED, size=5.8)


def fig_copper_bessemer(page, x, y, w, h):
    """Copper Smelting, Matte Formation & Bessemerization (Self-Reduction)."""
    g = Pen(page, x, y, w, h, 538, 120)
    g.rect((5, 5, 528, 110), fill=LIGHT_BG, color=TEAL, width=1.0, radius=4)

    # Step 1: Roasting
    g.rect((15, 20, 115, 75), fill=PAPER, color=NAVY, width=1.0, radius=3)
    g.text(72, 31, "1. ROASTING", color=TEAL, size=7.5)
    g.text(72, 42, "2 CuFeS~2~ + O~2~ →", color=NAVY, size=6.0)
    g.text(72, 51, "Cu~2~S + 2 FeS + SO~2~↑", color=NAVY, size=6.0)
    g.text(72, 63, "Partial oxidation:", color=GRAY, size=5.5)
    g.text(72, 72, "2 FeS + 3 O~2~ →", color=NAVY, size=5.8)
    g.text(72, 81, "2 FeO + 2 SO~2~↑", color=NAVY, size=5.8)

    g.line((130, 57), (145, 57), color=TEAL, width=1.5)

    # Step 2: Smelting (Reverberatory Furnace)
    g.rect((145, 20, 120, 75), fill=PAPER, color=GOLD, width=1.0, radius=3)
    g.text(205, 31, "2. SMELTING (+ SiO~2~)", color=GOLD, size=7.2)
    g.text(205, 42, "Acidic flux SiO~2~ added:", color=NAVY, size=6.0)
    g.text(205, 51, "FeO + SiO~2~ → FeSiO~3~", color=RED, size=6.2)
    g.text(205, 60, "(Lighter slag, floats off)", color=GRAY, size=5.5)
    g.text(205, 72, "Heavy molten layer:", color=TEAL, size=6.0)
    g.text(205, 82, "COPPER MATTE", color=TEAL, size=6.8)
    g.text(205, 91, "(Cu~2~S + little FeS)", color=NAVY, size=5.8)

    g.line((265, 57), (280, 57), color=TEAL, width=1.5)

    # Step 3: Bessemer Converter
    g.rect((280, 20, 125, 75), fill=PAPER, color=RED, width=1.0, radius=3)
    g.text(342, 31, "3. BESSEMER CONVERTER", color=RED, size=7.2)
    g.text(342, 42, "Silica lined, air blown:", color=NAVY, size=5.8)
    g.text(342, 51, "Residual FeS removed as slag.", color=GRAY, size=5.5)
    g.text(342, 62, "Self-Reduction (Auto-Redox):", color=RED, size=6.0)
    g.text(342, 72, "2 Cu~2~O + Cu~2~S →", color=NAVY, size=6.2)
    g.text(342, 82, "6 Cu + SO~2~↑", color=RED, size=6.8)
    g.text(342, 91, "(No external reducing agent!)", color=GRAY, size=5.5)

    g.line((405, 57), (420, 57), color=TEAL, width=1.5)

    # Step 4: Blister Copper
    g.rect((420, 20, 105, 75), fill=PAPER, color=TEAL, width=1.0, radius=3)
    g.text(472, 31, "4. BLISTER COPPER", color=TEAL, size=7.2)
    g.text(472, 44, "≈98-99% Pure Cu", color=NAVY, size=6.5)
    g.text(472, 56, "Why 'Blister'?", color=RED, size=6.5)
    g.text(472, 67, "Bubbles of evolving", color=NAVY, size=5.8)
    g.text(472, 76, "SO~2~ gas burst on cooling,", color=NAVY, size=5.8)
    g.text(472, 85, "leaving blistered craters!", color=GOLD, size=5.8)

    g.text(269, 105, "Electro-refining: Blister Cu = Anode; Pure Cu strip = Cathode; Acidified CuSO~4~ = Electrolyte. Anode mud = Ag, Au, Pt, Se, Te.", color=GRAY, size=5.8)


def fig_refining_methods(page, x, y, w, h):
    """Comparison of Ultra-High-Purity Refining Methods: Zone Refining vs Vapour Phase."""
    g = Pen(page, x, y, w, h, 538, 120)
    g.rect((5, 5, 528, 110), fill=LIGHT_BG, color=TEAL, width=1.0, radius=4)

    # Left: Zone Refining (Fractional Crystallization)
    g.rect((15, 15, 245, 90), fill=PAPER, color=TEAL, width=1.0, radius=3)
    g.text(137, 26, "Zone Refining (Fractional Crystallization)", color=TEAL, size=7.2)
    # Ingot bar
    g.rect((30, 42, 215, 14), fill=(0.85, 0.85, 0.85), color=NAVY, width=1.0)
    # Molten zone
    g.rect((110, 38, 35, 22), fill=(1.0, 0.8, 0.4), color=RED, width=1.2)
    g.text(127, 50, "Molten Zone", color=RED, size=5.2)
    # Moving circular heater
    g.line((110, 35), (145, 35), color=RED, width=2.0)
    g.line((110, 63), (145, 63), color=RED, width=2.0)
    g.text(127, 32, "Circular Heater → (moves slowly)", color=RED, size=5.5)

    g.text(137, 72, "• Principle: Impurities are MORE SOLUBLE in the melt", color=NAVY, size=5.8)
    g.text(137, 81, "  than in the solid crystal lattice.", color=NAVY, size=5.8)
    g.text(137, 91, "• Metals refined: Si, Ge, Ga, In, B (Semiconductor Grade)", color=TEAL, size=6.0)
    g.text(137, 100, "• Impurities concentrate at one end, which is cut off.", color=GRAY, size=5.5)

    # Right: Vapour Phase Refining (Mond & Van Arkel)
    g.rect((275, 15, 250, 90), fill=PAPER, color=NAVY, width=1.0, radius=3)
    g.text(400, 26, "Vapour Phase Refining (Volatile Complex)", color=NAVY, size=7.2)

    # Mond Process
    g.text(400, 38, "1. Mond Process for Nickel (Ni):", color=GOLD, size=6.5)
    g.text(400, 48, "   Ni(impure) + 4 CO —(330-350 K)→ Ni(CO)~4~ (volatile gas)", color=NAVY, size=5.8)
    g.text(400, 57, "   Ni(CO)~4~ —(450-470 K)→ Ni(pure) + 4 CO↑", color=RED, size=5.8)

    # Van Arkel Process
    g.text(400, 71, "2. Van Arkel Method for Ti, Zr, Hf, B:", color=TEAL, size=6.5)
    g.text(400, 81, "   Zr(impure) + 2 I~2~ —(870 K)→ ZrI~4~ (volatile vapour)", color=NAVY, size=5.8)
    g.text(400, 91, "   ZrI~4~ —(Tungsten filament, 2075 K)→ Zr(pure) + 2 I~2~↑", color=RED, size=5.8)
    g.text(400, 101, "• Removes interstitial oxygen and nitrogen impurities!", color=GRAY, size=5.5)


REGISTRY = {
    "froth_floatation": (fig_froth_floatation, 0.22),
    "bayer_process": (fig_bayer_process, 0.22),
    "ellingham_diagram": (fig_ellingham_diagram, 0.22),
    "blast_furnace": (fig_blast_furnace, 0.22),
    "hall_heroult": (fig_hall_heroult, 0.22),
    "copper_bessemer": (fig_copper_bessemer, 0.22),
    "refining_methods": (fig_refining_methods, 0.22),
}
