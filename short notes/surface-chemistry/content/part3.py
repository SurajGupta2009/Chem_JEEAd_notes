"""Part 3: Colloids, Micelles, Preparation, Purification, Electrical Double Layer & Coagulation (SC-12 to SC-18)."""
from __future__ import annotations

SHEETS = [
    # ------------------------------------------------------------------ SC-12
    {
        "id": "SC-12",
        "title": "The Colloidal State: Classification by Physical States of Phases",
        "blocks": [
            ("lead", "**The Colloidal Realm** — Mesoscopic Systems Between Solutions and Suspensions (NCERT §5.3)"),
            ("p", "A **colloid** is a heterogeneous system in which one substance is dispersed (**Dispersed Phase**, diameter 1 to 1000 nm) as very fine particles in another substance called the **Dispersion Medium**. The colloidal state is a state of matter defined by particle dimensions, NOT by chemical composition!"),
            ("h2", "1. True Solution vs Colloid vs Suspension (Dimensional Hierarchy)"),
            ("table", ["Property", "True Solution (Homogeneous)", "Colloidal Sol (Heterogeneous)", "Suspension (Heterogeneous)"], [
                ["**Particle Diameter**", "< 1 nm (< 10 Å)", "**1 to 1000 nm** (10 to 10^4^ Å)", "> 1000 nm (> 10^4^ Å)"],
                ["**Visibility**", "Invisible under all optical microscopes", "Scatters light under ultramicroscope (Tyndall)", "Visible to naked eye or ordinary microscope"],
                ["**Filterability**", "Passes through filter paper and animal parchment", "Passes through ordinary filter paper, but **retained by ultrafilter/parchment**", "Retained by ordinary filter paper"],
                ["**Settling under Gravity**", "Does not settle under any gravity", "Does not settle by gravity; settles only in **ultracentrifuge**", "Settles rapidly under gravity"],
                ["**Colligative Properties**", "High osmotic pressure, ΔT_b, ΔT_f", "**Very small colligative effects** (large particles ⇒ low molarity)", "Practically undetectable"]
            ], [18, 26, 32, 24], "Table 3.1 — Comparative properties of three dispersed systems."),
            ("h2", "2. Master Classification by Physical State (NCERT Table 5.2 — 8 Colloid Types)"),
            ("table", ["Dispersed Phase", "Dispersion Medium", "Type of Colloid", "NCERT Everyday & Laboratory Examples"], [
                ["Solid", "Solid", "**Solid Sol**", "Ruby glass, gem stones, coloured alloys"],
                ["Solid", "Liquid", "**Sol**", "Paints, cell fluids, gold sol, As~2~S~3~ sol, starch in water"],
                ["Solid", "Gas", "**Aerosol (Solid)**", "Smoke, dust storms, automobile exhaust"],
                ["Liquid", "Solid", "**Gel**", "Cheese, butter, jellies, curd, shoe polish"],
                ["Liquid", "Liquid", "**Emulsion**", "Milk, hair cream, cod liver oil, cold cream"],
                ["Liquid", "Gas", "**Aerosol (Liquid)**", "Fog, mist, cloud, insect sprays"],
                ["Gas", "Solid", "**Solid Foam**", "Pumice stone, foam rubber, bread, aerogel"],
                ["Gas", "Liquid", "**Foam**", "Froth, whipped cream, soap lather"]
            ], [16, 18, 22, 44], "Table 3.2 — The 8 types of colloidal systems (Gas in Gas is always a true homogeneous solution!)."),
            ("trap", "TRAP: Why is there NO 'Gas-in-Gas' colloid? Because all gases mix completely by molecular diffusion to form a single, homogeneous thermodynamic phase. Heterogeneous boundary interfaces cannot exist between gases!")
        ]
    },

    # ------------------------------------------------------------------ SC-13
    {
        "id": "SC-13",
        "title": "Lyophilic vs Lyophobic Sols & Particle Architecture",
        "blocks": [
            ("lead", "**Affinity Classification** — Lyophilic ('Solvent-Loving') vs Lyophobic ('Solvent-Hating') Sols"),
            ("p", "Based on the nature of interaction between the dispersed phase and the dispersion medium, colloidal solutions are bifurcated into two drastically different categories."),
            ("h2", "1. Definitive Comparison: Lyophilic vs Lyophobic Sols (NCERT §5.4.2)"),
            ("table", ["Characteristic", "Lyophilic Sols (Intrinsic / Reversible)", "Lyophobic Sols (Extrinsic / Irreversible)"], [
                ["**Preparation**", "Prepared **directly** by shaking/heating with medium (e.g. starch, gelatin, gum, egg albumin in water)", "Cannot be prepared directly; require **special physical or chemical methods** (Bredig arc, peptization)"],
                ["**Affinity & Solvation**", "Strong attractive forces; particles are **heavily solvated (hydrated)** by a thick liquid envelope", "Weak attractive forces; particles are **poorly solvated / bare**"],
                ["**Reversibility**", "**Reversible sols**; if evaporated to dryness, residue reconstitutes sol simply upon adding solvent!", "**Irreversible sols**; once coagulated, adding dispersion medium does NOT reconstitute the sol!"],
                ["**Stability**", "**Extremely stable**; stabilized by BOTH electric charge and thick solvation sheath", "**Inherently unstable**; stabilized solely by electric charge; easily coagulated by trace electrolytes"],
                ["**Viscosity & Surface Tension**", "Viscosity is **much higher** than medium; surface tension is **lower** than medium", "Viscosity and surface tension are **nearly identical** to those of pure dispersion medium"],
                ["**Tyndall Effect & Migration**", "Weak Tyndall effect; particles may migrate in either direction or not at all", "**Strong Tyndall scattering**; particles carry definite positive or negative charge and migrate to one pole"]
            ], [18, 41, 41], "Table 3.3 — Lyophilic vs Lyophobic comparative diagnostic matrix."),
            ("h2", "2. Classification Based on Type of Particles (NCERT §5.4.3)"),
            ("bul", [
                "**1. Multimolecular Colloids:** Consist of aggregates of a large number of atoms or small molecules (diameter < 1 nm) held together by weak van der Waals dispersion forces to achieve colloidal dimensions (1 − 1000 nm). *Examples:* **Gold sol** (consists of clusters of various sizes of thousands of Au atoms); **Sulphur sol** (consists of multimolecular aggregates of S~8~ rings).",
                "**2. Macromolecular Colloids:** Consist of giant individual polymer molecules whose molecular size already falls naturally within the colloidal range (1 − 1000 nm). *Examples:* Naturally occurring macromolecules: **Starch, Cellulose, Proteins, Enzymes**; Synthetic polymers: **Nylon, Polythene, Polystyrene, Synthetic rubber**.",
                "**3. Associated Colloids (Micelles):** Substances that behave as normal strong electrolytes at low concentrations, but aggregate into colloidal particles called **Micelles** above a threshold concentration!"
            ])
        ]
    },

    # ------------------------------------------------------------------ SC-14
    {
        "id": "SC-14",
        "title": "Associated Colloids: Micelles, CMC, Kraft Temperature & Cleansing",
        "blocks": [
            ("lead", "**Associated Colloids (Micelles)** — Thermodynamics of Self-Assembly (NCERT §5.4.3)"),
            ("p", "Certain amphiphilic molecules (soaps, detergents) possess both a long non-polar hydrophobic hydrocarbon chain and a polar hydrophilic ionic head. In aqueous solution at low concentration, they behave as normal 1:1 electrolytes. Above a critical threshold, they spontaneously self-assemble into spherical colloidal aggregates called **Micelles**."),
            ("fig", "micelle_formation", "Fig. 3.1 — Surfactant structure: Sodium stearate, surface monolayer below CMC, and spherical micelle enclosing oil."),
            ("h2", "1. Two Thermodynamic Benchmarks for Micelle Formation"),
            ("bul", [
                "**1. Critical Micelle Concentration (CMC):** The **minimum concentration** of surfactant above which micelle formation begins. Below CMC, the surfactant exists as free unassociated ions; above CMC, all additional surfactant enters micelles. For sodium stearate soap: **CMC ≈ 10^−4^ to 10^−3^ mol/L**.",
                "**2. Kraft Temperature (T_k):** The **minimum temperature** above which the formation of micelles takes place. Below T_k, the surfactant's solubility is too low to reach the CMC; above T_k, solubility increases sharply, permitting micellization.",
                "**Aggregation Number:** The average number of monomer surfactant molecules grouped into a single micelle (typically **50 to 100 molecules** per micelle)."
            ]),
            ("h2", "2. Cleansing Action of Soap (NCERT Mechanism)"),
            ("p", "• Most dirt and grime on fabrics consists of oily or greasy organic deposits that water cannot wet.\n"
                  "• Soap molecules (e.g. Sodium Stearate, C~17~H~35~COO^−^Na^+^) dissolve in water. The non-polar hydrophobic tails (C~17~H~35~^−^) penetrate into the grease droplet, while the negatively charged polar heads (−COO^−^) project outward into the surrounding water.\n"
                  "• This forms an **oil-in-water emulsion droplet** enveloped by a dense negative charge layer. The electrostatic repulsion between identical −COO^−^ heads prevents the droplets from coalescing. Rinsing with running water carries the emulsified oil droplets away!"),
            ("trap", "TRAP: Cleansing in Hard Water — Hard water contains Ca^2+^ and Mg^2+^ ions which precipitate soaps as insoluble scum: 2 C~17~H~35~COO^−^ + Ca^2+^ → (C~17~H~35~COO)~2~Ca ↓. Synthetic detergents (e.g. Sodium Lauryl Sulphate CH~3~(CH~2~)~11~SO~4~^−^Na^+^) work in hard water because their calcium salts are completely soluble!")
        ]
    },

    # ------------------------------------------------------------------ SC-15
    {
        "id": "SC-15",
        "title": "Preparation & Purification of Colloids: Bredig's Arc & Peptization",
        "blocks": [
            ("lead", "**Synthesis and Purification of Colloidal Sols** (NCERT §5.4.4 & §5.4.5)"),
            ("p", "Lyophobic sols cannot be made by simple mixing and require either **Dispersion Methods** (breaking coarse particles down to colloidal size) or **Condensation / Aggregation Methods** (nucleating molecular ions into colloidal clusters)."),
            ("h2", "1. Preparation of Lyophobic Sols"),
            ("table", ["Method Class", "Process Name", "Chemical Equation / Operating Technique", "Key Mechanism"], [
                ["**Dispersion**", "**Bredig's Arc Method**\n(Electro-dispersion)", "An electric arc is struck between two metal electrodes (Au, Ag, Pt) immersed in ice-cold water containing trace KOH.", "The intense heat of the arc vaporizes the metal; the ice-cold bath instantly condenses the vapour into colloidal gold sol. Trace KOH acts as stabilizing electrolyte."],
                ["**Dispersion**", "**Peptization**", "Freshly precipitated Fe(OH)~3~ shaken with trace FeCl~3~ solution → Reddish brown [Fe(OH)~3~]Fe^3+^ sol.", "**Peptization:** The process of converting a freshly prepared precipitate into a colloidal sol by shaking with dispersion medium in presence of a small amount of electrolyte (Peptizing agent)."],
                ["**Condensation**", "**Double Decomposition**", "As~2~O~3~ + 3 H~2~S → **As~2~S~3~(sol)** + 3 H~2~O", "Yellow arsenious sulphide sol; particles preferentially adsorb S^2−^ ions."],
                ["**Condensation**", "**Oxidation**", "SO~2~ + 2 H~2~S —(HNO~3~)→ **3 S(sol)** + 2 H~2~O", "Colloidal sulphur sol formed by bubbling SO~2~ through H~2~S solution."],
                ["**Condensation**", "**Reduction**", "2 AuCl~3~ + 3 SnCl~2~ → **2 Au(sol)** + 3 SnCl~4~", "Reduction of auric chloride by stannous chloride yields **Purple of Cassius** (Gold sol)."],
                ["**Condensation**", "**Hydrolysis**", "FeCl~3~ + 3 H~2~O(boiling) → **Fe(OH)~3~(sol)** + 3 HCl", "Deep red hydrated ferric oxide sol; preferentially adsorbs common Fe^3+^ cation."]
            ], [15, 20, 37, 28], "Table 3.4 — Master methods for the preparation of colloidal solutions."),
            ("h2", "2. Purification of Colloidal Sols (Dialysis & Ultrafiltration)"),
            ("fig", "electrophoresis_dialysis", "Fig. 3.2 — Colloid purification and electrokinetic migration: Dialysis parchment bag and Electrophoresis U-tube."),
            ("bul", [
                "**Dialysis:** The process of removing dissolved crystalloid impurities (electrolytes) from a colloidal sol by diffusion through a semi-permeable membrane (animal bladder, parchment paper, or cellophane). Colloidal particles cannot pass through the membrane pores.",
                "**Electrodialysis:** The dialysis process is slow. When electrodes are placed on either side of the membrane and an electric potential gradient is applied, crystalloid ions migrate out rapidly (**10 to 100 times faster**).",
                "**Ultrafiltration:** Ordinary filter paper (pore size ~thousands of nm) is treated with a **4% solution of nitrocellulose in an alcohol-ether mixture (COLLODION)** and hardened with formaldehyde. This shrinks pore dimensions down to colloidal scale, retaining colloidal particles!"
            ])
        ]
    },

    # ------------------------------------------------------------------ SC-16
    {
        "id": "SC-16",
        "title": "Optical & Kinetic Properties: Tyndall Effect & Brownian Motion",
        "blocks": [
            ("lead", "**Physical Properties of Colloidal Sols** — Optical Scattering & Kinetic Collisions (NCERT §5.4.6)"),
            ("p", "Colloidal systems exhibit unique physical properties that directly confirm their heterogeneous, particulate nature: optical Tyndall scattering, kinetic Brownian motion, and diminutive colligative properties."),
            ("h2", "1. Optical Properties: The Tyndall Effect"),
            ("p", "• When a converging beam of light is passed through a colloidal sol in a dark room and viewed at right angles, the path of light becomes illuminated as a glowing cone (**Tyndall Cone**). This optical scattering of light by colloidal particles is called the **Tyndall Effect**.\n"
                  "• **Two Essential Conditions for Strong Tyndall Scattering (NCERT):**\n"
                  "  1. The **diameter of the dispersed particles** must not be much smaller than the wavelength (λ) of the incident light (d ≈ λ).\n"
                  "  2. The **Refractive Indices of the Dispersed Phase and Dispersion Medium must differ greatly in magnitude**!\n"
                  "• *Why do Lyophilic Sols show weak Tyndall effect?* Because lyophilic particles are heavily solvated by the medium; the refractive index of the particle is almost identical to that of the medium, so light passes through without significant scattering!"),
            ("h2", "2. Kinetic Properties: Brownian Motion"),
            ("bul", [
                "**Discovery & Nature:** Discovered in 1827 by Robert Brown. Under an ultramicroscope, colloidal particles appear as shining points of light executing **continuous, erratic, rapid zig-zag motion** in all directions.",
                "**Physical Cause:** Caused by the **unbalanced bombardment of colloidal particles by the rapid thermal motions of molecules of the dispersion medium** from all sides.",
                "**Two Decisive Factors:** Brownian motion is **faster** when: (1) The particle size is **smaller**; (2) The viscosity of the medium is **lower**. It is completely independent of the chemical nature of the colloid!",
                "**Role in Colloid Stability:** Brownian motion acts as a stirring force opposing gravity, **preventing colloidal particles from settling down**. It is the primary kinetic reason for sol stability!"
            ]),
            ("h2", "3. Color of Colloidal Sols"),
            ("p", "• The color of a colloidal sol depends on the wavelength of light scattered by the dispersed particles, which varies with **particle size and shape**.\n"
                  "• *Example:* Extremely fine gold sol is **red**; as particle size grows, it turns **purple**, then **blue**, and finally **golden yellow**!"),
            ("trap", "TRAP: Colligative Properties of Colloids — Because colloidal particles are massive aggregates, the total number of particles per litre is vastly smaller than in a true solution of the same weight concentration. Hence, osmotic pressure, ΔT_b, and ΔT_f are **extremely tiny** (only osmotic pressure can be accurately measured to determine molar mass of polymers)!")
        ]
    },

    # ------------------------------------------------------------------ SC-17
    {
        "id": "SC-17",
        "title": "Electrical Double Layer, Zeta Potential & Sol Charge Rules",
        "blocks": [
            ("lead", "**Origin of Charge on Colloidal Particles** — Helmholtz Double Layer & Preferential Adsorption"),
            ("p", "Colloidal particles always carry an electric charge (either all positive or all negative in a given sol). Mutual electrostatic repulsion between identical charges prevents them from coagulating into larger non-colloidal aggregates, imparting long-term stability."),
            ("fig", "electrical_double_layer", "Fig. 3.3 — Helmholtz Electrical Double Layer: Stern fixed layer, diffuse mobile layer, and Zeta potential (ζ) decay."),
            ("h2", "1. Preferential Ion Adsorption Axiom (Paneth-Fajans Rule)"),
            ("p", "The colloidal surface preferentially adsorbs from solution that specific ion which is **COMMON TO ITS OWN CRYSTAL LATTICE**!"),
            ("table", ["Reaction Scenario", "Reagents & Relative Proportions", "Ion Adsorbed (Common Ion)", "Sol Nature & Formulation"], [
                ["**AgI Sol in Excess KI**", "Dilute AgNO~3~ added to **excess KI**", "I^−^ is in excess and common to AgI lattice", "**Negatively Charged Sol:**\n**[AgI] I^−^ : K^+^**"],
                ["**AgI Sol in Excess AgNO~3~**", "Dilute KI added to **excess AgNO~3~**", "Ag^+^ is in excess and common to AgI lattice", "**Positively Charged Sol:**\n**[AgI] Ag^+^ : NO~3~^−^**"],
                ["**Ferric Hydroxide Sol**", "FeCl~3~ added to **excess boiling water**", "Fe^3+^ is common to hydrated oxide", "**Positively Charged Sol:**\n**[Fe~2~O~3~·xH~2~O] Fe^3+^ : 3Cl^−^**"],
                ["**Ferric Hydroxide Sol (Base)**", "FeCl~3~ added to **excess NaOH solution**", "OH^−^ is in excess and common to lattice", "**Negatively Charged Sol:**\n**[Fe(OH)~3~] OH^−^ : Na^+^**"]
            ], [20, 26, 28, 26], "Table 3.5 — Classical preferential adsorption charge determinations in JEE Advanced."),
            ("h2", "2. Master Classification of Sols by Charge (NCERT Catalog)"),
            ("table", ["Positively Charged Sols (+ve)", "Negatively Charged Sols (−ve)"], [
                ["• **Hydrated metallic oxides:** Al~2~O~3~·xH~2~O, CrO~3~·xH~2~O, Fe~2~O~3~·xH~2~O\n• **Basic dye stuffs:** Methylene blue sol\n• **Hemoglobin** (in blood)\n• **Oxides:** TiO~2~ sol\n• [AgI]Ag^+^ (in excess AgNO~3~)", "• **Metals:** Copper sol, Silver sol, Gold sol, Platinum sol\n• **Metallic sulphides:** As~2~S~3~, Sb~2~S~3~, CdS sols\n• **Acid dye stuffs:** Eosin, Congo red sol\n• **Natural macromolecular sols:** Starch, Gum, Gelatin, Clay, Charcoal\n• [AgI]I^−^ (in excess KI)"]
            ], [50, 50], "Table 3.6 — Definitive catalog of positive and negative sols."),
            ("key", "Zeta Potential (Electrokinetic Potential ζ): The potential difference between the fixed Stern layer of adsorbed ions and the mobile diffuse layer of counter-ions. High |ζ| > 30 mV maintains mutual repulsion; when |ζ| drops below ~25 mV, coagulation occurs!")
        ]
    },

    # ------------------------------------------------------------------ SC-18
    {
        "id": "SC-18",
        "title": "Coagulation, Hardy-Schulze Rule, Flocculation & Gold Number",
        "blocks": [
            ("lead", "**Precipitation and Protection of Colloidal Sols** (NCERT §5.4.6 & §5.5)"),
            ("p", "The process of aggregating colloidal particles together into larger, non-colloidal clusters that settle down as a precipitate is called **Coagulation, Flocculation, or Precipitation**."),
            ("h2", "1. The Hardy-Schulze Rule (NCERT Formulation)"),
            ("bul", [
                "**1. Sign Rule:** The ion of an added electrolyte carrying a charge **OPPOSITE to that of the colloidal particles** is effective in causing coagulation (called the **Active Ion / Coagulating Ion**).",
                "**2. Valency Rule:** The **coagulating power** of an electrolyte is **directly proportional to the FOURTH POWER of the valency (z^4^)** of the coagulating ion!\n"
                "  **Coagulating Power ∝ z^4^**\n"
                "• **For a Negatively Charged Sol (e.g. As~2~S~3~ sol, Gold sol):** Coagulating ions are cations:\n"
                "  **Al^3+^ > Ba^2+^ > Na^+^**   (Ratios roughly 1000 : 100 : 1!)\n"
                "• **For a Positively Charged Sol (e.g. Fe(OH)~3~ sol):** Coagulating ions are anions:\n"
                "  **[Fe(CN)~6~]^4−^ > PO~4~^3−^ > SO~4~^2−^ > Cl^−^**"
            ]),
            ("h2", "2. Coagulation Value (Flocculation Value)"),
            ("p", "• **Definition:** The minimum concentration of an electrolyte (in **millimoles per litre, mmol/L**) required to cause complete coagulation of a colloidal sol within **two hours**.\n"
                  "• **Inverse Relationship:** A smaller coagulation value signifies a vastly stronger coagulating power:\n"
                  "  **Coagulating Power ∝ 1 / Coagulation Value**\n"
                  "  *Example:* If coagulation value of NaCl = 52 mmol/L and AlCl~3~ = 0.093 mmol/L, Al^3+^ is 52 / 0.093 ≈ 560 times more powerful!"),
            ("h2", "3. Protective Colloids & Zsigmondy's Gold Number"),
            ("p", "• Lyophilic sols are much more stable than lyophobic sols. When a lyophilic colloid (gelatin, gum) is added to a lyophobic sol, it forms a protective hydrophilic sheath around the lyophobic particles, shielding them from coagulation by electrolytes (**Protective Colloid**).\n"
                  "• **Gold Number:** The **minimum mass of protective colloid in milligrams (mg)** required to prevent the coagulation of **10 mL of a standard gold sol** when **1 mL of 10% NaCl solution** is rapidly added to it.\n"
                  "  **Protective Power ∝ 1 / Gold Number**\n"
                  "  *Gelatin (0.005–0.01) > Egg albumin (0.1–0.2) > Gum Arabic (0.15–0.25) > Starch (20–25)*. Gelatin has the highest protective power!"),
            ("trap", "TRAP: Electrophoresis vs Electroosmosis — In electrophoresis, colloidal particles move while the dispersion medium is stationary. In **electroosmosis**, colloidal particles are prevented from moving by a semi-permeable membrane; the **dispersion medium moves** under the applied electric field!")
        ]
    }
]
