"""Sheets 10 to 18 for d- and f-Block Elements."""

SHEETS_PART2 = [
    {
        "id": "sheet_10",
        "num": 10,
        "title": "Sheet 10 — Complex Formation, Catalysis, Interstitials & Alloys",
        "badge": "Properties & Materials",
        "boxes": [
            {
                "title": "1. High Propensity for Complex Formation",
                "tag": "Coordination Driver",
                "accent": "teal",
                "bullets": [
                    "• Transition metals form an immense variety of coordination complexes (e.g. [Fe(CN)~6~]^4−^, [Cu(NH~3~)~4~]^2+^, [PtCl~4~]^2−^).",
                    "• **Four Governing Reasons:**",
                    "  1. **Small Ionic Size & High Nuclear Charge:** Resulting in very high charge-to-radius ratio (high charge density).",
                    "  2. **Availability of Vacant Low-Energy (n−1)d, ns, and np Orbitals:** Readily accept lone pairs donated by ligands.",
                    "  3. **Variable Oxidation States:** Provide electronic flexibility to stabilize varied coordination geometries.",
                    "  4. **CFSE Gain:** Crystal field stabilization energy stabilizes particular ligand-metal geometries."
                ]
            },
            {
                "title": "2. Catalytic Properties & Mechanisms",
                "tag": "Industrial Catalysis",
                "accent": "navy",
                "bullets": [
                    "• **Two Complementary Mechanisms:**",
                    '  1. **Variable Valency (Homogeneous Catalysis):** Transition metals cycle between oxidation states, lowering activation energy. E.g. Oxidation of iodide by persulfate catalyzed by Fe^3+^: (Step 1) 2 Fe^3+^ + 2 I^-^ → 2 Fe^2+^ + I~2~; (Step 2) 2 Fe^2+^ + S~2~O~8~^2−^ → 2 Fe^3+^ + 2 SO~4~^2−^.',
                    "  2. **Adsorption & Active Surface (Heterogeneous Catalysis):** Utilizing vacant d orbitals to form weak chemisorption bonds with reactant molecules, increasing local concentration and weakening covalent bonds.",
                    "• **Industrial Heavyweights:** Fe in Haber's Process (NH~3~); V~2~O~5~ in Contact Process (SO~2~ to SO~3~); Finely divided Ni in hydrogenation of oils; TiCl~4~ + Al(C~2~H~5~)~3~ (Ziegler-Natta Catalyst) in ethene polymerization."
                ]
            },
            {
                "title": "3. Interstitial Compounds & Alloy Formation",
                "tag": "Materials Science",
                "accent": "gold",
                "bullets": [
                    "• **Interstitial Compounds:** Formed when small non-metal atoms (H, C, N, B) get trapped inside interstitial voids of transition metal crystal lattices. E.g. TiC, Mn~4~N, Fe~3~H, VH~0.56~.",
                    "  - Non-stoichiometric; neither purely ionic nor covalent.",
                    "  - **Key Characteristics:** Very high melting points (higher than pure metals); extremely hard (TiC approaches diamond hardness); retain metallic electrical conductivity; chemically inert.",
                    "• **Alloy Formation:** Transition metals have very similar atomic radii (within 15% of each other, satisfying Hume-Rothery rules) → atoms of one metal readily replace atoms of another in the crystal lattice.",
                    "  - E.g. **Brass** (Cu 60-80% + Zn 20-40%), **Bronze** (Cu 80% + Sn 20%), **Stainless Steel** (Fe + Cr 18% + Ni 8% + C)."
                ]
            }
        ]
    },
    {
        "id": "sheet_11",
        "num": 11,
        "title": "Sheet 11 — Potassium Dichromate — Manufacture & Structural Equilibrium",
        "badge": "K2Cr2O7 Chemistry",
        "figure": "chromate_dichromate",
        "boxes": [
            {
                "title": "1. Industrial Manufacture of K~2~Cr~2~O~7~ from Chromite Ore",
                "tag": "Three-Step Synthesis",
                "accent": "teal",
                "bullets": [
                    "• **Step 1: Oxidative Roasting with Soda Ash (Chromate Formation):**",
                    "  Chromite ore (ferrochrome, FeCr~2~O~4~ or FeO·Cr~2~O~3~) is fused with sodium carbonate in excess air in a reverberatory furnace:",
                    '  4 FeCr~2~O~4~ + 8 Na~2~CO~3~ + 7 O~2~ → 8 Na~2~CrO~4~ (yellow) + 2 Fe~2~O~3~ (brown↓) + 8 CO~2~',
                    "  The roasted mass is extracted with water; yellow sodium chromate dissolves while Fe~2~O~3~ remains as an insoluble residue.",
                    "• **Step 2: Acidification to Dichromate:**",
                    "  Yellow Na~2~CrO~4~ solution is filtered and acidified with concentrated H~2~SO~4~:",
                    '  2 Na~2~CrO~4~ + H~2~SO~4~ → Na~2~Cr~2~O~7~ (orange) + Na~2~SO~4~↓ + H~2~O',
                    "  Less soluble Na~2~SO~4~ crystallizes out first (as Glauber's salt) and is removed.",
                    "• **Step 3: Conversion to Potassium Dichromate (Fractional Crystallization):**",
                    "  Sodium dichromate is treated with KCl:",
                    '  Na~2~Cr~2~O~7~ + 2 KCl → K~2~Cr~2~O~7~ (orange↓) + 2 NaCl',
                    "  **Why K~2~Cr~2~O~7~ instead of Na~2~Cr~2~O~7~ in titrations?** K~2~Cr~2~O~7~ is moderately soluble in cold water and **non-hygroscopic** (pure primary standard). Na~2~Cr~2~O~7~ is deliquescent (absorbs moisture from air), making accurate weighing impossible!"
                ]
            },
            {
                "title": "2. The Chromate-Dichromate pH Equilibrium",
                "tag": "Structural Reversibility",
                "accent": "navy",
                "bullets": [
                    "• **Dynamic Reversible Switch:**",
                    '  2 CrO~4~^2−^ (yellow) + 2 H^+^ ⇌ Cr~2~O~7~^2−^ (orange) + H~2~O',
                    "  - In **acidic medium (pH < 7)**, equilibrium shifts right → **Orange Cr~2~O~7~^2−^** dominates.",
                    "  - In **basic medium (pH > 7)**, adding OH^−^ removes H^+^ → equilibrium shifts left → **Yellow CrO~4~^2−^** dominates.",
                    "• **Oxidation State Constant:** Chromium remains in the **+6** oxidation state in both ions! This is an acid-base condensation reaction, **NOT a redox process**.",
                    "• **Structural Parameters:**",
                    "  - **Chromate ([CrO~4~]^2−^):** Tetrahedral; all four Cr-O bond lengths are identical (166 pm) due to resonance.",
                    "  - **Dichromate ([Cr~2~O~7~]^2−^):** Consists of two tetrahedra sharing one oxygen corner. Cr-O-Cr bond angle is **126°**. The bridging Cr-O bonds are longer (**179 pm**), while six terminal Cr-O bonds are shorter (**163 pm**)."
                ]
            }
        ]
    },
    {
        "id": "sheet_12",
        "num": 12,
        "title": "Sheet 12 — Potassium Dichromate — Oxidizing Reactions & Chromyl Chloride Test",
        "badge": "Redox & Tests",
        "boxes": [
            {
                "title": "1. Oxidizing Action of K~2~Cr~2~O~7~ in Acidic Medium",
                "tag": "Equivalent Weight = M/6",
                "accent": "teal",
                "bullets": [
                    "• **Fundamental Redox Half-Reaction:** In acidic solution (dil H~2~SO~4~), dichromate acts as a powerful oxidant, being reduced to green Cr^3+^:",
                    '  Cr~2~O~7~^2−^ + 14 H^+^ + 6 e^-^ → 2 Cr^3+^ (green) + 7 H~2~O (E° = +1.33 V)',
                    '• **Equivalent Weight:** E = (Molar Mass) / 6 = 294.18 / 6 = 49.03 g/eq.',
                    "• **Major Quantitative Reactions:**",
                    '  1. **Oxidation of Fe^2+^ to Fe^3+^:** Cr~2~O~7~^2−^ + 14 H^+^ + 6 Fe^2+^ → 2 Cr^3+^ + 6 Fe^3+^ + 7 H~2~O.',
                    '  2. **Oxidation of Iodide to Iodine:** Cr~2~O~7~^2−^ + 14 H^+^ + 6 I^-^ → 2 Cr^3+^ + 3 I~2~ + 7 H~2~O.',
                    '  3. **Oxidation of H~2~S to Sulfur:** Cr~2~O~7~^2−^ + 8 H^+^ + 3 H~2~S → 2 Cr^3+^ + 3 S↓ (colloidal white) + 7 H~2~O.',
                    '  4. **Oxidation of Sulfite to Sulfate:** Cr~2~O~7~^2−^ + 8 H^+^ + 3 SO~3~^2−^ → 2 Cr^3+^ + 3 SO~4~^2−^ + 4 H~2~O.',
                    '  5. **Oxidation of Nitrite to Nitrate:** Cr~2~O~7~^2−^ + 8 H^+^ + 3 NO~2~^-^ → 2 Cr^3+^ + 3 NO~3~^-^ + 4 H~2~O.',
                    '  6. **Oxidation of Tin(II) to Tin(IV):** Cr~2~O~7~^2−^ + 14 H^+^ + 3 Sn^2+^ → 2 Cr^3+^ + 3 Sn^4+^ + 7 H~2~O.'
                ]
            },
            {
                "title": "2. Chromyl Chloride Test (Confirmatory Test for Cl^−^)",
                "tag": "High-Yield Qualitative Analysis",
                "accent": "navy",
                "bullets": [
                    "• **Procedure & Reaction:** Solid chloride salt is heated with solid K~2~Cr~2~O~7~ and concentrated H~2~SO~4~:",
                    '  K~2~Cr~2~O~7~ + 4 KCl + 6 H~2~SO~4~ → 2 CrO~2~Cl~2~ ↑ (deep red vapor) + 6 KHSO~4~ + 3 H~2~O',
                    "• **Absorption in NaOH:** Red vapors of chromyl chloride (CrO~2~Cl~2~) are passed into NaOH solution to form yellow sodium chromate:",
                    '  CrO~2~Cl~2~ + 4 NaOH → Na~2~CrO~4~ (yellow solution) + 2 NaCl + 2 H~2~O',
                    "• **Lead Acetate Confirmation:** Acetic acid + lead acetate is added → bright yellow precipitate of lead chromate forms:",
                    '  Na~2~CrO~4~ + Pb(CH~3~COO)~2~ → PbCrO~4~↓ (bright yellow) + 2 CH~3~COONa',
                    "• **Crucial JEE Exceptions:** Chlorides of heavy metals (**Hg~2~Cl~2~, HgCl~2~, AgCl, PbCl~2~, SnCl~2~**) DO NOT give this test because they are covalent or sparingly soluble. Also, bromides and iodides give free Br~2~ and I~2~, not chromyl halides."
                ]
            },
            {
                "title": "3. The Butterfly Peroxide: Chromium Pentoxide (CrO~5~)",
                "tag": "Blue Peroxide Test",
                "accent": "gold",
                "bullets": [
                    "• When an acidified solution of dichromate is treated with H~2~O~2~ in the presence of ether or amyl alcohol:",
                    '  Cr~2~O~7~^2−^ + 2 H^+^ + 4 H~2~O~2~ → 2 CrO~5~ (intense blue) + 5 H~2~O',
                    '• **Butterfly Structure:** Cr has ONE oxo oxygen (Cr=O) and TWO peroxo groups (Cr(O~2~)~2~).',
                    '• **Oxidation State of Cr in CrO~5~:** Oxo oxygen has oxidation state −2; four peroxo oxygens have −1 each. Net: x + (-2) + 4(-1) = 0 ⇒ **x = +6**! (NOT +10!).',
                    "• **Instability:** Blue color fades rapidly in water as CrO~5~ decomposes to Cr^3+^ and O~2~; stabilized in ether by forming a 1:1 adduct."
                ]
            }
        ]
    },
    {
        "id": "sheet_13",
        "num": 13,
        "title": "Sheet 13 — Potassium Permanganate — Preparation, Structure & Disproportionation",
        "badge": "KMnO4 Chemistry",
        "figure": "permanganate_manganate",
        "boxes": [
            {
                "title": "1. Industrial Preparation of KMnO~4~ from Pyrolusite (MnO~2~)",
                "tag": "Two-Step Industrial Synthesis",
                "accent": "teal",
                "bullets": [
                    "• **Step 1: Oxidative Alkaline Fusion (Manganate Formation):**",
                    "  Finely powdered pyrolusite ore (MnO~2~) is fused with KOH (or K~2~CO~3~) in the presence of air or an oxidizing agent like KNO~3~ or KClO~3~:",
                    '  2 MnO~2~ + 4 KOH + O~2~ → 2 K~2~MnO~4~ (dark green) + 2 H~2~O',
                    "  Dark green potassium manganate (K~2~MnO~4~) is formed.",
                    "• **Step 2: Oxidation of Manganate to Permanganate:**",
                    '  - **Commercial / Electrolytic Route:** Green alkaline solution is electrolyzed between iron electrodes. At anode: MnO~4~^2−^ → MnO~4~^-^ + e^-^ (oxidation to purple permanganate).',
                    "  - **Laboratory / Chemical Route (Disproportionation):** Green manganate solution is acidified or treated with CO~2~ or Cl~2~:",
                    '    3 MnO~4~^2−^ (green) + 4 H^+^ → 2 MnO~4~^-^ (purple) + MnO~2~↓ (brown) + 2 H~2~O',
                    '    2 K~2~MnO~4~ + Cl~2~ → 2 KMnO~4~ + 2 KCl'
                ]
            },
            {
                "title": "2. Structures & Magnetism of Manganate and Permanganate",
                "tag": "Crystal & Orbital Data",
                "accent": "navy",
                "bullets": [
                    '• Both ions adopt a **tetrahedral geometry** involving d^3^s (or sp^3^) hybridization with strong pπ-dπ bonds between manganese and oxygen.',
                    "• **Potassium Manganate ([MnO~4~]^2−^):**",
                    '  - Mn is in **+6** oxidation state (3d^1^).',
                    '  - Has 1 unpaired electron (n = 1) → **Paramagnetic** (μ = 1.73 BM). Dark green color.',
                    "• **Potassium Permanganate ([MnO~4~]^−^):**",
                    '  - Mn is in **+7** oxidation state (3d^0^).',
                    '  - All electrons paired (n = 0) → **Diamagnetic** (temperature-independent weak paramagnetism).',
                    '  - **Intense Purple Color:** Arises from **LMCT (Ligand-to-Metal Charge Transfer)** from O^2−^ → Mn^7+^, NOT from d-d transitions!'
                ]
            },
            {
                "title": "3. Disproportionation & Stability Conditions",
                "tag": "pH Master Principle",
                "accent": "gold",
                "bullets": [
                    "• **Manganate ([MnO~4~]^2−^):** Stable ONLY in strongly alkaline solution (pH > 12). In neutral or acidic media, it spontaneously disproportionates into [MnO~4~]^−^ (+7) and MnO~2~ (+4).",
                    '• **Permanganate ([MnO~4~]^−^):** Decomposes slowly in acidic solution with sunlight: 4 MnO~4~^-^ + 4 H^+^ → 4 MnO~2~ + 3 O~2~ + 2 H~2~O. Hence, standard KMnO~4~ solutions are stored in dark amber bottles.'
                ]
            }
        ]
    },
    {
        "id": "sheet_14",
        "num": 14,
        "title": "Sheet 14 — Potassium Permanganate — Medium-Dependent Oxidizing Reactions",
        "badge": "KMnO4 Redox Spectrum",
        "boxes": [
            {
                "title": "1. Medium Dependence: Acidic, Neutral/Faintly Alkaline & Strongly Alkaline",
                "tag": "The Three Half-Reactions",
                "accent": "teal",
                "bullets": [
                    "• **1. Acidic Medium (dilute H~2~SO~4~):** Mn(+7) is reduced by **5 electrons** to Mn^2+^ (+2):",
                    '  MnO~4~^-^ + 8 H^+^ + 5 e^-^ → Mn^2+^ (faint pink) + 4 H~2~O (E° = +1.51 V)',
                    '  **Eq. Wt = M/5** = 158.04 / 5 = 31.6 g/eq.',
                    "• **2. Neutral or Faintly Alkaline Medium (Baeyer's Condition):** Mn(+7) is reduced by **3 electrons** to brown insoluble MnO~2~ (+4):",
                    '  MnO~4~^-^ + 2 H~2~O + 3 e^-^ → MnO~2~↓ (brown) + 4 OH^-^ (E° = +1.23 V)',
                    '  **Eq. Wt = M/3** = 158.04 / 3 = 52.68 g/eq.',
                    "• **3. Strongly Alkaline Medium:** Mn(+7) is reduced by **1 electron** to green manganate MnO~4~^2−^ (+6):",
                    '  MnO~4~^-^ + e^-^ → MnO~4~^2−^ (green) (E° = +0.56 V)',
                    '  **Eq. Wt = M/1** = 158.04 g/eq.'
                ]
            },
            {
                "title": "2. Major Redox Reactions in Acidic Medium",
                "tag": "Quantitative Volumetry",
                "accent": "navy",
                "bullets": [
                    "• **Oxidation of Oxalate / Oxalic Acid:**",
                    '  2 MnO~4~^-^ + 16 H^+^ + 5 C~2~O~4~^2−^ → 2 Mn^2+^ + 10 CO~2~↑ + 8 H~2~O',
                    "  (Reaction is slow initially; catalyzed autocatalytically by product Mn^2+^ ions!).",
                    '• **Oxidation of Iron(II):** MnO~4~^-^ + 8 H^+^ + 5 Fe^2+^ → Mn^2+^ + 5 Fe^3+^ + 4 H~2~O.',
                    '• **Oxidation of Iodide to Iodine:** 2 MnO~4~^-^ + 16 H^+^ + 10 I^-^ → 2 Mn^2+^ + 5 I~2~ + 8 H~2~O.',
                    '• **Oxidation of Nitrite to Nitrate:** 2 MnO~4~^-^ + 6 H^+^ + 5 NO~2~^-^ → 2 Mn^2+^ + 5 NO~3~^-^ + 3 H~2~O.',
                    '• **Oxidation of H~2~S to Sulfur:** 2 MnO~4~^-^ + 6 H^+^ + 5 H~2~S → 2 Mn^2+^ + 5 S↓ + 8 H~2~O.'
                ]
            },
            {
                "title": "3. Major Redox Reactions in Neutral / Faintly Alkaline Medium",
                "tag": "JEE Trap Alert",
                "accent": "gold",
                "bullets": [
                    "• **Oxidation of Iodide to IODATE (Crucial Contrast!):**",
                    "  In acidic medium, I^−^ is oxidized to I~2~. But in neutral/faintly alkaline medium, I^−^ is oxidized all the way to **Iodate ([IO~3~]^−^)**:",
                    '  2 MnO~4~^-^ + H~2~O + I^-^ → 2 MnO~2~↓ + IO~3~^-^ + 2 OH^-^',
                    "• **Oxidation of Thiosulfate to SULFATE:**",
                    '  8 MnO~4~^-^ + 3 S~2~O~3~^2−^ + H~2~O → 8 MnO~2~↓ + 6 SO~4~^2−^ + 2 OH^-^',
                    '• **Why HCl cannot be used to acidify KMnO~4~:** KMnO~4~ is a stronger oxidant (E° = +1.51 V) than chlorine (E° = +1.36 V), so it oxidizes HCl to Cl~2~ gas: 2 MnO~4~^-^ + 16 HCl → 2 Mn^2+^ + 5 Cl~2~↑ + 8 H~2~O. Only dilute H~2~SO~4~ is suitable!'
                ]
            }
        ]
    },
    {
        "id": "sheet_15",
        "num": 15,
        "title": "Sheet 15 — The Lanthanoids (4f Series) — Properties & Chemistry",
        "badge": "4f Elements",
        "boxes": [
            {
                "title": "1. Electronic Configuration & The Dominant +3 State",
                "tag": "4f Series Overview",
                "accent": "teal",
                "bullets": [
                    "• **Scope:** 14 elements following Lanthanum (La 57), from **Cerium (Ce 58) to Lutetium (Lu 71)**.",
                    "• **General Valence Configuration:** **[Xe] 4f^1-14^ 5d^0-1^ 6s^2^**.",
                    "  - 5d orbital has 1 electron only in **La ([Xe] 5d^1^ 6s^2^), Ce ([Xe] 4f^1^ 5d^1^ 6s^2^), Gd ([Xe] 4f^7^ 5d^1^ 6s^2^), and Lu ([Xe] 4f^14^ 5d^1^ 6s^2^)**.",
                    "  - In all other lanthanoids, 5d electron is shifted into 4f.",
                    "• **The Supreme Dominance of +3 State:** All lanthanoids exhibit **+3** as their principal, most stable oxidation state. Achieved by loss of two 6s electrons and one 4f (or 5d) electron."
                ]
            },
            {
                "title": "2. Exceptions to +3: Stable +2 and +4 States",
                "tag": "High-Yield RedOx Traps",
                "accent": "navy",
                "bullets": [
                    '• **Cerium (+4):** Ce^4+^ attains empty noble gas **4f^0^** configuration. Exceptionally strong oxidizing agent in aqueous solution (E°(Ce^4+^/Ce^3+^) = +1.74 V), used as volumetric oxidant (cerimetry).',
                    "• **Terbium (+4):** Tb^4+^ attains half-filled **4f^7^** configuration. Acts as strong oxidant.",
                    '• **Europium (+2):** Eu^2+^ attains half-filled **4f^7^** configuration ([Xe] 4f^7^). Strong reducing agent, readily oxidized to Eu^3+^ (E°(Eu^3+^/Eu^2+^) = -0.43 V).',
                    "• **Ytterbium (+2):** Yb^2+^ attains completely filled **4f^14^** configuration. Strong reducing agent."
                ]
            },
            {
                "title": "3. Lanthanoid Contraction: Causes, Magnetic & Optical Behavior",
                "tag": "NCERT Master Points",
                "accent": "gold",
                "bullets": [
                    "• **Lanthanoid Contraction Across Series:** Steady decrease in atomic and ionic radii from Ce^3+^ (103 pm) to Lu^3+^ (86 pm). Total ionic contraction is only 17 pm, but cumulative effect is enormous.",
                    "• **Basic Character Trend:** Decrease in ionic radius increases polarizing power (Fajans' rule) → covalent character of M-OH increases → **Ce(OH)~3~ is most basic, Lu(OH)~3~ is least basic**.",
                    "• **Sharp f-f Absorption Spectra:** 4f electrons are deeply shielded by outer 5s^2^ 5p^6^ shells → crystal field from solvent ligands cannot perturb 4f levels → **f-f absorption bands are extremely sharp, line-like** (used in laser crystals, e.g. Nd:YAG).",
                    '• **Mischmetal:** Alloy consisting of ≈95% Lanthanoid metals (mainly Ce ≈50%, La ≈40%), ≈5% Fe, and traces of S, C, Ca. Used in cigarette lighter flints and tracer bullets.'
                ]
            }
        ]
    },
    {
        "id": "sheet_16",
        "num": 16,
        "title": "Sheet 16 — The Actinoids (5f Series) & Comparison with Lanthanoids",
        "badge": "5f Elements",
        "figure": "lanthanoid_actinoid_comparison",
        "boxes": [
            {
                "title": "1. Electronic Configuration & Multiple Oxidation States",
                "tag": "5f Energetics",
                "accent": "teal",
                "bullets": [
                    "• **Scope:** 14 elements following Actinium (Ac 89), from **Thorium (Th 90) to Lawrencium (Lr 103)**.",
                    "• **General Valence Configuration:** **[Rn] 5f^1-14^ 6d^0-2^ 7s^2^**.",
                    "• **Wide Spectrum of Oxidation States:** Unlike lanthanoids (which are restricted to +3), early actinoids exhibit a large variety of oxidation states: **Th (+4), Pa (+5), U (+3, +4, +5, +6), Np (+3, +4, +5, +6, +7), Pu (+3, +4, +5, +6, +7)**.",
                    "• **Why such variable valency?** In actinoids, **5f, 6d, and 7s energy levels are comparable in energy** (very small energy gap), allowing all outer electrons to participate in bonding!"
                ]
            },
            {
                "title": "2. Actinoid Contraction vs Lanthanoid Contraction",
                "tag": "Nuclear Shielding",
                "accent": "navy",
                "bullets": [
                    "• **Actinoid Contraction:** Progressive decrease in size of atoms and M^3+^/M^4+^ ions across the series.",
                    "• **Comparison:** **Actinoid contraction from element to element is GREATER than lanthanoid contraction!**",
                    '• **Physical Reason:** 5f orbitals have a more diffuse spatial distribution than 4f orbitals, resulting in **even poorer shielding** of the nuclear charge. Consequently, the effective nuclear charge (Z~eff~) increases more rapidly across the actinoid series.'
                ]
            },
            {
                "title": "3. Detailed Comparison: Lanthanoids vs Actinoids",
                "tag": "JEE High-Yield Comparison",
                "accent": "gold",
                "bullets": [
                    "• **Oxidation States:** Lanthanoids show mainly +3 (few +2, +4). Actinoids exhibit multiple high states (+3 to +7).",
                    "• **Complex Formation:** Lanthanoids have low complexing tendency (weak bonding). Actinoids have **much higher complexing tendency** due to higher charge density and accessible 5f/6d orbitals.",
                    "• **Oxocations:** Lanthanoids do NOT form oxocations. Actinoids readily form stable oxocations like **[UO~2~]^2+^, [PuO~2~]^2+^, [NpO~2~]^+^**.",
                    "• **Basic Strength:** Actinoid hydroxides are more basic than corresponding lanthanoid hydroxides.",
                    "• **Radioactivity:** In lanthanoids, **only Promethium (Pm 61)** is radioactive. In actinoids, **ALL elements are radioactive** (elements beyond Uranium, Z > 92, are synthetic transuranic elements)."
                ]
            }
        ]
    },
    {
        "id": "sheet_17",
        "num": 17,
        "title": "Sheet 17 — Key Compounds of d-Block Metals — Ag, Cu & Zn",
        "badge": "Inorganic Salts",
        "boxes": [
            {
                "title": "1. Silver Chemistry: AgNO~3~ & Silver Halides",
                "tag": "Lunar Caustic & Photography",
                "accent": "teal",
                "bullets": [
                    '• **Silver Nitrate (AgNO~3~, Lunar Caustic):** Produced by dissolving pure silver in dilute HNO~3~: 3 Ag + 4 HNO~3~ → 3 AgNO~3~ + NO↑ + 2 H~2~O.',
                    '  - Thermal Decomposition: 2 AgNO~3~ —(Δ)→ 2 Ag + 2 NO~2~ + O~2~ (decomposes directly to metallic silver).',
                    "  - Caustic Action: On organic matter/skin, produces a black metallic silver stain.",
                    "• **Silver Halides & Ammonia Solubility:**",
                    "  - **AgF:** Water soluble, yellow-brown crystalline.",
                    '  - **AgCl (White curdy ppt):** Readily soluble in dilute aqueous NH~3~ forming diamminesilver(I): AgCl + 2 NH~3~ → [Ag(NH~3~)~2~]^+^ + Cl^-^.',
                    '  - **AgBr (Pale yellow ppt):** Sparingly soluble in dilute NH~3~, soluble in concentrated NH~3~; soluble in sodium thiosulfate (hypo): AgBr + 2 Na~2~S~2~O~3~ → Na~3~[Ag(S~2~O~3~)~2~] + NaBr (photographic fixing).',
                    "  - **AgI (Bright yellow ppt):** Completely insoluble in both dilute and concentrated NH~3~; dissolves only in cyanide or hypo."
                ]
            },
            {
                "title": "2. Copper Chemistry: Blue Vitriol & Cuprous Compounds",
                "tag": "CuSO4 & CuI",
                "accent": "navy",
                "bullets": [
                    "• **Copper Sulfate Pentahydrate (CuSO~4~·5H~2~O, Blue Vitriol):**",
                    '  - **Structural Insight:** Four water molecules are coordinated to Cu^2+^ in a square planar arrangement ([Cu(H~2~O)~4~]^2+^), while the fifth water molecule is held by **hydrogen bonds** between coordinated waters and the sulfate anion: [Cu(H~2~O)~4~]SO~4~· H~2~O!',
                    "  - **Thermal Dehydration:**",
                    '    CuSO~4~· 5H~2~O —(100° C)→ CuSO~4~· H~2~O —(250° C)→ CuSO~4~ (white anhydrous) —(750° C)→ CuO + SO~3~',
                    "• **Reaction with KI (Iodometric Titration Foundation):**",
                    '  2 CuSO~4~ + 4 KI → 2 CuI↓ (white) + I~2~ + 2 K~2~SO~4~',
                    "  Liberated iodine is titrated with hypo using starch indicator."
                ]
            },
            {
                "title": "3. Zinc Chemistry: Zinc Blende, Amphoterism & Lithopone",
                "tag": "Amphoteric Metal",
                "accent": "gold",
                "bullets": [
                    "• **Amphoteric Nature of Zn, ZnO, and Zn(OH)~2~:** React with both acids and bases:",
                    '  Zn + 2 NaOH → Na~2~ZnO~2~ (sodium zincate) + H~2~↑',
                    '  ZnO + 2 NaOH + H~2~O → Na~2~[Zn(OH)~4~]',
                    "• **Zinc Vitriol (ZnSO~4~·7H~2~O, White Vitriol):** Isomorphous with Epsom salt (MgSO~4~·7H~2~O).",
                    '• **Lithopone:** Equimolar mixture of **BaSO~4~ + ZnS**, prepared by precipitation: BaS + ZnSO~4~ → BaSO~4~↓ + ZnS↓. Used as an excellent non-poisonous white paint pigment (does not blacken in H~2~S atmosphere!).'
                ]
            }
        ]
    },
    {
        "id": "sheet_18",
        "num": 18,
        "title": "Sheet 18 — Key Compounds of Iron & JEE Advanced Reasoning Bank",
        "badge": "Fe Chemistry & Traps",
        "boxes": [
            {
                "title": "1. Iron Compounds: Mohr's Salt, Green Vitriol & Prussian Blue",
                "tag": "Complexes & Double Salts",
                "accent": "teal",
                "bullets": [
                    "• **Mohr's Salt (Ferrous Ammonium Sulfate):**",
                    "  - Formula: **FeSO~4~·(NH~4~)~2~SO~4~·6H~2~O**.",
                    "  - Primary standard for Fe^2+^ volumetry because it is **resistant to atmospheric oxidation** in solid form (unlike pure FeSO~4~·7H~2~O, which rapidly turns brown due to basic ferric sulfate).",
                    "• **Ferrous Sulfate (FeSO~4~·7H~2~O, Green Vitriol):**",
                    '  - Thermal Decomposition: 2 FeSO~4~· 7H~2~O —(Δ)→ Fe~2~O~3~ (red-brown) + SO~2~↑ + SO~3~↑ + 14 H~2~O.',
                    "• **Prussian Blue & Turnbull's Blue Identity:**",
                    '  - Fe^3+^ + potassium ferrocyanide → **Prussian Blue**: Fe^3+^ + [Fe(CN)~6~]^4−^ → Fe~4~[Fe(CN)~6~]~3~ (or KFe[Fe(CN)~6~]).',
                    "  - Fe^2+^ + potassium ferricyanide → **Turnbull's Blue**: Fe^2+^ + [Fe(CN)~6~]^3−^ → KFe[Fe(CN)~6~].",
                    '  - **Modern Spectroscopic Truth:** Both compounds are chemically identical: **iron(III) hexacyanoferrate(II)** (KFe^III^[Fe^II^(CN)~6~]), with intense deep blue colour due to **inter-valence charge transfer (IVCT)** between Fe(II) and Fe(III)!'
                ]
            },
            {
                "title": "2. Brown Ring Complex Structure & Mechanism",
                "tag": "Spectroscopy & Nitrosyl",
                "accent": "navy",
                "bullets": [
                    "• **Test for Nitrate:** Nitrate solution + freshly prepared FeSO~4~ + conc H~2~SO~4~ along test tube walls.",
                    "• **Formula:** **[Fe(H~2~O)~5~(NO)]SO~4~**.",
                    "• **Charge Transfer & Oxidation State:**",
                    '  - Historically formulated as Fe(+1) and NO^+^. Modern spectroscopic measurements reveal that electron transfer occurs from NO to Fe^3+^, giving an equilibrium between Fe(+1)-NO^+^ and Fe(+3)-NO^−^ with **3 unpaired electrons** (μ~eff~ ≈ 3.87 BM).',
                    "  - Brown color is due to **charge transfer** between iron and nitrosyl ligand."
                ]
            },
            {
                "title": "3. JEE Advanced Reasoning Bank — Top Traps Solved",
                "tag": "Exam Master File",
                "accent": "gold",
                "bullets": [
                    "• **Q1: Why is Sc^3+^ diamagnetic and colourless while Ti^3+^ is purple?**",
                    "  Sc^3+^ has [Ar] 3d^0^ (no d electrons, no d-d transition). Ti^3+^ has 3d^1^; visible light promotes electron from t~2g~ to e~g~.",
                    "• **Q2: Why is the enthalpy of atomization of Zn lowest in 3d?**",
                    "  Zn has completely filled 3d^10^ 4s^2^; no unpaired d-electrons participate in metallic bonding.",
                    "• **Q3: Why is Cr^2+^ reducing while Mn^3+^ is oxidizing though both are 3d^4^?**",
                    "  Cr^2+^ oxidizes to Cr^3+^ (half-filled t~2g~^3^ in octahedral field, high CFSE). Mn^3+^ reduces to Mn^2+^ (half-filled 3d^5^ shell, huge exchange energy).",
                    "• **Q4: Why does Cu^+^ disproportionate in aqueous solution?**",
                    '  Although Cu^+^ has stable 3d^10^, Cu^2+^ has much higher charge density, yielding a very large negative hydration enthalpy (Δ~hyd~ H° = −2121 kJ/mol) that more than overcomes the second ionization energy of copper.'
                ]
            }
        ]
    }
]
