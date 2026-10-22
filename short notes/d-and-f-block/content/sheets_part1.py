"""Sheets 1 to 9 for d- and f-Block Elements."""

SHEETS_PART1 = [
    {
        "id": "sheet_01",
        "num": 1,
        "title": "Sheet 01 — Introduction, Position & Ground State Configurations",
        "badge": "d-Block Core",
        "boxes": [
            {
                "title": "1. Position in the Periodic Table & Transition Element Definition",
                "tag": "IUPAC Definition & Scope",
                "accent": "teal",
                "bullets": [
                    "• **Periodic Position:** Lies in the middle of the Periodic Table between s-block (Groups 1-2, highly electropositive metals) and p-block (Groups 13-18, electronegative non-metals). Occupies **Groups 3 to 12 (Periods 4, 5, 6, and 7)**.",
                    "• **Transition Character:** Form a transitional bridge in electronic and chemical behavior from ionic, electropositive s-block elements to covalent, electronegative p-block elements.",
                    "• **IUPAC Formal Definition:** A transition element is defined as an element having an **incompletely filled d-subshell (d^1^ to d^9^)** in its neutral ground state OR in any of its common oxidation states.",
                    "• **Group 12 Non-Transition Enigma (Zn, Cd, Hg):** Zinc ([Ar] 3d^10^ 4s^2^), Cadmium ([Kr] 4d^10^ 5s^2^), and Mercury ([Xe] 4f^14^ 5d^10^ 6s^2^) have completely filled (n−1)d^10^ subshells in both elemental state and common divalent oxidation state (+2).",
                    "• **Why studied with d-block?** They complete the d-block series and show continuous physical trends (complexation with ligands, soft Pearson acid behavior in Hg^2+^), but lack typical transition properties (diamagnetic, colorless salts, low melting points, Hg is liquid).",
                    "• **Four Transition Series:** 3d series (Sc 21 to Zn 30 in Period 4), 4d series (Y 39 to Cd 48 in Period 5), 5d series (La 57, Hf 72 to Hg 80 in Period 6, interrupted by 14 4f lanthanoids), 6d series (Ac 89, Rf 104 to Cn 112 in Period 7, interrupted by 14 5f actinoids)."
                ]
            },
            {
                "title": "2. Electronic Configurations & Thermodynamic Drivers for Anomalies",
                "tag": "Orbital Energetics",
                "accent": "navy",
                "bullets": [
                    "• **General Valence Configuration:** **(n−1)d^1-10^ ns^1-2^** (where n = 4 for 3d, 5 for 4d, 6 for 5d). Note: (n−1)d and ns orbitals possess very close energy levels.",
                    '• **Order of Filling vs Ionization:** By Aufbau rule, 4s orbital fills before 3d in neutral atoms (E~4s~ < E~3d~). However, upon ionization, **4s electrons are ALWAYS lost first** because once 3d is populated, increased nuclear shielding (Z~eff~) lowers 3d energy below 4s (E~3d~ < E~4s~ in cations!).',
                    "• **3d Series Anomalous Configurations:**",
                    "  - **Chromium (Z = 24):** Expected [Ar] 3d^4^ 4s^2^ → **Observed [Ar] 3d^5^ 4s^1^**.",
                    "  - **Copper (Z = 29):** Expected [Ar] 3d^9^ 4s^2^ → **Observed [Ar] 3d^10^ 4s^1^**.",
                    "• **Driving Force Behind Half & Fully Filled Shells:**",
                    '  1. **Exchange Energy (ΔE~ex~):** Quantum mechanical exchange of electrons with parallel spins between degenerate orbitals releases stabilizing energy (K · (n(n-1)) / 2). For 3d^5^, number of pairs = 5 × 4 / 2 = 10; for 3d^4^, pairs = 4 × 3 / 2 = 6. The jump of 4 exchange pairs heavily stabilizes 3d^5^ 4s^1^.',
                    "  2. **Symmetrical Electron Distribution:** Spherical symmetrical charge distribution around nucleus minimizes inter-electronic repulsions.",
                    "• **4d and 5d Anomalies (JEE Advanced Crucial Data):**",
                    "  - **Palladium (Pd, Z = 46):** **[Kr] 4d^10^ 5s^0^** — completely devoid of 5s electrons due to large 4d-5s gap and immense exchange stabilization of d^10^.",
                    "  - **Pt (Z = 78):** [Xe] 4f^14^ 5d^9^ 6s^1^; **Au (Z = 79):** [Xe] 4f^14^ 5d^10^ 6s^1^.",
                    "  - **Mo (Z = 42):** [Kr] 4d^5^ 5s^1^; **Ru (Z = 44):** [Kr] 4d^7^ 5s^1^; **Rh (Z = 45):** [Kr] 4d^8^ 5s^1^; **Ag (Z = 47):** [Kr] 4d^10^ 5s^1^."
                ]
            },
            {
                "title": "3. JEE Advanced Key Takeaways & Common Pitfalls",
                "tag": "Exam Trap Alert",
                "accent": "gold",
                "bullets": [
                    "• **Trap 1:** Writing electronic configuration of ions like Fe^2+^ as [Ar] 3d^4^ 4s^2^. WRONG! 4s electrons are lost FIRST: Fe^2+^ is **[Ar] 3d^6^ 4s^0^**, Sc^3+^ is [Ar] 3d^0^, Cu^+^ is [Ar] 3d^10^.",
                    "• **Trap 2:** Assuming only half-filled and full-filled configurations can have s^1^. In 4d series, Nb ([Kr] 4d^4^ 5s^1^), Ru ([Kr] 4d^7^ 5s^1^), and Rh ([Kr] 4d^8^ 5s^1^) also have 5s^1^ due to subtle balance between pairing energy and orbital contraction.",
                    "• **Trap 3:** Confusing transition elements with d-block elements: All transition elements are d-block elements, but not all d-block elements are transition elements (Zn, Cd, Hg are strictly d-block but not transition)."
                ]
            }
        ]
    },
    {
        "id": "sheet_02",
        "num": 2,
        "title": "Sheet 02 — Physical Properties, Metallic Character & Enthalpies of Atomization",
        "badge": "Lattice & Bonding",
        "boxes": [
            {
                "title": "1. Metallic Bonding & Physical Nature",
                "tag": "Lattice Cohesion",
                "accent": "teal",
                "bullets": [
                    "• **Metallic Characteristics:** Transition elements exhibit typical metallic properties: high tensile strength, ductility, malleability, high thermal and electrical conductivities, and high metallic luster.",
                    "• **Crystal Structures:** Hardness and high density stem from dense metallic packing: bcc (body-centered cubic), ccp/fcc (cubic close-packed), and hcp (hexagonal close-packed) lattices.",
                    "• **Dual Bonding Model:** Metallic bonding in transition metals involves BOTH valence **ns electrons** (delocalized sea) AND unpaired **(n−1)d electrons** (covalent-like directional d-d overlap between adjacent atoms).",
                    "• **Hardness Trend:** High number of unpaired d electrons leads to strong covalent interatomic bonding → metals are hard and possess low volatility. Elements in Group 12 (Zn, Cd, Hg) have no unpaired d electrons (d^10^) → soft metals with low boiling points; Hg is a liquid at room temperature."
                ]
            },
            {
                "title": "2. Melting & Boiling Points",
                "tag": "Thermodynamics",
                "accent": "navy",
                "bullets": [
                    "• **Parabolic Trend:** In each transition series, melting point rises to a maximum near the middle (Group 6: Cr, Mo, W) and then falls regularly towards Group 12.",
                    "• **Record Highs:** **Tungsten (W, 3422 °C)** has the highest melting point of all metals, followed by Rhenium (Re) and Osmium (Os), due to maximum covalent bonding from 5d electrons.",
                    "• **The Dip at Mn and Tc:** Manganese ([Ar] 3d^5^ 4s^2^) and Technetium ([Kr] 4d^5^ 5s^2^) exhibit anomalously lower melting points despite having 5 unpaired d electrons! Reason: Symmetrical stable half-filled d^5^ configuration holds electrons tightly to the nucleus, causing poor delocalization into the metallic lattice and unusual complex crystal structures with longer interatomic bonds."
                ]
            },
            {
                "title": '3. Enthalpy of Atomization (Δ~a~H°)',
                "tag": "NCERT Data & Analysis",
                "accent": "gold",
                "bullets": [
                    "• **Definition:** Enthalpy change when 1 mole of solid metal is dissociated into gaseous atoms: M(s) → M(g). Directly reflects the strength of the metallic crystal lattice.",
                    "• **Correlation with Unpaired Electrons:** Higher number of unpaired d-electrons creates stronger d-d orbital overlap → higher atomization enthalpy.",
                    "• **Series Hierarchy:** **5d series > 4d series > 3d series**. Heavier 4d and 5d metals have much more diffuse d-orbitals that overlap strongly in space (enhanced d-d bonding) → heavier transition metals are noble, hard, and form strong metal-metal clusters (e.g. [Re~2~Cl~8~]^2−^, W~6~Cl~12~).",
                    "• **Group 12 Anomaly:** Zn (126 kJ/mol), Cd, Hg have the lowest atomization enthalpies in their respective series because no d electrons participate in bonding."
                ]
            }
        ]
    },
    {
        "id": "sheet_03",
        "num": 3,
        "title": "Sheet 03 — Atomic & Ionic Radii Trends & Lanthanoid Contraction",
        "badge": "Radii & Contraction",
        "figure": "lanthanoid_contraction",
        "boxes": [
            {
                "title": "1. Trends in Atomic and Ionic Radii in 3d Series",
                "tag": "Shielding vs Nuclear Charge",
                "accent": "teal",
                "bullets": [
                    "• **Across a Series (Sc to Zn):** Radii decrease initially, remain almost flat in the middle, and slightly increase at the end.",
                    '  1. **Sc to Cr (Decrease):** Electrons enter inner (n−1)d subshell. Increase in nuclear charge (Z~eff~) dominates over the screening effect of d electrons → atomic radii contract.',
                    '  2. **Mn to Ni (Nearly Constant):** Increased shielding by added d electrons balances the increased nuclear pull (Z~eff~ ≈ screening) → size remains virtually unchanged (Fe ≈ Co ≈ Ni ≈ 125 pm).',
                    "  3. **Cu to Zn (Slight Expansion):** Filling of d^10^ subshell causes strong electron-electron repulsion among paired electrons which exceeds nuclear attraction, expanding the electron cloud (Cu: 128 pm, Zn: 137 pm).",
                    "• **Ionic Radii:** M^2+^ and M^3+^ follow the same regular decreasing trend across the series due to steadily increasing effective nuclear charge."
                ]
            },
            {
                "title": "2. Lanthanoid Contraction: Origin & Consequences",
                "tag": "High-Yield JEE Core",
                "accent": "navy",
                "bullets": [
                    "• **Down the Group:** Normally, moving from 3d to 4d series increases size due to an extra principal shell (Sc: 162 pm → Y: 180 pm; Ti: 147 pm → Zr: 160 pm).",
                    "• **The 4d ≈ 5d Anomaly:** Moving from 4d to 5d, radii are **almost IDENTICAL** (Zr: 160 pm ≈ Hf: 159 pm; Nb: 146 pm ≈ Ta: 146 pm; Mo: 139 pm ≈ W: 139 pm)!",
                    "• **Origin:** Intervening filling of the **14 4f electrons** before 5d series (Lanthanoids: Ce 58 to Lu 71). The 4f subshell has a diffuse, highly multi-lobed spatial shape with extremely poor screening capability (order: s > p > d > f).",
                    "• **Massive Nuclear Pull:** Nuclear charge increases by 32 units (+32 protons) from 4d to 5d, but poorly screened 4f electrons allow this huge positive charge to pull outer 5d and 6s shells inward with tremendous force, completely cancelling normal shell-expansion.",
                    "• **Key Consequences:**",
                    "  - **Chemical Twins:** Zr/Hf and Nb/Ta have almost identical chemical and physical properties; extremely difficult to separate in nature (require ion-exchange chromatography).",
                    "  - **Abnormal Density Surge:** Since volume is nearly identical to 4d elements but mass is roughly doubled, densities of 5d elements are exceptionally high (**Osmium = 22.59 g/cm^3^, Iridium = 22.56 g/cm^3^** — densest known substances!).",
                    "  - **Basic Strength of Hydroxides:** Size decreases from La^3+^ to Lu^3+^ → covalent character increases (Fajans' rule) → basic strength decreases: **La(OH)~3~ is most basic, Lu(OH)~3~ is least basic**."
                ]
            }
        ]
    },
    {
        "id": "sheet_04",
        "num": 4,
        "title": "Sheet 04 — Ionization Enthalpy Patterns & Irregularities",
        "badge": "Ionization & Orbitals",
        "boxes": [
            {
                "title": '1. Trends in Ionization Enthalpies (IE~1~, IE~2~, IE~3~)',
                "tag": "NCERT Data Analysis",
                "accent": "teal",
                "bullets": [
                    "• **General Across 3d Series:** Ionization enthalpies increase from left to right, but much less steeply than in s and p blocks because additional electrons enter inner (n−1)d subshell, partially shielding outer ns electrons.",
                    '• **IE~1~ Trends:** Sc (631) to Zn (906 kJ/mol). Highest IE~1~ in Zn due to removal of electron from completely filled, stable 4s^2^ orbital.',
                    '• **IE~2~ Anomalies (Extremely High Values for Cr and Cu):**',
                    '  - **Cr (1592 kJ/mol):** Second electron must be removed from stable half-filled **3d^5^** (Cr^+^: [Ar] 3d^5^ → Cr^2+^: 3d^4^). Loss of exchange energy makes IE~2~ very high.',
                    "  - **Cu (1958 kJ/mol):** Second electron must be removed from fully filled, extraordinarily stable **3d^10^** (Cu^+^: [Ar] 3d^10^ → Cu^2+^: 3d^9^).",
                    '• **IE~3~ Anomalies (Extremely High Values for Mn and Zn):**',
                    "  - **Mn (3248 kJ/mol):** Third electron must be stripped from exceptionally stable **3d^5^** (Mn^2+^: [Ar] 3d^5^ → Mn^3+^: 3d^4^). Hence, Mn^2+^ resists oxidation to Mn^3+^.",
                    '  - **Fe (2957 kJ/mol):** Relatively low IE~3~ because removing third electron yields stable **3d^5^** (Fe^2+^: [Ar] 3d^6^ → Fe^3+^: 3d^5^). Thus, Fe^2+^ is easily oxidized to Fe^3+^.',
                    "  - **Zn (3833 kJ/mol):** Disruption of completely filled 3d^10^ (Zn^2+^: [Ar] 3d^10^ → Zn^3+^: 3d^9^)."
                ]
            },
            {
                "title": "2. Comparison of 3d, 4d, and 5d Ionization Enthalpies",
                "tag": "Lanthanoid Impact",
                "accent": "navy",
                "bullets": [
                    "• **Vertical Trend Disruption:** In s and p blocks, IE decreases down the group. In transition groups, IE follows the anomalous order: **5d > 3d > 4d** (or 5d > 4d > 3d in many groups!).",
                    '• **Why 5d has HIGHEST IE:** Because of **Lanthanoid Contraction**, 5d elements experience an enormous effective nuclear charge (Z~eff~) without size expansion. Valence 6s electrons are held with intense electrostatic force.',
                    "• **Chemical Inertness of Heavy Metals:** High IE values of 5d metals (Pt, Au, Hg) explain why Gold and Platinum are noble, chemically inert, and resist oxidation/dissolution in standard mineral acids."
                ]
            },
            {
                "title": "3. JEE Advanced Concept Master",
                "tag": "Thermodynamic Reality",
                "accent": "gold",
                "bullets": [
                    "• **Thermodynamic Stability of Oxidation States:** Thermodynamic stability of an ion in aqueous solution does NOT depend on ionization energy alone! It depends on the net balance of **Atomization + Ionization Enthalpies vs Hydration Enthalpy**.",
                    '• **Cu^+^ vs Cu^2+^ in Water:** Although IE~2~ of Cu is very high (+1958 kJ/mol), **Cu^2+^(aq) is far more stable than Cu^+^(aq)** in water because high charge density of Cu^2+^ yields massive negative hydration enthalpy (Δ~hyd~ H° = −2121 kJ/mol), which more than compensates for IE~2~! Cu^+^ disproportionates: 2 Cu^+^(aq) → Cu^2+^(aq) + Cu(s).'
                ]
            }
        ]
    },
    {
        "id": "sheet_05",
        "num": 5,
        "title": "Sheet 05 — Variable Oxidation States & Thermodynamic Stability",
        "badge": "Oxidation States",
        "boxes": [
            {
                "title": "1. Spectrum of Oxidation States across 3d Series",
                "tag": "Valence Participation",
                "accent": "teal",
                "bullets": [
                    "• **Why Variable Oxidation States?** Valence electrons in transition metals occupy (n−1)d and ns orbitals. The energy difference between 3d and 4s is extremely small, allowing both to participate in chemical bonding.",
                    "• **Summary of Common Oxidation States in 3d:**",
                    "  - **Sc (+3):** Only stable state; [Ar] 3d^0^ noble core. No +2 state.",
                    "  - **Ti (+2, +3, +4):** +4 is most stable (TiO~2~, TiCl~4~).",
                    "  - **V (+2, +3, +4, +5):** +5 is oxidizing (V~2~O~5~), +4 is stable oxo-cation [VO]^2+^.",
                    "  - **Cr (+2, +3, +4, +5, +6):** +3 is most stable (t~2g~^3^ CFSE stability); +6 is strongly oxidizing (Cr~2~O~7~^2−^); +2 is reducing.",
                    "  - **Mn (+2, +3, +4, +5, +6, +7):** Maximum number of oxidation states in 3d (+2 to +7); +2 (3d^5^) is most stable; +7 (MnO~4~^−^) is powerful oxidant.",
                    "  - **Fe (+2, +3, +4, +6):** +2 and +3 are most common; ferrate [FeO~4~]^2−^ exists in alkaline media.",
                    "  - **Co (+2, +3):** +2 in simple aqueous salts; +3 in strong field octahedral complexes.",
                    "  - **Ni (+2, +3, +4):** +2 is thermodynamically dominant (Ni^2+^); +4 in complexes like K~2~[NiF~6~].",
                    "  - **Cu (+1, +2):** +1 in solid halides/oxides (CuCl, Cu~2~O); +2 in aqueous solution.",
                    "  - **Zn (+2):** Only +2; completely filled 3d^10^."
                ]
            },
            {
                "title": "2. Comparative Stability: 3d vs Heavier 4d/5d Congeners",
                "tag": "Crucial Group Trend",
                "accent": "navy",
                "bullets": [
                    "• **Contrasting Group Trends (p-Block vs d-Block):**",
                    "  - In p-block (Group 14, 15), lower oxidation state becomes more stable down the group due to the *inert pair effect* (Pb^2+^ > Pb^4+^, Bi^3+^ > Bi^5+^).",
                    "  - **In d-block, THE EXACT OPPOSITE OCCURS! HIGHER oxidation states become MORE STABLE down the group!**",
                    "• **Group 6 Demonstration:**",
                    "  - Cr(+6) in dichromate [Cr~2~O~7~]^2−^ is a **strong oxidizing agent** (readily reduced to Cr^3+^).",
                    "  - Mo(+6) in MoO~3~ and W(+6) in WO~3~ are **extraordinarily stable and non-oxidizing**!",
                    "• **Group 8 Demonstration:**",
                    "  - Fe(+8) does not exist (Fe tops out at +6 in unstable ferrate).",
                    "  - Ru and Os easily form stable volatile tetroxides: **RuO~4~ and OsO~4~ (+8 oxidation state!)**.",
                    "• **Physical Reason:** Larger radial extent of 4d and 5d orbitals allows more effective multi-center covalent overlap with electronegative ligands, stabilizing high oxidation states."
                ]
            },
            {
                "title": "3. Acidity & Covalency Trends of Transition Oxides",
                "tag": "Fajans' Rule in d-Block",
                "accent": "gold",
                "bullets": [
                    "• As oxidation state increases, polarizing power of the metal cation increases, pulling oxide electron density towards itself (increasing covalent character):",
                    "  - **Low Oxidation State (+2, +3):** Basic, ionic (e.g. MnO, CrO, FeO). Dissolve in acid to form hydrated cations.",
                    "  - **Intermediate State (+4):** Amphoteric (e.g. MnO~2~, Cr~2~O~3~, VO~2~). React with both acids and bases.",
                    "  - **High Oxidation State (+5, +6, +7):** Acidic, covalent (e.g. CrO~3~, Mn~2~O~7~, V~2~O~5~). Form oxo-acids (H~2~CrO~4~, HMnO~4~) and oxo-anions ([CrO~4~]^2−^, [MnO~4~]^−^)."
                ]
            }
        ]
    },
    {
        "id": "sheet_06",
        "num": 6,
        "title": "Sheet 06 — Standard Electrode Potentials & Thermochemical Cycles",
        "badge": "E° & Energetics",
        "figure": "electrode_potentials",
        "boxes": [
            {
                "title": "1. Thermochemical Cycle for M^2+^/M Standard Potential",
                "tag": "Thermodynamics",
                "accent": "teal",
                "bullets": [
                    '• The standard electrode potential E°(M^2+^/M) measures the free energy change for: M^2+^(aq) + 2e^-^ → M(s).',
                    "• Linked to three fundamental thermodynamic enthalpies:",
                    '  1. **Sublimation Enthalpy (Δ~sub~ H°):** M(s) → M(g) [Endothermic, > 0].',
                    '  2. **Ionization Enthalpies (IE~1~ + IE~2~):** M(g) → M^2+^(g) + 2e^-^ [Endothermic, > 0].',
                    '  3. **Hydration Enthalpy (Δ~hyd~ H°):** M^2+^(g) → M^2+^(aq) [Exothermic, < 0].',
                    '• Net Δ H° = Δ~sub~H° + (IE~1~ + IE~2~) + Δ~hyd~H°. More negative Δ H° makes the metal more reducing (more negative E°).'
                ]
            },
            {
                "title": "2. Analysis of 3d Series E°(M^2+^/M) Irregularities",
                "tag": "NCERT Key Data",
                "accent": "navy",
                "bullets": [
                    '• **General Trend:** Values become less negative across the series, reflecting general increase in (IE~1~ + IE~2~).',
                    '• **The Copper Anomaly (E° = +0.34 V):** Copper is the ONLY 3d metal with a **positive reduction potential**! Reason: Extremely high sum of atomization and ionization enthalpies is NOT compensated by its hydration enthalpy. Consequently, Cu cannot displace H~2~ from non-oxidizing acids (HCl, dil H~2~SO~4~); only oxidizing acids (HNO~3~, conc H~2~SO~4~) react by reducing nitrogen/sulfur.',
                    '• **Manganese Peak (E° = -1.18 V):** More negative than expected from trend. Reason: Mn^2+^ attains extra exchange stability of **half-filled 3d^5^** shell, lowering IE~2~ and stabilizing the aqueous cation.',
                    '• **Zinc Peak (E° = -0.76 V):** More negative due to completely filled **3d^10^** in Zn^2+^.',
                    '• **Nickel Peak (E° = -0.25 V):** More negative than predicted because Ni^2+^ has an exceptionally high negative hydration enthalpy (small ionic radius, high charge density).'
                ]
            },
            {
                "title": "3. The E°(M^3+^/M^2+^)& Redox Coupling System",
                "tag": "High-Yield JEE Advanced",
                "accent": "gold",
                "bullets": [
                    '• **Manganese (E°(Mn^3+^/Mn^2+^) = +1.57 V):** Extremely positive! Mn^3+^ (3d^4^) desperately seeks an electron to become stable 3d^5^ (Mn^2+^). Hence, Mn^3+^ is a powerful oxidizing agent.',
                    '• **Chromium (E°(Cr^3+^/Cr^2+^) = -0.41 V):** Negative value! Cr^2+^ (3d^4^) is a **strong reducing agent** because oxidation yields Cr^3+^ with half-filled stable **t~2g~^3^** configuration in octahedral crystal field (CFSE stabilization!).',
                    '• **Iron (E°(Fe^3+^/Fe^2+^) = +0.77 V):** Moderate positive value. Fe^3+^ has stable 3d^5^, making Fe^2+^ easily oxidizable by atmospheric oxygen.',
                    '• **Cobalt (E°(Co^3+^/Co^2+^) = +1.97 V):** Co^3+^(aq) oxidizes water to O~2~, but is stabilized in complexes with strong field ligands like NH~3~ ([Co(NH~3~)~6~]^3+^, d^6^ low-spin diamagnetic).'
                ]
            }
        ]
    },
    {
        "id": "sheet_07",
        "num": 7,
        "title": "Sheet 07 — Higher Oxidation State Stability — Halides & Oxides",
        "badge": "Fluorides & Oxides",
        "boxes": [
            {
                "title": "1. Transition Metal Halides & Maximum Oxidation States",
                "tag": "Fluorine Electronegativity",
                "accent": "teal",
                "bullets": [
                    "• **Fluorine Power:** Highest oxidation states are achieved ONLY in **fluorides** due to small size, high electronegativity, and massive lattice energy (or high metal-fluorine bond dissociation energy).",
                    "• **Maximum Halides in 3d:**",
                    "  - Ti forms **TiF~4~** (+4), V forms **VF~5~** (+5), Cr forms **CrF~6~** (+6, unstable/disputed; CrF~5~ is standard).",
                    "  - Manganese cannot form MnF~7~ (highest fluoride is **MnF~4~**); Mn tops out at +7 only with oxygen (MnO~3~F or Mn~2~O~7~).",
                    "• **Halide Instability with Fe and Cu:**",
                    '  - **FeI~3~ does not exist!** Reason: Fe^3+^ is a strong enough oxidant to oxidize iodide to iodine: 2 Fe^3+^ + 2 I^-^ → 2 Fe^2+^ + I~2~.',
                    '  - **CuI~2~ does not exist!** Cu^2+^ oxidizes I^−^: 2 Cu^2+^ + 4 I^-^ → 2 CuI(s) ↓ (white) + I~2~. Only CuI (cuprous iodide) is stable.',
                    "  - **CuF~2~ is stable** (ionic, high lattice energy), whereas CuF is unstable and disproportionates."
                ]
            },
            {
                "title": "2. Oxides vs Fluorides: Oxygen's Superiority",
                "tag": "pπ-dπ Multiple Bonding",
                "accent": "navy",
                "bullets": [
                    "• **Why Oxygen Stabilizes Higher States Better than Fluorine?**",
                    "  Although fluorine is more electronegative than oxygen, **oxygen has the unique ability to form multiple pπ-dπ bonds** with the transition metal!",
                    "• **Case Study — Manganese:** Highest fluoride is MnF~4~ (+4), but highest oxide is **Mn~2~O~7~ (+7)**, a dark green, explosive covalent oil where each Mn is tetrahedrally coordinated to four oxygens (including one bridging Mn-O-Mn link).",
                    "• **Case Study — Vanadium & Chromium:**",
                    "  - Vanadium forms stable oxo-cations: **[VO~2~]^+^ (+5)**, **[VO]^2+^ (+4)**.",
                    "  - Chromium forms **CrO~3~ (+6)** and chromyl fluoride **CrO~2~F~2~**, stabilized by terminal oxo double bonds."
                ]
            },
            {
                "title": "3. Oxides of 3d Metals & Structures",
                "tag": "Acidity Spectrum",
                "accent": "gold",
                "bullets": [
                    "• **Chromium Oxides Hierarchy:**",
                    "  - **CrO (+2):** Basic; dissolves in mineral acids to give blue Cr^2+^(aq).",
                    "  - **Cr~2~O~3~ (+3):** Amphoteric; green solid; dissolves in acids to give [Cr(H~2~O)~6~]^3+^ and in concentrated alkali to give chromite [Cr(OH)~4~]^−^.",
                    "  - **CrO~3~ (+6):** Strongly acidic; red needles; anhydride of chromic acid (H~2~CrO~4~); powerful explosive oxidizing agent.",
                    "• **Vanadium Pentoxide (V~2~O~5~):** Amphoteric; dissolves in acid to give dioxovanadium(V) cation [VO~2~]^+^ and in alkali to give vanadate [VO~4~]^3−^."
                ]
            }
        ]
    },
    {
        "id": "sheet_08",
        "num": 8,
        "title": "Sheet 08 — Magnetic Properties & Spin-Only Formula",
        "badge": "Magnetism & Moments",
        "boxes": [
            {
                "title": "1. Origin of Magnetism & Spin-Only Formula",
                "tag": "Quantum Basis",
                "accent": "teal",
                "bullets": [
                    '• **Two Magnetic Contributions:** Magnetic moment arises from (1) electron spin angular momentum (S), and (2) orbital angular momentum (L).',
                    '• **Quenching of Orbital Contribution in 3d:** In 3d transition metals, outer 3d orbitals are directly exposed to the electrostatic field of surrounding ligands/ions (Crystal Field). This electric field quenches (cancels) the orbital angular momentum (L ≈ 0).',
                    "• **Spin-Only Formula (Bohr Magnetons, BM):**",
                    '  μ~s~ = √(n(n+2)) BM = 2√(S(S+1)) BM',
                    '  where n is the number of unpaired d electrons, S = n/2 is the total spin, and 1 BM = eh / (4π m~e~) = 9.274 × 10^−24^ J/T.',
                    "• **Direct Value Quick-Lookup Table:**",
                    '  - n = 1: √3 = 1.73 BM (Ti^3+^, Cu^2+^, V^4+^)',
                    '  - n = 2: √8 = 2.83 BM (Ti^2+^, V^3+^, Ni^2+^)',
                    '  - n = 3: √15 = 3.87 BM (V^2+^, Cr^3+^, Co^2+^)',
                    '  - n = 4: √24 = 4.90 BM (Cr^2+^, Fe^2+^, Mn^3+^)',
                    '  - n = 5: √35 = 5.92 BM (Mn^2+^, Fe^3+^ — maximum in 3d series!).'
                ]
            },
            {
                "title": "2. Types of Magnetic Behavior",
                "tag": "Solid State Magnetism",
                "accent": "navy",
                "bullets": [
                    '• **Diamagnetism:** All electrons paired (n = 0). Weakly repelled by magnetic field. E.g. Sc^3+^ (d^0^), Ti^4+^ (d^0^), Cu^+^ (d^10^), Zn^2+^ (d^10^).',
                    "• **Paramagnetism:** Unpaired electrons present (n ≥ 1). Attracted into magnetic field; inversely proportional to temperature (Curie's Law: χ = C/T).",
                    "• **Ferromagnetism:** Extreme paramagnetism where permanent magnetic domains align spontaneously in the direction of the field (Fe, Co, Ni, CrO~2~). CrO~2~ is used in magnetic audio/video recording tapes."
                ]
            },
            {
                "title": "3. Deviations in 4d, 5d Series & Rare Earths",
                "tag": "Advanced Concept",
                "accent": "gold",
                "bullets": [
                    '• **Why Spin-Only Formula FAILS in 4d and 5d:** In heavier transition metals, spin-orbit coupling is extraordinarily strong; orbital angular momentum is NOT quenched. Total angular momentum J must be used.',
                    '• **Lanthanoids Magnetism:** As 4f electrons are deeply buried, crystal field cannot quench orbital motion: μ = g~J~ √(J(J+1)) is used. However, **Gd^3+^ (4f^7^, L = 0)** obeys the spin-only formula perfectly (n = 7, μ = 7.94 BM)!'
                ]
            }
        ]
    },
    {
        "id": "sheet_09",
        "num": 9,
        "title": "Sheet 09 — Formation of Coloured Ions — d-d vs Charge Transfer",
        "badge": "Colors & Spectroscopy",
        "boxes": [
            {
                "title": "1. Mechanism of Colour: d-d Electronic Transitions",
                "tag": "Crystal Field Splitting",
                "accent": "teal",
                "bullets": [
                    '• **Degeneracy Breakdown:** In an isolated gaseous transition metal atom, all five d-orbitals are degenerate (equal in energy). When ligands/water molecules approach in an octahedral field, the orbitals split into lower energy **t~2g~** (d~xy~, d~yz~, d~zx~) and higher energy **e~g~** (d~x²−y²~, d~z²~) sets.',
                    '• **Photon Absorption:** When visible light strikes the complex, an electron absorbs energy equal to Δ~o~ (hν) and jumps from t~2g~ to e~g~. The transmitted light possesses the **complementary colour**.',
                    "• **Why d^0^ and d^10^ are Colourless:**",
                    "  - **d^0^ Ions:** Sc^3+^, Ti^4+^, V^5+^ have NO electrons to promote → colourless salts.",
                    "  - **d^10^ Ions:** Cu^+^, Zn^2+^, Cd^2+^, Hg^2+^ have no vacant d orbital to receive promoted electrons → colourless salts."
                ]
            },
            {
                "title": "2. Charge Transfer (CT): Intensely Coloured d^0^ Systems",
                "tag": "High-Yield JEE Advance",
                "accent": "navy",
                "bullets": [
                    "• **The Grand JEE Paradox:** Why are [MnO~4~]^−^ (intense purple), [Cr~2~O~7~]^2−^ (bright orange), and [CrO~4~]^2−^ (vivid yellow) intensely coloured even though Mn(+7) and Cr(+6) have **d^0^ configurations**?",
                    "• **Mechanism: Ligand-to-Metal Charge Transfer (LMCT):**",
                    "  - Since metal is in a very high oxidation state with strong positive pull and vacant d-orbitals, an electron temporarily migrates from the ligand (oxide O^2−^ 2p orbital) to the metal's empty d-orbitals upon absorption of visible light.",
                    '  - **Laporte Rule:** LMCT transitions are fully *Laporte-allowed* (p to d transition involves change of parity g → u), yielding molar extinction coefficients ≈ 10^4^ L mol^−1^ cm^−1^ (1000x more intense than weak Laporte-forbidden d-d transitions!).',
                    "• **Other Famous CT Systems:**",
                    "  - **Fe(SCN)~3~ or [Fe(H~2~O)~5~(SCN)]^2+^:** Blood red colour due to LMCT from SCN^−^ to Fe^3+^.",
                    "  - **HgI~2~ (Scarlet red), AgI (Yellow), Ag~3~PO~4~ (Yellow):** LMCT from iodide/phosphate to metal."
                ]
            },
            {
                "title": "3. Reference Table of 3d Ion Aqueous Colours",
                "tag": "Memory Anchor",
                "accent": "gold",
                "bullets": [
                    "• Sc^3+^ (d^0^): Colourless | Ti^4+^ (d^0^): Colourless | Ti^3+^ (d^1^): **Purple / Violet**",
                    "• V^4+^ ([VO]^2+^, d^1^): **Blue** | V^3+^ (d^2^): **Green** | V^2+^ (d^3^): **Violet**",
                    "• Cr^3+^ (d^3^): **Violet-Green** | Cr^2+^ (d^4^): **Sky Blue**",
                    "• Mn^2+^ (d^5^): **Very Pale Pink (nearly colourless)** (spin-forbidden d-d transition!)",
                    "• Fe^3+^ (d^5^): **Yellow / Amber-Brown** | Fe^2+^ (d^6^): **Pale Green**",
                    "• Co^2+^ (d^7^): **Pink** (octahedral) / **Deep Blue** (tetrahedral [CoCl~4~]^2−^)",
                    "• Ni^2+^ (d^8^): **Bright Green** | Cu^2+^ (d^9^): **Blue** ([Cu(H~2~O)~6~]^2+^) | Zn^2+^ (d^10^): Colourless."
                ]
            }
        ]
    }
]
