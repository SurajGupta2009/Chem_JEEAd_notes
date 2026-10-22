"""Part 2: Thermodynamic Principles, Ellingham Diagrams & Reduction Methods (MT-07 to MT-12)."""
from __future__ import annotations

SHEETS = [
    # ------------------------------------------------------------------ MT-07
    {
        "id": "MT-07",
        "title": "Thermodynamics of Reduction: Gibbs Free Energy & Ellingham Diagrams",
        "blocks": [
            ("lead", "**Thermodynamic Foundations of Pyrometallurgy** — Ellingham Diagrams (NCERT §6.3)"),
            ("p", 'For any metallurgical reduction to proceed spontaneously at temperature T, the overall change in standard Gibbs free energy must be negative: **ΔG° = ΔH° − T ΔS° < 0**. An **Ellingham diagram** is a graphical plot of Δ~r~ G° versus Absolute Temperature T for the formation of metal oxides per mole of consumed oxygen: (2x/y) M + O~2~(g) → (2/y) M~x~O~y~(s).'),
            ("fig", "ellingham_diagram", "Fig. 2.1 — The Ellingham Diagram: Slopes, phase change kinks, crossover temperatures, and C/CO lines."),
            ("h2", "1. Crucial Features of the Ellingham Diagram"),
            ("bul", [
                "**1. Positive Slope for Metal Oxides:** Since O~2~(g) (a highly disordered gas) is consumed to form a dense, ordered solid oxide, entropy decreases: **ΔS° < 0**. Because slope = d(ΔG°)/dT = −ΔS°, the slope is **positive (+ve)**! Lines slope upward from left to right.",
                "**2. Abrupt Upward Kink upon Phase Transition:** When the metal or oxide melts or vaporizes, ΔS° becomes even more negative (gas to liquid/solid involves huge entropy drop). Hence, the slope abruptly steepens (+ve slope increases) at the melting/boiling point of the metal (e.g. sharp upward kinks at the boiling points of Mg at 1390 K and Zn at 1180 K)!",
                '**3. Feasibility Criterion:** Any metal whose oxide line lies **LOWER** on the Ellingham diagram can reduce the oxide of any metal lying **HIGHER** on the diagram at that temperature! (Because reversing the higher reaction and adding yields a net negative Δ~r~ G°).'
            ]),
            ("trap", 'CRITICAL TRAP: Ellingham diagrams provide purely **THERMODYNAMIC FEASIBILITY**; they give ZERO information regarding the **KINETICS (rate of reaction)**! A reaction may have a massive negative ΔG° at room temperature but possess an immense activation energy (E~a~), making it imperceptibly slow unless heated to operating temperature!')
        ]
    },

    # ------------------------------------------------------------------ MT-08
    {
        "id": "MT-08",
        "title": "The Anomalous Carbon Curves: C vs CO as Universal Reducing Agents",
        "blocks": [
            ("lead", "**The Carbon-Oxygen System in Ellingham Space** — Why Carbon Reduces Almost Everything"),
            ("p", "In the Ellingham diagram, carbon exhibits three distinct oxidation lines with wildly different slopes, governed strictly by the stoichiometry of gas moles formed versus consumed."),
            ("h2", "1. Analysis of the Three Carbon Curves"),
            ("table", ["Oxidation Reaction", "Stoichiometry & Entropy Change", "Slope on Ellingham Plot", "Thermodynamic Consequence"], [
                ["**C(s) + O~2~(g) → CO~2~(g)**", "1 mole gas in → 1 mole gas out: **ΔS° ≈ 0**", "**Nearly horizontal** (zero slope)", 'Line remains flat across all temperatures (≈−394 kJ/mol)'],
                ["**2CO(g) + O~2~(g) → 2CO~2~(g)**", "3 moles gas in → 2 moles gas out: **ΔS° < 0**", "**Positive slope** (slopes upward)", "Strong reducing agent only at **low temperatures** (T < 1073 K)"],
                ["**2C(s) + O~2~(g) → 2CO(g)**", "1 mole gas in → 2 moles gas out: **ΔS° > 0**!", "**NEGATIVE slope** (slopes downward!)", "As T increases, ΔG° becomes **increasingly negative**!"]
            ], [22, 26, 24, 28], "Table 2.1 — The three carbon oxidation curves in Ellingham diagrams."),
            ("h2", "2. The Carbon Crossover Point at 1073 K (Boudouard Equilibrium)"),
            ("p", "At approximately **1073 K (800°C)**, the curves for C → CO and C → CO~2~ intersect. This temperature represents the fundamental crossover boundary:\n"
                  "• **Below 1073 K:** The oxidation of CO to CO~2~ lies lower than C → CO~2~. Therefore, **CO is a thermodynamically stronger and kinetically superior reducing agent than carbon**! This explains why in the upper (cooler) zone of the blast furnace, iron oxides are reduced by CO, not C!\n"
                  "• **Above 1073 K:** The curve for 2C + O~2~ → 2CO dives continuously downwards. Therefore, **Carbon (coke) becomes a dramatically stronger reducing agent than CO**, and directly reduces FeO in the high-temperature hearth!"),
            ("key", "Boudouard Equilibrium: C(s) + CO~2~(g) ⇌ 2CO(g) (ΔH > 0). Le Chatelier's principle dictates that high temperature favours endothermic CO formation, while low temperature favours CO~2~.")
        ]
    },

    # ------------------------------------------------------------------ MT-09
    {
        "id": "MT-09",
        "title": "Smelting & Carbon Reduction: Extraction of Iron, Zinc & Tin",
        "blocks": [
            ("lead", "**Carbon Smelting** — Industrial High-Temperature Reduction of Intermediate Oxides"),
            ("p", "Carbon reduction (smelting) is applied to moderately electropositive metals whose oxides lie above the downward-sloping carbon line at attainable furnace temperatures (1000 − 1800 K)."),
            ("h2", "1. Carbon Reduction of Zinc Oxide (Extraction of Zinc)"),
            ("bul", [
                "**Ore & Roasting:** Sphalerite (ZnS) is roasted to Zincite: 2ZnS + 3O~2~ —(1200 K)→ 2ZnO + 2SO~2~ ↑.",
                '**Reduction Reaction:** Crushed ZnO is mixed with powdered coke and heated to ≈1673 K in vertical retort furnaces: **ZnO(s) + C(s) —(1673 K)→ Zn(g) + CO(g)**.',
                "**Crucial Physical Detail:** Zinc boils at **1180 K (907°C)**! At the reduction temperature (1673 K), zinc is formed in the **vapour state**! The vapours are rapidly condensed by cooling to prevent re-oxidation by CO.",
                '**Spelter:** The condensed crude zinc is ≈97-98% pure, known commercially as **Spelter** (contains Pb, Fe, Cd impurities).'
            ]),
            ("h2", "2. Carbon Reduction of Cassiterite (Extraction of Tin)"),
            ("p", "• Roasted tinstone (SnO~2~) is mixed with anthracite coal and limestone flux and smelted in a reverberatory furnace at 1500 K:\n"
                  "  **SnO~2~ + 2C —(1500 K)→ Sn(l) + 2CO ↑**\n"
                  "• Molten tin is tapped off, leaving slag containing residual tin ('tin slag'), which is re-smelted with more lime and coke."),
            ("table", ["Metal Oxide", "Operating Temp", "Physical State of Metal", "Furnace Type", "Refining Requirement"], [
                ["**ZnO**", '≈1673 K', "**Vapour** (b.p. 1180 K)", "Vertical retort / Belgo-furnace", "Fractional distillation (removes Pb, Cd)"],
                ["**SnO~2~**", '≈1500 K', "**Molten liquid**", "Reverberatory furnace", "Liquation followed by poling"],
                ["**PbO**", '≈1200 K', "**Molten liquid**", "Blast / Reverberatory furnace", "Parke's / Pattinson's process (desilverization)"]
            ], [15, 18, 22, 22, 23], "Table 2.2 — Industrial carbon reduction parameters for non-ferrous metals.")
        ]
    },

    # ------------------------------------------------------------------ MT-10
    {
        "id": "MT-10",
        "title": "Self-Reduction (Auto-Reduction) of Copper, Lead & Mercury Sulphides",
        "blocks": [
            ("lead", "**Auto-Reduction (Self-Reduction)** — Reduction Without External Reducing Agents (NCERT §6.4)"),
            ("p", "Applied exclusively to the sulphide ores of metals having **relatively low electropositivity** and intermediate affinity for oxygen and sulphur: **Copper (Cu), Lead (Pb), and Mercury (Hg)**. No carbon or external flux is added for reduction!"),
            ("h2", "1. The Fundamental Self-Reduction Principle"),
            ("p", "The concentrated sulphide ore is subjected to **partial roasting** in air to convert a portion of it into the corresponding metal oxide or sulphate. Air supply is then cut off, and the temperature is raised. The newly formed oxide/sulphate reacts with the remaining unoxidized sulphide ore to yield the free metal and SO~2~ gas!"),
            ("h2", "2. Industrial Self-Reduction Case Studies"),
            ("table", ["Metal", "Ore & Formula", "Step 1: Partial Roasting (with Air)", "Step 2: Self-Reduction (Air Cut Off)"], [
                ["**Copper (Cu)**", "Chalcocite / Copper Glance\n(Cu~2~S)", "2Cu~2~S + 3O~2~ —(Δ)→ 2Cu~2~O + 2SO~2~ ↑", "**2Cu~2~O + Cu~2~S —(Δ)→ 6Cu(l) + SO~2~ ↑**\nOccurs in Bessemer converter; produces *Blister Copper*!"],
                ["**Lead (Pb)**", "Galena\n(PbS)", "2PbS + 3O~2~ —(Δ)→ 2PbO + 2SO~2~ ↑\nPbS + 2O~2~ —(Δ)→ PbSO~4~", "**2PbO + PbS —(Δ)→ 3Pb(l) + SO~2~ ↑**\n**PbSO~4~ + PbS —(Δ)→ 2Pb(l) + 2SO~2~ ↑**\nOccurs on the hearth of a reverberatory furnace."],
                ["**Mercury (Hg)**", "Cinnabar\n(HgS)", "2HgS + 3O~2~ —(Δ)→ 2HgO + 2SO~2~ ↑", "**2HgO + HgS —(Δ)→ 3Hg(g) + SO~2~ ↑**\n(Also direct thermal decomposition: HgO —(Δ)→ Hg + ½O~2~; Hg boils at 630 K and is distilled)."]
            ], [15, 20, 32, 33], "Table 2.3 — Self-reduction stoichiometry for Cu, Pb, and Hg in JEE Advanced."),
            ("trap", 'TRAP: Can Zinc or Iron undergo self-reduction? ABSOLUTELY NOT! The oxides ZnO and FeO are far too thermodynamically stable compared to ZnS and FeS (their Δ~f~ G° lines lie deep below the sulphide lines). Thus, ZnO + ZnS → 3Zn + SO~2~ has a heavily positive ΔG° and cannot occur under any metallurgical conditions!')
        ]
    },

    # ------------------------------------------------------------------ MT-11
    {
        "id": "MT-11",
        "title": "Thermite Reduction, Metal Displacement & Hydrometallurgy",
        "blocks": [
            ("lead", "**Thermite Process & Displacement Reduction** — Highly Exothermic Metallurgical Reactions"),
            ("p", "When an oxide is too stable to be reduced by carbon, or when the metal reacts with carbon to form brittle interstitial carbides (like Cr~3~C~2~, Mn~3~C, TiC), more electropositive metals (Al, Mg, Na) are deployed as reducing agents."),
            ("h2", "1. Goldschmidt Thermite Process (Aluminothermic Reduction)"),
            ("p", '• **Physical Basis:** Aluminium has an extraordinarily high affinity for oxygen due to the massive negative standard enthalpy of formation of alumina: **Δ~f~ H°(Al~2~O~3~) = −1676 kJ/mol**!\n'
                  "• **Charge & Ignition:** The metal oxide is mixed with granular aluminium powder (3:1 ratio called **Thermite**), placed in a fire-clay crucible embedded in sand, and ignited using an ignition mixture of **Barium peroxide (BaO~2~) + Mg ribbon**:\n"
                  '  **Cr~2~O~3~ + 2Al → Al~2~O~3~ + 2Cr(l)** (ΔH = −540 kJ/mol, T > 3000 K!)\n'
                  "  **3Mn~3~O~4~ + 8Al → 4Al~2~O~3~ + 9Mn(l)**\n"
                  '  **Fe~2~O~3~ + 2Al → Al~2~O~3~ + 2Fe(l)** (Thermite welding of railway tracks!)\n'
                  "• The reaction generates so much heat that the reduced metal is obtained in the **molten liquid state**, while lighter Al~2~O~3~ floats cleanly on top as slag."),
            ("h2", "2. Metal Displacement & Hydrometallurgy of Low-Grade Ores"),
            ("p", "• Low-grade copper ores and tailings (CuO, CuCO~3~) are leached with dilute H~2~SO~4~ to yield aqueous CuSO~4~.\n"
                  "• The solution is treated with scrap iron or hydrogen gas to displace copper metal economically:\n"
                  '  **Cu^2+^(aq) + Fe(s) → Cu(s) + Fe^2+^(aq)** (ΔE° = +0.78 V)\n'
                  "  **Cu^2+^(aq) + H~2~(g) → Cu(s) + 2H^+^(aq)**"),
            ("key", "Why is scrap iron preferred over scrap zinc to precipitate copper? Even though Zinc is more electropositive (E° = −0.76 V), Zinc is vastly more expensive than scrap iron! Scrap iron provides cheap, high-yield displacement.")
        ]
    },

    # ------------------------------------------------------------------ MT-12
    {
        "id": "MT-12",
        "title": "Electrometallurgy: Fused Salt Electrolysis for Highly Electropositive Metals",
        "blocks": [
            ("lead", "**Electrolytic Reduction of Halides & Oxides** — Taming s-Block & Reactive Metals (NCERT §6.4)"),
            ("p", "Metals with strongly negative reduction potentials (Na, K, Mg, Ca, Al) CANNOT be reduced by chemical agents (carbon forms carbides, hydrogen fails, Ellingham lines are at the very bottom). Furthermore, they **CANNOT be extracted by electrolyzing their aqueous solutions** because H~2~O is reduced preferentially to H~2~ gas (E° = −0.83 V) instead of the metal! Hence, **FUSED (MOLTEN) SALT ELECTROLYSIS** is mandatory."),
            ("h2", "1. Industrial Electrometallurgical Processes"),
            ("table", ["Metal", "Industrial Process", "Fused Electrolyte Composition", "Electrode Reactions & JEE Traps"], [
                ["**Sodium (Na)**", "**Down's Process**", "Molten NaCl (40%) + CaCl~2~ (60%)", '**Why add CaCl~2~?** Pure NaCl melts at 1074 K (where Na vaporizes and forms a fog with melt). Adding CaCl~2~ lowers m.p. to ≈873 K!\n• Cathode (Iron): Na^+^ + e^−^ → Na(l)\n• Anode (Graphite): 2Cl^−^ → Cl~2~(g) + 2e^−^'],
                ["**Magnesium (Mg)**", "**Dow's Sea Water Process**", "Anhydrous MgCl~2~ (35%) + NaCl (50%) + CaCl~2~ (15%)", "Carnallite (KCl·MgCl~2~·6H~2~O) cannot be dehydrated by direct heating (hydrolyzes to MgO + 2HCl). It must be dehydrated in a stream of dry HCl gas!\n• Cathode (Steel): Mg^2+^ + 2e^−^ → Mg(l)"],
                ["**Aluminium (Al)**", "**Hall-Héroult Process**", "Molten Al~2~O~3~ (5%) + Na~3~AlF~6~ (85%) + CaF~2~ (10%)", "Pure Al~2~O~3~ melts at 2320 K and is a poor conductor. Cryolite lowers m.p. to 1170 K and provides ionic conductivity.\n• Cathode (Carbon lining): Al^3+^ + 3e^−^ → Al(l)\n• Anode (Graphite): 2O^2−^ + C → CO~2~ + 4e^−^"]
            ], [15, 20, 27, 38], "Table 2.4 — Master Electrometallurgical processes and electrolyte additives."),
            ("trap", "EXAMINER TRAP: In Down's process, Ca^2+^ has a more negative reduction potential than Na^+^ under operating conditions, so ONLY sodium is deposited at the cathode; trace Ca that codeposits forms an immiscible crust that is easily separated.")
        ]
    }
]
