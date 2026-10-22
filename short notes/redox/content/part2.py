"""Redox Reactions — Part 2: Sheets RD-07 to RD-12.

Covers:
- RD-07: Balancing Redox Reactions: The Oxidation Number Method
- RD-08: Balancing Redox Reactions: The Ion-Electron (Half-Reaction) Method
- RD-09: The Concept of n-factor: Acids, Bases, Salts & Non-Redox Systems
- RD-10: n-factor in Redox Systems: KMnO4, K2Cr2O7, Oxalates & Ferrous Salts
- RD-11: n-factor in Disproportionation & Complex Mixed Oxidation Systems
- RD-12: The Law of Chemical Equivalence: Gram Equivalents & Normality
"""
from __future__ import annotations

SHEETS = [
    # ------------------------------------------------------------------ RD-07
    {
        "id": "RD-08",
        "title": "Balancing Redox Reactions: The Oxidation Number Method",
        "blocks": [
            ("lead", "**The Oxidation Number Method (NCERT 7.3.2 a)** — Stepwise Algorithm"),
            ("p", "Based on the fundamental principle that the **total increase in oxidation number** of the oxidised species "
                  "must equal the **total decrease in oxidation number** of the reduced species."),
            ("h2", "1. Standard 5-Step Procedural Algorithm"),
            ("bul", [
                "**Step 1 (Identify O.S.):** Write the skeletal equation and assign oxidation states to all atoms to identify which elements are undergoing oxidation and reduction.",
                "**Step 2 (Equalize redox atoms):** Multiply species containing the changing elements by integer coefficients so that the number of atoms undergoing redox changes is equal on both sides.",
                "**Step 3 (Calculate ΔO.N. per formula unit):** Determine the net increase in O.N. per formula unit and net decrease in O.N. per formula unit. Multiply the two reactants by suitable cross-coefficients so that **Total Increase in O.N. = Total Decrease in O.N.**",
                "**Step 4 (Balance charge via H^+^ / OH^−^):**\n"
                "  • In **Acidic Medium:** Add **H^+^** ions to the side that is deficient in positive charge.\n"
                "  • In **Basic Medium:** Add **OH^−^** ions to the side that is deficient in negative charge.",
                "**Step 5 (Balance O and H via H~2~O):** Count Oxygen atoms on both sides and add the required number of **H~2~O molecules** to the oxygen-deficient side. Verify that Hydrogen atoms automatically balance!",
            ]),
            ("h2", "2. Worked Exemplar: Cr~2~O~7~^2−^ + Fe^2+^ in Acidic Medium"),
            ("key", "Balancing Step-by-Step:\n"
                    "1. Skeletal: **Cr~2~O~7~^2−^(+6) + Fe^2+^(+2) → Cr^3+^(+3) + Fe^3+^(+3)**\n"
                    "2. Equalize Cr: Cr~2~O~7~^2−^ → 2 Cr^3+^. Change per Cr = 3 e^-^; **Total decrease per Cr~2~O~7~^2−^ = 2 × 3 = 6**.\n"
                    "3. Fe change: Fe^2+^ → Fe^3+^. **Total increase per Fe^2+^ = 1**.\n"
                    "4. Cross-multiply: **1 Cr~2~O~7~^2−^ + 6 Fe^2+^ → 2 Cr^3+^ + 6 Fe^3+^**\n"
                    "5. Balance charge: Left has (−2 + 6(+2) = +10); Right has (2(+3) + 6(+3) = +24). Need +14 on Left:\n"
                    "   **Cr~2~O~7~^2−^ + 6 Fe^2+^ + 14 H^+^ → 2 Cr^3+^ + 6 Fe^3+^**\n"
                    "6. Balance O via H~2~O: Left has 7 O; add 7 H~2~O to right:\n"
                    "   **Cr~2~O~7~^2−^ + 6 Fe^2+^ + 14 H^+^ → 2 Cr^3+^ + 6 Fe^3+^ + 7 H~2~O** (Completely Balanced!)"),
        ],
    },
    # ------------------------------------------------------------------ RD-08
    {
        "id": "RD-09",
        "title": "Balancing Redox Reactions: The Ion-Electron (Half-Reaction) Method",
        "blocks": [
            ("lead", "**The Half-Reaction Method (NCERT 7.3.2 b)** — Rigorous Charge & Electron Tracking"),
            ("p", "The half-reaction method splits the overall redox reaction into two separate half-reactions: an **Oxidation Half-Reaction (OHR)** "
                  "and a **Reduction Half-Reaction (RHR)**. Each is balanced independently for atoms and electrons, and then combined."),
            ("h2", "1. Universal Half-Reaction Protocol"),
            ("table", ["Step Number", "Operation in Acidic Medium", "Operation in Basic Medium"], [
                ["Step 1: Split", "Split skeletal ionic reaction into OHR and RHR.", "Split skeletal ionic reaction into OHR and RHR."],
                ["Step 2: Balance other atoms", "Balance all atoms other than H and O first.", "Balance all atoms other than H and O first."],
                ["Step 3: Balance O atoms", "Add **H~2~O** to the oxygen-deficient side.", "Add **H~2~O** to the oxygen-deficient side."],
                ["Step 4: Balance H atoms", "Add **H^+^** to the hydrogen-deficient side.", "Add **H~2~O** to H-deficient side and equal **OH^−^** to opposite side (or balance with H^+^ first, then add OH^−^ to neutralize H^+^)."],
                ["Step 5: Balance charge", "Add **electrons (e^−^)** to the more positive side.", "Add **electrons (e^−^)** to the more positive side."],
                ['Step 6: Equalize e^-^ & Add', "Multiply half-reactions by integers so e^−^ cancel, then sum and cancel duplicate H~2~O/H^+^.", "Multiply by integers so e^−^ cancel, then sum and cancel duplicate species."],
            ], [16, 42, 42], "Table 2.1 — Stepwise rules for ion-electron balancing in acidic vs basic media."),
            ("h2", "2. Worked Exemplar: Permanganate + Iodide in Basic Medium (NCERT Problem 7.9)"),
            ("key", "Reaction: **MnO~4~^−^ + I^−^ → MnO~2~ + IO~3~^−^ (Basic Medium)**\n"
                    "• **Oxidation Half-Reaction:** I^−^ → IO~3~^−^\n"
                    "  - Add 3 H~2~O to left: I^−^ + 3 H~2~O → IO~3~^−^\n"
                    "  - Add 6 H^+^ to right: I^−^ + 3 H~2~O → IO~3~^−^ + 6 H^+^\n"
                    "  - Add 6 e^−^ to right: I^−^ + 3 H~2~O → IO~3~^−^ + 6 H^+^ + 6 e^−^\n"
                    "• **Reduction Half-Reaction:** MnO~4~^−^ → MnO~2~\n"
                    "  - Add 2 H~2~O to right: MnO~4~^−^ → MnO~2~ + 2 H~2~O\n"
                    "  - Add 4 H^+^ to left: MnO~4~^−^ + 4 H^+^ → MnO~2~ + 2 H~2~O\n"
                    "  - Add 3 e^−^ to left: MnO~4~^−^ + 4 H^+^ + 3 e^−^ → MnO~2~ + 2 H~2~O\n"
                    "• Multiply RHR by 2 to equalize electrons (6 e^−^):\n"
                    "  **2 MnO~4~^−^ + 8 H^+^ + 6 e^−^ → 2 MnO~2~ + 4 H~2~O**\n"
                    "• Add OHR and RHR: 2 MnO~4~^−^ + I^−^ + 2 H^+^ → 2 MnO~2~ + IO~3~^−^ + H~2~O\n"
                    "• Convert to Basic Medium: add 2 OH^−^ to both sides (2 H^+^ + 2 OH^−^ = 2 H~2~O):\n"
                    "  **2 MnO~4~^−^ + I^−^ + H~2~O → 2 MnO~2~ + IO~3~^−^ + 2 OH^−^** (Completely Balanced!)"),
        ],
    },
    # ------------------------------------------------------------------ RD-09
    {
        "id": "RD-10",
        "title": "The Concept of n-factor: Acids, Bases, Salts & Non-Redox Systems",
        "blocks": [
            ("lead", "**The n-Factor (Valence Factor)** — The Bridge Between Moles and Equivalents"),
            ("p", "The n-factor represents the number of moles of electrons transferred, H^+^ ions replaced, OH^−^ ions furnished, "
                  "or total cationic/anionic charge per mole of the substance in a specific reaction."),
            ("h2", "1. Universal Mathematical Definitions"),
            ("key", "• **Equivalent Weight (E):** **E = Molar Mass (M) / n-factor**\n"
                    "• **Number of Gram Equivalents (eq):** **eq = Weight (w) / E = moles (n) × n-factor**\n"
                    "• **Normality (N):** **N = Molarity (M) × n-factor**"),
            ("h2", "2. n-factor for Non-Redox Species"),
            ("table", ["Substance Category", "Operational Rule for n-factor", "Classic Examples & Key Traps"], [
                ["Acids", "**Basicity:** Number of replaceable H^+^ ions furnished **in that specific reaction**", "• HCl: n = 1; H~2~SO~4~: n = 2 (in full neutralization)\n• H~2~SO~4~ + NaOH → NaHSO~4~ + H~2~O: **n = 1**!\n• **H~3~PO~4~:** Tribasic, **n = 3** (3 P—OH)\n• **H~3~PO~3~:** Dibasic, **n = 2** (2 P—OH, 1 non-ionisable P—H!)\n• **H~3~PO~2~:** Monobasic, **n = 1** (1 P—OH, 2 non-ionisable P—H!)\n• **H~3~BO~3~ (Boric acid):** Monobasic Lewis acid, **n = 1** (accepts OH^−^: B(OH)~4~^−^)"],
                ["Bases", "**Acidity:** Number of replaceable OH^−^ ions furnished in that reaction", "• NaOH: n = 1; Ba(OH)~2~: n = 2\n• Al(OH)~3~ + 2 HCl → Al(OH)Cl~2~ + 2 H~2~O: **n = 2**!"],
                ["Neutral Salts (No redox)", "**Total positive or negative electrical charge** carried by ions per formula unit", "• NaCl: n = 1; Na~2~SO~4~: n = 2; AlCl~3~: n = 3\n• **Al~2~(SO~4~)~3~:** 2 Al^3+^ (+6) or 3 SO~4~^2−^ (−6) ⇒ **n = 6**\n• **Potash Alum [K~2~SO~4~·Al~2~(SO~4~)~3~·24H~2~O]:** K~2~SO~4~ (2) + Al~2~(SO~4~)~3~ (6) ⇒ **n = 8**"],
            ], [20, 35, 45], "Table 2.2 — Systematic determination of n-factor for non-redox substances."),
        ],
    },
    # ------------------------------------------------------------------ RD-10
    {
        "id": "RD-11",
        "title": "n-factor in Redox Systems: KMnO4, K2Cr2O7, Oxalates & Ferrous Salts",
        "blocks": [
            ("lead", "**Redox n-Factor** — Net Electron Transfer per Formula Unit"),
            ("p", "In redox reactions, **n-factor = Total change in oxidation number per molecule/formula unit of reactant** = Number of electrons gained or lost per mole of reactant."),
            ("fig", "nfactor", "Fig. 2.1 — Universal n-factor matrix: KMnO4 in 3 media, K2Cr2O7, and Ferrous Oxalate."),
            ("h2", "1. Potassium Permanganate (KMnO~4~, M = 158 g/mol) in Three Media"),
            ("table", ["Medium", "Reduction Half-Reaction", "Change in O.S. (Δ)", "n-factor", "Equivalent Weight (E)"], [
                ["Acidic Medium (dil H~2~SO~4~)", "MnO~4~^−^(+7) + 8 H^+^ + 5 e^−^ → **Mn^2+^(+2)** + 4 H~2~O", "+7 → +2 (Δ = 5)", "**n = 5**", "**E = M / 5 = 31.6**"],
                ["Neutral or Faintly Alkaline", "MnO~4~^−^(+7) + 2 H~2~O + 3 e^−^ → **MnO~2~(+4)** + 4 OH^−^", "+7 → +4 (Δ = 3)", "**n = 3**", "**E = M / 3 = 52.7**"],
                ["Strongly Alkaline Medium", "MnO~4~^−^(+7) + e^−^ → **MnO~4~^2−^(+6)** (Manganate ion, green)", "+7 → +6 (Δ = 1)", "**n = 1**", "**E = M / 1 = 158.0**"],
            ], [22, 38, 16, 10, 14], "Table 2.3 — Medium-dependent redox behavior of Potassium Permanganate."),
            ("h2", "2. Common Reductants and their n-Factors in JEE"),
            ("table", ["Reductant Species", "Oxidation Half-Reaction", "Atoms Changing O.S.", "n-factor Calculation", "Resulting n-factor"], [
                ["Potassium Dichromate (K~2~Cr~2~O~7~)", "Cr~2~O~7~^2−^(+6) + 14 H^+^ + 6 e^−^ → 2 Cr^3+^(+3)", "2 Cr atoms per molecule", "2 × (6 − 3)", "**n = 6** (E = M/6 = 49.0)"],
                ["Oxalic Acid / Oxalate (H~2~C~2~O~4~ / C~2~O~4~^2−^)", "C~2~O~4~^2−^(+3) → 2 CO~2~(+4) + 2 e^−^", "2 C atoms per molecule", "2 × (4 − 3)", "**n = 2** (E = M/2)"],
                ["Ferrous Sulphate (FeSO~4~)", "Fe^2+^(+2) → Fe^3+^(+3) + e^−^", "1 Fe atom", "1 × (3 − 2)", "**n = 1** (E = M/1)"],
                ["Ferrous Oxalate (FeC~2~O~4~)", 'Fe^2+^ → Fe^3+^ + e^−^ AND C~2~O~4~^2−^ → 2 CO~2~ + 2 e^−^', "**Both cation and anion oxidised!**", "1 (from Fe) + 2 (from C~2~O~4~)", "**n = 3** (E = M/3)"],
                ["Ferric Oxalate [Fe~2~(C~2~O~4~)~3~]", "Fe is already +3 (no ox); 3 C~2~O~4~^2−^ → 6 CO~2~ + 6 e^−^", "6 C atoms", "3 × 2 electrons lost", "**n = 6** (E = M/6)"],
                ["Sodium Thiosulphate (Na~2~S~2~O~3~)", "2 S~2~O~3~^2−^(+2) → S~4~O~6~^2−^(+2.5) + 2 e^−^ (with I~2~)", "2 S atoms per molecule", "2 × (2.5 − 2)", "**n = 1** (E = M/1)"],
            ], [22, 34, 18, 16, 10], "Table 2.4 — Universal reference table for common redox partners in titrations."),
        ],
    },
    # ------------------------------------------------------------------ RD-11
    {
        "id": "RD-12",
        "title": "n-factor in Disproportionation & Complex Mixed Oxidation Systems",
        "blocks": [
            ("lead", "**Advanced n-Factor Calculations** — Disproportionation and Multiple Redox Sites"),
            ("p", "When a single species contains multiple atoms undergoing oxidation/reduction in different directions, "
                  "or undergoes disproportionation, calculate the effective n-factor using total electron exchange."),
            ("h2", "1. Disproportionation n-Factor Formula"),
            ("key", "For an element undergoing disproportionation where one mole undergoes oxidation with change n~1~ and reduction with change n~2~:\n"
                    "• **If 1 mole of reactant splits into both paths:**\n"
                    '  **1 / n~eq~ = 1 / n~1~ + 1 / n~2~ ⇒ n-factor = (n~1~ · n~2~) / (n~1~ + n~2~)**\n'
                    "• **Example 1: Chlorine in Cold/Dilute Alkali:**\n"
                    '  Cl~2~(0) → Cl^−^(−1) [n~1~ = 1 e^-^ per Cl] AND Cl~2~(0) → ClO^−^(+1) [n~2~ = 1 e^-^ per Cl]\n'
                    "  n-factor of Cl~2~ = **(1 × 1) / (1 + 1) = 0.5** per Cl atom (or **1** per Cl~2~ molecule: 2 Cl atoms transfer 1 electron total).\n"
                    "• **Example 2: Chlorine in Hot/Concentrated Alkali:**\n"
                    '  Cl~2~(0) → 5 Cl^−^(−1) (5 e^-^ gained) AND Cl~2~(0) → ClO~3~^−^(+5) (5 e^-^ lost)\n'
                    "  n-factor of Cl~2~ = **(1 × 5) / (1 + 5) = 5/6** per Cl atom (or **5/3** per Cl~2~ molecule)."),
            ("h2", "2. Multi-Element Redox (Cuprous Sulphide Cu~2~S)"),
            ("p", "Consider the oxidation of **Cuprous Sulphide (Cu~2~S)** to **Cu^2+^ + SO~2~** in acidic medium:\n"
                  "• Cu goes from **+1 to +2**: 2 Cu atoms lose **2 × 1 = 2 electrons**.\n"
                  "• S goes from **−2 to +4**: 1 S atom loses **6 electrons**.\n"
                  "• **Total electrons lost per mole of Cu~2~S = 2 + 6 = 8 electrons!**\n"
                  '• Therefore, **n-factor of Cu~2~S = 8** ⇒ **Equivalent Weight E = M / 8**!'),
            ("h2", "3. Partial Redox Reactions"),
            ("bul", [
                "**When a reagent acts BOTH as a redox agent and as an acid/base (salt former):**\n"
                "  Example: **2 KMnO~4~ + 16 HCl → 2 KCl + 2 MnCl~2~ + 5 Cl~2~ + 8 H~2~O**\n"
                "  - Out of 16 moles of HCl: **10 moles are oxidised** to 5 Cl~2~ (lose 10 e^-^), while **6 moles act merely as acid** (forming KCl and MnCl~2~ without changing O.S. −1).\n"
                "  - **n-factor of HCl in this reaction = (Total e^-^ lost) / (Total moles of HCl) = 10 / 16 = 5/8**!\n"
                "  - Equivalent weight of HCl = **M / (5/8) = 1.6 M**.",
            ]),
        ],
    },
    # ------------------------------------------------------------------ RD-12
    {
        "id": "RD-13",
        "title": "The Law of Chemical Equivalence: Gram Equivalents & Normality",
        "blocks": [
            ("lead", "**The Law of Equivalence** — Stoichiometric Calculations Without Balanced Equations"),
            ("p", "The golden rule of volumetric quantitative analysis: **In any chemical reaction, 1 gram equivalent of any reactant "
                  "always reacts completely with 1 gram equivalent of any other reactant to produce 1 gram equivalent of each product.**"),
            ("h2", "1. Universal Equivalence Relations"),
            ("key", "**Law of Chemical Equivalence:** For a general reaction a A + b B → Products:\n"
                    "Equivalents of A = Equivalents of B = Equivalents of each Product\n"
                    "• In terms of mass and equivalent weight: **w~A~ / E~A~ = w~B~ / E~B~**\n"
                    "• In terms of Molarity and Volume (in mL): **(M~A~ · n~A~) · V~A~(mL) = (M~B~ · n~B~) · V~B~(mL)**\n"
                    "• In terms of Normality and Volume: **N~A~ · V~A~ = N~B~ · V~B~**\n"
                    "• **Number of milliequivalents (meq):** **meq = N × V(mL) = M × n-factor × V(mL)**"),
            ("h2", "2. Normality of Resulting Mixtures"),
            ("table", ["Type of Mixture", "Governing Condition", "Resulting Normality Formula"], [
                ["Two Similar Reactants (e.g. two acids or two oxidants)", "Reagents do not react with each other; equivalents are additive", "**N~final~ = (N~1~V~1~ + N~2~V~2~) / (V~1~ + V~2~)**"],
                ["Opposing Reactants (Acid + Base / Oxidant + Reductant)", "Neutralization / Redox reaction consumes equivalents", "If N~1~V~1~ > N~2~V~2~:\n**N~residual~ = (N~1~V~1~ − N~2~V~2~) / (V~1~ + V~2~)**"],
                ["Exact Equivalence Point", "Complete quantitative consumption with zero residual", "**N~1~V~1~ = N~2~V~2~** (Endpoint of titration)"],
            ], [25, 35, 40], "Table 2.5 — Mixture normality equations for quantitative volumetric analysis."),
            ("h2", "3. Advantages Over the Mole Method"),
            ("p", "In the mole method, a balanced chemical equation with correct stoichiometric coefficients is strictly mandatory. "
                  "In the **equivalent method**, stoichiometry is already absorbed into the n-factor! You do NOT need to balance the overall equation — only know the initial and final oxidation states."),
        ],
    },
]
