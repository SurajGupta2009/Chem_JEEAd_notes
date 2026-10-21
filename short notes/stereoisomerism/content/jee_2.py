# -*- coding: utf-8 -*-
"""Part I, sheets J-09 … J-17."""

SHEETS = [
    # ------------------------------------------------------------------ J-09
    {
        "id": "J-09",
        "title": "Physical properties of geometrical isomers",
        "blocks": [
            ("p", "cis and trans isomers are diastereomers: same connectivity, different 3-D shape, different physical "
                  "properties. Four properties are examined again and again, and each has one controlling idea — learn the "
                  "idea, not the list."),
            ("table", ["Property", "Usually larger for", "Controlling idea"], [
                ["dipole moment, μ", "cis", "the two bond moments add (same side) in cis and partly cancel in trans"],
                ["boiling point", "cis (with an important exception)", "cis is more polar; dipole–dipole attraction is stronger in the liquid"],
                ["melting point", "trans", "trans packs better laterally, so the lattice is tighter and the melting point is higher"],
                ["solubility in water", "cis (usually)", "the cis isomer is more polar"],
                ["thermodynamic stability", "trans", "bulky groups are further apart — less steric strain"],
            ], [24, 30, 46], "Table 2.15 — one controlling idea per property; the exceptions follow from the same idea."),
            ("h2", "2.29  Dipole moment"),
            ("p", "A bond dipole is a vector along the bond. In cis-1,2-dichloroethene the two C–Cl bond moments point to the "
                  "same side and **add**; in the trans isomer they point in opposite directions and cancel. So μ(cis) > "
                  "μ(trans), and for trans-1,2-dichloroethene μ = 0. The same logic explains why cis-but-2-ene has a small "
                  "dipole while trans-but-2-ene has μ = 0."),
            ("fig", "butene", "Fig. 2.4 — cis and trans but-2-ene. The C–CH~3~ bond moments add in cis and cancel in trans, which is why only the cis isomer has a measurable dipole.", 0.24),
            ("warn", "Do not say “the trans isomer has zero dipole moment” as a universal rule. Trans-1,2-dichloroethene has μ = 0, but a trans isomer with two different polar groups (trans-1-chloro-1-propene, for example) has a non-zero dipole. Work the vectors."),
            ("h2", "2.30  Boiling point and solubility"),
            ("p", "Boiling requires the molecules to escape from each other, so it tracks **intermolecular attraction**: larger μ "
                  "gives stronger dipole–dipole attraction, so the cis isomer normally boils higher. Water solubility tracks "
                  "polarity and hydrogen bonding with water, so the cis isomer usually dissolves better as well."),
            ("p", "The exception that JEE loves is **maleic acid versus fumaric acid**. Maleic acid is the cis diacid; its "
                  "two –COOH groups are close enough to form an **intramolecular** hydrogen bond, which reduces the number of "
                  "groups available for hydrogen bonding with neighbours. Fumaric acid, being trans, cannot form that internal "
                  "bond, so it hydrogen-bonds **between** molecules. Fumaric acid therefore has the much higher melting point "
                  "and is much less soluble in water, despite being the symmetric isomer."),
            ("key", "Melting point follows symmetry; boiling point follows attractive forces. They usually point in opposite directions for a cis/trans pair, and an intramolecular hydrogen bond can reverse the boiling-point order."),
            ("warn", "Do not extend the maleic/fumaric argument to boiling point. Fumaric acid sublimes and decomposes near 200 °C and does not give a clean normal boiling point, so “fumaric has the higher boiling point” is not a safe exam answer. Stick to melting point and solubility, which are measured and quoted for this pair."),
            ("h2", "2.31  Stability"),
            ("p", "Trans is normally more stable because the bulky groups are further apart. The margin is small for but-2-ene "
                  "(about 4 kJ mol^−1^) and large when the substituents are big. Two important exceptions: cis-cycloalkenes "
                  "in small rings are more stable because trans is geometrically impossible, and cis-azobenzene is less "
                  "stable than trans by about 50 kJ mol^−1^ because the cis form forces the phenyl rings into each other."),
            ("h2", "2.32  Separating the pair"),
            ("p", "Because cis and trans are diastereomers, their boiling points differ and they can be separated by fractional "
                  "distillation; their melting points differ even more, which is why recrystallisation usually works for the "
                  "solids. This is the reason a cis/trans mixture is a normal separation problem, not a resolution problem — "
                  "no chiral reagent is needed."),
            ("note", "Numerical values in this section are standard textbook figures quoted to fix orders of magnitude (μ of cis-1,2-dichloroethene ≈ 1.9 D, μ of trans = 0; ΔH for cis → trans but-2-ene ≈ −4 kJ mol^−1^). Do not memorise the third digit; memorise the direction and the reason."),
            ("h2", "2.33  Three worked property questions"),
            ("p", "**(a) Which has the higher boiling point, cis- or trans-but-2-ene?** The cis isomer has a small but real "
                  "dipole (the two C–CH~3~ moments do not cancel), so dipole–dipole attraction is stronger in the liquid. "
                  "cis-But-2-ene boils at about 4 °C against 1 °C for trans; the difference is small because the molecule is "
                  "small, with polar substituents such as Cl the gap widens."),
            ("p", "**(b) Which has the higher melting point, maleic or fumaric acid?** Fumaric acid (trans) is more symmetric "
                  "and packs better in the crystal, so it melts at about 287 °C (with decomposition) against about 135 °C for "
                  "maleic acid. Maleic acid's intramolecular hydrogen bond also reduces its ability to form an extended lattice."),
            ("p", "**(c) Which is more soluble in water, cis- or trans-butenedioic acid?** Maleic acid is more polar and its "
                  "intramolecular hydrogen bond leaves one carbonyl and one hydroxyl available to water; fumaric acid's two "
                  "carboxyl groups are both engaged in the intermolecular network of the crystal, so it dissolves less readily. "
                  "Maleic acid is markedly more soluble."),
            ("table", ["Property", "Maleic (cis)", "Fumaric (trans)", "Reason"], [
                ["melting point", "≈ 135 °C", "≈ 287 °C", "packing / symmetry"],
                ["solubility in water", "high", "low", "polarity, H-bonding"],
                ["heat of combustion", "lower", "higher", "cis is less stable"],
                ["dipole moment", "larger", "zero by symmetry", "vector addition"],
            ], [24, 18, 18, 40], "Table 2.16 — the data pattern behind the rules."),
            ("warn", "Do not transfer the maleic/fumaric boiling-point reversal to every cis/trans pair. It happens because of a specific intramolecular hydrogen bond between two –COOH groups held close. Without such a group, the cis isomer boils higher."),
        ],
    },
    # ------------------------------------------------------------------ J-10
    {
        "id": "J-10",
        "title": "Optical activity and the polarimeter",
        "blocks": [
            ("p", "An optically active substance rotates the plane of vibration of plane-polarised light. Everything "
                  "quantitative in optical isomerism comes from one instrument, the polarimeter, and one formula, the "
                  "specific rotation."),
            ("h2", "3.1  Plane-polarised light"),
            ("p", "Ordinary light vibrates in every plane perpendicular to its direction of travel. Pass it through a Nicol "
                  "prism — a calcite (CaCO~3~) crystal cut so that only one plane survives — and the emerging light vibrates in "
                  "a single plane. That is plane-polarised light (PPL). Rotate the prism and you rotate the plane."),
            ("fig", "polarimeter", "Fig. 3.1 — the polarimeter. The sample is placed between two Nicol prisms; the rotation of the analyser needed to restore darkness equals the optical rotation of the sample.", 0.26),
            ("h2", "3.2  The polarimeter"),
            ("num", [
                "Source gives ordinary light.",
                "Polariser (first Nicol prism) converts it to PPL.",
                "Sample tube of length l contains the solution of concentration c.",
                "Analyser (a second Nicol prism) is rotated until the field is dark again.",
                "The angle moved by the analyser is the **observed rotation** α. Clockwise, looking towards the source, is **dextrorotatory** (+); anticlockwise is **laevorotatory** (−).",
            ]),
            ("p", "An inactive sample leaves the plane unchanged, so the analyser needs no adjustment. An active sample rotates it; "
                  "the two enantiomers rotate it by equal amounts in opposite directions."),
            ("h2", "3.3  Specific rotation"),
            ("p", "Observed rotation depends on how many active molecules the light meets, so it depends on the tube length, the "
                  "concentration, the temperature, the solvent and the wavelength. To compare compounds we quote the **specific "
                  "rotation**, defined at a stated wavelength and temperature:"),
            ("eq", ["[α] = α / (l × c)",
                    "l in dm · c in g mL^−1^"]),
            ("bul", [
                "α is the observed rotation in degrees, with its sign.",
                "l is the path length in **decimetres** (10 cm = 1 dm, so a 10 cm tube has l = 1).",
                "c is the concentration in **g mL^−1^**, not mol L^−1^; a value given as “5 g per 100 mL”, then c = 0.05 g mL^−1^.",
                "The standard sodium line is quoted as [α]~D~, at 589 nm.",
            ]),
            ("p", "**Worked numerical.** A 10 cm tube contains a solution of 5.0 g of a compound in 100 mL of solvent; the observed "
                  "rotation is +6.7°. Then l = 1 dm, c = 5.00/100 = 0.0500 g mL^−1^, and [α] = 6.7/(1 × 0.050) = +134°. A sample "
                  "of the same compound 2.5 g per 100 mL in a 20 cm tube gives α = [α] × l × c = 134 × 2 × 0.025 = +6.7° as well — "
                  "the specific rotation is a property of the compound, the observed rotation is a property of the experiment."),
            ("warn", "Units are the trap. A tube of 5 cm is l = 0.5 dm, not 5. A concentration of 10 g L^−1^ is 0.010 g mL^−1^, not 10. And the sign must be carried through the arithmetic."),
        ],
    },
    # ------------------------------------------------------------------ J-11
    {
        "id": "J-11",
        "title": "Chirality, stereocentres and the activity rules",
        "blocks": [
            ("h2", "3.4  What specific rotation does and does not tell you"),
            ("p", "The sign of [α] tells you the direction of rotation; it does not tell you the configuration. D-(+)-"
                  "glyceraldehyde rotates light clockwise and has the R configuration; some R compounds are (−). Equally, the "
                  "magnitude depends on wavelength and solvent, so a rotation measured in water cannot be compared with one "
                  "measured in chloroform unless both are stated."),
            ("key", "Configuration (R/S, D/L), optical rotation sign ((+)/(−)) and chirality are three different things. A molecule can be (R) and laevorotatory; a meso compound is achiral whatever you write next to it."),
            ("warn", "A racemic mixture has α = 0 because the two rotations cancel. A meso compound has α = 0 because the molecule is achiral — internal compensation. The measured number is the same; the cause is not."),
            ("h2", "3.5  Chiral and achiral"),
            ("p", "A molecule is chiral if it cannot be superimposed on its mirror image. Your hands are the model: mirror images, "
                  "never superimposable. The test is always the same: build the mirror image mentally and try to rotate it onto "
                  "the original. If every atom can be brought into coincidence, the molecule is achiral and optically inactive."),
            ("fig", "chiralcarbon", "Fig. 3.2 — a carbon with four different groups and its mirror image. Three groups can always be matched; the fourth always ends up on the wrong side, which is why the pair is non-superimposable.", 0.32),
            ("h2", "3.6  The chiral carbon"),
            ("p", "A tetrahedral carbon carrying four different groups is a **stereocentre** (chiral centre, asymmetric carbon). "
                  "Isotopes count as different groups; H and D make a chiral carbon. Carbon atoms that are sp or sp^2^ hybridised "
                  "can never be stereocentres, because they do not carry four groups in a tetrahedral arrangement."),
            ("p", "To test a candidate carbon, compare the **whole group** attached along each bond, not just the first atom. Two "
                  "chains that look identical near the carbon may differ three bonds away. This is exactly the CIP comparison of "
                  "section 2.8 applied to four groups."),
            ("h2", "3.7  The three rules for optical activity"),
            ("table", ["Situation", "Conclusion", "Reason"], [
                ["exactly one stereocentre", "always optically active", "no internal plane or centre is possible"],
                ["more than one, dissimilar ends", "always optically active", "no internal mirror plane would have to map the two ends onto each other"],
                ["more than one, similar ends", "may be active or meso", "a symmetric conformation can supply an internal plane"],
                ["no stereocentre", "may still be active", "axial or planar chirality (sections 3.35–3.37)"],
            ], [26, 24, 50], "Table 3.2 — the three rules and their reasons."),
            ("key", "One stereocentre guarantees activity. Many stereocentres do not guarantee activity, and no stereocentre does not guarantee inactivity. The only universal test is the search for symmetry elements."),
            ("h2", "3.8  Finding stereocentres in real structures"),
            ("bul", [
                "**Open chains**: mark every carbon with four different groups, including CH(OH), CH(NH~2~), CH(halogen) and carbons carrying D/T.",
                "**Rings**: a ring carbon with two ring paths that differ (count round the ring both ways) plus H plus a substituent is a stereocentre; 1,2- and 1,4-disubstituted cyclohexanes with different substituents qualify.",
                "**Fused rings**: count the junction carbons whose four groups differ, but remember that a rigid junction may lock two centres together (section 6.14).",
                "**A carbon flanked by two stereocentres** can itself become a stereocentre, because “R” and “S” are different groups. This is the pseudoasymmetric carbon of section 6.33.",
                "**Nitrogen**: an amine nitrogen inverts rapidly at room temperature and is not a stereocentre; a quaternary ammonium nitrogen with four different groups is; a nitrogen in a three-membered ring inverts slowly enough to be one.",
            ]),
            ("h2", "3.9  Five structures, five decisions"),
            ("table", ["Structure", "Stereocentre?", "Why"], [
                ["CH~3~CH(OH)COOH (lactic acid)", "yes, 1", "C2 carries H, OH, CH~3~, COOH"],
                ["CH~3~CH~2~CH~2~OH", "no", "no carbon has four different groups"],
                ["HOOC–CH(OH)–CH(OH)–COOH (tartaric)", "yes, 2", "C2 and C3, each with H, OH, COOH and the other half"],
                ["(CH~3~)~2~C(OH)CH~2~CH~3~", "no", "C2 carries two CH~3~"],
                ["CH~3~CH=CHCH~3~", "no", "no tetrahedral carbon with four groups"],
            ], [34, 18, 48], "Table 3.3 — the first decision in every question: does a stereocentre exist?"),
            ("h2", "3.10  Stereocentres in rings and bridged systems"),
            ("p", "In a ring, the two “ring paths” from a carbon count as two substituents. If they are different — which happens "
                  "whenever the ring is unsymmetrically substituted — that carbon is a stereocentre. In a bridged bicyclic the two "
                  "bridgehead carbons can be stereocentres, but because each bridgehead's configuration is tied to the other's "
                  "(the ring cannot turn one without the other), the pair counts as **one** independent stereocentre in the "
                  "counting formulas."),
            ("note", "Ring junction stereochemistry is where the optical and geometrical chapters meet: a cis junction often has a plane, and a trans junction often removes it. Sheets X-03 and X-05 take this further."),
        ],
    },
    # ------------------------------------------------------------------ J-12
    {
        "id": "J-12",
        "title": "Elements of symmetry and the activity test",
        "blocks": [
            ("h2", "3.11  Plane of symmetry"),
            ("p", "A plane of symmetry (σ) divides the molecule into two halves that are mirror images. Its presence makes the "
                  "molecule achiral, because the mirror image can be superimposed by reflecting through that plane. Look for "
                  "planes in the molecular plane, perpendicular to it, and — often forgotten — through a bond or through a ring "
                  "carbon."),
            ("h2", "3.12  Centre of symmetry"),
            ("p", "A centre of symmetry (i) is a point such that every atom has an identical atom on the opposite side at the same "
                  "distance. Molecules with i are achiral; the mirror image is generated by inversion, which is a rotation plus a "
                  "reflection in disguise. trans-But-2-ene, trans-decalin and many trans-1,4-disubstituted cyclohexanes have a "
                  "centre of symmetry."),
            ("h2", "3.13  Alternating axis"),
            ("p", "An alternating axis S~n~ is a rotation by 360°/n followed by reflection in a plane perpendicular to the axis. "
                  "S~1~ is the same as a plane of symmetry, S~2~ is the same as a centre of symmetry, and an S~n~ axis does not by "
                  "itself make a molecule achiral — the only achiral cases are those that can be written with σ or i."),
            ("key", "S~1~ = σ and S~2~ = i. Those two identities are worth memorising because they explain why “it has an S~n~ axis” is not the test: after writing S~1~ and S~2~, the test reduces to “is there a plane or a centre?”"),
            ("h2", "3.14  The activity test"),
            ("num", [
                "Convert every stereocentre to (R) or (S), or convert the whole molecule to one projection.",
                "Look for a plane of symmetry, including the conformation you would not normally draw.",
                "Look for a centre of symmetry; in symmetric chains it often appears exactly when the two halves read opposite.",
                "If neither is present, the molecule is chiral; if either is present, it is achiral.",
            ]),
            ("p", "Three facts make the test quick. First, any molecule with one stereocentre is automatically chiral, so only "
                  "molecules with two or more need the test. Second, a symmetric chain with an odd number of centres has a plane "
                  "through the middle centre (which is why that centre is pseudoasymmetric). Third, a symmetric chain with an even "
                  "number of centres has a plane through the central bond when the two halves are opposite (R,S) — the meso case."),
            ("table", ["Molecule", "Symmetry elements", "Chiral?"], [
                ["tartaric acid (R,R)", "C~2~ only", "yes"],
                ["tartaric acid (R,S)", "σ (internal), i", "no (meso)"],
                ["2,3-dichlorobutane (R,R)", "C~2~", "yes"],
                ["2,3-dichlorobutane (R,S)", "σ", "no (meso)"],
                ["cis-1,2-dimethylcyclopropane", "σ", "no"],
                ["trans-1,2-dimethylcyclopropane", "C~2~ only", "yes"],
                ["cis-1,4-dimethylcyclohexane", "σ, i", "no"],
            ], [36, 34, 30], "Table 3.4 — a table worth reproducing in the exam margin before you start a counting question."),
            ("warn", "The absence of a plane is not the same as chirality, and the presence of a C~2~ axis is not a sign of chirality either — it is the absence of any improper operation (σ, i, S~n~) that matters. That is why this sheet tests σ and i, and not C~n~."),
        ],
    },
    # ------------------------------------------------------------------ J-13
    {
        "id": "J-13",
        "title": "Enantiomers, diastereomers, meso and racemic",
        "blocks": [
            ("h2", "3.15  The four labels"),
            ("table", ["Pair / species", "Relationship", "Physical properties", "Separable by distillation?"], [
                ["enantiomers", "non-superimposable mirror images", "identical except the sign of [α]", "no"],
                ["diastereomers", "stereoisomers that are not mirror images", "different mp, bp, solubility, [α]", "yes"],
                ["meso compound", "a single achiral molecule with stereocentres", "—", "it is one compound"],
                ["racemic mixture", "1:1 mixture of two enantiomers", "same as either pure enantiomer", "no (it is a mixture, not a compound)"],
            ], [22, 34, 26, 18], "Table 3.5 — the table examiners use for one-mark contrasts."),
            ("h2", "3.16  Meso compounds"),
            ("p", "A meso compound contains stereocentres but is achiral because an internal plane (or centre) makes the two halves "
                  "cancel. The classic case is **tartaric acid**: (R,R) and (S,S) are the active pair, and (R,S) is meso. The meso "
                  "form has a plane through the middle of the C2–C3 bond, so its mirror image is itself."),
            ("fig", "tartaric", "Fig. 3.3 — the three stereoisomers of tartaric acid. The (R,S) form has an internal mirror plane (dashed) and is meso; the (R,R) and (S,S) forms are the active enantiomeric pair.", 0.40),
            ("p", "Two 3-D consequences are worth remembering. First, a meso compound is a diastereomer of both active forms, so it has "
                  "different physical properties and can be separated from them. Second, a meso molecule has **no optical rotation** "
                  "but is not a racemic mixture — melting-point and crystallography can tell the two apart."),
            ("h2", "3.17  Racemic mixtures and compensation"),
            ("p", "A racemic mixture contains equal amounts of the two enantiomers; their rotations are equal and opposite, so the "
                  "observed rotation is zero. This is **external compensation** — two different molecules cancelling. A meso "
                  "compound is inactive by **internal compensation** — one molecule cancelling itself. The distinction is a standard two-mark question."),
            ("bul", [
                "Racemic mixtures are written (±) or (d,l).",
                "They form whenever a reaction creates a stereocentre in an achiral environment, because the two faces of a planar intermediate are attacked equally.",
                "Racemisation is the conversion of a pure enantiomer into a racemic mixture — for example by enolisation at a stereocentre, or by an S~N~1 reaction through a planar carbocation.",
            ]),
            ("key", "Meso = one molecule, internally compensated. Racemic = two molecules, externally compensated. Both show α = 0; only the meso compound is achiral."),
            ("h2", "3.18  Special cases"),
            ("p", "**(a) Tartaric acid.** Three stereoisomers: (R,R), (S,S) active; (R,S) meso. The meso form has a plane, so it is "
                  "achiral; the two active forms are enantiomers of each other and diastereomers of the meso form."),
            ("p", "**(b) 2,3-Dichlorobutane.** Same pattern: (R,R) and (S,S) are the active pair, (R,S) is meso. Note that the two "
                  "halogens are identical, so the ends are similar and the meso form exists; replace one Cl by Br and the ends "
                  "become different and all four stereoisomers are active."),
            ("p", "**(c) 2,3-Dihydroxybutanedioic acid versus 2,3-dihydroxypentanedioic acid.** The first is tartaric (similar "
                  "ends, meso exists). The second has different ends, so no meso form; four stereoisomers, all active."),
            ("h2", "3.19  Meso identification, worked three ways"),
            ("num", [
                "**Draw the Fischer projection flat.** If the top half is the mirror image of the bottom half across a horizontal mid-line, the compound is meso.",
                "**Convert to (R)/(S).** If the descriptors are opposite at every centre (R,S or S,R) and the chain is symmetric, it is meso.",
                "**Look for the plane in 3-D.** In a staggered conformation with the two halves anti, the plane through the central bond becomes visible.",
            ]),
            ("p", "All three methods must agree. The Fischer test is fastest under time pressure, but it is only valid while the "
                  "projection is correctly drawn; that is why the conversion to (R)/(S) is the safe check."),
            ("h2", "3.20  Separating meso from racemic"),
            ("p", "A meso compound and a racemic mixture can both show zero rotation, but they behave differently: the meso compound "
                  "is a single substance with a sharp melting point, while the racemic mixture melts over a range (and often lower "
                  "than either pure enantiomer). Crystallisation of the racemic mixture may give a racemic compound (a 1:1 crystal) "
                  "or a conglomerate (a mechanical mixture of the two enantiomer crystals) — the second can, in favourable cases, be "
                  "separated by hand-picking or by preferential crystallisation."),
            ("warn", "A racemic mixture does not have to be 50:50 exactly to show zero rotation; any mixture whose rotations cancel is optically inactive. The exam phrase is “optically inactive due to external compensation”, not “achiral”."),
        ],
    },
    # ------------------------------------------------------------------ J-14
    {
        "id": "J-14",
        "title": "Resolution: separating enantiomers",
        "blocks": [
            ("p", "Enantiomers have identical physical properties in an achiral environment, so they cannot be separated by "
                  "distillation, crystallisation or ordinary chromatography. Separation requires making them diastereomeric, and "
                  "that means introducing a chiral influence."),
            ("h2", "3.21  The chemical method"),
            ("num", [
                "React the racemic mixture with a single enantiomer of a chiral reagent (a resolving agent).",
                "The two enantiomers now form two **diastereomeric** salts (or esters, or amides), which have different physical properties.",
                "Separate the diastereomers by fractional crystallisation.",
                "Hydrolyse each diastereomer back to the pure enantiomer and recover the resolving agent.",
            ]),
            ("p", "The classical example is the resolution of a racemic amine with (+)-tartaric acid: the two diastereomeric "
                  "tartrates have different solubilities, so one crystallises first. Racemic acids are resolved with a chiral base "
                  "such as brucine or quinine."),
            ("key", "Resolution works by converting an enantiomer pair into a diastereomer pair. Diastereomers differ in physical properties; enantiomers do not. Every resolution method is a version of that sentence."),
            ("h2", "3.22  The other methods"),
            ("bul", [
                "**Biological / enzymatic**: an enzyme is chiral and acts on only one enantiomer, so it can destroy one component (kinetic resolution) or convert it selectively.",
                "**Chiral chromatography**: a chiral stationary phase (cellulose derivatives, cyclodextrins) forms diastereomeric complexes with the two enantiomers, so they elute at different times.",
                "**Mechanical separation**: only when the racemic mixture crystallises as a conglomerate; historically the first resolution (Pasteur, tartaric acid salts, 1848).",
                "**Preferential crystallisation**: seeding a supersaturated racemic solution with one pure enantiomer crystal.",
            ]),
            ("h2", "3.23  Optical purity"),
            ("p", "The composition of a mixture of enantiomers is expressed as **optical purity** (also called enantiomeric excess, ee):"),
            ("eq", ["ee = (observed [α] / [α] of the pure enantiomer) × 100 %",
                    "ee = ([R] − [S]) / ([R] + [S]) × 100 %"]),
            ("p", "A sample with [α] = +9.0° whose pure enantiomer has [α] = +15.0° has ee = 60 %, so it contains 80 % of one "
                  "enantiomer and 20 % of the other. Note that ee is a ratio of rotations, not a ratio of concentrations taken "
                  "directly — the two are equivalent only because rotation is proportional to concentration."),
            ("note", "Optical purity and enantiomeric excess are the same number when the only chiral species present are the two enantiomers. If a meso compound or an achiral impurity is present, the measured rotation no longer reports ee reliably."),
            ("h2", "3.24  Three worked numericals"),
            ("p", "**(a)** A solution contains 4.0 g of a compound in 50 mL, in a 20 cm tube; the observed rotation is −8.0°. "
                  "Then l = 2 dm and c = 0.080 g mL^−1^, so [α] = −8.0/(2 × 0.080) = −50°. The substance is laevorotatory."),
            ("p", "**(b)** Pure (R)-butan-2-ol has [α] = +13.5°. What rotation would a 15 cm tube containing 0.20 g mL^−1^ show? "
                  "α = [α] × l × c = 13.5 × 1.5 × 0.20 = +4.05°."),
            ("p", "**(c)** A 10 cm tube of a 2.0 % (w/v) solution rotates PPL by +2.4°. Then [α] = 2.4/(1 × 0.020) = +120°. A 2.0 % w/v "
                  "solution is 2.0 g per 100 mL = 0.020 g mL^−1^; converting correctly is the whole question."),
            ("table", ["Given", "Convert to", "Divide / multiply by"], [
                ["10 cm tube", "l = 1.00 dm", "÷ 10"],
                ["20 cm tube", "l = 2.00 dm", "÷ 10"],
                ["5 cm tube", "l = 0.50 dm", "÷ 10"],
                ["x g per 100 mL", "c = x/100 g mL^−1^", "÷ 100"],
                ["x g L^−1^", "c = x/1000 g mL^−1^", "÷ 1000"],
                ["x % w/v", "c = x/100 g mL^−1^", "÷ 100"],
            ], [26, 30, 44], "Table 3.6 — unit conversions that decide the mark."),
            ("warn", "Blind use of the observed rotation is proportional to path length and to concentration. c = [α] l c, which is exactly the definition rearranged. It holds for dilute solutions; at high concentration, solute–solute interactions make [α] non-linear in c (and [α] then depends slightly on the concentration at which it was measured)."),
        ],
    },
    # ------------------------------------------------------------------ J-15
    {
        "id": "J-15",
        "title": "Projections: wedge–dash, Fischer, Newman, sawhorse",
        "blocks": [
            ("h2", "3.25  Fischer projection rules"),
            ("num", [
                "The carbon chain is drawn **vertically**, with the most oxidised carbon at the top.",
                "**Vertical bonds go back**, away from you; **horizontal bonds come forward**, towards you.",
                "The intersection of the cross is a carbon; its substituents are the four bond ends.",
                "A 90° rotation in the plane of the paper inverts the configuration; a 180° rotation in the plane preserves it.",
                "Swapping any two groups at a centre inverts that centre; swapping twice restores it.",
            ]),
            ("fig", "fischer", "Fig. 3.4 — the same molecule drawn as a Fischer projection and as a wedge–dash structure. In the Fischer, the two horizontal bonds come towards you and the two vertical bonds go back.", 0.34),
            ("key", "In a Fischer projection, a 180° rotation in the plane is allowed and keeps the molecule the same; a 90° rotation is forbidden because it turns the vertical (back) bonds into horizontal (front) bonds. This one rule answers most projection questions."),
            ("h2", "3.26  Converting between projections"),
            ("p", "The safe conversion is always via the wedge–dash drawing. Build the molecule once in 3-D, then read off each "
                  "projection from it. Do not try to convert Fischer directly to Newman by moving groups on the paper — that is "
                  "where most errors happen."),
            ("num", [
                "Fischer → wedge–dash: put the vertical groups behind the plane and the horizontal groups in front; then rotate the whole molecule so that the main chain is zig-zag.",
                "Wedge–dash → Newman: look down the bond of interest; the group on the front carbon is the centre of the front circle, the three others radiate from it.",
                "Newman → sawhorse: tilt the Newman projection so that the front and back carbons are visible as points, and connect the corresponding substituents.",
                "Sawhorse → Fischer: rotate about the central bond until the main chain is vertical and both ends point away from you, then flatten.",
            ]),
            ("h2", "3.27  Reading a Newman projection"),
            ("p", "In a Newman projection you look down a C–C bond. The front carbon is the point where three bonds meet; the back "
                  "carbon is the circle. A substituent drawn from the circle is on the back carbon, and its apparent position is "
                  "the projection of the real bond. The dihedral angle is measured between a front and a back substituent, "
                  "looking along the bond."),
            ("fig", "newman", "Fig. 3.5 — staggered and eclipsed Newman projections of ethane. In the eclipsed form each rear C–H hides behind a front C–H; that is the source of torsional strain.", 0.26),
            ("h2", "3.28  Two worked conversions"),
            ("p", "**(a) (R)-lactic acid as a Fischer.** Put COOH at the top and CH~3~ at the bottom; H and OH go on the horizontal "
                  "arms. With OH on the right and H on the left, the priorities are OH (1) > COOH (2) > CH~3~ (3) > H (4). H is on "
                  "a horizontal arm, so it points towards you; read the other three in the direction 1 → 2 → 3 and reverse the "
                  "answer. 1 → 2 → 3 runs clockwise → S, reversed → R."),
            ("p", "**(b) The same molecule as a Newman projection.** Looking down C2–C3 with COOH at the top of the front carbon, "
                  "the OH and H are arranged so that OH is on the right and H on the left; the back carbon carries three H. "
                  "Rotating the front carbon to bring H to the back position reproduces the Fischer arrangement, which is the "
                  "check that the conversion is right."),
            ("warn", "Never rotate a Fischer projection by 90° to make it fit the page. A 90° rotation converts every wedge into a dash and gives the enantiomer. Rotate by 180°, or redraw from the 3-D structure."),
        ],
    },
    # ------------------------------------------------------------------ J-16
    {
        "id": "J-16",
        "title": "R/S: the absolute configuration",
        "blocks": [
            ("h2", "3.29  The four steps"),
            ("num", [
                "Rank the four groups on the stereocentre by CIP priority (section 2.8).",
                "Look along the bond from the stereocentre to the **lowest-priority group** (usually H), so that H points away from you.",
                "Read the direction 1 → 2 → 3: clockwise is **R** (*rectus*), anticlockwise is **S** (*sinister*).",
                "If the lowest-priority group points towards you, reverse the answer.",
            ]),
            ("key", "R/S is a property of the whole configuration, not of a drawing. Any rotation, any projection, any conformation of the same molecule gives the same descriptor — that is exactly why it is useful."),
            ("h2", "3.30  Worked examples"),
            ("p", "**(a) 2-Butanol, CH~3~CH(OH)CH~2~CH~3~.** Priorities: OH (1) > CH~2~CH~3~ (2) > CH~3~ (3) > H (4). With H pointing away "
                  "and the sequence 1 → 2 → 3 clockwise, the configuration is (R)."),
            ("p", "**(b) Glyceraldehyde, HOCH~2~CH(OH)CHO.** Priorities on C2: OH (1) > CHO (2) > CH~2~OH (3) > H (4) — the aldehyde "
                  "carbon counts as (O, O, H) and beats CH~2~OH, which is (O, H, H). D-Glyceraldehyde is (R)."),
            ("p", "**(c) A Fischer with H horizontal.** If H is on a horizontal arm it points towards you, so read 1 → 2 → 3 and "
                  "reverse. A clockwise 1 → 2 → 3 with H horizontal is (S)."),
            ("p", "**(d) A molecule with two centres.** Assign each centre separately; the molecule's name lists both, e.g. "
                  "(2R,3S)-2,3-dichloropentane. Do not try to assign “the molecule” a single descriptor."),
            ("h2", "3.31  R/S for special centres"),
            ("table", ["Centre", "How to rank", "Note"], [
                ["carbon with D/T", "D > H; T > D", "isotopes are different groups"],
                ["nitrogen (quaternary)", "four groups, no lone pair", "a stereocentre if all four differ"],
                ["nitrogen (amine)", "three groups + lone pair", "inverts rapidly; not a stereocentre unless in a small ring"],
                ["sulfur (sulfoxide)", "lone pair is the lowest ligand", "sulfoxides are configurationally stable"],
                ["phosphorus (phosphine)", "lone pair lowest", "inverts slowly; can be resolved"],
                ["allene end", "axial, not a centre", "use a/d or the axial R/S convention of section 6.8"],
            ], [26, 32, 42], "Table 3.8 — centres beyond carbon, and why some of them are not centres."),
            ("warn", "The lone pair is always the lowest-priority “group”. A nitrogen with three different groups plus a lone pair has a configuration, but in an ordinary amine it inverts at about 10^10^ s^−1^ at room temperature, so it is not a resolvable stereocentre."),
        ],
    },
    # ------------------------------------------------------------------ J-17
    {
        "id": "J-17",
        "title": "D/L, threo/erythro and the older nomenclature",
        "blocks": [
            ("h2", "3.32  Relative configuration"),
            ("p", "Before R/S existed, configurations were related to a standard: **D-(+)-glyceraldehyde**. A compound whose "
                  "highest-priority stereocentre has the same arrangement as D-glyceraldehyde is given the D prefix; the opposite "
                  "is L. This is *relative* configuration: it names the family, not the absolute arrangement."),
            ("p", "The convention survives because nature uses it. Amino acids are almost all L, sugars are mostly D, and the "
                  "phrases “D-sugar” and “L-amino acid” carry biochemical meaning that R/S does not."),
            ("table", ["Prefix", "What it fixes", "What it does not fix"], [
                ["D / L", "the arrangement at the highest-priority centre relative to glyceraldehyde", "the sign of rotation"],
                ["(+) / (−)", "the direction the compound rotates PPL", "the configuration"],
                ["R / S", "the absolute configuration at each centre", "the sign of rotation"],
            ], [18, 44, 38], "Table 3.9 — three independent labels that are constantly confused."),
            ("key", "D and L do not mean (+)- and (−)-. D-Glyceraldehyde happens to be (+), but D-lactic acid is (−). Any statement that equates D/L with +/− is wrong."),
            ("h2", "3.33  threo and erythro"),
            ("p", "For a chain with two adjacent stereocentres carrying the same groups, the older names describe the relationship "
                  "between the two substituents in the Fischer projection. If the two identical groups are on the **same side**, "
                  "the arrangement is **erythro**; if they are on opposite sides, it is **threo**. The names come from the sugars "
                  "erythrose and threose."),
            ("bul", [
                "erythro: the two like groups are on the same side of the Fischer projection.",
                "threo: the two like groups are on opposite sides.",
                "The names are **relative** — they describe one diastereomer relative to the other, and each of them may be chiral or meso depending on the ends.",
                "For 2,3-dichlorobutane the erythro form is the meso one (a plane), and the threo form is the active pair.",
            ]),
            ("h2", "3.34  Why the older names survive"),
            ("p", "Three reasons. First, the names describe a **relationship** that R/S does not state directly: whether two "
                  "substituents are on the same face. Second, they are shorter to say for long chains. Third, they are used in "
                  "the carbohydrate and amino-acid literature, where the relative arrangement is what matters chemically "
                  "(for example, in the erythro/threo selectivity of aldol reactions)."),
            ("p", "The exam-safe approach is to give both: “the threo pair, i.e. (2R,3R) and (2S,3S)”. If a question uses "
                  "threo/erythro without defining the reference groups, state your definition in one line before answering."),
            ("note", "threo/erythro are not the same as syn/anti. syn/anti describe a double bond or a ring face; threo/erythro describe two adjacent tetrahedral centres. Confusing them is a common way to lose a mark on a straightforward question."),
            ("warn", "Do not assume that erythro always means meso. Erythro means “like groups on the same side”; whether that gives a plane depends on the ends. With different ends, the erythro form is chiral as well."),
        ],
    },
]
