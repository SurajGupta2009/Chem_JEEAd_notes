# -*- coding: utf-8 -*-
"""Part II, sheets X-01 … X-06 — JEE Advanced extensions."""

SHEETS = [
    # ------------------------------------------------------------------ X-01
    {
        "id": "X-01",
        "title": "Symmetry, rigorously",
        "blocks": [
            ("lead", "Part I used three symmetry elements as a yes/no test. Part II states the criterion properly, because the harder "
                     "JEE Advanced items — and every isomer-counting question with a ring — need the full set."),
            ("h2", "6.1  The five operations"),
            ("table", ["Element", "Operation", "Symbol", "Improper?"], [
                ["identity", "do nothing", "E", "—"],
                ["proper axis", "rotate 360/n", "C~n~", "no"],
                ["plane", "reflect", "σ", "yes"],
                ["centre", "invert through a point", "i", "yes"],
                ["alternating axis", "rotate 360/n, then reflect in the plane perpendicular to the axis", "S~n~", "yes (n even), no (n odd)"],
            ], [18, 46, 18, 18], "Table 6.1 — the complete inventory for molecular symmetry."),
            ("p", "Only the **improper** operations (σ, i, S~n~) change the handedness of an object. A molecule is chiral if and only if it "
                  "has no improper operation. Proper rotations C~n~ preserve handedness, so a molecule with a C~3~ axis can be perfectly chiral."),
            ("key", "Chiral ⇔ no σ, no i, no S~n~. Not “no symmetry”: a chiral molecule may have as many proper axes as it likes."),
            ("h2", "6.2  The identities worth knowing"),
            ("bul", [
                "**S~1~ = σ.** Rotate by 360° (do nothing) and reflect: that is a plain reflection in a plane.",
                "**S~2~ = i.** Rotate by 180° and reflect in the perpendicular plane: that is inversion.",
                "**S~n~ with n even implies a C~n/2~ axis**, so S~4~ implies C~2~, S~6~ implies C~3~. Improper axes therefore do not add new chirality decisions beyond σ and i for small n.",
                "**σ and i together imply a C~2~ axis** through their intersection, which is why trans-decalin (i) also has a C~2~.",
            ]),
            ("h2", "6.3  Worked symmetry assignments"),
            ("table", ["Molecule", "Elements present", "Chiral?"], [
                ["H~2~O", "C~2~, two σ~v~", "no"],
                ["NH~3~", "C~3~, three σ~v~", "no"],
                ["CH~4~", "4 C~3~, 3 S~4~, 6 σ~d~", "no"],
                ["CHFClBr", "none (C~1~)", "yes"],
                ["staggered ethane", "C~3~, 3 C~2~, i, S~6~", "no"],
                ["chair cyclohexane", "C~3~, 3 C~2~, 3 σ~d~, i", "no"],
                ["twist-boat cyclohexane", "C~2~, no σ, no i, S~n~", "yes (a pair)"],
            ], [28, 40, 32], "Table 6.2 — assignments to check your intuition against."),
            ("h2", "6.4  Asymmetric versus dissymmetric"),
            ("p", "A molecule with no element at all except the identity (point group C~1~) is **asymmetric** and also chiral. A molecule with "
                  "proper axes but no improper element (point group D~n~, for example) is **dissymmetric**: it is chiral, but it has "
                  "rotational symmetry. This is the precise version of the statement “all asymmetric molecules are chiral, but not all "
                  "chiral molecules are asymmetric”."),
            ("h2", "6.5  Why the test is enough"),
            ("p", "If an improper operation maps the molecule onto itself, there is a rigid motion that carries the mirror image onto the "
                  "original — so the two are superimposable and the molecule is achiral. Conversely, if the mirror image can be "
                  "superimposed on the original, the operation that does it is improper. That is the proof in one line, and it is worth "
                  "writing in an answer."),
            ("h2", "6.6  Symmetry of the conformers of ethane"),
            ("p", "Staggered ethane (D~3d~) has a C~3~ axis, three C~2~ axes perpendicular to it, a centre of symmetry, an S~6~ axis and three "
                  "σ~d~ planes. Eclipsed ethane (D~3h~) has a C~3~ axis, three C~2~ axes, a σ~h~ plane and three σ~v~ planes, and no centre. "
                  "Both are achiral, but for different reasons."),
            ("table", ["Species", "Proper axes", "Improper elements", "Chiral?"], [
                ["staggered ethane", "C~3~, 3 C~2~", "i, S~6~ (and σ~d~)", "no"],
                ["eclipsed ethane", "C~3~, 3 C~2~", "σ~h~, S~3~", "no"],
                ["gauche butane", "C~2~", "none", "yes (conformational)"],
                ["anti butane", "C~2h~", "i, σ~h~", "no"],
                ["chair cyclohexane", "C~3~, 3 C~2~", "i, S~6~, σ~d~", "no"],
                ["twist-boat cyclohexane", "C~2~", "none", "yes (a pair)"],
            ], [26, 22, 26, 26], "Table 6.3 — the same molecule can be chiral in one conformation and achiral in another."),
            ("p", "The twist-boat of cyclohexane is chiral, and the two twist-boats are enantiomers. They interconvert through the (achiral) "
                  "chair at a rate of about 10^5^ s^−1^ at room temperature, so the population of the chiral species is negligible, and "
                  "cyclohexane itself is achiral. At low temperature the interconversion slows and the chirality of a fleeting species "
                  "can be observed spectroscopically."),
            ("h2", "6.7  A final checklist for “is it chiral?”"),
            ("num", [
                "Draw the most symmetric conformation you can find. If it has σ or i, the molecule is achiral — stop.",
                "If no improper element is present, look for a stereocentre, a chiral axis or a chiral plane to explain the chirality.",
                "If the molecule is flexible, ask whether the conformers interconvert at room temperature. If they do, the sample is achiral even if individual conformers are chiral.",
                "If the interconversion is slow (atropisomerism, a rigid ring), the conformer is the molecule, and the chirality is observable.",
            ]),
            ("warn", "Point-group labels are a convenience, not a requirement. If you can point to a plane, a centre or an S~n~ axis, you have already decided the question; naming the group adds nothing to the chemistry."),
        ],
    },
    # ------------------------------------------------------------------ X-02
    {
        "id": "X-02",
        "title": "Axial chirality: allenes, spiro and biphenyls",
        "blocks": [
            ("h2", "6.8  The chirality axis"),
            ("p", "In an allene the four substituents lie in two perpendicular planes, and the molecule has a chiral axis along the C=C=C line. "
                  "If both ends carry two different groups, the molecule is chiral. The two enantiomers are labelled aR and aS (or P and M); "
                  "the priority rule for the axis is the same CIP apparatus applied to each end, and the descriptors follow from the "
                  "arrangement of the higher-priority groups."),
            ("p", "For JEE it is enough to know that the enantiomers exist and are not labelled with R/S at a carbon. If you do assign the axial "
                  "descriptor, look down the axis, rank the two groups on each end, and compare the near and far ends exactly as you would "
                  "for a stereocentre."),
            ("h2", "6.9  Cumulenes with more than two double bonds"),
            ("table", ["Number of C=C", "End planes", "Chirality (both ends unsymmetrical)", "Geometrical isomerism"], [
                ["2", "perpendicular", "yes, chiral axis", "no"],
                ["3", "coplanar", "no", "yes, E/Z"],
                ["4", "perpendicular", "yes, chiral axis", "no"],
                ["5", "coplanar", "no", "yes, E/Z"],
            ], [18, 22, 34, 26], "Table 6.4 — the odd/even rule continued indefinitely; each additional double bond rotates the far plane by 90°."),
            ("p", "The reason is that each additional double bond rotates the plane of the far end by 90°: with an even number of double bonds "
                  "the planes are perpendicular (no common reference plane, hence chirality), and with an odd number they are coplanar "
                  "(a common reference plane, hence cis/trans)."),
            ("h2", "6.10  Spiro compounds"),
            ("p", "Two rings sharing a tetrahedral carbon lie in perpendicular planes. If each ring carries different substituents on its two "
                  "sides, the molecule has a chirality axis through the spiro carbon. The decisive test is still a mirror plane: if either "
                  "ring is symmetric about the plane containing the other ring, the molecule is achiral."),
            ("key", "Draw each ring separately and ask whether it has a plane through the spiro carbon. Two unsymmetrical rings → chiral axis; one symmetrical ring → achiral."),
            ("h2", "6.11  Biphenyls and atropisomerism"),
            ("p", "The inter-ring bond of a biphenyl is a single bond, but rotation is hindered by the ortho hydrogens. With four bulky ortho "
                  "substituents the barrier is 80–160 kJ mol^−1^, high enough to isolate the two enantiomers at room temperature. This is "
                  "*atropisomerism* — chirality from restricted rotation about a single bond."),
            ("table", ["Ortho substitution", "Barrier", "Isolable at 25 °C?"], [
                ["none (biphenyl)", "≈ 8 kJ mol^−1^", "no"],
                ["2,2′-dimethyl", "≈ 80 kJ mol^−1^", "borderline"],
                ["2,2′-di-tert-butyl", "≈ 150 kJ mol^−1^", "yes"],
                ["2,2′,6,6′-tetramethyl", "≈ 150 kJ mol^−1^", "yes"],
            ], [36, 24, 40], "Table 6.5 — atropisomerism needs bulk, not just a substituent."),
            ("p", "The classic example is 2,2′,6,6′-tetramethylbiphenyl-3,3′-dicarboxylic acid (the “Mills–Nixon” molecule, whose two "
                  "enantiomers were resolved in 1933 — the first proof that restricted rotation alone can generate chirality). It sits in "
                  "the same chapter because the argument is the same one used for allenes: a locked axis, two unsymmetrical ends, no plane."),
            ("warn", "Ortho substituents alone are not enough: if each ring is symmetrically substituted (for example 2,2′,6,6′-tetramethylbiphenyl with identical groups at 3 and 5), a plane exists and the compound is achiral. Both conditions are needed."),
        ],
    },
    # ------------------------------------------------------------------ X-03
    {
        "id": "X-03",
        "title": "Ring stereochemistry: junctions, trans-cycloalkenes, steroids",
        "blocks": [
            ("h2", "6.12  Trans-cycloalkenes"),
            ("p", "A trans double bond inside a ring forces the two allylic carbons onto opposite faces. For rings of seven or fewer atoms "
                  "this is impossible without absurd strain; cyclooctene is the first that can twist enough. The strain energy of "
                  "trans-cyclooctene is about 50 kJ mol^−1^ above the cis isomer, and the trans form is chiral because the twist removes "
                  "every mirror plane."),
            ("table", ["Ring", "cis", "trans", "Note"], [
                ["cyclopropene", "only", "no", "trans would need a 60° twist"],
                ["cyclobutene", "only", "no", "highly strained"],
                ["cyclopentene", "only", "no", "half-chair, cis only"],
                ["cyclohexene", "only", "no", "half-chair, cis only"],
                ["cycloheptene", "only", "no", "trans is calculable but not isolable"],
                ["cyclooctene", "yes", "yes", "trans is chiral and isolable"],
            ], [22, 26, 24, 28], "Table 6.7 — the ring size decides whether the trans alkene exists."),
            ("h2", "6.13  Fused ring junctions"),
            ("p", "In a fused bicyclic system each junction carbon carries one hydrogen. Cis means both hydrogens on the same face; trans "
                  "means opposite faces. For decalin both are possible: cis-decalin is flexible and less stable, trans-decalin is rigid and "
                  "more stable. But here achiral — cis has a plane (on one ring conformation) and trans a centre."),
            ("p", "In the steroids the same junction appears at C5/C10 and at C8/C9. The C5, C8, C9 and C14 series differ only in configuration "
                  "at C5, which is a ring junction; the two series have different shapes, different biological activities, and are "
                  "diastereomers. This is the most important real-world consequence of ring-junction stereochemistry."),
            ("h2", "6.14  Counting with coupled centres"),
            ("p", "In a rigid bicyclic system the two bridgehead carbons cannot invert independently. Flipping one would require breaking the "
                  "bridge, so the pair behaves as **one** stereocentre when you apply 2^n^."),
            ("num", [
                "Count each coupled bridgehead pair as **one** centre.",
                "If the bridgeheads are equivalent by symmetry, the molecule has fewer stereoisomers than the naive count; if they are not, the cis and trans are diastereomers.",
                "Do not push the shortcut into a rigid cage. For 2,5-disubstituted bicyclo[2.2.1]heptane the two bridgeheads are coupled, but the C2 and C5 substituents can only point along the two available directions, so some of the 2^n^ drawings close on themselves. Draw the cage, mark each substituent up or down, and discard drawings that superimpose — never quote a number from n alone.",
            ]),
            ("key", "The “bridgeheads count as one” shortcut applies to coupled centres only. In a flexible ring such as cyclohexane the two substituted carbons are independent, and each contributes its own factor."),
            ("h2", "6.15  Medium rings"),
            ("p", "Cyclooctane adopts the boat–chair (crown) conformation; cyclononane has several low-energy conformers; cyclodecane is the "
                  "smallest ring with a stable transannular interaction. These are not in the JEE syllabus, but they explain why the "
                  "odd/even rule for trans-alkenes changes at eight: the ring has to be large enough that a trans arrangement is not "
                  "prohibitively strained."),
        ],
    },
    # ------------------------------------------------------------------ X-04
    {
        "id": "X-04",
        "title": "Conformational analysis quantitatively",
        "blocks": [
            ("h2", "6.16  From energies to populations"),
            ("p", "The Boltzmann distribution converts an energy difference into a population ratio: N~i~/N~j~ = exp(−ΔE/RT). At 298 K, "
                  "RT = 2.48 kJ mol^−1^, so each 5.7 kJ mol^−1^ of energy costs a factor of 10 in population. This is the single most "
                  "useful numerical fact in conformational analysis."),
            ("h2", "6.17  A-values"),
            ("p", "The A-value of a substituent is the free-energy cost of putting it axial in cyclohexane, measured from the equilibrium "
                  "ratio of the two chairs. It is the quantitative version of the 1,3-diaxial argument."),
            ("table", ["Substituent", "A-value / kJ mol^−1^", "≈ % equatorial at 25 °C"], [
                ["H", "0", "50"],
                ["F", "1.0", "60"],
                ["CH~3~", "7.3", "95"],
                ["CH~2~CH~3~", "7.5", "95"],
                ["CH(CH~3~)~2~", "9.0", "97"],
                ["C(CH~3~)~3~", "20", ">99.9"],
                ["OH", "4.0", "84"],
                ["OCH~3~", "2.5", "73"],
            ], [24, 30, 46], "Table 6.8 — A-values; use them to compare two chairs, not to predict a third decimal place."),
            ("p", "Note that the A-value of OH is much smaller than that of CH~3~, even though OH is heavier. The controlling factor is not "
                  "mass but the length and shape of the bond: a C–O bond is shorter than a C–C bond, so an axial OH reaches less far into "
                  "the 1,3-diaxial hydrogens."),
            ("h2", "6.18  1,3-diaxial interactions"),
            ("p", "An axial substituent on C1 points towards the axial hydrogens on C3 and C5. Each such H···X interaction costs roughly "
                  "3.5–4 kJ mol^−1^ for a methyl group, and there are two of them, which is where the ≈ 7.3 kJ mol^−1^ A-value comes from. "
                  "A 1,3-diaxial methyl–methyl interaction (two methyls both axial on C1 and C3) is much larger, which is why "
                  "1,3-dimethylcyclohexane strongly prefers the e,e chair."),
            ("key", "Two 1,3-diaxial interactions ≈ one A-value. That is why the A-value is roughly twice a single H···CH~3~ interaction, and why 1,3-diaxial methyl–methyl contacts dominate the conformational analysis of substituted cyclohexanes."),
            ("h2", "6.19  The anomeric effect"),
            ("p", "In a pyranose ring an electronegative substituent at C1 (the anomeric carbon) often prefers the **axial** position, contrary "
                  "to the steric prediction. The reason is stereoelectronic: an axial C–X σ* orbital accepts electron density from a lone "
                  "pair on the ring oxygen (the n → σ* interaction), and that overlap is only possible when X is axial. The effect is worth "
                  "about 4–8 kJ mol^−1^ in water and larger in non-polar solvents."),
            ("p", "This is the first genuinely stereoelectronic effect in the chapter, and it is worth understanding rather than memorising: "
                  "the same n → σ* requirement explains why glycosidic bonds are hydrolysed by an axial-assistance mechanism, and why "
                  "α-glucose is more stable than the steric argument would predict."),
            ("warn", "The anomeric effect is not a JEE Main topic. In a JEE Advanced answer, one sentence — “the axial C–X bond allows n → σ* donation from the ring oxygen” — is enough; do not build an answer around it unless the question mentions anomers."),
        ],
    },
    # ------------------------------------------------------------------ X-05
    {
        "id": "X-05",
        "title": "Cyclohexane dynamics and fused systems",
        "blocks": [
            ("h2", "6.20  The ring-flip path"),
            ("p", "The chair-to-chair interconversion does not pass through the boat. The path is chair → half-chair (transition state, "
                  "≈ 45 kJ mol^−1^) → twist-boat (shallow minimum, ≈ 23 kJ mol^−1^) → half-chair → chair. The twist-boat is a genuine "
                  "intermediate on the path, which is why cooling a cyclohexane sample can, in principle, trap it."),
            ("bul", [
                "Chair: all bonds staggered, no strain — the global minimum.",
                "Twist-boat: one eclipsing interaction removed relative to the boat; ≈ 23 kJ mol^−1^ above the chair.",
                "Boat: two flagpole hydrogens; ≈ 29 kJ mol^−1^ above the chair; not a minimum on the true path.",
                "Half-chair: the highest point, ≈ 45 kJ mol^−1^; the C–C–C angles are strained.",
            ]),
            ("h2", "6.21  Fused rings cannot flip"),
            ("p", "A fused bicyclic system such as decalin cannot undergo a chair flip without breaking a bond, because the shared bond locks "
                  "both rings. The consequence is that substituents on a fused system have fixed axial/equatorial assignments, and cis/trans "
                  "ring junctions are configurationally stable. This is why steroids have a fixed shape and why their stereochemistry is "
                  "described by the junction configuration rather than by a conformational average."),
            ("h2", "6.22  Bridgehead double bonds (Bredt's rule)"),
            ("p", "A double bond at a bridgehead of a small bicyclic system would require the bridgehead to be planar, which the cage cannot "
                  "accommodate. Bredt's rule therefore says that bridgehead double bonds are stable only in large rings (roughly, when the "
                  "bridge contains at least eight atoms). Norbornene cannot have a bridgehead double bond; the corresponding alkene is "
                  "isolable only in much larger bicyclic systems."),
            ("table", ["System", "Bridgehead C=C?", "Why"], [
                ["bicyclo[2.2.1]heptane", "no", "bridgehead cannot be planar"],
                ["bicyclo[2.2.2]octane", "no", "same"],
                ["bicyclo[4.4.0]decane (decalin)", "yes, at the junction", "the ring is large enough"],
                ["bicyclo[3.3.1]nonane", "no", "still too rigid"],
            ], [34, 22, 44], "Table 6.9 — Bredt's rule is about the size of the cage, not about the ring count."),
            ("key", "Bredt's rule: no double bond at a bridgehead unless the bridge is long enough to let the bridgehead be planar. It is a strain argument, not a rule about atoms."),
            ("warn", "Bredt's rule is often quoted as “no double bond at a bridgehead”. The exceptions in large rings are real, and JEE Advanced has asked about them; state the rule as a rule of thumb about strain, not as a prohibition."),
        ],
    },
    # ------------------------------------------------------------------ X-06
    {
        "id": "X-06",
        "title": "Stereospecific, stereoselective, and reaction design",
        "blocks": [
            ("h2", "6.23  Two words examiners test"),
            ("p", "A reaction is **stereospecific** if a defined stereoisomer of the starting material gives a defined stereoisomer of the "
                  "product — the stereochemistry is fixed by the mechanism, for every molecule. S~N~2 is stereospecific: (R) gives (S) and "
                  "nothing else."),
            ("p", "A reaction is **stereoselective** if one stereoisomer is formed preferentially from a substrate that could give several — "
                  "the stereochemistry is a matter of preference, not of mechanism. Hydrogenation of an alkene bearing a nearby "
                  "stereocentre is stereoselective: one diastereomer dominates, but both may be formed."),
            ("table", ["Reaction", "Stereospecific?", "Stereoselective?", "Why"], [
                ["S~N~2", "yes", "—", "backside attack fixes the product"],
                ["E2", "yes", "yes (Zaitsev)", "anti-periplanar geometry + alkene stability"],
                ["Br~2~ addition", "yes", "—", "anti addition through the bromonium ion"],
                ["hydrogenation of a substituted alkene", "no", "yes", "the catalyst face is favoured by sterics"],
                ["nucleophilic addition to a chiral aldehyde", "no", "yes", "Cram / Felkin–Anh"],
            ], [30, 16, 16, 38], "Table 6.10 — the distinction is mechanism versus preference."),
            ("key", "Stereospecific: every molecule reacts the same way for a geometric reason. Stereoselective: one outcome dominates for an energetic reason. A reaction can be both, but never one without a reason."),
            ("h2", "6.24  Applying the Cram rule"),
            ("p", "When a nucleophile adds to a carbonyl adjacent to a stereocentre, the Cram rule predicts attack on the less hindered face in "
                  "the conformation in which the largest group on the stereocentre is eclipsed with the carbonyl oxygen. The Felkin–Anh "
                  "model refines this with the “large, medium, small” arrangement and is the version used for predicting the major "
                  "diastereomer in modern answers."),
            ("num", [
                "Draw the carbonyl with the adjacent stereocentre.",
                "Rank the three groups on the stereocentre as large, medium and small.",
                "Put the large group perpendicular to the carbonyl plane, with the medium group on the other side.",
                "The nucleophile attacks the face opposite the large group — the Bürgi–Dunitz angle is about 107°.",
            ]),
            ("p", "The Felkin–Anh product is the major diastereomer when the stereocentre's groups differ strongly in size; the Cram product "
                  "often coincides with it for simple alkyl substituents. Both are *models* — the exam asks you to apply the rule stated "
                  "in the question, not to decide which model is correct."),
            ("h2", "6.25  Stereochemistry of addition to cis/trans alkenes"),
            ("p", "This is the table from Part I, restated as a reaction-design principle. For a **cis** alkene, syn addition gives the meso "
                  "compound and anti addition the racemic pair. For a **trans** alkene it is reversed. So choosing a reagent is choosing a "
                  "stereochemical outcome: OsO~4~ (syn) and Br~2~ (anti) are not interchangeable if you care about the product's symmetry."),
            ("table", ["Target", "Alkene", "Reagent", "Outcome"], [
                ["meso diol", "cis", "OsO~4~ / H~2~O~2~ (syn)", "one compound"],
                ["racemic diol", "trans", "OsO~4~ / H~2~O~2~ (syn)", "a pair"],
                ["meso dibromide", "trans", "Br~2~ (anti)", "one compound"],
                ["racemic dibromide", "cis", "Br~2~ (anti)", "a pair"],
            ], [24, 14, 32, 30], "Table 6.11 — pick the reagent that gives the symmetry you want."),
            ("warn", "Do not call a reaction “stereospecific” merely because one product predominates. Stereospecificity is a yes/no statement about mechanism; the word for preference is stereoselective."),
        ],
    },
]
