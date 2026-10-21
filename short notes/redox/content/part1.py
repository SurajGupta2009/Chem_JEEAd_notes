"""Redox Reactions — Part 1: Sheets RD-01 to RD-07.

Covers:
- RD-01: The Three Tiers of Redox: Classical, Electronic & Oxidation Number
- RD-02: Rules for Assigning Oxidation Numbers & Periodic Trends
- RD-03: The Peroxide Traps: CrO5, Caro's Acid & Marshall's Acid
- RD-04: Mixed Oxides & Fractional Oxidation States: Fe3O4, Pb3O4, C3O2, Br3O8, S4O6^2-
- RD-05: Chemical Significance: Oxidation Number vs Formal Charge vs Real Charge
- RD-06: Classification of Redox Reactions: Combination, Decomposition, Displacement
- RD-07: Disproportionation, Comproportionation & Non-Redox Traps
"""
from __future__ import annotations

SHEETS = [
    # ------------------------------------------------------------------ RD-01
    {
        "id": "RD-01",
        "title": "The Three Tiers of Redox: Classical, Electronic & Oxidation Number",
        "blocks": [
            ("lead", "**The Evolution of Redox Theory** — NCERT Three-Tier Conceptual Hierarchy"),
            ("p", "Redox processes govern chemistry from metabolic respiration and industrial metallurgy to battery electrochemistry. "
                  "NCERT develops the concept across three historical tiers: Classical (Oxygen/Hydrogen) → Electronic (Electron transfer) → Oxidation Number (Formal bookkeeping)."),
            ("fig", "redox_tiers", "Fig. 1.1 — The conceptual evolution of Redox from Classical to Electronic to Oxidation Number bookkeeping."),
            ("h2", "1. Historical Breakdown of the Three Tiers"),
            ("table", ["Tier", "Core Definition of Oxidation", "Core Definition of Reduction", "Where the Model Breaks Down"], [
                ["Tier 1: Classical (7.1)", "**Addition of Oxygen** or electronegative element; **Removal of Hydrogen** or electropositive element", "**Removal of Oxygen** or electronegative element; **Addition of Hydrogen** or electropositive element", "Fails in reactions with no O or H (e.g. 2Na + Cl~2~ → 2NaCl). Misleads in non-redox oxygen transfers (CaO + SO~3~ → CaSO~4~)."],
                ["Tier 2: Electronic (7.2)", "**Loss of electrons** (OIL: Oxidation Is Loss). Species becomes more positive / less negative.", "**Gain of electrons** (RIG: Reduction Is Gain). Species becomes less positive / more negative.", "Fails in covalent reactions where electrons are merely shifted rather than completely transferred (e.g. H~2~ + Cl~2~ → 2HCl)."],
                ["Tier 3: Oxidation Number (7.3)", "**Increase in Oxidation Number (O.N.)** of an element in the given species.", "**Decrease in Oxidation Number (O.N.)** of an element in the given species.", "Universal operational tool! However, O.N. is a formal book-keeping device; it does NOT imply real physical ionic charges."],
            ], [22, 28, 28, 22], "Table 1.1 — Comparative operational definitions across the three tiers of redox theory."),
            ("h2", "2. Fundamental Terminology in Redox"),
            ("bul", [
                "**Oxidising Agent (Oxidant):** The reactant that supplies electronegative atoms, removes electrons, or undergoes a **decrease in oxidation number**. It oxidises others and is **itself reduced**.",
                "**Reducing Agent (Reductant):** The reactant that supplies electropositive atoms, donates electrons, or undergoes an **increase in oxidation number**. It reduces others and is **itself oxidised**.",
                "**Redox Couple (7.4):** A pair consisting of the oxidised and reduced forms of the same substance taking part in an oxidation or reduction half-reaction, denoted as **Ox / Red** (e.g. Cu^2+^ / Cu, Fe^3+^ / Fe^2+^).",
            ]),
        ],
    },
    # ------------------------------------------------------------------ RD-02
    {
        "id": "RD-02",
        "title": "Rules for Assigning Oxidation Numbers & Periodic Trends",
        "blocks": [
            ("lead", "**Oxidation Number Rules** — The Rigorous Book-Keeping Protocol (NCERT 7.3)"),
            ("p", "Oxidation number denotes the residual charge which an atom appears to have when all other atoms from the molecule "
                  "are removed as ions by counting shared electrons towards the more electronegative partner."),
            ("h2", "1. The Master Axioms for Assigning Oxidation State"),
            ("table", ["Element / Environment", "Assigned Oxidation State", "Exceptions & Severe JEE Traps"], [
                ["Elemental / Free State", "**Strictly 0**", "O~2~, O~3~, P~4~, S~8~, C~60~, Fe, Cl~2~, H~2~ all have O.S. = 0."],
                ["Fluorine (F)", "**Always −1** in ALL compounds", "**NO EXCEPTIONS!** F is the most electronegative element (Pauling 4.0). In HOF, F is −1, O is 0, H is +1."],
                ["Alkali Metals (Group 1: Li, Na, K, Rb, Cs)", "**Always +1** in all compounds", "**NO EXCEPTIONS!** Never exhibits +2 or 0 in compounds."],
                ["Alkaline Earths (Group 2: Be, Mg, Ca, Sr, Ba)", "**Always +2** in all compounds", "**NO EXCEPTIONS!** Only two valence s-electrons."],
                ["Hydrogen (H)", "**+1** with non-metals", "**−1 in metal hydrides** (ionic hydrides: NaH, CaH~2~, LiAlH~4~, NaBH~4~, where metal is less EN)."],
                ["Oxygen (O)", "**Normally −2** (Oxides: H~2~O, CO~2~, MgO)", "• **−1 in Peroxides:** H~2~O~2~, Na~2~O~2~, BaO~2~\n• **−½ in Superoxides:** KO~2~, RbO~2~, CsO~2~\n• **+2 in OF~2~** (F is more EN than O)\n• **+1 in O~2~F~2~** (dioxygen difluoride)\n• **0 in O~2~ and O~3~**; **+½ in O~2~^+^**."],
                ["Halogens (Cl, Br, I)", "**Normally −1** (Halides)", "**Positive O.S. (+1 to +7)** when bonded to more EN atoms (O and F)! E.g. ClO~4~^−^ (+7), Cl~2~O~7~ (+7), IF~7~ (+7), ICl (+1 for I)."],
            ], [22, 28, 50], "Table 1.2 — Universal hierarchical rules for assigning oxidation states."),
            ("h2", "2. Algebraic Sum Rule for Neutral and Polyatomic Species"),
            ("key", "• In a **neutral molecule**, the algebraic sum of oxidation numbers of all atoms is **identically 0**:\n"
                    "  For A~x~B~y~: **x · O.S.(A) + y · O.S.(B) = 0**\n"
                    "• In a **polyatomic ion**, the algebraic sum equals the **net electrical charge** of the ion:\n"
                    "  For [SO~4~]^2−^: O.S.(S) + 4(−2) = −2  ⇒  **O.S.(S) = +6**\n"
                    "• **Periodic Range Limit:** Maximum positive O.S. of a representative element **CANNOT exceed its valence shell group number** (e.g. S cannot exceed +6, P cannot exceed +5, Cr cannot exceed +6). If naive algebra yields > Group Number, look for a **peroxide bridge**!"),
        ],
    },
    # ------------------------------------------------------------------ RD-03
    {
        "id": "RD-03",
        "title": "The Peroxide Traps: CrO5, Caro's Acid & Marshall's Acid",
        "blocks": [
            ("lead", "**Peroxide Traps in Oxidation States** — When Naive Algebra Fails"),
            ("p", "Blind algebraic calculation often produces impossible oxidation states that violate the octet rule or exceed the total valence electrons of the atom. "
                  "Whenever an atom appears to exceed its maximum valence shell group number, draw the Lewis structure to locate peroxo (−O−O−) linkages."),
            ("fig", "peroxides", "Fig. 1.2 — Structures of classic peroxide exceptions: CrO5 (Butterfly), H2SO5 (Caro's), and H2S2O8 (Marshall's)."),
            ("h2", "1. High-Yield Peroxide Traps Comparison"),
            ("table", ["Compound", "Naive Formula O.S.", "True Structural O.S.", "Structural Rationale & Peroxide Bonds"], [
                ["Chromium Pentoxide (CrO~5~)", "Cr + 5(−2) = 0 ⇒ **Cr = +10 (IMPOSSIBLE!)**", "**Cr = +6**", "Butterfly structure: **1 oxo oxygen (=O, −2)** and **4 peroxo oxygens (−O−O−, −1 each)**. Cr has 6 valence electrons!"],
                ["Caro's Acid (H~2~SO~5~)", "2(+1) + S + 5(−2) = 0 ⇒ **S = +8 (IMPOSSIBLE!)**", "**S = +6**", "Peroxomonosulphuric acid: contains one **−O−O−H** peroxide group (−1 each) and three normal oxygens (−2 each). S is max +6."],
                ["Marshall's Acid (H~2~S~2~O~8~)", "2(+1) + 2S + 8(−2) = 0 ⇒ **S = +7 (IMPOSSIBLE!)**", "**Both S = +6**", "Peroxodisulphuric acid: two —SO~3~H units linked by a central **−O−O− peroxide bridge** (−1 each)."],
                ["Pyrosulphuric Acid (H~2~S~2~O~7~)", "2(+1) + 2S + 7(−2) = 0 ⇒ **S = +6**", "**Both S = +6**", "Oleum: contains an **S—O—S bridge**; NO peroxide link!"],
            ], [22, 22, 16, 40], "Table 1.3 — Peroxide species where naive algebraic sum violates maximum oxidation states."),
            ("key", "Peroxide Detection Rule:\n"
                    "If calculated O.S. exceeds maximum group valence (e.g. S in H~2~SO~5~ = +8, Cr in CrO~5~ = +10):\n"
                    "• The actual oxidation state of the central atom is equal to its **maximum group valence** (S = +6, Cr = +6)!\n"
                    "• The excess positive charge is accounted for by **peroxide oxygen atoms having O.S. = −1** instead of −2."),
        ],
    },
    # ------------------------------------------------------------------ RD-04
    {
        "id": "RD-04",
        "title": "Mixed Oxides & Fractional Oxidation States: Fe3O4, Pb3O4, C3O2, Br3O8",
        "blocks": [
            ("lead", "**Fractional Oxidation Numbers & Mixed Oxides** — Atomic Reality vs Averages"),
            ("p", "Fractional oxidation states (e.g. +8/3, +4/3, +2.5) are purely **mathematical averages** resulting from non-equivalent atoms "
                  "of the same element in different oxidation states within the same chemical formula unit (NCERT 7.3.2)."),
            ("fig", "fractionals", "Fig. 1.3 — Fractional oxidation state structures: Carbon Suboxide (C3O2) and Tribromooctaoxide (Br3O8)."),
            ("h2", "1. Classic Mixed-Valence Solids"),
            ("table", ["Formula Unit", "Average Formula O.S.", "True Stoichiometric Composition", "Individual Atomic Oxidation States"], [
                ["Magnetite (Fe~3~O~4~)", "**+8/3** (+2.67)", "Mixed stoichiometric spinel: **FeO · Fe~2~O~3~**", "One **Fe^2+^ (+2)** and two **Fe^3+^ (+3)** ions."],
                ["Red Lead (Pb~3~O~4~ / Sindoor)", "**+8/3** (+2.67)", "Mixed oxide: **2 PbO · PbO~2~**", "Two **Pb^2+^ (+2)** and one **Pb^4+^ (+4)** ions."],
                ["Hausmannite (Mn~3~O~4~)", "**+8/3** (+2.67)", "Mixed oxide: **2 MnO · MnO~2~**", "Two **Mn^2+^ (+2)** and one **Mn^4+^ (+4)** ions."],
                ["Sodium Tetrathionate (Na~2~S~4~O~6~)", "**+2.5** (+5/2)", "^−^O~3~S—S—S—SO~3~^−^", "Two central bridging S atoms = **0**; two terminal S atoms = **+5**."],
                ["Bleaching Powder (CaOCl~2~)", "**0**", "Mixed salt: **Ca^2+^ (OCl)^−^ (Cl)^−^**", "One hypochlorite Cl = **+1**; one chloride Cl = **−1**!"],
                ["Ammonium Nitrate (NH~4~NO~3~)", "**+1**", "Two discrete ions: **NH~4~^+^ and NO~3~^−^**", "Nitrogen in NH~4~^+^ = **−3**; Nitrogen in NO~3~^−^ = **+5**!"],
            ], [22, 16, 26, 36], "Table 1.4 — Deconvolution of fractional and ambiguous average oxidation numbers."),
        ],
    },
    # ------------------------------------------------------------------ RD-05
    {
        "id": "RD-05",
        "title": "Chemical Significance: Oxidation Number vs Formal Charge vs Real Charge",
        "blocks": [
            ("lead", "**Charge Concepts in Chemistry** — Dissecting O.N., Formal Charge & Partial Charge"),
            ("p", "A common source of confusion in JEE Advanced is equating oxidation state with formal charge or partial real charge. "
                  "They represent three distinct theoretical frameworks calculated under entirely different assumptions."),
            ("h2", "1. Conceptual Comparison of the Three Charges"),
            ("table", ["Feature", "Oxidation Number (O.N.)", "Formal Charge (F.C.)", "Real Partial Charge (δ)"], [
                ["Underlying Assumption", "**100% Ionic Limit:** All bonding electrons are assigned entirely to the more electronegative atom.", "**100% Covalent Limit:** All bonding electrons are shared equally (50:50) regardless of EN difference.", "**Actual Physical Charge:** Electron density calculated from dipole moments or quantum wavefunction."],
                ["Calculation Formula", "O.N. = V − N_lone − N_hetero_assigned", "F.C. = V − L − ½ S", "δ = q / e (fractional continuum between −1 and +1)"],
                ["Sensitivity to Electronegativity", "**Extremely sensitive** (step-function: winner takes all)", "**Completely blind** to electronegativity differences", "**Gradual function** of electronegativity difference"],
                ["Example: HCl", "H = **+1**, Cl = **−1**", "H = **0**, Cl = **0**", "H = **+0.18**, Cl = **−0.18**"],
                ["Example: CO", "C = **+2**, O = **−2**", "C = **−1**, O = **+1** (due to dative bond!)", "C = **−0.11**, O = **+0.11** (nearly non-polar, μ = 0.11 D)"],
            ], [18, 28, 28, 26], "Table 1.5 — Rigorous contrast between Oxidation Number, Formal Charge, and Real Charge."),
            ("h2", "2. Rules for Assigning O.N. from Lewis Structures"),
            ("key", "When dealing with organic molecules or coordination complexes, assign O.N. bond-by-bond:\n"
                    "• **Homonuclear Bond (A—A):** Shared pair divided equally → contribution to both atoms = **0**.\n"
                    "• **Heteronuclear Single Bond (A—B where B is more EN):** Both electrons go to B → **A gets +1, B gets −1**.\n"
                    "• **Heteronuclear Double/Triple Bond:** A gets **+2 / +3**, B gets **−2 / −3**.\n"
                    "• **Coordinate Dative Bond (A → B):**\n"
                    "  - If donor A is *less EN* than B: A gets **+2**, B gets **−2**.\n"
                    "  - If donor A is *more EN* than B: Electron pair stays with A → contribution to both = **0**!"),
        ],
    },
    # ------------------------------------------------------------------ RD-06
    {
        "id": "RD-06",
        "title": "Classification of Redox Reactions: Combination, Decomposition, Displacement",
        "blocks": [
            ("lead", "**Types of Redox Reactions (NCERT 7.3.1)** — Mechanistic Classification"),
            ("p", "Redox reactions are classified into four major categories based on the structural rearrangements of reactants and products: "
                  "Combination, Decomposition, Displacement (Metal & Non-Metal), and Disproportionation."),
            ("h2", "1. Combination & Decomposition Reactions"),
            ("table", ["Reaction Type", "General Form", "Key Criteria & Examples", "Non-Redox Traps to Watch"], [
                ["Combination (7.3.1 a)", "A + B → C", "At least one of A or B must be in **elemental form** (O.S. = 0):\n• C(0) + O~2~(0) → C(+4)O~2~(-2)\n• 3Mg(0) + N~2~(0) → Mg~3~(+2)N~2~(-3)\n• CH~4~(-4) + 2O~2~(0) → CO~2~(+4) + 2H~2~O(-2)", "CaO(+2,-2) + SO~3~(+6,-2) → CaSO~4~(+2,+6,-2) is **COMBINATION BUT NOT REDOX**! No change in O.S.!"],
                ["Decomposition (7.3.1 b)", "C → A + B", "Breakdown of a compound into two or more components, where at least one product is an **element**:\n• 2H~2~O(+1,-2) → 2H~2~(0) + O~2~(0)\n• 2KClO~3~(+1,+5,-2) → 2KCl(+1,-1) + 3O~2~(0)", "CaCO~3~(+2,+4,-2) —(Δ)→ CaO(+2,-2) + CO~2~(+4,-2) is **DECOMPOSITION BUT NOT REDOX**! All O.S. unchanged!"],
            ], [20, 16, 34, 30], "Table 1.6 — Combination and decomposition redox pathways contrasted with non-redox analogs."),
            ("h2", "2. Displacement Reactions (7.3.1 c)"),
            ("bul", [
                "**Metal Displacement:** A metal in a compound is displaced by another metal in the uncombined state. The displacing metal must have a **lower standard reduction potential (higher oxidation tendency)**:\n"
                "  • **CuSO~4~(aq) + Zn(s) → ZnSO~4~(aq) + Cu(s)** (Zn is oxidised 0 → +2; Cu is reduced +2 → 0).\n"
                "  • **TiCl~4~(l) + 2Mg(s) → Ti(s) + 2MgCl~2~(s)** (Kroll process for titanium extraction).\n"
                "  • **Cr~2~O~3~(s) + 2Al(s) → Al~2~O~3~(s) + 2Cr(s)** (Aluminothermic Goldschmidt reduction).",
                "**Non-Metal Displacement (Hydrogen Displacement):**\n"
                "  • **Active metals (Group 1 & 2: Na, Ca):** Displace H~2~ from cold water: **2Na + 2H~2~O → 2NaOH + H~2~↑**.\n"
                "  • **Less active metals (Mg, Fe):** Displace H~2~ only from steam: **Mg + H~2~O(g) → MgO + H~2~↑**; **3Fe + 4H~2~O(g) → Fe~3~O~4~ + 4H~2~↑**.\n"
                "  • **Metals above H in ECS (Zn, Fe):** Displace H~2~ from dilute non-oxidising acids (HCl, dil H~2~SO~4~): **Zn + 2HCl → ZnCl~2~ + H~2~↑**.",
                "**Halogen Displacement Activity Order:** **F~2~ > Cl~2~ > Br~2~ > I~2~** (decreases down group):\n"
                "  • Cl~2~(g) + 2KBr(aq) → 2KCl(aq) + Br~2~(l)\n"
                "  • Cl~2~(g) + 2KI(aq) → 2KCl(aq) + I~2~(s)\n"
                "  • F~2~ is so ferocious an oxidant that it attacks water directly: **2F~2~ + 2H~2~O → 4HF + O~2~↑** (cannot displace halogens in aqueous solution!).",
            ]),
        ],
    },
    # ------------------------------------------------------------------ RD-07
    {
        "id": "RD-07",
        "title": "Disproportionation, Comproportionation & Non-Redox Traps",
        "blocks": [
            ("lead", "**Auto-Redox Reactions** — Disproportionation and Comproportionation Criteria"),
            ("p", "In auto-redox reactions, the same element acts simultaneously as the oxidising agent and the reducing agent. "
                  "This requires the element to exist in an **intermediate oxidation state** capable of moving both up and down."),
            ("h2", "1. Disproportionation Reactions (7.3.1 d)"),
            ("key", "**Disproportionation Rule:** A reaction in which an element in one oxidation state is **simultaneously oxidised and reduced**.\n"
                    "• **Condition:** The reacting element must possess at least **three oxidation states**, and must be present in an **intermediate** state.\n"
                    "• Elements in their maximum O.S. (e.g. HNO~3~ where N is +5, KMnO~4~ where Mn is +7, H~2~SO~4~ where S is +6) **CANNOT disproportionate**!"),
            ("table", ["Reacting Element", "Intermediate State", "Disproportionation Reaction", "Products & Final O.S."], [
                ["Hydrogen Peroxide (O)", "O is **−1**", "2 H~2~O~2~(-1) → 2 H~2~O(-2) + O~2~(0)", "Reduced to **H~2~O (−2)**; Oxidised to **O~2~ (0)**"],
                ["Phosphorus (P~4~)", "P is **0**", "P~4~(0) + 3 OH^−^ + 3 H~2~O → **PH~3~(-3) + 3 H~2~PO~2~^−^(+1)**", "Reduced to **PH~3~ (−3)**; Oxidised to **Hypophosphite (+1)**"],
                ["Sulphur (S~8~)", "S is **0**", "S~8~(0) + 12 OH^−^ → **4 S^2−^(-2) + 2 S~2~O~3~^2−^(+2) + 6 H~2~O**", "Reduced to **S^2−^ (−2)**; Oxidised to **Thiosulphate (+2)**"],
                ["Chlorine in Cold Alkali", "Cl is **0**", "Cl~2~(0) + 2 NaOH(cold/dil) → **NaCl(-1) + NaClO(+1) + H~2~O**", "Reduced to **Cl^−^ (−1)**; Oxidised to **Hypochlorite (+1)**"],
                ["Chlorine in Hot Alkali", "Cl is **0**", "3 Cl~2~(0) + 6 NaOH(hot/conc) → **5 NaCl(-1) + NaClO~3~(+5) + 3 H~2~O**", "Reduced to **Cl^−^ (−1)**; Oxidised to **Chlorate (+5)**"],
                ["Fluorine (TRAP!)", "F is **0**", "2 F~2~ + 2 OH^−^ → **2 F^−^ + OF~2~ + H~2~O**", "**NOT DISPROPORTIONATION!** F only reduces (0 → −1). O is oxidised (−2 → +2). F has no positive O.S.!"],
            ], [18, 18, 38, 26], "Table 1.7 — Classic disproportionation reactions and the Fluorine non-disproportionation trap."),
            ("h2", "2. Comproportionation (Synproportionation)"),
            ("p", "The exact reverse of disproportionation: **two different oxidation states of the same element react to form a single intermediate oxidation state**:\n"
                  "• **Ag^2+^ + Ag(s) → 2 Ag^+^** (+2 and 0 → +1)\n"
                  "• **IO~3~^−^(+5) + 5 I^−^(-1) + 6 H^+^ → 3 I~2~(0) + 3 H~2~O** (+5 and −1 → 0 in iodometric titrations!)\n"
                  "• **2 H~2~S(-2) + SO~2~(+4) → 3 S(0) + 2 H~2~O** (Claus process for sulphur recovery)."),
        ],
    },
]
