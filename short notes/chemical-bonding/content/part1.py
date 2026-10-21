# -*- coding: utf-8 -*-
"""Chemical Bonding Part 1: Ionic Bond, Lattice Energy & Covalent Fundamentals (CB-01 to CB-08)."""

SHEETS = [
    # ------------------------------------------------------------------ CB-01
    {
        "id": "CB-01",
        "title": "Octet Rule, Lewis Structures, Formal Charge & Resonance",
        "blocks": [
            ("lead", "**Chemical Bonding Foundations** — Lewis Theory, Octet Limitations & Formal Charge"),
            ("p", "Atoms combine to achieve an inert gas electronic configuration ($ns^2 np^6$, octet) by sharing, losing, or gaining electrons. "
                  "Lewis structures account for valence electrons as bonding pairs and lone pairs."),
            ("h2", "1. Limitations & Failures of the Octet Rule"),
            ("table", ["Octet Exception Type", "Characteristics & Electron Count", "Classic Chemical Examples"], [
                ["Incomplete Octet (Hypovalent)", "Central atom has fewer than 8 valence electrons (electron-deficient)", "BeCl2 (4 e-), BF3 (6 e-), AlCl3 (6 e-), B2H6"],
                ["Expanded Octet (Hypervalent)", "Central atom expands coordination using vacant d-orbitals (> 8 e-)", "PCl5 (10 e-), SF6 (12 e-), IF7 (14 e-), H2SO4 (12 e-)"],
                ["Odd-Electron Molecules", "Unpaired electron present; paramagnetic in gas phase", "NO (11 valence e-), NO2 (17 valence e-), ClO2 (19 e-)"],
                ["Noble Gas Compounds", "Heavier noble gases form covalent bonds despite full octet", "XeF2, XeF4, XeF6, XeO3, KrF2"],
            ], [25, 35, 40], "Table 1.1 — Systematic classification of octet rule violations."),
            ("h2", "2. Formal Charge Calculation"),
            ("key", "**Formal Charge (FC)** on an atom in a Lewis formula:\n"
                    "$$\\text{FC} = V - L - \\frac{1}{2} S$$\n"
                    "where $V$ = valence electrons in free neutral atom, $L$ = non-bonding lone pair electrons, $S$ = shared bonding electrons.\n"
                    "• The most stable Lewis structure is the one where formal charges are closest to zero, and negative formal charges reside on the most electronegative atoms."),
            ("h2", "3. Resonance & Resonance Energy"),
            ("p", "When a single Lewis structure cannot describe the observed properties of a molecule (e.g. equal bond lengths in CO3^2-, O3, benzene), "
                  "the actual molecule is represented as a **resonance hybrid** of canonical contributing structures:\n"
                  "• All canonical forms must have identical atomic positions (differ only in electron distribution) and equal unpaired electrons.\n"
                  "• **Resonance Energy** = Experimental Heat of Formation - Calculated Heat of most stable canonical form (stabilises the molecule)."),
        ],
    },
    # ------------------------------------------------------------------ CB-02
    {
        "id": "CB-02",
        "title": "The Ionic Bond: Born-Haber Cycle, Lattice Energy & Hydration",
        "blocks": [
            ("lead", "**The Ionic Bond** — Electrostatic Formation, Born-Haber Thermodynamics & Solvation"),
            ("p", "Formed by complete transfer of electrons between elements of low ionization energy (metals) and high electron affinity (non-metals). "
                  "Ionic compounds do not exist as discrete molecules, but as infinite crystalline 3D lattices held by nondirectional Coulombic forces."),
            ("h2", "1. Lattice Energy (U) & Born-Landé Equation"),
            ("p", "Lattice energy is the energy released when 1 mole of crystalline ionic solid is formed from isolated gaseous ions:\n"
                  "$$M^+(g) + X^-(g) \\rightarrow MX(s) + U$$\n"
                  "Governed by the **Born-Landé Equation**: $U \\propto \\frac{|z_+ z_-|}{r_+ + r_-}$."),
            ("fig", "bornhaber", "Fig. 1.1 — Born-Haber thermochemical cycle for Sodium Chloride NaCl."),
            ("key", "Lattice Energy Dependencies:\n"
                    "• **Charge Product ($|z_+ z_-|$):** Dominant factor! E.g. $U(\\text{MgO}) \\approx 4 \\times U(\\text{NaCl})$ because $(+2)(-2) = 4$ vs $(+1)(-1) = 1$.\n"
                    "• **Interionic Distance ($r_+ + r_-$):** $U(\\text{LiF}) > U(\\text{LiCl}) > U(\\text{LiBr}) > U(\\text{LiI})$."),
            ("h2", "2. Enthalpy of Solution & Hydration Energy"),
            ("p", "When an ionic solid dissolves in water:\n"
                  "$$\\Delta H_{\\text{solution}} = \\text{Lattice Energy } (U) + \\Delta H_{\\text{hydration}}$$\n"
                  "• For dissolution to be spontaneous ($\Delta G < 0$), either **$|\\Delta H_{\\text{hyd}}| > U$** (exothermic), or entropy of dissolution ($T\\Delta S$) overcomes small positive $\Delta H$.\n"
                  "• If Lattice Energy greatly exceeds Hydration Energy (e.g. BaSO4, CaF2), the compound is **insoluble in water**!"),
        ],
    },
    # ------------------------------------------------------------------ CB-03
    {
        "id": "CB-03",
        "title": "Fajans' Rules: Covalent Character in Ionic Compounds",
        "blocks": [
            ("lead", "**Fajans' Rules** — Polarization, Polarizability & Covalent Character"),
            ("p", "No ionic bond is 100% ionic. When a small cation approaches a large electron-rich anion, its positive field "
                  "attracts the anion's electron cloud and repels its nucleus, distorting the electron cloud towards the inter-nuclear region."),
            ("fig", "fajans", "Fig. 1.2 — Polarization of an anion cloud by a polarizing cation leading to covalent character."),
            ("h2", "1. Fajans' Four Guiding Principles"),
            ("table", ["Factor", "Condition Favoring Polarization (Covalency)", "Underlying Physical Rationale"], [
                ["1. Cation Size", "**Small cation** (High charge density $\\phi = z/r$)", "Small cation concentrates positive field, exerting intense electrostatic pull on anion cloud (e.g. LiCl is more covalent than KCl)"],
                ["2. Anion Size", "**Large anion** (High polarizability)", "Outer valence electrons in large anion are loosely held by nucleus and easily deformed (e.g. AgI is far more covalent than AgF)"],
                ["3. Ionic Charge", "**High charge on Cation or Anion**", "Higher positive charge increases pull; higher negative charge makes anion more easily polarizable: SnCl4 (covalent liquid) vs SnCl2 (ionic solid)"],
                ["4. Electronic Config.", "**Pseudo-Noble Gas Cation ($ns^2 np^6 nd^{10}$)**", "Cations with 18-electron shell (Cu+, Ag+, Zn2+, Cd2+) have poor d-electron shielding -> higher effective $Z_{\\text{eff}}$ than noble gas cations (Na+, K+) of similar size! AgCl is covalent/insoluble, NaCl is ionic/soluble!"],
            ], [20, 38, 42], "Table 1.2 — The four Fajans' rules governing covalent character."),
            ("h2", "2. Physical Consequences of Polarization in JEE"),
            ("bul", [
                "**Melting Point Order:** Increased covalency lowers melting points: **NaCl (801°C) > MgCl2 (714°C) > AlCl3 (sublimes 180°C)**; **CaF2 > CaCl2 > CaBr2 > CaI2**.",
                "**Solubility in Water:** Covalency reduces solubility in polar water and increases solubility in organic solvents (LiCl soluble in alcohol/acetone, NaCl insoluble).",
                "**Intensity of Colour:** Extensive polarization shifts charge-transfer absorption into the visible spectrum: **AgF (white) -> AgCl (white) -> AgBr (pale yellow) -> AgI (deep yellow)**; **PbO (yellow) vs PbS (black)**.",
            ]),
        ],
    },
    # ------------------------------------------------------------------ CB-04
    {
        "id": "CB-04",
        "title": "Solubility & Thermal Stability Trends of Ionic Salts",
        "blocks": [
            ("lead", "**Solubility & Thermal Stability** — Polyatomic Anions & Decomposition Patterns"),
            ("p", "The thermal stability and aqueous solubility of ionic compounds containing polyatomic oxyanions (CO3^2-, SO4^2-, NO3^-, OH^-) "
                  "follow clear thermodynamic principles governed by cation size and lattice energy."),
            ("h2", "1. Thermal Stability of Carbonates & Nitrates"),
            ("p", "Thermal decomposition of oxy-salts is driven by the difference in lattice energy between the salt and the product oxide:\n"
                  "$$MCO_3(s) \\xrightarrow{\\Delta} MO(s) + CO_2(g)$$\n"
                  "• A small, highly polarizing cation polarizes an adjacent oxygen atom in CO3^2-, weakening the C-O bond and facilitating decomposition into MO + CO2 at lower temperatures!"),
            ("table", ["Oxy-Salt Family", "Thermal Stability Order Down Group 1 / 2", "Decomposition Reaction & Products"], [
                ["Group 2 Carbonates", "**BeCO3 < MgCO3 < CaCO3 < SrCO3 < BaCO3**", "MCO3 --(Δ)--> MO + CO2 (BaCO3 requires red heat >1300°C)"],
                ["Group 1 Carbonates", "**Li2CO3 decomposes; others (Na to Cs) DO NOT decompose!**", "Li2CO3 --(Δ)--> Li2O + CO2 (Li+ is small like Mg2+, diagonal relationship). Na2CO3 melts without decomposing!"],
                ["Group 2 Nitrates", "**Be(NO3)2 < Mg(NO3)2 < Ca(NO3)2 < Ba(NO3)2**", "2 M(NO3)2 --(Δ)--> **2 MO + 4 NO2↑ (brown) + O2↑**"],
                ["Group 1 Nitrates", "**Decompose to Nitrites (except Li!)**", "2 NaNO3 --(Δ)--> **2 NaNO2 + O2↑** (No NO2!)\n4 LiNO3 --(Δ)--> **2 Li2O + 4 NO2↑ + O2↑** (Behaves like Mg!)"],
            ], [20, 42, 38], "Table 1.3 — Thermal stability and decomposition pathways of oxyanion salts."),
            ("h2", "2. Solubility Trends: Small vs Bulky Anions"),
            ("bul", [
                "**Rule 1 (Bulky Polyatomic Anions: SO4^2-, CO3^2-, CrO4^2-):** Lattice energy changes very little down the group because $r_-$ is huge ($r_+ + r_- \\approx r_-$). Therefore, **hydration energy dominates**! Since hydration energy decreases rapidly with cation size, **solubility DECREASES down the group**:\n"
                "  **BeSO4 > MgSO4 > CaSO4 > SrSO4 > BaSO4 (insoluble!)**.",
                "**Rule 2 (Small Monatomic Anions: OH^-, F^-):** Lattice energy drops more steeply than hydration energy as cation radius increases. Therefore, **solubility INCREASES down the group**:\n"
                "  **Be(OH)2 < Mg(OH)2 < Ca(OH)2 < Sr(OH)2 < Ba(OH)2**.",
            ]),
        ],
    },
    # ------------------------------------------------------------------ CB-05
    {
        "id": "CB-05",
        "title": "Valence Bond Theory: Overlap, Sigma & Pi Bonds",
        "blocks": [
            ("lead", "**Valence Bond Theory (VBT)** — Orbital Overlap, Directional Bonding & Bond Strengths"),
            ("p", "Developed by Heitler and London, extended by Pauling and Slater. A covalent bond is formed by the pairing of "
                  "spins of electrons in two overlapping half-filled atomic orbitals. Greater overlap = stronger bond!"),
            ("h2", "1. Sigma (σ) vs Pi (π) Bonds"),
            ("table", ["Feature", "Sigma (σ) Bond", "Pi (π) Bond"], [
                ["Mode of Overlap", "**End-to-end / Axial / Head-on** along inter-nuclear axis", "**Sideways / Lateral / Parallel** overlap perpendicular to axis"],
                ["Types of Overlapping Orbitals", "s-s, s-p_z, p_z-p_z, hybrid-hybrid (sp^n-sp^n)", "p_x-p_x, p_y-p_y, d_xy-p_y, d-d lateral"],
                ["Extent of Overlap & Strength", "**Greater overlap -> Strong bond**", "**Lesser overlap -> Weaker bond**"],
                ["Electron Cloud Geometry", "Cylindrically symmetrical about inter-nuclear axis", "Two sausage-like lobes above and below nodal plane"],
                ["Rotation Around Bond", "**Free rotation** permitted without breaking overlap", "**Restricted rotation** (twisting destroys overlap -> stereoisomerism!)"],
                ["Independent Existence", "Can exist independently (single bonds are always σ)", "Never exists alone; formed only after a σ-bond is established"],
            ], [20, 40, 40], "Table 1.4 — Comprehensive structural contrast between σ and π bonds."),
            ("h2", "2. Strength Order of Orbital Overlaps"),
            ("key", "For same principal quantum number $n$:\n"
                    "• Axial: **p-p (axial) > s-p > s-s** (p-orbitals are directional, concentrating electron density along bond axis; s-orbitals are spherical and diffuse).\n"
                    "• With differing shell $n$:\n"
                    "  **1s-1s > 1s-2p > 2s-2p > 2p-2p > 3p-3p** (smaller orbitals overlap closer to nuclei, releasing higher bond energy!)."),
            ("h2", "3. Maximum Overlap Principle & Bond Angles"),
            ("p", "Pure p-orbitals are oriented at 90° to each other (p_x, p_y, p_z). If bonding occurred via pure p-orbitals without "
                  "hybridization, bond angles in CH4, NH3, H2O would all be 90°. The observed angles (109.5°, 107.8°, 104.5°) "
                  "necessitate the concept of **hybridization**."),
        ],
    },
    # ------------------------------------------------------------------ CB-06
    {
        "id": "CB-06",
        "title": "Hybridization Master Rules: sp, sp2, sp3, sp3d, sp3d2, sp3d3",
        "blocks": [
            ("lead", "**Hybridization Theory** — Steric Number, Geometry & Percentage s-Character"),
            ("p", "Hybridization is the mathematical mixing of atomic orbitals of comparable energy on the same atom to form "
                  "an equal number of new equivalent **hybrid orbitals** having definite directional orientations in space."),
            ("h2", "1. Steric Number Rule for Hybridization"),
            ("key", "$$\\text{Steric Number (SN)} = \\text{Number of } \\sigma\\text{-bonds} + \\text{Number of lone pairs on central atom}$$\n"
                    "• SN = 2 -> **sp** (Linear, 180°)\n"
                    "• SN = 3 -> **sp^2** (Trigonal planar, 120°)\n"
                    "• SN = 4 -> **sp^3** (Tetrahedral, 109°28')\n"
                    "• SN = 5 -> **sp^3d** (Trigonal bipyramidal, axial + equatorial)\n"
                    "• SN = 6 -> **sp^3d^2** (Octahedral, 90°)\n"
                    "• SN = 7 -> **sp^3d^3** (Pentagonal bipyramidal, 72° and 90°)"),
            ("h2", "2. Specific d-Orbitals Involved in Hybridization (Critical JEE Advanced Topic)"),
            ("table", ["Hybridization", "Ideal Geometry", "Specific d-Orbitals Used", "Why this d-orbital?"], [
                ["sp^3d", "Trigonal bipyramidal (TBP)", "**d_{z^2}** (axial bonds lie on z-axis)", "d_{z^2} has maximum electron density along z-axis, forming 2 linear axial bonds"],
                ["dsp^2", "Square planar", "**d_{x^2-y^2}**", "Lobes point directly along x and y Cartesian axes to meet ligands"],
                ["sp^3d^2 / d^2sp^3", "Octahedral", "**d_{x^2-y^2} and d_{z^2}**", "Both e_g orbitals point along Cartesian axes where 6 ligands approach"],
                ["sp^3d^3", "Pentagonal bipyramidal", "**d_{z^2}, d_{x^2-y^2}, d_{xy}**", "d_{z^2} forms 2 axial bonds; d_{x^2-y^2} and d_{xy} lie in xy-equatorial plane"],
            ], [18, 26, 26, 30], "Table 1.5 — Exact d-orbital participation in higher hybrid states."),
            ("h2", "3. Influence of Percentage s-Character"),
            ("p", "As percentage s-character increases: $sp^3 (25\\%) < sp^2 (33.3\\%) < sp (50\\%)$:\n"
                  "• **Electronegativity:** $sp > sp^2 > sp^3$ (s-electrons are held closer to nucleus).\n"
                  "• **Bond Angle:** $sp (180°) > sp^2 (120°) > sp^3 (109.5°)$.\n"
                  "• **Bond Length:** $sp-sp < sp^2-sp^2 < sp^3-sp^3$.\n"
                  "• **Bond Strength:** $sp-sp > sp^2-sp^2 > sp^3-sp^3$."),
        ],
    },
    # ------------------------------------------------------------------ CB-07
    {
        "id": "CB-07",
        "title": "Bent's Rule & Energetic Partitioning of Orbitals",
        "blocks": [
            ("lead", "**Bent's Rule** — Electronegativity & Hybrid Orbital s/p Character Partitioning"),
            ("p", "In molecules with non-equivalent hybrid orbitals (e.g. sp^3d or unsymmetrically substituted sp^3), "
                  "the s- and p-character are not distributed equally among all bonds."),
            ("key", "**Bent's Rule Formulation:**\n"
                    "\"More electronegative substituents prefer hybrid orbitals having **LESS s-character** (more p-character), "
                    "whereas more electropositive substituents and lone pairs prefer hybrid orbitals having **MORE s-character**.\""),
            ("h2", "1. Application to Trigonal Bipyramidal (sp^3d) Systems"),
            ("p", "sp^3d hybridization is partitioned into two independent sets:\n"
                  "• **Equatorial Set:** $sp^2$ hybridized (33.3% s-character, planar 120°).\n"
                  "• **Axial Set:** $pd_{z^2}$ hybridized (**0% s-character**, linear 180° along z-axis)."),
            ("table", ["Substituent / Group", "Preferred Position in sp^3d", "Direct Chemical Consequence in PCl3F2 / SF4"], [
                ["Lone Pairs", "**Equatorial** (maximum s-character)", "In SF4, lone pair occupies equatorial position (See-Saw shape). In ClF3, 2 lone pairs are equatorial (T-shaped). In XeF2, 3 lone pairs are equatorial (Linear)."],
                ["Electronegative Atoms (F)", "**Axial** (minimum s-character)", "In PCl3F2, both Fluorine atoms go strictly to **axial** positions! Molecule is non-polar (μ = 0)."],
                ["Less Electronegative / Bulky (CH3, Cl)", "**Equatorial** (higher s-character)", "In P(CH3)2F3, both CH3 groups occupy equatorial sites."],
            ], [25, 25, 50], "Table 1.6 — Applications of Bent's Rule in sp3d stereochemistry."),
            ("h2", "2. Bond Angle Modifications in sp^3 Molecules"),
            ("bul", [
                "**CH2F2 vs CH4:** In CH2F2, the electronegative F atoms pull p-character into the C-F bonds. Consequently, the C-H bonds gain extra s-character, causing the **H-C-H bond angle to EXPAND (>109.5°)** and the **F-C-F bond angle to CONTRACT (<109.5°)**!",
                "**Bond Length Effect:** Higher s-character shortens the bond: C-H bond in CH2F2 is shorter and stronger than in CH4.",
            ]),
        ],
    },
    # ------------------------------------------------------------------ CB-08
    {
        "id": "CB-08",
        "title": "Drago's Rule & Non-Hybridization in Heavy Hydrides",
        "blocks": [
            ("lead", "**Drago's Rule** — Ineffective Hybridization in Heavier Period 3+ Hydrides"),
            ("p", "Why are the bond angles in PH3, AsH3, H2S, H2Se all close to 90°, while NH3 is 107.8° and H2O is 104.5°? "
                  "Drago's rule provides the thermodynamic explanation."),
            ("key", "**Drago's Rule Conditions:**\n"
                    "Hybridization does **NOT take place** if all three conditions are satisfied:\n"
                    "1. The central atom belongs to **Period 3 or below** (P, As, Sb, Bi, S, Se, Te).\n"
                    "2. The central atom has at least **one non-bonding lone pair**.\n"
                    "3. The attached terminal atoms have electronegativity **$\\chi \\le 2.1$** (e.g. Hydrogen, $\\chi_H = 2.1$)."),
            ("h2", "1. Bond Angle Comparison: Period 2 vs Periods 3–5"),
            ("table", ["Group 15 Hydride", "Bond Angle", "Group 16 Hydride", "Bond Angle", "Stereochemical Status"], [
                ["NH3", "**107.8°**", "H2O", "**104.5°**", "Normal sp^3 hybridization with lone pair repulsions"],
                ["PH3", "**93.5°**", "H2S", "**92.1°**", "Drago system: No hybridization, pure p-orbital bonds"],
                ["AsH3", "**91.8°**", "H2Se", "**91.0°**", "Pure p-orbital overlap (angle approaches 90°)"],
                ["SbH3", "**91.3°**", "H2Te", "**89.5°**", "Pure p-orbital overlap (angle approaches 90°)"],
            ], [18, 16, 18, 16, 32], "Table 1.7 — Sharp bond angle drop illustrating Drago's rule."),
            ("h2", "2. Chemical Consequences of Drago's Rule"),
            ("bul", [
                "**Lone Pair Nature:** In PH3 and H2S, the lone pair resides in an **almost pure unhybridized s-orbital** (spherical, close to nucleus, high s-character).",
                "**Lewis Basicity:** NH3 is a strong Lewis base because its lone pair is in an $sp^3$ directional orbital pointing outwards. PH3 is an **extremely poor Lewis base** because its s-orbital lone pair is tightly held and nondirectional!",
                "**Proton Affinity:** PH3 does not protonate easily; PH4^+ exists only with conjugate bases of superacids (PH4I), whereas NH4^+ salts are ubiquitous.",
            ]),
        ],
    },
]
