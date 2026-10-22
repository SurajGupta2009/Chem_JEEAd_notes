"""Part 3: Refining Techniques & Complete Extraction of Individual Metals (MT-13 to MT-18)."""
from __future__ import annotations

SHEETS = [
    # ------------------------------------------------------------------ MT-13
    {
        "id": "MT-13",
        "title": "Refining of Crude Metals: Liquation, Distillation & Poling",
        "blocks": [
            ("lead", "**Purification of Crude Metals** — Thermal, Physical & Chemical Refining (NCERT §6.5)"),
            ("p", "Metals obtained after reduction are 'crude' and contain unreacted ore, other metals, non-metals (C, Si, P, S), or slag. Refining upgrades purity to >99.9%. The choice of technique depends on differences in physical or chemical properties between the metal and its impurities."),
            ("h2", "1. Distillation Refining"),
            ("p", "• **Principle:** Applied to metals with **low boiling points** contaminated with non-volatile impurities.\n"
                  "• **Technique:** Crude metal is heated above its boiling point; the pure metal vapours distill off and are condensed in a cooled receiver.\n"
                  "• **Applicable Metals:** **Zinc** (b.p. 1180 K), **Cadmium** (b.p. 1040 K), and **Mercury** (b.p. 630 K)."),
            ("h2", "2. Liquation Refining"),
            ("p", "• **Principle:** Applied when the **metal has a much lower melting point** than the contaminating impurities.\n"
                  "• **Technique:** Crude metal is placed on the sloping hearth of a reverberatory furnace heated slightly above the metal's melting point. The low-melting pure metal melts and flows down the slope into a collection well, leaving the solid, infusible dross behind.\n"
                  "• **Applicable Metals:** **Tin (Sn)** (m.p. 505 K, separated from high-melting iron dross) and **Lead (Pb)** (separated from copper and silver dross)."),
            ("h2", "3. Poling (Green Wood Refining)"),
            ("p", "• **Principle & Technique:** Used when the crude metal contains **its own oxide as the primary impurity** (e.g. Cu~2~O in blister copper, or SnO~2~ in tin). The molten crude metal is vigorously stirred with **poles of fresh green wood**.\n"
                  "• **Mechanism:** The intense heat causes the green wood to release reducing hydrocarbon gases (chiefly **Methane CH~4~**), which chemically reduce the metal oxide back to free metal without introducing new impurities:\n"
                  "  3 Cu~2~O + CH~4~ → 6 Cu + CO ↑ + 2 H~2~O ↑\n"
                  "  SnO~2~ + CH~4~ → Sn + CO ↑ + 2 H~2~O ↑"),
            ("h2", "4. Cupellation Refining"),
            ("p", "• Used to refine crude Silver or Gold containing **Lead (Pb)** impurity (from lead-silver ores).\n"
                  "• Molten crude alloy is heated in an oval porous cupel made of bone-ash or cement in a blast of air. Lead oxidizes rapidly to volatile litharge (PbO), which vaporizes and is absorbed by the porous bone-ash walls, leaving a gleaming bead of pure silver!"),
            ("trap", "TRAP: Poling reduces oxides back to metal; it does NOT remove non-metal impurities like sulphur or phosphorus!")
        ]
    },

    # ------------------------------------------------------------------ MT-14
    {
        "id": "MT-14",
        "title": "Ultra-Pure Refining: Zone Refining & Vapour Phase (Mond & Van Arkel)",
        "blocks": [
            ("lead", "**Ultra-High Purity Refining** — Semiconductor Grade Materials & Volatile Complexes"),
            ("p", "Certain high-technology applications (semiconductors, solar cells, aerospace alloys) demand extreme purity levels exceeding **99.9999% (six-nines purity)**. Conventional thermal methods cannot reach this threshold."),
            ("fig", "refining_methods", "Fig. 3.1 — High-Purity Refining: Zone refining mechanism and Vapour Phase complexes (Mond and Van Arkel)."),
            ("h2", "1. Zone Refining (Fractional Crystallization Principle)"),
            ("bul", [
                '**Underlying Principle:** Based on the fundamental thermodynamic fact that **impurities are significantly MORE SOLUBLE in the molten liquid state than in the corresponding solid crystal lattice** (K~D~ = C~S~ / C~L~ < 1).',
                "**Working Mechanism:** A circular mobile induction heater surrounds a rod of impure metal enclosed in an inert atmosphere (argon) and travels slowly from one end to the other. As the molten zone sweeps forward, pure metal recrystallizes behind it, while impurities stay segregated in the molten zone!",
                "**Repetition & Truncation:** The process is repeated in the identical direction multiple times. The impurities become heavily concentrated at one end of the ingot, which is finally sawn off and discarded.",
                "**Applicable Elements:** **Silicon (Si), Germanium (Ge), Gallium (Ga), Indium (In), Boron (B)** — vital for transistor and semiconductor manufacturing!"
            ]),
            ("h2", "2. Vapour Phase Refining: Two Essential Criteria"),
            ("p", "Vapour phase refining requires two strict chemical conditions:\n"
                  "1. The metal must react with an available reagent at low temperature to form a **readily volatile compound**.\n"
                  "2. The volatile compound must easily **decompose at a higher temperature to regenerate the pure metal**."),
            ("table", ["Process Name", "Target Metal", "Formation Reaction (Low Temp)", "Decomposition Reaction (High Temp)"], [
                ["**Mond's Process**", "**Nickel (Ni)**", "**Ni + 4CO —(330 - 350 K)→ Ni(CO)~4~(g)**\nForms volatile, tetrahedral Nickel tetracarbonyl", "**Ni(CO)~4~ —(450 - 470 K)→ Ni(s) + 4CO(g) ↑**\nPure Ni deposits on heated pellets; CO recycled!"],
                ["**Van Arkel - de Boer Process**", "**Titanium (Ti), Zirconium (Zr), Hafnium (Hf), Boron**", "**Zr(s) + 2I~2~(g) —(870 K)→ ZrI~4~(g)**\n(Crude metal reacts in evacuated vessel)", "**ZrI~4~(g) —(W filament, 2075 K)→ Zr(s) + 2I~2~(g) ↑**\nDecomposes on white-hot filament; strips interstitial O~2~/N~2~!"]
            ], [22, 18, 30, 30], "Table 3.1 — Vapour phase refining pathways tested in JEE Advanced."),
            ("trap", "TRAP: Van Arkel process is specifically designed to eliminate trace interstitial impurities of **Oxygen and Nitrogen** that cause severe embrittlement in space-grade Ti and Zr metals!")
        ]
    },

    # ------------------------------------------------------------------ MT-15
    {
        "id": "MT-15",
        "title": "Electrolytic Refining: Anode Mud, Overvoltage & Recovery of Precious Metals",
        "blocks": [
            ("lead", "**Electrolytic Refining (Electro-Refining)** — Ultimate Purity for Copper, Silver & Gold"),
            ("p", "Electro-refining yields commercial copper (>99.95%) suitable for electrical wiring, where even 0.05% arsenic or iron reduces conductivity by >10%."),
            ("h2", "1. Electro-Refining Setup for Copper"),
            ("table", ["Cell Component", "Physical Material Used", "Electrochemical Function / Mechanism"], [
                ["**Anode (+)**", 'Thick cast slabs of **crude Blister Copper** (≈98% pure)', "Oxidizes copper and more electropositive base metals into solution:\nCu(s) → Cu^2+^(aq) + 2e^−^"],
                ["**Cathode (−)**", "Very thin sheets of **pure Copper** coated with graphite", "Selectively plates out pure copper metal from electrolyte:\nCu^2+^(aq) + 2e^−^ → Cu(s)"],
                ["**Electrolyte**", 'Acidified aqueous CuSO~4~ (≈15% CuSO~4~ + 5% H~2~SO~4~)', "Provides high Cu^2+^ ionic flux; H~2~SO~4~ prevents hydrolysis of Cu^2+^"],
                ["**Operating Voltage**", 'Low voltage (≈0.2 – 0.4 V) precisely controlled', "Prevents more electropositive base metals from discharging at cathode"]
            ], [18, 26, 32, 24], "Table 3.2 — Electro-refining cell parameters."),
            ("h2", "2. Anode Mud (Anode Slime) — Chemistry & Economic Value"),
            ("p", "Impurities present in crude blister copper behave in two distinct ways based on their standard reduction potentials (E°):\n"
                  "• **More Electropositive Impurities (Fe, Zn, Ni):** Have more negative reduction potentials than copper (E° < +0.34 V). They oxidize preferentially into the electrolyte as Fe^2+^, Zn^2+^, Ni^2+^ ions, but **DO NOT plate out at the cathode** because Cu^2+^ is much more readily reduced!\n"
                  "• **Less Electropositive / Noble Impurities (Ag, Au, Pt, Se, Te, Sb):** Have positive reduction potentials (E° > +0.34 V). They are **NOT oxidized** at the low operating voltage and drop from the dissolving anode as an insoluble sludge called **ANODE MUD**!\n"
                  "• *Economic Impact:* The recovery of gold, silver, and platinum from anode mud completely covers the electrical cost of the entire refining plant!"),
            ("key", "Chromatographic Refining (NCERT §6.5): Based on differential adsorption of components of a mixture on an adsorbent (e.g. Al~2~O~3~ column). Used for separating micro-gram quantities of lanthanoids and actinoids.")
        ]
    },

    # ------------------------------------------------------------------ MT-16
    {
        "id": "MT-16",
        "title": "Extraction of Iron: The Blast Furnace Architecture, Zones & Reactions",
        "blocks": [
            ("lead", "**Industrial Pyrometallurgy of Iron** — The Blast Furnace (NCERT §6.6)"),
            ("p", 'Iron is extracted from Haematite (Fe~2~O~3~) in a colossal vertical tower (blast furnace, ≈30 m high) lined with refractory fire-bricks, operating continuously for years under a counter-current flow of solids and hot gas.'),
            ("fig", "blast_furnace", "Fig. 3.2 — The Blast Furnace: Reduction zones, slag formation, combustion hearth, and forms of iron."),
            ("h2", "1. Thermal Zones & Stepwise Chemical Transformations"),
            ("table", ["Zone & Temp Range", "Primary Chemical Reactions", "Thermodynamic Role / Nature"], [
                ["**1. Zone of Reduction**\n(Top of stack, 500 – 800 K)", "3 Fe~2~O~3~ + CO → 2 Fe~3~O~4~ + CO~2~\nFe~3~O~4~ + 4 CO → 3 Fe + 4 CO~2~\nFe~2~O~3~ + CO → 2 FeO + CO~2~", "Exothermic gas-solid reduction;\nCO is the primary reducing agent (Ellingham: CO → CO~2~ lies lower)"],
                ["**2. Zone of Slag Formation**\n(Belly / Middle, 900 – 1200 K)", "CaCO~3~ —(Δ)→ CaO + CO~2~ ↑ (Calcination)\nCaO + SiO~2~ → CaSiO~3~ (Slag formation)\nFeO + CO → Fe + CO~2~", "Flux CaO captures quartz gangue SiO~2~;\nFusible molten CaSiO~3~ floats above molten iron"],
                ["**3. Zone of Fusion & Carburization**\n(Bosh, 1200 – 1500 K)", 'Spongy iron absorbs carbon (lowering its m.p. from 1811 K to ≈1473 K) and melts;\nFeO + C → Fe + CO (Direct carbon reduction)', 'Endothermic direct reduction by coke;\nCarbon dissolution creates Pig Iron (≈4% C)'],
                ["**4. Zone of Combustion**\n(Hearth / Tuyeres, 1500 – 2170 K)", 'C + O~2~ → CO~2~ (ΔH = −393.5 kJ, T ≈ 2170 K)\nC + CO~2~ → 2 CO (ΔH = +163.2 kJ, Boudouard)', "Blasts of preheated air burn coke to CO~2~, which immediately reduces to CO reducing gas"]
            ], [22, 44, 34], "Table 3.3 — Comprehensive thermal and chemical zones of the blast furnace."),
            ("trap", "TRAP: Does haematite get reduced directly to Fe in a single step? NO! Reduction proceeds strictly sequentially: Fe~2~O~3~ → Fe~3~O~4~ → FeO → Fe!")
        ]
    },

    # ------------------------------------------------------------------ MT-17
    {
        "id": "MT-17",
        "title": "Extraction of Copper: Smelting, Copper Matte & Bessemerization",
        "blocks": [
            ("lead", "**Pyrometallurgy of Copper from Chalcopyrite** — Matte Smelting & Auto-Reduction (NCERT §6.6)"),
            ("p", "Copper pyrites (CuFeS~2~) contains equal molar amounts of copper and iron. The central metallurgical challenge is the **preferential removal of iron as slag** prior to reducing copper sulphide."),
            ("fig", "copper_bessemer", "Fig. 3.3 — Copper pyrometallurgy: Roasting, smelting in reverberatory furnace, Bessemerization, and blister formation."),
            ("h2", "1. Stepwise Metallurgy of Copper Pyrites"),
            ("bul", [
                "**Step 1: Crushing & Froth Floatation:** Concentrated using pine oil and potassium ethyl xanthate collector.",
                '**Step 2: Roasting in Reverberatory Furnace:** Heated in excess air to remove moisture, arsenic, and antimony as volatile oxides:\n2 CuFeS~2~ + O~2~ → Cu~2~S + 2 FeS + SO~2~ ↑ 2 FeS + 3 O~2~ → 2 FeO + 2 SO~2~ ↑',
                '**Step 3: Smelting in Reverberatory Furnace (+ Silica Flux):** Roasted ore is mixed with **coke and acidic flux SiO~2~**. Because Iron has a higher affinity for oxygen than copper, FeO preferentially reacts with SiO~2~:\n**FeO + SiO~2~ → FeSiO~3~(l)** (Fusible slag floats on top!)\nThe heavier bottom molten layer is **COPPER MATTE** (primarily Cu~2~S + trace FeS, ≈45–50% Cu).',
                '**Step 4: Bessemerization (Pear-shaped, silica-lined converter):** Hot air blast oxidizes residual FeS to FeO, captured by the silica lining as FeSiO~3~ slag. Then, **auto-reduction** converts Cu~2~S to molten copper:\n2 Cu~2~S + 3 O~2~ → 2 Cu~2~O + 2 SO~2~ ↑ **2 Cu~2~O + Cu~2~S → 6 Cu(l) + SO~2~ ↑**',
                '**Step 5: Solidification:** Cooling molten copper releases dissolved SO~2~ gas, creating blisters on the surface (**Blister Copper**, ≈98% pure). Refined by electro-refining.'
            ]),
            ("trap", "EXAMINER TRAP: Copper Matte composition is a universal favourite in JEE! Matte is a mixture of **Cu~2~S and FeS** (NEVER CuS or Fe~2~S~3~!).")
        ]
    },

    # ------------------------------------------------------------------ MT-18
    {
        "id": "MT-18",
        "title": "Extraction of Aluminium, Zinc, Gold & Master Reagents Matrix",
        "blocks": [
            ("lead", "**Hall-Héroult, Hydrometallurgy & Master Synthesis Matrix** (NCERT §6.6 & §6.7)"),
            ("p", "A high-density master reference sheet consolidating aluminium electrometallurgy, zinc pyrometallurgy, gold/silver hydrometallurgy, and industrial metallurgical constants."),
            ("fig", "hall_heroult", "Fig. 3.4 — Hall-Héroult Electrolytic Cell: Carbon cathode lining, graphite anodes, and cryolite electrolyte."),
            ("h2", "1. Hall-Héroult Process Constants & Traps (NCERT §6.6)"),
            ("bul", [
                '**Electrolyte Formulation:** Purified Al~2~O~3~ (≈5%) dissolved in molten **Cryolite (Na~3~AlF~6~, ≈85%)** and **Fluorspar (CaF~2~, ≈10%)** at 1170–1220 K.',
                '**Why add Cryolite & CaF~2~?** Pure alumina melts at an impractically high 2320 K and is an electrical insulator. Cryolite acts as a solvent, dramatically lowers the melting point to ≈1170 K, and provides mobile ions for high electrical conductivity!',
                '**Carbon Anode Consumption Trap:** At the anode, oxygen anions discharge to form CO and CO~2~: C + 2 O^2−^ → CO~2~ + 4 e^−^. For **EVERY 1 kg of aluminium produced, ≈0.5 kg of graphite anode is burned away**! Anodes must be continuously replaced.'
            ]),
            ("h2", "2. Master Synthesis Matrix: Complete Extraction Pathways for JEE Advanced"),
            ("table", ["Metal", "Principal Ore", "Beneficiation Method", "Conversion to Oxide", "Primary Reduction Process", "Final Refining Method"], [
                ["**Al**", "Bauxite (Al~2~O~3~·2H~2~O)", "Bayer's / Hall's Leaching", "Calcination (1470 K)", "**Hall-Héroult Electrolysis** (fused cryolite)", "Hoope's Three-Layer Electrolytic Process"],
                ["**Fe**", "Haematite (Fe~2~O~3~)", "Gravity wash + Magnetic", "Calcination in kiln", "**Carbon / CO Smelting** in Blast Furnace", "Puddling furnace to wrought iron; Bessemer/BOS to steel"],
                ["**Cu**", "Chalcopyrite (CuFeS~2~)", "Froth Floatation (pine oil)", "Partial Roasting", "**Smelting + Self-Reduction** in Bessemer converter", "**Electro-refining** (anode mud yields Au, Ag)"],
                ["**Zn**", "Sphalerite (ZnS)", "Froth Floatation", "Roasting to ZnO", "**Carbon Reduction** in vertical retort (1673 K)", "Fractional Distillation (removes Pb, Cd)"],
                ["**Pb**", "Galena (PbS)", "Froth Floatation", "Partial Roasting", "**Self-Reduction** (reverberatory hearth)", "Parke's / Pattinson's process (Ag removal) + Bett's process"],
                ["**Sn**", "Cassiterite (SnO~2~)", "Magnetic (removes wolframite)", "Roasting (removes S, As)", "**Carbon Smelting** in reverberatory furnace", "Liquation followed by Poling"],
                ["**Au / Ag**", "Native Au / Argentite (Ag~2~S)", "Crushing & Pulverization", "None (Direct leaching)", "**Cyanide Hydrometallurgy + Zn displacement**", "Cupellation (removes Pb) + Electrolytic refining"]
            ], [10, 18, 18, 16, 20, 18], "Table 3.4 — Master Extractive Metallurgy matrix across all metals for JEE Advanced.")
        ]
    }
]
