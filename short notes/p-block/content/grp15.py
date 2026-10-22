# -*- coding: utf-8 -*-
"""Group 15: Nitrogen Family (10 sheets / pages G15-01 to G15-10)."""

SHEETS = [
    # ------------------------------------------------------------------ G15-01
    {
        "id": "G15-01",
        "title": "Group 15 Trends, Anomalous N, Catenation & Allotropy",
        "blocks": [
            ("lead", '**Group 15: Nitrogen Family (ns^2^ np^3^)** — Pnictogens & Periodic Trends'),
            ("p", "Contains N, P (non-metals), As, Sb (metalloids), Bi (post-transition metal). "
                  'The valence shell has a stable half-filled p^3^ configuration, resulting in unusually high ionization energies.'),
            ("h2", "1. Periodic Trends of Group 15"),
            ("table", ["Element", "Config.", "Covalent Radius (pm)", "IE-1 (kJ/mol)", "Electronegativity", "Allotropes"], [
                ["N", '[He] 2s^2^ 2p^3^', "70", "1402", "3.0", "Dinitrogen gas (α, β solid forms)"],
                ["P", '[Ne] 3s^2^ 3p^3^', "110", "1012", "2.1", "White, Red, Black (α, β), Violet"],
                ["As", '[Ar] 3d^10^ 4s^2^ 4p^3^', "121", "947", "2.0", "Grey (metallic), Yellow, Black"],
                ["Sb", '[Kr] 4d^10^ 5s^2^ 5p^3^', "141", "834", "1.9", "Metallic (silver-grey), Yellow, Black"],
                ["Bi", '[Xe] 4f^14^ 5d^10^ 6s^2^ 6p^3^', "148", "703", "1.9", "White with pinkish tinge (only 1 form)"],
            ], [10, 24, 20, 16, 14, 16], "Table 15.1 — Physical and atomic properties of Group 15 elements."),
            ("key", 'IE-1 is substantially higher than Group 16 elements (e.g., IE~1~(N) = 1402 > IE~1~(O) = 1314 kJ/mol) '
                    'due to the extra stability of the half-filled 2p^3^ subshell in Nitrogen!'),
            ("h2", "2. Anomalous Behaviour of Nitrogen"),
            ("bul", [
                "**Small size & High Electronegativity:** Forms very strong **pπ-pπ triple bonds** (:N≡N: bond energy = 945.8 kJ/mol). Nitrogen exists as a chemically inert diatomic gas at RTP.",
                "**Single Bond Anomaly (N-N vs P-P):** N-N single bond energy (160 kJ/mol) is **much WEAKER** than P-P single bond energy (213 kJ/mol) due to intense inter-electronic repulsion between lone pairs in the compact 2p shell. Hence, **catenation in N is very limited** compared to P.",
                '**Absence of d-orbitals:** Nitrogen has a **maximum covalency of 4** (one 2s and three 2p orbitals). It CANNOT form pentahalides (NF5 does not exist) or expand octet like P (PCl5, PF6^-^).',
            ]),
            ("h2", "3. Oxidation States & Inert Pair Effect"),
            ("p", "Common states: -3, +3, +5. Moving down the group:\n"
                  '• **-3 state stability decreases:** Bi^3-^ is virtually unknown due to metallic electropositive nature.\n'
                  '• **+5 state stability decreases:** Bi(+5) is unstable and a **powerful oxidising agent** (BiF5 is known, but BiCl5 does not exist; NaBiO3 is a classic analytical oxidant for Mn^2+^ → MnO4^-^).\n'
                  "• **+3 state stability increases:** Bi(+3) is the most stable state of Bismuth due to the **inert pair effect**."),
        ],
    },
    # ------------------------------------------------------------------ G15-02
    {
        "id": "G15-02",
        "title": "Dinitrogen N2 & Active Nitrogen",
        "blocks": [
            ("lead", "**Dinitrogen (N2)** — Preparation, Inertness, Fixation & Chemical Reactions"),
            ("p", "Constitutes 78% of air by volume. Colorless, odorless, diamagnetic gas, condensation temp 77.2 K."),
            ("h2", "1. Laboratory & High-Purity Preparations"),
            ("table", ["Method", "Reaction Equation", "Purity & Key Notes"], [
                ["Aqueous Nitrite Reaction", "NH4Cl(aq) + NaNO2(aq) → **N2↑** + NaCl + 2 H2O", "Standard lab prep; contains trace NO and HNO3 impurities (purified by passing through aq. H2SO4 + K2Cr2O7)"],
                ["Thermal Decomposition of Dichromate", '(NH4)2Cr2O7 —(Δ)→ **N2↑** + Cr2O3 (green solid) + 4 H2O', "Volcano reaction; exothermic decomposition of orange crystals"],
                ["Thermal Azide Decomposition", 'Ba(N3)2 —(300°C)→ Ba + **3 N2↑** or 2 NaN3 → 2 Na + **3 N2↑**', "**Ultra-pure N2 (>99.99%)**; sodium azide used in automobile airbags!"],
                ["Oxidation of Ammonia", "8 NH3 + 3 Cl2 (excess NH3) → **N2↑** + 6 NH4Cl  or  2 NH3 + 3 CuO → **N2↑** + 3 Cu + 3 H2O", "Yellow liquid NCl3 formed if Cl2 is in excess!"],
            ], [22, 42, 36], "Table 15.2 — Synthetic routes to Dinitrogen."),
            ("key", "Ultra-Pure Nitrogen is prepared exclusively by the **thermal decomposition of sodium or barium azide** NaN3 / Ba(N3)2."),
            ("h2", "2. Chemical Reactivity of N2"),
            ("p", "Remarkably unreactive at room temperature because of the immense bond dissociation enthalpy of N≡N (945.8 kJ/mol). "
                  "Becomes active only at elevated temperatures:"),
            ("bul", [
                "**With Metals (Nitrides):** 6 Li + N2 → 2 Li3N (ruby red ionic solid); 3 Mg + N2 → Mg3N2 (reacts with water to evolve NH3: Mg3N2 + 6 H2O → 3 Mg(OH)2 + 2 NH3↑).",
                "**With Non-Metals:**\n"
                "  • N2 + 3 H2 ⇌ 2 NH3 (Haber process, 700 K, 200 atm, Fe/Mo catalyst, ΔH = -92.4 kJ/mol).\n"
                "  • N2 + O2 ⇌ 2 NO (Electric arc, T > 2000 K, Birkeland-Eyde process, endothermic ΔH = +180 kJ/mol).",
                "**Nitrolim Formation:** CaC2 + N2 —(1373 K)→ **CaCN2 + C** ('Nitrolim' or Calcium Cyanamide). Used as an agricultural fertilizer; slowly hydrolyses in soil to urea and ammonia: CaCN2 + 3 H2O → CaCO3 + 2 NH3.",
            ]),
        ],
    },
    # ------------------------------------------------------------------ G15-03
    {
        "id": "G15-03",
        "title": "Ammonia NH3 & Liquid Ammonia as Non-Aqueous Solvent",
        "blocks": [
            ("lead", "**Ammonia (NH3)** — Haber Synthesis, Molecular Properties & Liquid NH3 Solvent"),
            ("p", 'Trigonal pyramidal geometry (sp^3^ hybridized, one lone pair, bond angle 107.8°, dipole moment 1.47 D). '
                  "Associated in liquid and solid states via intermolecular hydrogen bonding."),
            ("h2", "1. Synthesis: The Haber-Bosch Process"),
            ("key", "N2(g) + 3 H2(g) ⇌ 2 NH3(g)   ΔH° = -92.4 kJ/mol (Exothermic)\n"
                    'Optimum Le Chatelier conditions: High pressure (≈200 atm), Moderate temperature (≈700 K), '
                    "Catalyst: Iron oxide (FeO/Fe2O3) with promoter K2O and Al2O3 (increases surface area and activity)."),
            ("h2", "2. Chemical Reactions of NH3"),
            ("bul", [
                '**Basic Nature & Salt Formation:** Weak base in water (K~b~ = 1.8 × 10^-5^). Forms ammonium salts with acids (NH3 + HCl → NH4Cl white dense fumes).',
                '**Precipitation of Metal Hydroxides:** Fe^3+^ + 3 NH4OH → Fe(OH)3↓ (reddish brown); Zn^2+^ + 2 NH4OH → Zn(OH)2↓ (white, dissolves in excess NH3 forming [Zn(NH3)4]^2+^).',
                "**Complexation with Transition Metals (Deep Blue / Colour Changes):**\n"
                '  • Cu^2+^(aq) (pale blue) + 4 NH3 → **[Cu(NH3)4]^2+^** (tetraamminecopper(II), deep Prussian blue).\n'
                '  • AgCl↓ (white precipitate) + 2 NH3 → **[Ag(NH3)2]^+^** + Cl^-^ (soluble diamminesilver(I)).',
                "**Nessler's Reagent Test:** Alkaline K2[HgI4] + NH3 → **[HgO·Hg(NH2)I]↓** (Iodide of Millon's base, brown precipitate). Extremely sensitive qualitative test for NH4^+^.",
            ]),
            ("h2", "3. Liquid Ammonia as a Non-Aqueous Ionising Solvent"),
            ("p", 'Liquid NH3 (bp -33°C) autoionizes: 2 NH3 ⇌ NH4^+^ (acid analogue) + NH2^-^ (base analogue). '
                  "Alkali metals dissolve in liquid ammonia giving spectacular solutions:"),
            ("table", ["Concentration", "Colour & Magnetic Property", "Active Species & Behaviour"], [
                ["Dilute Solution (<3 M)", "**Deep Blue**, strongly **paramagnetic**", '**Ammoniated electrons [e(NH3)~y~]^-^**: Powerful reducing agent (Birch reduction)'],
                ["Concentrated (>3 M)", "**Bronze / Copper luster**, **diamagnetic**", "Electrons pair up to form diamagnetic electron pairs; metallic electrical conductivity"],
            ], [22, 28, 50], "Table 15.3 — Metal-ammonia solutions (NCERT & JD Lee core)."),
        ],
    },
    # ------------------------------------------------------------------ G15-04
    {
        "id": "G15-04",
        "title": "Hydrazine N2H4, Hydroxylamine NH2OH & Hydrazoic Acid HN3",
        "blocks": [
            ("lead", "**Nitrogen Hydrides & Derivatives** — N2H4, NH2OH, HN3 & Redox Chemistry"),
            ("p", "Nitrogen forms a remarkable sequence of hydrides spanning oxidation states from -3 to -1/3."),
            ("h2", "1. Hydrazine (N2H4, H2N-NH2, Oxidation State = -2)"),
            ("bul", [
                '**Raschig Synthesis:** 2 NH3 + NaOCl —(gelatin/glue catalyst)→ **N2H4** + NaCl + H2O.\n'
                '  (Gelatin complexes with heavy metal ions like Cu^2+^ which would otherwise catalyse hydrazine decomposition!).',
                '**Structure:** Gauche conformation (dihedral angle ≈ 90° to minimise lone-pair repulsions, sp^3^ N atoms).',
                '**Reactions & Uses:** Fuming colorless liquid, bifunctional weak base (pK~b1~ = 6.07). Powerful **reducing agent**:\n'
                "  N2H4 + 2 I2 → N2↑ + 4 HI  (quantitative, no residue; hence used as rocket propellant fuel with N2O4).",
            ]),
            ("h2", "2. Hydroxylamine (NH2OH, Oxidation State = -1)"),
            ("p", 'Prepared by electrolytic reduction of nitric acid: HNO3 + 6 H^+^ + 6 e^-^ → **NH2OH** + 2 H2O.\n'
                  "Acts as both oxidising and reducing agent:\n"
                  '• Reducing action: 2 NH2OH + 4 Fe^3+^ → N2O + 4 Fe^2+^ + 4 H^+^ + H2O.\n'
                  '• Oxidising action: NH2OH + 2 Fe^2+^ + 2 H^+^ → NH3 + 2 Fe^3+^ + H2O.\n'
                  "Forms **oximes** with aldehydes and ketones: R2C=O + NH2OH → R2C=N-OH + H2O."),
            ("h2", "3. Hydrazoic Acid & Azides (HN3, Oxidation State = -1/3)"),
            ("table", ["Compound / Ion", "Formal Oxidation State", "Structure & Geometry", "Safety / Stability"], [
                ["Hydrazoic acid HN3", "-1/3", "H-N1=N2=N3 (linear N-N-N backbone, angle 171°)", "Colorless, volatile liquid (bp 37°C), violently explosive!"],
                ['Azide Ion N3^-^', "-1/3", '[:N=N=N:]^-^ (symmetric linear, D~∞h~, N-N bond 116 pm)', "Pb(N3)2 used in percussion caps and explosive detonators"],
            ], [20, 18, 32, 30], "Table 15.4 — Azide systems in inorganic chemistry."),
            ("key", "Oxidation State Summary of Nitrogen Hydrides:\n"
                    "• **NH3:** -3  |  **N2H4:** -2  |  **NH2OH:** -1  |  **N2:** 0  |  **HN3:** -1/3"),
        ],
    },
    # ------------------------------------------------------------------ G15-05
    {
        "id": "G15-05",
        "title": "Oxides of Nitrogen (N2O, NO, N2O3, NO2, N2O4, N2O5)",
        "blocks": [
            ("lead", "**Oxides of Nitrogen** — Structures, Oxidation States, Colors & Magnetic Properties"),
            ("p", "Nitrogen forms six classic oxides across oxidation states from +1 to +5. Several possess odd electrons."),
            ("h2", "1. Comprehensive Summary of Nitrogen Oxides"),
            ("table", ["Oxide", "Oxid. State", "Prep Reaction", "Colour & Physical State", "Magnetic Nature"], [
                ["N2O (Nitrous oxide)", "+1", 'NH4NO3 —(Δ, 250°C)→ N2O + 2 H2O', "Colorless gas (Laughing gas)", "Diamagnetic (Neutral)"],
                ["NO (Nitric oxide)", "+2", "2 NaNO2 + 2 FeSO4 + 3 H2SO4 → Fe2(SO4)3 + 2 NaHSO4 + 2 H2O + 2 NO", "Colorless gas (Liquid is blue)", "**Paramagnetic (gas)**, Diamag (liquid/solid dimer) (Neutral)"],
                ["N2O3 (Sesquioxide)", "+3", '2 NO + N2O4 —(250 K)→ 2 N2O3', "**Deep Blue liquid** / solid", "Diamagnetic (Acidic)"],
                ["NO2 (Dioxide)", "+4", '2 Pb(NO3)2 —(Δ, 673 K)→ 2 PbO + 4 NO2 + O2', "**Brown gas**", "**Paramagnetic** (odd-electron molecule) (Acidic)"],
                ["N2O4 (Tetroxide)", "+4", "2 NO2 ←(cool / warm)→ N2O4", "Colorless liquid / solid", "Diamagnetic (Acidic)"],
                ["N2O5 (Pentoxide)", "+5", "4 HNO3 + P4O10 → 4 HPO3 + 2 N2O5", "Colorless crystalline solid", "Diamagnetic (Strongly Acidic)"],
            ], [15, 8, 35, 22, 20], "Table 15.5 — Complete spectrum of Nitrogen Oxides (NCERT & JD Lee core)."),
            ("key", "Neutral Oxides: **N2O and NO** are completely NEUTRAL to litmus! All other oxides (N2O3, NO2, N2O4, N2O5) are acidic anhydrides."),
            ("h2", "2. Bonding & Structural Details"),
            ("bul", [
                "**NO (Paramagnetic Monomer vs Diamagnetic Dimer):** Gas contains 11 valence electrons; unpaired electron resides in a π* antibonding molecular orbital (bond order 2.5). In liquid and solid states, it dimerises to planar cis-O=N-N=O, pairing electrons (diamagnetic).",
                "**NO2 ⇌ N2O4 Equilibrium:** NO2 has a single odd electron on N (brown, paramagnetic, bent O-N-O angle 134°). On cooling, two NO2 molecules dimerise to form planar N2O4 with an unusually long N-N bond (175 pm vs normal 145 pm) due to repulsion between bonding pairs.",
                '**Solid N2O5 Ionic Lattice:** In the gas phase, N2O5 is molecular (O2N-O-NO2). In the **solid crystalline state**, it exists as an ionic salt: **[NO2]^+^ [NO3]^-^ (Nitronium nitrate)**! Linear [NO2]^+^ cation + planar trigonal [NO3]^-^ anion.',
            ]),
            ("trap", 'TRAP: Liquid N2O4 undergoes auto-ionization: N2O4 ⇌ NO^+^ (nitrosyl cation) + NO3^-^ (nitrate anion). It acts as a non-aqueous solvent where NOCl acts as an acid and AgNO3 acts as a base!'),
        ],
    },
    # ------------------------------------------------------------------ G15-06
    {
        "id": "G15-06",
        "title": "Oxoacids of Nitrogen: HNO2, HNO3 & Brown Ring Test",
        "blocks": [
            ("lead", "**Oxoacids of Nitrogen** — Nitrous Acid, Nitric Acid & The Brown Ring Test Mechanism"),
            ("p", "Primary oxoacids: Nitrous acid HNO2 (+3, unstable, weak acid) and Nitric acid HNO3 (+5, strong acid & oxidising agent)."),
            ("h2", "1. Nitrous Acid (HNO2) & Disproportionation"),
            ("p", 'Prepared freshly in cold: NaNO2 + HCl —(0-5°C)→ NaCl + HNO2. On warming, it **disproportionates**:\n'
                  '3 HNO2 —(warm)→ **HNO3 (+5) + 2 NO (+2) + H2O**.\n'
                  'Acts as both oxidising agent (oxidises I^-^ to I2) and reducing agent (decolourises KMnO4).'),
            ("h2", "2. Nitric Acid (HNO3) Manufacture: Ostwald Process"),
            ("bul", [
                '**Step 1 (Catalytic Oxidation):** 4 NH3(g) + 5 O2(g) —(Pt-Rh gauze, 1150 K, 9 bar)→ **4 NO(g)** + 6 H2O(g) (exothermic).',
                "**Step 2 (Dimerization / Oxidation):** 2 NO(g) + O2(g) ⇌ **2 NO2(g)**.",
                "**Step 3 (Absorption in Water):** 3 NO2(g) + H2O(l) → **2 HNO3(aq) + NO(g)** (NO is recycled back to Step 2).",
            ]),
            ("h2", "3. Oxidising Action of HNO3 on Metals"),
            ("table", ["Metal", "Concentration of HNO3", "Oxidation Product & Nitrogen Gas Evolved"], [
                ["Copper (Cu)", 'Dilute HNO3 (≈20%)', "3 Cu + 8 HNO3 → 3 Cu(NO3)2 + 4 H2O + **2 NO↑** (Nitric oxide)"],
                ["Copper (Cu)", 'Concentrated HNO3 (≈70%)', "Cu + 4 HNO3 → Cu(NO3)2 + 2 H2O + **2 NO2↑** (Brown gas)"],
                ["Zinc (Zn)", 'Dilute HNO3 (≈20%)', "4 Zn + 10 HNO3 → 4 Zn(NO3)2 + 5 H2O + **N2O↑** (Nitrous oxide)"],
                ["Zinc (Zn)", 'Concentrated HNO3 (≈70%)', "Zn + 4 HNO3 → Zn(NO3)2 + 2 H2O + **2 NO2↑** (Brown gas)"],
                ["Zinc (Zn)", 'Very Dilute HNO3 (≈6%)', "4 Zn + 10 HNO3 → 4 Zn(NO3)2 + 3 H2O + **NH4NO3** (Ammonium nitrate)"],
            ], [15, 25, 60], "Table 15.6 — Reaction of metals with dilute vs concentrated Nitric Acid (JEE Classic)."),
            ("h2", '4. Mechanism of the Brown Ring Test for Nitrate (NO3^-^)'),
            ("p", "Aqueous nitrate + freshly prepared FeSO4 + conc. H2SO4 carefully poured down the side of the test tube:\n"
                  '1. Reduction: NO3^-^ + 3 Fe^2+^ + 4 H^+^ → 3 Fe^3+^ + **NO** + 2 H2O.\n'
                  '2. Coordination & Complex Formation: [Fe(H2O)6]^2+^ + NO → **[Fe(H2O)5(NO)]^2+^** (Brown Ring) + H2O.'),
            ("key", '**Oxidation State of Fe in Brown Ring Complex [Fe(H2O)5(NO)]^2+^:**\n'
                    'One electron is transferred from NO to Fe^2+^, creating **Fe(+I) (d^7^, t2g^5^ eg^2^)** and **NO^+^ (nitrosonium ion)**!\n'
                    "Magnetic Moment: **μ = √15 ≈ 3.87 BM (3 unpaired electrons)**. This is a critical JEE Advanced question."),
        ],
    },
    # ------------------------------------------------------------------ G15-07
    {
        "id": "G15-07",
        "title": "Phosphorus Allotropes (White, Red, Black) & PH3",
        "blocks": [
            ("lead", "**Phosphorus Allotropes & Phosphine** — White, Red, Black Allotropy & PH3 Smoke Rings"),
            ("p", "Phosphorus exists in three major allotropic forms: White (P4), Red (polymeric), and Black (layered)."),
            ("h2", "1. Comparative Allotropy of Phosphorus"),
            ("table", ["Property", "White Phosphorus", "Red Phosphorus", "Black Phosphorus (α and β)"], [
                ["Molecular Structure", "Discrete P4 tetrahedra (angle 60°)", "Complex 3D polymer of linked P4 rings", "Layered puckered hexagonal sheets (flaky)"],
                ["Physical State", "Translucent waxy solid (soft, cuts with knife)", "Reddish-violet powdery solid (odorless)", "Black lustrous flaky solid (graphite-like)"],
                ["Toxicity & Chemiluminescence", "**Highly toxic**, glows green in dark (chemiluminescence)", "**Non-toxic**, does NOT glow in dark", "Non-toxic, completely non-reactive"],
                ["Reactivity & Ignition", "Spontaneously catches fire in air at 30°C (kept under water!)", "Stable in air, ignites at 260°C", "Least reactive, highly inert"],
                ["Solubility", "Insoluble in H2O, soluble in CS2 and benzene", "Insoluble in both H2O and CS2", "Insoluble in all ordinary solvents"],
            ], [18, 26, 28, 28], "Table 15.7 — Comparison of Phosphorus allotropes (NCERT core)."),
            ("fig", "phosphorus", "Fig. 15.1 — White P4 discrete tetrahedron vs Red Phosphorus polymeric chain."),
            ("h2", "2. Phosphine (PH3) — Synthesis & Reactions"),
            ("bul", [
                "**Preparation (Disproportionation of White P4):**\n"
                '  P4 + 3 NaOH + 3 H2O —(inert CO2 atm)→ **PH3↑ + 3 NaH2PO2** (Sodium hypophosphite, +1 state).\n'
                "  (Pure PH3 is non-flammable; it catches fire spontaneously due to traces of **P2H4 (diphosphane)** impurity!).",
                "**Holmes Smoke Signals:** Containers of CaC2 + Ca3P2 pierced and thrown into sea. Water reacts:\n"
                "  Ca3P2 + 6 H2O → 3 Ca(OH)2 + 2 PH3↑ (contains P2H4 → ignites → produces vortex smoke rings of P4O10).\n"
                "  CaC2 + 2 H2O → Ca(OH)2 + C2H2↑ (acetylene burns giving bright illuminating flame).",
                "**Basicity:** PH3 is a very weak base (much weaker than NH3, no H-bonding, Drago's rule: unhybridized pure p-orbital lone pair). Only forms salts with strong acids: PH3 + HI → **PH4I** (Phosphonium iodide).",
            ]),
        ],
    },
    # ------------------------------------------------------------------ G15-08
    {
        "id": "G15-08",
        "title": "Halides of Phosphorus: PCl3 & PCl5 (Gas vs Solid)",
        "blocks": [
            ("lead", "**Phosphorus Halides** — PCl3, PCl5, Axial/Equatorial Bonds & Solid-State Ionization"),
            ("p", 'Phosphorus forms trihalides PX3 (sp^3^ pyramidal) and pentahalides PX5 (sp^3^d trigonal bipyramidal).'),
            ("h2", "1. Phosphorus Trichloride (PCl3)"),
            ("bul", [
                "**Synthesis:** P4 + 6 Cl2 (dry, limited) → 4 PCl3  (or: P4 + 8 SOCl2 → 4 PCl3 + 4 SO2 + 2 S2Cl2).",
                '**Structure:** Pyramidal (sp^3^ P, one lone pair, P-Cl bond length 204 pm).',
                "**Hydrolysis:** PCl3 + 3 H2O → **H3PO3** + 3 HCl (violent, fumes copiously in moist air).",
                "**Reactions with Organic OH:** 3 C2H5OH + PCl3 → 3 C2H5Cl + H3PO3; 3 CH3COOH + PCl3 → 3 CH3COCl + H3PO3.",
            ]),
            ("h2", "2. Phosphorus Pentachloride (PCl5) — Gas vs Solid State"),
            ("table", ["State of Matter", "Chemical Structure & Species Present", "Bond Lengths & Geometry"], [
                ["Gas Phase & Liquid", "Discrete molecular PCl5", 'Trigonal bipyramidal (sp^3^d): **3 equatorial bonds (202 pm) + 2 axial bonds (240 pm)**. Axial bonds are longer and weaker due to 3 × 90° repulsions!'],
                ["Solid Crystalline State", '**Ionic Solid:** [PCl4]^+^ [PCl6]^-^', '[PCl4]^+^ is **tetrahedral (sp^3^)**; [PCl6]^-^ is **octahedral (sp^3d^2)**!'],
                ["PBr5 Solid State", '**Ionic Solid:** [PBr4]^+^ [Br]^-^', '[PBr4]^+^ tetrahedral cation + Br^-^ anion (P is too small to coordinate 6 bulky Br atoms!)'],
            ], [18, 32, 50], "Table 15.8 — Gas-phase vs Solid-state structures of Phosphorus pentahalides."),
            ("key", "Why are axial bonds longer than equatorial bonds in PCl5?\n"
                    "Equatorial P-Cl bonds experience repulsion from only two adjacent bonds at 90°. "
                    "Each axial P-Cl bond experiences repulsion from **three equatorial bonds at 90°**, making them longer and weaker!"),
            ("h2", "3. Hydrolysis of PCl5"),
            ("p", "Stepwise hydrolysis:\n"
                  "• Step 1 (Limited water): PCl5 + H2O → **POCl3 (Phosphorus oxychloride)** + 2 HCl.\n"
                  "• Step 2 (Excess water): POCl3 + 3 H2O → **H3PO4 (Orthophosphoric acid)** + 3 HCl.\n"
                  "Net: **PCl5 + 4 H2O → H3PO4 + 5 HCl**."),
        ],
    },
    # ------------------------------------------------------------------ G15-09
    {
        "id": "G15-09",
        "title": "Oxides of Phosphorus: P4O6 & P4O10",
        "blocks": [
            ("lead", "**Oxides of Phosphorus** — P4O6, P4O10, Adamantane Cages & Dehydrating Power"),
            ("p", "Prepared by burning white phosphorus in air/oxygen: limited air gives P4O6, excess air gives P4O10."),
            ("h2", "1. Structure & Bonding of P4O6 and P4O10"),
            ("fig", "p4o10", "Fig. 15.2 — Adamantane cage architecture of P4O6 and P4O10."),
            ("table", ["Feature", "Phosphorus Trioxide (P4O6)", "Phosphorus Pentoxide (P4O10)"], [
                ["Combustion Condition", "P4 + 3 O2 (limited) → P4O6", "P4 + 5 O2 (excess) → P4O10"],
                ["Formal Oxidation State", "+3", "+5"],
                ["Number of P-O-P Bridges", "6 bridging P-O-P bonds", "6 bridging P-O-P bonds"],
                ["Terminal P=O Bonds", "0 (each P retains one lone pair)", "4 terminal P=O bonds (dπ-pπ backbonding)"],
                ["Total Number of P-O Bonds", "12 P-O single bonds", "**16 P-O bonds** (12 bridging + 4 terminal)"],
                ["Hybridization of P", 'sp^3^ (pyramidal at each P)', 'sp^3^ (tetrahedral at each P)'],
            ], [22, 38, 40], "Table 15.9 — Structural parameters of P4O6 vs P4O10 cages."),
            ("key", "Counting Bonds in P4O10 (Guaranteed JEE Question):\n"
                    "• Bridging P-O-P linkages = **6**\n"
                    "• Terminal P=O double bonds = **4**\n"
                    "• Total P-O single bond vectors in cage = **12** (plus 4 terminal = 16 total)"),
            ("h2", "2. Hydrolysis Pathways & Acid Anhydrides"),
            ("bul", [
                "**Hydrolysis of P4O6:** P4O6 + 6 H2O (cold) → **4 H3PO3 (Phosphorous acid)**.\n"
                "  (With hot water, disproportionates: P4O6 + 6 H2O → 3 H3PO4 + PH3↑).",
                "**Hydrolysis of P4O10:** Stepwise hydration:\n"
                '  P4O10 —(+2 H2O)→ 4 HPO3 (Metaphosphoric acid) —(+2 H2O)→ 2 H4P2O7 (Pyrophosphoric acid) —(+2 H2O)→ **4 H3PO4 (Orthophosphoric acid)**.',
                "**Powerful Dehydrating Action of P4O10:** It strips water from acids to generate anhydrides:\n"
                "  • 2 HNO3 + P4O10 → **N2O5** + 2 HPO3\n"
                "  • 2 H2SO4 + P4O10 → **2 SO3** + 4 HPO3\n"
                "  • 2 CH3CONH2 + P4O10 → **2 CH3CN (Acetonitrile)** + 4 HPO3\n"
                "  • (COOH)2 + P4O10 → **CO + CO2** + 2 HPO3",
            ]),
        ],
    },
    # ------------------------------------------------------------------ G15-10
    {
        "id": "G15-10",
        "title": "Oxoacids of Phosphorus: H3PO2, H3PO3, H3PO4, Polyphosphoric",
        "blocks": [
            ("lead", "**Oxoacids of Phosphorus** — Basicity, P-H Bonds & Reducing Power"),
            ("p", 'Phosphorus forms a famous series of oxoacids characterized by tetrahedral sp^3^ P atoms with '
                  "at least one P=O bond and one P-OH bond. Basicity equals the number of P-OH bonds!"),
            ("h2", "1. Comprehensive Oxoacids Table"),
            ("table", ["Oxoacid", "Formula", "State", "Basicity", "No. of P-H", "Reducing Character"], [
                ["Hypophosphorous acid", "H3PO2", "+1", "**1 (Monobasic)**", "**2 P-H bonds**", "Very Strong (reduces AgNO3 → Ag↓)"],
                ["Orthophosphorous acid", "H3PO3", "+3", "**2 (Dibasic)**", "**1 P-H bond**", "Strong (reduces CuSO4 → Cu↓)"],
                ["Orthophosphoric acid", "H3PO4", "+5", "**3 (Tribasic)**", "**0 P-H bonds**", "Non-reducing"],
                ["Pyrophosphoric acid", "H4P2O7", "+5", "**4 (Tetrabasic)**", "0 P-H bonds", "Non-reducing (P-O-P bridge)"],
                ["Hypophosphoric acid", "H4P2O6", "+4", "**4 (Tetrabasic)**", "0 P-H bonds", "Non-reducing (**P-P direct bond!**)"],
                ["Cyclotrimetaphosphoric", "(HPO3)3", "+5", "**3 (Tribasic)**", "0 P-H bonds", "Non-reducing (3 P-O-P bridges)"],
            ], [20, 12, 10, 16, 16, 26], "Table 15.10 — Structural formulas and properties of Phosphorus oxoacids."),
            ("key", "Basicity vs Reducing Rule:\n"
                    '• **Basicity = Number of P-OH bonds** (only H attached to oxygen is ionisable as H^+^).\n'
                    "• **Reducing Power = Number of P-H bonds** (hydrogenic H attached directly to P is reducing!)."),
            ("h2", "2. Diagnostic Disproportionation of Intermediate Acids"),
            ("p", "Acids containing phosphorus in intermediate oxidation states (+1 to +4) **disproportionate** on heating:\n"
                  '• 4 H3PO3 (+3) —(Δ, 200°C)→ **3 H3PO4 (+5) + PH3 (-3)**\n'
                  '• 2 H3PO2 (+1) —(Δ, 160°C)→ **H3PO4 (+5) + PH3 (-3)**'),
            ("h2", "3. Quantitative Reaction with Silver Nitrate"),
            ("p", "Hypophosphorous acid H3PO2 has two P-H bonds and acts as a powerful analytical reducing agent:\n"
                  "4 AgNO3 + 2 H2O + H3PO2 → **4 Ag↓ (black metallic mirror) + H3PO4 + 4 HNO3**."),
        ],
    },
]
