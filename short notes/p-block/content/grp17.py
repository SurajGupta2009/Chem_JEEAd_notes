# -*- coding: utf-8 -*-
"""Group 17: Halogens (9 sheets / pages G17-01 to G17-09)."""

SHEETS = [
    # ------------------------------------------------------------------ G17-01
    {
        "id": "G17-01",
        "title": "Group 17 Trends, Anomalous F, Bond Dissociation Anomaly",
        "blocks": [
            ("lead", '**Group 17: Halogens (ns^2^ np^5^)** — Salt Formers & Periodic Anomalies'),
            ("p", "Contains F, Cl (gases), Br (volatile red liquid), I (lustrous solid), At, Ts (radioactive). "
                  "Highest effective nuclear charge in their respective periods, having the most negative electron gain enthalpies."),
            ("h2", "1. Periodic Trends of Halogens"),
            ("table", ["Element", "Config.", "Covalent Radius (pm)", "IE-1 (kJ/mol)", 'ΔH~eg~ (kJ/mol)', "Bond Enthalpy X2 (kJ/mol)"], [
                ["F", '[He] 2s^2^ 2p^5^', "64", "1680", "-328", "**158.8 (Low!)**"],
                ["Cl", '[Ne] 3s^2^ 3p^5^', "99", "1256", "**-349 (Most negative!)**", "**242.6 (Highest!)**"],
                ["Br", '[Ar] 3d^10^ 4s^2^ 4p^5^', "114", "1142", "-325", "192.8"],
                ["I", '[Kr] 4d^10^ 5s^2^ 5p^5^', "133", "1008", "-295", "151.1"],
            ], [8, 24, 20, 16, 18, 14], "Table 17.1 — Physical and atomic properties of Group 17 elements."),
            ("key", "Bond Dissociation Enthalpy Anomaly (Classic JEE Question):\n"
                    "**Cl2 (242.6) > Br2 (192.8) > F2 (158.8) > I2 (151.1 kJ/mol)**.\n"
                    "F2 has a lower bond energy than both Cl2 and Br2 because of severe inter-electronic repulsions between the non-bonding electron pairs in the extremely small F2 molecule (F-F distance = 143 pm)!"),
            ("h2", "2. Oxidising Power & Electrode Potentials"),
            ("p", "Standard reduction potential: F2 (+2.87 V) > Cl2 (+1.36 V) > Br2 (+1.09 V) > I2 (+0.54 V).\n"
                  "Fluorine is the most powerful oxidising agent in chemistry. Why F2 > Cl2 despite lower electron gain enthalpy?\n"
                  "Standard reduction potential depends on the Born-Haber cycle parameters:"),
            ("bul", [
                '1. **Low Bond Dissociation Enthalpy:** ΔH~diss~(F2) is very low (+158.8 kJ/mol) → easy atomisation.',
                '2. **Very High Hydration Enthalpy:** F^-^ is small with immense charge density, releasing huge hydration enthalpy: ΔH~hyd~(F^-^) = **-515 kJ/mol** (vs Cl^-^ = -381 kJ/mol).',
                "3. **Conclusion:** High hydration energy and low bond dissociation energy more than compensate for the slightly less negative electron gain enthalpy of F2!",
            ]),
            ("h2", "3. Anomalous Behaviour of Fluorine"),
            ("p", "Only oxidation state is **-1** (no d-orbitals, most electronegative element). Maximum covalency is strictly 1 (or 2 in rare bridging/coordination). "
                  "HF is a weak acid with high boiling point (293 K) due to zig-zag hydrogen-bonded chains (H-F...H-F...)."),
        ],
    },
    # ------------------------------------------------------------------ G17-02
    {
        "id": "G17-02",
        "title": "Preparation & Industrial Extraction of F2, Cl2, Br2, I2",
        "blocks": [
            ("lead", "**Extraction of Halogens** — Moissan Electrolysis, Deacon Process & Br2/I2 Mining"),
            ("p", 'Because F2 is the strongest oxidant, no chemical reagent can oxidise F^-^ to F2; it is produced exclusively by electrolysis.'),
            ("h2", "1. Extraction of Fluorine (Dennis-Moissan Process)"),
            ("bul", [
                '**Electrolyte:** Anhydrous molten mixture of **KF + 2 HF (KF·2HF)** at ≈100°C in a Monel metal or steel vessel.',
                '**Why Anhydrous HF alone cannot be used:** Pure anhydrous liquid HF is a non-electrolyte (does not conduct electricity). Adding KF supplies K^+^ and [HF2]^-^ ions, making it conductive.',
                "**Electrodes:** Carbon (graphite) anode, steel vessel as cathode. A copper diaphragm separates anode and cathode to prevent explosive recombination of H2 and F2:\n"
                '  • At Cathode: 2 H^+^ + 2e^-^ → **H2↑**\n'
                '  • At Anode: 2 F^-^ → **F2↑** + 2e^-^',
            ]),
            ("h2", "2. Manufacture of Chlorine (Cl2)"),
            ("table", ["Process", "Reagents / Mechanism", "Key Reaction Equation"], [
                ["Deacon's Process", "Oxidation of HCl gas by atmospheric O2 with CuCl2 catalyst (723 K)", '4 HCl + O2 —(CuCl2, 723 K)→ **2 Cl2 + 2 H2O**'],
                ["Chlor-Alkali (Nelson / Castner-Kellner)", "Electrolysis of aqueous brine (NaCl)", '2 NaCl + 2 H2O —(electrolysis)→ **Cl2 (anode) + H2 (cathode) + 2 NaOH**'],
                ["Laboratory Prep", "Oxidation of conc. HCl with MnO2 or KMnO4", "MnO2 + 4 HCl → **MnCl2 + Cl2↑ + 2 H2O**\n2 KMnO4 + 16 HCl → **2 KCl + 2 MnCl2 + 5 Cl2↑ + 8 H2O**"],
            ], [22, 38, 40], "Table 17.2 — Synthetic and industrial processes for Chlorine."),
            ("h2", "3. Recovery of Bromine and Iodine"),
            ("bul", [
                '**Bromine from Sea Brine:** Sea water contains Br^-^ (≈65 ppm). Acidified with H2SO4, treated with Cl2 gas: **2 Br^-^ + Cl2 → 2 Cl^-^ + Br2↑**. Blown out with air, absorbed in Na2CO3 solution: 3 Na2CO3 + 3 Br2 → 5 NaBr + NaBrO3 + 3 CO2.',
                "**Iodine from Caliche (Chile Saltpetre):** Contains sodium iodate NaIO3. Reduced with sodium bisulphite: **2 NaIO3 + 5 NaHSO3 → 2 Na2SO4 + 3 NaHSO4 + I2↓ + H2O**.",
                "**Iodine from Seaweeds (Laminaria):** Ash (Kelp) contains iodides; boiled with conc. H2SO4 and MnO2: 2 NaI + MnO2 + 3 H2SO4 → 2 NaHSO4 + MnSO4 + **I2↑** + 2 H2O.",
            ]),
        ],
    },
    # ------------------------------------------------------------------ G17-03
    {
        "id": "G17-03",
        "title": "Hydrogen Halides HX: Thermal Stability, Acidity & Reducing Power",
        "blocks": [
            ("lead", "**Hydrogen Halides (HX)** — Boiling Points, Bond Energies, Acidity & Reducing Trends"),
            ("p", "Prepared by direct combination or by salt + acid reactions: NaX + H2SO4 → NaHSO4 + HX."),
            ("h2", "1. Periodic Trends in Hydrogen Halides"),
            ("table", ["Property", "HF", "HCl", "HBr", "HI", "Trend / Underlying Reason"], [
                ["Boiling Point (K)", "**293 (Highest!)**", "189", "206", "238", "HF is anomalously high due to strong intermolecular H-bonding; then increases with van der Waals dispersion forces: **HCl < HBr < HI < HF**"],
                ["Bond Length (pm)", "91.7", "127.4", "141.4", "**160.9**", "Increases down group with increasing halogen size"],
                ["Bond Enthalpy (kJ/mol)", "**574**", "432", "363", "295", "Decreases sharply as overlap efficiency declines"],
                ["Thermal Stability", "**Most Stable**", "Stable", "Decomposes >800 K", "**Decomposes readily**", "Parallels bond dissociation energy: **HF > HCl > HBr > HI**"],
                ['Acidic Strength (K~a~)', 'Weak (3.5×10^-4^)', 'Strong (≈10^7^)', 'Very Strong (≈10^9^)', '**Strongest (≈10^10^)**', "Follows inverse of H-X bond strength: **HF < HCl < HBr < HI**"],
                ["Reducing Character", "Nil", "Very Weak", "Strong", "**Strongest**", "HI easily oxidises to I2: **HF < HCl < HBr < HI**"],
            ], [18, 10, 10, 10, 10, 42], "Table 17.3 — Master summary of Hydrogen Halide properties."),
            ("key", "Critical Sequences for JEE:\n"
                    "• **Boiling Point:** HCl < HBr < HI < **HF**\n"
                    "• **Acidic Strength:** HF < HCl < HBr < **HI**\n"
                    "• **Reducing Power:** HF < HCl < HBr < **HI**\n"
                    "• **Thermal Stability:** **HF** > HCl > HBr > HI"),
            ("h2", "2. Preparation Traps with H2SO4"),
            ("trap", "TRAP: HBr and HI CANNOT be prepared by heating NaBr/NaI with conc. H2SO4!\n"
                    "Conc. H2SO4 is a strong oxidising agent that oxidises HBr to Br2 and HI to I2:\n"
                    "2 NaBr + 2 H2SO4 → Na2SO4 + **Br2 (red vapor)** + SO2 + 2 H2O\n"
                    "2 NaI + 2 H2SO4 → Na2SO4 + **I2 (violet vapor)** + SO2 + 2 H2O.\n"
                    '**Correct Method:** Use non-oxidising **conc. H3PO4**: 3 NaBr + H3PO4 —(Δ)→ Na3PO4 + 3 HBr↑.'),
        ],
    },
    # ------------------------------------------------------------------ G17-04
    {
        "id": "G17-04",
        "title": "Halogen Oxides: OF2, O2F2, Cl2O, ClO2, Cl2O6, Cl2O7, I2O5",
        "blocks": [
            ("lead", "**Halogen Oxides** — OF2, Paramagnetic ClO2, Dimeric Cl2O6 & I2O5 in CO Estimation"),
            ("p", "Fluorine forms oxygen fluorides (F is more electronegative than O). Other halogens form oxides."),
            ("h2", "1. Oxygen Fluorides (OF2 and O2F2)"),
            ("bul", [
                "**OF2 (Oxygen Difluoride):** Prepared: 2 NaOH (cold, 2% dil.) + 2 F2 → **OF2↑** + 2 NaF + H2O. V-shaped (angle 103°, F-O-F repulsions compress angle below water's 104.5°). Oxidation state of O is **+2**.",
                "**O2F2 (Dioxygen Difluoride):** Prepared: F2 + O2 in electric discharge at 90 K. Open-book structure like H2O2. Oxidation state of O is **+1**. Extremely powerful fluorinating agent; reacts with plutonium: **Pu + 3 O2F2 → PuF6 + 3 O2** (used to recover Pu from spent nuclear fuel!).",
            ]),
            ("h2", "2. Oxides of Chlorine"),
            ("table", ["Oxide", "Oxid. State", "Structure & Geometry", "Key Reaction / Diagnostic Behavior"], [
                ["Cl2O", "+1", "Bent V-shaped (angle 111°)", "2 HgO + 2 Cl2 → HgO·HgCl2 + **Cl2O**; Anhydride of HOCl"],
                ["ClO2", "+4", 'Bent (odd-electron, 19 e^-^)', "**Paramagnetic gas**; does not dimerise readily; bleaching agent for wood pulp; 2 ClO2 + 2 NaOH → **NaClO2 + NaClO3** + H2O (mixed anhydride!)"],
                ["Cl2O6", "+6", '**Liquid / Solid: [ClO2]^+^ [ClO4]^-^**', "Mixed anhydride of HClO3 and HClO4: Cl2O6 + H2O → **HClO3 + HClO4**"],
                ["Cl2O7", "+7", "Two ClO3 tetrahedra sharing O bridge", "Anhydride of perchloric acid: 2 HClO4 + P4O10 → **Cl2O7** + 4 HPO3. Colorless oily liquid, explodes violently on percussion!"],
            ], [12, 10, 32, 46], "Table 17.4 — Comprehensive spectrum of Chlorine Oxides."),
            ("h2", "3. Iodine Pentoxide (I2O5) & Quantitative Estimation of CO"),
            ("key", 'Prepared by dehydrating iodic acid: 2 HIO3 —(440 K)→ **I2O5** + H2O.\n'
                    "White crystalline solid, highly stable. Reacts quantitatively with Carbon Monoxide at 170°C:\n"
                    "**I2O5 + 5 CO → I2 + 5 CO2**.\n"
                    "The liberated I2 is titrated against standard sodium thiosulphate (Na2S2O3) with starch indicator. "
                    "This is the standard analytical method for estimating toxic CO in air and flue gases!"),
        ],
    },
    # ------------------------------------------------------------------ G17-05
    {
        "id": "G17-05",
        "title": "Oxoacids of Halogens: Acid Strength, Redox & Anion Stability",
        "blocks": [
            ("lead", "**Oxoacids of Halogens** — Acid Strengths, Anion Resonance & Thermal Stability"),
            ("p", "Halogens form four series of oxoacids: Hypohalous (HOX, +1), Halous (HXO2, +3), Halic (HXO3, +5), Perhalic (HXO4, +7)."),
            ("h2", "1. Complete Classification of Halogen Oxoacids"),
            ("table", ["Oxidation State", "Acid Family", "Fluorine", "Chlorine", "Bromine", "Iodine"], [
                ["+1", "Hypohalous (HOX)", "HOF (only one!)", "HOCl", "HOBr", "HOI"],
                ["+3", "Halous (HXO2)", "—", "HClO2", "—", "—"],
                ["+5", "Halic (HXO3)", "—", "HClO3", "HBrO3", "HIO3"],
                ["+7", "Perhalic (HXO4)", "—", "HClO4", "HBrO4", "HIO4 / H5IO6 (Periodic)"],
            ], [15, 25, 15, 15, 15, 15], "Table 17.5 — Systematic matrix of halogen oxoacids."),
            ("h2", "2. Acid Strength Trends"),
            ("bul", [
                "**Trend 1 (Same Halogen, Increasing Oxidation State):**\n"
                "  **HOCl (+1) < HClO2 (+3) < HClO3 (+5) < HClO4 (+7)**.\n"
                '  Reason: Conjugate base stability increases as the negative charge is delocalised over more electronegative oxygen atoms via resonance: ClO^-^ (1 O) < ClO2^-^ (2 O) < ClO3^-^ (3 O) < **ClO4^-^ (4 O, charge density -0.25/O)**. HClO4 is one of the strongest known Bronsted acids!',
                "**Trend 2 (Different Halogens, Same Oxidation State):**\n"
                "  **HOCl > HOBr > HOI**.\n"
                '  Reason: As electronegativity of halogen decreases (Cl > Br > I), polarity of the O-H bond decreases, making release of H^+^ less favorable.',
            ]),
            ("h2", "3. Oxidising Power vs Thermal Stability"),
            ("table", ["Family Sequence", "Acid Strength Order", "Thermal Stability Order", "Oxidising Power Order"], [
                ["Chlorine Series", "HOCl < HClO2 < HClO3 < **HClO4**", "HOCl < HClO2 < HClO3 < **HClO4**", "**HOCl** > HClO2 > HClO3 > HClO4"],
            ], [20, 25, 25, 30], "Table 17.6 — Inverse relationship between stability and oxidising power."),
            ("key", "**Oxidising Power is INVERSE to acid stability:** Hypochlorous acid **HOCl is the STRONGEST oxidant**, "
                    "whereas perchloric acid **HClO4 is the weakest oxidant** in dilute aqueous solution!"),
        ],
    },
    # ------------------------------------------------------------------ G17-06
    {
        "id": "G17-06",
        "title": "Interhalogen Compounds: AX, AX3, AX5, AX7 (Structures & VSEPR)",
        "blocks": [
            ("lead", "**Interhalogen Compounds (XX'~n~)** — Synthesis, VSEPR Geometries & Reactivity"),
            ("p", "Formed when two different halogens react. General formula XX'~n~ where X is the larger halogen and "
                  "X' is the smaller, more electronegative halogen; n = 1, 3, 5, 7."),
            ("h2", "1. Comprehensive VSEPR Geometries of Interhalogens"),
            ("fig", "interhalogens", "Fig. 17.1 — Interhalogen geometries: ClF3 (T-Shaped), BrF5 (Square Pyramidal), and IF7 (Pentagonal Bipyramidal)."),
            ("table", ["Type", "Example", "Hybridization", "Lone Pairs on X", "VSEPR Geometry", "Physical State"], [
                ["XX'", "ClF, BrF, ICl", 'sp^3^', "3 lone pairs", "**Linear**", "ClF (gas), ICl (ruby red solid)"],
                ["XX'~3~", "ClF3, BrF3, ICl3", 'sp^3^d', "2 equatorial lp", "**T-Shaped** (bent T)", "ClF3 (gas), BrF3 (liquid), ICl3 (dimer solid)"],
                ["XX'~5~", "ClF5, BrF5, IF5", "sp^3d^2", "1 axial lp", "**Square Pyramidal**", "All colorless liquids/gases"],
                ["XX'~7~", "**IF7** (only one!)", "sp^3d^3", "0 lone pairs", "**Pentagonal Bipyramidal**", "Colorless gas (D~5h~ symmetry)"],
            ], [10, 16, 18, 16, 20, 20], "Table 17.7 — Complete structural geometries of interhalogens."),
            ("key", "Why is IF7 the ONLY XX'~7~ compound formed?\n"
                    "Because Iodine has the largest atomic radius in Group 17, and Fluorine has the smallest atomic radius. "
                    "The radius ratio r(I)/r(F) is maximum, allowing sterically uncrowded coordination of seven F atoms!"),
            ("h2", "2. Chemical Reactivity: Interhalogens vs Halogens"),
            ("p", "In general, **interhalogen compounds are MORE reactive than pure halogens (except F2)**.\n"
                  "Reason: The X-X' bond in an interhalogen is polar and weaker than the non-polar X-X bond in a pure halogen (except F-F where lone pair repulsions weaken the bond)."),
            ("h2", "3. Hydrolysis of Interhalogens"),
            ("p", "Hydrolysis always yields a **halide ion from the smaller halogen X'** and an **oxohalate ion from the larger central halogen X**:\n"
                  "• **XX' + H2O → HX' + HOX**  (e.g., ICl + H2O → HCl + HOI)\n"
                  "• **XX'~3~ + 2 H2O → 3 HX' + HXO2** (e.g., BrF3 + 2 H2O → 3 HF + HBrO2)\n"
                  "• **XX'~5~ + 3 H2O → 5 HX' + HXO3** (e.g., IF5 + 3 H2O → 5 HF + HIO3)\n"
                  "• **XX'~7~ + 4 H2O → 7 HX' + HXO4** (e.g., IF7 + 4 H2O → 7 HF + H5IO6)"),
            ("trap", "TRAP: ICl3 in the solid state exists as a planar bridged dimer **I2Cl6** with two bridging chlorine atoms (chlorine-bridged like Al2Cl6)!"),
        ],
    },
    # ------------------------------------------------------------------ G17-07
    {
        "id": "G17-07",
        "title": "Polyhalide Ions: I3-, I5-, ICl2-, ICl4- & Bonding",
        "blocks": [
            ("lead", '**Polyhalide Ions** — Triiodide I3^-^, ICl2^-^, ICl4^-^ & 3c-4e Hypervalent Bonding'),
            ("p", 'Halogens and interhalogens coordinate with halide ions to form polyhalide anions: X^-^ + n X2 → X~2n+1~^-^.'),
            ("h2", '1. Triiodide Ion (I3^-^) — Structure & Bonding'),
            ("bul", [
                "**Solubility of I2 in KI:** Pure iodine is virtually insoluble in pure water (non-polar). It dissolves readily in aqueous KI due to formation of the soluble **triiodide complex anion**:\n"
                '  **KI + I2 ⇌ K^+^ [I3]^-^**.',
                '**VSEPR Geometry:** Central I atom has 7 valence e^-^ + 1 from charge + 2 from bond pairs = 10 electrons = 5 pairs (sp^3^d hybridization).',
                "**Three Equatorial Lone Pairs:** The three lone pairs occupy equatorial positions at 120° to minimise repulsions. The two I-I bonds are axial (180°).\n"
                "  Geometry is **perfectly LINEAR (D~∞h~ symmetry)** with I-I bond length 292 pm.",
            ]),
            ("table", ["Polyhalide Ion", "Central Atom", "Hybridization", "Lone Pairs", "Geometry (VSEPR)", "Bond Angle"], [
                ['I3^-^', "I", 'sp^3^d', "3 equatorial", "**Linear**", "180°"],
                ['ICl2^-^', "I", 'sp^3^d', "3 equatorial", "**Linear**", "180°"],
                ['ICl4^-^', "I", "sp^3d^2", "2 axial", "**Square Planar**", "90°"],
                ['I3^+^ (Cation)', "I", 'sp^3^', "2 lone pairs", "**Bent / V-shaped**", "104°"],
                ['I5^-^', "I", "—", "—", '**V-shaped dimer** (I3^-^ coordinated to I2)', '≈95°'],
            ], [15, 12, 18, 16, 24, 15], "Table 17.8 — Geometries and electron pairs of Polyhalide species."),
            ("key", 'Why does Fluorine NOT form polyhalide anions (F3^-^ does not exist)?\n'
                    'Because Fluorine has no vacant d orbitals to expand its octet to accommodate 10 valence electrons (sp^3^d)!'),
            ("h2", "2. Polyhalide Cations"),
            ("p", 'Strong oxidising Lewis acids like AsF5 or SbF5 can pull F^-^ from interhalogens to generate polyhalide cations:\n'
                  '• ClF3 + SbF5 → **[ClF2]^+^ [SbF6]^-^** (bent [ClF2]^+^, sp^3^, 2 lone pairs)\n'
                  '• BrF5 + SbF5 → **[BrF4]^+^ [SbF6]^-^** (see-saw [BrF4]^+^, sp^3^d, 1 lone pair)'),
        ],
    },
    # ------------------------------------------------------------------ G17-08
    {
        "id": "G17-08",
        "title": "Pseudohalogens & Pseudohalides (CN-, SCN-, N3-)",
        "blocks": [
            ("lead", "**Pseudohalogens & Pseudohalides** — Cyanogen (CN)2, Thiocyanogen (SCN)2 & Chemistry"),
            ("p", "Pseudohalogens are univalent polyatomic groupings that resemble true halogens (X2) in their free state, "
                  'forming univalent anions (pseudohalides X^-^) and volatile hydrogen acids (HX).'),
            ("h2", "1. Defining Criteria for Pseudohalogens"),
            ("bul", [
                "1. They consist of two or more electronegative atoms, at least one of which is Nitrogen.",
                "2. They dimerise in the free state to neutral symmetric volatile dimers: **(CN)2 (Cyanogen)**, **(SCN)2 (Thiocyanogen)**, **(SeCN)2**, **(OCN)2**.",
                '3. They react with alkalis to disproportionate into pseudohalide and pseudohalite (like Cl2 + 2 OH^-^ → Cl^-^ + ClO^-^ + H2O):\n'
                '   **(CN)2 + 2 OH^-^ → CN^-^ (Cyanide) + OCN^-^ (Cyanate) + H2O**.',
                "4. They form insoluble silver, lead, and mercury(I) salts: AgCN (white↓), AgSCN (white↓), resembling AgCl↓.",
            ]),
            ("table", ["Pseudohalide Ion", "Formula", "Dimeric Pseudohalogen", 'Insoluble Ag^+^ Salt & Behaviour in NH3'], [
                ["Cyanide", 'CN^-^', "(CN)2 (Cyanogen, gas)", 'AgCN↓ (white, dissolves in excess NH3 and in excess CN^-^)'],
                ["Thiocyanate", 'SCN^-^', "(SCN)2 (Thiocyanogen, yellow oil)", 'AgSCN↓ (white, insoluble in dil. HNO3; reacts with Fe^3+^ → blood-red [Fe(SCN)]^2+^)'],
                ["Cyanate", 'OCN^-^', "(OCN)2", "AgOCN↓ (white)"],
                ["Azide", 'N3^-^', "(N3)2 (Does NOT exist!)", "AgN3↓ (white, shock-sensitive explosive detonator)"],
            ], [18, 12, 28, 42], "Table 17.9 — Classification of Pseudohalogens and Pseudohalides."),
            ("key", 'TRAP Question: Is Azide (N3^-^) a true pseudohalide?\n'
                    "N3^-^ is an **incomplete pseudohalide** because the free neutral dimer '(N3)2' (hexanitrogen N6) does NOT exist as a stable isolable molecule!"),
        ],
    },
    # ------------------------------------------------------------------ G17-09
    {
        "id": "G17-09",
        "title": "Bleaching Powder, Hypochlorites & Disproportionation Reactions",
        "blocks": [
            ("lead", "**Bleaching Powder & Disproportionation** — CaOCl2, Available Chlorine & Alkali Reactions"),
            ("p", "Bleaching powder is manufactured by action of chlorine on dry slaked lime: Ca(OH)2 + Cl2 → CaOCl2·H2O."),
            ("h2", "1. Composition & Chemical Nature of Bleaching Powder"),
            ("bul", [
                "**True Composition:** Bleaching powder is NOT a simple single compound CaOCl2. Its actual structural formula is a mixed double salt: **Ca(OCl)2·CaCl2·Ca(OH)2·2H2O**.",
                "**Oxidation State of Chlorine in CaOCl2:**\n"
                '  CaOCl2 dissociates into Ca^2+^, Cl^-^, and OCl^-^ ions.\n'
                '  • Direct Chloride ion (Cl^-^): **Oxidation state = -1**\n'
                '  • Hypochlorite ion (OCl^-^): **Oxidation state = +1**\n'
                "  • Average oxidation state = **0**! (Classic JEE question).",
                '**Auto-Decomposition on Long Standing:** 6 CaOCl2 —(standing in air)→ **Ca(ClO3)2 + 5 CaCl2** (loss of bleaching power).',
            ]),
            ("h2", "2. Available Chlorine & Iodometric Titration"),
            ("p", "The percentage of active chlorine liberated by treatment with excess dilute acid is called **Available Chlorine**:\n"
                  "CaOCl2 + 2 CH3COOH (or dil. H2SO4) → Ca(CH3COO)2 + H2O + **Cl2↑**.\n"
                  "The liberated Cl2 is reacted with excess KI: Cl2 + 2 KI → 2 KCl + **I2**. "
                  "The liberated I2 is titrated against standard 0.1 N Na2S2O3 with starch indicator: **I2 + 2 Na2S2O3 → 2 NaI + Na2S4O6**."),
            ("h2", "3. Master Summary of Halogen Disproportionation with Alkali"),
            ("table", ["Halogen", "With Cold, Dilute NaOH (15°C)", "With Hot, Concentrated NaOH (70°C)"], [
                ["Cl2", "Cl2 + 2 NaOH → **NaCl (-1) + NaOCl (+1)** + H2O", "3 Cl2 + 6 NaOH → **5 NaCl (-1) + NaClO3 (+5)** + 3 H2O"],
                ["Br2", "Br2 + 2 NaOH → **NaBr + NaOBr** + H2O (unstable)", "3 Br2 + 6 NaOH → **5 NaBr (-1) + NaBrO3 (+5)** + 3 H2O"],
                ["I2", "Disproportionates instantly to iodate even in cold!", "3 I2 + 6 NaOH → **5 NaI (-1) + NaIO3 (+5)** + 3 H2O"],
                ["F2 (Redox!)", "**2 F2 + 2 NaOH (dil) → 2 NaF + OF2↑ + H2O**", "**2 F2 + 4 NaOH (conc) → 4 NaF + O2↑ + 2 H2O**"],
            ], [15, 42, 43], "Table 17.10 — Reaction of Halogens with Cold/Dilute vs Hot/Concentrated Alkali."),
            ("key", "Fluorine does NOT disproportionate with alkali! Because F cannot have positive oxidation states, it oxidises hydroxide oxygen: **cold dil. NaOH gives OF2**, and **hot conc. NaOH gives O2**!"),
        ],
    },
]
