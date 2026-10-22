"""Part 3: Sheets CC-13 to CC-18 — Square Planar, Jahn-Teller, Color, Carbonyls, Stability & Applications."""
from __future__ import annotations

SHEETS = [
    # ------------------------------------------------------------------ CC-13
    {
        "id": "CC-13",
        "title": "CFT in Square Planar Complexes & Splitting Hierarchy",
        "blocks": [
            ("lead", "**Crystal Field Splitting in D~4h~ Geometry & The d^8^ Configuration** (NCERT §9.5.3)"),
            ("p", 'Square planar geometry (D~4h~) is derived conceptually from an octahedral complex by progressively pulling the two trans ligands along the z-axis to infinity (tetragonal distortion to the square planar limit).'),
            ("fig", "square_planar_splitting", "Fig. 13.1 — Octahedral to tetragonal to square planar (D~4h~) crystal field energy levels."),
            ("h2", "1. Orbital Energy Splitting in D~4h~ Symmetry"),
            ("bul", [
                '**1. d~x~²-y² (Highest Energy):** Lobes point directly at the 4 remaining in-plane ligands (x, y) ⇒ experiences maximal electrostatic repulsion; elevated to the highest energy level.',
                '**2. d~xy~ (Second Highest):** Lobes lie in the xy-plane between the ligands ⇒ substantial in-plane repulsion, but lower than d~x²−y²~.',
                '**3. d~z~² (Third Highest):** Completely relieved of direct axial ligand encounters; stabilized substantially, lying below d~xy~ (its donut ring lies in the xy-plane).',
                '**4. d~xz~, d~yz~ (Lowest Energy, Degenerate Pair):** Lobes point completely out of the coordination plane ⇒ experience minimum repulsion.',
                "**Master Energy Order in Square Planar:**",
                '  **d~x²−y²~ ≫ d~xy~ > d~z²~ > (d~xz~ = d~yz~)**',
                '  The total square planar splitting energy is **Δ~sp~ ≈ 1.3 to 1.74 Δ~o~**.'
            ]),
            ("h2", "2. Why d^8^ Metal Ions Universally Form Square Planar Complexes"),
            ("p", 'In d^8^ electronic systems (e.g. Ni^2+^, Pd^2+^, Pt^2+^, Au^3+^), the 8 d-electrons occupy the lower four orbitals in spin-paired configurations: (d~xz~, d~yz~)^4^ (d~z²~)^2^ (d~xy~)^2^, leaving the strongly destabilized d~x²−y²~ completely empty!\n'
                  "• This produces an enormous Crystal Field Stabilization Energy (CFSE gain) that heavily favors square planar over tetrahedral geometry.\n"
                  '• **All 4d^8^ (Pd^2+^) and 5d^8^ (Pt^2+^, Au^3+^) complexes are SQUARE PLANAR and DIAMAGNETIC**, regardless of ligand field strength (even with weak Cl^-^ in [PtCl~4~]^2−^)!'),
            ("h2", "3. Nickel(II) Complex Stereochemistry: [Ni(CN)~4~]^2−^ vs [NiCl~4~]^2−^"),
            ("table", ["Complex Ion", "Ligand Type / Field", "Geometry & Hybridization", 'Unpaired e^-^ (n)', "Magnetic Character"], [
                ['[Ni(CN)~4~]^2−^', 'Strong field CN^-^', '**Square Planar (dsp^2^)**', "**0**", "**Diamagnetic** (Yellow)"],
                ['[NiCl~4~]^2−^', 'Weak field Cl^-^', '**Tetrahedral (sp^3^)**', "**2**", '**Paramagnetic** (μ = 2.83 BM)'],
                ['[Ni(CO)~4~]', 'Strong field CO (Ni^0^, 3d^10^)', '**Tetrahedral (sp^3^)**', "**0**", "**Diamagnetic** (Colorless)"]
            ], [20, 22, 24, 14, 20], "Table 13.1 — Contrasting geometries and magnetism in nickel complexes."),
            ("trap", 'EXAM TRAP: [PtCl~4~]^2−^ and [Pt(NH~3~)~4~]^2+^ are BOTH square planar and diamagnetic because Pt is a 5d metal with huge Δ!')
        ]
    },

    # ------------------------------------------------------------------ CC-14
    {
        "id": "CC-14",
        "title": "Jahn–Teller Distortion & Tetragonal Elongation in d^9^ / High-Spin d^4^",
        "blocks": [
            ("lead", "**Electronic Degeneracy & Spontaneous Geometric Distortion** (JEE Advanced Special)"),
            ("p", "The Jahn–Teller Theorem states: *Any non-linear molecular system in a spatially degenerate electronic ground state is unstable and will undergo geometric distortion to lower its symmetry, remove the degeneracy, and lower the overall energy.*"),
            ("h2", '1. Asymmetric Electron Occupation: e~g~ vs t~2g~'),
            ("bul", [
                '**1. Strong Jahn–Teller Distortion (Asymmetric e~g~ Occupation):**',
                '  Because e~g~ orbitals (d~x²−y²~, d~z²~) point directly at ligands, an uneven electron distribution in e~g~ causes strong unequal repulsions on ligand pairs ⇒ **pronounced geometric distortion**.',
                '  - **d^9^ System (e.g. Cu^2+^, t~2g~^6^ e~g~^3^):** Most famous case! One orbital has 2 electrons while the other has 1 electron.',
                '  - **High-Spin d^4^ System (e.g. Cr^2+^, Mn^3+^, t~2g~^3^ e~g~^1^):** Unequal occupation of e~g~.',
                '  - **Low-Spin d^7^ System (e.g. Co^2+^ LS, Ni^3+^ LS, t~2g~^6^ e~g~^1^):** Pronounced distortion.',
                "**2. Weak Jahn–Teller Distortion (Asymmetric t~2g~ Occupation):**",
                '  t~2g~ orbitals point between ligands ⇒ unequal electron distribution (d^1^, d^2^, HS d^6^, HS d^7^) produces only **very weak, subtle distortions** that are experimentally hard to observe.',
                "**3. Zero Jahn–Teller Distortion (Symmetrical Occupation):**",
                '  d^3^ (t~2g~^3^), HS d^5^ (t~2g~^3^ e~g~^2^), LS d^6^ (t~2g~^6^), d^8^ (t~2g~^6^ e~g~^2^), and d^10^ (t~2g~^6^ e~g~^4^) have completely symmetrical sets ⇒ **zero distortion (perfect Oh symmetry)**!'
            ]),
            ("h2", "2. Tetragonal Elongation (z-out) vs Compression (z-in)"),
            ("p", 'In the vast majority of copper(II) complexes (e.g. [Cu(H~2~O)~6~]^2+^):\n'
                  '• If the 3rd e~g~ electron enters d~z²~ (d~z²~^2^ d~x²−y²~^1^), electrons shield the nucleus along the z-axis, weakening metal-ligand attraction ⇒ **two trans axial ligands move further away (z-elongation)**!\n'
                  '• **Result:** 4 short in-plane equatorial bonds and **2 longer axial bonds** (e.g. in CuF~2~, 4 equatorial Cu-F = 193 pm, 2 axial Cu-F = 227 pm!).'),
            ("h2", "3. Copper(II) Ammonia Complex Stepwise Stability Drop"),
            ("p", 'In [Cu(NH~3~)~4~(H~2~O)~2~]^2+^, adding ammonia readily replaces the 4 in-plane equatorial water molecules to form [Cu(NH~3~)~4~]^2+^, but the 5th and 6th water molecules on the elongated z-axis are so weakly bound that [Cu(NH~3~)~6~]^2+^ can ONLY be formed in anhydrous liquid ammonia!'),
            ("trap", 'HIGH-YIELD JEE ADVANCED QUESTION: Which of the following shows strong Jahn-Teller distortion? (A) [Cr(H~2~O)~6~]^3+^ (d^3^), (B) [Mn(H~2~O)~6~]^2+^ (d^5^), (C) [Cu(H~2~O)~6~]^2+^ (d^9^), (D) [Fe(CN)~6~]^4−^ (d^6^). **Answer is C** (d^9^ asymmetric e~g~)!')
        ]
    },

    # ------------------------------------------------------------------ CC-15
    {
        "id": "CC-15",
        "title": "Colour in Coordination Compounds & Absorption Spectroscopy",
        "blocks": [
            ("lead", "**Electronic Transitions & Complementary Visible Absorption** (NCERT §9.5.4)"),
            ("p", 'The vivid colors of coordination complexes arise primarily from the absorption of specific wavelengths of visible light to excite electrons between crystal-field-split d-orbitals (d-d transitions).'),
            ("h2", "1. Mechanism of Colour & The Complementary Wheel"),
            ("bul", [
                '**Light Absorption:** When white light strikes a solution of a complex with an incompletely filled d-subshell (d^1^ to d^9^), a photon of energy hν = Δ~o~ is absorbed to promote an electron from t~2g~ to e~g~.',
                "**Complementary Transmission:** The human eye perceives the light that is NOT absorbed — the **complementary color**:\n"
                  '  - **Absorbs Red** (long λ, small Δ) → Appears **Green**.\n'
                  '  - **Absorbs Yellow** → Appears **Violet / Blue**.\n'
                  '  - **Absorbs Blue-Green** → Appears **Red / Orange**.\n'
                  '  - **Absorbs Violet** (short λ, large Δ) → Appears **Yellow**.'
            ]),
            ("h2", "2. Influence of Ligand on Color: [Ni(H~2~O)~6~]^2+^ Stepwise Substitution"),
            ("p", 'Progressive replacement of weak H~2~O by stronger ethylenediamine (en) increases Δ~o~, shifting absorption to shorter wavelengths (higher frequency):\n'
                  '  1. [Ni(H~2~O)~6~]^2+^: **Green** (absorbs red light).\n'
                  '  2. [Ni(H~2~O)~4~(en)]^2+^: **Pale blue**.\n'
                  '  3. [Ni(H~2~O)~2~(en)~2~]^2+^: **Blue / Purple**.\n'
                  '  4. [Ni(en)~3~]^2+^: **Violet** (absorbs yellow light, largest Δ~o~!).'),
            ("h2", "3. Ruby and Emerald: Crystal Field Gemstones"),
            ("bul", [
                '**Ruby:** Consists of colorless α-Al~2~O~3~ in which ≈ 0.5-1% of Al^3+^ sites are occupied by Cr^3+^ (d^3^). In the tight alumina lattice, Al-O distance is short, compressing Cr^3+^ ⇒ strong crystal field absorbs yellow-green light, transmitting **deep crimson red**!',
                '**Emerald:** Cr^3+^ replaces Al^3+^ in beryl (Be~3~Al~2~Si~6~O~18~). Larger silicate cavities provide a slightly weaker crystal field, shifting absorption into the red/yellow region and transmitting **brilliant green**!'
            ]),
            ("trap", 'WHY IS ANHYDROUS CuSO~4~ WHITE? When white anhydrous CuSO~4~ has no water ligands, the crystal field splitting is zero (Δ = 0). All 5 d-orbitals remain degenerate; no d-d transitions are possible ⇒ pure white!')
        ]
    },

    # ------------------------------------------------------------------ CC-16
    {
        "id": "CC-16",
        "title": 'Bonding in Metal Carbonyls: Synergic Effect & IR ν~C~O Trends',
        "blocks": [
            ("lead", "**Organometallic Synergy: σ-Donation & π-Backbonding** (NCERT §9.6)"),
            ("p", 'Homoleptic metal carbonyls (e.g. [Ni(CO)~4~], [Fe(CO)~5~], [Cr(CO)~6~]) exhibit unique metal-carbon bonding characterized by mutual reinforcement between σ and π bonds.'),
            ("fig", "carbonyl_synergic_bonding", "Fig. 16.1 — Synergic M-CO bonding: σ donation from C lone pair and π backbonding into CO π* orbitals."),
            ("h2", "1. The Synergic Bonding Mechanism"),
            ("bul", [
                '**1. M ← C σ-Bond:** Carbon atom of CO donates its lone pair of electrons from a filled non-bonding sp-hybrid orbital into an empty hybrid orbital of the transition metal.',
                '**2. M → C π-Backbond:** Filled d-orbitals (d~xy~, d~yz~, d~zx~) of the transition metal overlap sideways with the **empty antibonding π* molecular orbitals** of the carbon monoxide ligand.',
                '**3. The Synergic Loop:** σ-donation increases electron density on the metal, facilitating π-backdonation; simultaneously, π-backdonation relieves excess negative charge from the metal, strengthening the σ-bond! This self-reinforcing cooperative loop is called **synergic bonding**.'
            ]),
            ("h2", '2. Impact on M-C and C-O Bond Orders & IR Stretching Frequencies (ν~C~O)'),
            ("p", 'When electrons are back-donated into the **antibonding π* orbital** of CO:\n'
                  '• Metal-Carbon (M-C) bond order increases (approaching double bond M=C): bond becomes **shorter and stronger**.\n'
                  '• Carbon-Oxygen (C-O) bond order decreases (from triple bond C≡O towards double bond C=O): bond becomes **longer and weaker**!\n'
                  "• By Hooke's Law (ν = 1 / (2π c)√(k/μ)), a weaker bond has a lower force constant k and thus a **lower IR stretching frequency ν~CO~**."),
            ("h2", "3. Isoelectronic Carbonyl Series (JEE Advanced Master Metric)"),
            ("table", ["Carbonyl Species", "Metal & OS", "Extrapolated π-Backdonation", "M-C Bond Strength / Length", 'C-O Bond Order & IR ν~CO~ (cm^−1^)'], [
                ['[Mn(CO)~6~]^+^', 'Mn(+1)', "Least (positive charge holds d-electrons)", "Weakest / Longest M-C", '**Strongest C-O / Highest ν~CO~** (≈2090 cm^−1^)'],
                ['[Cr(CO)~6~]', 'Cr(0)', "Intermediate", "Intermediate M-C", 'Intermediate C-O (≈2000 cm^−1^)'],
                ['[V(CO)~6~]^-^', 'V(-1)', "**Most (negative charge repels d-electrons)**", "**Strongest / Shortest M-C**", '**Weakest C-O / Lowest ν~CO~** (≈1860 cm^−1^)']
            ], [18, 16, 26, 20, 20], "Table 16.1 — Isoelectronic carbonyl comparison: charge vs backdonation and IR frequencies."),
            ("trap", 'CRITICAL JEE ADVANCED TRAP: Higher negative charge on the metal carbonyl complex ⇒ GREATER π-backdonation ⇒ SHORTER M-C bond ⇒ LONGEST C-O bond ⇒ LOWEST ν~CO~ stretching frequency!')
        ]
    },

    # ------------------------------------------------------------------ CC-17
    {
        "id": "CC-17",
        "title": "Thermodynamic vs Kinetic Stability & Irving–Williams Series",
        "blocks": [
            ("lead", "**Stepwise Formation Constants & Stability Determinants** (NCERT §9.8)"),
            ("p", "The stability of a complex in solution refers to the degree of association between the metal ion and the ligands involved in dynamic equilibrium."),
            ("h2", '1. Stepwise vs Overall Stability Constants (K~n~ vs β~n~)'),
            ("p", "In solution, ligands add to a metal ion in a stepwise sequence:\n"
                  '  M + L ⇌ ML (K~1~ = [ML] / [M][L])\n'
                  '  ML + L ⇌ ML~2~ (K~2~ = [ML~2~] / [ML][L])\n'
                  '  Overall: M + nL ⇌ ML~n~ (β~n~ = K~1~ · K~2~ · … · K~n~)\n'
                  '• In terms of logarithms: **log β~n~ = log K~1~ + log K~2~ + … + log K~n~**.\n'
                  '• **Universal Trend:** Stepwise constants almost invariably follow: **K~1~ > K~2~ > K~3~ > ... > K~n~** due to electrostatic repulsion, statistical probability of vacant sites, and steric crowding.'),
            ("h2", "2. The Irving–Williams Series for Divalent 3d Metal Ions"),
            ("p", 'For high-spin octahedral complexes of divalent 3d transition metal cations (M^2+^), stability increases progressively regardless of the ligand nature, reaching a sharp maximum at Copper:\n'
                  '  **Ba^2+^ < Sr^2+^ < Ca^2+^ < Mg^2+^ < Mn^2+^ < Fe^2+^ < Co^2+^ < Ni^2+^ < Cu^2+^ > Zn^2+^**\n'
                  "• **Physical Driving Factors:**\n"
                  '  1. **Ionic Size Decrease:** Radii contract from Mn^2+^ to Cu^2+^, increasing electrostatic charge density (q/r).\n'
                  '  2. **CFSE Gain:** Crystal field stabilization energy increases progressively from d^5^ (Mn^2+^, CFSE = 0) to d^8^ (Ni^2+^).\n'
                  '  3. **The Copper Peak (Cu^2+^ > Zn^2+^):** Copper(II) (d^9^) experiences intense **Jahn–Teller distortion**, shortening 4 equatorial bonds and producing an exceptionally stable complex! Zn^2+^ (d^10^, CFSE = 0) drops sharply in stability.'),
            ("h2", "3. Thermodynamic vs Kinetic Stability"),
            ("bul", [
                '**Thermodynamic Stability:** Measured by the equilibrium formation constant β~n~ (or Δ G° = -RT ln β~n~). High β indicates a stable complex.',
                "**Kinetic Stability (Lability vs Inertness):** Refers to the **rate of ligand substitution**:\n"
                  '  - **Labile Complexes:** Undergo ligand substitution very rapidly (t~1/2~ < 1 minute). E.g. [Cu(NH~3~)~4~]^2+^ exchanges with ^14^NH~3~ instantaneously.\n'
                  '  - **Inert Complexes:** Undergo ligand exchange very slowly (t~1/2~ > 1 minute). E.g. d^3^ (Cr^3+^) and low-spin d^6^ (Co^3+^) complexes are kinetically inert!'
            ]),
            ("trap", 'CRITICAL TRAP: [Fe(CN)~6~]^4−^ is thermodynamically very stable (huge β), but kinetically labile. Conversely, [Co(NH~3~)~6~]^3+^ is thermodynamically unstable in acid (breaks down to Co^2+^), but kinetically so inert that it persists for days without decomposing!')
        ]
    },

    # ------------------------------------------------------------------ CC-18
    {
        "id": "CC-18",
        "title": "Applications of Coordination Compounds & JEE Advanced Master Sheet",
        "blocks": [
            ("lead", "**Bio-Inorganic Role, Metallurgical Extraction & Medicine** (NCERT §9.7)"),
            ("h2", "1. Major Analytical, Metallurgical & Biological Applications"),
            ("bul", [
                '**1. Analytical Chemistry:** Ni^2+^ reacts with dmg in ammoniacal solution to give a **scarlet red precipitate** [Ni(dmg)~2~] stabilized by O-H···O hydrogen bonds. Hardness of water is estimated with standard Na~2~H~2~EDTA (EBT indicator).',
                '**2. Metallurgy & Metal Extraction:** **MacArthur-Forrest Cyanide Process:** Au/Ag leached with NaCN: 4Au + 8CN^-^ + 2H~2~O + O~2~ → 4[Au(CN)~2~]^-^ + 4OH^-^, recovered by zinc displacement. **Mond Process:** Nickel purified via volatile [Ni(CO)~4~].',
                '**3. Biological Role:** **Chlorophyll:** Coordination complex of **Mg^2+^** (photosynthesis). **Hemoglobin:** Complex of **Fe^2+^** with protoporphyrin IX (oxygen carrier). **Vitamin B~12~:** Complex of **Co^3+^** (corrin ring).',
                '**4. Medicinal Chemistry:** **Cisplatin (cis-[Pt(NH~3~)~2~Cl~2~]):** Potent anti-cancer agent. **Chelation Therapy:** Ca-EDTA^2−^ for lead poisoning; D-penicillamine for Wilson disease.'
            ]),
            ("h2", "2. JEE Advanced Core Master Reasoning Bank"),
            ("table", ["Exam Diagnostic Question", "Core Theoretical Principle", "Precise Exam Explanation"], [
                ["**Why is [Fe(H~2~O)~6~]^3+^ colored while [Mn(H~2~O)~6~]^2+^ is very pale?**", "Laporte & Spin Selection", 'Mn^2+^ is high-spin d^5^; any d-d transition requires spin flip (spin-forbidden). Fe^3+^ has charge transfer enhancement.'],
                ["**Why is [CoF~6~]^3−^ paramagnetic while [Co(NH~3~)~6~]^3+^ is diamagnetic?**", "Splitting vs Pairing", 'F^-^ is weak field (Δ~o~ < P ⇒ t~2g~^4^ e~g~^2^, 4 unp). NH~3~ is strong field (Δ~o~ > P ⇒ t~2g~^6^ e~g~^0^, 0 unp).'],
                ["**Why do tetrahedral complexes never form low-spin states?**", 'Magnitude of Δ~t~', 'Δ~t~ = 4 / 9 Δ~o~. Electrostatic field is weak, so Δ~t~ < P always holds.'],
                ["**Why does [Ni(dmg)~2~] precipitate selectively?**", "Hydrogen Bonding", "Planar arrangement with 2 symmetrical O-H···O bridges forms a neutral, highly insoluble chelate lattice."]
            ], [28, 28, 44], "Table 18.1 — Authoritative JEE Advanced reasoning traps and diagnostic answers."),
            ("trap", 'FINAL EXAM WARNING: In metal carbonyls, backbonding reduces the C-O bond order and increases the M-C bond order! Always check whether the question asks about M-C or C-O bond length before answering!')
        ]
    }
]
