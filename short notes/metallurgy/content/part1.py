"""Part 1: Minerals, Ores, Concentration, Calcination & Roasting (MT-01 to MT-06)."""
from __future__ import annotations

SHEETS = [
    # ------------------------------------------------------------------ MT-01
    {
        "id": "MT-01",
        "title": "Minerals, Ores, Occurrence of Metals & Planetary Distribution",
        "blocks": [
            ("lead", "**Minerals vs Ores** — Thermodynamic Stability, Terrestrial Abundance & Economic Viability"),
            ("p", "Elements occur in nature either in the **Native (Free) state** or in the **Combined state** depending on their electrochemical reactivity (E°). Highly unreactive noble metals (Au, Pt, and rarely Ag, Cu) occur native. Electropositive metals (s-block, Al, Zn, Fe) possess strongly negative oxidation potentials and occur exclusively as oxides, sulphides, carbonates, halides, or silicates."),
            ("h2", "1. Fundamental Definitions & The Thermodynamic Criterion"),
            ("bul", [
                "**Mineral:** A naturally occurring, homogeneous inorganic substance having a definite chemical composition and crystalline structure found in the Earth's crust.",
                "**Ore:** A mineral from which one or more metals can be extracted **conveniently and profitably (economically viable)**. Hence: *All ores are minerals, but all minerals are NOT ores!*",
                "**Gangue (Matrix):** The non-metallic, undesirable earthy or rocky impurities (silica SiO~2~, clay, silicates, limestone) contaminating the mined mineral ore.",
                "**Abundance Hierarchy in Earth's Crust:** By mass percentage: **O** (46.6%) > **Si** (27.7%) > **Al** (8.1%, most abundant metal) > **Fe** (5.0%, second most abundant metal) > **Ca** > **Na** > **K** > **Mg**."
            ]),
            ("h2", "2. Master Classification Table of Principal Ores (NCERT Table 6.1)"),
            ("table", ["Metal", "Principal Ore", "Chemical Formula", "Class / Type", "Remarks & Traps"], [
                ["**Aluminium**", "Bauxite\nKaolinite (China clay)", "AlO~x~(OH)~3-2x~ (0 < x < 1)\nAl~2~Si~2~O~5~(OH)~4~", "Oxide / Hydroxide\nSilicate clay", "Corundum = α-Al~2~O~3~; Cryolite = Na~3~AlF~6~\nKaolinite is a mineral, not an economic ore"],
                ["**Iron**", "Haematite\nMagnetite\nSiderite\nIron Pyrites", "Fe~2~O~3~\nFe~3~O~4~\nFeCO~3~\nFeS~2~", "Red oxide\nMagnetic mixed oxide\nCarbonate\nDisulphide", "Iron pyrites ('Fool's Gold') is NOT used for Fe extraction due to high S content (used for H~2~SO~4~)"],
                ["**Copper**", "Copper Pyrites (Chalcopyrite)\nMalachite\nCuprite\nCopper Glance (Chalcocite)", "CuFeS~2~\nCuCO~3~·Cu(OH)~2~\nCu~2~O\nCu~2~S", "Mixed sulphide\nBasic carbonate (Green)\nRed oxide (Ruby copper)\nSulphide", "Azurite = 2CuCO~3~·Cu(OH)~2~ (Blue)\nChalcopyrite yields >70% of world's Cu"],
                ["**Zinc**", "Zinc Blende / Sphalerite\nCalamine\nZincite", "ZnS\nZnCO~3~\nZnO", "Sulphide\nCarbonate\nOxide", "Sphalerite crystallizes in ccp (Z=4); Wurtzite is the hcp polymorph"],
                ["**Lead / Tin**", "Galena\nCassiterite (Tinstone)", "PbS\nSnO~2~", "Sulphide\nOxide", "Anglesite = PbSO~4~; Cerussite = PbCO~3~\nCassiterite contains magnetic wolframite impurity"]
            ], [15, 23, 27, 17, 18], "Table 1.1 — Comprehensive ore reference matrix for JEE Advanced."),
            ("trap", "CRITICAL TRAP: Iron Pyrites (FeS~2~) is called 'Fool's Gold'. Even though it contains ≈46.6% iron, it is strictly NEVER used as an ore of iron in commercial metallurgy because the sulphur cannot be completely eliminated, leaving brittle iron (hot shortness). Instead, it is burned exclusively to produce SO~2~ for sulphuric acid manufacture!")
        ]
    },

    # ------------------------------------------------------------------ MT-02
    {
        "id": "MT-02",
        "title": "Physical Beneficiation: Crushing, Gravity Separation & Magnetic Sorting",
        "blocks": [
            ("lead", "**Concentration of Ores (Beneficiation / Dressing)** — Physical Separation Techniques"),
            ("p", "Extraction begins by crushing the mined lumps in jaw crushers followed by pulverization in stamp/ball mills. Beneficiation removes gangue particles to enrich the metal concentration before chemical reduction. Physical methods exploit physical property disparities: density, magnetic susceptibility, or preferential wettability."),
            ("h2", "1. Hydraulic Washing (Gravity Separation / Levigation)"),
            ("p", "• **Physical Principle:** Based on the difference in **specific gravities (densities)** between the heavier ore particles and lighter gangue.\n"
                  "• **Apparatus & Working:** An upward stream of running water flows over a vibrating inclined table with wooden corrugations (Wilfley table) or hydraulic classifiers. The lighter gangue particles are washed away by the water stream, while the heavier ore grains settle in the grooves.\n"
                  '• **Applicability:** Heavily concentrated oxide and native ores: Haematite (Fe~2~O~3~, sp. gr. ≈5.2), Cassiterite (SnO~2~, sp. gr. ≈7.0), and native Gold/Platinum.'),
            ("h2", "2. Magnetic Separation"),
            ("p", "• **Physical Principle:** Exploits differences in **magnetic susceptibility** between the ore and the contaminating gangue particles (either the ore is magnetic and gangue non-magnetic, or vice-versa).\n"
                  "• **Apparatus:** Pulverized ore is dropped onto a moving conveyor belt stretched across two rollers, one of which houses a powerful electromagnet. Non-magnetic particles drop straight down under gravity into the outer receptacle; magnetic particles cling to the belt until it leaves the magnetic field, dropping into an inner bin."),
            ("table", ["Separation Case", "Magnetic Component", "Non-Magnetic Component", "Metallurgical Context"], [
                ["**Wolframite from Tinstone**", "Wolframite: FeWO~4~ + MnWO~4~ (Magnetic)", "Cassiterite: SnO~2~ (Diamagnetic)", "Removal of heavy tungstate impurities from tin ore"],
                ["**Silica from Haematite**", "Haematite: Fe~2~O~3~ / Fe~3~O~4~ (Ferromagnetic)", "Silica / Gangue: SiO~2~ (Diamagnetic)", "Upgrading low-grade iron ores"],
                ["**Rutile from Ilmenite**", "Ilmenite: FeTiO~3~ (Magnetic)", "Rutile: TiO~2~ / Zircon (Non-magnetic)", "Processing monazite beach sands of Kerala"]
            ], [25, 25, 25, 25], "Table 1.2 — Commercial magnetic separation cases tested in JEE Advanced."),
            ("key", 'Key Formula for Specific Gravity Differential: Separation efficiency η ∝ (ρ~ore~ − ρ~fluid~) / (ρ~gangue~ − ρ~fluid~). If ρ~ore~ ≫ ρ~gangue~, gravity separation gives rapid, near-quantitative recovery.')
        ]
    },

    # ------------------------------------------------------------------ MT-03
    {
        "id": "MT-03",
        "title": "Froth Floatation: Collectors, Frothers, Stabilizers & Depressants",
        "blocks": [
            ("lead", "**Froth Floatation Process** — Surface Chemistry of Preferential Wetting (NCERT §6.2.3)"),
            ("p", "Pioneered for concentrating **sulphide ores** (ZnS, PbS, CuFeS~2~, Cu~2~S). Physical basis: **Preferential wettability** — sulphide ore particles are preferentially wetted by non-polar oils (hydrophobic), whereas earthy gangue particles are wetted by water (hydrophilic)."),
            ("fig", "froth_floatation", "Fig. 1.1 — Froth floatation cell: agitator, rising mineral-laden bubbles, collectors, and depressant mechanism."),
            ("h2", "1. Reagents in Froth Floatation: Roles & Chemical Formulations"),
            ("bul", [
                "**1. Frothing Agents (Frothers):** Lower the surface tension of water to produce a stable, persistent foam that carries minerals to the top. *Examples:* **Pine oil**, camphor oil, eucalyptus oil, and higher aliphatic alcohols.",
                "**2. Collectors (Hydrophobizing Agents):** Polar-nonpolar amphiphilic molecules whose polar heads chemisorb onto the metal cations of the sulphide surface, orienting their long non-polar hydrocarbon tails outward into the liquid, rendering the ore hydrophobic! *Examples:* **Sodium/Potassium ethyl xanthate** (C~2~H~5~OCS~2~^−^Na^+^), potassium amyl xanthate, fatty acids.",
                "**3. Froth Stabilizers:** Molecules that stabilize the thin liquid lamellae of the bubbles, preventing premature collapse before skimming. *Examples:* **Aniline** (C~6~H~5~NH~2~) and **Cresols** (o, m, p-CH~3~C~6~H~4~OH).",
                "**4. Depressants (Selective Flotation):** Used when two sulphide ores co-exist in the same deposit (e.g. Galena PbS containing Zinc Blende ZnS). Adding **NaCN or KCN** selectively depresses ZnS by forming a water-soluble coordination complex: **ZnS + 4 CN^−^ → [Zn(CN)~4~]^2−^ + S^2−^**. The complexed zinc remains in solution, while unreacted PbS is collected in the froth! Later, adding an **activator** (CuSO~4~) reactivates ZnS by precipitating insoluble CuS on its surface!"
            ]),
            ("trap", "EXAMINER TRAP: Depressant mechanism is a classic JEE question! In a mixture of PbS and ZnS, adding NaCN does NOT precipitate anything new; it dissolves ZnS as a stable cyanide complex [Zn(CN)~4~]^2−^. Galena (PbS) does NOT form a stable soluble cyanide complex under these conditions and floats freely.")
        ]
    },

    # ------------------------------------------------------------------ MT-04
    {
        "id": "MT-04",
        "title": "Chemical Leaching: Bayer's, Hall's, Serpeck's & Cyanide Processes",
        "blocks": [
            ("lead", "**Hydrometallurgical Leaching** — Selective Chemical Dissolution (NCERT §6.2.4)"),
            ("p", "Leaching is used when the ore is soluble in a specific chemical reagent (acid, base, or complexing ligand) while the gangue impurities remain completely insoluble, or vice-versa. The dissolved metal is subsequently recovered by precipitation or displacement."),
            ("fig", "bayer_process", "Fig. 1.2 — Bayer Process cycle: Digestion under pressure, red mud filtration, seeding neutralization, and calcination."),
            ("h2", "1. Leaching of Bauxite for Pure Alumina (Comparison of 3 Industrial Methods)"),
            ("table", ["Process Name", "Target Impurity in Bauxite", "Leaching Reagent & Reaction", "Precipitation & Calcination Steps"], [
                ["**Bayer's Process**\n(Red Bauxite)", "Mainly Fe~2~O~3~ (red color)\n+ minor SiO~2~, TiO~2~", "Digested with conc. NaOH at 473-523 K, 35-36 bar:\nAl~2~O~3~·2H~2~O + 2NaOH + H~2~O → 2Na[Al(OH)~4~]\nSiO~2~ + 2NaOH → Na~2~SiO~3~ + H~2~O (Red mud filtered)", "Neutralized with CO~2~ gas and seeded with fresh Al(OH)~3~:\n2Na[Al(OH)~4~] + CO~2~ → 2Al(OH)~3~ ↓ + Na~2~CO~3~\nCalcinated at 1470 K: Al(OH)~3~ / Al~2~O~3~·xH~2~O —(Δ)→ Al~2~O~3~ + xH~2~O"],
                ["**Hall's Process**\n(Red Bauxite)", "Fe~2~O~3~, SiO~2~", 'Fused with anhydrous Na~2~CO~3~ at ≈1273 K:\nAl~2~O~3~ + Na~2~CO~3~ → 2NaAlO~2~ + CO~2~ ↑\nFe~2~O~3~ remains unreacted and filtered', "Leach extract bubbled with CO~2~ at 323-333 K:\n2NaAlO~2~ + CO~2~ + 3H~2~O → 2Al(OH)~3~ ↓ + Na~2~CO~3~\nFollowed by calcination to Al~2~O~3~ at 1470 K"],
                ["**Serpeck's Process**\n(White Bauxite)", "Mainly **SiO~2~**\n(Silica-rich, iron-poor)", 'Heated with Coke + N~2~ gas at ≈2073 K:\nAl~2~O~3~ + 3C + N~2~ → 2AlN + 3CO ↑\nSiO~2~ + 2C → Si ↑ + 2CO ↑ (Si volatilizes)', "Hydrolysis of Aluminium Nitride:\nAlN + 3H~2~O → Al(OH)~3~ ↓ + NH~3~ ↑\n*Valuable byproduct: Ammonia gas!* Filtered & calcinated."]
            ], [18, 20, 31, 31], "Table 1.3 — Complete comparative matrix of industrial bauxite leaching processes."),
            ("h2", "2. Mac-Arthur Forrest Cyanide Process for Gold & Silver"),
            ("p", "• **Dissolution (Oxidative Leaching):** Finely powdered native gold or argentite (Ag~2~S) is treated with dilute (0.1–0.2%) NaCN in the presence of air (O~2~ acts as the crucial oxidizing agent!):\n"
                  "  4 Au + 8 CN^−^ + 2 H~2~O + O~2~ → 4 [Au(CN)~2~]^−^ + 4 OH^−^\n"
                  '  Ag~2~S + 4 CN^−^ ⇌ 2 [Ag(CN)~2~]^−^ + S^2−^ (O~2~ oxidizes S^2−^ to SO~4~^2−^ to drive equilibrium forward!)\n'
                  "• **Precipitation (Displacement):** The metal is recovered by adding electropositive **Zinc dust**:\n"
                  "  2 [Au(CN)~2~]^−^ + Zn → [Zn(CN)~4~]^2−^ + 2 Au ↓")
        ]
    },

    # ------------------------------------------------------------------ MT-05
    {
        "id": "MT-05",
        "title": "Conversion to Oxide: Calcination vs Roasting Mechanisms",
        "blocks": [
            ("lead", "**Pyrometallurgical Pre-Treatment** — Why Convert Ores to Oxides Prior to Reduction?"),
            ("p", "Sulphides, carbonates, and hydrated oxides are thermodynamically difficult to reduce directly to metals because their reduction Gibbs energies (ΔG°) are unfavorable, or they form volatile toxic gases. Metal oxides, however, possess well-characterized negative ΔG° curves that are readily reduced by carbon or CO at accessible temperatures!"),
            ("h2", "1. Calcination vs Roasting — Definitive Diagnostic Comparison"),
            ("table", ["Feature / Parameter", "Calcination (Thermal Decomposition)", "Roasting (Thermal Oxidation)"], [
                ["**Atmosphere**", "Heated in **absence or limited supply of air** below its melting point", "Heated in a **regular supply of excess air** below its melting point"],
                ["**Target Ores**", "Hydrated oxides, hydroxides, and **carbonates**", "**Sulphide ores** exclusively (ZnS, PbS, CuFeS~2~)"],
                ["**Chemical Reactions**", "Decomposition & dehydration:\n• CaCO~3~ —(Δ)→ CaO + CO~2~ ↑\n• FeCO~3~ —(Δ)→ FeO + CO~2~ ↑\n• Al~2~O~3~·2H~2~O —(Δ)→ Al~2~O~3~ + 2H~2~O ↑\n• CuCO~3~·Cu(OH)~2~ —(Δ)→ 2CuO + CO~2~ + H~2~O", "Oxidation of metal and non-metal impurities:\n• 2ZnS + 3O~2~ —(Δ)→ 2ZnO + 2SO~2~ ↑\n• 2PbS + 3O~2~ —(Δ)→ 2PbO + 2SO~2~ ↑\n• Impurity oxidation: S + O~2~ → SO~2~ ↑; P~4~ + 5O~2~ → P~4~O~10~ ↑; 4As + 3O~2~ → 2As~2~O~3~ ↑ (volatile)"],
                ["**Physical Change**", "Ore becomes **porous and dry**, expulsion of crystal water and CO~2~", "Ore becomes **porous sintered oxide**; toxic SO~2~ channeled to contact process"],
                ["**Furnace Employed**", "Reverberatory furnace or shaft kiln", "Reverberatory furnace or multiple-hearth roaster"]
            ], [20, 40, 40], "Table 1.4 — Calcination vs Roasting comparison."),
            ("key", "Crucial Physical Benefit of Calcination/Roasting: The expulsion of gaseous products (CO~2~, H~2~O, SO~2~) generates a vast network of internal micro-capillaries. This tremendous **increase in surface porosity** allows gaseous reducing agents (like CO) to rapidly penetrate deep into the ore matrix during blast furnace smelting!"),
            ("trap", "TRAP: Chloridizing Roasting vs Roasting — Roasting with NaCl converts refractory ores into water-soluble chlorides (e.g. Ag~2~S + 2NaCl → 2AgCl + Na~2~S), used prior to cyanidation. Do not confuse standard oxidative roasting with chloridizing roasting!")
        ]
    },

    # ------------------------------------------------------------------ MT-06
    {
        "id": "MT-06",
        "title": "Flux, Gangue & Slag: High-Temperature Acid-Base Chemistry",
        "blocks": [
            ("lead", "**Flux-Gangue-Slag High-Temperature Equilibrium** — High-Temperature Lewis Acid-Base Reactions"),
            ("p", "Even after physical beneficiation, some non-fusible gangue impurities remain embedded in the ore. A **Flux** is a chemical substance added during smelting to react with non-fusible gangue at elevated temperatures, converting it into a **fusible (low-melting), light molten liquid called SLAG**."),
            ("h2", "1. The Slag Equation: Gangue + Flux = Slag"),
            ("p", "• **Physical Properties of Slag:**\n"
                  "  1. **Low Melting Point:** Fusible at furnace operating temperatures.\n"
                  "  2. **Low Density:** Significantly lighter than the molten metal; forms an immiscible floating blanket over the molten metal bath.\n"
                  "  3. **Protective Blanket:** The floating slag layer shields the hot molten metal from aerial re-oxidation by atmospheric O~2~!"),
            ("h2", "2. Classification of Fluxes & Slag Chemistry"),
            ("table", ["Gangue Nature", "Nature of Flux Required", "Flux Substance Added", "Slag Formation Reaction", "Metallurgical System"], [
                ["**Acidic Gangue**\n(Excess SiO~2~, P~4~O~10~)", "**Basic Flux**", "Limestone CaCO~3~ (decomposes to CaO), MgCO~3~, or FeCO~3~", "CaO + SiO~2~ → CaSiO~3~ (Calcium silicate slag)\n6CaO + P~4~O~10~ → 2Ca~3~(PO~4~)~2~ (Thomas slag)", "**Blast Furnace extraction of Iron** (Haematite has quartz SiO~2~ gangue)"],
                ["**Basic Gangue**\n(Excess FeO, CaO, MgO)", "**Acidic Flux**", "Silica sand (SiO~2~) or Borax (Na~2~B~4~O~7~)", "FeO + SiO~2~ → FeSiO~3~ (Ferrous silicate slag)\nCaO + SiO~2~ → CaSiO~3~", "**Extraction of Copper** from chalcopyrite (roasting produces FeO gangue!)"],
                ["**Neutral Flux**", "**Neutral / Fluidity Aid**", "Fluorspar (CaF~2~), Cryolite (Na~3~AlF~6~)", "Does not form new chemical compound; lowers melt viscosity and melting point", "**Hall-Héroult Process** for Alumina"]
            ], [18, 16, 20, 26, 20], "Table 1.5 — Flux and slag systems in extractive metallurgy."),
            ("key", "Thomas Slag (Agricultural Fertilizer): The slag produced during steel manufacturing in the basic Bessemer process contains Ca~3~(PO~4~)~2~·CaSiO~3~. Known as **Thomas Slag**, it is pulverized and sold directly as a rich phosphorus fertilizer for agriculture!")
        ]
    }
]
