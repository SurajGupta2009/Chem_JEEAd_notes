# -*- coding: utf-8 -*-
"""Part I, sheets J-18 … J-24."""

SHEETS = [
    # ------------------------------------------------------------------ J-18
    {
        "id": "J-18",
        "title": "Chirality without a chiral carbon",
        "blocks": [
            ("p", "Every counterexample to “chiral means a chiral carbon” is built the same way: a **locked axis or plane**, "
                  "two unsymmetrical ends, and no internal mirror plane. Once you have seen the pattern, the compounds stop "
                  "looking exceptional."),
            ("h2", "3.35  Allenes"),
            ("p", "An allene C=C=C has two perpendicular end planes. If one end carries a, b (a ≠ b) and the other carries x, y "
                  "(x ≠ y), the molecule has no plane and no centre, and the two arrangements are non-superimposable mirror "
                  "images. The chirality belongs to the **axis**, not to any atom. The descriptors used for such compounds are "
                  "a/d or the axial R/S convention; JEE asks only that you recognise chirality and count the two enantiomers."),
            ("key", "Allene rule: both ends unsymmetrical → chiral (one pair). Either end symmetric → achiral. This is the same odd–even argument as section 2.18, used for the optical chapter."),
            ("h2", "3.36  Spiro compounds"),
            ("p", "A spiro carbon joins two rings in perpendicular planes. If each ring is unsymmetrically substituted (different "
                  "groups on the two sides of the spiro atom), the molecule has axial chirality; if either ring has a plane "
                  "through the spiro atom, the molecule is achiral. The test is therefore per ring, not per molecule."),
            ("p", "The classic exam case is spiro[3.3]heptane with two different substituents on each ring — substituted "
                  "cyclobutanes — which exists as a pair of enantiomers. The spiro carbon itself is not a stereocentre: it carries "
                  "two identical ring paths on each side only if the rings are symmetric, but even when they are not, the "
                  "chirality is axial, not central."),
            ("h2", "3.37  Substituted biphenyls"),
            ("p", "Two benzene rings joined by a single bond can rotate about it. Bulky substituents in the ortho positions prevent "
                  "that rotation, and the rings lock at an angle to each other. With four different ortho substituents the two "
                  "locked arrangements are non-superimposable mirror images — **atropisomers** (axial chirality from restricted "
                  "rotation)."),
            ("p", "The barrier for 2,2′-disubstituted biphenyls is typically 80–160 kJ mol^−1^, enough to isolate the enantiomers at "
                  "room temperature. Key exam examples: 6,6′-dinitro-2,2′-diphenic acid and 2,2′,6,6′-tetramethylbiphenyl-3,3′-"
                  "dicarboxylic acid (Mills–Nixon). If all four ortho positions carry the same group, the molecule has a plane and "
                  "is achiral."),
            ("table", ["Structure", "Chiral?", "Reason"], [
                ["biphenyl", "no", "free rotation; planar average"],
                ["2,2′-dimethylbiphenyl", "no", "two identical halves → plane"],
                ["2,2′-dimethyl-6,6′-dinitrobiphenyl", "yes", "four different ortho groups; rotation locked"],
                ["2,2′,6,6′-tetramethylbiphenyl", "no", "symmetrical; plane perpendicular to the axis"],
                ["1,1′-binaphthyl-2,2′-diol (BINOL)", "yes", "two naphthyl halves, no mirror plane"],
            ], [40, 12, 48], "Table 3.10 — the substituent pattern decides, not the ring size."),
            ("h2", "3.38  Helicenes and propellers"),
            ("p", "A helicene is a chain of ortho-fused benzene rings that cannot lie flat; it coils like a spring, and the two coils "
                  "are non-superimposable mirror images. Propeller-shaped molecules (three or four rings twisted the same way about "
                  "a central bond) are chiral for the same reason. Both are chiral because the *whole shape* is handed, not "
                  "because of any one atom."),
            ("h2", "3.39  Metal complexes"),
            ("p", "An octahedral complex with three bidentate ligands, [M(en)~3~]^n+^, is chiral: the three chelate rings can wind "
                  "clockwise or anticlockwise, giving the **Λ** and **Δ** enantiomers. The metal carries no “four different "
                  "groups” in the organic sense. This is the inorganic face of the same idea and is examined in coordination "
                  "chemistry."),
            ("note", "Chirality is a property of the **arrangement**, not of an atom. Any statement that “chiral molecules must contain a chiral carbon” is wrong, and the standard counterexamples are allene, the ortho-substituted biphenyl and the Λ/Δ complex."),
        ],
    },
    # ------------------------------------------------------------------ J-19
    {
        "id": "J-19",
        "title": "Counting optical isomers and total stereoisomers",
        "blocks": [
            ("h2", "3.40  The counting table"),
            ("p", "Let n be the number of **independent** stereocentres. If the two ends of the molecule are constitutionally "
                  "different, no meso form is possible. If the ends are the same, half of the 2^n^ strings are the same molecule "
                  "written from the other end, and the palindromic ones are meso."),
            ("table", ["Case", "Optically active", "Meso (inactive)", "Total stereoisomers"], [
                ["different ends (any n)", "2^n^", "0", "2^n^"],
                ["similar ends, n even", "2^(n−1)^", "2^(n/2 − 1)^", "2^(n−1)^ + 2^(n/2 − 1)^"],
                ["similar ends, n odd", "2^(n−1)^ − 2^((n−1)/2)^", "2^((n−1)/2)^", "2^(n−1)^"],
            ], [26, 26, 22, 26], "Table 3.12 — the counting table. Burnside's lemma (sheet X-07) gives the same numbers: N = (2^n^ + 2^ceil(n/2)^)/2."),
            ("p", "The table is easier to remember if you think of the **total** first. With similar ends the total is "
                  "2^(n−1)^ + 2^(n/2−1)^ for even n and 2^(n−1)^ for odd n; the meso members are the palindromic strings, and the "
                  "rest come in enantiomeric pairs. Check with tartaric acid, n = 2: total 2 + 1 = 3 — the active pair (R,R)/(S,S) "
                  "and one meso (R,S)."),
            ("table", ["n", "Ends", "Active", "Meso", "Total", "Example"], [
                ["1", "—", "2", "0", "2", "lactic acid"],
                ["2", "different", "4", "0", "4", "2-chloro-3-bromobutane"],
                ["2", "similar", "2", "1", "3", "tartaric acid"],
                ["3", "different", "8", "0", "8", "2,3,4-trihydroxypentanedioic acid"],
                ["3", "similar", "2", "2", "4", "trihydroxyglutaric acid"],
                ["4", "similar", "8", "2", "10", "four-centre symmetric diol"],
            ], [8, 16, 14, 12, 12, 38], "Table 3.13 — values to check your formula against."),
            ("h2", "3.41  Worked example: trihydroxyglutaric acid"),
            ("p", "HOOC–CH(OH)–CH(OH)–CH(OH)–COOH has three stereocentres and similar ends. n = 3 odd: active = 2^2^ − 2^1^ = 2, "
                  "meso = 2^1^ = 2, total = 4. The single active pair is (R,R,R)/(S,S,S). The two meso forms both have an (R) end and "
                  "an (S) end with a middle carbon that is **pseudoasymmetric** — its two halves are (R) and (S), which count as "
                  "different groups — so (R,r,S) and (R,s,S) are diastereomers and are counted separately. That is why the meso column "
                  "reads 2 and not 1, and it is the one place where the odd-n row differs from the even-n row in kind, not just in "
                  "arithmetic."),
            ("p", "Note the contrast with geometrical isomerism of a symmetric triene: octa-2,4,6-triene has 2^(3−1)^ + 2^((3−1)/2)^ = 6 "
                  "geometrical isomers, while a three-centre chain with pseudoasymmetry has 4 optical isomers. The two counts use different "
                  "equivalence rules because a cis/trans descriptor is a two-state label on a *bond*, whereas R/S is tied to an atom whose "
                  "neighbours may themselves be chiral. Do not mix the two formulas."),
            ("h2", "3.42  A four-centre symmetric chain"),
            ("p", "HOOC–CH(OH)–CH(OH)–CH(OH)–CH(OH)–COOH has n = 4 and similar ends. Active = 2^3^ = 8, meso = 2^1^ = 2, total = 10. "
                  "Which strings are meso? A compound is achiral only if its mirror image can be written as the same molecule from "
                  "the other end, that is if s = invert(reverse(s)). For n = 4 that forces each half to be the mirror of the other: "
                  "(R,S,R,S) ≡ (S,R,S,R) is one meso compound and (R,R,S,S) ≡ (S,S,R,R) is the other, each with a plane through the "
                  "middle of the chain. Every remaining string is paired with a non-identical mirror image, which is where the 8 "
                  "active forms come from."),
            ("key", "Two routes must agree. Closed formulas (the table) and orbit counting (Burnside) give the same number for every n. If they disagree, your n is wrong or the ends are not really similar."),
            ("h2", "3.43  Combined geometrical and optical counting"),
            ("num", [
                "Count the geometrical isomers first, treating each as a separate skeleton.",
                "For each geometrical isomer, count its stereocentres and apply the table.",
                "Add up. Some geometrical isomers may be meso (a cis ring with a plane) and contribute no active forms.",
            ]),
            ("p", "**Worked: 2,4-hexadien-1-ol type chain.** Two C=C centres give three geometrical isomers (similar ends). Each has "
                  "no stereocentre, so the total is 3 stereoisomers, all achiral. **Worked: 2,4-dichlorohexa-2,4-diene.** Two C=C "
                  "and two stereocentres, with each C=C giving a geometrical choice — the enumeration is skeleton by skeleton, not "
                  "a single formula."),
            ("warn", "The formulas count **stereocentres**, not geometrical centres. A molecule with a C=C and two stereocentres has 3 geometrical isomers and, for each, up to four optical possibilities; do not multiply n's."),
            ("key", "Never multiply “geometrical × optical” blindly. Enumerate the skeletons first, then test each for symmetry; the formulas are shortcuts for symmetric chains, not a substitute for drawing."),
        ],
    },
    # ------------------------------------------------------------------ J-20
    {
        "id": "J-20",
        "title": "Relation questions: identical, enantiomer, diastereomer",
        "blocks": [
            ("p", "A large family of objective questions gives two or four drawings and asks for their relationship. There is one "
                  "reliable procedure."),
            ("h2", "3.44  The four-step procedure"),
            ("num", [
                "**Molecular formula and connectivity.** If they differ, the compounds are structural isomers or unrelated — stop.",
                "**Convert both to the same projection** (Fischer is usually fastest for chains, Newman for conformations).",
                "**Try the allowed operations** on one structure: 180° rotation of the whole Fischer, two swaps at a centre, rotation about a single bond. If it becomes the other, they are **identical**.",
                "**Compare centre by centre.** If every centre is inverted and the drawings are mirror images, they are **enantiomers**. If some centres match and some are inverted, they are **diastereomers**.",
            ]),
            ("table", ["Observation after normalising", "Relationship"], [
                ["superimposable by rotation / even swaps", "identical (same compound)"],
                ["mirror images, no rotation superimposes them", "enantiomers"],
                ["some centres same, some inverted", "diastereomers"],
                ["same configuration, different rotation about a single bond", "conformers (identical compound)"],
                ["different connectivity", "structural isomers"],
            ], [52, 48], "Table 3.15 — the decision table for relation questions."),
            ("h2", "3.45  Worked comparisons"),
            ("p", "**(a) Two Fischer projections that differ by a 180° rotation.** They are the same molecule. A 180° rotation in the "
                  "plane is allowed and changes nothing; a 90° rotation would give the enantiomer."),
            ("p", "**(b) Two Fischer projections with one centre swapped.** Diastereomers. Swapping two groups at a single centre "
                  "inverts that centre only, which is the definition of a diastereomeric change."),
            ("p", "**(c) (R)-lactic acid and (S)-lactic acid.** Enantiomers: one centre, every descriptor inverted, mirror images."),
            ("p", "**(d) (2R,3R)- and (2R,3S)-tartaric acid.** Diastereomers: one centre the same, one inverted. The second is the "
                  "meso form, so the pair is also “active versus inactive”, which is worth saying in a descriptive answer."),
            ("p", "**(e) A wedge–dash drawing and its mirror image, both rotated.** Rotate one in the plane and compare; if the "
                  "wedges now coincide, they are identical. This is where most candidates lose a mark by assuming every mirror "
                  "image is an enantiomer."),
            ("h2", "3.46  A fast symmetry check"),
            ("p", "Before doing any R/S assignment, look for a horizontal mirror line in the Fischer projection. If the top half is "
                  "the mirror of the bottom half, the molecule is meso and its mirror image is itself — which immediately answers "
                  "“identical or enantiomer?” without any assignment. Use this as a five-second filter, then confirm with R/S."),
            ("warn", "“Not superimposable” is not the same as “enantiomers”. Two diastereomers are also non-superimposable. The definition of enantiomers needs both facts: mirror images **and** non-superimposable."),
            ("key", "In a relation question, always state the evidence: “same formula, same connectivity, all centres inverted, mirror images → enantiomers”. The reason earns the mark; the label alone may not."),
        ],
    },
    # ------------------------------------------------------------------ J-21
    {
        "id": "J-21",
        "title": "Configuration and conformation; barriers to rotation",
        "blocks": [
            ("p", "Configuration is the arrangement that can be changed only by breaking bonds. Conformation is the arrangement "
                  "that changes by rotating about single bonds. Everything in sections 4 and 5 depends on keeping those two "
                  "words apart."),
            ("h2", "4.1  Why rotation has a barrier"),
            ("p", "Even a single bond resists rotation a little. When two bonds on adjacent carbons line up, their electron pairs "
                  "repel — **torsional strain** — and the energy rises. The barrier is the height of that rise. Ethane's barrier "
                  "is about 12.5 kJ mol^−1^ (textbook value; modern measurements give ≈ 12.1); butane's highest barrier, the "
                  "methyl–methyl eclipse, is about 19–25 kJ mol^−1^."),
            ("table", ["Bond", "Barrier ≈", "Consequence at 25 °C"], [
                ["C–C in ethane", "12.5 kJ mol^−1^", "free rotation; conformers not isolable"],
                ["C–C in butane", "19–25 kJ mol^−1^", "free rotation; anti favoured"],
                ["C–N in amides", "≈ 75 kJ mol^−1^", "slow rotation; cis/trans amides separable"],
                ["C=C π bond", "250–270 kJ mol^−1^", "no rotation; geometrical isomers isolable"],
                ["biphenyl, 2,2′-disubstituted", "80–160 kJ mol^−1^", "atropisomers isolable"],
            ], [34, 22, 44], "Table 4.1 — the barrier decides whether an arrangement is a conformer or a configuration."),
            ("key", "A conformer becomes a configuration when its barrier is high enough to isolate it at room temperature (roughly above 80 kJ mol^−1^). The same geometric idea — a locked arrangement — can therefore be conformational in one molecule and configurational in another."),
            ("h2", "4.2  What raises the barrier"),
            ("bul", [
                "**Partial double-bond character**: amides, esters, enamines, and the C–N bond of a thioamide.",
                "**Steric bulk on both sides**: ortho-substituted biphenyls, tri-tert-butylmethane.",
                "**Ring constraints**: a bond inside a small ring cannot rotate without breaking the ring.",
            ]),
            ("h2", "4.3  Representing conformations"),
            ("p", "Three representations are used, and each has a rule that must be respected. In a **Newman** projection you look "
                  "down the bond: front carbon as a point, back carbon as a circle. In a **sawhorse** drawing you look from the "
                  "side: both carbons visible, bonds drawn at an angle. In a **wedge–dash** drawing the chain is in the plane and "
                  "the substituents are above/below it."),
            ("p", "In a Newman projection, the dihedral angle θ is the angle between a chosen front substituent and a chosen back "
                  "substituent, measured looking down the bond. θ = 0° is eclipsed, θ = 60° is staggered. The energy profile is a "
                  "periodic function of θ with three maxima and three minima per 360° for ethane."),
            ("note", "When you convert a sawhorse to a Newman, keep the same viewing direction. Rotating the whole molecule in space is allowed; rotating only the back carbon changes the conformation you are describing."),
        ],
    },
    # ------------------------------------------------------------------ J-22
    {
        "id": "J-22",
        "title": "Ethane and butane: the energy profile",
        "blocks": [
            ("h2", "4.4  Ethane"),
            ("p", "Eclipsed ethane has three H–H eclipses and is about 12.5 kJ mol^−1^ above staggered. Staggered ethane has three "
                  "equivalent conformations related by 120° rotation and is the minimum. The barrier is small because the only "
                  "interaction is between C–H σ bonds; there is no steric bulk."),
            ("fig", "newman", "Fig. 4.1 — staggered and eclipsed ethane in Newman projection. In the eclipsed form each rear C–H hides behind a front C–H; that is the source of torsional strain.", 0.24),
            ("h2", "4.5  Butane"),
            ("p", "Rotation about C2–C3 in butane has three distinct staggered conformers: **anti** (θ = 180°, methyls opposite) and "
                  "two **gauche** forms (θ = 60° and 300°, methyls 60° apart). Anti is the global minimum; each gauche is about "
                  "3.8 kJ mol^−1^ higher because of the methyl–methyl steric interaction. The maxima are the eclipsed forms, with the "
                  "CH~3~/CH~3~ eclipse highest."),
            ("fig", "butane", "Fig. 4.2 — the potential energy of butane as the C2–C3 bond rotates. Minima at 60° (gauche), 180° (anti) and 300° (gauche); maxima at 0° (syn) and 120°/240° (CH~3~/H eclipses).", 0.28),
            ("table", ["Conformer (θ)", "Relative energy", "Why"], [
                ["anti (180°)", "0", "methyls farthest apart"],
                ["gauche (60°, 300°)", "≈ 3.8 kJ mol^−1^", "one CH~3~/CH~3~ gauche interaction"],
                ["H/CH~3~ eclipsed (120°, 240°)", "≈ 16 kJ mol^−1^", "one methyl eclipse + torsional strain"],
                ["CH~3~/CH~3~ eclipsed (0°)", "≈ 19–25 kJ mol^−1^", "methyl eclipse + full torsional strain"],
            ], [32, 24, 44], "Table 4.2 — butane's energy ladder. Populations follow Boltzmann (sheet X-04)."),
            ("p", "At room temperature the anti form is favoured but not exclusively populated: with ΔE ≈ 3.8 kJ mol^−1^, the "
                  "Boltzmann ratio anti : gauche ≈ 4.6 : 1 per gauche form, so about 70 % anti and 30 % gauche in total. The "
                  "rotation is fast, so the NMR spectrum shows one averaged methyl signal, not separate signals for each conformer."),
            ("h2", "4.6  Are conformers ever chiral?"),
            ("p", "Yes — and this is a favourite JEE Advanced point. The gauche conformer of butane has no plane and no centre, so it "
                  "is chiral; the two gauche forms are enantiomers. But they interconvert rapidly by rotation through the anti form, "
                  "so butane itself is achiral (a conformational average) and cannot be resolved. The molecule is achiral; the "
                  "conformer is chiral. The lesson: chirality can be a property of a conformation, but optical activity requires the "
                  "chiral species to be long-lived."),
            ("key", "A molecule is achiral if it has a conformation with a plane — even if other conformations are chiral — because the interconversion is fast. Optical activity needs a *configurational* lock, not a conformational one."),
            ("h2", "4.7  Barrier data worth remembering"),
            ("table", ["Quantity", "Value", "Use"], [
                ["ethane barrier", "≈ 12.5 kJ mol^−1^", "benchmark for torsional strain"],
                ["butane anti → gauche", "≈ 3.8 kJ mol^−1^", "benchmark for a gauche CH~3~/CH~3~ interaction"],
                ["cyclohexane chair → twist-boat", "≈ 23 kJ mol^−1^", "chair is strongly favoured"],
                ["cyclohexane chair → boat", "≈ 29 kJ mol^−1^", "boat is not a minimum"],
                ["methylcyclohexane axial → equatorial", "≈ 7.3 kJ mol^−1^", "A-value of CH~3~"],
                ["cyclohexane ring flip", "≈ 45 kJ mol^−1^", "fast at room temperature"],
            ], [40, 24, 36], "Table 4.3 — values to order, not to measure."),
        ],
    },
    # ------------------------------------------------------------------ J-23
    {
        "id": "J-23",
        "title": "Cycloalkanes and the cyclohexane chair",
        "blocks": [
            ("h2", "4.8  Ring strain"),
            ("p", "A ring is strained when its bond angles depart from 109.5° or when its hydrogens are forced into eclipsed "
                  "arrangements. Cyclopropane has angle strain (60° versus 109.5°) and torsional strain (all C–H eclipsed); "
                  "cyclobutane is puckered to relieve some of it; cyclopentane is a floppy envelope; cyclohexane can adopt the "
                  "strain-free chair."),
            ("table", ["Ring", "Strain ≈", "Shape", "Note"], [
                ["3", "115 kJ mol^−1^", "planar triangle", "very high; ring-opening reactions"],
                ["4", "110 kJ mol^−1^", "puckered", "still high"],
                ["5", "26 kJ mol^−1^", "envelope", "small"],
                ["6", "0", "chair", "strain-free"],
                ["7–12", "20–50 kJ mol^−1^", "various", "medium-ring strain"],
            ], [12, 22, 26, 40], "Table 4.5 — the strain ladder; cyclohexane is the special case, not the rule."),
            ("h2", "4.9  The chair"),
            ("p", "The chair has all bond angles at 109.5° and all adjacent C–H bonds staggered, so it has no angle or torsional "
                  "strain. Each carbon carries one **axial** bond (vertical, parallel to the C3 axis) and one **equatorial** bond "
                  "(roughly in the ring plane, pointing outwards). Axial bonds alternate up/down around the ring; equatorial bonds "
                  "do too, in the opposite sense."),
            ("fig", "ringae", "Fig. 4.3 — axial and equatorial bonds on a cyclohexane chair. At each carbon one bond is vertical (axial) and one is roughly radial (equatorial); the up/down sense alternates round the ring.", 0.32),
            ("h2", "4.10  Ring flipping"),
            ("p", "A chair flips to the other chair by passing through a half-chair and a twist-boat. In the flip, every axial bond "
                  "becomes equatorial and every equatorial becomes axial, but the **up/down sense is preserved**: an “up” "
                  "substituent stays up. The barrier is about 45 kJ mol^−1^, so the flip is fast at room temperature (about 10^5^ "
                  "s^−1^) and the two chairs are conformers, not isomers."),
            ("key", "Flip: a ⇄ e, e ⇄ a, up stays up, down stays down. This one sentence answers most ring-flip questions, including why a 1,2-disubstituted cyclohexane has the same cis/trans label in both chairs."),
            ("h2", "4.11  Worked chair problems"),
            ("p", "**(a) Which chair of methylcyclohexane is more stable?** The one with CH~3~ equatorial. The axial conformer has two "
                  "1,3-diaxial H···CH~3~ interactions, worth about 7.3 kJ mol^−1^ in total, so the equatorial form dominates "
                  "(≈ 95 % at 25 °C)."),
            ("p", "**(b) Is cis-1,2-dimethylcyclohexane chiral?** No. Its more stable chair has one CH~3~ axial and one equatorial, "
                  "and the ring has a plane of symmetry; the molecule is meso. The trans isomer (e,e or a,a) is chiral and exists "
                  "as a pair."),
            ("p", "**(c) Which is more stable, cis- or trans-1,4-dimethylcyclohexane?** Trans, because it can place both methyls "
                  "equatorial (e,e). Cis-1,4 must be a,e."),
            ("h2", "4.12  The boat, the twist-boat and the actual path"),
            ("p", "The boat has two flagpole hydrogens pointing at each other, which costs about 29 kJ mol^−1^ relative to the chair; "
                  "the twist-boat relieves that by twisting, but is still about 23 kJ mol^−1^ above the chair and is not a minimum "
                  "on the true path. The real flip goes chair → half-chair (≈ 45 kJ mol^−1^, the transition state) → twist-boat → "
                  "half-chair → chair."),
            ("note", "The boat is often drawn as if it were an intermediate. It is not on the minimum-energy path; the twist-boat is the shallow minimum between the two chairs, and the half-chair is the barrier."),
            ("h2", "4.13  What NMR sees"),
            ("p", "At room temperature the ring flip is fast on the NMR timescale, so axial and equatorial hydrogens average and a "
                  "monosubstituted cyclohexane shows one set of signals. Cool the sample and the flip slows; the axial and "
                  "equatorial protons then separate, which is the classic variable-temperature NMR experiment for cyclohexane "
                  "conformational analysis."),
        ],
    },
    # ------------------------------------------------------------------ J-24
    {
        "id": "J-24",
        "title": "Substituted cyclohexanes",
        "blocks": [
            ("h2", "4.14  The placement rules"),
            ("num", [
                "Draw the chair and mark each carbon up or down.",
                "Draw both chairs (after a flip) and place the substituent axial in one and equatorial in the other.",
                "Choose the chair with the larger group equatorial.",
                "For two substituents, check whether the required up/down pattern gives a,e or e,e — that decides stability.",
            ]),
            ("table", ["Relationship", "cis", "trans", "More stable"], [
                ["1,2", "a,e (one up, one down on adjacent carbons is trans — see note)", "e,e or a,a", "trans (e,e)"],
                ["1,3", "e,e or a,a", "a,e", "cis (e,e)"],
                ["1,4", "a,e", "e,e or a,a", "trans (e,e)"],
            ], [22, 30, 22, 26], "Table 4.6 — for identical substituents. Check the up/down pattern on a drawing before quoting this table."),
            ("p", "The patterns are easy to remember as a sequence: 1,2-cis is a,e; 1,3-cis is e,e; 1,4-cis is a,e. Trans is the "
                  "opposite in each case. The reason is the alternation of the up/down sense around the ring: going one carbon "
                  "changes the sense, going two carbons keeps it."),
            ("h2", "4.15  Why the pattern alternates"),
            ("p", "Label the carbons C1 to C6. On C1 axial is up and equatorial is down. On C2 axial is down, equatorial up; on C3 "
                  "axial is up, and so on. A cis relationship means both substituents are on the same face (both up or both "
                  "down); a trans relationship means opposite faces. Combine that with the axial/equatorial assignments and the "
                  "table follows without memorisation."),
            ("h2", "4.16  Locked chairs and the tert-butyl group"),
            ("p", "A *tert*-butyl group is so bulky that it is essentially always equatorial; the axial conformer is about "
                  "20 kJ mol^−1^ higher and is not populated. This **locks** the chair: the ring can no longer flip, because the "
                  "flip would put the tert-butyl group axial. Consequences: cis-4-tert-butyl-1-methylcyclohexane has methyl axial "
                  "(it cannot be equatorial in the same chair), and the molecule is effectively frozen in one conformation."),
            ("key", "A tert-butyl group is a conformational lock. If a question asks for the most stable conformation of a molecule containing one, put it equatorial and do not flip."),
            ("h2", "4.17  Stability and heat of combustion"),
            ("p", "The more stable an isomer, the lower its heat of combustion (less energy released on burning to CO~2~ and "
                  "H~2~O). Heats of combustion therefore give an experimental ranking of isomer stability: trans-1,2-dimethyl-"
                  "cyclohexane (e,e) < cis (a,e) < trans (a,a) in energy, which is the same order as their heats of combustion. "
                  "For cis/trans alkenes the same logic applies, but the differences are smaller."),
            ("warn", "The table above assumes identical substituents. With different substituents, “cis” and “trans” do not by themselves decide stability — you must place the larger group equatorial. A cis isomer with the large group equatorial can beat a trans isomer that forces it axial."),
            ("note", "A-values (the energy cost of an axial substituent) are tabulated in sheet X-04: CH~3~ ≈ 7.3, Et ≈ 7.5, i-Pr ≈ 9.0, t-Bu ≈ 20 kJ mol^−1^. They are the quantitative version of the argument on this page."),
        ],
    },
]
