# -*- coding: utf-8 -*-
"""Group 13: Boron Family (8 sheets / pages G13-01 to G13-08)."""

SHEETS = [
    # ------------------------------------------------------------------ G13-01
    {
        "id": "G13-01",
        "title": "Group 13 Trends, Anomalies, Inert Pair & Boron Extraction",
        "blocks": [
            ("lead", '**Group 13: Boron Family (ns^2^ np^1^)** — Periodic Trends & Anomalies'),
            ("p", "Group 13 contains B (non-metal), Al (metal/amphoteric), Ga, In, Tl (post-transition metals). "
                  "The chemistry is dominated by: small size of B, inert pair effect descending the group, and "
                  "poor d/f electron shielding causing atomic radius and ionization enthalpy anomalies."),
            ("h2", "1. Atomic Radii & Ionization Enthalpy Anomalies"),
            ("table", ["Element", "IE-1 (kJ/mol)", "Atomic Radius (pm)", "Key Electronic Reason"], [
                ['B [He] 2s^2^ 2p^1^', "801", "85", "Extremely small size, covalent network, high charge density"],
                ['Al [Ne] 3s^2^ 3p^1^', "577", "143", "Normal expansion with full 8-electron noble core"],
                ['Ga [Ar] 3d^10^ 4s^2^ 4p^1^', "579", "135", 'r(Ga) < r(Al)! Poor shielding by 3d^10^ → Z~eff~ increases'],
                ['In [Kr] 4d^10^ 5s^2^ 5p^1^', "558", "167", "Normal size increase after 4d shell"],
                ['Tl [Xe] 4f^14^ 5d^10^ 6s^2^ 6p^1^', "589", "170", "IE(Tl) > IE(In)! Lanthanoid contraction (poor 4f shielding)"],
            ], [22, 18, 22, 38], "Table 13.1 — G13 physical property anomalies (NCERT & JD Lee)."),
            ("key", "Atomic Radius Order: **B < Ga < Al < In ≈ Tl** (Ga smaller than Al due to 3d contraction).\n"
                    "Ionization Enthalpy Order: **B > Tl > Ga > Al > In** (Tl has 2nd highest IE due to 4f contraction)."),
            ("h2", "2. Inert Pair Effect & Oxidation States (+3 vs +1)"),
            ("p", 'Descending the group, the 6s^2^ pair of valence electrons becomes increasingly reluctant to '
                  "participate in bonding due to high effective nuclear charge following 4f and 5d subshells."),
            ("bul", [
                '**+3 Stability Order:** B(+3) > Al(+3) > Ga(+3) > In(+3) > Tl(+3). Tl^3+^ is a powerful **oxidising agent** (Tl^3+^ + 2e^-^ → Tl^+^, E° = +1.26 V).',
                "**+1 Stability Order:** B(+1) < Al(+1) < Ga(+1) < In(+1) < **Tl(+1)**. TlCl, TlOH are ionic and stable like alkali metals (TlOH is a strong base).",
                '**Al(+1) and Ga(+1):** Disproportionate in water: 3 Ga^+^ → 2 Ga + Ga^3+^.',
            ]),
            ("trap", 'TRAP: TlI3 is NOT Thallium(III) iodide! It is an ionic compound **Tl^+^ (I3^-^)** containing the linear triiodide anion. Tl^3+^ readily oxidises I^-^ to I2!'),
            ("h2", "3. Extraction & Reactivity of Boron"),
            ("p", "Boron is extracted from **Borax (Na2B4O7·10H2O)** or **Colemanite (Ca2B6O11·5H2O)**:\n"
                  "1. Boil ore with dil. H2SO4 → precipitate orthoboric acid H3BO3.\n"
                  "2. Ignite H3BO3 → B2O3. Then reduce: B2O3 + 3 Mg → 2 B (amorphous) + 3 MgO.\n"
                  "3. Ultra-pure crystalline B via van Arkel: 2 BBr3 + 3 H2 (Ta filament, 1200°C) → 2 B + 6 HBr."),
        ],
    },
    # ------------------------------------------------------------------ G13-02
    {
        "id": "G13-02",
        "title": "Diborane B2H6: 3c-2e Banana Bonds, Reactions & Cleavage",
        "blocks": [
            ("lead", "**Diborane (B2H6)** — Synthesis, 3c-2e Bonding, Cleavage & Reactions"),
            ("p", "Boron has only 3 valence electrons, so monomeric BH3 has only 6 valence electrons (Lewis acid). "
                  "It dimerises to B2H6 via two electron-deficient bridging bonds (multicentre 3c-2e bonds)."),
            ("h2", "1. Structure & Multi-Centre Bonding of B2H6"),
            ("fig", "diborane", "Fig. 13.1 — Diborane geometry with terminal (Ht) and bridging (Hb) hydrogens."),
            ("bul", [
                "**Terminal B-Ht:** 4 normal covalent 2c-2e bonds, coplanar in the xy-plane (B-Ht = 119 pm, H-B-H = 121°).",
                "**Bridging B-Hb-B:** 2 three-centre two-electron (3c-2e) 'banana' bonds, lying above and below the xy-plane (B-Hb = 133 pm, B-Hb-B = 97°).",
                '**Hybridization of B:** Each Boron atom is **sp^3^ hybridized** (4 electron domains). Total valence electrons = 2×3 + 6×1 = 12 electrons (6 pairs for 8 bond vectors).',
            ]),
            ("h2", "2. Cleavage of B2H6: Symmetrical vs Unsymmetrical"),
            ("p", "The mode of Lewis base cleavage depends directly on the base's steric size and hardness:"),
            ("table", ["Type of Cleavage", "Reagents (Lewis Bases)", "Product & Reaction Equation"], [
                ["Symmetrical Cleavage", "Bulky/Soft bases: NMe3, THF, CO, SMe2, PMe3", "B2H6 + 2 NMe3 → 2 Me3N:BH3 (splits into two BH3·L)"],
                ["Unsymmetrical Cleavage", "Small/Hard bases: NH3 (low T), MeNH2, Me2NH", 'B2H6 + 2 NH3 → [H2B(NH3)2]^+^ [BH4]^-^ (ionic salt)'],
            ], [22, 28, 50], "Table 13.2 — Cleavage mechanisms of Diborane (NCERT & JD Lee core)."),
            ("key", "Industrial Prep: 2 BF3 + 6 NaH → B2H6 + 6 NaF (at 450 K in polyether).\n"
                    "Laboratory Prep: 4 BF3·OEt2 + 3 LiAlH4 → 2 B2H6 + 3 LiAlF4 + 4 Et2O.\n"
                    "Redox Prep: 2 NaBH4 + I2 → B2H6 + 2 NaI + H2 (in diglyme)."),
            ("h2", "3. Reactions of B2H6"),
            ("bul", [
                "**Combustion:** B2H6 + 3 O2 → B2O3 + 3 H2O (ΔH° = -1976 kJ/mol, violent green flame, high fuel value).",
                "**Hydrolysis:** B2H6 + 6 H2O → 2 H3BO3 + 6 H2 (rapid, quantitative evolution of hydrogen).",
                "**Hydroboration:** B2H6 + 6 RCH=CH2 → 2 B(CH2CH2R)3 (syn-addition, anti-Markovnikov alcohol precursor).",
            ]),
        ],
    },
    # ------------------------------------------------------------------ G13-03
    {
        "id": "G13-03",
        "title": "Higher Boranes, Borohydrides & Organoboranes",
        "blocks": [
            ("lead", "**Higher Boranes & Hydroborates** — Wade's Rules, NaBH4 & Borazine"),
            ("p", "Boranes form extensive cluster families classified by skeletal electron pairs (Wade-Mingos rules): "
                  'Closo (B~n~ H~n+2~)^2-^, Nido (B~n~ H~n+4~), Arachno (B~n~ H~n+6~), and Hypho (B~n~ H~n+8~).'),
            ("h2", "1. Borazine B3N3H6 ('Inorganic Benzene')"),
            ("p", "Heating the unsymmetrical cleavage product of diborane and ammonia gives Borazine:\n"
                  '3 B2H6 + 6 NH3 (low T) → 3 [H2B(NH3)2]^+[BH4]^- —(heat, 450 K)→ **2 B3N3H6** + 12 H2\n'
                  "Alternate synthesis: 3 BCl3 + 3 NH4Cl → (ClBNH)3 + 9 HCl; reduce with NaBH4 → B3N3H6."),
            ("table", ["Property", "Benzene (C6H6)", "Borazine (B3N3H6)"], [
                ["Aromaticity", "Completely delocalised (150 kJ/mol)", "Partially delocalised (pi polar towards N)"],
                ["Polarity & Reactivity", "Non-polar, electrophilic substitution", "Polar (B^δ+ - N^δ-), addition reactions dominant"],
                ["Addition of HCl", "No reaction without AlCl3", "Adds 3 HCl readily: H to N, Cl to B → B3N3H9Cl3"],
                ["Hydrolysis", "Resistant to hydrolysis", "Hydrolyses readily: B3N3H6 + 9 H2O → 3 H3BO3 + 3 NH3 + 3 H2"],
            ], [22, 38, 40], "Table 13.3 — Comparison of Benzene vs Inorganic Benzene."),
            ("key", 'Borazine is **iso-electronic and iso-structural** to Benzene (planar hexagonal ring, sp^2^ B and N), '
                    'but chemically MUCH more reactive due to electronegativity difference (χ~N~ = 3.0, χ~B~ = 2.0).'),
            ("h2", "2. Sodium Borohydride (NaBH4) & LiAlH4"),
            ("bul", [
                "**NaBH4 Synthesis:** 4 NaH + B(OMe)3 → NaBH4 + 3 NaOMe (at 250°C).\n"
                '  Structure: Ionic [Na]^+^ [BH4]^-^ (tetrahedral BH4^-^, sp^3^ B, regular 2c-2e B-H bonds, 8 valence e^-^).',
                "**LiAlH4 Synthesis:** 4 LiH + AlCl3 → LiAlH4 + 3 LiCl (in dry ether).\n"
                "  Reducing power: LiAlH4 is a far stronger hydride donor than NaBH4 because Al-H is more polar and weaker than B-H. LiAlH4 reacts violently with water/alcohols; NaBH4 can be used in basic water/MeOH.",
            ]),
            ("trap", "TRAP: NaBH4 reduces aldehydes and ketones to alcohols, but does NOT reduce esters, amides, or carboxylic acids under standard conditions. LiAlH4 reduces all of them."),
        ],
    },
    # ------------------------------------------------------------------ G13-04
    {
        "id": "G13-04",
        "title": "Boron Trihalides, Lewis Acidity & Back-Bonding",
        "blocks": [
            ("lead", "**Boron Trihalides (BX3)** — pπ-pπ Back-Bonding & Lewis Acidity Inversion"),
            ("p", 'In BX3 (X = F, Cl, Br, I), Boron is sp^2^ hybridized with a vacant, unhybridized 2p~z~ orbital '
                  "perpendicular to the planar molecule. The halogen atom has filled p orbitals with lone pairs."),
            ("h2", "1. pπ-pπ Back-Bonding Mechanism"),
            ("p", "The lone pair in a filled 2p orbital of Fluorine overlaps sideways with the empty 2p orbital of Boron, "
                  "forming a **pπ-pπ dative back-bond**. This gives partial double bond character to the B-X bond."),
            ("table", ["Halide", "Back-Bond Overlap", "Extent of Back-Bonding", "Observed B-X Bond Length"], [
                ["BF3", "2p(B) ← 2p(F) (identical size, excellent match)", "Maximum back-bonding", "130 pm (much shorter than single bond 152 pm)"],
                ["BCl3", "2p(B) ← 3p(Cl) (diffuse 3p, poor overlap)", "Weak back-bonding", "175 pm"],
                ["BBr3", "2p(B) ← 4p(Br) (very diffuse 4p)", "Very weak back-bonding", "187 pm"],
                ["BI3", "2p(B) ← 5p(I) (energy/size mismatch)", "Negligible back-bonding", "210 pm"],
            ], [18, 32, 25, 25], "Table 13.4 — Back-bonding variation across Boron Trihalides."),
            ("key", "LEWIS ACIDITY ORDER: **BF3 < BCl3 < BBr3 < BI3** (Opposite of halogen electronegativity!).\n"
                    "Reason: In BF3, strong 2p-2p back-bonding satisfies Boron's electron deficiency. In BI3, negligible back-bonding leaves Boron completely vacant and most hungry for external electron pairs."),
            ("h2", "2. Hydrolysis of Boron Trihalides"),
            ("bul", [
                "**BCl3, BBr3, BI3:** Undergo complete hydrolysis without secondary complexation:\n"
                "  BX3 + 3 H2O → H3BO3 + 3 HX (vigorous, fumes in moist air).",
                "**BF3 Anomaly (Partial Hydrolysis):**\n"
                "  Step 1: 4 BF3 + 3 H2O → B(OH)3 + 3 HBF4  (or: BF3 + 3 H2O → H3BO3 + 3 HF)\n"
                '  Step 2: HF immediately attacks unreacted BF3: 3 BF3 + 3 HF → **3 H^+^ [BF4]^-^** (Fluoroboric acid).\n'
                "  Net reaction: **4 BF3 + 3 H2O → H3BO3 + 3 H[BF4]** (does not go to completion to yield pure HF!).",
            ]),
            ("trap", "TRAP: BF3 does NOT give white fumes of HF on hydrolysis because HF reacts with BF3 to form HBF4! BCl3 fumes copiously because HCl gas does not coordinate to BCl3."),
        ],
    },
    # ------------------------------------------------------------------ G13-05
    {
        "id": "G13-05",
        "title": "Boric Acid H3BO3 & Borax Na2B4O7·10H2O",
        "blocks": [
            ("lead", "**Orthoboric Acid & Borax** — Layered Hydrogen Bonding & Aprotic Acidity"),
            ("p", "Orthoboric acid H3BO3 (or B(OH)3) is a white, slippery, crystalline solid with a layered sheet structure "
                  "held together by extensive planar hydrogen bonds. It acts as a mild antiseptic."),
            ("h2", "1. Nature of Acidity: Monobasic Lewis Acid"),
            ("p", 'H3BO3 is **NOT a protonic Bronsted acid** (does not lose its own H^+^). It acts as a **monobasic Lewis acid** '
                  'by accepting OH^-^ from water, thereby releasing H^+^ from the solvent:'),
            ("key", 'B(OH)3 + 2 H2O ⇌ [B(OH)4]^-^ + H3O^+^ (pK~a~ = 9.25, very weak)\n'
                    "It cannot be titrated directly against standard NaOH because the endpoint is diffuse."),
            ("h2", "2. Enhancement of Acidity by Polyhydroxy Compounds (cis-Diols)"),
            ("p", 'When cis-diols (glycerol, mannitol, catechol, or sorbitol) are added, the [B(OH)4]^-^ chelate forms a '
                  "very stable spirocyclic bis-chelate complex, shifting the equilibrium completely to the right:"),
            ("bul", [
                'Reaction: B(OH)3 + 2 C3H5(OH)3 ⇌ [B(C3H6O3)2]^-^ + H3O^+^ + 2 H2O.',
                "Result: Boric acid becomes a **strong monoprotic acid** and can be titrated sharply against NaOH using phenolphthalein indicator!",
                "Requirement: The diol must have **cis-vicinal -OH groups** (trans-diols do not enhance acidity).",
            ]),
            ("h2", "3. Thermal Action on Boric Acid"),
            ("p", "Stepwise dehydration on heating:\n"
                  'H3BO3 —(373 K, -H2O)→ **HBO2 (Metaboric acid)** —(433 K, -H2O)→ **H2B4O7 (Tetraboric acid)** —(red heat)→ **B2O3 (Boron sesquioxide / glassy mass)**.'),
            ("h2", "4. Borax (Na2B4O7·10H2O)"),
            ("p", "Correct structural formula: **Na2[B4O5(OH)4]·8H2O**. It contains 8 water molecules of crystallization."),
            ("fig", "borax", "Fig. 13.2 — Structure of the [B4O5(OH)4]2- anion in Borax."),
            ("bul", [
                "**Borax in Water:** Undergoes hydrolysis to give an alkaline buffer solution:\n"
                "  Na2B4O7 + 7 H2O → 2 NaOH + 4 H3BO3 (solution is alkaline, pH ≈ 9).",
            ]),
        ],
    },
    # ------------------------------------------------------------------ G13-06
    {
        "id": "G13-06",
        "title": "Borax Bead Test, Borate Minerals & Fluoboric Acid",
        "blocks": [
            ("lead", "**Borax Bead Test & Chemical Analysis** — Colored Metaborates & Fluoroborates"),
            ("p", "On heating in a platinum wire loop, borax swells up as water of crystallization is lost, and then "
                  "melts into a clear, transparent, glassy bead containing **NaBO2 + B2O3**."),
            ("h2", "1. Chemistry of the Borax Bead Test"),
            ("p", 'Na2B4O7·10H2O —(heat, -10 H2O)→ Na2B4O7 —(fuse)→ **2 NaBO2 (Sodium metaborate) + B2O3 (Boric anhydride)**\n'
                  "When heated with transition metal salts, B2O3 reacts with metal oxides to form characteristically coloured **metaborates M(BO2)2**:"),
            ("table", ["Metal Cation", "Oxidising Flame (Hot / Cold)", "Reducing Flame (Hot / Cold)", "Metaborate Formed"], [
                ['Cu^2+^', "Green (hot) / Blue (cold)", "Colorless (hot) / Opaque Red (cold, Cu metal)", "Cu(BO2)2 / Cu"],
                ['Co^2+^', "Deep Blue (hot & cold)", "Deep Blue (hot & cold)", "Co(BO2)2"],
                ['Cr^3+^', "Dark Yellow (hot) / Green (cold)", "Green (hot & cold)", "Cr(BO2)3"],
                ['Fe^3+^', "Yellowish-brown (cold)", "Bottle Green (cold)", "Fe(BO2)2 / Fe(BO2)3"],
                ['Ni^2+^', "Violet/Brown (hot) / Brown (cold)", "Grey (reduced Ni particles)", "Ni(BO2)2"],
            ], [15, 30, 30, 25], "Table 13.5 — Characteristic flame colours in Borax Bead Test."),
            ("h2", "2. Qualitative Test for Borate: Ethyl Borate Test"),
            ("p", "Borate salt + conc. H2SO4 + Ethanol → Heat → **Triethyl borate B(OC2H5)3** vapours burn with a "
                  "characteristic **green-edged flame**:\n"
                  'H3BO3 + 3 C2H5OH —(conc. H2SO4)→ B(OC2H5)3↑ + 3 H2O.'),
            ("h2", "3. Fluoroboric Acid (HBF4)"),
            ("bul", [
                "Preparation: B(OH)3 + 4 HF → H[BF4] + 3 H2O.",
                'Structure: [BF4]^-^ is perfectly tetrahedral (sp^3^, 4 equivalent B-F bonds of 143 pm).',
                'Properties: Strong acid, non-coordinating anion, used in Balz-Schiemann diazotisation (ArN2^+^ BF4^-^ → ArF + N2 + BF3).',
            ]),
        ],
    },
    # ------------------------------------------------------------------ G13-07
    {
        "id": "G13-07",
        "title": "Boron Nitride (Inorganic Graphite) & B-N vs C-C",
        "blocks": [
            ("lead", '**Boron Nitride (BN)~x~** — Synthesis, Allotropes & Comparison with Carbon'),
            ("p", 'Boron Nitride is iso-electronic with Carbon (B + N = 3 + 5 = 8 e^-^ = 2 × C). '
                  "It exists in two major crystalline forms: Hexagonal BN (h-BN, inorganic graphite) and Cubic BN (c-BN, borazon, inorganic diamond)."),
            ("h2", "1. Hexagonal Boron Nitride (h-BN: 'Inorganic Graphite')"),
            ("bul", [
                '**Synthesis:** B2O3 + 2 NH3 —(1200 K)→ 2 BN + 3 H2O (or: BCl3 + NH3 → BN + 3 HCl at 1000°C).',
                "**Structure:** Planar hexagonal rings of alternating B and N atoms (B-N bond length 145 pm).",
                "**Layer Stacking Difference:** In graphite, layers are stacked in an ABAB pattern with atoms displaced. In h-BN, layers are stacked directly **AA'AA'** with B atoms directly over N atoms in adjacent layers (dipole-dipole attraction B^δ+...N^δ-).",
                "**Electrical Conductivity:** Graphite is a good conductor (delocalised π electrons). h-BN is a **white insulator** (wide bandgap ≈ 5.9 eV) because π electrons are tightly held by electronegative Nitrogen atoms!",
            ]),
            ("table", ["Feature", "Graphite (Carbon)", "Hexagonal Boron Nitride (h-BN)"], [
                ["Color & Appearance", "Grey-black, metallic luster", "Pure white solid ('White Graphite')"],
                ["Layer Stacking", "ABAB... (staggered rings)", "AA'AA'... (B above N eclipsed)"],
                ["Electrical Conduction", "Conductor along planes (semimetal)", "Electrical Insulator (wide bandgap)"],
                ["Chemical Resistance", "Oxidises at 700°C", "Resistant to oxidation up to 1000°C, inert to acids"],
            ], [22, 38, 40], "Table 13.6 — Direct structural comparison between Graphite and h-BN."),
            ("h2", "2. Cubic Boron Nitride (c-BN: 'Borazon')"),
            ("p", "Formed by heating h-BN under extreme pressure (60,000 atm, 1800°C). It has a zinc-blende (diamond-like) "
                  "three-dimensional tetrahedral network. It is second only to diamond in hardness, but has higher thermal "
                  "stability in air and does not react with ferrous metals during high-speed cutting."),
        ],
    },
    # ------------------------------------------------------------------ G13-08
    {
        "id": "G13-08",
        "title": "Aluminium Chemistry, Al2Cl6, Alums & Industrial Uses",
        "blocks": [
            ("lead", "**Aluminium Chemistry** — Halide Dimers, Alums, Passivation & Thermite"),
            ("p", "Aluminium is the most abundant metal in the Earth's crust (8.3% by mass). Key ore is **Bauxite AlOx(OH)3-2x** "
                  "purified by Bayer's process and reduced by the Hall-Héroult electrolytic process."),
            ("h2", "1. Aluminium Chloride (AlCl3 vs Al2Cl6)"),
            ("bul", [
                "**Anhydrous AlCl3:** White crystalline solid, highly hygroscopic. Prepared by: 2 Al + 3 Cl2 → 2 AlCl3 (or: Al2O3 + 3 C + 3 Cl2 → 2 AlCl3 + 3 CO).",
                '**Dimerisation in Vapor/Non-polar solvents:** AlCl3 dimerises to **Al2Cl6** through two bridging dative bonds (Cl: → Al). Each Al is sp^3^ hybridized with an octet.',
                '**High Temperature Dissociation:** At T > 1000 K, Al2Cl6 dissociates into planar monomeric **AlCl3** (sp^2^, Lewis acid).',
                '**In Water:** Al2Cl6 dissolves exothermically and ionizes: Al2Cl6 + 12 H2O → 2 [Al(H2O)6]^3+^ + 6 Cl^-^ (octahedral complex, acidic pH due to hydrolysis).',
            ]),
            ("key", "AlCl3 cannot be prepared anhydrous by heating AlCl3·6H2O! On heating, it undergoes hydrolysis:\n"
                    '2 AlCl3·6H2O —(heat)→ Al2O3 + 6 HCl + 9 H2O.'),
            ("h2", "2. Alums: General Formula M2SO4·M'2(SO4)3·24H2O"),
            ("p", 'Where M = univalent cation (K^+^, Na^+^, NH4^+^, Rb^+^, Cs^+^; NOT Li^+^ due to small size) and '
                  "M' = trivalent cation (Al^3+^, Cr^3+^, Fe^3+^, Co^3+^).\n"
                  "Structural formula: **[M(H2O)6]^+^ [M'(H2O)6]^3+^ (SO4^2-^)2**."),
            ("table", ["Common Alum", "Formula", "Primary Uses"], [
                ["Potash Alum", "K2SO4·Al2(SO4)3·24H2O", "Water purification (coagulation of colloidal clay), mordant in dyeing"],
                ["Ammonium Alum", "(NH4)2SO4·Al2(SO4)3·24H2O", "Baking powder, water treatment, fire-retardant textiles"],
                ["Chrome Alum", "K2SO4·Cr2(SO4)3·24H2O", "Leather tanning (cross-links collagen proteins)"],
                ["Ferric Alum", "(NH4)2SO4·Fe2(SO4)3·24H2O", "Indicator in Volhard's titration of halides"],
            ], [20, 42, 38], "Table 13.7 — Composition and applications of Alums in JEE."),
            ("h2", "3. Passivation & Goldschmidt Thermite Process"),
            ("bul", [
                "**Passivation:** Conc. HNO3 makes Al passive by forming a dense, insoluble, protective oxide film of Al2O3. Hence, conc. HNO3 can be transported in Al containers.",
                "**Thermite Reaction:** Fe2O3 + 2 Al → Al2O3 + 2 Fe(l)  (ΔH = -850 kJ/mol, T ≈ 3000°C, used for on-site welding of railway tracks).",
            ]),
        ],
    },
]
