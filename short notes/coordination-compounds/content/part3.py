"""Part 3: Sheets CC-13 to CC-18 — Square Planar, Jahn-Teller, Color, Carbonyls, Stability & Applications."""
from __future__ import annotations

SHEETS = [
    # ------------------------------------------------------------------ CC-13
    {
        "id": "CC-13",
        "title": "CFT in Square Planar Complexes & Splitting Hierarchy",
        "blocks": [
            ("lead", "**Crystal Field Splitting in D_4h Geometry & The d^8^ Configuration** (NCERT §9.5.3)"),
            ("p", "Square planar geometry ($D_{4h}$) is derived conceptually from an octahedral complex by progressively pulling the two trans ligands along the z-axis to infinity (tetragonal distortion to the square planar limit)."),
            ("fig", "square_planar_splitting", "Fig. 13.1 — Octahedral to tetragonal to square planar (D_4h) crystal field energy levels."),
            ("h2", "1. Orbital Energy Splitting in D_4h Symmetry"),
            ("bul", [
                "**1. d_x²-y² (Highest Energy):** Lobes point directly at the 4 remaining in-plane ligands ($x, y$) $\\implies$ experiences maximal electrostatic repulsion; elevated to the highest energy level.",
                "**2. d_xy (Second Highest):** Lobes lie in the $xy$-plane between the ligands $\\implies$ substantial in-plane repulsion, but lower than $d_{x^2-y^2}$.",
                "**3. d_z² (Third Highest):** Completely relieved of direct axial ligand encounters; stabilized substantially, lying below $d_{xy}$ (its donut ring lies in the $xy$-plane).",
                "**4. d_xz, d_yz (Lowest Energy, Degenerate Pair):** Lobes point completely out of the coordination plane $\\implies$ experience minimum repulsion.",
                "**Master Energy Order in Square Planar:**",
                "  $$\\mathbf{d_{x^2-y^2} \\gg d_{xy} > d_{z^2} > (d_{xz} = d_{yz})}$$",
                "  The total square planar splitting energy is $\\mathbf{\\Delta_{sp} \\approx 1.3 \\text{ to } 1.74 \\Delta_o}$."
            ]),
            ("h2", "2. Why d^8^ Metal Ions Universally Form Square Planar Complexes"),
            ("p", "In $d^8$ electronic systems (e.g. $\\text{Ni}^{2+}, \\text{Pd}^{2+}, \\text{Pt}^{2+}, \\text{Au}^{3+}$), the 8 d-electrons occupy the lower four orbitals in spin-paired configurations: $(d_{xz}, d_{yz})^4 (d_{z^2})^2 (d_{xy})^2$, leaving the strongly destabilized $d_{x^2-y^2}$ completely empty!\n"
                  "• This produces an enormous Crystal Field Stabilization Energy (CFSE gain) that heavily favors square planar over tetrahedral geometry.\n"
                  "• **All 4d^8^ (Pd^2+^) and 5d^8^ (Pt^2+^, Au^3+^) complexes are SQUARE PLANAR and DIAMAGNETIC**, regardless of ligand field strength (even with weak $\\text{Cl}^-$ in $[\\text{PtCl}_4]^{2-}$)!"),
            ("h2", "3. Nickel(II) Complex Stereochemistry: [Ni(CN)~4~]^2−^ vs [NiCl~4~]^2−^"),
            ("table", ["Complex Ion", "Ligand Type / Field", "Geometry & Hybridization", "Unpaired e^- (n)", "Magnetic Character"], [
                ["$[\\text{Ni(CN)}_4]^{2-}$", "Strong field $\\text{CN}^-$", "**Square Planar ($dsp^2$)**", "**0**", "**Diamagnetic** (Yellow)"],
                ["$[\\text{NiCl}_4]^{2-}$", "Weak field $\\text{Cl}^-$", "**Tetrahedral ($sp^3$)**", "**2**", "**Paramagnetic** ($\\mu = 2.83\\text{ BM}$)"],
                ["$[\\text{Ni(CO)}_4]$", "Strong field $\\text{CO}$ ($Ni^0, 3d^{10}$)", "**Tetrahedral ($sp^3$)**", "**0**", "**Diamagnetic** (Colorless)"]
            ], [20, 22, 24, 14, 20], "Table 13.1 — Contrasting geometries and magnetism in nickel complexes."),
            ("trap", "EXAM TRAP: $[\\text{PtCl}_4]^{2-}$ and $[\\text{Pt(NH}_3)_4]^{2+}$ are BOTH square planar and diamagnetic because Pt is a 5d metal with huge $\\Delta$!")
        ]
    },

    # ------------------------------------------------------------------ CC-14
    {
        "id": "CC-14",
        "title": "Jahn–Teller Distortion & Tetragonal Elongation in d^9^ / High-Spin d^4^",
        "blocks": [
            ("lead", "**Electronic Degeneracy & Spontaneous Geometric Distortion** (JEE Advanced Special)"),
            ("p", "The Jahn–Teller Theorem states: *Any non-linear molecular system in a spatially degenerate electronic ground state is unstable and will undergo geometric distortion to lower its symmetry, remove the degeneracy, and lower the overall energy.*"),
            ("h2", "1. Asymmetric Electron Occupation: e_g vs t_2g"),
            ("bul", [
                "**1. Strong Jahn–Teller Distortion (Asymmetric e_g Occupation):**",
                "  Because $e_g$ orbitals ($d_{x^2-y^2}, d_{z^2}$) point directly at ligands, an uneven electron distribution in $e_g$ causes strong unequal repulsions on ligand pairs $\\implies$ **pronounced geometric distortion**.",
                "  - **d^9^ System (e.g. Cu^2+^, t_2g^6 e_g^3):** Most famous case! One orbital has 2 electrons while the other has 1 electron.",
                "  - **High-Spin d^4^ System (e.g. Cr^2+^, Mn^3+^, t_2g^3 e_g^1):** Unequal occupation of $e_g$.",
                "  - **Low-Spin d^7^ System (e.g. Co^2+^ LS, Ni^3+^ LS, t_2g^6 e_g^1):** Pronounced distortion.",
                "**2. Weak Jahn–Teller Distortion (Asymmetric t_2g Occupation):**",
                "  $t_{2g}$ orbitals point between ligands $\\implies$ unequal electron distribution ($d^1, d^2, \\text{HS } d^6, \\text{HS } d^7$) produces only **very weak, subtle distortions** that are experimentally hard to observe.",
                "**3. Zero Jahn–Teller Distortion (Symmetrical Occupation):**",
                "  $d^3$ ($t_{2g}^3$), HS $d^5$ ($t_{2g}^3 e_g^2$), LS $d^6$ ($t_{2g}^6$), $d^8$ ($t_{2g}^6 e_g^2$), and $d^{10}$ ($t_{2g}^6 e_g^4$) have completely symmetrical sets $\\implies$ **zero distortion (perfect Oh symmetry)**!"
            ]),
            ("h2", "2. Tetragonal Elongation (z-out) vs Compression (z-in)"),
            ("p", "In the vast majority of copper(II) complexes (e.g. $[\\text{Cu(H}_2\\text{O)}_6]^{2+}$):\n"
                  "• If the 3rd $e_g$ electron enters $d_{z^2}$ ($d_{z^2}^2 d_{x^2-y^2}^1$), electrons shield the nucleus along the z-axis, weakening metal-ligand attraction $\\implies$ **two trans axial ligands move further away (z-elongation)**!\n"
                  "• **Result:** 4 short in-plane equatorial bonds and **2 longer axial bonds** (e.g. in $\\text{CuF}_2$, 4 equatorial Cu-F = 193 pm, 2 axial Cu-F = 227 pm!)."),
            ("h2", "3. Copper(II) Ammonia Complex Stepwise Stability Drop"),
            ("p", "In $[\\text{Cu(NH}_3)_4(\\text{H}_2\\text{O)}_2]^{2+}$, adding ammonia readily replaces the 4 in-plane equatorial water molecules to form $[\\text{Cu(NH}_3)_4]^{2+}$, but the 5th and 6th water molecules on the elongated z-axis are so weakly bound that $[\\text{Cu(NH}_3)_6]^{2+}$ can ONLY be formed in anhydrous liquid ammonia!"),
            ("trap", "HIGH-YIELD JEE ADVANCED QUESTION: Which of the following shows strong Jahn-Teller distortion? (A) $[\\text{Cr(H}_2\\text{O)}_6]^{3+}$ ($d^3$), (B) $[\\text{Mn(H}_2\\text{O)}_6]^{2+}$ ($d^5$), (C) $[\\text{Cu(H}_2\\text{O)}_6]^{2+}$ ($d^9$), (D) $[\\text{Fe(CN)}_6]^{4-}$ ($d^6$). **Answer is C** ($d^9$ asymmetric $e_g$)!")
        ]
    },

    # ------------------------------------------------------------------ CC-15
    {
        "id": "CC-15",
        "title": "Colour in Coordination Compounds & Absorption Spectroscopy",
        "blocks": [
            ("lead", "**Electronic Transitions & Complementary Visible Absorption** (NCERT §9.5.4)"),
            ("p", "The vivid colors of coordination complexes arise primarily from the absorption of specific wavelengths of visible light to excite electrons between crystal-field-split d-orbitals ($d\\text{-}d$ transitions)."),
            ("h2", "1. Mechanism of Colour & The Complementary Wheel"),
            ("bul", [
                "**Light Absorption:** When white light strikes a solution of a complex with an incompletely filled d-subshell ($d^1$ to $d^9$), a photon of energy $h\\nu = \\Delta_o$ is absorbed to promote an electron from $t_{2g}$ to $e_g$.",
                "**Complementary Transmission:** The human eye perceives the light that is NOT absorbed — the **complementary color**:\n"
                  "  - **Absorbs Red** (long $\\lambda$, small $\\Delta$) $\\rightarrow$ Appears **Green**.\n"
                  "  - **Absorbs Yellow** $\\rightarrow$ Appears **Violet / Blue**.\n"
                  "  - **Absorbs Blue-Green** $\\rightarrow$ Appears **Red / Orange**.\n"
                  "  - **Absorbs Violet** (short $\\lambda$, large $\\Delta$) $\\rightarrow$ Appears **Yellow**."
            ]),
            ("h2", "2. Influence of Ligand on Color: [Ni(H~2~O)~6~]^2+^ Stepwise Substitution"),
            ("p", "Progressive replacement of weak $\\text{H}_2\\text{O}$ by stronger ethylenediamine (en) increases $\\Delta_o$, shifting absorption to shorter wavelengths (higher frequency):\n"
                  "  1. $[\\text{Ni(H}_2\\text{O)}_6]^{2+}$: **Green** (absorbs red light).\n"
                  "  2. $[\\text{Ni(H}_2\\text{O)}_4(\\text{en})]^{2+}$: **Pale blue**.\n"
                  "  3. $[\\text{Ni(H}_2\\text{O)}_2(\\text{en})_2]^{2+}$: **Blue / Purple**.\n"
                  "  4. $[\\text{Ni(en)}_3]^{2+}$: **Violet** (absorbs yellow light, largest $\\Delta_o$!)."),
            ("h2", "3. Ruby and Emerald: Crystal Field Gemstones"),
            ("bul", [
                "**Ruby:** Consists of colorless $\\alpha\\text{-Al}_2\\text{O}_3$ in which $\\sim 0.5\\text{-}1\\%$ of $\\text{Al}^{3+}$ sites are occupied by $\\text{Cr}^{3+}$ ($d^3$). In the tight alumina lattice, $\\text{Al-O}$ distance is short, compressing $\\text{Cr}^{3+}$ $\\implies$ strong crystal field absorbs yellow-green light, transmitting **deep crimson red**!",
                "**Emerald:** $\\text{Cr}^{3+}$ replaces $\\text{Al}^{3+}$ in beryl ($\text{Be}_3\\text{Al}_2\\text{Si}_6\\text{O}_{18}$). Larger silicate cavities provide a slightly weaker crystal field, shifting absorption into the red/yellow region and transmitting **brilliant green**!"
            ]),
            ("trap", "WHY IS ANHYDROUS CuSO~4~ WHITE? When white anhydrous $\\text{CuSO}_4$ has no water ligands, the crystal field splitting is zero ($\\Delta = 0$). All 5 d-orbitals remain degenerate; no $d\\text{-}d$ transitions are possible $\\implies$ pure white!")
        ]
    },

    # ------------------------------------------------------------------ CC-16
    {
        "id": "CC-16",
        "title": "Bonding in Metal Carbonyls: Synergic Effect & IR ν_CO Trends",
        "blocks": [
            ("lead", "**Organometallic Synergy: σ-Donation & π-Backbonding** (NCERT §9.6)"),
            ("p", "Homoleptic metal carbonyls (e.g. $[\\text{Ni(CO)}_4], [\\text{Fe(CO)}_5], [\\text{Cr(CO)}_6]$) exhibit unique metal-carbon bonding characterized by mutual reinforcement between $\\sigma$ and $\\pi$ bonds."),
            ("fig", "carbonyl_synergic_bonding", "Fig. 16.1 — Synergic M-CO bonding: σ donation from C lone pair and π backbonding into CO π* orbitals."),
            ("h2", "1. The Synergic Bonding Mechanism"),
            ("bul", [
                "**1. M $\\leftarrow$ C $\\sigma$-Bond:** Carbon atom of CO donates its lone pair of electrons from a filled non-bonding sp-hybrid orbital into an empty hybrid orbital of the transition metal.",
                "**2. M $\\rightarrow$ C $\\pi$-Backbond:** Filled d-orbitals ($d_{xy}, d_{yz}, d_{zx}$) of the transition metal overlap sideways with the **empty antibonding $\\pi^*$ molecular orbitals** of the carbon monoxide ligand.",
                "**3. The Synergic Loop:** $\\sigma$-donation increases electron density on the metal, facilitating $\\pi$-backdonation; simultaneously, $\\pi$-backdonation relieves excess negative charge from the metal, strengthening the $\\sigma$-bond! This self-reinforcing cooperative loop is called **synergic bonding**."
            ]),
            ("h2", "2. Impact on M-C and C-O Bond Orders & IR Stretching Frequencies (ν_CO)"),
            ("p", "When electrons are back-donated into the **antibonding $\\pi^*$ orbital** of CO:\n"
                  "• Metal-Carbon ($\text{M-C}$) bond order increases (approaching double bond $\\text{M}=\\text{C}$): bond becomes **shorter and stronger**.\n"
                  "• Carbon-Oxygen ($\text{C-O}$) bond order decreases (from triple bond $\\text{C}\\equiv\\text{O}$ towards double bond $\\text{C}=\\text{O}$): bond becomes **longer and weaker**!\n"
                  "• By Hooke's Law ($\\nu = \\frac{1}{2\\pi c}\\sqrt{k/\\mu}$), a weaker bond has a lower force constant $k$ and thus a **lower IR stretching frequency $\\nu_{\\text{CO}}$**."),
            ("h2", "3. Isoelectronic Carbonyl Series (JEE Advanced Master Metric)"),
            ("table", ["Carbonyl Species", "Metal & OS", "Extrapolated π-Backdonation", "M-C Bond Strength / Length", "C-O Bond Order & IR $\\nu_{\\text{CO}}$ (cm^−1^)"], [
                ["$[\\text{Mn(CO)}_6]^+$", "$\\text{Mn}(+1)$", "Least (positive charge holds d-electrons)", "Weakest / Longest M-C", "**Strongest C-O / Highest $\\nu_{\\text{CO}}$** (~2090 cm^−1^)"],
                ["$[\\text{Cr(CO)}_6]$", "$\\text{Cr}(0)$", "Intermediate", "Intermediate M-C", "Intermediate C-O (~2000 cm^−1^)"],
                ["$[\\text{V(CO)}_6]^-$", "$\\text{V}(-1)$", "**Most (negative charge repels d-electrons)**", "**Strongest / Shortest M-C**", "**Weakest C-O / Lowest $\\nu_{\\text{CO}}$** (~1860 cm^−1^)"]
            ], [18, 16, 26, 20, 20], "Table 16.1 — Isoelectronic carbonyl comparison: charge vs backdonation and IR frequencies."),
            ("trap", "CRITICAL JEE ADVANCED TRAP: Higher negative charge on the metal carbonyl complex $\\implies$ GREATER $\\pi$-backdonation $\\implies$ SHORTER M-C bond $\\implies$ LONGEST C-O bond $\\implies$ LOWEST $\\nu_{\\text{CO}}$ stretching frequency!")
        ]
    },

    # ------------------------------------------------------------------ CC-17
    {
        "id": "CC-17",
        "title": "Thermodynamic vs Kinetic Stability & Irving–Williams Series",
        "blocks": [
            ("lead", "**Stepwise Formation Constants & Stability Determinants** (NCERT §9.8)"),
            ("p", "The stability of a complex in solution refers to the degree of association between the metal ion and the ligands involved in dynamic equilibrium."),
            ("h2", "1. Stepwise vs Overall Stability Constants (K_n vs β_n)"),
            ("p", "In solution, ligands add to a metal ion in a stepwise sequence:\n"
                  "  $$\\text{M} + \\text{L} \\rightleftharpoons \\text{ML} \\quad (K_1 = [\\text{ML}] / [\\text{M}][\\text{L}])$$\n"
                  "  $$\\text{ML} + \\text{L} \\rightleftharpoons \\text{ML}_2 \\quad (K_2 = [\\text{ML}_2] / [\\text{ML}][\\text{L}])$$\n"
                  "  $$\\text{Overall: } \\text{M} + n\\text{L} \\rightleftharpoons \\text{ML}_n \\quad (\\beta_n = K_1 \\cdot K_2 \\cdot \\dots \\cdot K_n)$$\n"
                  "• In terms of logarithms: $\\mathbf{\\log \\beta_n = \\log K_1 + \\log K_2 + \\dots + \\log K_n}$.\n"
                  "• **Universal Trend:** Stepwise constants almost invariably follow: **K_1 > K_2 > K_3 > ... > K_n** due to electrostatic repulsion, statistical probability of vacant sites, and steric crowding."),
            ("h2", "2. The Irving–Williams Series for Divalent 3d Metal Ions"),
            ("p", "For high-spin octahedral complexes of divalent 3d transition metal cations ($M^{2+}$), stability increases progressively regardless of the ligand nature, reaching a sharp maximum at Copper:\n"
                  "  $$\\mathbf{Ba^{2+} < Sr^{2+} < Ca^{2+} < Mg^{2+} < Mn^{2+} < Fe^{2+} < Co^{2+} < Ni^{2+} < Cu^{2+} > Zn^{2+}}$$\n"
                  "• **Physical Driving Factors:**\n"
                  "  1. **Ionic Size Decrease:** Radii contract from $Mn^{2+}$ to $Cu^{2+}$, increasing electrostatic charge density ($q/r$).\n"
                  "  2. **CFSE Gain:** Crystal field stabilization energy increases progressively from $d^5$ ($Mn^{2+}$, CFSE = 0) to $d^8$ ($Ni^{2+}$).\n"
                  "  3. **The Copper Peak ($Cu^{2+} > Zn^{2+}$):** Copper(II) ($d^9$) experiences intense **Jahn–Teller distortion**, shortening 4 equatorial bonds and producing an exceptionally stable complex! $Zn^{2+}$ ($d^{10}$, CFSE = 0) drops sharply in stability."),
            ("h2", "3. Thermodynamic vs Kinetic Stability"),
            ("bul", [
                "**Thermodynamic Stability:** Measured by the equilibrium formation constant $\\beta_n$ (or $\\Delta G^\\circ = -RT \\ln \\beta_n$). High $\\beta$ indicates a stable complex.",
                "**Kinetic Stability (Lability vs Inertness):** Refers to the **rate of ligand substitution**:\n"
                  "  - **Labile Complexes:** Undergo ligand substitution very rapidly ($t_{1/2} < 1\\text{ minute}$). E.g. $[\\text{Cu(NH}_3)_4]^{2+}$ exchanges with $^{14}\\text{NH}_3$ instantaneously.\n"
                  "  - **Inert Complexes:** Undergo ligand exchange very slowly ($t_{1/2} > 1\\text{ minute}$). E.g. $d^3$ ($Cr^{3+}$) and low-spin $d^6$ ($Co^{3+}$) complexes are kinetically inert!"
            ]),
            ("trap", "CRITICAL TRAP: $[\\text{Fe(CN)}_6]^{4-}$ is thermodynamically very stable (huge $\\beta$), but kinetically labile. Conversely, $[\\text{Co(NH}_3)_6]^{3+}$ is thermodynamically unstable in acid (breaks down to $\\text{Co}^{2+}$), but kinetically so inert that it persists for days without decomposing!")
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
                "**1. Analytical Chemistry:** \\text{Ni}^{2+} reacts with dmg in ammoniacal solution to give a **scarlet red precipitate** [\\text{Ni(dmg)}_2] stabilized by O-H···O hydrogen bonds. Hardness of water is estimated with standard \\text{Na}_2\\text{H}_2\\text{EDTA} (EBT indicator).",
                "**2. Metallurgy & Metal Extraction:** **MacArthur-Forrest Cyanide Process:** Au/Ag leached with NaCN: $4\\text{Au} + 8\\text{CN}^- + 2\\text{H}_2\\text{O} + \\text{O}_2 \\rightarrow 4[\\text{Au(CN)}_2]^- + 4\\text{OH}^-$, recovered by zinc displacement. **Mond Process:** Nickel purified via volatile [\\text{Ni(CO)}_4].",
                "**3. Biological Role:** **Chlorophyll:** Coordination complex of **\\text{Mg}^{2+}** (photosynthesis). **Hemoglobin:** Complex of **\\text{Fe}^{2+}** with protoporphyrin IX (oxygen carrier). **Vitamin B~12~:** Complex of **\\text{Co}^{3+}** (corrin ring).",
                "**4. Medicinal Chemistry:** **Cisplatin ($cis-[\\text{Pt(NH}_3)_2\\text{Cl}_2]$):** Potent anti-cancer agent. **Chelation Therapy:** \\text{Ca-EDTA}^{2-} for lead poisoning; D-penicillamine for Wilson disease."
            ]),
            ("h2", "2. JEE Advanced Core Master Reasoning Bank"),
            ("table", ["Exam Diagnostic Question", "Core Theoretical Principle", "Precise Exam Explanation"], [
                ["**Why is [Fe(H~2~O)~6~]^3+^ colored while [Mn(H~2~O)~6~]^2+^ is very pale?**", "Laporte & Spin Selection", "$\\text{Mn}^{2+}$ is high-spin $d^5$; any $d\\text{-}d$ transition requires spin flip (spin-forbidden). $\\text{Fe}^{3+}$ has charge transfer enhancement."],
                ["**Why is [CoF~6~]^3−^ paramagnetic while [Co(NH~3~)~6~]^3+^ is diamagnetic?**", "Splitting vs Pairing", "$\\text{F}^-$ is weak field ($\\Delta_o < P \\implies t_{2g}^4 e_g^2$, 4 unp). $\\text{NH}_3$ is strong field ($\\Delta_o > P \\implies t_{2g}^6 e_g^0$, 0 unp)."],
                ["**Why do tetrahedral complexes never form low-spin states?**", "Magnitude of $\\Delta_t$", "$\\Delta_t = \\frac{4}{9} \\Delta_o$. Electrostatic field is weak, so $\\Delta_t < P$ always holds."],
                ["**Why does [Ni(dmg)~2~] precipitate selectively?**", "Hydrogen Bonding", "Planar arrangement with 2 symmetrical O-H···O bridges forms a neutral, highly insoluble chelate lattice."]
            ], [28, 28, 44], "Table 18.1 — Authoritative JEE Advanced reasoning traps and diagnostic answers."),
            ("trap", "FINAL EXAM WARNING: In metal carbonyls, backbonding reduces the \\text{C-O} bond order and increases the \\text{M-C} bond order! Always check whether the question asks about \\text{M-C} or \\text{C-O} bond length before answering!")
        ]
    }
]
