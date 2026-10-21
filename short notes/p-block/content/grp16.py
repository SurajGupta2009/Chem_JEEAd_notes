# -*- coding: utf-8 -*-
"""Group 16: Chalcogens (8 sheets / pages G16-01 to G16-08)."""

SHEETS = [
    # ------------------------------------------------------------------ G16-01
    {
        "id": "G16-01",
        "title": "Group 16 Trends, Allotropy & pπ-dπ Bonding",
        "blocks": [
            ("lead", "**Group 16: Chalcogens (ns^2 np^4)** — Ore Formers & Periodic Trends"),
            ("p", "Contains O, S (non-metals), Se, Te (metalloids), Po (radioactive α-emitter metal). "
                  "The electronic configuration has two unpaired p-electrons. Key themes: anomalous oxygen properties, "
                  "catenation in sulphur, and pπ-dπ vs pπ-pπ multiple bonding."),
            ("h2", "1. Periodic Trends of Group 16"),
            ("table", ["Element", "Config.", "Covalent Radius (pm)", "IE-1 (kJ/mol)", "ΔH_eg (kJ/mol)", "Electronegativity"], [
                ["O", "[He] 2s^2 2p^4", "66", "1314", "-141", "3.5 (2nd highest after F)"],
                ["S", "[Ne] 3s^2 3p^4", "104", "1000", "**-200 (Most negative!)**", "2.5"],
                ["Se", "[Ar] 3d^10 4s^2 4p^4", "117", "941", "-195", "2.4"],
                ["Te", "[Kr] 4d^10 5s^2 5p^4", "137", "869", "-190", "2.1"],
                ["Po", "[Xe] 4f^14 5d^10 6s^2 6p^4", "146", "813", "-174", "2.0"],
            ], [10, 24, 20, 16, 18, 12], "Table 16.1 — Physical and atomic parameters of Group 16 elements."),
            ("key", "Electron Gain Enthalpy Anomaly:\n"
                    "**S (-200) > Se (-195) > Te (-190) > Po (-174) > O (-141 kJ/mol)**.\n"
                    "Oxygen has the LEAST negative electron gain enthalpy in the entire group because of its very compact 2p subshell, causing severe inter-electronic repulsions for incoming electrons!"),
            ("h2", "2. Catenation & Allotropy"),
            ("p", "Sulphur shows maximum catenation in Group 16 because the S-S single bond (213 kJ/mol) is far stronger "
                  "than the O-O single bond (142 kJ/mol). Polysulphide ions like S_n^2- (e.g. S2^2-, S5^2-) and polythionates "
                  "exist stably in aqueous solution."),
            ("h2", "3. Multiple Bonding: pπ-pπ vs pπ-dπ"),
            ("bul", [
                "**Oxygen:** Forms strong **pπ-pπ double bonds** (O=O, C=O, N=O) due to compact 2p orbitals. Hence, oxygen exists as a diatomic gas O2 with weak van der Waals forces.",
                "**Sulphur & Heavier Chalcogens:** Cannot form stable pπ-pπ bonds; instead, they form single bonds with extensive catenation, leading to polyatomic crown molecules like **S8** (solid at RTP).",
                "**d-Orbital Participation:** Sulphur expands its octet using vacant 3d orbitals, forming hexa-coordinate molecules like **SF6** and utilizing **pπ-dπ back-bonding** in SO2 and SO3.",
            ]),
        ],
    },
    # ------------------------------------------------------------------ G16-02
    {
        "id": "G16-02",
        "title": "Dioxygen O2 & Ozone O3: Structure, Resonance & Oxidation",
        "blocks": [
            ("lead", "**Dioxygen & Ozone** — Paramagnetism of O2 & Strong Oxidising Action of O3"),
            ("p", "Oxygen exists as triplet ground-state O2 (paramagnetic) and triatomic allotrope Ozone O3 (diamagnetic)."),
            ("h2", "1. Dioxygen (O2) — Molecular Orbital Configuration"),
            ("p", "Valence electron count = 12 electrons. MO configuration:\n"
                  "σ(2s)^2 σ*(2s)^2 σ(2p_z)^2 π(2p_x)^2 π(2p_y)^2 **π*(2p_x)^1 π*(2p_y)^1**.\n"
                  "Bond order = (8 - 4)/2 = **2**. It possesses **two unpaired electrons** in degenerate π* antibonding orbitals, explaining its experimental **paramagnetism**."),
            ("h2", "2. Ozone (O3) — Synthesis & Angular Resonance Structure"),
            ("bul", [
                "**Synthesis (Silent Electric Discharge):** 3 O2 <===> 2 O3 (ΔH° = +142 kJ/mol, endothermic). A silent electric discharge is used to prevent local heating which would decompose O3 back to O2.",
                "**Structure:** V-shaped angular geometry (C_2v symmetry), sp^2 hybridized central O atom, bond angle **117°**, O-O bond length **128 pm** (intermediate between single bond 148 pm and double bond 121 pm due to resonance).",
                "**Thermodynamics of Ozone:** Thermodynamically unstable: 2 O3 -> 3 O2 (ΔH < 0 and ΔS > 0, so **ΔG is immensely negative**). High concentrations can decompose explosively!",
            ]),
            ("h2", "3. Powerful Oxidising Action & Qualitative Tests for Ozone"),
            ("table", ["Substance Oxidised", "Reaction Equation", "Observation / Diagnostic Test"], [
                ["Lead Sulphide (black)", "PbS (black) + 4 O3 -> **PbSO4 (white)** + 4 O2", "Decolourisation of black lead sulphide paper"],
                ["Potassium Iodide (KI)", "2 KI + H2O + O3 -> **2 KOH + I2 + O2**", "Turns starch paper blue (Quantitative iodometric estimation: titrate I2 with Na2S2O3)"],
                ["Mercury Metal (Hg)", "**2 Hg + O3 -> Hg2O + O2**", "**Tailing of Mercury:** Hg loses its meniscus and sticks to glass surface due to Hg2O formation. Restored by shaking with water!"],
                ["Potassium Manganate", "2 K2MnO4 (green) + H2O + O3 -> **2 KMnO4 (purple)** + 2 KOH + O2", "Oxidation of green manganate to purple permanganate"],
            ], [20, 42, 38], "Table 16.2 — Diagnostic oxidising reactions of Ozone."),
            ("key", "Tailing of Mercury Test: 2 Hg + O3 -> Hg2O + O2. The loss of meniscus is a unique and specific test for Ozone in JEE."),
        ],
    },
    # ------------------------------------------------------------------ G16-03
    {
        "id": "G16-03",
        "title": "Allotropes of Sulphur: Rhombic (α), Monoclinic (β), Plastic, S6/S8/S2",
        "blocks": [
            ("lead", "**Allotropes of Sulphur** — Rhombic (α), Monoclinic (β), Chair S6 & Paramagnetic S2"),
            ("p", "Sulphur exhibits more allotropes than almost any other element. The most important crystalline forms are Rhombic (α) and Monoclinic (β)."),
            ("h2", "1. Rhombic (α-Sulphur) vs Monoclinic (β-Sulphur)"),
            ("table", ["Property", "Rhombic Sulphur (α)", "Monoclinic Sulphur (β)"], [
                ["Crystal System", "Orthorhombic (octahedral crystals)", "Monoclinic (needle-shaped crystals)"],
                ["Colour & Density", "Bright yellow, density 2.06 g/cm^3", "Amber yellow, density 1.96 g/cm^3"],
                ["Melting Point", "385.8 K (112.8°C)", "393 K (119.2°C)"],
                ["Stability Range", "**Stable below 369 K (96°C)**", "**Stable above 369 K (96°C)**"],
                ["Solubility", "Insoluble in H2O, soluble in CS2 (~30 g/100g)", "Insoluble in H2O, soluble in CS2"],
            ], [18, 41, 41], "Table 16.3 — Comparison of Rhombic and Monoclinic Sulphur."),
            ("key", "**Transition Temperature (369 K / 95.6°C):** Below 369 K, α-sulphur is stable. Above 369 K, β-sulphur is stable. "
                    "At exactly 369 K, both allotropes coexist in dynamic equilibrium (Enantiotropic allotropy)."),
            ("h2", "2. Molecular Geometry: Crown S8 & Chair S6"),
            ("fig", "sulfur", "Fig. 16.1 — Puckered S8 crown ring (D4d) with bond parameters."),
            ("bul", [
                "**Puckered S8 Crown:** Both α and β sulphur consist of puckered S8 crown rings (D_4d symmetry). S-S bond distance = 204 pm, S-S-S angle = 107°.",
                "**Engels Sulphur (S6):** Prepared by reacting Na2S2O3 with conc. HCl. Contains a puckered **chair conformation** (like cyclohexane) with S-S-S angle = 102.2° and S-S distance = 205.7 pm.",
                "**High Temperature S2 Molecule (Paramagnetism):** At elevated temperatures (> 1000 K), sulphur vapor exists predominantly as diatomic **S2** molecules. Just like O2, S2 has **two unpaired electrons** in its π* antibonding molecular orbitals and is **paramagnetic**!",
            ]),
            ("h2", "3. Plastic (Amorphous) Sulphur"),
            ("p", "Formed by pouring boiling liquid sulphur (at ~440 K, dark brown viscous liquid with broken S8 chains) "
                  "in a thin stream into cold water. Yellow-brown rubbery elastic mass containing tangled helical polymer chains (S_μ). "
                  "It is insoluble in CS2; slowly reverts to rhombic α-sulphur on standing."),
        ],
    },
    # ------------------------------------------------------------------ G16-04
    {
        "id": "G16-04",
        "title": "Hydrides of G16: H2O, H2S, H2Se, H2Te & Anomalous H2O",
        "blocks": [
            ("lead", "**Group 16 Hydrides (H2E)** — Volatility, Acidity, Bond Angles & Drago's Rule"),
            ("p", "All chalcogens form volatile hydrides H2E (E = O, S, Se, Te, Po). Properties show sharp trends."),
            ("h2", "1. Periodic Trends in Hydrides"),
            ("table", ["Property", "H2O", "H2S", "H2Se", "H2Te", "Reason / Principle"], [
                ["Boiling Point (K)", "**373**", "213", "232", "269", "H2O is anomalously high due to extensive 3D intermolecular H-bonding; then increases with molar mass (dispersion forces): **H2S < H2Se < H2Te < H2O**"],
                ["Bond Angle (°)", "**104.5°**", "92.1°", "91.0°", "90.0°", "**Drago's Rule:** In H2S, H2Se, H2Te, no sp^3 hybridization occurs; bonds formed by almost pure p orbitals (approx 90°)!"],
                ["Thermal Stability", "**High**", "Moderate", "Low", "Very Poor", "E-H bond dissociation energy decreases down the group as orbital overlap becomes diffuse: **H2O > H2S > H2Se > H2Te**"],
                ["Reducing Character", "Nil", "Mild", "Strong", "**Strongest**", "Follows inverse of thermal stability: **H2O < H2S < H2Se < H2Te**"],
                ["Acidic Strength (K_a)", "10^-14", "10^-7", "10^-4", "**10^-3**", "E-H bond length increases and bond energy decreases: **H2O < H2S < H2Se < H2Te**"],
            ], [18, 10, 10, 10, 10, 42], "Table 16.4 — Systematic trends in Group 16 hydrides."),
            ("key", "Critical Order Sequences:\n"
                    "• **Boiling Point:** H2S < H2Se < H2Te < **H2O**\n"
                    "• **Acidic Strength:** H2O < H2S < H2Se < **H2Te**\n"
                    "• **Thermal Stability:** **H2O** > H2S > H2Se > H2Te\n"
                    "• **Reducing Power:** H2O < H2S < H2Se < **H2Te**"),
            ("h2", "2. Hydrogen Sulphide (H2S) in Qualitative Analysis"),
            ("p", "Rotten egg smell, poisonous gas. Precipitates metal cations as insoluble sulphides based on K_sp:\n"
                  "• **Group II Cations (Acidic medium, dil. HCl):** Low [S^2-] due to common ion effect of H^+; precipitates low K_sp sulphides (CuS, PbS, Bi2S3, CdS, HgS).\n"
                  "• **Group IV Cations (Basic medium, NH4OH + NH4Cl):** High [S^2-] due to removal of H^+ by OH^-; precipitates higher K_sp sulphides (ZnS, NiS, CoS, MnS)."),
        ],
    },
    # ------------------------------------------------------------------ G16-05
    {
        "id": "G16-05",
        "title": "Oxides of Sulphur: SO2, SO3 & Bleaching Action",
        "blocks": [
            ("lead", "**Oxides of Sulphur** — SO2, SO3 Polymerism & Temporary Bleaching Action"),
            ("p", "Sulphur forms two commercially crucial oxides: Sulphur dioxide SO2 and Sulphur trioxide SO3."),
            ("h2", "1. Sulphur Dioxide (SO2) — Structure & Bleaching"),
            ("bul", [
                "**Synthesis:** S + O2 -> SO2 (industrial)  or  Cu + 2 H2SO4 (conc.) --(Δ)--> CuSO4 + SO2↑ + 2 H2O (lab).",
                "**Structure:** V-shaped angular (sp^2 S, one lone pair, O-S-O angle 119.5°, bond length 143 pm equalized by resonance involving pπ-pπ and pπ-dπ bonding).",
                "**Bleaching Action (Temporary by Reduction):** In the presence of moisture, SO2 acts as a reducing bleaching agent:\n"
                "  SO2 + 2 H2O -> H2SO4 + **2 [H] (Nascent Hydrogen)**\n"
                "  Coloured organic matter + [H] -> **Colourless product**.\n"
                "  (On exposure to atmospheric oxygen, the bleached matter is re-oxidised back to coloured state. Contrast with Cl2 bleaching, which is permanent by oxidation!).",
            ]),
            ("table", ["Reagent", "Reaction with SO2", "Diagnostic Observation"], [
                ["Acidified K2Cr2O7 (orange)", "K2Cr2O7 + H2SO4 + 3 SO2 -> **Cr2(SO4)3 (green)** + K2SO4 + H2O", "Orange solution turns emerald green (Test for SO2!)"],
                ["Acidified KMnO4 (purple)", "2 KMnO4 + 2 H2O + 5 SO2 -> K2SO4 + **2 MnSO4 (colorless)** + 2 H2SO4", "Pink/purple permanganate decolourises completely"],
                ["Ferric Chloride (FeCl3)", "2 FeCl3 + SO2 + 2 H2O -> **2 FeCl2 (pale green)** + H2SO4 + 2 HCl", "Yellow ferric solution reduced to green ferrous"],
                ["Iodine solution (I2)", "I2 + SO2 + 2 H2O -> **2 HI (colorless)** + H2SO4", "Brown iodine solution decolourises"],
            ], [22, 43, 35], "Table 16.5 — Characteristic redox reactions of Sulphur Dioxide."),
            ("h2", "2. Sulphur Trioxide (SO3) & Solid Allotropes"),
            ("p", "In the gas phase, SO3 is planar trigonal (sp^2, D_3h symmetry, three equivalent S=O bonds). "
                  "In the solid state, it undergoes remarkable polymerisation:\n"
                  "• **γ-SO3 (Trimer):** Cyclic trimer **(SO3)3** or S3O9 with a puckered 6-membered ring of alternating S and O atoms.\n"
                  "• **β-SO3 & α-SO3 (Linear Polymers):** Infinite helical chains of tetrahedral SO4 units sharing corners, resembling asbestos fibers (mp 32°C and 62°C)."),
        ],
    },
    # ------------------------------------------------------------------ G16-06
    {
        "id": "G16-06",
        "title": "Oxoacids of Sulphur I: Sulphurous, Sulphuric & Contact Process",
        "blocks": [
            ("lead", "**Oxoacids of Sulphur (Part I)** — Contact Process & H2SO4 Dehydrating Action"),
            ("p", "Sulphuric acid H2SO4 ('King of Chemicals') is manufactured worldwide via the Contact Process."),
            ("h2", "1. Contact Process for H2SO4 Manufacture"),
            ("bul", [
                "**Step 1:** Burning sulphur or iron pyrites in air: S + O2 -> SO2  (or 4 FeS2 + 11 O2 -> 2 Fe2O3 + 8 SO2).",
                "**Step 2 (The Catalytic Key Step):** Catalytic oxidation of SO2 to SO3:\n"
                "  **2 SO2(g) + O2(g) <===(V2O5, 720 K, 2 bar)===> 2 SO3(g)**   ΔH° = -196.6 kJ/mol (Exothermic).\n"
                "  (Optimal conditions: excess O2, 2 bar pressure, 720 K with Vanadium pentoxide V2O5 catalyst).",
                "**Step 3:** Absorption of SO3 in 98% H2SO4 to form **Oleum (Pyrosulphuric acid H2S2O7)**:\n"
                "  SO3 + H2SO4 -> **H2S2O7**.\n"
                "  (Direct absorption in water is avoided because it forms a dense, unmanageable acid mist!).",
                "**Step 4:** Dilution of oleum with calculated quantity of water: H2S2O7 + H2O -> **2 H2SO4**.",
            ]),
            ("h2", "2. Chemical Properties & Dehydrating Action of H2SO4"),
            ("table", ["Reaction Category", "Substrate", "Reaction Equation & Observation"], [
                ["Dehydrating Action", "Cane Sugar (Sucrose C12H22O11)", "C12H22O11 --(conc. H2SO4)--> **12 C (black spongy char) + 11 H2O** (Charring of sugar)"],
                ["Dehydrating Action", "Ethanol (C2H5OH)", "C2H5OH --(conc. H2SO4, 443 K)--> **C2H4 (Ethene)** + H2O"],
                ["Dehydrating Action", "Formic Acid (HCOOH)", "HCOOH --(conc. H2SO4)--> **CO↑** + H2O"],
                ["Dehydrating Action", "Oxalic Acid ((COOH)2)", "(COOH)2 --(conc. H2SO4)--> **CO↑ + CO2↑** + H2O"],
                ["Oxidising Action", "Copper (Cu)", "Cu + 2 H2SO4 (conc.) --(Δ)--> CuSO4 + **SO2↑** + 2 H2O"],
                ["Oxidising Action", "Carbon (C) & Sulphur (S)", "C + 2 H2SO4 -> **CO2 + 2 SO2** + 2 H2O; S + 2 H2SO4 -> **3 SO2** + 2 H2O"],
            ], [20, 25, 55], "Table 16.6 — Diagnostic dehydrating and oxidising reactions of Sulphuric Acid."),
            ("key", "Dilution Rule: Always add **acid slowly to water with constant stirring**, NEVER water to concentrated acid (huge exothermic hydration causes dangerous boiling and acid splattering!)."),
        ],
    },
    # ------------------------------------------------------------------ G16-07
    {
        "id": "G16-07",
        "title": "Oxoacids of Sulphur II: Thionic & Peroxo Acids (Caro, Marshall)",
        "blocks": [
            ("lead", "**Oxoacids of Sulphur (Part II)** — Peroxoacids, Thionic Series & Thiosulphate"),
            ("p", "Peroxoacids contain the -O-O- peroxo linkage (formal oxidation state of peroxo oxygens = -1)."),
            ("h2", "1. Peroxomonosulphuric Acid (Caro's Acid, H2SO5)"),
            ("p", "Prepared by reacting chlorosulphonic acid with hydrogen peroxide: ClSO3H + H2O2 -> **H2SO5** + HCl.\n"
                  "Structural Formula: **HO-SO2-O-O-H**.\n"
                  "Formal Oxidation State Calculation: 2(+1) + S + 3(-2) + 2(-1) = 0  ===>  **S = +6** (NOT +8!).\n"
                  "Contains one peroxo (-O-O-) bond, two S=O bonds, and one normal S-OH bond."),
            ("h2", "2. Peroxodisulphuric Acid (Marshall's Acid, H2S2O8)"),
            ("p", "Prepared by anodic oxidation of cold 50% H2SO4 at high current density: 2 HSO4^- -> **H2S2O8** + 2e^-.\n"
                  "Structural Formula: **HO-SO2-O-O-SO2-OH**.\n"
                  "Oxidation State of both Sulphur atoms = **+6** (contains one bridging -O-O- peroxide bond).\n"
                  "Hydrolysis: H2S2O8 + H2O -> H2SO5 + H2SO4; H2SO5 + H2O -> H2SO4 + **H2O2** (industrial route to H2O2)."),
            ("table", ["Oxoacid", "Formula", "S Oxidation State", "Key Structural Linkage", "Basicity"], [
                ["Sulphurous acid", "H2SO3", "+4", "One lone pair on S, one S=O, two S-OH", "2 (Dibasic)"],
                ["Dithionous acid", "H2S2O4", "+3", "Direct **S-S bond**, two S=O, two S-OH", "2 (Dibasic)"],
                ["Dithionic acid", "H2S2O6", "+5", "Direct **S-S bond**, four S=O, two S-OH", "2 (Dibasic)"],
                ["Polythionic acid", "H2S_nO6", "Average", "Polysulphide chain **-S_(n-2)-** flanked by -SO3H", "2 (Dibasic)"],
                ["Pyrosulphuric (Oleum)", "H2S2O7", "+6", "**S-O-S bridge**, four S=O, two S-OH", "2 (Dibasic)"],
                ["Caro's acid", "H2SO5", "+6", "**One -O-O- bridge**, two S=O, one S-OH", "1 (Monobasic!)"],
                ["Marshall's acid", "H2S2O8", "+6", "**One -O-O- bridge**, four S=O, two S-OH", "2 (Dibasic)"],
            ], [18, 10, 14, 46, 12], "Table 16.7 — Master classification of Sulphur oxoacids."),
            ("h2", "3. Sodium Thiosulphate (Na2S2O3·5H2O, 'Hypo')"),
            ("bul", [
                "**Synthesis:** Na2SO3 + S --(boil with water)--> Na2S2O3.\n"
                "  Structure: Tetrahedral with one O replaced by S: central S is +5, terminal S is -1 (Average = +2).",
                "**Photography (Fixer):** AgBr + 2 Na2S2O3 -> **Na3[Ag(S2O3)2] (soluble complex)** + NaBr.",
                "**Iodometry:** 2 Na2S2O3 + I2 -> **Na2S4O6 (Sodium tetrathionate)** + 2 NaI.",
                "**With Strong Oxidant (Cl2):** Na2S2O3 + 4 Cl2 + 5 H2O -> **2 NaHSO4 + 8 HCl + H2SO4** (acts as 'Antichlor').",
            ]),
        ],
    },
    # ------------------------------------------------------------------ G16-08
    {
        "id": "G16-08",
        "title": "Halides & Oxohalides of Sulphur: SF4, SF6, SOCl2, SO2Cl2",
        "blocks": [
            ("lead", "**Sulphur Halides & Oxohalides** — SF4 (See-Saw), SF6 (Inert Octahedron) & Thionyl Chloride"),
            ("p", "Sulphur forms hexafluoride SF6, tetrahalides SF4, SCl4, and dihalides SCl2, S2Cl2."),
            ("h2", "1. Sulphur Hexafluoride (SF6) — Kinetic Inertness"),
            ("bul", [
                "**Structure:** Regular Octahedral (sp^3d^2, O_h symmetry, all S-F bonds = 156 pm).",
                "**Extraordinary Chemical Inertness:** SF6 is non-toxic, odorless, completely inert to water, boiling molten KOH, and acids. Does not hydrolyse even at 500°C!",
                "**Reason for Inertness:** S atom is coordinatively saturated and sterically shielded by six compact Fluorine atoms. Water molecules cannot approach the central Sulphur atom, and Sulphur cannot expand its coordination sphere further.",
                "**Applications:** High dielectric strength gas used as an electrical insulator in high-voltage circuit breakers and transformers.",
            ]),
            ("table", ["Compound", "Hybridization", "Geometry (VSEPR)", "Hydrolysis & Reactivity"], [
                ["SF4", "sp^3d (1 lone pair eq)", "**See-Saw (Distorted tetrahedron)**", "Hydrolyses violently: SF4 + 2 H2O -> **SO2 + 4 HF** (fluorinating agent)"],
                ["SF6", "sp^3d^2 (0 lone pair)", "**Regular Octahedral**", "Completely inert to water and hot caustic alkali"],
                ["SCl4", "sp^3d (1 lone pair)", "See-Saw", "Thermally unstable; decomposes above -30°C: SCl4 -> SCl2 + Cl2"],
                ["S2Cl2", "sp^3 (bent per S)", "Open-book / H2O2-like", "Yellow liquid; reacts with water: 2 S2Cl2 + 2 H2O -> SO2 + 3 S + 4 HCl"],
            ], [12, 22, 28, 38], "Table 16.8 — Comparative structures and reactions of Sulphur halides."),
            ("h2", "2. Thionyl Chloride (SOCl2) & Sulphuryl Chloride (SO2Cl2)"),
            ("bul", [
                "**Thionyl Chloride (SOCl2):** Pyramidal (sp^3, 1 lone pair, one S=O, two S-Cl).\n"
                "  Darzens reaction (organic synthesis of alkyl chlorides): R-OH + SOCl2 --(pyridine)--> **R-Cl + SO2↑ + HCl↑**.\n"
                "  (Both by-products SO2 and HCl are gases, escaping spontaneously to leave pure alkyl chloride!).",
                "**Sulphuryl Chloride (SO2Cl2):** Tetrahedral (sp^3, two S=O, two S-Cl).\n"
                "  Hydrolysis: SO2Cl2 + 2 H2O -> **H2SO4 + 2 HCl**.",
            ]),
        ],
    },
]
