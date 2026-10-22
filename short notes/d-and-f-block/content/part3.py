"""Part 3: Sheets DF-13 to DF-18 — KMnO4, Lanthanoids, Actinoids, Ag/Cu/Zn/Fe & JEE Bank."""
from __future__ import annotations

SHEETS = [
    # ------------------------------------------------------------------ DF-13
    {
        "id": "DF-13",
        "title": "Potassium Permanganate: Synthesis, Tetrahedral Geometry & Disproportionation",
        "blocks": [
            ("lead", "**Manufacture from Pyrolusite Ore & Structural Properties** (NCERT §8.4)"),
            ("p", "Potassium permanganate (KMnO~4~) is the most widely utilized transition metal oxidizing agent in analytical and synthetic chemistry, manufactured from pyrolusite ore (MnO~2~)."),
            ("fig", "permanganate_manganate", "Fig. 13.1 — Tetrahedral structures of manganate (green, paramag.) and permanganate (purple, diamag.)."),
            ("h2", "1. Two-Step Industrial Manufacture"),
            ("bul", [
                "**Step 1: Oxidative Alkaline Fusion of Pyrolusite:**",
                "  Finely powdered MnO~2~ is fused with KOH (or K~2~CO~3~) in presence of atmospheric air or an oxidizing agent like KNO~3~ or KClO~3~:",
                '  2 MnO~2~ + 4 KOH + O~2~ → 2 K~2~MnO~4~ (dark green) + 2 H~2~O',
                "  Dark green potassium manganate (K~2~MnO~4~) is formed.",
                "**Step 2: Oxidation of Manganate to Permanganate:**",
                '  - **Commercial Electrolytic Route:** Alkaline manganate solution is electrolyzed between iron electrodes. At anode: MnO~4~^2−^ → MnO~4~^-^ + e^-^ (oxidation to purple permanganate).',
                "  - **Laboratory Chemical Route (Disproportionation):** Green manganate is acidified or bubbled with CO~2~ or Cl~2~:",
                '    3 MnO~4~^2−^ (green) + 4 H^+^ → 2 MnO~4~^-^ (purple) + MnO~2~↓ (brown) + 2 H~2~O',
                '    2 K~2~MnO~4~ + Cl~2~ → 2 KMnO~4~ + 2 KCl'
            ]),
            ("h2", "2. Structural, Magnetic & Optical Comparison"),
            ("table", ["Property", "Potassium Manganate (K~2~MnO~4~)", "Potassium Permanganate (KMnO~4~)"], [
                ["**Oxidation State of Mn**", '+6 (3d^1^ configuration)', '+7 (3d^0^ configuration)'],
                ["**Geometry & Hybridization**", 'Tetrahedral (d^3^s or sp^3^ with pπ-dπ bonding)', 'Tetrahedral (d^3^s or sp^3^ with pπ-dπ bonding)'],
                ["**Magnetic Property**", '**Paramagnetic** (1 unpaired electron, μ = 1.73 BM)', "**Diamagnetic** (0 unpaired electrons)"],
                ["**Colour & Spectroscopy**", "**Dark Green** (d-d transition + LMCT)", '**Intense Deep Purple** (pure LMCT: O^2−^ → Mn^7+^)'],
                ["**Solution Stability**", "Stable ONLY in strongly alkaline solution (pH > 12)", "Stable in neutral/dilute acid; decomposes slowly in light"]
            ], [22, 39, 39], "Table 13.1 — Comparative properties of manganate and permanganate."),
            ("trap", 'CRITICAL TRAP: KMnO~4~ has ZERO unpaired d-electrons (d^0^), yet it is intensely purple! Never claim its color is due to d-d transition; it is strictly caused by Ligand-to-Metal Charge Transfer (LMCT)!')
        ]
    },

    # ------------------------------------------------------------------ DF-14
    {
        "id": "DF-14",
        "title": "Potassium Permanganate: Medium-Dependent Redox Spectrum & Titrations",
        "blocks": [
            ("lead", "**Volumetric Equivalent Weights Across Three Media** (NCERT §8.4)"),
            ("p", "The oxidizing power and equivalent weight of KMnO~4~ vary dramatically depending upon the pH of the reaction medium, transferring 5, 3, or 1 electron."),
            ("h2", "1. The Three Half-Reactions & Equivalent Weights"),
            ("bul", [
                "**1. Acidic Medium (dilute H~2~SO~4~):** Mn(+7) is reduced by **5 electrons** to Mn^2+^ (+2):",
                '  MnO~4~^-^ + 8 H^+^ + 5 e^-^ → Mn^2+^ (faint pink) + 4 H~2~O (E° = +1.51 V)',
                '  **Equivalent Weight** = (Molar Mass) / 5 = 158.04 / 5 = **31.61 g/eq**.',
                "**2. Neutral or Faintly Alkaline Medium (Baeyer's Condition):** Mn(+7) is reduced by **3 electrons** to brown insoluble MnO~2~ (+4):",
                '  MnO~4~^-^ + 2 H~2~O + 3 e^-^ → MnO~2~↓ (brown) + 4 OH^-^ (E° = +1.23 V)',
                '  **Equivalent Weight** = (Molar Mass) / 3 = 158.04 / 3 = **52.68 g/eq**.',
                "**3. Strongly Alkaline Medium:** Mn(+7) is reduced by **1 electron** to green manganate MnO~4~^2−^ (+6):",
                '  MnO~4~^-^ + e^-^ → MnO~4~^2−^ (green) (E° = +0.56 V)',
                '  **Equivalent Weight** = (Molar Mass) / 1 = **158.04 g/eq**.'
            ]),
            ("h2", "2. Quantitative Acidic Redox Reactions"),
            ("table", ["Reducing Agent", "Oxidized Product", "Ionic Equation", "Special Feature"], [
                ["**Oxalate (C~2~O~4~^2−^)**", "CO~2~ gas", '2 MnO~4~^-^ + 16 H^+^ + 5 C~2~O~4~^2−^ → 2 Mn^2+^ + 10 CO~2~↑ + 8 H~2~O', "Autocatalyzed by product Mn^2+^ ions!"],
                ["**Fe^2+^ (Mohr's Salt)**", "Fe^3+^ (Ferric)", 'MnO~4~^-^ + 8 H^+^ + 5 Fe^2+^ → Mn^2+^ + 5 Fe^3+^ + 4 H~2~O', "KMnO~4~ acts as self-indicator"],
                ["**I^−^ (Iodide)**", "I~2~ (Iodine)", '2 MnO~4~^-^ + 16 H^+^ + 10 I^-^ → 2 Mn^2+^ + 5 I~2~ + 8 H~2~O', "Forms brown iodine solution"],
                ["**H~2~S**", "S (Colloidal sulfur)", '2 MnO~4~^-^ + 6 H^+^ + 5 H~2~S → 2 Mn^2+^ + 5 S↓ + 8 H~2~O', "Turbid white colloidal sulfur"],
                ["**NO~2~^−^ (Nitrite)**", "NO~3~^−^ (Nitrate)", '2 MnO~4~^-^ + 6 H^+^ + 5 NO~2~^-^ → 2 Mn^2+^ + 5 NO~3~^-^ + 3 H~2~O', "Colorless nitrate solution"]
            ], [18, 16, 44, 22], "Table 14.1 — Standard acidic redox titrations using KMnO~4~."),
            ("h2", "3. Neutral / Faintly Alkaline Traps (JEE Advanced Core)"),
            ("bul", [
                "**Oxidation of Iodide to IODATE (Crucial Contrast!):**",
                "  In acidic medium, I^−^ gives I~2~. In neutral/faintly alkaline medium, I^−^ is oxidized to **Iodate ([IO~3~]^−^)**:",
                '  2 MnO~4~^-^ + H~2~O + I^-^ → 2 MnO~2~↓ + IO~3~^-^ + 2 OH^-^',
                "**Oxidation of Thiosulfate to SULFATE:**",
                '  8 MnO~4~^-^ + 3 S~2~O~3~^2−^ + H~2~O → 8 MnO~2~↓ + 6 SO~4~^2−^ + 2 OH^-^',
                '**Why HCl cannot be used to acidify KMnO~4~?** KMnO~4~ (E° = +1.51 V) oxidizes HCl (E° = +1.36 V) to toxic Cl~2~ gas: 2 MnO~4~^-^ + 16 HCl → 2 Mn^2+^ + 5 Cl~2~↑ + 8 H~2~O. Dilute H~2~SO~4~ must be used!'
            ]),
            ("trap", "SELF-INDICATOR ACTION: KMnO~4~ acts as its own indicator in titrations. A single excess drop imparts a permanent, unmistakable pale pink color to the solution at the equivalence point!")
        ]
    },

    # ------------------------------------------------------------------ DF-15
    {
        "id": "DF-15",
        "title": "The Lanthanoids (4f Series): Chemistry, Contraction & Mischmetal",
        "blocks": [
            ("lead", "**Inner Transition Series (4f Orbital Filling)** (NCERT §8.5)"),
            ("p", "The 14 lanthanoids span from **Cerium (Ce 58) to Lutetium (Lu 71)** following Lanthanum (La 57). They are characterized by the progressive filling of 4f inner orbitals shielded by outer 5s, 5p, and 6s subshells."),
            ("h2", "1. Electronic Configurations & Dominant Oxidation States"),
            ("bul", [
                "**General Valence Configuration:** **[Xe] 4f^1-14^ 5d^0-1^ 6s^2^**.",
                "  - 5d orbital has 1 electron only in **La ([Xe] 5d^1^ 6s^2^), Ce ([Xe] 4f^1^ 5d^1^ 6s^2^), Gd ([Xe] 4f^7^ 5d^1^ 6s^2^), and Lu ([Xe] 4f^14^ 5d^1^ 6s^2^)**.",
                "  - In all other lanthanoids, 5d electron is shifted into 4f subshell.",
                "**The Supreme Dominance of +3 State:** All lanthanoids exhibit **+3** as their principal, most stable oxidation state in aqueous solution and solid compounds.",
                "**Exceptions (+2 and +4 States):**",
                '  - **Ce^4+^ (+4):** Attains empty noble gas **4f^0^** configuration. Exceptionally powerful oxidant (E° = +1.74 V), used in volumetric cerimetry.',
                "  - **Tb^4+^ (+4):** Attains stable half-filled **4f^7^** configuration. Strong oxidant.",
                '  - **Eu^2+^ (+2):** Attains stable half-filled **4f^7^** configuration ([Xe] 4f^7^). Strong reducing agent (E°(Eu^3+^/Eu^2+^) = -0.43 V).',
                "  - **Yb^2+^ (+2):** Attains completely filled **4f^14^** configuration. Strong reducing agent."
            ]),
            ("h2", "2. Lanthanoid Contraction: Causes & Consequences"),
            ("p", "Steady decrease in atomic and ionic radii from Ce^3+^ (103 pm) to Lu^3+^ (86 pm) due to poor shielding of diffuse 4f electrons."),
            ("table", ["Consequence", "Underlying Chemical / Physical Cause", "Practical Observation / Impact"], [
                ["**Basic Strength of Hydroxides**", "Smaller ionic size increases covalent character (Fajans)", "**Ce(OH)~3~ is most basic, Lu(OH)~3~ is least basic**"],
                ["**Separation Difficulty**", "Nearly identical chemical properties and ionic sizes", "Requires fractional crystallization or ion-exchange chromatography"],
                ["**4d/5d Twin Pairs**", "Cancels normal group radius expansion", "Zr/Hf, Nb/Ta, Mo/W have identical sizes and co-occur in nature"]
            ], [26, 36, 38], "Table 15.1 — Major consequences of Lanthanoid Contraction."),
            ("h2", "3. Chemical Reactivity, Sharp Spectra & Mischmetal"),
            ("bul", [
                "**Reactivity:** Electropositive metals, resembling Calcium: react with water yielding H~2~, burn in O~2~ forming Ln~2~O~3~, react with halogens forming LnX~3~.",
                "**Sharp f-f Absorption Bands:** 4f electrons are deeply buried inside the atom and shielded by 5s^2^ 5p^6^ electrons → crystal fields cannot broaden orbital levels → absorption spectra consist of **extremely sharp lines** (used in Nd:YAG laser rods).",
                '**Mischmetal:** Alloy consisting of ≈95% Lanthanoid metals (Ce ≈50%, La ≈40%), ≈5% Fe, and traces of S, C, Ca. Used in cigarette lighter flints and tracer bullets.'
            ]),
            ("trap", "RADIOACTIVITY CHECK: Among all 14 lanthanoids, **ONLY Promethium (Pm 61)** is radioactive and synthetic; all other 13 lanthanoids are non-radioactive stable elements!")
        ]
    },

    # ------------------------------------------------------------------ DF-16
    {
        "id": "DF-16",
        "title": "The Actinoids (5f Series) & Lanthanoid vs Actinoid Comparison",
        "blocks": [
            ("lead", "**Inner Transition Series (5f Orbital Filling)** (NCERT §8.6)"),
            ("p", "The 14 actinoids span from **Thorium (Th 90) to Lawrencium (Lr 103)** following Actinium (Ac 89). They involve the progressive population of 5f subshell."),
            ("fig", "lanthanoid_actinoid_comparison", "Fig. 16.1 — Comparative properties: 4f Lanthanoids vs 5f Actinoids."),
            ("h2", "1. Electronic Configuration & Multiple Oxidation States"),
            ("bul", [
                "**General Valence Configuration:** **[Rn] 5f^1-14^ 6d^0-2^ 7s^2^**.",
                "**Wide Spectrum of Oxidation States:** Unlike lanthanoids (dominated by +3), early actinoids exhibit multiple oxidation states: **Th (+4), Pa (+5), U (+3, +4, +5, +6), Np (+3, +4, +5, +6, +7), Pu (+3, +4, +5, +6, +7)**.",
                "**Physical Reason:** In actinoids, **5f, 6d, and 7s energy levels are extremely close in energy** (very small energy gap), allowing all outer electrons to participate in chemical bonding!"
            ]),
            ("h2", "2. Actinoid Contraction vs Lanthanoid Contraction"),
            ("bul", [
                "**Actinoid Contraction:** Progressive decrease in size of atoms and M^3+^/M^4+^ ions across the series.",
                "**Comparison:** **Actinoid contraction from element to element is GREATER than lanthanoid contraction!**",
                '**Physical Cause:** 5f orbitals extend further from the nucleus than 4f orbitals, resulting in **even poorer shielding** of nuclear charge. Consequently, effective nuclear charge (Z~eff~) increases more steeply across the actinoid series.'
            ]),
            ("h2", "3. Rigorous Comparison: Lanthanoids vs Actinoids"),
            ("table", ["Feature", "Lanthanoids (4f Series)", "Actinoids (5f Series)"], [
                ["**Oxidation States**", "Predominantly **+3** (rarely +2, +4)", "**Multiple states: +3, +4, +5, +6, +7**"],
                ["**Energy Gap**", "Large gap between 4f, 5d, and 6s orbitals", "Very small gap between 5f, 6d, and 7s orbitals"],
                ["**Complexing Ability**", "Low tendency (4f orbitals deeply buried)", "**High tendency** (5f orbitals extend spatially)"],
                ["**Oxocations**", "Do NOT form oxocations", "Readily form stable oxocations: **[UO~2~]^2+^, [PuO~2~]^2+^**"],
                ["**Basic Strength**", "Hydroxides are less basic", "Hydroxides are more basic"],
                ["**Radioactivity**", "Only Promethium (Pm) is radioactive", "**ALL actinoids are intensely radioactive!**"]
            ], [22, 39, 39], "Table 16.1 — Comprehensive Lanthanoid vs Actinoid comparison."),
            ("trap", "TRANSURANIC ELEMENTS: Elements beyond Uranium (Z > 92, from Neptunium onwards) are completely synthetic, man-made transuranic elements produced in nuclear reactors!")
        ]
    },

    # ------------------------------------------------------------------ DF-17
    {
        "id": "DF-17",
        "title": "Key Compounds of d-Block Metals: Silver, Copper & Zinc Chemistry",
        "blocks": [
            ("lead", "**Industrial Compounds & Analytical Chemistry of Ag, Cu, and Zn**"),
            ("p", "The chemistry of late 3d and 4d metals involves distinctive precipitation, complexation, and redox reactions central to qualitative analysis and industrial technology."),
            ("h2", "1. Silver Chemistry: AgNO~3~ & Silver Halides"),
            ("bul", [
                '**Silver Nitrate (AgNO~3~, Lunar Caustic):** Prepared by dissolving pure Ag in dilute HNO~3~: 3 Ag + 4 HNO~3~ → 3 AgNO~3~ + NO↑ + 2 H~2~O.',
                '  - **Thermal Decomposition:** 2 AgNO~3~ —(Δ)→ 2 Ag + 2 NO~2~↑ + O~2~↑ (decomposes directly to metallic silver).',
                "  - **Caustic Stain:** On skin/organic matter, produces a permanent black metallic silver stain.",
                "**Silver Halides Ammonia & Hypo Solubility:**",
                '  - **AgCl (White curdy ppt):** Soluble in dilute aqueous NH~3~: AgCl + 2 NH~3~ → [Ag(NH~3~)~2~]^+^ + Cl^-^.',
                '  - **AgBr (Pale yellow ppt):** Sparingly soluble in dilute NH~3~, soluble in concentrated NH~3~; dissolves in hypo: AgBr + 2 Na~2~S~2~O~3~ → Na~3~[Ag(S~2~O~3~)~2~] + NaBr (photographic fixing).',
                "  - **AgI (Bright yellow ppt):** Insoluble in both dilute and concentrated NH~3~; soluble only in KCN or hypo."
            ]),
            ("h2", "2. Copper Chemistry: Blue Vitriol & Cuprous Compounds"),
            ("bul", [
                "**Copper Sulfate Pentahydrate (CuSO~4~·5H~2~O, Blue Vitriol):**",
                '  - **Structural Insight:** Four water molecules coordinate to Cu^2+^ in a square plane ([Cu(H~2~O)~4~]^2+^), while the fifth water molecule is held by **hydrogen bonds** between coordinated waters and sulfate: [Cu(H~2~O)~4~]SO~4~· H~2~O!',
                "  - **Thermal Dehydration:**",
                '    CuSO~4~· 5H~2~O —(100° C)→ CuSO~4~· H~2~O —(250° C)→ CuSO~4~ (white) —(750° C)→ CuO + SO~3~',
                "**Reaction with KI (Iodometric Titration Foundation):**",
                '  2 CuSO~4~ + 4 KI → 2 CuI↓ (white) + I~2~ + 2 K~2~SO~4~',
                "  Liberated iodine is titrated against standard hypo solution using starch indicator."
            ]),
            ("h2", "3. Zinc Chemistry: Amphoterism & Lithopone"),
            ("bul", [
                "**Amphoteric Nature:** Zn, ZnO, and Zn(OH)~2~ react with both acids and strong bases:",
                '  Zn + 2 NaOH → Na~2~ZnO~2~ (sodium zincate) + H~2~↑',
                '  ZnO + 2 NaOH + H~2~O → Na~2~[Zn(OH)~4~]',
                "**Zinc Vitriol (ZnSO~4~·7H~2~O, White Vitriol):** Isomorphous with Epsom salt (MgSO~4~·7H~2~O).",
                '**Lithopone:** Equimolar mixture of **BaSO~4~ + ZnS**, prepared by precipitation: BaS + ZnSO~4~ → BaSO~4~↓ + ZnS↓. Non-poisonous white paint pigment (does not blacken in H~2~S atmosphere!).'
            ]),
            ("trap", 'EXAM TRAP: CuCl~2~ is green in concentrated solution, turns sky-blue upon dilution due to transformation of [CuCl~4~]^2−^ (yellow/green) into [Cu(H~2~O)~6~]^2+^ (blue)!')
        ]
    },

    # ------------------------------------------------------------------ DF-18
    {
        "id": "DF-18",
        "title": "Key Compounds of Iron & JEE Advanced Reasoning Bank",
        "blocks": [
            ("lead", "**Iron Complexes, Brown Ring Test & High-Yield Exam Traps**"),
            ("p", "Iron exhibits intricate coordination and redox chemistry, providing foundation tests in qualitative inorganic analysis."),
            ("h2", "1. Mohr's Salt, Green Vitriol & Prussian Blue"),
            ("bul", [
                "**Mohr's Salt (Ferrous Ammonium Sulfate):** **FeSO~4~·(NH~4~)~2~SO~4~·6H~2~O**.",
                "  - Primary volumetric standard for Fe^2+^ because it is **resistant to atmospheric oxidation** in solid form (unlike FeSO~4~·7H~2~O which rapidly oxidizes to basic ferric sulfate).",
                "**Green Vitriol (FeSO~4~·7H~2~O):**",
                '  - Thermal Decomposition: 2 FeSO~4~· 7H~2~O —(Δ)→ Fe~2~O~3~ (red-brown) + SO~2~↑ + SO~3~↑ + 14 H~2~O.',
                "**Prussian Blue & Turnbull's Blue Identity:**",
                '  - Fe^3+^ + potassium ferrocyanide → **Prussian Blue**: Fe^3+^ + [Fe(CN)~6~]^4−^ → KFe^III^[Fe^II^(CN)~6~].',
                "  - Fe^2+^ + potassium ferricyanide → **Turnbull's Blue**: Fe^2+^ + [Fe(CN)~6~]^3−^ → KFe^III^[Fe^II^(CN)~6~].",
                "  - **Modern Spectroscopic Truth:** Both are chemically IDENTICAL: **iron(III) hexacyanoferrate(II)**! The intense deep blue color arises from **inter-valence charge transfer (IVCT)** between Fe^2+^ and Fe^3+^."
            ]),
            ("h2", "2. The Brown Ring Nitrate Complex"),
            ("p", "Formed at the interface in the brown ring test for nitrate:\n"
                  "• **Formula:** **[Fe(H~2~O)~5~(NO)]SO~4~**.\n"
                  '• **Electronic Nature:** Electron transfer from NO to Fe^3+^ establishes an equilibrium between Fe(+1)-NO^+^ and Fe(+3)-NO^−^ with **3 unpaired electrons** (μ~eff~ ≈ 3.87 BM).\n'
                  "• **Colour Origin:** Intense brown color is due to **charge transfer** between iron and nitrosyl ligand."),
            ("h2", "3. JEE Advanced Master Reasoning Bank"),
            ("table", ["Exam Question", "Fundamental Chemical Principle", "Precise Exam Justification"], [
                ["**Why is Sc^3+^ colourless while Ti^3+^ is purple?**", "d-d electronic excitation", "Sc^3+^ is [Ar] 3d^0^ (no d-electrons). Ti^3+^ is 3d^1^; visible photon excites electron from t~2g~ to e~g~."],
                ["**Why is atomization enthalpy of Zn lowest in 3d?**", "Metallic lattice cohesion", "Zn has completely filled 3d^10^ 4s^2^; no unpaired d-electrons participate in covalent d-d overlap."],
                ["**Why is Cr^2+^ reducing while Mn^3+^ is oxidizing?**", "Electronic shell stability", "Cr^2+^ oxidizes to Cr^3+^ (stable half-filled t~2g~^3^ CFSE). Mn^3+^ reduces to Mn^2+^ (stable 3d^5^ exchange energy)."],
                ["**Why does Cu^+^ disproportionate in water?**", "Hydration vs Ionization balance", 'Cu^2+^ has high charge density, giving massive negative hydration enthalpy (Δ~hyd~ H° = −2121 kJ/mol) overcoming IE~2~.']
            ], [28, 28, 44], "Table 18.1 — Essential JEE Advanced reasoning traps and authoritative explanations."),
            ("trap", "EXAM TRAP: Sodium nitroprusside Na~2~[Fe(CN)~5~(NO)] reacts with sulfide ion (S^2−^) to give an intense purple/violet coloration of [Fe(CN)~5~(NOS)]^4−^ — classic confirmatory test for sulfide!")
        ]
    }
]
