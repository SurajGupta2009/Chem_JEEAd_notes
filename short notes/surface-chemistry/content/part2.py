"""Part 2: Catalysis, Modern Adsorption Theory, Shape-Selective Zeolites & Enzyme Kinetics (SC-07 to SC-11)."""
from __future__ import annotations

SHEETS = [
    # ------------------------------------------------------------------ SC-07
    {
        "id": "SC-07",
        "title": "Catalysis: Homogeneous vs Heterogeneous Systems & Promoters",
        "blocks": [
            ("lead", "**Catalysis Principles** — Accelerating Chemical Transformations (NCERT §5.2)"),
            ("p", "A **catalyst** is a substance which alters the rate of a chemical reaction without itself undergoing any permanent chemical or quantitative change at the end of the reaction. Promoters enhance catalytic efficiency, while poisons inhibit it."),
            ("h2", "1. Homogeneous vs Heterogeneous Catalysis"),
            ("table", ["Type of Catalysis", "Physical State Criteria", "Industrial Chemical Exemplars (NCERT)", "Mechanism"], [
                ["**Homogeneous Catalysis**", "Reactants and catalyst exist in the **SAME single physical phase** (all gas or all liquid)", "• **Lead Chamber Process for H~2~SO~4~:**\n  2 SO~2~(g) + O~2~(g) —[NO(g)]→ 2 SO~3~(g)\n• **Hydrolysis of Methyl Acetate:**\n  CH~3~COOCH~3~(l) + H~2~O(l) —[HCl(l)]→ CH~3~COOH(l) + CH~3~OH(l)\n• **Hydrolysis of Cane Sugar (Inversion):**\n  C~12~H~22~O~11~(aq) + H~2~O(l) —[H~2~SO~4~(l)]→ C~6~H~12~O~6~(aq) + C~6~H~12~O~6~(aq)", "Proceeds via intermediate compound formation theory (Arrhenius/Lewis acid-base coordination)"],
                ["**Heterogeneous Catalysis**", "Reactants and catalyst exist in **DIFFERENT physical phases** (typically gaseous reactants over solid catalyst)", "• **Haber's Process for Ammonia:**\n  N~2~(g) + 3 H~2~(g) —[Fe(s) + Mo/K~2~O/Al~2~O~3~]→ 2 NH~3~(g)\n• **Ostwald's Process for Nitric Acid:**\n  4 NH~3~(g) + 5 O~2~(g) —[Pt/Rh gauze(s)]→ 4 NO(g) + 6 H~2~O(g)\n• **Contact Process for Sulphuric Acid:**\n  2 SO~2~(g) + O~2~(g) —[V~2~O~5~(s)]→ 2 SO~3~(g)\n• **Hydrogenation of Vegetable Oils:**\n  Vegetable Oil(l) + H~2~(g) —[Ni(s)]→ Vegetable Ghee / Fat(s)", "Proceeds via modern adsorption theory on solid surface active sites"]
            ], [18, 22, 38, 22], "Table 2.1 — Homogeneous vs Heterogeneous Catalysis systems in NCERT."),
            ("h2", "2. Promoters and Catalytic Poisons"),
            ("bul", [
                "**Promoters:** Substances that are not catalysts themselves, but whose presence **increases the catalytic activity** of the catalyst. *Example:* In Haber's process, **Molybdenum (Mo)** acts as a promoter for the **Iron (Fe)** catalyst, expanding the iron lattice and increasing active site spacing. Modern catalysts use **K~2~O and Al~2~O~3~** as structural promoters.",
                "**Catalytic Poisons (Inhibitors):** Substances that destroy or diminish catalytic activity by competing for active sites or forming unreactive surface complexes. *Examples:* Trace **CO or H~2~S** poisons the iron catalyst in Haber's synthesis; **Arsenic (As~2~O~3~)** poisons platinum in the Contact process."
            ]),
            ("trap", 'TRAP: Does a catalyst alter the equilibrium constant (K~eq~) or standard Gibbs free energy (ΔG°)? ABSOLUTELY NOT! A catalyst accelerates the forward and reverse reactions by the exact same factor, helping attain equilibrium faster without changing equilibrium composition!')
        ]
    },

    # ------------------------------------------------------------------ SC-08
    {
        "id": "SC-08",
        "title": "Modern Adsorption Theory of Heterogeneous Catalysis",
        "blocks": [
            ("lead", "**Modern Surface Adsorption Theory** — Intermediate Compound + Adsorption Mechanics (NCERT §5.2.2)"),
            ("p", 'Explains the mechanism of heterogeneous catalysis on solid surfaces. The catalyst functions by providing localized **active sites (free valencies)** that adsorb reactant molecules, weaken their internal bonds, form an activated complex with lower activation energy (E~a~), and desorb products.'),
            ("fig", "catalysis_cycle", "Fig. 2.1 — The 5-step cycle of heterogeneous catalysis: Diffusion, chemisorption, reaction, desorption, and product diffusion."),
            ("h2", "1. The 5-Step Catalytic Cycle (NCERT Sequence)"),
            ("bul", [
                "**Step 1: Diffusion of Reactants:** Gaseous/liquid reactant molecules diffuse from the bulk phase to the outer boundary layer and pores of the solid catalyst.",
                "**Step 2: Chemisorption of Reactants:** Reactant molecules form chemical bonds with the free valencies of surface metal atoms at active sites (edges, corners, cracks), releasing heat of adsorption.",
                "**Step 3: Chemical Reaction via Activated Complex:** Adsorbed adjacent molecules react with each other on the surface to form a transient **surface activated complex** [A—B—Catalyst]‡. Internal bonds break and new bonds form with significantly reduced activation energy!",
                "**Step 4: Desorption of Reaction Products:** The newly formed product molecules possess lower affinity for the catalyst surface and **desorb into the gas phase**, regenerating the active site intact for subsequent turnovers.",
                "**Step 5: Diffusion of Products:** Desorbed products diffuse away from the catalyst surface into the bulk stream."
            ]),
            ("h2", "2. Two Cardinal Features of Solid Catalysts (NCERT §5.2.3)"),
            ("table", ["Feature", "Definition & Scientific Principle", "Industrial Chemical Proof"], [
                ["**1. Activity**", "The capacity of a catalyst to accelerate the reaction rate. Some catalysts increase rates by **up to 10^10^ times**! The chemisorption must be strong enough to be active, but not so strong that products cannot desorb (volcano curve).", "Mixture of H~2~ and O~2~ does not react for centuries at 298 K; adding trace finely divided **Platinum** causes instantaneous explosive reaction to form H~2~O!"],
                ["**2. Selectivity**", "The ability of a catalyst to **direct a reaction to yield particular products**, excluding other possible thermodynamic pathways. A given set of reactants yields totally different products depending on the catalyst used!", 'Reactants CO + H~2~ (Synthesis Gas):\n• CO + 3 H~2~ —(Ni)→ CH~4~ + H~2~O (Methanation)\n• CO + 2 H~2~ —(Cu/ZnO-Cr~2~O~3~)→ CH~3~OH (Methanol)\n• CO + H~2~ —(Cu)→ HCHO (Methanal)']
            ], [20, 42, 38], "Table 2.2 — Activity vs Selectivity of heterogeneous catalysts."),
            ("key", "Sabatier Principle: Catalytic activity peaks at an intermediate heat of chemisorption (Volcano plot). Group 7 to 11 metals show maximum catalytic activity (Group 8, 9, 10 peak for hydrogenation).")
        ]
    },

    # ------------------------------------------------------------------ SC-09
    {
        "id": "SC-09",
        "title": "Shape-Selective Catalysis by Zeolites & ZSM-5 Architecture",
        "blocks": [
            ("lead", "**Shape-Selective Catalysis** — Nanoporous Molecular Sieves (NCERT §5.2.3)"),
            ("p", "A catalytic reaction that depends on the **pore structure and cage size of the catalyst** as well as on the **size and shape of the reactant and product molecules** is termed **Shape-Selective Catalysis**."),
            ("h2", "1. Zeolites: Architecture & Chemistry"),
            ("bul", [
                "**Chemical Nature:** Microporous aluminosilicates with general formula: M~x/n~[(AlO~2~)~x~(SiO~2~)~y~]·mH~2~O, where M is a metal cation of valence n.",
                "**Honeycomb Network:** Formed by a 3-dimensional infinite network of rigid **SiO~4~ and AlO~4~^−^ tetrahedra** linked by sharing oxygen vertices, forming a **three-dimensional Al—O—Si framework**.",
                '**Molecular Sieve Action:** Because Al^3+^ replaces Si^4+^ in the framework, each Al atom imparts a net negative charge, balanced by exchangeable cations (Na^+^, H^+^, Ca^2+^). The framework encloses regular channels, tunnels, and cages of molecular dimensions (aperture size ≈260 to 740 pm).',
                "**Reactivity Constraint:** Only those reactant molecules whose kinetic diameters are **smaller than the zeolite pore apertures** can enter the interior cages to react; and only products smaller than the pores can diffuse out!"
            ]),
            ("h2", "2. ZSM-5 in Petrochemical Refining (NCERT Landmark)"),
            ("p", '• **ZSM-5 (Zeolite Socony Mobil-5):** An acidic aluminosilicate zeolite possessing a pore size of ≈550 pm.\n'
                  "• **Gasoline Synthesis:** Directly converts aliphatic alcohols into synthetic gasoline (hydrocarbons) by dehydrating them inside its rigid channels:\n"
                  "  x CH~3~OH —(ZSM-5, 673 K)→ Gasoline (Mixture of branched hydrocarbons + Aromatics) + x H~2~O\n"
                  "• Also used for shape-selective isomerization of xylenes (selectively producing p-xylene over bulky o- and m-xylenes)."),
            ("trap", "TRAP: Why are zeolites exceptionally good acidic catalysts? When synthetic zeolites are treated with ammonium salts and heated, the exchangeable cations become acidic **H^+^ protons attached to framework oxygens (Brønsted acid sites)**!")
        ]
    },

    # ------------------------------------------------------------------ SC-10
    {
        "id": "SC-10",
        "title": "Enzyme Catalysis: Biochemical Lock-and-Key Mechanics",
        "blocks": [
            ("lead", "**Biochemical Catalysis** — The Biological Engines of Life (NCERT §5.2.4)"),
            ("p", "Enzymes are complex nitrogenous organic compounds produced by living cells (globular proteins of high molecular mass, 15,000 to 1,000,000 g/mol). They catalyze hundreds of metabolic reactions with unmatched efficiency, speed, and absolute stereo-specificity."),
            ("h2", "1. Major Industrial & Biological Enzymes (NCERT Catalog)"),
            ("table", ["Enzyme", "Source Organism", "Enzymatic Reaction Catalyzed"], [
                ["**Invertase**", "Yeast", "C~12~H~22~O~11~ + H~2~O → C~6~H~12~O~6~ (Glucose) + C~6~H~12~O~6~ (Fructose)"],
                ["**Zymase**", "Yeast", "C~6~H~12~O~6~ → 2 C~2~H~5~OH + 2 CO~2~ ↑ (Alcoholic fermentation)"],
                ["**Diastase**", "Malted barley", "2 (C~6~H~10~O~5~)~n~ + n H~2~O → n C~12~H~22~O~11~ (Starch to Maltose)"],
                ["**Maltase**", "Yeast", "C~12~H~22~O~11~ + H~2~O → 2 C~6~H~12~O~6~ (Maltose to Glucose)"],
                ["**Urease**", "Soyabean", "NH~2~CONH~2~ + H~2~O → 2 NH~3~ + CO~2~ ↑ (Urea hydrolysis)"],
                ["**Pepsin / Trypsin**", "Stomach / Pancreas", "Proteins → Polypeptides → Amino acids in intestine"]
            ], [15, 20, 65], "Table 2.3 — Classical enzymatic reactions tested in JEE."),
            ("h2", "2. Characteristics of Enzyme Catalysis"),
            ("bul", [
                "**1. Extreme Efficiency:** One molecule of an enzyme can transform **one million molecules of reactant per minute** (Turnover number).",
                "**2. Absolute Specificity:** Each enzyme catalyzes only one specific reaction. *Urease hydrolyzes urea, but has ZERO effect on methylurea!*",
                "**3. Optimum Temperature & pH:** Maximum activity occurs at body temperature (**310 K (37°C)**) and physiological pH (**7.4**). At extreme temperatures or pH, the protein denatures and loses activity permanently.",
                "**4. Co-enzymes & Activators:** Catalytic power increases dramatically in presence of small non-protein molecules (vitamins = co-enzymes) or metal ions (Na^+^, Mn^2+^, Co^2+^, Cu^2+^)."
            ])
        ]
    },

    # ------------------------------------------------------------------ SC-11
    {
        "id": "SC-11",
        "title": "Michaelis-Menten Kinetics: Lock-and-Key Mechanism & Rate Law",
        "blocks": [
            ("lead", "**Enzyme Reaction Kinetics** — The Michaelis-Menten Mechanism (JEE Advanced Quantitative Model)"),
            ("p", "In 1894, Emil Fischer proposed the **Lock-and-Key hypothesis**: the enzyme surface possesses specific active cavities with functional groups (−COOH, −NH~2~, −SH, −OH) that complementary substrate molecules fit into, analogous to a key fitting into a lock."),
            ("h2", "1. Two-Step Kinetic Mechanism"),
            ("p", "• **Step 1: Rapid, reversible binding of Substrate (S) to Enzyme (E):**\n"
                  '  E + S ⇌ ES (Enzyme-Substrate Complex, rate constants k~1~, k~−1~)\n'
                  "• **Step 2: Slow, rate-determining decomposition of complex into Product (P):**\n"
                  "  ES —(k~2~)→ E + P\n"
                  "• Rate of product formation: r = k~2~ [ES]. Applying steady-state approximation (d[ES]/dt = 0):\n"
                  '  **r = (V~max~ [S]) / (K~m~ + [S])**\n'
                  'where V~max~ = k~2~ [E]~0~ is the maximum achievable velocity, and K~m~ = (k~−1~ + k~2~) / k~1~ is the **Michaelis Constant**.'),
            ("h2", '2. Physical Significance of K~m~ and Limiting Kinetic Orders'),
            ("table", ["Substrate Concentration", "Kinetic Condition", "Resulting Rate Law", "Reaction Order"], [
                ['**Very Low: [S] ≪ K~m~**', 'K~m~ + [S] ≈ K~m~', 'r = (V~max~ / K~m~) [S]', "**First Order** with respect to substrate"],
                ['**Very High: [S] ≫ K~m~**', 'K~m~ + [S] ≈ [S]', 'r = V~max~ = constant', "**Zero Order** (Enzyme is completely saturated!)"],
                ['**Equimolar: [S] = K~m~**', 'r = (V~max~ [S]) / (2[S]) = ½ V~max~', 'K~m~ equals the substrate conc at which r = ½ V~max~', "Half-maximal velocity benchmark"]
            ], [22, 24, 34, 20], "Table 2.4 — Kinetic regimes of the Michaelis-Menten equation."),
            ("key", 'Lineweaver-Burk Double Reciprocal Plot: Taking reciprocals of the rate equation gives: 1/r = (K~m~ / V~max~) · (1/[S]) + (1 / V~max~). Plotting 1/r vs 1/[S] gives a straight line with slope = K~m~ / V~max~ and Y-intercept = 1 / V~max~!')
        ]
    }
]
