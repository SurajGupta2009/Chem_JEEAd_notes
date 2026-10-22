"""Redox Reactions — Part 3: Sheets RD-13 to RD-18.

Covers:
- RD-13: Redox Titrations: Permanganometry, Dichromatometry, Iodometry & Iodimetry
- RD-14: Electrochemical Cells: The Daniell Cell, Half-Cells & Salt Bridge
- RD-15: Standard Reduction Potentials (NCERT Table 7.1) & Electrochemical Series
- RD-16: Feasibility, Spontaneity, Disproportionation & E° Predictions
- RD-17: Advanced Thermodynamics: ΔG°, Equilibrium Constant K & Cell Potentials
- RD-18: Master Synthesis & Quick-Revision Matrix for JEE Advanced
"""
from __future__ import annotations

SHEETS = [
    # ------------------------------------------------------------------ RD-13
    {
        "id": "RD-14",
        "title": "Redox Titrations: Permanganometry, Dichromatometry & Iodometry",
        "blocks": [
            ("lead", "**Quantitative Redox Titrimetry (NCERT 7.3.3)** — Analytical Applications"),
            ("p", "Redox titrations determine the concentration of unknown reductants or oxidants using solutions of known strength. "
                  "Detection of the stoichiometric equivalence point depends on distinct visual indicator mechanisms."),
            ("fig", "titration", "Fig. 3.1 — Redox titration apparatus and indicator mechanisms: Permanganometry, Dichromatometry, and Iodometry."),
            ("h2", "1. Permanganometry (KMnO~4~ Titrations)"),
            ("bul", [
                "**Self-Indicator Action:** KMnO~4~ acts as its own internal indicator. The intense purple **MnO~4~^−^** ion is reduced to nearly colourless **Mn^2+^** in acidic solution. The very first slight excess drop of KMnO~4~ imparts an unreacted, permanent pale pink colour to the solution.",
                "**Acid Medium Selection (CRITICAL JEE TRAP):**n"
                "  • **Dilute H~2~SO~4~ is strictly used:** It does not react with KMnO~4~ and does not undergo redox decomposition.n"
                "  • **HCl CANNOT BE USED:** KMnO~4~ is strong enough to oxidise Cl^−^ to Cl~2~ gas (**2 KMnO~4~ + 16 HCl → 2 MnCl~2~ + 5 Cl~2~↑**), consuming titrant erroneously.n"
                "  • **HNO~3~ CANNOT BE USED:** HNO~3~ is itself a strong oxidising agent; it competes with KMnO~4~ by oxidising the analyte.",
            ]),
            ("h2", "2. Dichromatometry (K~2~Cr~2~O~7~ Titrations)"),
            ("p", "K~2~Cr~2~O~7~ is a primary standard (obtained highly pure and stable, unlike KMnO~4~). Reduced from orange **Cr~2~O~7~^2−^ (+6)** to green **Cr^3+^ (+3)**.n"
                  "• Because green Cr^3+^ masks visual colour changes, **an external redox indicator (Diphenylamine)** is added. At the end point, excess dichromate oxidises diphenylamine to an intense deep **blue-violet** diphenylbenzidine violet complex.n"
                  "• **HCl can be used here!** Dichromate is a milder oxidant than permanganate and cannot oxidise dilute Cl^−^ to Cl~2~."),
            ("h2", "3. Iodometry vs Iodimetry (JEE Advanced Distinction)"),
            ("table", ["Feature", "Iodimetry (Direct Titration)", "Iodometry (Indirect Titration)"], [
                ["Principle", "**Direct titration** of a reducing agent using a standard solution of Iodine (I~2~).", "**Indirect titration** of an oxidising agent by adding excess KI, then titrating liberated I~2~ against standard Na~2~S~2~O~3~."],
                ["Standard Solution Used", "Standard **I~2~ solution in KI** (forming I~3~^−^)", "Standard **Sodium Thiosulphate (Na~2~S~2~O~3~)**"],
                ["Analytes Determined", "Mild reducing agents: AsO~3~^3−^, Sn^2+^, H~2~S, SO~3~^2−^", "Strong oxidising agents: Cu^2+^, Cr~2~O~7~^2−^, ClO^−^, MnO~4~^−^, H~2~O~2~, O~3~"],
                ["The Classic Cu^2+^ Reaction", "—", '**2 Cu^2+^ + 4 I^−^ → Cu~2~I~2~(s)↓ (white ppt) + I~2~**\nFollowed by: **I~2~ + 2 S~2~O~3~^2−^ → 2 I^−^ + S~4~O~6~^2−^**'],
                ["Indicator Timing Trap", "Starch added at beginning.", "**Starch MUST BE ADDED NEAR THE END POINT** (when solution turns pale straw yellow)! If added too early, I~2~ is trapped irreversibly inside the starch helix."],
            ], [18, 38, 44], "Table 3.1 — Fundamental analytical contrast between Iodimetry and Iodometry."),
        ],
    },
    # ------------------------------------------------------------------ RD-14
    {
        "id": "RD-15",
        "title": "Electrochemical Cells: The Daniell Cell, Half-Cells & Salt Bridge",
        "blocks": [
            ("lead", "**Electrochemical Cells (NCERT 7.4)** — Converting Chemical Energy to Electrical Energy"),
            ("p", "When a redox reaction is carried out indirectly in two separate compartments, electron transfer cannot occur directly. "
                  "Electrons are forced through an external metallic circuit, generating electric current."),
            ("fig", "daniell", "Fig. 3.2 — The Daniell galvanic cell showing anode oxidation, cathode reduction, salt bridge, and electron flow."),
            ("h2", "1. Architecture of the Daniell Cell"),
            ("table", ["Component", "Anode Half-Cell (Left)", "Cathode Half-Cell (Right)"], [
                ["Electrode & Solution", "**Zinc rod** immersed in 1.0 M ZnSO~4~ solution", "**Copper rod** immersed in 1.0 M CuSO~4~ solution"],
                ["Half-Reaction Occurring", "**Oxidation:** Zn(s) → Zn^2+^(aq) + 2 e^−^", "**Reduction:** Cu^2+^(aq) + 2 e^−^ → Cu(s)"],
                ["Electrical Polarity", "**Negative (−)** (Source of electrons)", "**Positive (+)** (Sink for electrons)"],
                ["Electrode Mass Change", "Zinc rod **dissolves / loses mass**", "Copper rod **deposits / gains mass**"],
                ["Standard Potential (E°)", "E°(Zn^2+^/Zn) = **−0.76 V**", "E°(Cu^2+^/Cu) = **+0.34 V**"],
                ['Cell EMF (E°~cell~)', 'E°~cell~ = E°~cathode~ − E°~anode~ = +0.34 V − (−0.76 V) = **+1.10 V**', ""],
            ], [20, 40, 40], "Table 3.2 — Comprehensive operational breakdown of the Daniell cell."),
            ("h2", "2. The Functions of the Salt Bridge"),
            ("key", "The salt bridge is an inverted U-tube filled with an inert electrolyte (KCl, KNO~3~, or NH~4~NO~3~) in agar-agar gel.n"
                    "• **Function 1 (Completes the Circuit):** Allows migration of ions between the two half-cells, maintaining electrical continuity.n"
                    "• **Function 2 (Maintains Electrical Neutrality):** As Zn^2+^ accumulates at anode, Cl^−^ migrates into anode beaker; as Cu^2+^ is consumed at cathode, K^+^ migrates into cathode beaker.n"
                    "• **Function 3 (Eliminates Liquid Junction Potential):** Prevents the accumulation of opposing charges at the liquid-liquid boundary.n"
                    '• **Inertness Constraint:** Velocities (transference numbers) of cation and anion must be nearly identical (u~+~ ≈ u~−~). **KCl cannot be used if half-cell contains Ag^+^, Pb^2+^, or Hg~2~^2+^** because insoluble precipitates (AgCl, PbCl~2~) form and clog the bridge!'),
        ],
    },
    # ------------------------------------------------------------------ RD-15
    {
        "id": "RD-16",
        "title": "Standard Reduction Potentials & The Electrochemical Series",
        "blocks": [
            ("lead", "**Electrochemical Series (NCERT Table 7.1)** — The Absolute Measure of Redox Power"),
            ("p", "Electrode potential (E) is the potential difference between the metal electrode and its surrounding ions in solution. "
                  "By universal IUPAC convention, **all standard potentials (E°) are tabulated as Standard Reduction Potentials (SRP)** at 298 K, 1 atm, and 1.0 M concentration."),
            ("h2", "1. Standard Hydrogen Electrode (SHE / NHE) — The Universal Datum"),
            ("p", "The potential of an individual isolated half-cell cannot be measured. The **Standard Hydrogen Electrode (SHE)** is assigned a potential of **identically 0.00 V at all temperatures**:\n"
                  '2 H^+^(aq, 1.0 M) + 2 e^-^ ⇌ H~2~(g, 1 bar) (E° = 0.00 V)\n'
                  "• Platinized platinum foil coated with finely divided platinum black adsorbs H~2~ gas and establishes rapid thermodynamic equilibrium with aqueous H^+^."),
            ("h2", "2. Master Trends in the Electrochemical Series"),
            ("table", ["Redox Couple (Ox / Red)", "Standard Reduction Potential (E°)", "Chemical Implications & Behavior"], [
                ["F~2~(g) / F^−^", "**+2.87 V (Highest!)**", "**Strongest oxidising agent** known. Fluorine has the greatest tendency to gain electrons and be reduced to F^−^. Cannot be oxidised by any chemical reagent."],
                ["S~2~O~8~^2−^ / SO~4~^2−^", "**+2.01 V**", "Very powerful peroxo oxidant."],
                ["MnO~4~^−^ / Mn^2+^ (acidic)", "**+1.51 V**", "Strong oxidising agent in acidic titrations."],
                ["Cl~2~(g) / Cl^−^", "**+1.36 V**", "Strong oxidant; oxidises Br^−^ and I^−^."],
                ["Cr~2~O~7~^2−^ / Cr^3+^ (acidic)", "**+1.33 V**", "Primary standard oxidant."],
                ["O~2~(g) / H~2~O", "**+1.23 V**", "Thermodynamic boundary for water oxidation."],
                ["Br~2~(l) / Br^−^", "**+1.09 V**", "Moderate oxidant."],
                ["Ag^+^ / Ag", "**+0.80 V**", "Easily reduced to metal."],
                ["Fe^3+^ / Fe^2+^", "**+0.77 V**", "Reversible biochemical / titrimetric couple."],
                ["I~2~(s) / I^−^", "**+0.54 V**", "Mild oxidant / I^−^ is moderate reductant."],
                ["Cu^2+^ / Cu", "**+0.34 V**", "Positive SRP: unreactive towards non-oxidising acids (does not liberate H~2~ from HCl)."],
                ["**2 H^+^ / H~2~(g)**", "**0.00 V (Arbitrary Datum)**", "**Reference benchmark** separating active from noble metals."],
                ["Fe^2+^ / Fe", "**−0.44 V**", "Active metal: dissolves in acid with H~2~ liberation."],
                ["Zn^2+^ / Zn", "**−0.76 V**", "Standard anode; reducing agent."],
                ["Al^3+^ / Al", "**−1.66 V**", "Powerful reductant (thermite process)."],
                ["Mg^2+^ / Mg", "**−2.36 V**", "Reacts with steam / hot water."],
                ["Na^+^ / Na", "**−2.71 V**", "Violently reacts with cold water."],
                ["Li^+^ / Li", "**−3.05 V (Lowest!)**", "**Strongest reducing agent in aqueous solution!** Lithium has the lowest SRP due to immense **Hydration Enthalpy**."],
            ], [22, 28, 50], "Table 7.1 — Standard reduction potentials of selected couples at 298 K."),
        ],
    },
    # ------------------------------------------------------------------ RD-16
    {
        "id": "RD-17",
        "title": "Feasibility, Spontaneity, Disproportionation & E° Predictions",
        "blocks": [
            ("lead", "**Thermodynamic Predictions from E°** — Feasibility Criteria and Latimer Diagrams"),
            ("p", "Standard reduction potentials provide the exact quantitative basis to predict whether a chemical reaction "
                  "will occur spontaneously, whether a metal will liberate hydrogen, and whether a species will disproportionate."),
            ("h2", "1. Spontaneity Rule of Redox Reactions"),
            ("key", '• Standard Cell Potential: **E°~cell~ = E°~cathode~ (SRP of reduction) − E°~anode~ (SRP of oxidation)**\n'
                    "• **Thermodynamic Criterion:** A redox reaction is spontaneous under standard conditions if and only if:\n"
                    '  **E°~cell~ > 0 (Positive EMF)** ⇔ **ΔG° = −n F E°~cell~ < 0**\n'
                    "• **Relative Position Rule:** An oxidising agent can oxidise any reducing agent that lies **BELOW it in the reduction potential series** (more negative SRP)."),
            ("h2", "2. Liberation of Hydrogen Gas from Dilute Acids"),
            ("p", "For a metal to displace H~2~ from dilute acids (2 H^+^ + 2 e^−^ → H~2~, E° = 0.00 V):\n"
                  "• **Requirement:** Metal must have a **NEGATIVE SRP** (E° < 0.00 V). E.g. Zn (−0.76 V), Fe (−0.44 V), Mg (−2.36 V).\n"
                  "• Metals with **POSITIVE SRP** (Cu +0.34 V, Ag +0.80 V, Au +1.50 V) **CANNOT liberate H~2~ from dilute HCl or dil H~2~SO~4~**! "
                  "(They dissolve only in oxidising acids like concentrated HNO~3~ through reduction of nitrogen, not reduction of H^+^!)."),
            ("h2", "3. Latimer Diagrams & The Disproportionation Test (JEE Advanced)"),
            ("p", "A **Latimer diagram** writes oxidation states of an element from left to right in decreasing order:\n"
                  'A —(E~1~°)→ B —(E~2~°)→ C\n'
                  "• **Disproportionation Criterion:** Species B will **spontaneously disproportionate** into A and C if and only if:\n"
                  '  **E°~right~ (E°~2~) > E°~left~ (E°~1~)**\n'
                  '• **Rationale:** In disproportionation: B is reduced to C (Potential = +E°~2~) and B is oxidised to A (Potential = −E°~1~). Net EMF = **E°~2~ − E°~1~ > 0**!\n'
                  "• **Example (Copper in aqueous solution):**\n"
                  '  Cu^2+^ —(+0.15 V)→ Cu^+^ —(+0.52 V)→ Cu\n'
                  '  Here, E°~right~ (+0.52 V) > E°~left~ (+0.15 V).\n'
                  '  Therefore, **Cu^+^ spontaneously disproportionates in water: 2 Cu^+^ → Cu^2+^ + Cu(s)** (E°~net~ = +0.37 V)!'),
        ],
    },
    # ------------------------------------------------------------------ RD-17
    {
        "id": "RD-18",
        "title": "Thermodynamics of Redox: ΔG°, Equilibrium Constant K & Cell Potentials",
        "blocks": [
            ("lead", "**Thermodynamic Interrelations** — Connecting EMF, Free Energy & Equilibrium"),
            ("p", "The electrical work performed by a galvanic cell is quantitatively linked to the decrease in Gibbs free energy "
                  "and the thermodynamic equilibrium constant of the chemical reaction."),
            ("h2", "1. Gibbs Free Energy and Cell Potential"),
            ("key", "**Fundamental Thermodynamic Equation:**n"
                    'Δ G° = −n · F · E°~cell~\n'
                    "where:n"
                    "• **n** = number of moles of electrons transferred in the balanced redox equation.\n"
                    "• **F** = Faraday's constant ≈ **96,485 C/mol** (charge carried by 1 mole of electrons).\n"
                    '• **E°~cell~** = standard electromotive force of the cell in Volts (J/C).\n'
                    '• **Important Property:** Δ G° is an **extensive property** (additive), whereas E° is an **intensive property** (NOT directly additive!).'),
            ("h2", "2. Calculation of Non-Adjacent Half-Cell Potentials (Critical Trap)"),
            ("p", 'To find the potential for a composite couple from two consecutive steps (A —(E~1~°)→ B —(E~2~°)→ C, net A —(E~3~°)→ C):\n'
                  '• **NEVER add potentials directly:** E~3~° ≠ E~1~° + E~2~°!\n'
                  '• **MUST add Gibbs energies:** Δ G~3~° = Δ G~1~° + Δ G~2~°\n'
                  '  −n~3~ F E~3~° = −n~1~ F E~1~° + (−n~2~ F E~2~°)\n'
                  '  E~3~° = (n~1~ E~1~° + n~2~ E~2~°) / n~3~\n'
                  '• **Classic Problem:** Given Fe^3+^ + e^-^ → Fe^2+^ (E~1~° = +0.77 V) and Fe^2+^ + 2e^-^ → Fe (E~2~° = −0.44 V):\n'
                  '  For Fe^3+^ + 3e^-^ → Fe: E~3~° = (1 × 0.77 + 2 × (−0.44)) / 3 = −0.037 V!'),
            ("h2", "3. Relation with Equilibrium Constant (K)"),
            ("p", "At 298 K, substituting R = 8.314 J/(mol K), T = 298 K, and F = 96,485 C/mol:\n"
                  'Δ G° = −RT ln K = −2.303 RT log~10~ K\n'
                  'E°~cell~ = (2.303 RT) / (n F) log~10~ K = (0.0591 / n) log~10~ K\n'
                  '• For the Daniell cell (n = 2, E° = 1.10 V): log~10~ K = (2 × 1.10) / 0.0591 = 37.22 ⇒ K ≈ 1.7 × 10^37^ (reaction goes to absolute completion!).'),
        ],
    },
    # ------------------------------------------------------------------ RD-18
    {
        "id": "RD-19",
        "title": "Master Synthesis & Quick-Revision Matrix for JEE Advanced",
        "blocks": [
            ("lead", "**Master Quick-Revision Matrix** — Core Principles, Decision Algorithms & Traps"),
            ("p", "A consolidated high-density review summarizing the essential rules, calculations, and analytical traps in Redox Reactions & Equivalent Concept."),
            ("h2", "1. Universal 5-Step Redox Diagnostic Protocol"),
            ("bul", [
                "**Step 1: Assign Structural O.S.:** Check for peroxides (CrO~5~ = +6, H~2~SO~5~ = +6, H~2~S~2~O~8~ = +6), mixed oxides (Fe~3~O~4~, Pb~3~O~4~ = +8/3), or fractional chains (C~3~O~2~, S~4~O~6~^2−^).",
                "**Step 2: Identify Redox Roles:** Max O.S. can only be oxidant; Min O.S. can only be reductant; Intermediate O.S. can be both or disproportionate.",
                "**Step 3: Calculate n-factor:**\n"
                "  - For simple redox: n = Total change in O.S. per molecule.\n"
                "  - For multiple oxidised atoms (e.g. FeC~2~O~4~): sum changes (1 + 2 = 3).\n"
                "  - For disproportionation: n = (n~1~ · n~2~) / (n~1~ + n~2~).",
                "**Step 4: Apply Equivalence:** Equivalents of Oxidant = Equivalents of Reductant (N~1~V~1~ = N~2~V~2~). Avoid writing balanced equations unless asked.",
                '**Step 5: Check EMF & Spontaneity:** E°~cell~ = E°~red~,cathode − E°~red~,anode > 0. For Latimer diagrams, disproportionation requires E°~right~ > E°~left~.',
            ]),
            ("h2", "2. Master Summary Table of Key Reagents in Redox Titrations"),
            ("table", ["Reagent", "Medium / Reaction Conditions", "n-factor", "Equivalent Weight (E)", "Special Feature / Indicator"], [
                ["KMnO~4~", "Acidic (dil H~2~SO~4~)", "**5**", "**M / 5 = 31.6**", "Self-indicator (pink endpoint). HCl cannot be used."],
                ["KMnO~4~", "Neutral / Faintly Alkaline", "**3**", "**M / 3 = 52.7**", "Forms brown MnO~2~ precipitate."],
                ["KMnO~4~", "Strongly Alkaline", "**1**", "**M / 1 = 158.0**", "Forms green manganate [MnO~4~]^2−^."],
                ["K~2~Cr~2~O~7~", "Acidic (H~2~SO~4~ or HCl)", "**6**", "**M / 6 = 49.0**", "Primary standard; external indicator: diphenylamine."],
                ["H~2~C~2~O~4~ · 2H~2~O", "Acidic (titration with KMnO~4~)", "**2**", "**M / 2 = 63.0**", 'Primary standard oxalic acid; titration heated to ≈60°C.'],
                ["Na~2~S~2~O~3~ · 5H~2~O", "Iodometry (with I~2~)", "**1**", "**M / 1 = 248.2**", "Starch indicator added near straw-yellow endpoint."],
                ["FeSO~4~ · 7H~2~O", "Redox titrations", "**1**", "**M / 1 = 278.0**", "Green vitriol; oxidised Fe^2+^ → Fe^3+^."],
                ["FeC~2~O~4~", "Acidic (with KMnO~4~)", "**3**", "**M / 3**", "Both Fe^2+^ and C~2~O~4~^2−^ oxidised simultaneously!"],
            ], [18, 26, 12, 16, 28], "Table 3.3 — Universal operational constants for redox volumetric titrations."),
        ],
    },
]
