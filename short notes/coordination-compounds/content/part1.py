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
                ["**Classic Examples**", "Mohr's Salt: $\\text{FeSO}_4\\cdot(\\text{NH}_4)_2\\text{SO}_4\\cdot 6\\text{H}_2\\text{O}$; Potash Alum: $\\text{K}_2\\text{SO}_4\\cdot\\text{Al}_2(\\text{SO}_4)_3\\cdot 24\\text{H}_2\\text{O}$", "Potassium Ferrocyanide: $\\text{K}_4[\\text{Fe(CN)}_6] \\rightarrow 4\\text{K}^+ + [\\text{Fe(CN)}_6]^{4-}$ (No free $\\text{Fe}^{2+}$!)"]
            ], [20, 40, 40], "Table 1.1 — Diagnostic comparison between double salts and coordination complexes."),
            ("h2", "2. Alfred Werner's Coordination Theory Postulates"),
            ("bul", [
                "**1. Two Types of Valencies:** Transition metals exhibit two distinct types of valency: **Primary Valency** and **Secondary Valency**.",
                "**2. Primary Valency (Ionizable, Non-directional):** Corresponds to the **formal oxidation state** of the central metal. Satisfied exclusively by negative ions (anions). In structural formulas, represented by **dashed lines** ($---$).",
                "**3. Secondary Valency (Non-ionizable, Directional):** Corresponds to the **Coordination Number (CN)** of the central metal. Satisfied by neutral molecules or anions. Directed towards fixed positions in space, dictating the **three-dimensional stereochemistry / geometry** (e.g. octahedral, tetrahedral, square planar). In structural formulas, represented by **solid lines** (—).",
                "**4. Dual Behavior of Ligands:** An anion may simultaneously satisfy BOTH primary and secondary valencies (e.g. $[\text{Co(NH}_3)_5\text{Cl}]\text{Cl}_2$, where one $\text{Cl}^-$ is inside the coordination sphere). It does not ionize in solution!"
            ]),
            ("trap", "CRITICAL TRAP: When $[\text{Co(NH}_3)_4\text{Cl}_2]\text{Cl}$ is treated with excess $\text{AgNO}_3$, exactly **1 mole of AgCl** precipitates per mole of complex, because only the outer-sphere chloride ion is ionizable! The two inner chlorides satisfy secondary valency.")
        ]
    },

    # ------------------------------------------------------------------ CC-02
    {
        "id": "CC-02",
        "title": "Werner's Formulations, Electrical Conductance & AgCl Precipitation",
        "blocks": [
            ("lead", "**Quantitative Experimental Verification of Werner's Formulations** (NCERT Table 9.1)"),
            ("p", "Alfred Werner established the correct structural formulas of cobalt(III) ammine complexes by correlating electrical molar conductivity, cryoscopic depression of freezing point (van 't Hoff factor $i$), and quantitative precipitation of chloride ions with excess $\text{AgNO}_3$."),
            ("h2", "1. Analysis of the Classic Cobalt(III) Ammine Series"),
            ("table", ["Traditional Name / Color", "Empirical Formula", "Modern Werner Formulation", "Molar Conductivity / Electrolyte Type", "Moles of AgCl ppt per mole of complex"], [
                ["**Luteo complex** (Yellow)", "$\\text{CoCl}_3\\cdot 6\\text{NH}_3$", "$[\\text{Co(NH}_3)_6]\\text{Cl}_3$", "**1 : 3 electrolyte** (4 ions total: $[\\text{Co(NH}_3)_6]^{3+} + 3\\text{Cl}^-$)", "**3 moles AgCl**"],
                ["**Purpureo complex** (Purple)", "$\\text{CoCl}_3\\cdot 5\\text{NH}_3$", "$[\\text{Co(NH}_3)_5\\text{Cl}]\\text{Cl}_2$", "**1 : 2 electrolyte** (3 ions total: $[\\text{Co(NH}_3)_5\\text{Cl}]^{2+} + 2\\text{Cl}^-$)", "**2 moles AgCl**"],
                ["**Praseo complex** (Green, trans)", "$\\text{CoCl}_3\\cdot 4\\text{NH}_3$", "$[\\text{Co(NH}_3)_4\\text{Cl}_2]\\text{Cl}$", "**1 : 1 electrolyte** (2 ions total: $[\\text{Co(NH}_3)_4\\text{Cl}_2]^+ + \\text{Cl}^-$)", "**1 mole AgCl**"],
                ["**Violeo complex** (Violet, cis)", "$\\text{CoCl}_3\\cdot 4\\text{NH}_3$", "$[\\text{Co(NH}_3)_4\\text{Cl}_2]\\text{Cl}$", "**1 : 1 electrolyte** (2 ions total: $[\\text{Co(NH}_3)_4\\text{Cl}_2]^+ + \\text{Cl}^-$)", "**1 mole AgCl**"],
                ["**Neutral complex**", "$\\text{CoCl}_3\\cdot 3\\text{NH}_3$", "$[\\text{Co(NH}_3)_3\\text{Cl}_3]$", "**Non-electrolyte** (0 ions, non-conducting solution)", "**0 moles AgCl** (No ppt!)"]
            ], [18, 16, 22, 26, 18], "Table 2.1 — Werner's cobalt ammine series: formulation, ions, and AgCl stoichiometry."),
            ("h2", "2. Physical Measurements Confirming Werner's Formulations"),
            ("bul", [
                "**1. Molar Electrical Conductivity (Λ_m):** Directly proportional to the number of free ions produced in solution: $\\Lambda_m(\\text{1:3}) > \\Lambda_m(\\text{1:2}) > \\Lambda_m(\\text{1:1}) > \\text{Non-electrolyte} \\approx 0$.",
                "**2. Colligative Properties (van 't Hoff factor i):** Depression of freezing point ($\\Delta T_f = i K_f m$) confirms the total particle count: $i = 4$ for $[\text{Co(NH}_3)_6]\text{Cl}_3$; $i = 3$ for $[\text{Co(NH}_3)_5\text{Cl}]\text{Cl}_2$; $i = 2$ for $[\text{Co(NH}_3)_4\text{Cl}_2]\text{Cl}$; $i = 1$ for $[\text{Co(NH}_3)_3\text{Cl}_3]$.",
                "**3. Reagent Test with H~2~SO~4~:** In $[\text{Co(NH}_3)_5\text{SO}_4]\text{Br}$, adding $\text{BaCl}_2$ produces NO white precipitate of $\text{BaSO}_4$ because sulfate is inside the coordination sphere! Adding $\text{AgNO}_3$ produces pale yellow $\text{AgBr}\\downarrow$ instantly."
            ]),
            ("trap", "JEE ADVANCED TRAP: When $100\\text{ mL}$ of $0.1\\text{ M } [\\text{Pt(NH}_3)_4\\text{Cl}_2]\\text{Cl}_2$ is treated with excess $\text{AgNO}_3$, millimoles of AgCl precipitated = $100 \\times 0.1 \\times 2 = 20\\text{ mmol}$ (0.02 mol), NOT 40 mmol!")
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
                "**Coordination Sphere:** The central atom/ion together with all its directly attached ligands enclosed within **square brackets** $[\\dots]$. It behaves as a single discrete, non-ionizable chemical unit in solution.",
                "**Ionization Sphere (Counter Ions):** The ionizable species written outside the square brackets that balance the net electrical charge of the coordination entity (e.g. $\\text{K}^+$ in $\\text{K}_4[\\text{Fe(CN)}_6]$, $\\text{Cl}^-$ in $[\\text{Co(NH}_3)_6]\\text{Cl}_3$)."
            ]),
            ("h2", "2. Coordination Number (CN) & Coordination Polyhedra"),
            ("p", "The **Coordination Number (CN)** of a central metal ion in a complex is defined as the **total number of ligand donor atoms** to which the metal is directly bonded:\n"
                  "  $$\\mathbf{\\text{CN}} = \\sum (\\text{Number of ligands} \\times \\text{Denticity})$$\n"
                  "• For monodentate ligands: $\\text{CN} = \\text{number of ligands}$. E.g. in $[\\text{PtCl}_6]^{2-}$, $\\text{CN} = 6$.\n"
                  "• For bidentate ligands: each ligand contributes 2 donor bonds. E.g. in $[\\text{Fe(C}_2\\text{O}_4)_3]^{3-}$, $\\text{CN} = 3 \\times 2 = \\mathbf{6}$! In $[\\text{Co(en)}_3]^{3+}$, $\\text{CN} = 3 \\times 2 = \\mathbf{6}$!\n"
                  "• In $[\\text{Fe(EDTA)}]^-$, $\\text{EDTA}^{4-}$ is hexadentate $\\implies \\mathbf{\\text{CN} = 6}$."),
            ("h2", "3. Calculation of Central Metal Oxidation State (OS)"),
            ("table", ["Complex Species", "Ligand Charges", "Algebraic Charge Equation", "Calculated Metal OS"], [
                ["$[\\text{Fe(CN)}_6]^{4-}$", "$\\text{CN}^- = -1$", "$x + 6(-1) = -4 \\implies x = +2$", "**Fe(+II)**"],
                ["$[\\text{Co(NH}_3)_5\\text{Cl}]^{2+}$", "$\\text{NH}_3 = 0, \\text{Cl}^- = -1$", "$x + 5(0) + (-1) = +2 \\implies x = +3$", "**Co(+III)**"],
                ["$[\\text{Ni(CO)}_4]$", "$\\text{CO} = 0$", "$x + 4(0) = 0 \\implies x = 0$", "**Ni(0)** (Zero valent!)"],
                ["$[\\text{Fe(H}_2\\text{O)}_5(\\text{NO})]\\text{SO}_4$", "$\\text{H}_2\\text{O} = 0, \\text{NO}^+ = +1, \\text{SO}_4^{2-} = -2$", "$x + 5(0) + (+1) - 2 = 0 \\implies x = +1$", "**Fe(+I)** (Brown ring complex)"],
                ["$[\\text{Pt(NH}_3)_2\\text{Cl(NO}_2)]$", "$\\text{NH}_3 = 0, \\text{Cl}^- = -1, \\text{NO}_2^- = -1$", "$x + 2(0) - 1 - 1 = 0 \\implies x = +2$", "**Pt(+II)**"]
            ], [26, 26, 30, 18], "Table 3.1 — Oxidation state calculations of representative coordination complexes."),
            ("trap", "EXAM TRAP: Do not confuse Coordination Number with Oxidation State! In $[\\text{Fe(C}_2\\text{O}_4)_3]^{3-}$, the Coordination Number is 6, while the Oxidation State of iron is +3.")
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
                ["**Monodentate**", "Aqua ($\\text{H}_2\\text{O}$), Ammine ($\\text{NH}_3$)", "O, N", "0", "Neutral molecules with lone pairs"],
                ["**Monodentate**", "Halido ($\\text{F}^-, \\text{Cl}^-, \\text{Br}^-, \\text{I}^-$)", "Halogen", "−1", "Typical monoatomic anionic ligands"],
                ["**Bidentate**", "Ethylenediamine (**en**)", "**2 N atoms**", "0", "Neutral symmetrical chelate; $\\text{H}_2\\text{N-CH}_2\\text{-CH}_2\\text{-NH}_2$"],
                ["**Bidentate**", "Oxalato (**ox**)", "**2 O atoms**", "−2", "Anionic symmetrical chelate; $[\\text{C}_2\\text{O}_4]^{2-}$"],
                ["**Bidentate**", "Glycinato (**gly**)", "**1 N, 1 O**", "−1", "Unsymmetrical bidentate ligand; $\\text{H}_2\\text{N-CH}_2\\text{-COO}^-$"],
                ["**Bidentate**", "Dimethylglyoximato (**dmg**)", "**2 N atoms**", "−1", "Forms scarlet red $[\\text{Ni(dmg)}_2]$ stabilized by H-bonding"],
                ["**Polydentate**", "Diethylenetriamine (**dien**)", "**3 N atoms**", "0", "Tridentate neutral chelating ligand"],
                ["**Polydentate**", "Triethylenetetramine (**trien**)", "**4 N atoms**", "0", "Tetradentate neutral chelating ligand"],
                ["**Hexadentate**", "Ethylenediaminetetraacetate (**EDTA**)", "**2 N + 4 O**", "**−4**", "Hexadentate master chelate; traps $\\text{Ca}^{2+}, \\text{Mg}^{2+}, \\text{Pb}^{2+}$"]
            ], [16, 24, 18, 10, 32], "Table 4.1 — Comprehensive classification of ligands by denticity and donor atoms."),
            ("h2", "2. Ambidentate Ligands (Linkage Isomerism Source)"),
            ("p", "A monodentate ligand possessing **two distinct donor atoms**, but able to bind through **ONLY ONE donor atom at a time**, is called an **ambidentate ligand**:\n"
                  "• **Nitrito-N vs Nitrito-O:** $\\text{M} \\leftarrow \\mathbf{\\text{NO}_2^-}$ (Nitro / Nitrito-N, binds via N) vs $\\text{M} \\leftarrow \\mathbf{\\text{ONO}^-}$ (Nitrito / Nitrito-O, binds via O).\n"
                  "• **Thiocyanato vs Isothiocyanato:** $\\text{M} \\leftarrow \\mathbf{\\text{SCN}^-}$ (Thiocyanato-S, binds via S) vs $\\text{M} \\leftarrow \\mathbf{\\text{NCS}^-}$ (Isothiocyanato-N, binds via N).\n"
                  "• **Cyanido vs Isocyanido:** $\\text{M} \\leftarrow \\mathbf{\\text{CN}^-}$ (Cyanido-C) vs $\\text{M} \\leftarrow \\mathbf{\\text{NC}^-}$ (Cyanido-N / Isocyanido)."),
            ("h2", "3. Flexidentate Ligands"),
            ("p", "Polydentate ligands that do not always utilize their maximum denticity, but adjust their number of bound donor atoms depending on the metal and reaction conditions:\n"
                  "• **EDTA^4−^:** Hexadentate in $[\\text{Co(EDTA)}]^-$, but acts as **pentadentate** in $[\\text{Co(EDTA)Br}]^{2-}$ where one carboxylate group remains uncoordinated!\n"
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
                  "  $$[\\text{Ni(H}_2\\text{O)}_6]^{2+} + 6\\text{NH}_3 \\rightleftharpoons [\\text{Ni(NH}_3)_6]^{2+} + 6\\text{H}_2\\text{O} \\quad (\\log \\beta = 8.61)$$\n"
                  "  $$[\\text{Ni(H}_2\\text{O)}_6]^{2+} + 3\\text{en} \\rightleftharpoons [\\text{Ni(en)}_3]^{2+} + 6\\text{H}_2\\text{O} \\quad (\\log \\beta = 18.28)$$\n"
                  "The complex with ethylenediamine is nearly $10^{10}$ times more stable!"),
            ("bul", [
                "**Entropy Driven Phenomenon (ΔS > 0):** In the reaction with en, 4 reactant particles ($1 \\text{ complex} + 3 \\text{ en}$) produce **7 product particles** ($1 \\text{ complex} + 6 \\text{ free } \\text{H}_2\\text{O}$).",
                "**Thermodynamic Consequence:** Release of 6 ordered coordinated water molecules into bulk solvent generates a massive increase in translational entropy: **ΔS° is large and POSITIVE (+ve)**! Since $\\Delta G^\\circ = \\Delta H^\\circ - T\\Delta S^\\circ$, this makes $\\Delta G^\\circ$ heavily negative.",
                "**Ring Size Rule:** 5-membered chelate rings are most stable with saturated aliphatic diamines (en); 6-membered rings are most stable when conjugated resonance is present (acetylacetonate, **acac**)."
            ]),
            ("h2", "2. The Macrocyclic Effect"),
            ("p", "Complexes of **macrocyclic polydentate ligands** (e.g. crown ethers, cryptands, porphyrin ring in heme/chlorophyll) are significantly more stable than complexes of open-chain polydentate ligands with the same donor atoms. This enhanced stability arises because macrocyclic ligands are **pre-organized in space** (smaller loss of conformational entropy upon binding)."),
            ("h2", "3. Practical Applications of Chelation"),
            ("bul", [
                "**1. Water Hardness Estimation:** Titration of hard water with **$\text{Na}_2\text{H}_2\text{EDTA}$** using Eriochrome Black-T (EBT) indicator selectively chelates $\text{Ca}^{2+}$ and $\text{Mg}^{2+}$.",
                "**2. Chelation Therapy (Antidotes):** $\text{EDTA}^{4-}$ is used to treat **lead poisoning** by forming stable water-soluble $[\text{Pb(EDTA)}]^{2-}$ excreted in urine. **D-penicillamine** chelates excess copper in Wilson's disease. **Desferrioxamine B** removes toxic iron overload."
            ]),
            ("trap", "EXAM TRAP: Dimethylglyoxime ($\text{dmg}^-$) forms an extraordinarily stable bis-complex with $\text{Ni}^{2+}$: $[\text{Ni(dmg)}_2]$. Its stability is bolstered by TWO intramolecular **O-H···O hydrogen bonds** holding the two planar rings in a rigid square planar geometry!")
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
                "**1. Order of Cation and Anion:** The cation is ALWAYS named first, followed by the anion (whether complex or simple). E.g. in $\\text{K}_4[\\text{Fe(CN)}_6]$, Potassium is named first; in $[\\text{Co(NH}_3)_6]\\text{Cl}_3$, Hexaamminecobalt(III) is named first.",
                "**2. Inside the Coordination Entity:** Ligands are listed in **alphabetical order** based on their first letter, regardless of their charge or number, followed by the central metal name.",
                "**3. Ligand Name Modifications:**",
                "  - Anionic ligands ending in *-ide*, *-ite*, *-ate* are changed to end in **-ido**, **-ito**, **-ato** (e.g. $\\text{Cl}^- \\rightarrow$ chlorido, $\\text{CN}^- \\rightarrow$ cyanido, $\\text{OH}^- \\rightarrow$ hydroxido, $\\text{C}_2\\text{O}_4^{2-} \\rightarrow$ oxalato, $\\text{SO}_4^{2-} \\rightarrow$ sulfato).",
                "  - Neutral ligands retain regular names, with four key exceptions: $\\mathbf{\\text{H}_2\\text{O} = \\text{aqua}}$, $\\mathbf{\\text{NH}_3 = \\text{ammine}}$ (double 'm'!), $\\mathbf{\\text{CO} = \\text{carbonyl}}$, $\\mathbf{\\text{NO} = \\text{nitrosyl}}$.",
                "**4. Numerical Prefixes:** *di-*, *tri-*, *tetra-*, *penta-*, *hexa-*. When the ligand name already contains a numerical prefix (e.g. ethylenediamine) or is polydentate, use **bis-**, **tris-**, **tetrakis-** with the ligand enclosed in parentheses.",
                "**5. Metal Ending:**",
                "  - In **cationic or neutral complexes**, the metal retains its standard English name (e.g. cobalt, platinum, iron).",
                "  - In **anionic complexes**, the metal name MUST end in the suffix **-ate** (e.g. cobaltate, platinate, ferrate, cuprate, argentate, aurate).",
                "**6. Oxidation State:** Roman numeral enclosed in parentheses immediately following the metal name without space (e.g. iron(II), nickel(0))."
            ]),
            ("h2", "2. Master Worked IUPAC Examples"),
            ("table", ["Chemical Formula", "Ion Type", "Correct IUPAC Name", "High-Yield Error to Avoid"], [
                ["$[\\text{Co(NH}_3)_6]\\text{Cl}_3$", "Cationic complex", "**Hexaamminecobalt(III) chloride**", "Do not write 'trichloride' for counter ion!"],
                ["$\\text{K}_4[\\text{Fe(CN)}_6]$", "Anionic complex", "**Potassium hexacyanidoferrate(II)**", "Must use Latin root 'ferrate', not 'ironate'!"],
                ["$\\text{K}_2[\\text{PtCl}_6]$", "Anionic complex", "**Potassium hexachloridoplatinate(IV)**", "Metal suffix must be '-ate'"],
                ["$[\\text{Pt(NH}_3)_2\\text{Cl(NO}_2)]$", "Neutral complex", "**Diamminechloridonitrito-N-platinum(II)**", "Alphabetical: ammine (a) < chlorido (c) < nitrito (n)"],
                ["$[\\text{Co(en)}_3]_2(\\text{SO}_4)_3$", "Cationic complex", "**Tris(ethane-1,2-diamine)cobalt(III) sulfate**", "Must use 'tris', not 'tri' for en!"],
                ["$[\\text{Cr(en)}_2\\text{Cl}_2]\\text{Cl}$", "Cationic complex", "**Dichloridobis(ethane-1,2-diamine)chromium(III) chloride**", "Chlorido (c) precedes ethane-1,2-diamine (e)"]
            ], [22, 18, 36, 24], "Table 6.1 — Authoritative IUPAC names of high-yield JEE complexes."),
            ("trap", "CRITICAL TRAP: For coordination isomers where both cation and anion are complexes, like $[\\text{Pt(NH}_3)_4][\\text{PtCl}_4]$: Name is **Tetraammineplatinum(II) tetrachloridoplatinate(II)**. The cationic platinum has NO '-ate' suffix, while the anionic platinum MUST end in '-ate'!")
        ]
    }
]
