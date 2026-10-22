"""Part 1: Adsorption Fundamentals, Thermodynamics, Physisorption vs Chemisorption & Isotherms (SC-01 to SC-06)."""
from __future__ import annotations

SHEETS = [
    # ------------------------------------------------------------------ SC-01
    {
        "id": "SC-01",
        "title": "Surface Phenomena: Adsorption vs Absorption, Sorption & Terminology",
        "blocks": [
            ("lead", "**Surface and Interface Phenomena** — Molecular Mechanics at Boundaries (NCERT §5.1)"),
            ("p", "Surfaces arise from the boundary separating two bulk phases. Because boundary molecules lack symmetrical coordination, they possess **unbalanced residual attractive forces**, giving rise to distinct surface phenomena: surface tension, surface energy, and adsorption."),
            ("fig", "adsorption_residual", "Fig. 1.1 — Origin of adsorption: Unbalanced residual forces on surface molecules vs isotropic bulk forces."),
            ("h2", "1. Core Definitions (NCERT §5.1.1)"),
            ("bul", [
                "**Adsorption:** The phenomenon of attracting and retaining molecules of a substance on the **surface of a solid or liquid**, resulting in a **higher concentration of the substance at the surface than in the bulk**. It is strictly a **surface phenomenon**.",
                "**Adsorbate:** The molecular substance or species which concentrates or adsorbs at the surface (e.g. gases like NH~3~, SO~2~, H~2~, or dyes in solution).",
                "**Adsorbent:** The solid or liquid material on whose surface the adsorption takes place (e.g. activated charcoal, silica gel, alumina gel, clay, colloidal metals like finely divided Ni, Pt, Pd). High specific surface area (m^2^/g) maximizes adsorption capacity.",
                "**Desorption:** The reverse process of removing an adsorbed substance from the surface of the adsorbent (typically by heating or lowering pressure).",
                "**Absorption:** The phenomenon in which the substance is **uniformly distributed throughout the body (bulk)** of the solid or liquid. It is strictly a **bulk phenomenon**.",
                "**Sorption:** When both adsorption and absorption occur simultaneously (e.g. dying of cotton fabric — dye initially adsorbs onto cotton fibres and then slowly absorbs into the interior bulk)."
            ]),
            ("h2", "2. Classical Diagnostic Comparison (NCERT Exemplar)"),
            ("table", ["Property / Action", "Adsorption (Surface)", "Absorption (Bulk)"], [
                ["**Definition**", "Concentration at the surface is **higher** than in the bulk", "Uniform concentration throughout the entire bulk of material"],
                ["**Kinetic Rate**", "Rapid initially, then slows down until dynamic equilibrium", "Occurs at a uniform, steady rate throughout"],
                ["**Temperature Effect**", "Decreases with increase in temperature (exothermic)", "Generally independent of temperature or weakly influenced"],
                ["**Classic Laboratory Test**", "**Silica Gel in moist air:** Adsorbs water vapour exclusively onto its outer pores (stays dry inside)", "**Anhydrous CaCl~2~ in moist air:** Absorbs water into its crystal lattice, forming a hydrated liquid solution (deliquescence)"]
            ], [22, 39, 39], "Table 1.1 — Adsorption vs Absorption comparison tested in JEE."),
            ("trap", "CRITICAL TRAP: When NH~3~ gas is exposed to water, it is ABSORBED into the bulk forming NH~4~OH. When NH~3~ is exposed to activated charcoal, it is ADSORBED onto the surface pores! Do not mix up the matrix material!")
        ]
    },

    # ------------------------------------------------------------------ SC-02
    {
        "id": "SC-02",
        "title": "Thermodynamics of Adsorption: Enthalpy, Entropy & Spontaneity",
        "blocks": [
            ("lead", "**Thermodynamic Driving Forces** — Why Adsorption is ALWAYS Exothermic (NCERT §5.1.2)"),
            ("p", "During adsorption, the residual surface attractive forces of the adsorbent are satisfied by forming bonds or physical interactions with adsorbate molecules. This leads to a substantial decrease in surface energy, which is released as thermal energy: **Adsorption is ALWAYS an exothermic process!**"),
            ("h2", "1. Thermodynamic Analysis of the Adsorption Equilibrium"),
            ("bul", [
                "**1. Standard Enthalpy Change (ΔH < 0):** Since surface energy drops when molecules adhere to the surface, heat is released: **ΔH is universally negative (−ve)**. There are NO endothermic adsorptions known under standard conditions!",
                "**2. Standard Entropy Change (ΔS < 0):** Free gas molecules move randomly in three dimensions. When adsorbed on a two-dimensional surface, their translational freedom is heavily restricted: **molecular chaos decreases, so ΔS is universally negative (−ve)**!",
                "**3. Spontaneity Condition (ΔG = ΔH − TΔS < 0):** For adsorption to occur spontaneously at constant temperature and pressure: ΔG = ΔH − TΔS < 0. Since ΔS is negative, the term **−TΔS is POSITIVE (+ve)**! Therefore, for ΔG to be negative, **|ΔH| MUST BE NUMERICALLY GREATER than |TΔS|**!",
                "**4. Dynamic Equilibrium:** As adsorption progresses, active surface sites fill up, ΔH becomes progressively less negative, while −TΔS remains positive. Eventually, **ΔH = TΔS**, yielding **ΔG = 0**. At this point, dynamic adsorption equilibrium is achieved!"
            ]),
            ("h2", "2. Le Chatelier's Principle Applied to Adsorption Equilibrium"),
            ("p", "The reversible adsorption equilibrium of a gas on a solid adsorbent is represented as:\n"
                  "  **Gas (Adsorbate) + Solid (Adsorbent) ⇌ Adsorption Complex + Heat (ΔH < 0)**\n"
                  "• **Effect of Temperature:** Because the forward reaction is exothermic, increasing temperature shifts the equilibrium in the reverse direction according to Le Chatelier's principle. Hence, **adsorption almost always decreases with rising temperature**!\n"
                  '• **Effect of Pressure:** In the forward direction, gaseous molecules condense to a surface film (gas volume decreases, Δn~g~ < 0). Increasing pressure shifts the equilibrium forward: **adsorption increases with increasing gas pressure**!'),
            ("key", "Thermodynamic Gold Rule for JEE: In all spontaneous adsorptions: ΔH < 0, ΔS < 0, and ΔG < 0. As adsorption approaches equilibrium, ΔG becomes less negative until ΔG = 0.")
        ]
    },

    # ------------------------------------------------------------------ SC-03
    {
        "id": "SC-03",
        "title": "Types of Adsorption: Physisorption vs Chemisorption Matrix",
        "blocks": [
            ("lead", "**Physisorption vs Chemisorption** — Physical vs Chemical Forces (NCERT §5.1.3 & Table 5.1)"),
            ("p", "Depending on the nature of the attractive forces binding the adsorbate to the adsorbent, adsorption is classified into **Physical Adsorption (Physisorption)** and **Chemical Adsorption (Chemisorption / Activated Adsorption)**."),
            ("h2", "1. Master Comparison Matrix (NCERT Table 5.1)"),
            ("table", ["Characteristic / Parameter", "Physisorption (van der Waals)", "Chemisorption (Chemical Bonds)"], [
                ["**Cause of Attraction**", "Weak van der Waals dispersion forces", "Strong chemical bonds (covalent or ionic)"],
                ["**Specificity**", "**Non-specific in nature**; any gas can be adsorbed on any solid to some degree", "**Highly specific**; occurs only if chemical bond formation is possible (e.g. O~2~ on metals)"],
                ["**Reversibility**", "**Completely reversible**; desorbs upon decreasing P or heating", "**Irreversible**; desorption often yields a different compound (e.g. O~2~ on C desorbs as CO/CO~2~)"],
                ["**Enthalpy of Adsorption (ΔH)**", "**Low: 20 to 40 kJ/mol** (comparable to heat of liquefaction)", "**High: 80 to 240 kJ/mol** (comparable to chemical bond dissociation energies)"],
                ['**Activation Energy (E~a~)**', "**Negligible or Zero**; occurs readily at low temperatures", "**Significant activation energy required**; often called *Activated Adsorption*"],
                ["**Temperature Effect**", "**Decreases continuously** with rising temperature (isobar slopes down)", '**First increases** (acquires E~a~), reaches a maximum, then **decreases** (exothermic desorption)'],
                ["**Surface Coverage Layers**", "**Forms multimolecular layers** at high gas pressure", "**Strictly unimolecular (monolayer)**; once valence sites are saturated, no further bonding occurs"],
                ["**State of Adsorbate**", "Adsorbate molecules retain their chemical identity intact", "Adsorbate molecules dissociate into atoms or ions (e.g. H~2~ → 2 H atoms on Ni)"]
            ], [18, 41, 41], "Table 1.2 — Comprehensive Physisorption vs Chemisorption comparative matrix."),
            ("trap", "TRAP: Can Physisorption transform into Chemisorption? YES! At low temperatures, H~2~ adsorbs physically on Ni as intact H~2~ molecules (ΔH ≈ 20 kJ/mol). Upon heating, the H-H bond dissociates into chemisorbed hydrogen atoms (ΔH ≈ 180 kJ/mol)!")
        ]
    },

    # ------------------------------------------------------------------ SC-04
    {
        "id": "SC-04",
        "title": "Factors Affecting Adsorption: Critical Temperature & Porosity",
        "blocks": [
            ("lead", "**Factors Governing Gas-Solid Adsorption** — Adsorbent Surface Area & Liquefaction Tendency"),
            ("p", "The extent of adsorption of a gas on a solid surface (x/m, mass of gas adsorbed per gram of adsorbent) is controlled by four macroscopic variables: nature of the gas, surface area of the adsorbent, temperature, and pressure."),
            ("h2", '1. Nature of the Gas & Critical Temperature (T~c~)'),
            ("p", '• **Fundamental Rule:** Easily liquefiable gases (having higher critical temperatures T~c~) possess stronger intermolecular van der Waals forces. Consequently, **gases with higher T~c~ are adsorbed much more readily and to a vastly greater extent**!\n'
                  "• **Adsorption Sequence on Activated Charcoal (NCERT Data):**\n"
                  "  SO~2~ (430 K) > NH~3~ (406 K) > CO~2~ (304 K) > CH~4~ (190 K) > CO (134 K) > N~2~ (126 K) > H~2~ (33 K)"),
            ("table", ["Gas", 'Critical Temp T~c~ (K)', "Volume Adsorbed (mL per g of charcoal at 288 K)", "Reason for Relative Order"], [
                ["**SO~2~**", "430 K", "380 mL", "High polarizability and permanent dipole moment"],
                ["**NH~3~**", "406 K", "181 mL", "Strong hydrogen bonding and dipole interaction"],
                ["**CO~2~**", "304 K", "21.6 mL", "Quadrupole moment and easily compressible"],
                ["**CH~4~**", "190 K", "16.2 mL", "Weak dispersion forces"],
                ["**CO**", "134 K", "9.3 mL", "Very low polarizability"],
                ["**N~2~**", "126 K", "8.0 mL", "Non-polar diatomic gas"],
                ["**H~2~**", "33 K", "4.5 mL", "Extremely tiny molecular mass; weakest dispersion forces"]
            ], [12, 18, 28, 42], "Table 1.3 — Critical temperature vs volume of gas adsorbed on charcoal."),
            ("h2", "2. Specific Surface Area and Activation of Adsorbent"),
            ("bul", [
                "**Surface Area:** Adsorption is directly proportional to the surface area of the adsorbent. Finely divided, powdered, or porous materials (like silica gel, charcoal) provide massive specific surface areas (up to 1000 m^2^/g!).",
                "**Activation of Adsorbent:** Involves increasing the adsorbing power of an adsorbent by: (1) Subdividing it into fine particles; (2) Removing already adsorbed gases by heating in superheated steam or vacuum at 600–1000 K; (3) Creating artificial fissures, cracks, and roughness."
            ]),
            ("key", "Key Exam Takeaway: When asked which gas is adsorbed maximum by charcoal in a given mixture, always select the gas with the **HIGHEST critical temperature (highest boiling point)**!")
        ]
    },

    # ------------------------------------------------------------------ SC-05
    {
        "id": "SC-05",
        "title": "Adsorption Isotherms: The Freundlich Empirical Model",
        "blocks": [
            ("lead", "**Freundlich Adsorption Isotherm** — Quantitative Pressure Dependence at Constant Temperature"),
            ("p", "An **adsorption isotherm** is a mathematical equation or curve representing the variation in the quantity of gas adsorbed by unit mass of solid adsorbent (x/m) with pressure (p) of the gas at **constant temperature**."),
            ("fig", "isotherms", "Fig. 1.2 — Freundlich isotherm curve: three pressure regions and logarithmic linear plot."),
            ("h2", "1. Mathematical Formulation (NCERT §5.1.5)"),
            ("p", "In 1909, Herbert Freundlich proposed the classical empirical relationship:\n"
                  '  **x/m = k · p^1/n^ (n > 1)**\n'
                  "where x = mass of gas adsorbed, m = mass of adsorbent, p = gas pressure, and k, n are empirical constants depending on the nature of the gas, adsorbent, and temperature (n > 1)."),
            ("h2", "2. Behavior in Three Distinct Pressure Domains"),
            ("bul", [
                "**1. At Low Pressure:** Adsorption varies linearly with pressure: 1/n = 1 ⇒ **x/m = k · p^1^**. The curve is a straight line through the origin.",
                "**2. At Intermediate Pressure:** Adsorption depends on a fractional power of pressure: **x/m = k · p^1/n^**, where the exponent **1/n ranges between 0 and 1** (typically 0.1 to 0.5).",
                "**3. At High Pressure:** The surface becomes completely saturated with a layer of gas molecules. Further increase in pressure causes NO additional adsorption: 1/n = 0 ⇒ **x/m = k · p^0^ = constant**!"
            ]),
            ("h2", "3. Logarithmic Linear Form & Graphical Verification"),
            ("p", "Taking logarithms on both sides of the Freundlich equation:\n"
                  "  **log~10~(x/m) = log~10~ k + (1/n) log~10~ p**\n"
                  "• Plotting **log(x/m) on the Y-axis** versus **log p on the X-axis** yields a straight line with:\n"
                  "  - **Slope = 1/n** (must lie between 0 and 1). If slope = 0, adsorption is independent of P; if slope = 1, x/m ∝ p.\n"
                  "  - **Y-Intercept = log k** (antilog of intercept gives the constant k)."),
            ("trap", "TRAP: What is the physical limitation of the Freundlich isotherm? It is purely **EMPIRICAL** and breaks down completely at **HIGH GAS PRESSURES**, where the experimental curve plateaus while the equation predicts a continuous increase!")
        ]
    },

    # ------------------------------------------------------------------ SC-06
    {
        "id": "SC-06",
        "title": "Langmuir Adsorption Isotherm & Adsorption from Solutions",
        "blocks": [
            ("lead", "**Langmuir Kinetic Model & Solution Phase Adsorption** (JEE Advanced Theoretical Extensions)"),
            ("p", "In 1916, Irving Langmuir derived the first theoretical adsorption isotherm from dynamic kinetic considerations, postulating that adsorption occurs until a **single monolayer** saturates fixed elementary sites."),
            ("h2", "1. Langmuir Postulates & Derivation"),
            ("bul", [
                "**Fixed Elementary Sites:** Adsorbent surface contains a fixed number of equivalent active sites, each capable of holding exactly one adsorbate molecule.",
                "**No Lateral Interactions:** Adsorbed molecules do not exert forces on neighbouring sites.",
                "**Dynamic Equilibrium:** Rate of adsorption (condensation) = Rate of desorption (evaporation).\n"
                '  - Rate of adsorption: R~a~ = k~a~ p (1 − θ), where θ is fractional surface coverage.\n'
                '  - Rate of desorption: R~d~ = k~d~ θ.\n'
                '  - At equilibrium: k~a~ p (1 − θ) = k~d~ θ ⇒ **θ = (K p) / (1 + K p)** where K = k~a~ / k~d~ is the adsorption coefficient.',
                "**Final Langmuir Isotherm:** Since x/m ∝ θ: **x/m = (a p) / (1 + b p)** ⇔ **p / (x/m) = (1/a) + (b/a) p**. Plotting p / (x/m) vs p gives a straight line with slope = b/a and intercept = 1/a across ALL pressures!"
            ]),
            ("h2", "2. Adsorption from Solution Phase (NCERT §5.1.6)"),
            ("p", "Solid adsorbents can also adsorb dissolved solutes from liquid solutions (e.g. activated charcoal decolorizing raw brown cane sugar solution by adsorbing coloring pigments; charcoal removing acetic acid from aqueous solution).\n"
                  "• **Modified Freundlich Isotherm for Solutions:** Pressure p is replaced by equilibrium solute **Concentration C**:\n"
                  "  **x/m = k · C^1/n^** ⇔ **log(x/m) = log k + (1/n) log C**\n"
                  "• Extent of adsorption x/m increases with: (1) Increasing solute concentration C; (2) Decreasing temperature; (3) Increasing surface area of adsorbent."),
            ("key", "Freundlich Solution Plot: Plotting log(x/m) vs log C yields a straight line with slope = 1/n and intercept = log k. If 1/n is outside the range 0 to 1, the Freundlich isotherm is invalid.")
        ]
    }
]
