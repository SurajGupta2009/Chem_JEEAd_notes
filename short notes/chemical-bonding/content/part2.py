# -*- coding: utf-8 -*-\n"""Chemical Bonding Part 2: VSEPR Geometries, Back-Bonding, Bridge Bonds & MOT (CB-09 to CB-16)."""

SHEETS = [
    # ------------------------------------------------------------------ CB-09
    {
        "id": "CB-09",
        "title": "VSEPR Theory: Electron Pair Repulsions & Molecular Geometries",
        "blocks": [
            ("lead", "**VSEPR Theory** — Gillespie-Nyholm Electron Pair Repulsions & Molecular Geometries"),
            ("p", "Valence Shell Electron Pair Repulsion (VSEPR) predicts molecular geometry by minimizing electrostatic "
                  "repulsions between electron pairs (bonding pairs and lone pairs) surrounding the central atom."),
            ("key", "**Repulsion Hierarchy:**\n"
                    "**lp − lp > lp − bp > bp − bp**\n"
                    "• Lone pairs occupy more space because they are attracted by only one positive nucleus, whereas bond pairs are shared between two nuclei."),
            ("fig", "vsepr", "Fig. 2.1 — Key distorted VSEPR geometries: Bent (H2O), Pyramidal (NH3), See-Saw (SF4), T-Shaped (ClF3)."),
            ("h2", "1. Comprehensive VSEPR Geometries Table"),
            ("table", ["Type", "Formula", "Bond Pairs", "Lone Pairs", "Electron Geometry", "Observed Molecular Shape", "Examples"], [
                ["AB2", "BeCl2", "2", "0", "Linear", "**Linear** (180°)", "BeF2, CO2, HCN, CS2"],
                ["AB2E", "SO2", "2", "1", "Trigonal planar", "**Bent / V-shaped** (<120°)", "SO2, O3, NO2^-, SnCl2(g)"],
                ["AB3", "BF3", "3", "0", "Trigonal planar", "**Trigonal planar** (120°)", "BF3, BCl3, SO3, NO3^-"],
                ["AB4", "CH4", "4", "0", "Tetrahedral", "**Tetrahedral** (109.5°)", "CH4, CCl4, SiF4, NH4^+, SO4^2-"],
                ["AB3E", "NH3", "3", "1", "Tetrahedral", "**Trigonal pyramidal** (107.8°)", "NH3, PCl3, H3O^+, ClO3^-"],
                ["AB2E2", "H2O", "2", "2", "Tetrahedral", "**Bent / V-shaped** (104.5°)", "H2O, OF2, SCl2, ClO2^-"],
                ["AB5", "PCl5", "5", "0", "Trigonal bipyramidal", "**Trigonal bipyramidal**", "PCl5, PF5, AsF5"],
                ["AB4E", "SF4", "4", "1", "Trigonal bipyramidal", "**See-Saw** (1 lp eq)", "SF4, SeF4, TeCl4"],
                ["AB3E2", "ClF3", "3", "2", "Trigonal bipyramidal", "**T-Shaped** (2 lp eq)", "ClF3, BrF3, ICl3"],
                ["AB2E3", "XeF2", "2", "3", "Trigonal bipyramidal", "**Linear** (3 lp eq, 180°)", "XeF2, I3^-, ICl2^-"],
                ["AB6", "SF6", "6", "0", "Octahedral", "**Regular Octahedral** (90°)", "SF6, SeF6, [PF6]^-"],
                ["AB5E", "BrF5", "5", "1", "Octahedral", "**Square Pyramidal**", "BrF5, IF5, XeOF4"],
                ["AB4E2", "XeF4", "4", "2", "Octahedral", "**Square Planar** (2 lp ax)", "XeF4, [ICl4]^-"],
                ["AB7", "IF7", "7", "0", "Pentagonal bipyramidal", "**Pentagonal bipyramidal**", "IF7 (72° eq, 90° ax)"],
                ["AB6E", "XeF6", "6", "1", "Pentagonal bipyramidal", "**Distorted Octahedral**", "XeF6 (fluxional lp)"],
            ], [8, 8, 8, 8, 20, 24, 24], "Table 2.1 — Master compendium of VSEPR molecular geometries."),
        ],
    },
    # ------------------------------------------------------------------ CB-10
    {
        "id": "CB-10",
        "title": "Bond Parameters: Order, Length, Energy & Angle Influences",
        "blocks": [
            ("lead", "**Bond Parameters** — Energetics, Radii, Resonance & Angle Determinants"),
            ("p", "A covalent bond is characterized by four interrelated quantitative parameters: "
                  "Bond Order, Bond Length, Bond Dissociation Enthalpy, and Bond Angle."),
            ("h2", "1. Bond Order vs Length vs Dissociation Enthalpy"),
            ("key", "General Interrelationships:\n"
                    "• **Bond Order ∝ Bond Strength ∝ Force Constant ∝ Bond Energy**\n"
                    "• **Bond Order ∝ 1 / (Bond Length)**\n"
                    "• E.g. Carbon-Carbon bonds: C-C (154 pm, 348 kJ) -> C=C (134 pm, 614 kJ) -> C≡ C (120 pm, 839 kJ)."),
            ("h2", "2. Master Rules Governing Bond Angles in Chemistry"),
            ("table", ["Determinant Factor", "Governing Rule / Trend", "Classic Comparative Examples"], [
                ["1. Hybridization State", "Higher s-character opens the angle: sp (180°) > sp^2^^ (120°) > sp^3^^ (109.5°)", "BeCl2 (180°) > BCl3 (120°) > CH4 (109.5°)"],
                ["2. Number of Lone Pairs", "Each additional lone pair compresses bond angle by ~2° to 2.5°", "CH4 (0 lp, 109.5°) > NH3 (1 lp, 107.8°) > H2O (2 lp, 104.5°)"],
                ["3. Central Atom Electronegativity (Same Halogen/Terminal)", "When terminal atoms are identical, **higher central atom EN increases bond angle** (electron pairs pulled closer to center -> greater mutual repulsion)", "NH3 (107.8°) > PH3 (93.5°) > AsH3 (91.8°)nH2O (104.5°) > H2S (92.1°) > H2Se (91.0°)"],
                ["4. Terminal Atom Electronegativity (Same Central Atom)", "When central atom is identical, **higher terminal atom EN decreases bond angle** (electron pairs pulled away from center -> lesser mutual repulsion)", "PI3 (102°) > PBr3 (101.5°) > PCl3 (100°) > PF3 (97.8°)nOF2 (103.2°) < H2O (104.5°) < Cl2O (111°!)"],
                ["5. Steric Crowding of Bulky Groups", "Bulky ligands force angles wide open to relieve van der Waals clash", "O(CH3)2 (111.7°) > H2O (104.5°); O(SiH3)2 (144°!)"],
            ], [22, 38, 40], "Table 2.2 — Systematic hierarchy determining bond angle variations."),
        ],
    },
    # ------------------------------------------------------------------ CB-11
    {
        "id": "CB-11",
        "title": "Dipole Moment: Vector Addition, Percentage Ionic Character & Symmetry",
        "blocks": [
            ("lead", "**Dipole Moment (μ)** — Polar Bonds, Molecular Geometry & % Ionic Character"),
            ("p", "A bond between two atoms of different electronegativity is polar. The electric dipole moment measures "
                  "the extent of charge separation: {μ} = q × d (units: Debye, 1 D = 3.33564 × 10^-30 C·m)."),
            ("h2", "1. Molecular Dipole Moment as a Vector Sum"),
            ("fig", "dipole", "Fig. 2.2 — Dipole moment vector analysis: NH3 vs NF3 and planar symmetrical cancellation."),
            ("p", "Molecular dipole moment is the **vector resultant** of all individual bond dipole moments and lone pair moments:\n"
                  "**μ_{net} = √{μ~1~^2 + μ~2~^2 + 2μ~1~μ~2~ cos θ}**\n"
                  "• Symmetrical molecules with identical surrounding atoms have **μ = 0** (vectors cancel): "
                  "Linear (CO2, BeF2), Trigonal planar (BF3), Tetrahedral (CCl4, CH4), Octahedral (SF6), Square planar (XeF4)."),
            ("h2", "2. The Classic NH3 vs NF3 Comparison (JEE Favorite)"),
            ("table", ["Feature", "Ammonia (NH3)", "Nitrogen Trifluoride (NF3)"], [
                ["Individual Bond Dipoles", "N is more EN than H: N^δ- <--- H^δ+ (bond moments point **TOWARDS** N)", "F is more EN than N: N^δ+ ---> F^δ- (bond moments point **AWAY** from N)"],
                ["Lone Pair Dipole Direction", "Lone pair points upwards away from N nucleus", "Lone pair points upwards away from N nucleus"],
                ["Vector Resultant", "**Additive:** Orbital dipole and 3 N-H bond dipoles reinforce in the same direction!", "**Subtractive:** Lone pair dipole opposes the resultant of the 3 N-F bond dipoles!"],
                ["Experimental Net Dipole (μ)", "**1.47 D (High)**", "**0.24 D (Very Low!)**"],
            ], [20, 40, 40], "Table 2.3 — Why Ammonia has a six-fold higher dipole moment than Nitrogen Trifluoride."),
            ("h2", "3. Percentage Ionic Character (Hannay-Smith Equation)"),
            ("key", "**% Ionic Character = 16 |χ~A~ - χ~B~| + 3.5 (χ~A~ - χ~B~)^2**\n"
                    "Alternatively, from dipole measurements:\n"
                    "**%% Ionic Character = {μ_obs}{μ_calc} × 100%**"),
        ],
    },
    # ------------------------------------------------------------------ CB-12
    {
        "id": "CB-12",
        "title": "Back-Bonding: pπ-pπ, pπ-dπ, Lewis Acidity & Geometry Changes",
        "blocks": [
            ("lead", "**Back-Bonding (Dative π-Bonding)** — Lewis Acidity & Structural Reorganisation"),
            ("p", "Back-bonding is an internal coordinate π-bond formed when a filled p-orbital of a donor atom (with lone pairs) "
                  "overlaps sideways with a vacant unhybridized p- or d-orbital on an adjacent electron-deficient acceptor atom."),
            ("h2", "1. Types of Back-Bonding"),
            ("fig", "backbonding", "Fig. 2.3 — Dative back-bonding: BF3 pπ-pπ backbond and N(SiH3)3 planarization via pπ-dπ."),
            ("table", ["Type of Back-Bonding", "Orbital Interaction", "Key Chemical Examples", "Major Observed Consequences"], [
                ["pπ - pπ Back-Bonding", "Filled 2p (donor) -> Empty 2p (acceptor)", "BF3, B(OMe)3, B3N3H6", "B-F bond length drops to 130 pm (partial double bond); Inversion of BX3 Lewis acidity: **BF3 < BCl3 < BBr3 < BI3**"],
                ["pπ - dπ Back-Bonding", "Filled 2p (donor) -> Empty 3d (acceptor)", "N(SiH3)3, O(SiH3)2, P4O10, SO2, SO3", "Planarization of amine, drastic decrease in basicity, bond angle widening"],
            ], [20, 26, 24, 30], "Table 2.4 — Classification and manifestations of back-bonding."),
            ("h2", "2. Trimethylamine N(CH3)3 vs Trisilylamine N(SiH3)3 (Classic JEE Topic)"),
            ("table", ["Property", "Trimethylamine N(CH3)3", "Trisilylamine N(SiH3)3"], [
                ["Geometry around N", "**Trigonal Pyramidal** (sp^3^ N)", "**Planar Trigonal** (sp^2^ N)"],
                ["Back-Bonding", "**None** (Carbon has no empty d-orbitals)", "**Extensive 2pπ(N) -> 3dπ(Si) back-bonding**"],
                ["Hybridization of N", "sp^3^ (lone pair resides in hybrid orbital)", "sp^2^ (lone pair delocalised into 3d orbitals of 3 Si atoms)"],
                ["Lewis Basicity", "**Strong Lewis base** (donates available lone pair)", "**Weak / Non-basic** (lone pair is delocalised and unavailable)"],
                ["Adduct with BMe3", "Forms stable adduct Me3N:BMe3", "Does not form adduct (sterically and electronically inert)"],
            ], [20, 40, 40], "Table 2.5 — Structural contrast caused by pπ-dπ back-bonding."),
            ("key", "Inversion of Lewis Acidity in Boron Trihalides:\n"
                    "**BF3 < BCl3 < BBr3 < BI3**.\n"
                    "Reason: 2p(B) <--- 2p(F) overlap is optimal (same size and energy), satisfying B's electron deficiency. "
                    "In BI3, 2p(B) <--- 5p(I) overlap is ineffective due to size/energy mismatch, leaving B completely hungry for external electron pairs!"),
        ],
    },
    # ------------------------------------------------------------------ CB-13
    {
        "id": "CB-13",
        "title": "Bridge Bonding: 3c-2e Banana Bonds vs 3c-4e Halogen Bridges",
        "blocks": [
            ("lead", "**Bridge Bonding (Multicentre Bonds)** — 3c-2e Banana Bonds vs 3c-4e Halide Bridges"),
            ("p", "When monomeric molecules have incomplete octets (electron-deficient) and cannot satisfy them by back-bonding, "
                  "they dimerise or polymerise through multicentre bridging bonds."),
            ("h2", "1. 3c-2e 'Banana' Bonds (Electron-Deficient Bridges)"),
            ("fig", "diborane", "Fig. 2.4 — Bridge bonding modes: Diborane B2H6 3c-2e banana bond vs Al2Cl6 3c-4e dative bridge."),
            ("bul", [
                "**Diborane (B2H6):** Two B atoms and four terminal H atoms are coplanar. Two bridging H atoms lie above and below this plane.\n"
                "  Each B-Hb-B bridge is a **3-centre 2-electron (3c-2e)** bond sharing 2 electrons over 3 nuclei (B, H, B).\n"
                "  Each Boron atom is **sp^3^ hybridized** (12 valence electrons total).",
                "**Beryllium Hydride (BeH2)_n:** Solid (BeH2)_n forms an infinite chain of Be atoms joined by 3c-2e Be-H-Be bridges (Be is sp^3^ hybridized).",
                "**Aluminium Alkyls [Al(CH3)3]2:** Dimerises via **3c-2e Al-C-Al bridges** where the methyl carbon uses an sp^3^ orbital to bridge two Al atoms.",
            ]),
            ("table", ["Feature", "3c-2e Bridge (e.g. B2H6, [AlMe3]2)", "3c-4e Bridge (e.g. Al2Cl6, I2Cl6)"], [
                ["Bridging Atom", "Hydrogen (H) or Methyl (CH3) without lone pairs", "Halogen (Cl, Br, I) having lone pairs"],
                ["Total Electrons in Bridge", "**2 electrons** (electron-deficient 'banana' bond)", "**4 electrons** (1 normal covalent bond + 1 dative coordinate bond)"],
                ["Lewis Acidity of Dimer", "Still somewhat electron-deficient (cleaved by Lewis bases)", "Octet of central metal is completely satisfied"],
                ["Bond Order of Bridge", "0.5 per bridge link (weaker than terminal)", "1.0 per coordinate/covalent bond"],
            ], [20, 40, 40], "Table 2.6 — Comparison between 3c-2e and 3c-4e bridging architectures."),
            ("h2", "2. 3c-4e Halogen Bridges (Al2Cl6, BeCl2)"),
            ("p", "In **Al2Cl6**, each bridging chlorine atom donates a lone pair into the empty 3p/3d orbital of the adjacent Al atom. "
                  "Each Al atom achieves an octet through two terminal covalent bonds and two bridging (one covalent, one dative) bonds (sp^3^ Al).\n"
                  "In **BeCl2(solid)**, an infinite linear chain is formed via Be-Cl: -> Be coordinate bridges (sp^3^ Be, 4-coordinate). In vapor at 1200 K, it exists as linear monomer Cl-Be-Cl (sp Be)."),
        ],
    },
    # ------------------------------------------------------------------ CB-14
    {
        "id": "CB-14",
        "title": "Molecular Orbital Theory: LCAO Principles & s-p Mixing",
        "blocks": [
            ("lead", "**Molecular Orbital Theory (MOT)** — LCAO Principles, Bonding/Antibonding & s-p Mixing"),
            ("p", "Developed by Hund and Mulliken. Atomic orbitals combine linearly (LCAO) to form **Molecular Orbitals (MOs)** "
                  "delocalised over the entire molecule. Total number of MOs formed equals total number of combining atomic orbitals."),
            ("h2", "1. Bonding vs Antibonding Molecular Orbitals"),
            ("table", ["Feature", "Bonding MO (ψ_b = ψ_A + ψ_B)", "Antibonding MO (ψ_a = ψ_A - ψ_B)"], [
                ["Formation Mode", "Constructive interference (in-phase wave addition)", "Destructive interference (out-of-phase wave subtraction)"],
                ["Electron Density", "**High between nuclei** (shields nuclei from each other)", "**Zero at nodal plane** between nuclei"],
                ["Energy State", "**Lower energy** than combining atomic orbitals (Stabilising)", "**Higher energy** than combining atomic orbitals (Destabilising)"],
            ], [20, 40, 40], "Table 2.7 — Bonding versus Antibonding orbital characteristics."),
            ("fig", "mot", "Fig. 2.2 — MO energy level crossover caused by s-p mixing: B2, C2, N2 (≤14 e-) vs O2, F2 (>14 e-)."),
            ("h2", "2. The s-p Mixing Phenomenon (The Crossover in Energy)"),
            ("p", "In homonuclear diatomics of Li, Be, B, C, N (≤ 14 electrons), the energy gap between 2s and 2p_z atomic orbitals "
                  "is small (< 10 eV). Consequently, **2s and 2p_z orbitals mix**, pushing σ(2p_z) UP and σ^*(2s) DOWN:\n"
                  "• Result for ≤ 14e^−^ (B2, C2, N2): **π(2p_x) = π(2p_y) becomes LOWER in energy than σ(2p_z)**!\n"
                  "• For > 14e^−^ (O2, F2): Large 2s-2p gap (> 15 eV) prevents mixing; normal order where σ(2p_z) is lower than π(2p).\n"
                  "**Bond Order (BO) = (N~b~ − N~a~) / 2**"),
        ],
    },
    # ------------------------------------------------------------------ CB-15
    {
        "id": "CB-15",
        "title": "Homonuclear Diatomics: H2 to Ne2 MO Diagrams & Paramagnetism",
        "blocks": [
            ("lead", "**Homonuclear Diatomics** — Complete Electronic Configurations, Bond Orders & Magnetism"),
            ("p", "Evaluation of 2nd-row homonuclear diatomics using MO theory."),
            ("h2", "1. Master Electronic Configurations Table"),
            ("table", ["Molecule / Ion", "Total e-", "MO Electronic Configuration", "Bond Order", "Magnetic Character"], [
                ["H2", "2", "σ(1s)^2", "**1**", "Diamagnetic"],
                ["He2+", "3", "σ(1s)^2 σ*(1s)^1", "**0.5**", "Paramagnetic (1 unpaired e-)"],
                ["He2", "4", "σ(1s)^2 σ*(1s)^2", "**0**", "Does NOT exist!"],
                ["B2", "10", "KK σ(2s)^2 σ*(2s)^2 [π(2p_x)^1 = π(2p_y)^1]", "**1**", "**Paramagnetic** (2 unpaired e- in degenerate π)"],
                ["C2", "12", "KK σ(2s)^2 σ*(2s)^2 [π(2p_x)^2 = π(2p_y)^2]", "**2**", "**Diamagnetic** (Both bonds are **pure π-bonds!**)"],
                ["N2", "14", "KK σ(2s)^2 σ*(2s)^2 [π(2p_x)^2 = π(2p_y)^2] σ(2p_z)^2", "**3**", "Diamagnetic (1 σ + 2 π bonds)"],
                ["N2+", "13", "KK σ(2s)^2 σ*(2s)^2 [π(2p_x)^2 = π(2p_y)^2] σ(2p_z)^1", "**2.5**", "Paramagnetic (BO: N2 > N2+)"],
                ["O2+", "15", "KK σ(2s)^2 σ*(2s)^2 σ(2p_z)^2 [π(2p)^4] [π*(2p_x)^1]", "**2.5**", "Paramagnetic (BO: O2+ > O2)"],
                ["O2", "16", "KK σ(2s)^2 σ*(2s)^2 σ(2p_z)^2 [π(2p)^4] [π*(2p_x)^1 = π*(2p_y)^1]", "**2**", "**Paramagnetic** (2 unpaired e- in π*)"],
                ["O2- (Superoxide)", "17", "KK σ(2s)^2 σ*(2s)^2 σ(2p_z)^2 [π(2p)^4] [π*(2p)^3]", "**1.5**", "Paramagnetic (1 unpaired e-)"],
                ["O2^2- (Peroxide)", "18", "KK σ(2s)^2 σ*(2s)^2 σ(2p_z)^2 [π(2p)^4] [π*(2p)^4]", "**1**", "Diamagnetic (BO = 1, single O-O bond)"],
                ["F2", "18", "KK σ(2s)^2 σ*(2s)^2 σ(2p_z)^2 [π(2p)^4] [π*(2p)^4]", "**1**", "Diamagnetic"],
                ["Ne2", "20", "KK σ(2s)^2 σ*(2s)^2 σ(2p_z)^2 [π(2p)^4] [π*(2p)^4] σ*(2p_z)^2", "**0**", "Does NOT exist!"],
            ], [15, 8, 45, 12, 20], "Table 2.8 — Complete MO properties of homonuclear diatomics."),
            ("key", "Two Critical JEE Advanced Insights from MOT:\n"
                    "1. **C2 molecule:** In gaseous C2, the double bond consists of **TWO PI (π) BONDS AND NO SIGMA BOND** because the last 4 electrons enter the degenerate π(2p_x) and π(2p_y) orbitals!\n"
                    "2. **Bond Length Order of Dioxygen species:**\n"
                    "   Bond Order: O~2~^+^ (2.5) > O~2~ (2.0) > O~2~^−^ (1.5) > O~2~^2- (1.0)\n"
                    "   Bond Length: **O~2~^+^ < O~2~ < O~2~^−^ < O~2~^2-** (Peroxide has longest bond, ~149 pm)."),
        ],
    },
    # ------------------------------------------------------------------ CB-16
    {
        "id": "CB-16",
        "title": "Heteronuclear Diatomics: CO, NO, CN- & Isoelectronic Species",
        "blocks": [
            ("lead", "**Heteronuclear Diatomics** — Polar Molecular Orbitals, CO Anomaly & NO Redox"),
            ("p", "In heteronuclear diatomics (AB), the more electronegative atom has lower atomic orbital energies, "
                  "contributing more to bonding MOs, while the electropositive atom contributes more to antibonding MOs."),
            ("h2", "1. Carbon Monoxide (CO) — The HOMO/LUMO Anomaly"),
            ("bul", [
                "**Isoelectronic with N2:** 14 valence electrons (10 outer). Ground state configuration:\n"
                "  **σ(2s)^2 σ^*(2s)^2 [π(2p_x)^2 = π(2p_y)^2] σ(2p_z)^2**\n"
                "  Bond order = (8 - 2)/2 = 3 (one σ, two π bonds).",
                "**The CO+ Ionization Anomaly (Classic JEE Advanced Question):**\n"
                "  When CO is ionised to CO+, an electron is removed from the HOMO σ(2s). However, due to extensive s-p mixing and hybridization, this HOMO has **slight antibonding character**!\n"
                "  Consequently, upon removing this electron: **Bond Order of CO+ INCREASES to ~3.5**, and the C-O bond becomes **SHORTER AND STRONGER** (112.8 pm -> 111.5 pm)!",
            ]),
            ("h2", "2. Nitric Oxide (NO) — Odd-Electron Diatomic"),
            ("p", "Total valence electrons = 15. Electronic configuration:\n"
                  "**KK  σ(2s)^2 σ^*(2s)^2 σ(2p_z)^2 [π(2p_x)^2 = π(2p_y)^2] [π^*(2p_x)^1]**\n"
                  "• Bond Order = (8 - 3)/2 = 2.5. Paramagnetic (1 unpaired electron in π^*).\n"
                  "• Oxidation to Nitrosonium ion **NO+**: Removing the antibonding π^* electron yields NO+ (isoelectronic with N2):\n"
                  "  **Bond Order: NO^+^ (3.0) > NO (2.5) > NO^−^ (2.0)**\n"
                  "  NO+ is diamagnetic and has a shorter, much stronger bond than neutral NO."),
        ],
    },
]
