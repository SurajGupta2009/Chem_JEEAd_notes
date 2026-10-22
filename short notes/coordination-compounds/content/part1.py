"""Part 1: Sheets CC-01 to CC-06 — Werner's Theory, Ligands, Denticity, Chelation & IUPAC Nomenclature."""
from __future__ import annotations

SHEETS = [
    # ------------------------------------------------------------------ CC-01
    {
        "id": "CC-01",
        "title": "Introduction to Coordination Compounds & Werner's Theory",
        "blocks": [
            ("lead", "**Double Salts vs Coordination Complexes & Werner's Postulates** (NCERT §9.1)"),
            ("p", "Coordination compounds are addition compounds containing a central metal atom or ion surrounded by an array of bound ions or neutral molecules (ligands). They retain their structural identity in solid state as well as in aqueous solution."),
            ("fig", "werner_structures", "Fig. 1.1 — Primary (dashed, ionizable) vs Secondary (solid, directional) valencies in cobalt ammines."),
            ("h2", "1. Double Salts vs Coordination (Complex) Compounds"),
            ("table", ["Property", "Double Salts (e.g. Mohr's Salt, Alum, Carnallite)", "Coordination Complexes (e.g. K~4~[Fe(CN)~6~])"], [
                ["**Solution Behavior**", "Completely dissociate into constituent simple ions in water", "Retain identity; complex ion does NOT dissociate into simple ions"],
                ["**Chemical Tests**", "Give positive confirmatory tests for ALL individual constituent ions", "Do not give tests for constituent ions locked inside coordination sphere"],
                ["**Valency Nature**", "Governed strictly by normal electrovalent / ionic bonds", "Involves coordinate covalent (dative) bonds from ligands to metal"],
                ["**Classic Examples**", "Mohr's Salt: FeSO~4~·(NH~4~)~2~SO~4~· 6H~2~O; Potash Alum: K~2~SO~4~·Al~2~(SO~4~)~3~· 24H~2~O", 'Potassium Ferrocyanide: K~4~[Fe(CN)~6~] → 4K^+^ + [Fe(CN)~6~]^4−^ (No free Fe^2+^!)']
            ], [20, 40, 40], "Table 1.1 — Diagnostic comparison between double salts and coordination complexes."),
            ("h2", "2. Alfred Werner's Coordination Theory Postulates"),
            ("bul", [
                "**1. Two Types of Valencies:** Transition metals exhibit two distinct types of valency: **Primary Valency** and **Secondary Valency**.",
                '**2. Primary Valency (Ionizable, Non-directional):** Corresponds to the **formal oxidation state** of the central metal. Satisfied exclusively by negative ions (anions). In structural formulas, represented by **dashed lines** (---).',
                "**3. Secondary Valency (Non-ionizable, Directional):** Corresponds to the **Coordination Number (CN)** of the central metal. Satisfied by neutral molecules or anions. Directed towards fixed positions in space, dictating the **three-dimensional stereochemistry / geometry** (e.g. octahedral, tetrahedral, square planar). In structural formulas, represented by **solid lines** (—).",
                '**4. Dual Behavior of Ligands:** An anion may simultaneously satisfy BOTH primary and secondary valencies (e.g. [Co(NH~3~)~5~Cl]Cl~2~, where one Cl^-^ is inside the coordination sphere). It does not ionize in solution!'
            ]),
            ("trap", 'CRITICAL TRAP: When [Co(NH~3~)~4~Cl~2~]Cl is treated with excess AgNO~3~, exactly **1 mole of AgCl** precipitates per mole of complex, because only the outer-sphere chloride ion is ionizable! The two inner chlorides satisfy secondary valency.')
        ]
    },

    # ------------------------------------------------------------------ CC-02
    {
        "id": "CC-02",
        "title": "Werner's Formulations, Electrical Conductance & AgCl Precipitation",
        "blocks": [
            ("lead", "**Quantitative Experimental Verification of Werner's Formulations** (NCERT Table 9.1)"),
            ("p", "Alfred Werner established the correct structural formulas of cobalt(III) ammine complexes by correlating electrical molar conductivity, cryoscopic depression of freezing point (van 't Hoff factor i), and quantitative precipitation of chloride ions with excess AgNO~3~."),
            ("h2", "1. Analysis of the Classic Cobalt(III) Ammine Series"),
            ("table", ["Traditional Name / Color", "Empirical Formula", "Modern Werner Formulation", "Molar Conductivity / Electrolyte Type", "Moles of AgCl ppt per mole of complex"], [
                ["**Luteo complex** (Yellow)", 'CoCl~3~· 6NH~3~', '[Co(NH~3~)~6~]Cl~3~', '**1 : 3 electrolyte** (4 ions total: [Co(NH~3~)~6~]^3+^ + 3Cl^-^)', "**3 moles AgCl**"],
                ["**Purpureo complex** (Purple)", 'CoCl~3~· 5NH~3~', '[Co(NH~3~)~5~Cl]Cl~2~', '**1 : 2 electrolyte** (3 ions total: [Co(NH~3~)~5~Cl]^2+^ + 2Cl^-^)', "**2 moles AgCl**"],
                ["**Praseo complex** (Green, trans)", 'CoCl~3~· 4NH~3~', '[Co(NH~3~)~4~Cl~2~]Cl', '**1 : 1 electrolyte** (2 ions total: [Co(NH~3~)~4~Cl~2~]^+^ + Cl^-^)', "**1 mole AgCl**"],
                ["**Violeo complex** (Violet, cis)", 'CoCl~3~· 4NH~3~', '[Co(NH~3~)~4~Cl~2~]Cl', '**1 : 1 electrolyte** (2 ions total: [Co(NH~3~)~4~Cl~2~]^+^ + Cl^-^)', "**1 mole AgCl**"],
                ["**Neutral complex**", 'CoCl~3~· 3NH~3~', '[Co(NH~3~)~3~Cl~3~]', "**Non-electrolyte** (0 ions, non-conducting solution)", "**0 moles AgCl** (No ppt!)"]
            ], [18, 16, 22, 26, 18], "Table 2.1 — Werner's cobalt ammine series: formulation, ions, and AgCl stoichiometry."),
            ("h2", "2. Physical Measurements Confirming Werner's Formulations"),
            ("bul", [
                '**1. Molar Electrical Conductivity (Λ~m~):** Directly proportional to the number of free ions produced in solution: Λ~m~(1:3) > Λ~m~(1:2) > Λ~m~(1:1) > Non-electrolyte ≈ 0.',
                "**2. Colligative Properties (van 't Hoff factor i):** Depression of freezing point (Δ T~f~ = i K~f~ m) confirms the total particle count: i = 4 for [Co(NH~3~)~6~]Cl~3~; i = 3 for [Co(NH~3~)~5~Cl]Cl~2~; i = 2 for [Co(NH~3~)~4~Cl~2~]Cl; i = 1 for [Co(NH~3~)~3~Cl~3~].",
                '**3. Reagent Test with H~2~SO~4~:** In [Co(NH~3~)~5~SO~4~]Br, adding BaCl~2~ produces NO white precipitate of BaSO~4~ because sulfate is inside the coordination sphere! Adding AgNO~3~ produces pale yellow AgBr↓ instantly.'
            ]),
            ("trap", 'JEE ADVANCED TRAP: When 100 mL of 0.1 M [Pt(NH~3~)~4~Cl~2~]Cl~2~ is treated with excess AgNO~3~, millimoles of AgCl precipitated = 100 × 0.1 × 2 = 20 mmol (0.02 mol), NOT 40 mmol!')
        ]
    },

    # ------------------------------------------------------------------ CC-03
    {
        "id": "CC-03",
        "title": "Essential Terminology, Coordination Sphere & Oxidation State",
        "blocks": [
            ("lead", "**Anatomy of a Coordination Entity** (NCERT §9.2)"),
            ("p", "A coordination compound consists of a central coordination entity surrounded by ionizable counter ions. Mastery of coordination definitions is essential for IUPAC naming, isomerism, and crystal field analysis."),
            ("h2", "1. Structural Components of Coordination Entities"),
            ("bul", [
                "**Central Atom / Ion:** The metal atom or cation to which a fixed number of neutral molecules or anions are bound in a definite geometrical arrangement. Acts as a **Lewis Acid** (electron pair acceptor).",
                "**Ligands:** The neutral molecules, anions, or cations bound to the central metal atom/ion by donating at least one electron pair. Act as **Lewis Bases** (electron pair donors).",
                '**Coordination Sphere:** The central atom/ion together with all its directly attached ligands enclosed within **square brackets** […]. It behaves as a single discrete, non-ionizable chemical unit in solution.',
                '**Ionization Sphere (Counter Ions):** The ionizable species written outside the square brackets that balance the net electrical charge of the coordination entity (e.g. K^+^ in K~4~[Fe(CN)~6~], Cl^-^ in [Co(NH~3~)~6~]Cl~3~).'
            ]),
            ("h2", "2. Coordination Number (CN) & Coordination Polyhedra"),
            ("p", "The **Coordination Number (CN)** of a central metal ion in a complex is defined as the **total number of ligand donor atoms** to which the metal is directly bonded:\n"
                  '  **CN** = Σ (Number of ligands × Denticity)\n'
                  '• For monodentate ligands: CN = number of ligands. E.g. in [PtCl~6~]^2−^, CN = 6.\n'
                  '• For bidentate ligands: each ligand contributes 2 donor bonds. E.g. in [Fe(C~2~O~4~)~3~]^3−^, CN = 3 × 2 = **6**! In [Co(en)~3~]^3+^, CN = 3 × 2 = **6**!\n'
                  '• In [Fe(EDTA)]^-^, EDTA^4−^ is hexadentate ⇒ **CN = 6**.'),
            ("h2", "3. Calculation of Central Metal Oxidation State (OS)"),
            ("table", ["Complex Species", "Ligand Charges", "Algebraic Charge Equation", "Calculated Metal OS"], [
                ['[Fe(CN)~6~]^4−^', 'CN^-^ = -1', 'x + 6(-1) = -4 ⇒ x = +2', "**Fe(+II)**"],
                ['[Co(NH~3~)~5~Cl]^2+^', 'NH~3~ = 0, Cl^-^ = -1', 'x + 5(0) + (-1) = +2 ⇒ x = +3', "**Co(+III)**"],
                ['[Ni(CO)~4~]', 'CO = 0', 'x + 4(0) = 0 ⇒ x = 0', "**Ni(0)** (Zero valent!)"],
                ['[Fe(H~2~O)~5~(NO)]SO~4~', 'H~2~O = 0, NO^+^ = +1, SO~4~^2−^ = -2', 'x + 5(0) + (+1) - 2 = 0 ⇒ x = +1', "**Fe(+I)** (Brown ring complex)"],
                ['[Pt(NH~3~)~2~Cl(NO~2~)]', 'NH~3~ = 0, Cl^-^ = -1, NO~2~^-^ = -1', 'x + 2(0) - 1 - 1 = 0 ⇒ x = +2', "**Pt(+II)**"]
            ], [26, 26, 30, 18], "Table 3.1 — Oxidation state calculations of representative coordination complexes."),
            ("trap", 'EXAM TRAP: Do not confuse Coordination Number with Oxidation State! In [Fe(C~2~O~4~)~3~]^3−^, the Coordination Number is 6, while the Oxidation State of iron is +3.')
        ]
    },

    # ------------------------------------------------------------------ CC-04
    {
        "id": "CC-04",
        "title": "Ligands: Denticity, Ambidentate Isomerism & Flexidentate Behavior",
        "blocks": [
            ("lead", "**Complete Classification of Ligands by Electron Donation & Topology** (NCERT §9.2)"),
            ("p", "Ligands are categorized by charge (anionic, neutral, cationic) and by **denticity** (the number of donor atoms through which a single ligand binds simultaneously to the central metal atom)."),
            ("h2", "1. Monodentate, Bidentate & Polydentate Ligands"),
            ("table", ["Denticity Class", "Ligand Name & Abbreviation", "Donor Atoms", "Charge", "Coordination Notes"], [
                ["**Monodentate**", 'Aqua (H~2~O), Ammine (NH~3~)', "O, N", "0", "Neutral molecules with lone pairs"],
                ["**Monodentate**", 'Halido (F^-^, Cl^-^, Br^-^, I^-^)', "Halogen", "−1", "Typical monoatomic anionic ligands"],
                ["**Bidentate**", "Ethylenediamine (**en**)", "**2 N atoms**", "0", 'Neutral symmetrical chelate; H~2~N-CH~2~-CH~2~-NH~2~'],
                ["**Bidentate**", "Oxalato (**ox**)", "**2 O atoms**", "−2", 'Anionic symmetrical chelate; [C~2~O~4~]^2−^'],
                ["**Bidentate**", "Glycinato (**gly**)", "**1 N, 1 O**", "−1", 'Unsymmetrical bidentate ligand; H~2~N-CH~2~-COO^-^'],
                ["**Bidentate**", "Dimethylglyoximato (**dmg**)", "**2 N atoms**", "−1", 'Forms scarlet red [Ni(dmg)~2~] stabilized by H-bonding'],
                ["**Polydentate**", "Diethylenetriamine (**dien**)", "**3 N atoms**", "0", "Tridentate neutral chelating ligand"],
                ["**Polydentate**", "Triethylenetetramine (**trien**)", "**4 N atoms**", "0", "Tetradentate neutral chelating ligand"],
                ["**Hexadentate**", "Ethylenediaminetetraacetate (**EDTA**)", "**2 N + 4 O**", "**−4**", 'Hexadentate master chelate; traps Ca^2+^, Mg^2+^, Pb^2+^']
            ], [16, 24, 18, 10, 32], "Table 4.1 — Comprehensive classification of ligands by denticity and donor atoms."),
            ("h2", "2. Ambidentate Ligands (Linkage Isomerism Source)"),
            ("p", "A monodentate ligand possessing **two distinct donor atoms**, but able to bind through **ONLY ONE donor atom at a time**, is called an **ambidentate ligand**:\n"
                  '• **Nitrito-N vs Nitrito-O:** M ← **NO~2~^-^** (Nitro / Nitrito-N, binds via N) vs M ← **ONO^-^** (Nitrito / Nitrito-O, binds via O).\n'
                  '• **Thiocyanato vs Isothiocyanato:** M ← **SCN^-^** (Thiocyanato-S, binds via S) vs M ← **NCS^-^** (Isothiocyanato-N, binds via N).\n'
                  '• **Cyanido vs Isocyanido:** M ← **CN^-^** (Cyanido-C) vs M ← **NC^-^** (Cyanido-N / Isocyanido).'),
            ("h2", "3. Flexidentate Ligands"),
            ("p", "Polydentate ligands that do not always utilize their maximum denticity, but adjust their number of bound donor atoms depending on the metal and reaction conditions:\n"
                  '• **EDTA^4−^:** Hexadentate in [Co(EDTA)]^-^, but acts as **pentadentate** in [Co(EDTA)Br]^2−^ where one carboxylate group remains uncoordinated!\n'
                  "• **Sulfate (SO~4~^2−^):** Usually monodentate, but can act as bidentate chelate or bridging ligand in binuclear complexes."),
            ("trap", "CRITICAL DISTINCTION: Polydentate ligands donate through multiple donor atoms SIMULTANEOUSLY forming rings (chelates). Ambidentate ligands possess two possible donor atoms but coordinate through ONLY ONE at a given instant!")
        ]
    },

    # ------------------------------------------------------------------ CC-05
    {
        "id": "CC-05",
        "title": "Chelate Effect, Macrocyclic Effect & Stability Energetics",
        "blocks": [
            ("lead", "**Thermodynamic Driving Force of Ring-Forming Complexes** (NCERT §9.8)"),
            ("p", "When a di- or polydentate ligand binds to a central metal ion to form a **5- or 6-membered heterocyclic ring**, the complex is called a **chelate**, and the phenomenon is known as the **chelate effect**."),
            ("h2", "1. The Thermodynamic Origin of the Chelate Effect"),
            ("p", "Chelated complexes are exponentially more thermodynamically stable than analogous non-chelated complexes containing monodentate ligands with the same donor atoms:\n"
                  '  [Ni(H~2~O)~6~]^2+^ + 6NH~3~ ⇌ [Ni(NH~3~)~6~]^2+^ + 6H~2~O (log β = 8.61)\n'
                  '  [Ni(H~2~O)~6~]^2+^ + 3en ⇌ [Ni(en)~3~]^2+^ + 6H~2~O (log β = 18.28)\n'
                  'The complex with ethylenediamine is nearly 10^10^ times more stable!'),
            ("bul", [
                '**Entropy Driven Phenomenon (ΔS > 0):** In the reaction with en, 4 reactant particles (1 complex + 3 en) produce **7 product particles** (1 complex + 6 free H~2~O).',
                '**Thermodynamic Consequence:** Release of 6 ordered coordinated water molecules into bulk solvent generates a massive increase in translational entropy: **ΔS° is large and POSITIVE (+ve)**! Since Δ G° = Δ H° - TΔ S°, this makes Δ G° heavily negative.',
                "**Ring Size Rule:** 5-membered chelate rings are most stable with saturated aliphatic diamines (en); 6-membered rings are most stable when conjugated resonance is present (acetylacetonate, **acac**)."
            ]),
            ("h2", "2. The Macrocyclic Effect"),
            ("p", "Complexes of **macrocyclic polydentate ligands** (e.g. crown ethers, cryptands, porphyrin ring in heme/chlorophyll) are significantly more stable than complexes of open-chain polydentate ligands with the same donor atoms. This enhanced stability arises because macrocyclic ligands are **pre-organized in space** (smaller loss of conformational entropy upon binding)."),
            ("h2", "3. Practical Applications of Chelation"),
            ("bul", [
                '**1. Water Hardness Estimation:** Titration of hard water with **Na~2~H~2~EDTA** using Eriochrome Black-T (EBT) indicator selectively chelates Ca^2+^ and Mg^2+^.',
                "**2. Chelation Therapy (Antidotes):** EDTA^4−^ is used to treat **lead poisoning** by forming stable water-soluble [Pb(EDTA)]^2−^ excreted in urine. **D-penicillamine** chelates excess copper in Wilson's disease. **Desferrioxamine B** removes toxic iron overload."
            ]),
            ("trap", 'EXAM TRAP: Dimethylglyoxime (dmg^-^) forms an extraordinarily stable bis-complex with Ni^2+^: [Ni(dmg)~2~]. Its stability is bolstered by TWO intramolecular **O-H···O hydrogen bonds** holding the two planar rings in a rigid square planar geometry!')
        ]
    },

    # ------------------------------------------------------------------ CC-06
    {
        "id": "CC-06",
        "title": "IUPAC Nomenclature & Formula Writing of Coordination Entities",
        "blocks": [
            ("lead", "**Systematic IUPAC Nomenclature Rules & Formula Standards** (NCERT §9.3)"),
            ("p", "IUPAC nomenclature provides unambiguous rules for naming neutral, cationic, and anionic coordination complexes, bridge ligands, and structural isomers."),
            ("h2", "1. Systematic Rules for Naming Coordination Compounds"),
            ("bul", [
                '**1. Order of Cation and Anion:** The cation is ALWAYS named first, followed by the anion (whether complex or simple). E.g. in K~4~[Fe(CN)~6~], Potassium is named first; in [Co(NH~3~)~6~]Cl~3~, Hexaamminecobalt(III) is named first.',
                "**2. Inside the Coordination Entity:** Ligands are listed in **alphabetical order** based on their first letter, regardless of their charge or number, followed by the central metal name.",
                "**3. Ligand Name Modifications:**",
                '  - Anionic ligands ending in *-ide*, *-ite*, *-ate* are changed to end in **-ido**, **-ito**, **-ato** (e.g. Cl^-^ → chlorido, CN^-^ → cyanido, OH^-^ → hydroxido, C~2~O~4~^2−^ → oxalato, SO~4~^2−^ → sulfato).',
                "  - Neutral ligands retain regular names, with four key exceptions: **H~2~O = aqua**, **NH~3~ = ammine** (double 'm'!), **CO = carbonyl**, **NO = nitrosyl**.",
                "**4. Numerical Prefixes:** *di-*, *tri-*, *tetra-*, *penta-*, *hexa-*. When the ligand name already contains a numerical prefix (e.g. ethylenediamine) or is polydentate, use **bis-**, **tris-**, **tetrakis-** with the ligand enclosed in parentheses.",
                "**5. Metal Ending:**",
                "  - In **cationic or neutral complexes**, the metal retains its standard English name (e.g. cobalt, platinum, iron).",
                "  - In **anionic complexes**, the metal name MUST end in the suffix **-ate** (e.g. cobaltate, platinate, ferrate, cuprate, argentate, aurate).",
                "**6. Oxidation State:** Roman numeral enclosed in parentheses immediately following the metal name without space (e.g. iron(II), nickel(0))."
            ]),
            ("h2", "2. Master Worked IUPAC Examples"),
            ("table", ["Chemical Formula", "Ion Type", "Correct IUPAC Name", "High-Yield Error to Avoid"], [
                ['[Co(NH~3~)~6~]Cl~3~', "Cationic complex", "**Hexaamminecobalt(III) chloride**", "Do not write 'trichloride' for counter ion!"],
                ['K~4~[Fe(CN)~6~]', "Anionic complex", "**Potassium hexacyanidoferrate(II)**", "Must use Latin root 'ferrate', not 'ironate'!"],
                ['K~2~[PtCl~6~]', "Anionic complex", "**Potassium hexachloridoplatinate(IV)**", "Metal suffix must be '-ate'"],
                ['[Pt(NH~3~)~2~Cl(NO~2~)]', "Neutral complex", "**Diamminechloridonitrito-N-platinum(II)**", "Alphabetical: ammine (a) < chlorido (c) < nitrito (n)"],
                ['[Co(en)~3~]~2~(SO~4~)~3~', "Cationic complex", "**Tris(ethane-1,2-diamine)cobalt(III) sulfate**", "Must use 'tris', not 'tri' for en!"],
                ['[Cr(en)~2~Cl~2~]Cl', "Cationic complex", "**Dichloridobis(ethane-1,2-diamine)chromium(III) chloride**", "Chlorido (c) precedes ethane-1,2-diamine (e)"]
            ], [22, 18, 36, 24], "Table 6.1 — Authoritative IUPAC names of high-yield JEE complexes."),
            ("trap", "CRITICAL TRAP: For coordination isomers where both cation and anion are complexes, like [Pt(NH~3~)~4~][PtCl~4~]: Name is **Tetraammineplatinum(II) tetrachloridoplatinate(II)**. The cationic platinum has NO '-ate' suffix, while the anionic platinum MUST end in '-ate'!")
        ]
    }
]
