"""Part 2: Sheets CC-07 to CC-12 — Isomerism, EAN, VBT & Crystal Field Theory (Octahedral/Tetrahedral)."""
from __future__ import annotations

SHEETS = [
    # ------------------------------------------------------------------ CC-07
    {
        "id": "CC-07",
        "title": "Structural Isomerism: Ionization, Solvate, Linkage & Coordination",
        "blocks": [
            ("lead", "**Constitutional Isomerism in Coordination Entities** (NCERT §9.4.1)"),
            ("p", "Structural isomers possess the same molecular formula but differ in the connectivity of chemical bonds or distribution of ions between the inner coordination sphere and the outer ionization sphere."),
            ("h2", "1. The Four Primary Classes of Structural Isomerism"),
            ("bul", [
                "**1. Ionization Isomerism:** Arises when an ionizable counter-ion swaps places with a coordinated ligand within the coordination sphere, giving different ions in solution:",
                '  - Pair A: [Co(NH~3~)~5~**SO~4~**]**Br** (Red-violet) → gives Br^-^ ion (pale yellow ppt with AgNO~3~; no ppt with BaCl~2~).',
                '  - Pair B: [Co(NH~3~)~5~**Br**]**SO~4~** (Red) → gives SO~4~^2−^ ion (white ppt of BaSO~4~ with BaCl~2~; no ppt with AgNO~3~).',
                "**2. Solvate / Hydrate Isomerism:** Special case of ionization isomerism where water molecules differ in being coordinated as ligands vs trapped as crystal lattice solvent:",
                '  - [Cr(H~2~O)~6~]Cl~3~ (**Violet**): 3 free Cl^-^ ions; 3 moles AgCl ppt; 0 lattice H~2~O lost over H~2~SO~4~.',
                '  - [Cr(H~2~O)~5~Cl]Cl~2~·H~2~O (**Blue-green**): 2 free Cl^-^ ions; 2 moles AgCl ppt; 1 mole H~2~O lost.',
                '  - [Cr(H~2~O)~4~Cl~2~]Cl· 2H~2~O (**Dark green**): 1 free Cl^-^ ion; 1 mole AgCl ppt; 2 moles H~2~O lost.',
                "**3. Linkage Isomerism:** Occurs when an **ambidentate ligand** can bind to the metal through either of two different donor atoms:",
                '  - [Co(NH~3~)~5~(**NO~2~**)]Cl~2~ (**Yellow-brown**, Pentaamminenitrito-N-cobalt(III) chloride; M-N bond).',
                '  - [Co(NH~3~)~5~(**ONO**)]Cl~2~ (**Red**, Pentaamminenitrito-O-cobalt(III) chloride; M-O bond).',
                "**4. Coordination Isomerism:** Occurs in binuclear compounds where both cation and anion are complex ions, resulting from mutual exchange of ligands between the two metal centers:",
                '  - E.g. [Co(NH~3~)~6~][Cr(CN)~6~] and [Cr(NH~3~)~6~][Co(CN)~6~].'
            ]),
            ("h2", "2. Advanced Structural Variants for JEE Advanced"),
            ("bul", [
                "**Ligand Isomerism:** Isomerism originating within the organic ligand itself. E.g. 1,2-diaminopropane (pn) vs 1,3-diaminopropane (tn).",
                "**Coordination Position Isomerism:** In polynuclear bridged complexes, an exchange of non-bridging ligands between the two metal centers:",
                '  - [(NH~3~)~4~Co(μ-NH~2~)(μ-O~2~)Co(NH~3~)~2~Cl~2~]^2+^ vs [(NH~3~)~3~ClCo(μ-NH~2~)(μ-O~2~)Co(NH~3~)~3~Cl]^2+^.'
            ]),
            ("trap", 'EXAM TRAP: [Pt(NH~3~)~4~][PtCl~4~] and [Pt(NH~3~)~3~Cl][Pt(NH~3~)Cl~3~] are COORDINATION ISOMERS! Check the oxidation states carefully to ensure both complexes remain chemically viable (+2 on both Pt).')
        ]
    },

    # ------------------------------------------------------------------ CC-08
    {
        "id": "CC-08",
        "title": "Stereoisomerism: Geometrical (Cis-Trans & Fac-Mer) in CN = 4 and 6",
        "blocks": [
            ("lead", "**Spatial Arrangement of Ligands Around Metal Centers** (NCERT §9.4.2)"),
            ("p", "Stereoisomers have the same chemical formula and atom-to-atom bonding sequence, but differ in the three-dimensional orientation of ligands in space. Geometrical isomerism arises when ligands occupy adjacent (cis) or opposite (trans) coordination sites."),
            ("fig", "isomerism_cis_trans", "Fig. 8.1 — Cisplatin vs Trans-isomer and Facial (fac) vs Meridional (mer) octahedra."),
            ("h2", "1. Geometrical Isomerism in Coordination Number 4"),
            ("bul", [
                '**Tetrahedral Complexes (CN = 4):** CANNOT exhibit geometrical isomerism because all four coordination positions are mutually adjacent and equidistant to each other (all bond angles are 109.5°)! E.g. [Ma~2~b~2~], [Mabcd] have NO cis/trans isomers.',
                "**Square Planar Complexes (CN = 4, sp^2^d or dsp^2^):**",
                '  - **[Ma~2~b~2~]:** Forms **2 geometrical isomers**: **Cis** (identical ligands adjacent at 90°) and **Trans** (identical ligands opposite at 180°). Classic: **Cisplatin** (cis-[Pt(NH~3~)~2~Cl~2~], anti-cancer drug) vs **Transplatin** (inactive).',
                "  - **[Ma~2~bc]:** Forms **2 geometrical isomers** (cis and trans with respect to 'a').",
                "  - **[Mabcd]:** Forms **3 geometrical isomers** (fix ligand 'a' and place 'b', 'c', 'd' trans to it).",
                '  - **[M(AB)~2~]:** Unsymmetrical bidentate ligand (e.g. [Pt(gly)~2~]) forms **2 isomers** (cis and trans).'
            ]),
            ("h2", "2. Geometrical Isomerism in Octahedral Complexes (CN = 6)"),
            ("bul", [
                "**[Ma~4~b~2~]:** Forms **2 isomers** (Cis: 90° angle between 'b' ligands; Trans: 180° angle between 'b' ligands). E.g. [Co(NH~3~)~4~Cl~2~]^+^.",
                "**[Ma~3~b~3~] — Facial (fac) and Meridional (mer) Isomerism:**",
                "  - **Facial (fac-isomer):** Three donor atoms 'a' occupy the corners of a single triangular octahedral face. All three 'a' ligands are mutually cis (90°). E.g. fac-[Co(NH~3~)~3~(NO~2~)~3~].",
                "  - **Meridional (mer-isomer):** Three donor atoms 'a' lie on a common plane (the meridian) passing through the metal center. Two 'a' ligands are trans (180°), while the third is cis (90°).",
                '**[M(AA)~2~b~2~]:** (e.g. [Co(en)~2~Cl~2~]^+^) forms **Cis** and **Trans** isomers. The cis isomer lacks a center of inversion, while trans is centrosymmetric.'
            ]),
            ("trap", 'CRITICAL TRAP: [Ma~6~] and [Ma~5~b] CANNOT show geometrical isomerism in octahedral coordination! At least two non-identical ligands are required.')
        ]
    },

    # ------------------------------------------------------------------ CC-09
    {
        "id": "CC-09",
        "title": "Stereoisomerism: Optical Activity, Enantiomers & Master Counting Tables",
        "blocks": [
            ("lead", "**Chirality, Symmetry Elements & Isomer Counting Tables** (NCERT §9.4.2)"),
            ("p", "Optical isomers (enantiomers) are non-superimposable mirror images that rotate the plane of polarized light in opposite directions (dextro '+' and laevo '−'). Chirality requires the complete **absence of improper rotation axes (no plane of symmetry σ and no center of inversion i)**."),
            ("h2", "1. Optical Activity in Octahedral Complexes"),
            ("bul", [
                '**1. [M(AA)~3~] (Tris-chelate complexes):** E.g. [Co(en)~3~]^3+^, [Cr(ox)~3~]^3−^. Belong to chiral point group D~3~. Completely devoid of any plane of symmetry σ or center of inversion i ⇒ **Chiral and optically active!** Exist as non-superimposable Δ (right-handed propeller) and Λ (left-handed propeller) enantiomeric pair.',
                '**2. [M(AA)~2~b~2~] (Bis-chelate complexes):** E.g. [Co(en)~2~Cl~2~]^+^:',
                '  - **Trans-isomer:** Possesses a plane of symmetry (and center of inversion) ⇒ **Optically INACTIVE (achiral)**.',
                '  - **Cis-isomer:** Lacks any plane or center of symmetry ⇒ **Optically ACTIVE (chiral)**! Exists as d- and l-enantiomers.',
                "**3. [M(AA)b~2~c~2~]:** Cis-isomers are optically active; trans-isomers are optically inactive.",
                '**4. Square Planar Inactivity:** Square planar complexes possess a molecular plane of symmetry (the plane containing the metal and ligands) ⇒ **almost always optically INACTIVE** (rare exceptions occur with unsymmetrical bulky sterically hindered ligands).'
            ]),
            ("h2", "2. Master Isomer Counting Table (JEE Advanced Core)"),
            ("table", ["Complex Type", "Geometrical Isomers (GI)", "Optically Active Pairs (Enantiomers)", "Total Stereoisomers (GI + Enantiomeric excess)"], [
                ['[Ma~4~b~2~]', "2 (cis, trans)", "0 (both achiral)", "**2**"],
                ['[Ma~3~b~3~]', "2 (fac, mer)", "0 (both achiral)", "**2**"],
                ['[Ma~2~b~2~c~2~]', "5", "1 pair (all-cis is chiral)", "**6** (5 GI + 1 enantiomer)"],
                ['[Mabcdef]', "**15** (all distinct!)", "**15 pairs (all chiral!)**", "**30** (15 pairs of enantiomers)"],
                ['[M(AA)~3~]', "1", '1 pair (chiral Δ/Λ)', "**2**"],
                ['[M(AA)~2~b~2~]', "2 (cis, trans)", "1 pair (cis is chiral)", "**3** (trans + cis-d + cis-l)"],
                ['[M(AA)b~4~]', "1", "0", "**1**"]
            ], [20, 22, 28, 30], "Table 9.1 — Authoritative isomer counts for octahedral coordination complexes."),
            ("trap", 'EXAM TRAP: For [Co(en)~2~Cl~2~]^+^, the number of GEOMETRICAL isomers is 2 (cis, trans), but the TOTAL number of STEREOISOMERS is 3 (trans + d-cis + l-cis)!')
        ]
    },

    # ------------------------------------------------------------------ CC-10
    {
        "id": "CC-10",
        "title": "Bonding Theories: Sidgwick's EAN Rule & Valence Bond Theory (VBT)",
        "blocks": [
            ("lead", "**Effective Atomic Number & Orbital Hybridization Model** (NCERT §9.5.1)"),
            ("p", "Valence Bond Theory (VBT), developed by Linus Pauling, describes coordination bonding as the overlap of empty hybrid orbitals of the central metal with filled lone-pair orbitals of ligands."),
            ("h2", "1. Sidgwick's Effective Atomic Number (EAN) Rule"),
            ("p", "Sidgwick proposed that complex stability is maximized when the central metal attains the electronic configuration of the next noble gas (Kr = 36, Xe = 54, Rn = 86):\n"
                  '  **EAN** = Z - (Oxidation State) + 2 × (Coordination Number)\n'
                  '• In K~4~[Fe(CN)~6~]: EAN = 26 - (+2) + 2(6) = 24 + 12 = **36 (Kr)** ⇒ Obeys EAN rule.\n'
                  '• In [Ni(CO)~4~]: EAN = 28 - (0) + 2(4) = 28 + 8 = **36 (Kr)** ⇒ Obeys EAN rule.\n'
                  '• In [Cu(NH~3~)~4~]^2+^: EAN = 29 - (+2) + 2(4) = 27 + 8 = **35** ⇒ Violates EAN rule (stable nonetheless).'),
            ("h2", "2. Valence Bond Theory Postulates & Hybridization Types"),
            ("bul", [
                '**1. Empty Hybrid Orbitals:** Metal ion provides empty hybrid orbitals matching its CN: sp^3^ (Tetrahedral), dsp^2^ (Square Planar), d^2sp^3 (Inner Octahedral), sp^3d^2 (Outer Octahedral).',
                "**2. Inner vs Outer Orbital Complexes:**",
                '  - **Inner Orbital Complex (d^2sp^3):** Uses inner (n-1)d orbitals (3d). Requires pairing of unpaired d-electrons by strong field ligands ⇒ typically **low spin / diamagnetic**.',
                '  - **Outer Orbital Complex (sp^3d^2):** Uses outer nd orbitals (4d). Unpaired electrons remain unpaired in (n-1)d ⇒ typically **high spin / paramagnetic**.'
            ]),
            ("h2", "3. Five Standard VBT Worked Cases"),
            ("table", ["Complex Ion", "Config. / Metal OS", "Hybridization", "Geometry", 'Magnetic Property & Unpaired e^-^'], [
                ['[Fe(CN)~6~]^4−^', 'Fe^2+^ (3d^6^), strong CN^-^ pairs 3d', 'd^2sp^3', "Octahedral", '**Diamagnetic** (n = 0, μ = 0)'],
                ['[Fe(H~2~O)~6~]^2+^', 'Fe^2+^ (3d^6^), weak H~2~O no pairing', 'sp^3d^2', "Octahedral", '**Paramagnetic** (n = 4, μ = 4.90 BM)'],
                ['[Co(NH~3~)~6~]^3+^', 'Co^3+^ (3d^6^), strong NH~3~ pairs 3d', 'd^2sp^3', "Octahedral", '**Diamagnetic** (n = 0, μ = 0)'],
                ['[Ni(CN)~4~]^2−^', 'Ni^2+^ (3d^8^), strong CN^-^ pairs 3d', 'dsp^2^', "Square Planar", '**Diamagnetic** (n = 0, μ = 0)'],
                ['[NiCl~4~]^2−^', 'Ni^2+^ (3d^8^), weak Cl^-^ no pairing', 'sp^3^', "Tetrahedral", '**Paramagnetic** (n = 2, μ = 2.83 BM)']
            ], [18, 26, 14, 18, 24], "Table 10.1 — Classical VBT cases: hybridization, geometry, and magnetic properties."),
            ("trap", 'CRITICAL VBT FLAW: VBT cannot explain why [Co(NH~3~)~6~]^3+^ is diamagnetic with inner d^2sp^3 while [CoF~6~]^3−^ is paramagnetic with outer sp^3d^2! It cannot predict spectral absorption or color.')
        ]
    },

    # ------------------------------------------------------------------ CC-11
    {
        "id": "CC-11",
        "title": "Crystal Field Theory (CFT): Octahedral Splitting, CFSE & High/Low Spin",
        "blocks": [
            ("lead", "**Electrostatic Crystal Field & Degeneracy Breakdown** (NCERT §9.5.2)"),
            ("fig", "cft_octahedral", 'Fig. 11.1 — Octahedral (Δ~o~) and Tetrahedral (Δ~t~) crystal field splitting diagrams.'),
            ("h2", "1. Octahedral Splitting Mechanics & Pairing Criteria"),
            ("bul", [
                '**Axial Splitting:** 6 ligands approach along axes. **e~g~ Set (d~x²−y²~, d~z²~)** experiences direct axial repulsion ⇒ elevated by **+0.6 Δ~o~**. **t~2g~ Set (d~xy~, d~yz~, d~zx~)** avoids ligands ⇒ stabilized by **−0.4 Δ~o~**.',
                '**CFSE Formula:** **CFSE~oct~** = [ -0.4 n(t~2g~) + 0.6 n(e~g~) ] Δ~o~ + mP (P = pairing energy).',
                '**High Spin vs Low Spin:** Δ~o~ < P (weak field) ⇒ **High Spin** (t~2g~^3^ e~g~^1^). Δ~o~ > P (strong field) ⇒ **Low Spin** (t~2g~^4^ e~g~^0^, pairing favored).'
            ]),
            ("h2", "2. High-Spin vs Low-Spin Configurations & CFSE"),
            ("table", ["Config.", 'High Spin (t~2g~, e~g~)', "HS CFSE", "HS Unp.", 'Low Spin (t~2g~, e~g~)', "LS CFSE", "LS Unp."], [
                ["**d^4^**", 't~2g~^3^ e~g~^1^', '-0.6 Δ~o~', "4", 't~2g~^4^ e~g~^0^', '-1.6 Δ~o~ + P', "2"],
                ["**d^5^**", 't~2g~^3^ e~g~^2^', "**0.0** (Zero)", "5", 't~2g~^5^ e~g~^0^', '-2.0 Δ~o~ + 2P', "1"],
                ["**d^6^**", 't~2g~^4^ e~g~^2^', '-0.4 Δ~o~', "4", 't~2g~^6^ e~g~^0^', '**−2.4 Δ~o~ + 2P**', "**0 (Diamag)**"],
                ["**d^7^**", 't~2g~^5^ e~g~^2^', '-0.8 Δ~o~', "3", 't~2g~^6^ e~g~^1^', '-1.8 Δ~o~ + P', "1"]
            ], [12, 18, 14, 12, 18, 14, 12], "Table 11.1 — High-spin vs low-spin octahedral configurations and CFSE."),
            ("trap", 'CRITICAL TRAP: For d^8^, d^9^, d^10^, there is ONLY ONE configuration regardless of field: d^8^ is always t~2g~^6^ e~g~^2^ (n = 2), d^9^ is t~2g~^6^ e~g~^3^ (n = 1), and d^10^ is t~2g~^6^ e~g~^4^ (n = 0).')
        ]
    },
    # ------------------------------------------------------------------ CC-12
    {
        "id": "CC-12",
        "title": "CFT: Tetrahedral Splitting, The Spectrochemical Series & Factors Governing Δ",
        "blocks": [
            ("lead", "**Inverted Splitting & Factors Dictating Crystal Field Magnitude** (NCERT §9.5.2)"),
            ("p", "In tetrahedral complexes, four ligands approach from the corners of a cube containing the metal at its center, resulting in an inverted crystal field splitting pattern."),
            ("h2", '1. Tetrahedral Field Splitting (T~d~ Field)'),
            ("bul", [
                '**Inverted Orbitals:** Ligands approach along cube corners (between axes), directly closer to d~xy~, d~yz~, d~zx~ than to d~x²−y²~, d~z²~:',
                '  - **t~2~ Set (d~xy~, d~yz~, d~zx~):** Elevated by **+0.4 Δ~t~** above the barycentre.',
                '  - **e Set (d~x²−y²~, d~z²~):** Stabilized by **−0.6 Δ~t~** below the barycentre.',
                "  - Note: Subscript 'g' is omitted in tetrahedral complexes because a tetrahedron lacks an inversion center (i).",
                "**The Quantitative Relationship with Octahedral Field:**",
                '  **Δ~t~ = 4 / 9 Δ~o~** ≈ 0.44 Δ~o~',
                "  Because tetrahedral geometry has only 4 ligands (vs 6 in Oh) and none point directly at d-orbitals.",
                '**Consequence:** Since Δ~t~ is always much smaller than the pairing energy (Δ~t~ < P), **pairing NEVER occurs in tetrahedral complexes! ALL tetrahedral complexes are HIGH SPIN!**'
            ]),
            ("h2", "2. The Spectrochemical Series"),
            ("p", 'Experimentally determined order of ligands based on the increasing magnitude of crystal field splitting (Δ~o~) they produce:\n'
                  '  **I^-^ < Br^-^ < S^2−^ < SCN^-^ < Cl^-^ < N~3~^-^ < F^-^ < OH^-^ < C~2~O~4~^2−^ < H~2~O < NCS^-^ < edta^4−^ < NH~3~ < en < bpy < phen < NO~2~^-^ < PPh~3~ < CN^-^ < CO**\n'
                  '• **Weak Field Ligands (Halides, Oxygen donors):** Small Δ~o~, form high-spin complexes.\n'
                  '• **Strong Field Ligands (Nitrogen donors, Carbon donors):** Large Δ~o~, form low-spin complexes; **CO is the strongest field ligand** due to synergic π-backbonding!'),
            ("h2", "3. Four Factors Influencing the Magnitude of Δ"),
            ("bul", [
                '**1. Oxidation State of Metal:** Higher formal charge pulls ligands closer ⇒ larger repulsion: Δ~o~(M^3+^) > Δ~o~(M^2+^) by ≈50% (e.g. [Co(H~2~O)~6~]^3+^ is low-spin, but [Co(H~2~O)~6~]^2+^ is high-spin!).',
                '**2. Transition Series (3d vs 4d vs 5d):** Δ~o~ increases down the group by 30-50%: **5d > 4d > 3d** (diffuse orbitals interact more strongly). **All 4d and 5d complexes are LOW SPIN**, even with weak-field ligands like Cl^-^!',
                '**3. Geometry:** Δ~sp~ (1.74 Δ~o~) > Δ~o~ > Δ~t~ (0.44 Δ~o~).',
                '**4. Nature of Ligand:** Spectrochemical position dictated by σ-donation and π-acceptor ability.'
            ]),
            ("trap", 'HIGH-YIELD JEE TRAP: In [Co(ox)~3~]^3−^, oxalate is an oxygen-donor ligand, yet the complex is **diamagnetic and low spin**! Reason: Co^3+^ has high charge density, boosting Δ~o~ above P!')
        ]
    }
]
