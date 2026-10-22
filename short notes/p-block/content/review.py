# -*- coding: utf-8 -*-
"""Cross-Group Master Review Sheets (2 sheets / pages REV-01 to REV-02)."""

SHEETS = [
    # ------------------------------------------------------------------ REV-01
    {
        "id": "REV-01",
        "title": "Master Cross-Group Comparison: Trends, Inert Pair, Lewis Acidity",
        "blocks": [
            ("lead", "**Master Cross-Group Review** — Comparative Periodic Trends Across Groups 13 to 18"),
            ("p", "A consolidated comparison of anomalous trends, inert pair redox patterns, and Lewis acidity across all six p-block groups."),
            ("h2", "1. Atomic Radii & Ionization Energy Anomalies Summary"),
            ("table", ["Property / Trend", "Standard Group Expectation", "Actual Observed Sequence & Underlying Physical Reason"], [
                ["Atomic Radius in G13", "B < Al < Ga < In < Tl", '**B < Ga < Al < In ≈ Tl** (Ga < Al due to 3d transition contraction, d^10^ poor shielding)'],
                ["Ionization Enthalpy in G13", "B > Al > Ga > In > Tl", '**B > Tl > Ga > Al > In** (Tl > In due to 4f lanthanoid contraction, high Z~eff~)'],
                ["Ionization Enthalpy in G14", "C > Si > Ge > Sn > Pb", "**C > Si > Ge > Pb > Sn** (Pb > Sn due to 4f contraction)"],
                ["IE-1: G15 vs G16", "Group 16 > Group 15", '**Group 15 > Group 16** (N > O, P > S, As > Se due to stable half-filled np^3^ configuration)'],
                ["Electron Gain Enthalpy (G16)", "O > S > Se > Te", "**S > Se > Te > Po > O** (Oxygen is LEAST negative due to compact 2p inter-electronic repulsions)"],
                ["Electron Gain Enthalpy (G17)", "F > Cl > Br > I", "**Cl > F > Br > I** (Chlorine is MOST negative in entire periodic table; F has compact 2p repulsions)"],
                ["Bond Dissociation Energy (G17)", "F2 > Cl2 > Br2 > I2", "**Cl2 > Br2 > F2 > I2** (F2 has low bond energy due to severe lone-pair repulsions, 143 pm)"],
            ], [25, 25, 50], "Table R.1 — Master compendium of p-block periodic anomalies."),
            ("h2", "2. The Inert Pair Effect Matrix Across p-Block"),
            ("table", ["Group", "Lower State (+n)", "Higher State (+n+2)", "Oxidising Agent (+n+2 State)", "Reducing Agent (+n State)"], [
                ["Group 13", '+1 (Tl^+^ stable)', '+3 (B^3+^, Al^3+^ stable)', '**Tl^3+^ is strongly oxidising** (Tl^3+^ + 2e^-^ → Tl^+^)', 'Al^+^, Ga^+^ (disproportionate)'],
                ["Group 14", '+2 (Pb^2+^ stable)', '+4 (C^4+^, Si^4+^ stable)', '**Pb^4+^ is strongly oxidising** (PbO2 + 4 HCl → PbCl2 + Cl2)', '**Sn^2+^ is strongly reducing** (Sn^2+^ → Sn^4+^ + 2e^-^)'],
                ["Group 15", '+3 (Bi^3+^ stable)', '+5 (N^5+^, P^5+^ stable)', '**Bi^5+^ is strongly oxidising** (NaBiO3 oxidises Mn^2+^ to MnO4^-^)', 'P^3+^, As^3+^ (mild reducing)'],
            ], [15, 20, 20, 25, 20], "Table R.2 — Comparative redox chemistry governed by the inert pair effect."),
            ("key", "Inert Pair Generalisation:\n"
                    "• The lower oxidation state becomes progressively **MORE stable** descending the group: Tl(+) > In(+) > Ga(+) > Al(+) > B(+).\n"
                    "• The higher oxidation state becomes progressively **A STRONGER OXIDANT** descending the group: Tl(3+) > In(3+) > Ga(3+) > Al(3+)."),
        ],
    },
    # ------------------------------------------------------------------ REV-02
    {
        "id": "REV-02",
        "title": "Complete Hydrolysis Map: p-Block Halides, Oxides & Oxychlorides",
        "blocks": [
            ("lead", "**Complete Hydrolysis Map** — Mechanisms, Redox vs Non-Redox & Intermediate Acids"),
            ("p", "Hydrolysis in the p-block occurs via two distinct pathways: nucleophilic attack on empty d orbitals (SN2-type), "
                  "or coordination to an empty p orbital (Lewis acid-base). Below is the comprehensive master reaction map."),
            ("h2", "1. Non-Redox Hydrolysis (Oxidation State Preserved)"),
            ("table", ["Substrate", "Hydrolysis Equation", "Nature of Attack / Intermediate"], [
                ["BCl3, BBr3, BI3", "BX3 + 3 H2O → **H3BO3 + 3 HX**", "Water attacks vacant 2p orbital on Boron"],
                ["BF3", "**4 BF3 + 3 H2O → H3BO3 + 3 H[BF4]**", "HF formed coordinates with unreacted BF3 to give fluoroboric acid!"],
                ["SiCl4", "SiCl4 + 4 H2O → **Si(OH)4 (Silicic acid) → SiO2·2H2O + 4 HCl**", "Attack on vacant 3d orbitals; coordination number expands to 6"],
                ["PCl3", "PCl3 + 3 H2O → **H3PO3 (Phosphorous acid) + 3 HCl**", "Preserves +3 state; lone pair remains on P"],
                ["PCl5", "PCl5 + H2O → **POCl3** + 2 HCl; POCl3 + 3 H2O → **H3PO4 + 3 HCl**", "Stepwise via phosphorus oxychloride"],
                ["SF4", "SF4 + 2 H2O → **SO2 + 4 HF**", "Water attacks vacant d-orbitals; preserves +4 state"],
                ["XeF6", "XeF6 + H2O → **XeOF4** + 2 HF → **XeO2F2** + 4 HF → **XeO3 + 6 HF**", "Stepwise replacement of F2 by =O; all preserve Xe(+6)"],
            ], [18, 42, 40], "Table R.3 — Master non-redox hydrolysis reactions."),
            ("h2", "2. Redox & Disproportionation Hydrolysis Reactions"),
            ("table", ["Substrate", "Reaction Equation", "Type of Redox Reaction"], [
                ["NCl3", "NCl3 + 3 H2O → **NH3 (-3) + 3 HOCl (+1)**", 'Non-redox on paper, but N acts as negative end (χ~N~ > χ~Cl~)! Cl goes to HOCl, NOT HCl!'],
                ["P4 (in alkali)", "P4 + 3 NaOH + 3 H2O → **PH3 (-3) + 3 NaH2PO2 (+1)**", "Disproportionation of White Phosphorus"],
                ["Cl2 (in water)", "Cl2 + H2O ⇌ **HCl (-1) + HOCl (+1)**", "Disproportionation (forms chlorine water; turns blue litmus red then bleaches)"],
                ["XeF2", "**2 XeF2 + 2 H2O → 2 Xe (0) + 4 HF + O2 (0)**", "**Redox:** Xe(+2) reduced to 0; H2O(-2) oxidised to O2(0)"],
                ["XeF4", "**6 XeF4 + 12 H2O → 2 XeO3 (+6) + 4 Xe (0) + 24 HF + 3 O2↑**", "**Disproportionation + Redox:** Xe(+4) splits into +6 and 0"],
            ], [18, 47, 35], "Table R.4 — Redox and disproportionation hydrolysis pathways in JEE."),
            ("key", "The Classic NCl3 vs NF3 vs PCl3 Hydrolysis Trap:\n"
                    "• **NF3:** Does NOT hydrolyse at all (no vacant d-orbitals, high bond strength, non-polar).\n"
                    '• **NCl3:** Hydrolyses to **NH3 + HOCl** (because χ~N~ = 3.0 > χ~Cl~ = 2.8; water attacks Cl with empty 3d orbitals!).\n'
                    '• **PCl3:** Hydrolyses to **H3PO3 + HCl** (because χ~P~ = 2.1 < χ~Cl~ = 3.0; water attacks P with empty 3d orbitals!).'),
        ],
    },
]
