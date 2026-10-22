# -*- coding: utf-8 -*-\n"""Chemical Bonding Part 3: Secondary Interactions, H-Bonding & Crystal Structures (CB-17 to CB-24)."""

SHEETS = [
    # ------------------------------------------------------------------ CB-17
    {
        "id": "CB-17",
        "title": "Hydrogen Bonding: Intermolecular vs Intramolecular Chelation",
        "blocks": [
            ("lead", "**Hydrogen Bonding** — Dipole-Dipole Attraction, Conditions & Energetics"),
            ("p", "A special electrostatic attraction between a hydrogen atom covalently bonded to a strongly "
                  'electronegative small atom (F, O, N) and a lone pair on another electronegative atom: X-H^delta+^ ··· :Y^delta−^. '
                  'Bond strength ranges from 8 to 42 kJ/mol (much weaker than covalent ≈400 kJ, but stronger than van der Waals ≈2-4 kJ).'),
            ("fig", "hbonding", "Fig. 3.1 — Intermolecular H-bonding in ice cage vs Intramolecular chelation in o-nitrophenol."),
            ("h2", "1. Intermolecular vs Intramolecular Hydrogen Bonding"),
            ("table", ["Feature", "Intermolecular H-Bonding", "Intramolecular H-Bonding (Chelation)"], [
                ["Definition", "Occurs between **different molecules** of same or different substances", "Occurs **within the same molecule** between two functional groups"],
                ["Ring Formation", "Forms open chains or 3D polymeric networks", "Forms a stable **5- or 6-membered chelate ring**"],
                ["Boiling / Melting Point", "**Significantly ELEVATES** M.P. and B.P. (requires energy to break intermolecular network)", "**LOWERS** B.P. and M.P. (molecule curls internally, preventing intermolecular association)"],
                ["Viscosity & Surface Tension", "**High viscosity** (e.g. glycerol, H2SO4, water)", "**Low viscosity**, high volatility (steam volatile)"],
                ["Classic Organic Example", "**p-Nitrophenol** (high BP, soluble in water, non-volatile)", "**o-Nitrophenol** (steam volatile, lower BP, less soluble in water)"],
            ], [20, 40, 40], "Table 3.1 — Comparison of Inter- vs Intramolecular Hydrogen Bonding."),
            ("h2", "2. Physical Anomalies Caused by H-Bonding in Water"),
            ("bul", [
                "**Liquid Water vs Ice Density (Maximum Density at 4°C):** In ice, each oxygen is tetrahedrally surrounded by four H atoms (two covalent, two H-bonds), creating an **open cage-like structure** with large hexagonal voids. Density of ice < water (ice floats!). On heating from 0°C to 4°C, the cage collapses, packing molecules closer → **Density reaches maximum at 4°C (277 K)**.",
                "**Boiling Points of Group 15, 16, 17 Hydrides:** H2O, HF, NH3 have abnormally high boiling points compared to their heavier group congeners (H2S, HCl, PH3) due to strong intermolecular H-bonding.",
            ]),
        ],
    },
    # ------------------------------------------------------------------ CB-18
    {
        "id": "CB-18",
        "title": "Symmetrical H-Bonds [F-H-F]-, KHF2 & Clathrate Cages",
        "blocks": [
            ("lead", "**Symmetrical Hydrogen Bonds & Clathrates** — Strongest H-Bonds & Ice Clathrates"),
            ("p", 'While most hydrogen bonds are unsymmetrical (X-H ··· Y, length ≈170 pm), exceptionally strong '
                  "**symmetrical hydrogen bonds** exist where the proton sits exactly equidistant between two electronegative atoms."),
            ("h2", '1. The Bifluoride Ion [HF2]^-^ & KHF2 Salt'),
            ("bul", [
                '**Bifluoride Ion [F-H-F]^-^:** When KF dissolves in anhydrous liquid HF, it forms **Potassium bifluoride KHF2** containing the linear [F-H-F]^−^ anion:\n'
                '  **KF + HF → K^+^ [F-H-F]^-^**\n'
                "  • The proton sits symmetrically in the center: both F-H distances are identical (**113 pm**).\n"
                '  • Bond energy = **≈165 kJ/mol** (the strongest hydrogen bond known, possessing significant covalent character!).',
                "**Non-Existence of KHCl2, KHBr2, KHI2:** Chlorine, Bromine, and Iodine cannot form [HCl2]^−^ because their lower electronegativity and larger radii make H-bonding far too weak to stabilize the triatomic complex anion.",
            ]),
            ("h2", "2. Clathrate Hydrates (Gas Hydrates)"),
            ("table", ["Type of Clathrate", "Host Framework", "Guest Trapped Atoms", "Key Conditions & Properties"], [
                ["Methane Clathrate (Burning Ice)", "Ice hydrogen-bonded cage (tetrakaidecahedral)", "Methane CH4 gas molecules", 'Forms on ocean floors under high pressure; massive fossil energy reserve: CH~4~ · 5.75 H~2~O'],
                ["Noble Gas Clathrates", "Quinol (hydroquinone) hydrogen-bonded cage", "Ar, Kr, Xe (atomic radius 1.9 - 2.2 Å)", "He and Ne are too small and escape through the cage pores; no chemical bonding involved!"],
            ], [20, 26, 24, 30], "Table 3.2 — Hydrogen-bonded clathrate and inclusion architectures."),
            ("key", "TRAP: Does KHF2 exist as K^+^ + H^+^ + 2 F^−^? NO! It exists strictly as K^+^ and the complex bifluoride anion [HF~2~]^−^. On heating, it decomposes into KF + HF↑."),
        ],
    },
    # ------------------------------------------------------------------ CB-19
    {
        "id": "CB-19",
        "title": "Intermolecular Forces: Keesom, Debye, London Dispersion Forces",
        "blocks": [
            ("lead", "**van der Waals Forces** — Classification of Weak Non-Covalent Interactions"),
            ("p", "Collective term for weak intermolecular attractive forces that operate between neutral molecules. "
                  'They are non-directional and decay rapidly with distance (typically as 1/r^6^).'),
            ("h2", "1. Three Components of van der Waals Forces"),
            ("table", ["Interaction Name", "Nature of Interacting Molecules", "Distance Dependence", "Physical Mechanism"], [
                ["1. Keesom Forces (Dipole-Dipole)", "**Two permanent polar dipoles** (e.g. HCl···HCl)", '**E ∝ 1{r^3^} { (stationary)}, E ∝ 1{r^6^} { (rotating)}**', "Electrostatic alignment of permanent positive and negative ends of polar molecules (temperature dependent)"],
                ["2. Debye Forces (Dipole-Induced Dipole)", "**Permanent polar dipole + Non-polar molecule** (e.g. HCl···noble gas)", '**E ∝ 1{r^6^}**', "Permanent dipole induces an instantaneous dipole in the polarizable electron cloud of adjacent non-polar molecule"],
                ["3. London Dispersion Forces (Instantaneous Induced Dipole)", "**Two non-polar molecules / Noble gases** (e.g. He···He, CH4···CH4, I2···I2)", '**E ∝ 1{r^6^}**', "Synchronized quantum fluctuations of electron density create transient dipoles that induce corresponding dipoles in neighbors"],
            ], [22, 28, 20, 30], "Table 3.3 — The three van der Waals interaction regimes."),
            ("h2", "2. Factors Influencing London Dispersion Forces"),
            ("bul", [
                "**Molecular Size / Surface Area:** Larger molecules have greater surface area of contact → stronger dispersion forces (e.g. Boiling points: n{-pentane } (36°C) > isopentane  (28°C) > neopentane  (9.5°C) due to spherical branching).",
                "**Polarizability (Number of Electrons):** Heavier atoms have diffuse, easily deformable electron clouds → stronger forces: He < Ne < Ar < Kr < Xe and F~2~ < Cl~2~ < Br~2~ < I~2~ (gas → liquid → solid!).",
            ]),
        ],
    },
    # ------------------------------------------------------------------ CB-20
    {
        "id": "CB-20",
        "title": "Metallic Bonding: Electron Sea Model & Band Theory",
        "blocks": [
            ("lead", "**Metallic Bonding** — Drude-Lorentz Electron Sea & Band Theory of Solids"),
            ("p", "Metals possess low ionization energies and vacant valence orbitals. Metallic bonding accounts for their "
                  "high electrical and thermal conductivity, metallic luster, malleability, and ductility."),
            ("h2", "1. Electron Sea (Drude-Lorentz) Model"),
            ("p", "A metal is viewed as a regular lattice of positive metal ions (kernels) immersed in a delocalised 'sea' "
                  "of mobile valence electrons. Nondirectional electrostatic attraction binds kernels to the electron sea:\n"
                  "• **Electrical Conductivity:** Applied electric field causes directional drift of mobile electrons.\n"
                  "• **Malleability & Ductility:** When hammered, layers of metal kernels slide over one another without shattering because the electron sea instantly adjusts to new positions (unlike brittle ionic crystals)."),
            ("h2", "2. Band Theory of Solids (Molecular Orbital Continuum)"),
            ("fig", "bandtheory", "Fig. 3.2 — Band theory: Conductor (overlapping bands), Semiconductor (small gap), Insulator (large gap)."),
            ("p", "In an infinite crystal lattice of N atoms, N atomic orbitals overlap to form an almost continuous band of energy levels:\n"
                  "• **Valence Band (VB):** Lower energy band filled with valence electrons.\n"
                  "• **Conduction Band (CB):** Higher energy unoccupied band.\n"
                  '• **Forbidden Energy Gap (E~g~):** Energy separation between top of VB and bottom of CB.'),
            ("table", ["Solid Type", 'Energy Bandgap (E~g~)', "Conduction Mechanism & Temperature Dependence"], [
                ["Conductor (Metal)", '**E~g~ = 0** (Valence band overlaps conduction band)', "Electrons move freely into conduction band. **Conductivity DECREASES with increasing T** (lattice phonon vibrations scatter electrons)"],
                ["Semiconductor (Si, Ge)", '**Small E~g~ (0.5 to 3 eV)**', "Thermal excitation promotes electrons across gap. **Conductivity INCREASES with increasing T** (intrinsic and extrinsic doping: p-type and n-type)"],
                ["Insulator (Diamond, Quartz)", '**Large E~g~ (> 5 eV)**', "Electrons cannot overcome large bandgap under normal thermal energies; zero electrical conductivity"],
            ], [20, 30, 50], "Table 3.4 — Band theory classification of electrical behavior."),
        ],
    },
    # ------------------------------------------------------------------ CB-21
    {
        "id": "CB-21",
        "title": "Radius Ratio Rules & Coordination Number in Ionic Crystals",
        "blocks": [
            ("lead", "**Radius Ratio Rules** — Limiting Geometry & Coordination Polyhedra"),
            ("p", "In ionic crystals, the stable geometric arrangement maximizes cation-anion attraction while avoiding "
                  'anion-anion contact. The coordination number (CN) is governed by the **limiting radius ratio** r~+~ / r~−~ = r~c~ / r~a~.'),
            ("h2", "1. Limiting Radius Ratio Rules Table"),
            ("table", ['Radius Ratio (r~+~ / r~−~)', "Coordination Number", "Coordination Geometry", "Mineral Lattice Prototype"], [
                ["< 0.155", "2", "Linear", "Gaseous molecules (BeF2)"],
                ["0.155 - 0.225", "3", "Planar Triangular", 'Boron trioxide (B2O3), Borates [BO3]^3-^'],
                ["0.225 - 0.414", "4", "**Tetrahedral**", "**Zinc Blende (ZnS)**, Wurtzite, BeO, CuCl"],
                ["0.414 - 0.732", "6", "**Octahedral**", "**Rock Salt (NaCl)**, MgO, FeO, KBr"],
                ["0.732 - 1.000", "8", "**Body-Centered Cubic (Cubic)**", "**Caesium Chloride (CsCl)**, CsBr, TlCl"],
                ["1.000 (Equal sizes)", "12", "Close-Packed (FCC / HCP)", "Pure Metals (Cu, Ag, Au)"],
            ], [20, 16, 24, 40], "Table 3.5 — Limiting radius ratios and coordination geometries."),
            ("h2", "2. Geometric Derivations of Limiting Values"),
            ("fig", "radiusratio", "Fig. 3.2 — Geometric derivation of limiting radius ratios: Octahedral square diagonal (0.414) and Cubic body diagonal (0.732)."),
            ("bul", [
                "**Tetrahedral Limit (r~+~ / r~−~ = 0.225):** Central cation touches 4 anions at tetrahedron corners: cos(109.5°/2) = sin(54°44') = r~a~{r~c~ + r~a~} ⇒ r~c~ / r~a~ = 0.225.",
                '**Octahedral Limit (r~+~ / r~−~ = 0.414):** Diagonal of equatorial square: 2(r~c~ + r~a~) = √2 (2 r~a~) ⇒ r~c~ / r~a~ = √2 - 1 = 0.414.',
                '**Cubic Limit (r~+~ / r~−~ = 0.732):** Body diagonal of cube: 2(r~c~ + r~a~) = √3 (2 r~a~) ⇒ r~c~ / r~a~ = √3 - 1 = 0.732.',
            ]),
        ],
    },
    # ------------------------------------------------------------------ CB-22
    {
        "id": "CB-22",
        "title": "Classic Crystal Structures: NaCl, CsCl, ZnS, CaF2, Na2O",
        "blocks": [
            ("lead", "**Classic Ionic Crystal Structures** — Unit Cells, Packing & Void Occupancy"),
            ("p", "Ionic solids pack anions into close-packed lattices (FCC or HCP) with cations occupying tetrahedral or octahedral voids."),
            ("h2", "1. Master Structural Matrix of Ionic Solids"),
            ("fig", "crystals", "Fig. 3.3 — Classic ionic crystal lattices: NaCl (6:6), CsCl (8:8), and ZnS (4:4)."),
            ("table", ["Structure Type", "Anion Packing Array", "Cation Position & Void Occupancy", "Coord. No. (Cation : Anion)", "Formula Units per Cell (Z)"], [
                ["Rock Salt (NaCl)", 'FCC array of Cl^-^ ions', "Na+ occupies **ALL Octahedral Voids**", "**6 : 6**", "**Z = 4** NaCl units"],
                ["Caesium Chloride (CsCl)", 'Simple Cubic array of Cl^-^', "Cs+ occupies central **Cubic Void**", "**8 : 8**", "**Z = 1** CsCl unit"],
                ["Zinc Blende (Sphalerite ZnS)", 'FCC array of S^2-^ ions', 'Zn^2+^ occupies **ALTERNATE (50%) Tetrahedral Voids**', "**4 : 4**", "**Z = 4** ZnS units"],
                ["Fluorite (CaF2)", 'FCC array of Ca^2+^ ions', 'F^-^ occupies **ALL (100%) Tetrahedral Voids**', '**8 : 4** (Ca^2+^ is 8, F^-^ is 4)', "**Z = 4** CaF2 units"],
                ["Antifluorite (Na2O)", 'FCC array of O^2-^ ions', "Na+ occupies **ALL (100%) Tetrahedral Voids**", '**4 : 8** (Na+ is 4, O^2-^ is 8)', "**Z = 4** Na2O units"],
            ], [20, 22, 28, 18, 12], "Table 3.6 — Architectural parameters of standard ionic crystal lattices."),
            ("h2", "2. Transition Induced by Temperature and Pressure"),
            ("key", "Coordination Number Modulation:\n"
                    '• **High Pressure:** Compresses lattice, increasing Coordination Number: **NaCl (6:6) —(High Pressure)→ CsCl (8:8)**\n'
                    '• **High Temperature:** Expands lattice, decreasing Coordination Number: **CsCl (8:8) —(High Temperature (760 K))→ NaCl (6:6)**'),
        ],
    },
    # ------------------------------------------------------------------ CB-23
    {
        "id": "CB-23",
        "title": "Crystal Defects: Schottky, Frenkel & Non-Stoichiometric",
        "blocks": [
            ("lead", "**Crystal Imperfections & Defects** — Stoichiometric, Non-Stoichiometric & F-Centres"),
            ("p", "Real crystals deviate from perfect thermodynamic order above 0 K. Defects alter electrical conductivity, optical colour, and mechanical strength."),
            ("h2", "1. Stoichiometric Point Defects"),
            ("fig", "defects", "Fig. 3.4 — Crystal point defects: Schottky defect (equal ion vacancies) vs Frenkel defect (interstitial cation)."),
            ("table", ["Defect Type", "Physical Mechanism", "Effect on Crystal Density", "Conditions & Classic Examples"], [
                ["Schottky Defect", "**Equal number of cations and anions missing** from normal lattice sites, creating pairs of stoichiometric vacancies", "**Density DECREASES significantly** (mass decreases while cell volume is constant)", "Favored in highly ionic compounds with **high coordination number** and **nearly equal ionic sizes**: NaCl, KCl, CsCl, KBr, AgBr"],
                ["Frenkel Defect", "**Smaller ion (usually cation) leaves normal lattice site** and occupies an **interstitial void**", "**Density REMAINS UNCHANGED** (mass and volume both conserved)", 'Favored in compounds with **low coordination number** and **large size difference** (r~−~ ≫ r~+~): ZnS, AgCl, AgBr, AgI'],
            ], [18, 32, 25, 25], "Table 3.7 — Schottky versus Frenkel defects comparison."),
            ("key", "The AgBr Special Case (Universal JEE Question):\n"
                    "**Silver Bromide (AgBr) exhibits BOTH Schottky and Frenkel defects!** "
                    "Radius of Ag+ is intermediate; it can fit into interstitial voids (Frenkel) or form stoichiometric ion pairs (Schottky)."),
            ("h2", "2. Non-Stoichiometric Defects & F-Centres (Colour in Crystals)"),
            ("bul", [
                '**Metal Excess Defect by Anion Vacancies (F-Centres):** When NaCl is heated in sodium vapor, Na atoms deposit on surface, forming Na+; Cl^-^ ions diffuse to surface to form NaCl. The liberated electrons diffuse into the lattice and occupy the anion vacancies.\n'
                "  • An electron trapped in an anion vacancy is called an **F-Centre (Farbe centre / colour centre)**.\n"
                "  • Trapped electrons absorb visible light and undergo transitions: **NaCl becomes Yellow**, **KCl becomes Violet/Lilac**, **LiCl becomes Pink**!",
                '**Metal Deficiency Defect:** Cation vacancies where missing charge is compensated by adjacent cations in higher oxidation states (e.g. Non-stoichiometric FeO exists as Fe~0.95~O containing both Fe^2+^ and Fe^3+^).',
            ]),
        ],
    },
    # ------------------------------------------------------------------ CB-24
    {
        "id": "CB-24",
        "title": "Master Synthesis & Review: Predicting Bond Type & Geometry",
        "blocks": [
            ("lead", "**Master Bonding Decision Algorithm** — Step-by-Step Pathway for Any Molecule"),
            ("p", "A consolidated 5-step diagnostic workflow to solve any bonding, geometry, or polarity question in JEE Advanced."),
            ("h2", "1. The 5-Step Structural Decision Tree"),
            ("num", [
                "**Step 1: Compute Total Valence Electrons & Draw Lewis Formula:** Check if octet is complete, expanded (Period 3+), or hypovalent. Calculate formal charges to pick the best resonance structure.",
                "**Step 2: Determine Steric Number & Hybridization:** SN = σ-bonds + lone pairs. Apply Bent's rule if sp^3^d (lone pairs eq, electronegative atoms ax). Check Drago's rule (if central atom is Period 3+ with lp and attached to H, no hybridization!).",
                "**Step 3: Evaluate Back-Bonding / Bridge Bonding:** Check if an electron-deficient central atom (B, Be, Al) can receive dative π-backbonding from attached donor (F, O, N) or must dimerise via 3c-2e banana bonds (B2H6, BeH2) or 3c-4e halide bridges (Al2Cl6).",
                "**Step 4: Predict VSEPR Geometry & Net Dipole Moment:** Place electron pairs to minimize repulsions. Deduce vector sum {μ}: cancel symmetric vectors (CO2, BF3, CCl4, SF6, XeF4 → μ = 0); distorted systems retain permanent dipole.",
                "**Step 5: Apply Molecular Orbital Theory for Diatomics / Radicals:** For diatomics (1 to 20 electrons), write MO configuration. Check s-p mixing (≤ 14e^−^ vs > 14e^−^). Calculate Bond Order and identify unpaired electrons (paramagnetism).",
            ]),
            ("h2", "2. Master Diagnostic Summary Table"),
            ("table", ["Molecule", "Central Hybrid.", "VSEPR Geometry", "Dipole Moment (μ)", "Key Chemical Feature"], [
                ["XeF2", "sp^3^d (3 lp eq)", "**Linear**", "μ = 0", "3 equatorial lone pairs cancel; non-polar"],
                ["XeF4", 'sp^3^d^2^ (2 lp ax)', "**Square Planar**", "μ = 0", "2 axial lone pairs oppose; non-polar"],
                ["SF4", "sp^3^d (1 lp eq)", "**See-Saw**", "μ ≠ 0 (Polar)", "Equatorial lone pair distorts axial bonds"],
                ["ClF3", "sp^3^d (2 lp eq)", "**T-Shaped**", "μ ≠ 0 (Polar)", "Two equatorial lone pairs compress F-Cl-F to 87.5°"],
                ['I3^-^', "sp^3^d (3 lp eq)", "**Linear**", "μ = 0", "Linear symmetrical triiodide anion"],
                ['[ICl4]^-^', 'sp^3^d^2^ (2 lp ax)', "**Square Planar**", "μ = 0", "Octahedral parent geometry with 2 axial lone pairs"],
                ["N(SiH3)3", "sp^2^ (planar)", "**Planar Trigonal**", "μ = 0", "pπ-dπ back-bonding destroys basicity"],
                ["O(SiH3)2", "Bent (widened)", "**Bent (angle 144°)**", "μ ≠ 0", "2pπ(O) → 3dπ(Si) back-bonding widens angle"],
            ], [12, 18, 18, 16, 36], "Table 3.8 — Diagnostic matrix for classic examination molecules."),
        ],
    },
]
