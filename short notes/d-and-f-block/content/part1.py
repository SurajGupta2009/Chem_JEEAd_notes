"""Part 1: Sheets DF-01 to DF-06 — d-Block Fundamentals, Periodic Position, Configurations & Energetics."""
from __future__ import annotations

SHEETS = [
    # ------------------------------------------------------------------ DF-01
    {
        "id": "DF-01",
        "title": "d-Block Elements: Periodic Position, IUPAC Definition & Ground State Configurations",
        "blocks": [
            ("lead", "**Position in the Periodic Table & Transition Bridge** (NCERT §8.1)"),
            ("p", "The d-block comprises elements of Groups 3 to 12 occupying Periods 4, 5, 6, and 7. They bridge the highly electropositive, ionic s-block metals on the left and the electronegative, covalent p-block non-metals on the right, exhibiting intermediate transitional character."),
            ("h2", "1. IUPAC Definition & The Group 12 Enigma"),
            ("bul", [
                "**IUPAC Formal Definition:** A transition element is defined as an element which has an **incompletely filled d-subshell (d^1^ to d^9^)** in its ground state OR in any of its common oxidation states.",
                "**Group 12 Elements (Zn, Cd, Hg):** Zinc ([Ar] 3d^10^ 4s^2^), Cadmium ([Kr] 4d^10^ 5s^2^), and Mercury ([Xe] 4f^14^ 5d^10^ 6s^2^) have completely filled (n−1)d^10^ subshells in both their elemental ground state and their common +2 oxidation states (Zn^2+^, Cd^2+^, Hg^2+^).",
                "**Why Studied with Transition Metals?** They conclude the d-series, display continuous physical trends (complexation with Lewis bases, soft acid behavior), but strictly lack quintessential transition properties: they are diamagnetic, form colorless compounds, and have unusually low melting points (Hg is liquid at room temperature!).",
                "**Four Transition Series:** 3d series (Sc 21 to Zn 30 in Period 4), 4d series (Y 39 to Cd 48 in Period 5), 5d series (La 57, Hf 72 to Hg 80 in Period 6, interrupted by 14 4f lanthanoids), and 6d series (Ac 89, Rf 104 to Cn 112 in Period 7, interrupted by 14 5f actinoids)."
            ]),
            ("h2", "2. Valence Configurations & Origin of Anomalies"),
            ("p", 'The general valence configuration is **(n−1)d^1-10^ ns^1-2^**. In neutral atoms, Aufbau principle places 4s below 3d (E~4s~ < E~3d~). However, upon ionization, **4s electrons are ALWAYS lost first** because once 3d orbitals are populated, increased nuclear shielding causes 3d to sink deeper in energy than 4s (E~3d~ < E~4s~ in cations!).'),
            ("table", ["Element", "Atomic No.", "Expected Config.", "Observed Config.", "Physical Driving Force"], [
                ["**Chromium (Cr)**", "24", "[Ar] 3d^4^ 4s^2^", "**[Ar] 3d^5^ 4s^1^**", "Exchange energy maximization: 10 exchange pairs vs 6 pairs + spherical symmetry"],
                ["**Copper (Cu)**", "29", "[Ar] 3d^9^ 4s^2^", "**[Ar] 3d^10^ 4s^1^**", "Extraordinary stability of completely filled d^10^ subshell with minimal repulsions"],
                ["**Palladium (Pd)**", "46", "[Kr] 4d^8^ 5s^2^", "**[Kr] 4d^10^ 5s^0^**", "Completely filled 4d^10^; total absence of valence 5s electrons!"],
                ["**Platinum (Pt)**", "78", "[Xe] 4f^14^ 5d^8^ 6s^2^", "**[Xe] 4f^14^ 5d^9^ 6s^1^**", "Relativistic stabilization of 6s and d-shell exchange energy"],
                ["**Gold (Au)**", "79", "[Xe] 4f^14^ 5d^9^ 6s^2^", "**[Xe] 4f^14^ 5d^10^ 6s^1^**", "Filled 5d^10^ + strong relativistic contraction of valence 6s orbital"]
            ], [20, 12, 22, 22, 24], "Table 1.1 — Anomalous ground-state electronic configurations in d-block."),
            ("trap", "CRITICAL TRAP: Writing Fe^2+^ configuration as [Ar] 3d^4^ 4s^2^ is completely WRONG! In all transition cations, 4s electrons are lost FIRST: Fe^2+^ is [Ar] 3d^6^ 4s^0^, Sc^3+^ is [Ar] 3d^0^, and Cu^+^ is [Ar] 3d^10^.")
        ]
    },

    # ------------------------------------------------------------------ DF-02
    {
        "id": "DF-02",
        "title": "Physical Properties: Metallic Character, Lattices & Enthalpies of Atomization",
        "blocks": [
            ("lead", "**Lattice Cohesion & The Dual Metallic-Covalent Bonding Model** (NCERT §8.2)"),
            ("p", "All transition elements are typical metals possessing high tensile strength, ductility, malleability, high thermal/electrical conductivities, and metallic luster. They crystallize in dense close-packed structures: bcc, ccp (fcc), and hcp lattices."),
            ("h2", "1. Dual Nature of Bonding in Transition Metals"),
            ("bul", [
                "**Metallic Sea + Covalent d-d Overlap:** In transition metals, bonding involves BOTH delocalized valence **ns electrons** (typical metallic bonding) AND directional overlap of **unpaired (n−1)d electrons** between adjacent atoms (covalent bonding).",
                "**Hardness & Boiling Points:** Greater the number of unpaired d-electrons, stronger is the covalent interatomic bonding → metals are exceptionally hard with low volatility.",
                '**Group 12 Softness:** Zn, Cd, and Hg have no unpaired d electrons (d^10^). Covalent d-d overlap is absent; metallic bonding is weak → soft metals with low boiling points; Hg is a liquid at 298 K (Δ~vap~ H° = 59 kJ/mol).'
            ]),
            ("h2", "2. Melting Points & The Anomalous Dip at Mn and Tc"),
            ("p", "Melting points rise across a series, peaking at **Group 6 (Cr, Mo, W)** with maximum unpaired electrons, then decrease regularly towards Group 12. **Tungsten (W, 3422 °C)** holds the highest melting point of all metals, followed by Re and Os."),
            ("bul", [
                "**The Mn (1246 °C) and Tc Dip:** Despite having 5 unpaired d-electrons, Manganese and Technetium display anomalously low melting points!",
                "**Reason:** Symmetrical, tightly held half-filled **3d^5^ (and 4d^5^)** configuration holds electrons firmly to the nucleus, minimizing their delocalization into the metallic lattice. Furthermore, Mn adopts a complex distorted cubic lattice with unusually long interatomic distances."
            ]),
            ("h2", '3. Enthalpies of Atomization (Δ~a~H°) (NCERT §8.3.1)'),
            ("p", "Enthalpy of atomization is the energy required to dissociate 1 mole of solid metal into gaseous atoms: M(s) → M(g). It is a direct quantitative metric of metallic lattice strength."),
            ("table", ["Series", "Peak Element", 'Peak Δ~a~H° (kJ/mol)', "Group 12 Min. (kJ/mol)", "Physical Origin & Trend"], [
                ["**3d Series**", "Vanadium (V)", "515 kJ/mol", "Zn (126 kJ/mol)", "Unpaired 3d electrons maximize lattice cohesion; Zn has d^10^"],
                ["**4d Series**", "Niobium / Mo", "726 / 659 kJ/mol", "Cd (112 kJ/mol)", "Larger 4d radial extent enhances orbital overlap"],
                ["**5d Series**", "Tungsten (W)", "**849 kJ/mol**", "Hg (61 kJ/mol)", "**5d > 4d > 3d**: Diffuse 5d orbitals yield powerful M-M bonding!"]
            ], [18, 20, 20, 20, 22], "Table 2.1 — Atomization enthalpies across transition series."),
            ("trap", "EXAM TRAP: Group 5-6 metals have the maximum atomization energies (V/Nb peak in 3d/4d; W in 5d), and 5d series metals have systematically HIGHER atomization enthalpies than their 3d and 4d congeners. This explains why 5d elements are chemically noble, hard, and form stable metal-metal cluster compounds (e.g. [Re~2~Cl~8~]^2−^, W~6~Cl~12~).")
        ]
    },

    # ------------------------------------------------------------------ DF-03
    {
        "id": "DF-03",
        "title": "Atomic & Ionic Radii: 3d Series Trends & Lanthanoid Contraction",
        "blocks": [
            ("lead", "**Effective Nuclear Charge vs Screening Effect** (NCERT §8.3.2)"),
            ("p", "Atomic and ionic sizes dictate the chemical reactivity, hydration energetics, and coordination geometries of transition metal complexes. Across each transition series, radii exhibit a unique tripartite profile rather than a monotonic decline."),
            ("fig", "lanthanoid_contraction", "Fig. 3.1 — Atomic radii of 3d, 4d, and 5d transition series illustrating Lanthanoid Contraction."),
            ("h2", "1. Atomic Radii Profile across 3d Series (Sc to Zn)"),
            ("bul", [
                '**1. Sc to Cr (Steep Decrease):** Added electrons enter inner 3d subshell. Increase in nuclear charge (Z~eff~) heavily outweighs the poor mutual shielding provided by d-electrons → valence cloud contracts (Sc: 162 pm → Cr: 128 pm).',
                '**2. Mn to Ni (Nearly Flat Plateau):** Added 3d electrons now provide increased screening that virtually balances the increment in nuclear charge (Z~eff~ ≈ screening) → size remains nearly constant (Fe: 126 pm, Co: 125 pm, Ni: 125 pm).',
                "**3. Cu to Zn (Slight Expansion):** Filling of the completely paired 3d^10^ subshell creates strong inter-electronic repulsions that overpower nuclear attraction, causing electron cloud expansion (Cu: 128 pm → Zn: 137 pm)."
            ]),
            ("h2", "2. Lanthanoid Contraction: The 4d ≈ 5d Chemical Twin Phenomenon"),
            ("p", "Down a periodic group, atomic size normally increases due to addition of extra electron shells (Sc: 162 pm → Y: 180 pm). However, between 4d and 5d series, **radii are virtually IDENTICAL** (Zr: 160 pm ≈ Hf: 159 pm; Nb: 146 pm ≈ Ta: 146 pm; Mo: 139 pm ≈ W: 139 pm)!"),
            ("bul", [
                "**Physical Cause:** The intervening filling of **14 4f electrons** before 5d series (Cerium to Lutetium). 4f orbitals are diffuse with extremely poor shielding capability (screening order: s > p > d > f).",
                "**Nuclear Dominance:** Nuclear charge increases by +32 units from 4d to 5d, but poorly screened 4f electrons allow this enormous nuclear charge to pull valence 5d and 6s shells inward with massive force, completely neutralizing expected shell expansion.",
                "**Major Consequences:** (1) Zr/Hf and Nb/Ta are chemical twins with identical chemical behavior; (2) Densities of 5d metals double (Os = 22.59 g/cm^3^, Ir = 22.56 g/cm^3^); (3) Basic strength of hydroxides decreases steadily from La(OH)~3~ to Lu(OH)~3~."
            ]),
            ("trap", "JEE ADVANCED HIGHLIGHT: Due to Lanthanoid Contraction, Hf has a HIGHER ionization enthalpy than Zr, and separation of Zr and Hf requires fractional distillation of volatile alkoxides or ion-exchange chromatography; chemical precipitation cannot separate them!")
        ]
    },

    # ------------------------------------------------------------------ DF-04
    {
        "id": "DF-04",
        "title": "Ionization Enthalpy Patterns, IE Ratios & Transition Anomalies",
        "blocks": [
            ("lead", "**Ionization Energetics across 3d, 4d, and 5d Series** (NCERT §8.3.3)"),
            ("p", "Ionization enthalpy increases across each transition series, but the rate of increase is far less steep than in s and p blocks because incoming electrons enter an inner (n−1)d subshell, partially shielding the outer ns electrons from nuclear pull."),
            ("h2", "1. Analysis of First, Second, and Third Ionization Enthalpies"),
            ("bul", [
                '**First Ionization Enthalpy (IE~1~):** Ranges from Sc (631 kJ/mol) to Zn (906 kJ/mol). Zn exhibits the highest IE~1~ because the electron must be stripped from a stable, completely filled 4s^2^ orbital.',
                '**IE~2~ Anomalies (Chromium and Copper):**',
                "  - **Cr (1592 kJ/mol):** Second electron is removed from stable half-filled **3d^5^** (Cr^+^: [Ar] 3d^5^ → Cr^2+^: 3d^4^). Loss of huge exchange energy requires massive energy.",
                "  - **Cu (1958 kJ/mol):** Second electron is removed from exceptionally stable completely filled **3d^10^** (Cu^+^: [Ar] 3d^10^ → Cu^2+^: 3d^9^).",
                '**IE~3~ Anomalies (Manganese, Iron, and Zinc):**',
                "  - **Mn (3248 kJ/mol):** Third electron must be stripped from stable half-filled **3d^5^** (Mn^2+^: [Ar] 3d^5^ → Mn^3+^: 3d^4^). Hence, Mn^2+^ resists oxidation to Mn^3+^.",
                '  - **Fe (2957 kJ/mol):** Relatively low IE~3~ because removing third electron yields stable **3d^5^** (Fe^2+^: [Ar] 3d^6^ → Fe^3+^: 3d^5^). Thus, Fe^2+^ is easily oxidized to Fe^3+^.',
                "  - **Zn (3833 kJ/mol):** Requires disruption of completely filled, stable 3d^10^ core (Zn^2+^: [Ar] 3d^10^ → Zn^3+^: 3d^9^)."
            ]),
            ("h2", "2. Down the Group: The Anomalous 5d > 3d > 4d Hierarchy"),
            ("p", "In s and p blocks, IE decreases down a group due to increased atomic radius. In transition groups, IE follows the order: **5d > 3d > 4d** (or 5d > 4d > 3d in several groups)."),
            ("bul", [
                "**Why 5d has the HIGHEST Ionization Enthalpy:** Because of **Lanthanoid Contraction**, 5d elements experience an enormous increase in nuclear charge without size increase. Valence 6s electrons are held tightly by the nucleus.",
                "**Chemical Inertness of Heavy Metals:** Exceptionally high IE values of 5d metals (Pt, Au, Hg) explain why Gold and Platinum are chemically noble, resisting dissolution in standard mineral acids."
            ]),
            ("h2", "3. Thermodynamic Balance: Cu^+^ vs Cu^2+^ in Aqueous Media"),
            ("p", 'Thermodynamic stability in water depends on net energy balance (Δ~sub~H + IE~1~ + IE~2~ + Δ~hyd~H):\n'
                  '• Although IE~2~ of Cu is high (+1958 kJ/mol), **Cu^2+^(aq) is far more stable than Cu^+^(aq)** in water because high charge density of Cu^2+^ yields an immense negative hydration enthalpy (Δ~hyd~ H° = −2121 kJ/mol), which more than compensates for IE~2~!\n'
                  '• In aqueous solution, cuprous ion undergoes spontaneous disproportionation: **2 Cu^+^(aq) → Cu^2+^(aq) + Cu(s)** (E° = +0.37 V).'),
            ("trap", "EXAM TRAP: Cu^+^ is stable in insoluble solids (CuCl, CuBr, CuI) and complexes with π-acceptor ligands ([Cu(CN)~2~]^−^), but rapidly disproportionates in water!")
        ]
    },

    # ------------------------------------------------------------------ DF-05
    {
        "id": "DF-05",
        "title": "Variable Oxidation States & Comparative Group Stability",
        "blocks": [
            ("lead", "**Electronic Flexibility & High-Oxidation State Thermodynamics** (NCERT §8.3.4)"),
            ("p", "Unlike s-block metals which exhibit fixed oxidation states (+1 or +2), transition metals display a wide spectrum of oxidation states due to the very small energy gap between (n−1)d and ns orbitals, allowing both to participate in chemical bonding."),
            ("h2", "1. Oxidation State Spectrum in the 3d Series"),
            ("table", ["Element", "Outer Config.", "All Observed States", "Most Stable State", "Dominant Chemical Character"], [
                ["**Sc**", "3d^1^ 4s^2^", "+3", "**+3**", "d^0^ noble core; diamagnetic, colorless"],
                ["**Ti**", "3d^2^ 4s^2^", "+2, +3, +4", "**+4**", "d^0^ covalent/ionic; TiO~2~, TiCl~4~"],
                ["**V**", "3d^3^ 4s^2^", "+2, +3, +4, +5", "**+4, +5**", "+5 is oxidizing (V~2~O~5~); +4 is stable [VO]^2+^"],
                ["**Cr**", "3d^5^ 4s^1^", "+2, +3, +4, +5, +6", "**+3, +6**", "+3 (t~2g~^3^ CFSE stability); +6 is strong oxidant"],
                ["**Mn**", "3d^5^ 4s^2^", "+2, +3, +4, +5, +6, +7", "**+2, +4, +7**", "Maximum states (+2 to +7); +2 (d^5^) is stable"],
                ["**Fe**", "3d^6^ 4s^2^", "+2, +3, +4, +6", "**+2, +3**", "+3 (d^5^ stable); ferrate [FeO~4~]^2−^ in alkali"],
                ["**Co**", "3d^7^ 4s^2^", "+2, +3, +4", "**+2, +3**", "+2 in simple salts; +3 in strong field complexes"],
                ["**Ni**", "3d^8^ 4s^2^", "+2, +3, +4", "**+2**", "+2 is thermodynamically dominant (Ni^2+^)"],
                ["**Cu**", "3d^10^ 4s^1^", "+1, +2", "**+2 (aq)**", "+1 in solid halides; +2 in aqueous solution"],
                ["**Zn**", "3d^10^ 4s^2^", "+2", "**+2**", "Only +2; completely filled 3d^10^ shell"]
            ], [10, 16, 26, 18, 30], "Table 5.1 — Oxidation states of 3d transition metals."),
            ("h2", "2. Group Trends: Contrast Between d-Block and p-Block"),
            ("bul", [
                "**p-Block vs d-Block Contrast:** In p-block (Groups 14, 15), lower oxidation states become more stable down the group due to the *inert pair effect* (Pb^2+^ > Pb^4+^, Bi^3+^ > Bi^5+^).",
                "**In d-Block: HIGHER oxidation states become MORE STABLE down the group!**",
                "  - **Group 6 Proof:** Cr(+6) in dichromate [Cr~2~O~7~]^2−^ is a **strong oxidizing agent**, whereas Mo(+6) in MoO~3~ and W(+6) in WO~3~ are **extraordinarily stable and non-oxidizing**!",
                "  - **Group 8 Proof:** Fe tops out at +6 in unstable ferrate, while Ru and Os easily form stable volatile tetroxides: **RuO~4~ and OsO~4~ (+8 state!)**.",
                "**Physical Reason:** Greater radial extension of 4d and 5d orbitals allows effective multi-center covalent overlap with electronegative ligands, stabilizing higher formal oxidation states."
            ]),
            ("trap", "CRITICAL JEE ADVANCED TRAP: Acidic nature increases with increasing oxidation state: MnO (basic) < Mn~3~O~4~ < Mn~2~O~3~ < MnO~2~ (amphoteric) < Mn~2~O~7~ (strongly acidic covalent green oil!).")
        ]
    },

    # ------------------------------------------------------------------ DF-06
    {
        "id": "DF-06",
        "title": "Standard Electrode Potentials & Thermochemical Cycles",
        "blocks": [
            ("lead", "**Thermodynamic Anatomy of Reduction Potentials** (NCERT §8.3.5)"),
            ("p", 'The standard electrode potential E°(M^2+^/M) measures the free energy change for the reduction: M^2+^(aq) + 2e^-^ → M(s). It represents the net thermodynamic competition between sublimation, ionization, and hydration enthalpies.'),
            ("fig", "electrode_potentials", "Fig. 6.1 — Thermochemical Born-Haber cycle for E°(M2+/M) and 3d redox irregularities."),
            ("h2", "1. Analysis of E°(M^2+^/M) Irregularities across 3d Series"),
            ("bul", [
                '**General Trend:** Values become less negative across the series, reflecting the general rise in (IE~1~ + IE~2~).',
                '**The Copper Anomaly (E° = +0.34 V):** Copper is the ONLY 3d metal with a **positive reduction potential**! Reason: High enthalpy of atomization (+339 kJ/mol) combined with high (IE~1~ + IE~2~ = +2703 kJ/mol) is NOT compensated by its hydration enthalpy (−2121 kJ/mol). Cu cannot displace H~2~ from non-oxidizing mineral acids (HCl, dil H~2~SO~4~).',
                '**Manganese Peak (E° = -1.18 V):** More negative than expected because Mn^2+^ attains extra exchange stability of **half-filled 3d^5^** shell, lowering IE~2~.',
                '**Zinc Peak (E° = -0.76 V):** More negative due to the extra stability of completely filled **3d^10^** in Zn^2+^.',
                '**Nickel Peak (E° = -0.25 V):** More negative than predicted due to an exceptionally large negative hydration enthalpy.'
            ]),
            ("h2", "2. The E°(M^3+^/M^2+^) Redox Couple System"),
            ("bul", [
                '**Manganese (E° = +1.57 V):** Extremely positive! Mn^3+^ (3d^4^) desperately seeks an electron to become stable 3d^5^ (Mn^2+^). Hence, Mn^3+^ is a powerful oxidizing agent.',
                '**Chromium (E° = -0.41 V):** Negative value! Cr^2+^ (3d^4^) is a **strong reducing agent** because oxidation yields Cr^3+^ with half-filled stable **t~2g~^3^** configuration in octahedral crystal field (CFSE stabilization!).',
                '**Iron (E° = +0.77 V):** Moderate positive value. Fe^3+^ has stable 3d^5^, making Fe^2+^ easily oxidizable by air to Fe^3+^.'
            ]),
            ("trap", "EXAM TRAP: Cr^2+^ and Mn^3+^ both have 3d^4^ configuration, yet Cr^2+^ is reducing while Mn^3+^ is oxidizing! Always justify via t~2g~^3^ crystal field stability for Cr^3+^ vs 3d^5^ exchange stability for Mn^2+^.")
        ]
    }
]
