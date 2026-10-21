# -*- coding: utf-8 -*-
"""Group 14: Carbon Family (8 sheets / pages G14-01 to G14-08)."""

SHEETS = [
    # ------------------------------------------------------------------ G14-01
    {
        "id": "G14-01",
        "title": "Group 14 Trends, Catenation, Allotropy & Inert Pair",
        "blocks": [
            ("lead", "**Group 14: Carbon Family (ns^2 np^2)** — Periodic Trends, Catenation & Inert Pair"),
            ("p", "Contains C (non-metal), Si (metalloid), Ge (metalloid), Sn and Pb (metals). "
                  "Key characteristics: remarkable catenation ability of Carbon, pπ-pπ vs pπ-dπ multiple bonding, "
                  "and strong inert pair effect making Pb(II) far more stable than Pb(IV)."),
            ("h2", "1. Periodic Trends in Group 14"),
            ("table", ["Element", "Config.", "Covalent Radius (pm)", "IE-1 (kJ/mol)", "M.P. (°C)", "Electronegativity"], [
                ["C", "[He] 2s^2 2p^2", "77", "1086", "4100 (diamond)", "2.5"],
                ["Si", "[Ne] 3s^2 3p^2", "118", "786", "1410", "1.8"],
                ["Ge", "[Ar] 3d^10 4s^2 4p^2", "122", "761", "937", "1.8"],
                ["Sn", "[Kr] 4d^10 5s^2 5p^2", "140", "708", "232", "1.8"],
                ["Pb", "[Xe] 4f^14 5d^10 6s^2 6p^2", "146", "715 (Pb > Sn!)", "327", "1.9"],
            ], [12, 28, 20, 16, 14, 10], "Table 14.1 — Periodic properties of Group 14 elements."),
            ("key", "Ionization Enthalpy: **C > Si > Ge > Pb > Sn** (Pb has higher IE than Sn due to poor 4f shielding).\n"
                    "Catenation Order: **C >>> Si > Ge ≈ Sn >> Pb** (Directly follows E-E single bond strength: C-C 348 > Si-Si 297 > Ge-Ge 260 > Sn-Sn 240 kJ/mol)."),
            ("h2", "2. Inert Pair Effect & Redox Behaviour of Sn and Pb"),
            ("bul", [
                "**+4 Oxidation State:** C(+4), Si(+4), Ge(+4), Sn(+4) are stable. Pb(+4) is unstable and a **powerful oxidising agent** (PbO2 + 4 HCl -> PbCl2 + Cl2 + 2 H2O).",
                "**+2 Oxidation State:** Sn(+2) is a **strong reducing agent** (Sn^2+ -> Sn^4+ + 2e^-, E° = -0.15 V). Used to reduce FeCl3 to FeCl2, and HgCl2 to white Hg2Cl2 then black Hg.",
                "**Pb(+2) vs Pb(+4):** Pb(+2) is extremely stable. PbCl4 decomposes on warming to PbCl2 + Cl2. PbI4 and PbBr4 do not even exist because I^- and Br^- reduce Pb^4+ instantly!",
            ]),
            ("trap", "TRAP: PbO2 dissolves in conc. HNO3 with evolution of O2: 2 PbO2 + 4 HNO3 -> 2 Pb(NO3)2 + 2 H2O + O2↑. It does NOT form a nitrate of lead(IV)!"),
            ("h2", "3. Multiple Bonding: pπ-pπ vs dπ-pπ"),
            ("p", "Carbon forms very strong **pπ-pπ multiple bonds** (C=C, C≡C, C=O, C≡N) because 2p orbitals are compact and overlap sideways efficiently. "
                  "Heavier elements (Si, Ge, Sn) have large, diffuse p orbitals that cannot form stable pπ-pπ bonds; they prefer single bonds or use empty d orbitals (dπ-pπ)."),
        ],
    },
    # ------------------------------------------------------------------ G14-02
    {
        "id": "G14-02",
        "title": "Allotropes of Carbon: Diamond, Graphite & Fullerenes",
        "blocks": [
            ("lead", "**Allotropes of Carbon** — Diamond, Graphite, Fullerenes & Thermodynamic Stability"),
            ("p", "Carbon exhibits rich allotropy due to catenation and ability to adopt sp^3, sp^2, and sp hybridization."),
            ("h2", "1. Structural Comparison of Major Allotropes"),
            ("table", ["Property", "Diamond", "Graphite", "Fullerene (C60)"], [
                ["Hybridization & Geometry", "sp^3, 3D tetrahedral network", "sp^2, 2D planar hexagonal sheets", "sp^2 (curved), soccer-ball (Ih symmetry)"],
                ["C-C Bond Length", "154 pm (all uniform single bonds)", "141.5 pm (in-plane), 340 pm (inter-layer)", "145 pm (single, 6-5 ring), 138 pm (double, 6-6 ring)"],
                ["Conductivity", "Electrical insulator (bandgap 5.5 eV)", "Good electrical conductor along planes", "Semiconductor; K3C60 is a superconductor (18 K)"],
                ["Density & Hardness", "3.51 g/cm^3, Hardest natural substance", "2.22 g/cm^3, Soft, slippery (solid lubricant)", "1.65 g/cm^3, Molecular solid (soluble in toluene)"],
                ["Standard Heat of Formation", "+1.90 kJ/mol (metastable at RTP)", "**0.00 kJ/mol (Thermodynamically MOST stable)**", "+38.1 kJ/mol"],
            ], [18, 22, 24, 20, 16], "Table 14.2 — Comparative crystallography and physics of Carbon allotropes."),
            ("key", "**Thermodynamic Stability:** Graphite is the standard state of carbon (ΔH°_f = 0). "
                    "Diamond conversion to graphite is thermodynamically favored (ΔG < 0) but kinetically dormant (huge activation energy)."),
            ("h2", "2. Buckminsterfullerene (C60) Architecture"),
            ("bul", [
                "**Faces & Rings:** C60 contains **20 six-membered rings (hexagons)** and **12 five-membered rings (pentagons)**.",
                "**Isolated Pentagon Rule (IPR):** Six-membered rings can fuse with both hexagons and pentagons, but **five-membered rings ONLY fuse with six-membered rings** (no two pentagons share an edge, minimising strain).",
                "**Bond Alternation:** C=C double bonds exist strictly at the junction of two hexagons (6-6 ring fusion, length 138 pm). Single bonds exist at 6-5 junctions (145 pm).",
            ]),
            ("h2", "3. Amorphous Carbon Allotropes & Adsorption"),
            ("p", "Coke, Charcoal, Lampblack, Carbon black, and Activated Charcoal. Activated charcoal has an immense "
                  "surface area (~1000 m^2/g) and is used in gas masks, decolourisation of sugar, and water filtration."),
        ],
    },
    # ------------------------------------------------------------------ G14-03
    {
        "id": "G14-03",
        "title": "Carbides Classification: Ionic, Covalent & Interstitial",
        "blocks": [
            ("lead", "**Carbides** — Ionic (Salt-like), Covalent, Interstitial & Hydrolysis Pathways"),
            ("p", "Carbides are binary compounds of carbon with elements of lower or comparable electronegativity. "
                  "They are classified into three distinct structural classes based on bonding."),
            ("h2", "1. Salt-like (Ionic) Carbides & Hydrolysis Products"),
            ("p", "Formed by highly electropositive metals (Group 1, 2, Al). Classified by the hydrocarbon gas evolved on hydrolysis:"),
            ("table", ["Carbide Type", "Carbon Anion", "Example Carbides", "Hydrolysis Reaction & Gas Evolved"], [
                ["Methanides", "C^4- (isolated carbon)", "Al4C3, Be2C", "Al4C3 + 12 H2O -> 4 Al(OH)3 + **3 CH4↑** (Methane)"],
                ["Acetylides", "C2^2- ([:C≡C:]^2-)", "CaC2, MgC2, Cu2C2, Ag2C2", "CaC2 + 2 H2O -> Ca(OH)2 + **C2H2↑** (Ethyne / Acetylene)"],
                ["Allylenides", "C3^4- ([:C=C=C:]^4-)", "Mg2C3", "Mg2C3 + 4 H2O -> 2 Mg(OH)2 + **CH3-C≡CH↑** (Propyne / Allylene)"],
            ], [18, 20, 22, 40], "Table 14.3 — Ionic carbides and their diagnostic hydrolysis gases (JEE Favourite)."),
            ("key", "Memory Rule for Hydrolysis:\n"
                    "• **Be2C & Al4C3** -> CH4 (Methanides)\n"
                    "• **CaC2, BaC2, Na2C2** -> C2H2 (Acetylides)\n"
                    "• **Mg2C3** -> CH3-C≡CH (Allylenide / Propyne)"),
            ("h2", "2. Covalent & Interstitial Carbides"),
            ("bul", [
                "**Covalent Carbides:** Formed by elements of similar size and electronegativity:\n"
                "  • **Silicon Carbide (SiC, 'Carborundum'):** 3D diamond-like covalent network. Extremely hard (Mohs 9.5), inert to acids, refractory abrasive (prep: SiO2 + 3 C --(2000°C)--> SiC + 2 CO).\n"
                "  • **Boron Carbide (B4C):** Hardest artificial carbide, used in tank armor and nuclear reactor control rods.",
                "**Interstitial Carbides:** Formed by transition metals (TiC, WC, TaC, V4C3, Fe3C):\n"
                "  Small carbon atoms occupy octahedral interstitial voids in the close-packed metal lattice without changing metal structure. Retain metallic electrical conductivity, possess ultra-high melting points (>3000°C), and extreme hardness.",
            ]),
        ],
    },
    # ------------------------------------------------------------------ G14-04
    {
        "id": "G14-04",
        "title": "Oxides of Carbon: CO, CO2, C3O2 & Carbonates",
        "blocks": [
            ("lead", "**Oxides of Carbon** — CO (Ligand & Toxicity), CO2, C3O2 & Carbonate Chemistry"),
            ("p", "Carbon forms three well-characterised oxides: neutral CO, acidic CO2, and carbon suboxide C3O2."),
            ("h2", "1. Carbon Monoxide (CO) — Structure & Bonding"),
            ("p", "Iso-electronic with N2 and CN^- (10 valence electrons). Molecular Orbital configuration:\n"
                  "σ(2s)^2 σ*(2s)^2 π(2p_x)^2 π(2p_y)^2 σ(2p_z)^2. Bond order = 3 (one sigma, two pi bonds)."),
            ("bul", [
                "**Dipole Moment:** Remarkably low (0.11 D) directed C^δ- <--- O^δ+ (dative lone pair from O to C cancels electronegativity difference!).",
                "**Coordination Chemistry:** Acts as a strong **π-acid ligand** in transition metal carbonyls (e.g. Ni(CO)4, Fe(CO)5) via σ-donation from C and π-backbonding into empty π* orbitals of CO.",
                "**Toxicity:** Binds to blood haemoglobin ~300 times more strongly than O2 to form **carboxyhaemoglobin**, preventing oxygen delivery.",
            ]),
            ("table", ["Laboratory Synthesis", "Industrial / Gas Mixtures", "Reactions"], [
                ["Dehydration of Formic Acid: HCOOH --(conc. H2SO4, 373 K)--> CO + H2O", "Water Gas (Synthesis gas): C + H2O(g) --(1270 K)--> CO + H2", "Combustion: 2 CO + O2 -> 2 CO2 (blue flame)"],
                ["Dehydration of Oxalic Acid: (COOH)2 --(conc. H2SO4)--> CO + CO2 + H2O (absorb CO2 in KOH)", "Producer Gas: 2 C + O2 + 4 N2 --(1270 K)--> 2 CO + 4 N2", "Mond Process: Ni + 4 CO --(330 K)--> Ni(CO)4 --(450 K)--> Ni + 4 CO"],
            ], [33, 33, 34], "Table 14.4 — Synthesis and reactions of Carbon Monoxide."),
            ("h2", "2. Carbon Suboxide (C3O2)"),
            ("p", "Prepared by dehydrating malonic acid with phosphorus pentoxide:\n"
                  "CH2(COOH)2 + P4O10 --(150°C)--> **O=C=C=C=O** + 4 HPO3\n"
                  "Structure: Linear, cumulative double bond system, sp-hybridized central carbons, bp 7°C, foul odor. Hydrolyses back to malonic acid."),
            ("h2", "3. Carbon Dioxide (CO2) & Bicarbonate Buffers"),
            ("bul", [
                "Linear molecule (O=C=O, D_∞h symmetry), μ = 0, C-O bond length 116 pm (partial triple bond character).",
                "Lime water test: Ca(OH)2 + CO2 -> **CaCO3↓** (white turbidity) + H2O. Excess CO2 dissolves turbidity: CaCO3 + CO2 + H2O -> **Ca(HCO3)2** (soluble). On boiling, turbidity returns!",
            ]),
        ],
    },
    # ------------------------------------------------------------------ G14-05
    {
        "id": "G14-05",
        "title": "Oxides & Hydrides of Silicon: SiO2, Quartz & Silanes",
        "blocks": [
            ("lead", "**Silicon Dioxide (SiO2) & Silanes** — 3D Network Structure & Hydrolysis"),
            ("p", "While CO2 is a discrete linear gas, SiO2 is a high-melting 3D network solid because Si cannot form stable pπ-pπ double bonds with oxygen."),
            ("h2", "1. Structure & Allotropy of Silica (SiO2)"),
            ("bul", [
                "**Network Architecture:** Every Si atom is **sp^3 hybridized** and tetrahedrally bonded to 4 Oxygen atoms. Every O atom is shared between 2 Si atoms (Si-O-Si angle ≈ 144°), yielding empirical formula SiO2.",
                "**Crystalline Forms:** Quartz (piezoelectric), Tridymite, and Cristobalite (interconvertible at high temperatures).",
                "**Chemical Inertness:** Very inert; attacked only by HF and strong hot caustic alkali:\n"
                "  • With HF (Etching of glass): SiO2 + 4 HF -> **SiF4** + 2 H2O; SiF4 + 2 HF -> **H2SiF6** (Hydrofluorosilicic acid).\n"
                "  • With NaOH: SiO2 + 2 NaOH -> **Na2SiO3** (Water glass) + H2O.",
            ]),
            ("h2", "2. Silanes (Si_n H_{2n+2}) vs Alkanes"),
            ("p", "Silanes are the silicon hydrides (SiH4, Si2H6, up to Si6H14), prepared by reacting Mg2Si with dil. HCl:\n"
                  "Mg2Si + 4 HCl -> 2 MgCl2 + SiH4 (Monosilane)."),
            ("table", ["Property", "Methane (CH4)", "Silane (SiH4)"], [
                ["Combustion / Air Stability", "Stable in air, requires ignition (ΔH_comb = -890 kJ)", "Spontaneously inflammable in air (pyrophoric!):\nSiH4 + 2 O2 -> SiO2 + 2 H2O"],
                ["Hydrolysis by Water", "Completely inert to water and aqueous alkali", "Violently hydrolysed by even traces of base:\nSiH4 + (n+2) H2O --(OH^-)--> SiO2·nH2O + 4 H2↑"],
                ["Polarity of E-H Bond", "C^δ- - H^δ+ (χ_C = 2.5 > χ_H = 2.1)", "Si^δ+ - H^δ- (χ_Si = 1.8 < χ_H = 2.1; Hydridic H!)"],
                ["Mechanism of Attack", "Carbon has no vacant d orbitals; SN2 hindered", "Si has accessible empty 3d orbitals; nucleophilic attack by OH^- is very fast"],
            ], [22, 38, 40], "Table 14.5 — Why Silane is hyper-reactive compared to Methane."),
            ("trap", "TRAP: Carbon tetrachloride CCl4 is completely inert to water, but Silicon tetrachloride SiCl4 hydrolyses violently: SiCl4 + 4 H2O -> Si(OH)4 + 4 HCl. Si utilizes vacant 3d orbitals to expand its coordination number!"),
        ],
    },
    # ------------------------------------------------------------------ G14-06
    {
        "id": "G14-06",
        "title": "Silicates: Ortho, Pyro, Cyclic, Chain, Sheet & 3D Network",
        "blocks": [
            ("lead", "**Silicate Minerals** — Classification, Structural Units & Sharing of Oxygen Vertices"),
            ("p", "The basic building unit of all silicates is the tetrahedral **[SiO4]^4-** unit. Silicates are classified "
                  "strictly by how many corners (oxygen atoms) are shared between adjacent [SiO4] tetrahedra."),
            ("h2", "1. Classification of Silicates"),
            ("table", ["Silicate Class", "Shared O / Tetrahedron", "General Formula Unit", "Mineral Examples"], [
                ["1. Orthosilicates (Neso)", "0 (discrete units)", "[SiO4]^4-", "Phenacite (Be2SiO4), Willemite (Zn2SiO4), Olivine (Mg2SiO4), Forsterite"],
                ["2. Pyrosilicates (Soro)", "1 (dimeric unit)", "[Si2O7]^6-", "Thortveitite (Sc2Si2O7), Hemimorphite (Zn4(OH)2Si2O7·H2O)"],
                ["3. Cyclic / Ring", "2 (closed rings)", "[Si3O9]^6- or [Si6O18]^12-", "Benitoite (BaTiSi3O9), Beryl (Be3Al2Si6O18 — gemstone emerald)"],
                ["4. Single Chain (Ino / Pyroxenes)", "2 (infinite line)", "([SiO3]^2-)_n", "Diopside (CaMg(SiO3)2), Spodumene (LiAl(SiO3)2), Enstatite"],
                ["5. Double Chain (Amphiboles)", "2.5 (alternating 2 and 3)", "([Si4O11]^6-)_n", "Tremolite (Ca2Mg5(Si4O11)2(OH)2), Asbestos minerals"],
                ["6. Sheet Silicates (Phyllo)", "3 (2D planar infinite sheets)", "([Si2O5]^2-)_n", "Talc (Mg3(Si2O5)2(OH)2), Kaolinite (clay), Mica, Muscovite"],
                ["7. 3D Framework (Tecto)", "4 (all four corners shared)", "(SiO2)_n", "Quartz, Feldspar, Zeolites, Ultramarines"],
            ], [20, 22, 25, 33], "Table 14.6 — Master classification of Silicate minerals (JEE Advanced core)."),
            ("fig", "silicates", "Fig. 14.1 — Structural polyhedra of Ortho, Pyro, and Cyclic silicates."),
            ("key", "General Charge Rule: Formula of a silicate sharing 'c' corners per tetrahedron is **[SiO_{4 - c/2}]^{(4-c)-}**.\n"
                    "• c = 0 -> [SiO4]^4- (Ortho)\n"
                    "• c = 1 -> [Si2O7]^6- (Pyro)\n"
                    "• c = 2 -> [SiO3]_n^2n- (Cyclic & Single Chain)\n"
                    "• c = 3 -> [Si2O5]_n^2n- (Sheet)\n"
                    "• c = 4 -> SiO2 (3D Framework)"),
        ],
    },
    # ------------------------------------------------------------------ G14-07
    {
        "id": "G14-07",
        "title": "Silicones & Zeolites: Synthesis, Structure & Catalysis",
        "blocks": [
            ("lead", "**Silicones & Zeolites** — Synthetic Polymers & Shape-Selective Catalysts"),
            ("p", "Silicones are synthetic organosilicon polymers containing repeating **-R2Si-O-** units. "
                  "Zeolites are microporous aluminosilicate 3D framework molecular sieves."),
            ("h2", "1. Synthesis & Control of Silicones"),
            ("p", "Prepared from alkylchlorosilanes synthesized by Rochow reaction: 2 RCl + Si --(Cu powder, 570 K)--> R2SiCl2:"),
            ("bul", [
                "**Chain Propagation (Linear Silicones):** Hydrolysis of **R2SiCl2** gives R2Si(OH)2 which undergoes linear condensation polymerization:\n"
                "  n R2SiCl2 + 2n H2O -> n R2Si(OH)2 -> **...-O-Si(R2)-O-Si(R2)-O-...** (linear silicone).",
                "**Chain Termination (Controlling Molecular Weight):** Addition of **R3SiCl** produces monofunctional R3Si-OH, capping the chain ends and terminating growth.",
                "**Cross-Linked (Resin) Silicones:** Hydrolysis of **RSiCl3** produces trifunctional RSi(OH)3 which condenses in three directions forming a rigid 3D cross-linked silicone polymer.",
            ]),
            ("table", ["Monomer Precursor", "Hydrolysis Intermediate", "Resulting Silicone Polymer Structure"], [
                ["R3SiCl (monochlorosilane)", "R3SiOH (monofunctional)", "Dimer: R3Si-O-SiR3 (Chain Stopper / Capping agent)"],
                ["R2SiCl2 (dichlorosilane)", "R2Si(OH)2 (difunctional)", "Linear chain polymer or Cyclic oligomers (e.g. (R2SiO)3)"],
                ["RSiCl3 (trichlorosilane)", "RSi(OH)3 (trifunctional)", "Cross-linked 3D network resin (high thermal rigidity)"],
            ], [25, 25, 50], "Table 14.7 — Role of chlorosilane precursors in silicone architecture."),
            ("h2", "2. Properties & Applications of Silicones"),
            ("p", "High thermal stability, water-repellent (hydrophobic organic R groups point outward), electrical insulators, biocompatible (prosthetics, lubricants, waterproof fabrics)."),
            ("h2", "3. Zeolites: Three-Dimensional Aluminosilicates"),
            ("bul", [
                "**Formula & Charge Balance:** In 3D framework SiO2, when some Si^4+ atoms are replaced by Al^3+, the framework acquires a net negative charge balanced by extra-framework cations (Na^+, K^+, Ca^2+): **M_{x/n} [(AlO2)_x (SiO2)_y]·z H2O**.",
                "**Shape-Selective Catalysis:** Zeolites possess open honeycomb cages with uniform pore sizes (3 to 10 Å). Only molecules of fitting dimensions can enter and react.",
                "**ZSM-5 (Zeolite Socony Mobil-5):** Converts alcohols directly into gasoline (hydrocarbons) by shape-selective dehydration: **x CH3OH --(ZSM-5, 670 K)--> Gasoline (C_n H_{2n+2}) + x H2O**.",
                "**Water Softening:** Permutit (hydrated sodium aluminosilicate Na2Al2Si2O8·xH2O) exchanges Na^+ for Ca^2+ and Mg^2+ in hard water.",
            ]),
        ],
    },
    # ------------------------------------------------------------------ G14-08
    {
        "id": "G14-08",
        "title": "Halides & Low-Valent Chemistry of Si, Ge, Sn, Pb",
        "blocks": [
            ("lead", "**Group 14 Halides & Redox Trends** — Tetrahalides vs Dihalides"),
            ("p", "Tetrahalides MX4 (sp^3 tetrahedral) dominate for C, Si, Ge, and Sn, whereas dihalides MX2 (bent/polymeric) "
                  "become progressively stable descending to Pb due to the inert pair effect."),
            ("h2", "1. Tetrahalides: Hydrolysis Mechanisms & Exceptions"),
            ("bul", [
                "**CCl4 Inertness:** CCl4 does not hydrolyse in neutral or basic water because Carbon is in the 2nd period: no vacant d orbitals are available to expand its octet to accept the nucleophilic lone pair of water.",
                "**SiCl4, GeCl4, SnCl4 Hydrolysis:** Rapid and exothermic. Water coordinates to vacant d orbitals of the central atom forming a 5-coordinate intermediate, followed by elimination of HCl:\n"
                "  SiCl4 + 4 H2O -> [Si(OH)4] (orthosilicic acid) -> SiO2·xH2O + 4 HCl.",
                "**Lead Tetrahalides:** PbCl4 is a yellow oily liquid that readily decomposes to PbCl2 + Cl2. **PbBr4 and PbI4 do not exist** because Pb^4+ oxidises Br^- and I^- spontaneously.",
            ]),
            ("table", ["Halide", "Physical State", "Oxidation State", "Key Chemical Reaction / Behaviour"], [
                ["SnCl2", "White solid", "+2 (reducing)", "SnCl2 + 2 FeCl3 -> SnCl4 + 2 FeCl2; reduces HgCl2 -> Hg2Cl2↓ -> Hg↓"],
                ["SnCl4", "Colorless liquid (fuming)", "+4", "Forms hexachlorostannate with HCl: SnCl4 + 2 HCl -> H2[SnCl6]"],
                ["PbCl2", "White crystalline solid", "+2 (stable)", "Insoluble in cold water, soluble in hot water (recrystallises as needles)"],
                ["PbCl4", "Yellow liquid (unstable)", "+4 (oxidising)", "Decomposes explosively on heating: PbCl4 --(Δ)--> PbCl2 + Cl2↑"],
            ], [15, 25, 20, 40], "Table 14.8 — Comparative chemistry of Tin and Lead chlorides."),
            ("h2", "2. Dihalides & Carbene Analogues"),
            ("p", "In the gas phase, Group 14 dihalides (CF2, SiCl2, GeCl2, SnCl2, PbCl2) are VSEPR **bent (V-shaped)** molecules "
                  "with a lone pair and an empty p orbital (carbene analogues). In the solid state, SnCl2 and PbCl2 form "
                  "extended halogen-bridged polymers or ionic lattices."),
            ("key", "Oxidising vs Reducing Summary:\n"
                    "• **Sn^2+ is REDUCING:** Sn^2+ -> Sn^4+ + 2e^- (favors +4 state)\n"
                    "• **Pb^4+ is OXIDISING:** Pb^4+ + 2e^- -> Pb^2+ (favors +2 state due to inert pair effect)"),
        ],
    },
]
