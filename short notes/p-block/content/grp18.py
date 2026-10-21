# -*- coding: utf-8 -*-
"""Group 18: Noble Gases (5 sheets / pages G18-01 to G18-05)."""

SHEETS = [
    # ------------------------------------------------------------------ G18-01
    {
        "id": "G18-01",
        "title": "G18 Trends, Isolation, Liquid Helium & Clathrate Compounds",
        "blocks": [
            ("lead", "**Group 18: Noble Gases (ns^2 np^6)** — Periodic Trends, Liquid Helium & Clathrates"),
            ("p", "Contains He, Ne, Ar, Kr, Xe, Rn (radioactive). Completely filled valence shells confer extraordinary "
                  "chemical inertness, extremely high ionization energies, and zero electron affinity."),
            ("h2", "1. Periodic Trends in Group 18"),
            ("table", ["Element", "Config.", "Atomic Radius (pm)", "IE-1 (kJ/mol)", "ΔH_eg (kJ/mol)", "Boiling Point (K)"], [
                ["He", "1s^2", "99", "**2372 (Highest in PT!)**", "+48", "**4.2 (Lowest in PT!)**"],
                ["Ne", "[He] 2s^2 2p^6", "160", "2080", "+116", "27.1"],
                ["Ar", "[Ne] 3s^2 3p^6", "190", "1520", "+96", "87.2"],
                ["Kr", "[Ar] 3d^10 4s^2 4p^6", "200", "1351", "+96", "119.7"],
                ["Xe", "[Kr] 4d^10 5s^2 5p^6", "220", "1170", "+77", "165.0"],
                ["Rn", "[Xe] 4f^14 5d^10 6s^2 6p^6", "230", "1037", "+68", "211.0"],
            ], [8, 24, 20, 20, 16, 12], "Table 18.1 — Physical and atomic properties of Noble Gases."),
            ("key", "Helium Records in Chemistry:\n"
                    "• **Highest Ionization Enthalpy** in the entire periodic table (2372 kJ/mol).\n"
                    "• **Lowest Boiling Point** of any known substance (4.2 K at 1 atm).\n"
                    "• Does not solidify even at absolute zero (0 K) under atmospheric pressure; requires ~25 atm pressure!"),
            ("h2", "2. Liquid Helium & Superfluidity (Helium II)"),
            ("p", "Liquid helium undergoes a second-order phase transition at **2.18 K (the λ-point)** from normal liquid Helium I "
                  "to **Helium II (Superfluid)**:\n"
                  "• **Zero Viscosity:** Flows through sub-microscopic capillaries without friction; creeps up and over container walls in a thin Rollin film.\n"
                  "• **Enormous Thermal Conductivity:** ~800 times higher than copper! Liquid Helium II does not boil with bubbles; evaporation occurs silently from the surface."),
            ("h2", "3. Clathrate (Cage / Inclusion) Compounds"),
            ("bul", [
                "**Definition:** Non-stoichiometric guest-host inclusion compounds where noble gas atoms (guest) are physically trapped inside the hydrogen-bonded cage cavities of host molecules (quinol / hydroquinone or ice), without any chemical bonds.",
                "**Conditions for Clathrate Formation:**\n"
                "  • Host: Quinol (p-dihydroxybenzene) crystallised under pressure of noble gas.\n"
                "  • **Ar, Kr, Xe form clathrates** because their atomic radii (1.9 to 2.2 Å) fit snugly into the 4.0 Å cavities.\n"
                "  • **He and Ne do NOT form clathrates!** He and Ne atoms are too small and easily slip through the cavity walls without being trapped.",
            ]),
        ],
    },
    # ------------------------------------------------------------------ G18-02
    {
        "id": "G18-02",
        "title": "Xenon Fluorides: XeF2, XeF4, XeF6 Synthesis, Structure & Hydrolysis",
        "blocks": [
            ("lead", "**Xenon Fluorides (XeFn)** — Bartlett's Discovery, VSEPR Geometries & Hydrolysis"),
            ("p", "In 1962, Neil Bartlett noticed that O2 reacts with PtF6 to form [O2]^+ [PtF6]^-. Knowing the first IE of Xe "
                  "(1170 kJ/mol) is almost identical to that of O2 (1175 kJ/mol), he reacted Xe with PtF6 to synthesize the "
                  "first noble gas compound: **Xe^+ [PtF6]^- (orange-yellow solid)**."),
            ("h2", "1. Controlled Direct Synthesis of Xenon Fluorides"),
            ("table", ["Compound", "Xe : F2 Ratio", "Conditions (T, P)", "Physical State & Geometry"], [
                ["XeF2", "**2 : 1 (Excess Xe)**", "673 K, 1 bar (Nickel tube)", "White solid, sublimes at 298 K; **Linear** (sp^3d)"],
                ["XeF4", "**1 : 5 Ratio**", "873 K, 7 bar (Nickel tube)", "White crystalline solid; **Square Planar** (sp^3d^2)"],
                ["XeF6", "**1 : 20 (Excess F2)**", "573 K, 60-70 bar", "Colorless crystals (yellow liquid); **Distorted Octahedral**"],
            ], [12, 22, 26, 40], "Table 18.2 — Synthetic parameters for Xenon Fluorides (NCERT core)."),
            ("fig", "xenon", "Fig. 18.1 — VSEPR geometries of XeF2 (Linear), XeF4 (Square Planar), XeF6 (Distorted Octahedral)."),
            ("h2", "2. Hydrolysis Pathways of Xenon Fluorides (Crucial JEE Topic)"),
            ("bul", [
                "**1. Hydrolysis of XeF2 (Redox):**\n"
                "   **2 XeF2 + 2 H2O -> 2 Xe↑ + 4 HF + O2↑**   (Xe is reduced +2 -> 0; O is oxidised -2 -> 0).",
                "**2. Hydrolysis of XeF4 (Disproportionation):**\n"
                "   **6 XeF4 + 12 H2O -> 2 XeO3 (+6) + 4 Xe (0) + 24 HF + 3 O2↑**\n"
                "   (Xe(+4) disproportionates into Xe(+6) in XeO3 and Xe(0) gas!).",
                "**3. Hydrolysis of XeF6 (Non-Redox, Stepwise):**\n"
                "   • Partial hydrolysis (1 eq H2O): **XeF6 + H2O -> XeOF4 (colorless liquid) + 2 HF**\n"
                "   • Partial hydrolysis (2 eq H2O): **XeF6 + 2 H2O -> XeO2F2 (colorless solid) + 4 HF**\n"
                "   • Complete hydrolysis (3 eq H2O): **XeF6 + 3 H2O -> XeO3 (explosive solid) + 6 HF**  (All retain Xe in +6 state!).",
            ]),
            ("trap", "TRAP: Hydrolysis of XeF4 is a DISPROPORTIONATION reaction that evolves Xe gas, whereas complete hydrolysis of XeF6 is NON-REDOX and produces explosive solid XeO3 without liberating Xe gas!"),
        ],
    },
    # ------------------------------------------------------------------ G18-03
    {
        "id": "G18-03",
        "title": "Xenon Oxides & Oxofluorides: XeO3, XeO4, XeOF4, XeO2F2",
        "blocks": [
            ("lead", "**Xenon Oxides & Oxofluorides** — VSEPR Geometries, Hybridization & Explosive Nature"),
            ("p", "Xenon forms explosive oxides XeO3, XeO4, and intermediate oxofluorides XeOF4, XeO2F2, XeOF2."),
            ("h2", "1. Comprehensive Structural Matrix of Xenon-Oxygen Compounds"),
            ("table", ["Compound", "Xe Oxid. State", "Hybridization", "Lone Pairs", "VSEPR Shape", "Bond Parameters & Angles"], [
                ["XeO3", "+6", "sp^3", "1 lone pair", "**Pyramidal** (trigonal)", "Three Xe=O bonds (dπ-pπ), angle 103°"],
                ["XeO4", "+8", "sp^3", "0 lone pairs", "**Regular Tetrahedral**", "Four Xe=O double bonds, angle 109.5°"],
                ["XeOF4", "+6", "sp^3d^2", "1 lone pair (trans to =O)", "**Square Pyramidal**", "Four Xe-F basal + one Xe=O apical"],
                ["XeO2F2", "+6", "sp^3d", "1 equatorial lp", "**See-Saw**", "Two equatorial Xe=O + two axial Xe-F"],
                ["XeO3F2", "+8", "sp^3d", "0 lone pairs", "**Trigonal Bipyramidal**", "Three equatorial Xe=O + two axial Xe-F"],
            ], [14, 12, 16, 18, 20, 20], "Table 18.3 — Complete VSEPR geometries of Xenon Oxides and Oxofluorides."),
            ("key", "Pi Bonding in Xenon Oxides:\n"
                    "All Xe=O double bonds in xenon chemistry are formed by **dπ-pπ overlap** (donation of oxygen 2p electrons into empty xenon 5d orbitals). "
                    "For example, XeO3 has 3 dπ-pπ bonds, and XeO4 has 4 dπ-pπ bonds!"),
            ("h2", "2. Xenon Trioxide (XeO3) & Xenates"),
            ("bul", [
                "**Properties of XeO3:** Colorless, hygroscopic, highly explosive crystalline solid. Detonates on touch or heating:\n"
                "  2 XeO3(s) --(shock)--> 2 Xe(g) + 3 O2(g)   (ΔH° = -402 kJ/mol, violent explosion!).",
                "**Reaction with Base (Xenate Ion):** XeO3 dissolves in aqueous base to form xenate ion:\n"
                "  XeO3 + OH^- <===> **[HXeO4]^- (Hydrogen xenate ion)**.\n"
                "  In basic solution, xenate disproportionates slowly into **Perxenate [XeO6]^4-** and Xenon gas:\n"
                "  2 [HXeO4]^- + 2 OH^- -> **[XeO6]^4- (Perxenate, +8 state) + Xe + O2 + 2 H2O**.",
                "**Barium Perxenate Ba2XeO6:** Stable salt. Reacts with cold conc. H2SO4 to yield volatile, highly explosive gaseous **XeO4 (Xenon tetroxide)**:\n"
                "  Ba2XeO6 + 2 H2SO4 -> 2 BaSO4↓ + **XeO4↑** + 2 H2O.",
            ]),
        ],
    },
    # ------------------------------------------------------------------ G18-04
    {
        "id": "G18-04",
        "title": "Xenon Complexes, Fluoro-cations/anions & Bartlett Reaction",
        "blocks": [
            ("lead", "**Xenon Fluoride Complexes** — Fluoride Ion Acceptors vs Donors"),
            ("p", "Xenon fluorides react with fluoride ion acceptors (Lewis acids) to form fluoro-cations, and with "
                  "fluoride ion donors (alkali metal fluorides) to form fluoro-anions."),
            ("h2", "1. Fluoride Ion Donor Reactions (Forming Xenon Cations)"),
            ("p", "With strong covalent Lewis acids (MF5 where M = P, As, Sb, Bi, Ru, Pt, Nb, Ta), XeFn acts as a **fluoride ion donor** [F^- donor]:"),
            ("bul", [
                "• XeF2 + PF5 -> **[XeF]^+ [PF6]^-**   ([XeF]^+ is linear)",
                "• XeF2 + 2 SbF5 -> **[XeF]^+ [Sb2F11]^-**",
                "• XeF4 + SbF5 -> **[XeF3]^+ [SbF6]^-**  ([XeF3]^+ is T-shaped, sp^3d with 2 lone pairs)",
                "• XeF6 + AsF5 -> **[XeF5]^+ [AsF6]^-**  ([XeF5]^+ is square pyramidal, sp^3d^2 with 1 lone pair)",
            ]),
            ("table", ["Xenon Fluoride", "Lewis Acid / Base", "Product Salt Formed", "Role of Xenon Fluoride"], [
                ["XeF2", "PF5 / SbF5", "[XeF]^+ [PF6]^- / [XeF]^+ [SbF6]^-", "**F^- Donor (Lewis Base)**"],
                ["XeF4", "SbF5", "[XeF3]^+ [SbF6]^-", "**F^- Donor (Lewis Base)**"],
                ["XeF6", "AsF5 / SbF5", "[XeF5]^+ [AsF6]^- / [XeF5]^+ [SbF6]^-", "**F^- Donor (Lewis Base)**"],
                ["XeF6", "CsF / RbF (alkali fluorides)", "Cs^+ [XeF7]^- / Cs2[XeF8]", "**F^- Acceptor (Lewis Acid!)**"],
            ], [18, 24, 38, 20], "Table 18.4 — Dual Lewis acid-base behaviour of Xenon Fluorides."),
            ("key", "Dual Nature of XeF6:\n"
                    "XeF6 is amphoteric in the Lewis sense: it can donate F^- to SbF5 to form **[XeF5]^+**, "
                    "and it can accept F^- from alkali fluorides MF to form **[XeF7]^-** or **[XeF8]^2-** (Octafluoroxenate(VI) ion)!"),
            ("h2", "2. Geometry of [XeF8]^2- Anion"),
            ("p", "In Cs2[XeF8] and NO2[XeF8], the [XeF8]^2- anion has 8 bond pairs and 1 lone pair. "
                  "Its structural geometry is a **Square Antiprismatic** arrangement (D_4d symmetry). It is thermally stable up to 400°C."),
        ],
    },
    # ------------------------------------------------------------------ G18-05
    {
        "id": "G18-05",
        "title": "Noble Gas Compounds of Kr, Rn & Applications in JEE",
        "blocks": [
            ("lead", "**Krypton, Radon & JEE Applications** — KrF2, Radon Chemistry & Industrial Uses"),
            ("p", "Beyond Xenon, chemical reactivity in Group 18 is severely limited by ionization energy."),
            ("h2", "1. Chemistry of Krypton & Radon"),
            ("bul", [
                "**Krypton Difluoride (KrF2):** The only well-characterised krypton compound. Prepared by electrical discharge or UV irradiation of Kr + F2 at -196°C:\n"
                "  Kr + F2 --(glow discharge, 77 K)--> **KrF2 (colorless volatile solid)**.\n"
                "  Linear structure (sp^3d, 3 equatorial lone pairs). Thermally unstable (decomposes at 0°C). It is an even **stronger fluorinating agent than XeF2**:\n"
                "  Ag + KrF2 -> AgF2; Au + KrF2 + SbF5 -> **[AuF6]^-** (oxidises Gold to Au(+V)!).",
                "**Radon Chemistry:** Radon is radioactive (Rn-222, t_1/2 = 3.82 days, α-emitter). Forms **RnF2** (identified by radiochemical tracer and electromigration techniques). Covalent chemistry is difficult to study due to intense radiolysis.",
                "**Helium, Neon, Argon:** No neutral isolable chemical compounds known at standard conditions. Molecular ions like HeH^+, He2^+, ArH^+ detected only in mass spectrometers.",
            ]),
            ("h2", "2. Master Summary of Noble Gas Uses in JEE"),
            ("table", ["Gas", "Physical Property Utilised", "Industrial, Laboratory & Medical Applications"], [
                ["Helium (He)", "Low density & non-inflammable", "Filling weather balloons and airships (safe substitute for H2)"],
                ["Helium (He)", "Low solubility in blood at high pressure", "Deep-sea diving gas cylinders (mixture of **80% He + 20% O2**) to prevent the painful decompression sickness ('the bends')"],
                ["Helium (He)", "Extremely low boiling point (4.2 K)", "Cryogenic coolant for superconducting magnets in **MRI (Magnetic Resonance Imaging)** and NMR"],
                ["Neon (Ne)", "Bright orange-red glow in discharge tubes", "**Neon advertising display signs** and beacon lights for airfield navigation (penetrates fog)"],
                ["Argon (Ar)", "Complete chemical inertness & cheap", "Inert gas atmosphere in metallurgical arc-welding of Al and stainless steel; filling incandescent light bulbs"],
                ["Xenon & Krypton", "Intense bright flash on discharge", "High-speed photography strobe flashbulbs; lasers"],
                ["Radon (Rn)", "Radioactive α-emission", "Radiotherapy for cancer treatment; hydrological tracing"],
            ], [15, 30, 55], "Table 18.5 — Practical applications of Noble Gases in JEE."),
        ],
    },
]
