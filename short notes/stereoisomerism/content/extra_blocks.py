# -*- coding: utf-8 -*-
"""Extra blocks appended to a sheet, keyed by the authored sheet id.

Kept apart from the main content files so the expansion pass stays readable.
``build.renumber`` appends these blocks after the sheet's own blocks.
"""

EXTRA = {
    # ---------------------------------------------------------------- J-03
    "J-03": [
        ("h2", "2.6b  Oxime chemistry beyond the count"),
        ("p", "The C=N centre is not only a counting problem; it is a functional group with two examinable reactions. Both "
              "follow from the same geometry: the nitrogen lone pair fixes a plane, so the groups on the carbon are locked "
              "on one side or the other."),
        ("num", [
            "**Formation** is acid-catalysed and reversible: the amine attacks the carbonyl, a carbinolamine forms, and "
            "dehydration gives C=N. Because every step is reversible, the more stable (usually E) oxime accumulates — "
            "the reaction is under thermodynamic control.",
            "**Hydrolysis** reverses it: aqueous acid regenerates the carbonyl and hydroxylamine. This is why oximes are "
            "used as protecting groups for aldehydes and ketones.",
            "**Beckmann rearrangement** (H~2~SO~4~ or PCl~5~): the group *anti* to the –OH migrates to nitrogen and the "
            "product is a substituted amide, RCONHR′. The migrating group keeps its configuration, so the reaction is "
            "stereospecific — cyclohexanone oxime gives caprolactam, the monomer for nylon-6.",
        ]),
        ("p", "The Beckmann point is worth stating precisely: it is the group **anti** (trans) to the hydroxyl that migrates, "
              "not the group syn to it. For a ketoxime with two different groups, that means the two geometrical isomers give "
              "two different amides — a clean demonstration that E/Z isomerism is chemically consequential."),
        ("p", "**Worked E/Z assignment: butan-2-one oxime, CH~3~C(=NOH)CH~2~CH~3~.** On the carbon, ethyl (C,C,H) beats methyl "
              "(C,H,H), so ethyl is priority 1. On nitrogen, –OH beats the lone pair, so –OH is priority 1. If the –OH is on "
              "the same side as the ethyl group the oxime is (Z); on the opposite side it is (E). Both are isolable compounds, "
              "and their Beckmann products differ."),
        ("p", "**The 2,4-DNP test.** 2,4-Dinitrophenylhydrazine condenses with aldehydes and ketones to give a yellow-orange "
              "precipitate of the hydrazone. The test detects the C=O group, and the product it forms is exactly the C=N "
              "centre of the table above; a positive test therefore also means the product can exist as E/Z isomers."),
        ("key", "For a C=N centre: count the isomers from the carbon substituents (two different groups → 2), name them E/Z from CIP priorities, and remember that the two isomers can react differently (Beckmann)."),
        ("warn", "Do not write that oximes are “stable” or “unreactive”. They hydrolyse in aqueous acid and rearrange in concentrated acid — both reactions are used in synthesis and both are examinable as applications of the C=N geometry."),
    ],
    # ---------------------------------------------------------------- J-29
    "J-29": [
        ("h2", "Numbers worth carrying into the exam"),
        ("table", ["Quantity", "Value", "Where it is used"], [
            ["C=C rotation barrier", "250–270 kJ mol^−1^", "why geometrical isomers exist"],
            ["C–C rotation barrier (ethane)", "≈ 12.5 kJ mol^−1^", "conformers interconvert"],
            ["gauche CH~3~/CH~3~ interaction", "≈ 3.8 kJ mol^−1^", "butane populations"],
            ["chair → twist-boat", "≈ 23 kJ mol^−1^", "chair is the minimum"],
            ["cyclohexane ring flip", "≈ 45 kJ mol^−1^", "fast at 25 °C"],
            ["A-value of CH~3~", "≈ 7.3 kJ mol^−1^", "≈ 95 % equatorial"],
            ["A-value of t-Bu", "≈ 20 kJ mol^−1^", "conformational lock"],
            ["2,2′-disubstituted biphenyl barrier", "80–160 kJ mol^−1^", "atropisomers isolable"],
        ], [44, 26, 30], "Table R.1 — orders of magnitude, not measurements."),
        ("h2", "The five-second checks"),
        ("num", [
            "Does the molecule have a plane or a centre? If yes → achiral, stop.",
            "Are the two ends of the chain identical? If yes → use the symmetric counting row, not 2^n^.",
            "Is the lowest-priority group pointing towards you? If yes → reverse the R/S answer.",
            "Is the nucleophile strong and the solvent aprotic? If yes → S~N~2 (inversion).",
            "Did the alkene geometry change the meso/racemic outcome? Draw the bromonium ion, do not recall a rule.",
        ]),
        ("key", "Six ideas carry the whole chapter: rotation can be blocked; two different groups at each end; symmetry decides activity; a plane or centre decides achirality; inversion for S~N~2 and racemisation for S~N~1; equatorial beats axial."),
    ],

    # ---------------------------------------------------------------- J-02
    "J-02": [
        ("h2", "1.4  How the examiner phrases it"),
        ("table", ["Question stem", "First move", "What earns the mark"], [
            ["“How many stereoisomers?”", "count skeletons, then centres", "the number *and* the split into active/meso"],
            ["“Are they identical, enantiomers or diastereomers?”", "normalise both to one projection", "the evidence (centres inverted or not)"],
            ["“Is the compound optically active?”", "look for σ, i, S~n~", "the symmetry element, not the number of centres"],
            ["“Assign R/S”", "rank by CIP, put the lowest group away", "the priorities written out"],
            ["“Which is more stable?”", "count gauche/eclipsing or a/e interactions", "the interaction that decides it"],
            ["“Predict the product stereochemistry”", "name the mechanism first", "the mechanism → inversion / racemisation / syn / anti"],
        ], [34, 30, 36], "Table 1.2 — the six stems that cover almost every objective question on this chapter."),
        ("p", "Two habits save marks. First, when the stem says “stereoisomers”, give the total **and** the number of optically active forms; "
              "most marking schemes award the second number separately. Second, when the stem says “optically active”, do not count centres — "
              "look for the plane. A molecule with two centres and a plane is inactive, and a molecule with no centre and no plane (an allene) "
              "is active."),
        ("p", "A third habit is worth the ink: write the molecular formula before anything else. C~4~H~8~Cl~2~ tells you the skeleton is "
              "saturated, so any ring you draw is a real possibility; C~5~H~8~ tells you two degrees of unsaturation, so a ring plus a double "
              "bond is possible. Enumerations fail more often from a missed skeleton than from a missed stereocentre."),
    ],
    # ---------------------------------------------------------------- J-04
    "J-04": [
        ("h2", "2.11b  E/Z in rings and in polyenes"),
        ("p", "In a ring, “cis” and “trans” are still usable because the ring provides a reference plane, but the moment three or more "
              "substituents are present, cis/trans stops identifying the compound uniquely and E/Z is safer. E/Z in a ring is assigned "
              "exactly as in an open chain: compare the two groups on each alkene carbon by CIP priority, then look at which side of the "
              "double bond the priority-1 groups lie on."),
        ("p", "For a polyene, every double bond is assigned independently and the descriptors are listed with locants in ascending order: "
              "(2E,4Z,6E)-octa-2,4,6-triene. Do not average them and do not let one centre's assignment influence the next. The only "
              "coupling is through the chain geometry: a 2,4-diene drawn all-trans is a zig-zag, while a 2E,4Z diene has a pronounced "
              "kink, which is why the two differ in melting point and in their cyclisation behaviour."),
        ("table", ["Structure", "Descriptors", "Why it matters"], [
            ["(2E,4Z)-hexa-2,4-diene", "E at C2, Z at C4", "kinked; different shape from all-E"],
            ["(2E,4E)-hexa-2,4-diene", "E, E", "zig-zag; the more stable isomer"],
            ["(1Z,3Z)-cycloocta-1,3-diene", "Z, Z", "small-ring dienes are forced cis"],
            ["(2E)-3-methylpent-2-ene", "E", "CH~3~ vs CH~2~CH~3~ decides, not chain length"],
        ], [30, 22, 48], "Table 2.7 — descriptors are per centre, listed with locants."),
        ("key", "E/Z is assigned per double bond, in ascending locant order, and each assignment is independent. In rings, E/Z is safer than cis/trans as soon as more than two substituents are present."),
    ],
    # ---------------------------------------------------------------- J-05
    "J-05": [
        ("h2", "2.17b  Different substituents on the same ring"),
        ("p", "When the two substituents are different, the end-for-end equivalence disappears and the count usually rises. Work "
              "1-bromo-2-chlorocyclopropane: anchor Br up. Cl may be up (cis) or down (trans). The cis arrangement has a mirror plane "
              "through C3 and the C1–C2 bond, so it is achiral — one compound. The trans arrangement has no plane and no centre, so it "
              "is a pair of enantiomers — two compounds. Total: two geometrical isomers, three stereoisomers, two of them active."),
        ("p", "Now 1-bromo-1-chloro-2-methylcyclopropane. C1 carries Br and Cl and is not a stereocentre (the ring paths are different, "
              "but the two halogen groups differ, so it is a stereocentre — check: its four groups are Br, Cl, C2 and C3, all different, "
              "so it is a stereocentre). C2 carries H, CH~3~, C1 and C3, also four different groups. Two coupled centres on a ring: cis "
              "and trans give 2 geometrical isomers, each chiral (no plane), so 4 stereoisomers in two enantiomeric pairs."),
        ("table", ["Ring compound", "Geometrical", "Stereoisomers", "Active forms"], [
            ["1-bromo-2-chlorocyclopropane", "2", "3", "2 (trans pair)"],
            ["1-bromo-1-chloro-2-methylcyclopropane", "2", "4", "4 (two pairs)"],
            ["1,2-dibromocyclopropane", "2", "3", "2 (trans pair)"],
            ["1,2,3-tribromocyclopropane", "3", "4", "2 (one pair)"],
        ], [40, 16, 22, 22], "Table 2.10 — with different substituents, cis is often still achiral, but trans is always chiral."),
        ("warn", "Do not use the “all-cis is achiral” shortcut on a ring carrying three different substituents. All-cis-1,2,3-tribromocyclopropane has a plane (it is achiral), but all-cis-1-bromo-2-chloro-3-methylcyclopropane does not — the three groups are different, so no plane can map them onto each other."),
    ],
    # ---------------------------------------------------------------- J-10
    "J-10": [
        ("h2", "3.3b  Specific rotation of a mixture, and what changes it"),
        ("p", "Because rotation is proportional to the amount of each active species, a mixture's observed rotation is the sum of the "
              "contributions. For a two-enantiomer mixture with enantiomeric excess ee, the observed specific rotation is simply "
              "ee × [α]~pure~ — the relation used on sheet J-14 to measure optical purity."),
        ("p", "**Worked.** A sample of (S)-2-butanol shows [α] = +4.05° while the pure (S) enantiomer has [α] = +13.5°. Then "
              "ee = 4.05/13.5 = 30 %, so the sample contains 65 % (S) and 35 % (R). The observed rotation is positive, which tells you "
              "the (S) form is in excess — not that the sample is pure."),
        ("p", "Three variables change [α] without changing the compound: **temperature** (quoted as [α]~D~^25^), **solvent** (a polar "
              "solvent can hydrogen-bond to one face and shift the value), and **wavelength** (quoted as [α]~D~ for the sodium D line at "
              "589 nm; at other wavelengths the value can differ substantially, which is the basis of optical rotatory dispersion)."),
        ("table", ["Change", "Effect on α", "Effect on [α]"], [
            ["double the tube length", "doubles", "unchanged"],
            ["double the concentration", "doubles", "unchanged (dilute solutions)"],
            ["change the solvent", "changes", "changes"],
            ["change the temperature", "changes", "changes"],
            ["change the wavelength", "changes", "changes"],
            ["add an achiral impurity", "falls", "falls (concentration of active species is lower)"],
        ], [30, 26, 44], "Table 3.1 — what is a property of the experiment and what is a property of the compound."),
        ("key", "α belongs to the experiment; [α] belongs to the compound — but only when temperature, solvent and wavelength are quoted with it. An unqualified [α] value is incomplete."),
    ],
    # ---------------------------------------------------------------- J-18
    "J-18": [
        ("h2", "3.39b  The four kinds of chirality"),
        ("p", "It helps to sort every chiral molecule into one of four families. The families differ in *where* the handedness lives, "
              "and each has its own quick test."),
        ("table", ["Kind", "Where the handedness lives", "Test", "Example"], [
            ["central", "one atom with four different groups", "find the stereocentre", "lactic acid"],
            ["axial", "a locked axis with unsymmetrical ends", "both ends differ, rotation blocked", "allene, BINOL"],
            ["planar", "a plane that is not a mirror plane", "substituents arranged above/below a plane", "trans-cyclooctene, cyclophanes"],
            ["helical", "a screw-shaped framework", "the coil cannot be flattened", "helicene, some polymers"],
        ], [16, 38, 26, 20], "Table 3.11 — the four families; every chiral molecule belongs to one of them."),
        ("p", "**Planar chirality** deserves one line of explanation because it is easy to miss. A molecule such as a cyclophane can have "
              "a plane that contains the ring but is not a mirror plane, because the substituents above and below it are different. The "
              "molecule is then chiral even though no single atom carries four different groups and no axis is locked. Trans-cyclooctene "
              "is the smallest examinable example: the double bond forces the ring above and below the alkene plane, and the two "
              "enantiomers are configurationally stable at room temperature."),
        ("key", "Ask “where is the handedness?” rather than “where is the chiral carbon?”. Central, axial, planar and helical chirality cover every case JEE sets."),
    ],
    # ---------------------------------------------------------------- J-19
    "J-19": [
        ("h2", "3.43b  Four worked counts you can check against the table"),
        ("num", [
            "**2,3-Dichlorobutane**: two centres, similar ends (CH~3~ at both ends). n = 2 even → active 2, meso 1, total 3.",
            "**2-Chloro-3-bromobutane**: two centres, different ends. n = 2, different ends → active 4, meso 0, total 4.",
            "**2,3,4-Tribromopentane**: three centres, similar ends. n = 3 odd → active 2^2^ − 2^1^ = 2, meso 2, total 4.",
            "**2,3,4-Tribromohexane**: three centres, different ends (CH~3~ and C~2~H~5~). n = 3 → active 8, meso 0, total 8.",
        ]),
        ("p", "The pattern to notice is how much the ends matter: the same three-centre skeleton gives 4 stereoisomers with similar ends "
              "and 8 with different ends. That is the single most examined consequence of the counting table, and it is why the first "
              "question to ask is always “are the two ends constitutionally identical?”."),
        ("table", ["Molecule", "n", "Ends", "Active", "Meso", "Total"], [
            ["2,3-dichlorobutane", "2", "similar", "2", "1", "3"],
            ["2-chloro-3-bromobutane", "2", "different", "4", "0", "4"],
            ["2,3,4-tribromopentane", "3", "similar", "2", "2", "4"],
            ["2,3,4-tribromohexane", "3", "different", "8", "0", "8"],
            ["tartaric acid", "2", "similar", "2", "1", "3"],
            ["trihydroxyglutaric acid", "3", "similar", "2", "2", "4"],
        ], [34, 8, 18, 14, 12, 14], "Table 3.14 — the same skeleton with different ends; check your formula against every row."),
        ("warn", "“Different ends” means constitutionally different, not merely drawn differently. 2,3,4-tribromopentane has a CH~3~ at each end and is similar; 2,3,4-tribromohexane has CH~3~ at one end and C~2~H~5~ at the other and is different. A CH~2~ inserted at one end changes the answer from 4 to 8."),
    ],
    # ---------------------------------------------------------------- J-26
    "J-26": [
        ("h2", "5.10b  Counting the products of an addition"),
        ("p", "Addition questions usually ask for the number of products and whether they are optically active. Work in three steps: "
              "decide syn or anti from the reagent, draw the product for one face, then check the product for symmetry."),
        ("num", [
            "**cis-2-Butene + H~2~/Pd (syn)**: both H on one face → the two CH~3~ groups end up on the same side of the new C–C bond → the meso (2R,3S) pair collapses to one achiral compound: 1 product.",
            "**trans-2-Butene + H~2~/Pd (syn)**: the CH~3~ groups end up on opposite sides → (2R,3R) and (2S,3S) → a racemic pair: 2 products, optically inactive as a mixture.",
            "**cis-2-Butene + Br~2~ (anti)**: the two Br add from opposite faces → (2R,3R)/(2S,3S) → racemic pair: 2 products.",
            "**trans-2-Butene + Br~2~ (anti)**: opposite faces twice → the meso (2R,3S) compound: 1 product.",
        ]),
        ("table", ["Alkene", "Reagent (mode)", "Product", "Active?"], [
            ["cis-2-butene", "H~2~/Pd (syn)", "meso-2,3-dimethylbutane-like — one compound", "no"],
            ["trans-2-butene", "H~2~/Pd (syn)", "racemic pair", "mixture inactive"],
            ["cis-2-butene", "Br~2~ (anti)", "racemic pair", "mixture inactive"],
            ["trans-2-butene", "Br~2~ (anti)", "meso dibromide", "no"],
            ["cyclohexene", "Br~2~ (anti)", "trans-1,2-dibromocyclohexane (racemic)", "mixture inactive"],
            ["cyclohexene", "OsO~4~/H~2~O~2~ (syn)", "cis-1,2-cyclohexanediol (meso)", "no"],
        ], [24, 26, 34, 16], "Table 5.5 — the same two reagents, four different outcomes, decided by alkene geometry and addition mode."),
        ("key", "The number of products is decided by symmetry, not by the reagent. Ask: after the addition, is there a plane? If yes, one compound; if no, a racemic pair."),
        ("warn", "A racemic pair is “optically inactive” as a mixture but each molecule is chiral. An answer that says “the product is achiral because it is racemic” is wrong; say “a racemic mixture, therefore optically inactive”."),
    ],

    # ---------------------------------------------------------------- J-06
    "J-06": [
        ("h2", "2.21b  Worked cumulene and spiro questions"),
        ("num", [
            "**How many stereoisomers for CH~3~CH=C=CHCH~3~?** Two consecutive C=C (even), end planes perpendicular, each end carries H and CH~3~ → a pair of enantiomers, so **2** stereoisomers, both optically active.",
            "**How many for CH~3~CH=C=C=CHCH~3~?** Three consecutive C=C (odd), planes coplanar → cis and trans geometrical isomers, each with a plane → **2** stereoisomers, both achiral.",
            "**How many for (CH~3~)~2~C=C=CH~2~?** One end carries two CH~3~ → a mirror plane through the axis → **1** compound, achiral.",
            "**How many for 1,3-dimethylallene?** The same as the first case: 2 enantiomers. The name “1,3-dimethylallene” is another way of writing CH~3~CH=C=CHCH~3~.",
        ]),
        ("p", "For spiro compounds the counting is per ring. Spiro[3.3]heptane itself has two identical rings and two planes, so it is achiral. "
              "2,6-dimethylspiro[3.3]heptane, with one methyl on each ring at non-equivalent positions, has no plane and exists as a pair of "
              "enantiomers. The test is always the same: draw the two rings in perpendicular planes and look for a mirror plane that "
              "contains the spiro atom."),
        ("key", "Cumulene count: even number of C=C → chiral pair (if both ends differ); odd → cis/trans pair (achiral). Spiro count: test each ring separately, then look for a plane through the spiro atom."),
    ],
    # ---------------------------------------------------------------- J-08
    "J-08": [
        ("h2", "2.28b  Counting geometrical isomers of rings and cumulenes"),
        ("p", "Rings and cumulenes are where the 2^n^ formula is most often misapplied, because “a centre” is not always “a double bond”."),
        ("table", ["Structure", "Centres", "Count", "Reason"], [
            ["1,2-dimethylcyclopropane", "1 ring centre", "2", "cis and trans; trans is chiral"],
            ["1,2-dimethylcyclohexane", "1 ring centre", "2", "cis and trans; both achiral, trans is chiral? check: trans-1,2 has no plane → chiral pair (2), cis has a plane"],
            ["1,4-dimethylcyclohexane", "1 ring centre", "2", "cis and trans; cis has a plane"],
            ["CH~3~CH=C=CHCH~3~", "1 cumulene centre", "2", "enantiomeric pair, not cis/trans"],
            ["hexa-2,4-diene", "2 centres, similar ends", "3", "(E,E), (E,Z), (Z,Z)"],
            ["hexa-2,4-diene with different ends", "2 centres, different ends", "4", "(E,E), (E,Z), (Z,E), (Z,Z)"],
        ], [32, 22, 10, 36], "Table 2.14 — rings and cumulenes count as one centre each, not one per double bond."),
        ("warn", "The trans-1,2-dimethylcyclohexane row is a trap: its two chairs are (a,a) and (e,e), but flipping does not change the up/down sense, so the trans relationship is configurational. The molecule has no plane and no centre, so it is chiral and exists as a pair — the geometrical count is still 2, but the stereoisomer count is 3."),
    ],
    # ---------------------------------------------------------------- J-14
    "J-14": [
        ("h2", "3.24b  Resolution in practice"),
        ("p", "Resolution is a separation, so it always costs material. Three practical points decide whether a method is usable, and they "
              "are examinable as one-line answers."),
        ("num", [
            "**The resolving agent must be enantiopure.** A partially resolved agent gives partially resolved product; the two effects multiply.",
            "**The diastereomeric salts must differ enough in solubility.** If they crystallise together, fractional crystallisation fails and chromatography or a different agent is needed.",
            "**The hydrolysis step must not racemise the product.** Acid or base hydrolysis of an ester or salt can epimerise a centre next to a carbonyl, which undoes the separation.",
        ]),
        ("table", ["Method", "Chiral influence", "Scale", "Exam use"], [
            ["diastereomeric salt", "enantiopure acid or base", "industrial", "classic, easiest to write"],
            ["enzyme (kinetic)", "enzyme active site", "industrial, green", "“one enantiomer reacts, the other does not”"],
            ["chiral HPLC/GC", "chiral stationary phase", "analytical to preparative", "quickest to describe"],
            ["mechanical / conglomerate", "the crystal itself", "rare", "Pasteur; historical"],
        ], [28, 30, 22, 20], "Table 3.7 — four resolutions, one idea: make the pair diastereomeric."),
        ("key", "Every resolution is a diastereomer separation in disguise. Write that sentence first, then give the specific method."),
    ],
    # ---------------------------------------------------------------- J-22
    "J-22": [
        ("h2", "4.7b  Populations and the shape of the curve"),
        ("p", "The energy profile is only half the story; the population of each conformer follows the Boltzmann distribution, "
              "N~i~/N~j~ = exp(−ΔE/RT). At 298 K, RT ≈ 2.48 kJ mol^−1^, so a 3.8 kJ mol^−1^ gauche penalty gives a ratio of "
              "exp(−3.8/2.48) ≈ 0.22, i.e. each gauche form is about 22 % as populated as anti."),
        ("p", "Worked for butane: anti 1.0, two gauche forms 0.22 each, total 1.44, so anti ≈ 69 % and the two gauche forms ≈ 31 % "
              "combined. Rotamers interconvert quickly, so a physical measurement sees the weighted average — which is why the "
              "observed dipole moment of a flexible molecule rarely matches any single conformer."),
        ("table", ["ΔE / kJ mol^−1^", "Ratio at 298 K", "Population of the higher form"], [
            ["1", "0.67", "40 %"],
            ["2", "0.45", "31 %"],
            ["3.8", "0.22", "18 %"],
            ["7.3", "0.052", "5 %"],
            ["20", "3 × 10^−4^", "0.03 %"],
        ], [22, 24, 54], "Table 4.4 — the Boltzmann ladder; 20 kJ mol^−1^ is effectively a lock, 1 kJ mol^−1^ is a mixture."),
        ("key", "Order the conformers by energy, then convert to populations with exp(−ΔE/RT) at 298 K (RT ≈ 2.5 kJ mol^−1^). A 5.7 kJ mol^−1^ gap is a 90:10 mixture."),
    ],
    # ---------------------------------------------------------------- J-25
    "J-25": [
        ("h2", "5.5b  Three worked mechanism decisions"),
        ("p", "**(a) 2-bromobutane + NaCN in DMSO.** Secondary substrate, strong nucleophile, polar aprotic solvent → S~N~2. The product is "
              "2-methylbutanenitrile with **inversion** at C2. If the starting material is (R)-2-bromobutane, the product is the (S) "
              "nitrile — but check the priority order, because CN now replaces Br and the ranking at C2 changes."),
        ("p", "**(b) 2-bromo-2-methylbutane + water.** Tertiary substrate, weak nucleophile, protic solvent → S~N~1, and E1 competes. The "
              "substitution product is racemic 2-methylbutan-2-ol; the elimination product is 2-methylbut-2-ene (Zaitsev). Heating "
              "favours the alkene; a stronger, bulkier base such as tert-butoxide gives almost entirely E2."),
        ("p", "**(c) trans-1-bromo-4-tert-butylcyclohexane + ethoxide.** E2 requires a trans-diaxial H–C–C–Br arrangement. In this chair the "
              "Br is equatorial and the only β-H that is anti-periplanar is on C2/C6, which are equivalent; elimination gives "
              "4-tert-butylcyclohexene. The tert-butyl group locks the chair, so there is no conformational escape: if the required "
              "anti-periplanar H were absent, elimination would be very slow."),
        ("table", ["Substrate + conditions", "Mechanism", "Stereochemical outcome"], [
            ["secondary + CN^−^/DMSO", "S~N~2", "inversion"],
            ["tertiary + H~2~O, warm", "S~N~1 / E1", "racemic substitution + Zaitsev alkene"],
            ["secondary + EtO^−^/EtOH, heat", "E2", "anti elimination; alkene geometry from conformer"],
            ["primary + t-BuO^−^, heat", "E2", "anti elimination, Hofmann product"],
        ], [34, 20, 46], "Table 5.3 — three decisions, one method: substrate, nucleophile/base strength, solvent."),
    ],

    # ---------------------------------------------------------------- X-02
    "X-02": [
        ("h2", "6.11b  Naming and drawing an atropisomer"),
        ("p", "To draw the two enantiomers of a 2,2′,6,6′-tetrasubstituted biphenyl, draw the two rings in perspective, then hold one ring "
              "fixed and reflect the other through the plane of the first. The two drawings are mirror images and cannot be superimposed "
              "by rotation about the inter-ring bond, because that rotation is blocked. A common exam task is to decide whether a given "
              "substitution pattern is chiral; the four-question test below settles it without drawing both rings."),
        ("num", [
            "Are all four ortho positions substituted? If not, rotation is free and the molecule is achiral.",
            "Are the two rings identically substituted? If yes, a plane perpendicular to the axis survives and the molecule is achiral.",
            "Is there a C~2~ axis along the inter-ring bond with no plane? Then the molecule is chiral.",
            "Does the substitution give a plane through both rings (for example identical groups at 3 and 5 on one ring)? Then the molecule is achiral.",
        ]),
        ("table", ["Pattern", "Chiral?", "Deciding feature"], [
            ["2,2′-dimethylbiphenyl", "no", "two identical halves; free enough to rotate"],
            ["2,2′-dimethyl-6,6′-dinitrobiphenyl", "yes", "four different ortho groups, locked"],
            ["2,2′,6,6′-tetramethylbiphenyl", "no", "plane perpendicular to the axis"],
            ["2,2′,6,6′-tetramethylbiphenyl-3,3′-dicarboxylic acid", "yes", "the 3 and 3′ groups break the plane"],
            ["BINOL", "yes", "no plane; the two naphthyl halves are locked"],
        ], [46, 12, 42], "Table 6.6 — atropisomerism needs both bulk and asymmetry."),
        ("key", "Atropisomerism = restricted rotation + no plane. Bulk supplies the restriction; unsymmetrical substitution supplies the missing plane. Both are needed, and either one missing makes the compound achiral."),
    ],
    # ---------------------------------------------------------------- X-06
    "X-06": [
        ("h2", "6.25b  A worked stereoselective addition"),
        ("p", "**(R)-2-Methylbutanal + NaBH~4~.** The aldehyde carbon is prochiral; the adjacent C2 carries CH~3~, C~2~H~5~, H and CHO. Hydride "
              "can attack either face of the carbonyl, giving (2R,3R)- and (2R,3S)-2-methylbutan-1-ol — two diastereomers, not enantiomers, "
              "because the existing centre is unchanged."),
        ("p", "Which dominates? Apply Felkin–Anh: put the largest group on C2 (ethyl) perpendicular to the carbonyl plane, the medium group "
              "(methyl) on the other side, and the small group (H) between them. Hydride attacks the face opposite the large group. The "
              "major product is therefore the diastereomer with the new OH anti to the ethyl group — a stereoselective, not stereospecific, "
              "reaction."),
        ("table", ["Reagent", "Facial preference", "Reason"], [
            ["NaBH~4~, MeOH", "Felkin–Anh (opposite the large group)", "steric approach control"],
            ["LiAlH~4~, Et~2~O", "same, often lower selectivity", "smaller effective hydride donor"],
            ["Grignard, Et~2~O", "Cram chelation possible", "if a chelating group is present on C2"],
        ], [26, 36, 38], "Table 6.12 — the same substrate, three reagents, three selectivity models."),
        ("warn", "Do not call the two products enantiomers. The existing stereocentre is the same in both, so they are diastereomers — separable by ordinary means, with different physical properties."),
    ],
    # ---------------------------------------------------------------- X-07
    "X-07": [
        ("h2", "6.29b  Counting with two different symmetry operations"),
        ("p", "A molecule may have more than one operation that maps it onto itself, and each contributes its own fixed-point count. The "
              "tetramethylcyclobutane case of sheet J-05 is the smallest example: the square has a four-fold rotation and two kinds of "
              "mirror plane, and the up/down patterns must be counted under all of them, not just under a single flip."),
        ("table", ["Molecule", "Symmetry operations", "Orbit count", "Result"], [
            ["1,2,3,4-tetramethylcyclobutane", "E, C~2~, C~4~, C~4~^3^, 4 σ", "16 → 3", "3 achiral stereoisomers"],
            ["benzene, C~6~H~3~Cl~3~", "D~6h~ (12 operations)", "—", "3 positional isomers"],
            ["tartaric acid", "E, end-exchange", "(4 + 2)/2", "3 stereoisomers"],
            ["2,3,4-trihydroxypentanedioic acid", "E, end-exchange", "8 strings → 4", "2 active + 2 meso (pseudoasymmetric)"],
        ], [34, 26, 20, 20], "Table 6.15 — one method, four different groups."),
        ("p", "The last row is the subtle one. For an odd-n chain the exchange operation fixes the palindromic strings, but the middle "
              "carbon of a palindrome is pseudoasymmetric, so the two palindromes (R,S,R) and (S,R,S) are diastereomers, not the same "
              "compound. The orbit count therefore gives 8 arrangements → 6 orbits, matching active 6 + meso 2 in the Part I table when "
              "the ends are similar; the arithmetic is set out on sheet J-19."),
        ("key", "Orbit counting is not “divide by 2”. Each symmetry operation has its own fixed-point count, and the average of those counts is the number of distinct objects. For a chain that average is (2^n^ + F)/2."),
    ],
}
