# -*- coding: utf-8 -*-
"""Part I, sheets J-25 … J-29."""

SHEETS = [
    # ------------------------------------------------------------------ J-25
    {
        "id": "J-25",
        "title": "Reaction stereochemistry I: substitution and elimination",
        "blocks": [
            ("p", "Every substitution changes the configuration at the reacting carbon in a way that is fixed by the mechanism. "
                  "Learn the four entries in this sheet and you can answer most reaction-stereochemistry questions without "
                  "memorising a list of reactions."),
            ("h2", "5.1  S~N~2: backside attack, clean inversion"),
            ("fig", "sn2", "Fig. 5.1 — Walden inversion in S~N~2: backside nucleophilic attack via a pentacoordinate transition state.", 0.26),
            ("p", "The nucleophile attacks the carbon from the side opposite the leaving group, through a trigonal-bipyramidal "
                  "transition state, and the leaving group departs from the other side. The result is **inversion of "
                  "configuration** — the Walden inversion. If the starting material is (R), the product is (S) (unless the "
                  "priority order changes, which you must check)."),
            ("eq", ["rate = k[substrate][nucleophile]",
                    "stereochemistry: inversion (100 %)"]),
            ("bul", [
                "Favoured by methyl and primary halides, strong nucleophiles, polar aprotic solvents (DMSO, DMF, acetone).",
                "Retardation by β-branching: neopentyl halides react very slowly.",
                "A chiral secondary halide gives a chiral product with clean inversion; a racemic starting material gives a racemic product.",
            ]),
            ("h2", "5.2  S~N~1: planar carbocation, racemisation"),
            ("p", "The leaving group departs first, giving a planar carbocation; the nucleophile can then attack either face. If the "
                  "two faces are equally accessible, the product is racemic; in practice there is often slight inversion bias "
                  "because the leaving group blocks one face for a moment. The result is **racemisation with partial inversion**, "
                  "never clean retention."),
            ("eq", ["rate = k[substrate]",
                    "stereochemistry: racemisation (with inversion bias)"]),
            ("bul", [
                "Favoured by tertiary halides, weak nucleophiles (water, alcohols), polar protic solvents (water, ethanol).",
                "Allylic and benzylic halides are intermediate: the carbocation is stabilised by resonance.",
                "A carbocation adjacent to a stereocentre can also racemise that centre by hydride or alkyl shifts.",
            ]),
            ("key", "S~N~2 inverts, S~N~1 racemises. The carbon skeleton does not rearrange in S~N~2; it can in S~N~1. If a product has a rearranged skeleton, the mechanism was S~N~1 (or E1)."),
            ("h2", "5.3  Neighbouring-group participation and retention"),
            ("p", "If a nucleophile is already present in the molecule next to the leaving group (a carboxylate, a sulfide, an "
                  "amide nitrogen), it can attack intramolecularly, displacing the leaving group with **inversion** at that step. "
                  "The intermediate is then attacked by the external nucleophile at the same carbon, again with inversion. Two "
                  "inversions give **net retention** of configuration."),
            ("eq", "retention = two inversions (double displacement)"),
            ("h2", "5.4  Elimination"),
            ("p", "E2 is a concerted anti-periplanar elimination: the base removes a β-H while the leaving group departs from the "
                  "opposite side. The requirement is that H and L ~anti~ to each other, which fixes the stereochemistry of the "
                  "alkene: the two groups that were anti in the conformer end up on opposite sides (trans) of the new double bond."),
            ("p", "E1 goes through the same carbocation as S~N~1, so it loses stereochemical information at the reacting carbon and "
                  "gives the more substituted (Zaitsev) alkene. In a rigid ring, E2 needs a trans-diaxial arrangement of H and L; "
                  "if the only β-H is not anti-periplanar, elimination is slow and substitution may dominate."),
            ("table", ["Mechanism", "Stereochemical result", "Stereospecific?", "Example"], [
                ["S~N~2", "inversion", "yes", "primary halide + CN^−^"],
                ["S~N~1", "racemisation", "no", "tertiary halide + H~2~O"],
                ["E2", "anti elimination; alkene geometry set by the conformer", "yes", "2-bromobutane + EtO^−^"],
                ["E1", "Zaitsev alkene, lost stereochemistry at C–X", "no", "tertiary halide + heat"],
                ["neighbouring group", "retention (two inversions)", "yes", "mustard gas hydrolysis"],
            ], [20, 40, 16, 24], "Table 5.1 — the reaction table JEE asks for."),
            ("h2", "5.5  The substitution table JEE asks for"),
            ("table", ["Substrate", "Strong Nu^−^, aprotic", "Weak Nu, protic", "Bulky base, heat"], [
                ["CH~3~X", "S~N~2", "S~N~2 (slow)", "—"],
                ["primary RCH~2~X", "S~N~2", "S~N~2 (slow)", "E2"],
                ["secondary R~2~CHX", "S~N~2 + E2", "S~N~1 + E1", "E2 (Zaitsev)"],
                ["tertiary R~3~CX", "E2", "S~N~1 + E1", "E2 (Zaitsev)"],
                ["allylic / benzylic", "S~N~2", "S~N~1", "E2"],
            ], [26, 26, 24, 24], "Table 5.2 — substrate plus conditions decides the mechanism."),
            ("warn", "“Inversion” is about the position of the nucleophile relative to the leaving group, not about the R/S label. If the incoming group changes the CIP priority order, an inversion can leave the R/S descriptor unchanged. Work the priorities again after the reaction."),
        ],
    },
    # ------------------------------------------------------------------ J-26
    {
        "id": "J-26",
        "title": "Reaction stereochemistry II: addition and hydrogenation",
        "blocks": [
            ("h2", "5.6  Syn and anti addition"),
            ("p", "Addition to a C=C can deliver the two new groups to the same face (**syn**) or opposite faces (**anti**). The "
                  "stereochemistry of the product is fixed by the mechanism, not by the reagent's name:"),
            ("bul", [
                "**Syn**: H~2~/Pd (both H from the same face), hydroboration–oxidation (B and H syn), dihydroxylation with OsO~4~ (both OH syn), hydrogenation of an alkene.",
                "**Anti**: Br~2~ (bromonium ion opened from the back), HBr (via the bromonium/carbocation), epoxidation followed by anti opening in base.",
            ]),
            ("table", ["Alkene", "syn addition gives", "anti addition gives"], [
                ["cis-2-butene", "meso-2,3-butanediol / meso dibromide", "racemic pair"],
                ["trans-2-butene", "racemic pair", "meso compound"],
                ["cyclohexene", "cis-1,2 product", "trans-1,2 product"],
                ["1-methylcyclohexene", "cis (both on one face)", "trans"],
            ], [30, 34, 36], "Table 5.4 — the same reagent can give meso or racemic depending on the alkene geometry. This is the most examined table in the chapter."),
            ("key", "cis alkene + syn addition → meso. cis alkene + anti addition → racemic. trans alkene + syn addition → racemic. trans alkene + anti addition → meso. Reverse the alkene or the addition and you reverse the outcome."),
            ("h2", "5.7  Hydrogenation of an optically active alkene"),
            ("p", "If the alkene already contains a stereocentre, hydrogenation creates a **new** stereocentre and can give two "
                  "diastereomers, in unequal amounts (diastereoselective addition). The existing stereocentre biases which face "
                  "of the alkene is hydrogenated, so the product is not a racemic mixture: it is a mixture of diastereomers, "
                  "and the optical activity is retained because the original centre is untouched."),
            ("p", "If the alkene is the only source of chirality (for example an alkene that is chiral only because of the "
                  "arrangement of its substituents), hydrogenation destroys the chirality and the product is optically inactive. "
                  "This is the sense in which “hydrogenation of an optically active alkene can destroy the activity”."),
            ("h2", "5.8  Addition to a C=C that already has stereocentres"),
            ("p", "When a new centre is created next to an existing one, the two possible products are diastereomers. The facial "
                  "selectivity is decided by steric hindrance from the existing substituents (the “Cram” argument, sheet X-06): "
                  "the reagent approaches the face that is less crowded. In a ring, the approach is usually from the less hindered "
                  "face, which is why substituents direct hydrogenation cis or trans."),
            ("h2", "5.9  Addition to a carbonyl"),
            ("p", "Nucleophilic addition to a carbonyl creates a stereocentre when the two groups on the carbonyl carbon are "
                  "different. With an achiral carbonyl and an achiral nucleophile, the two faces are equivalent, so a racemic "
                  "mixture results. With a chiral carbonyl (one that already contains a stereocentre) the faces are "
                  "diastereotopic, giving diastereomers — the basis of the Cram and Felkin–Anh rules."),
            ("h2", "5.10  A worked addition problem"),
            ("p", "**cis-2-Butene + Br~2~.** Anti addition of Br~2~ gives the (2R,3R)/(2S,3S) pair — a racemic mixture. **trans-2-Butene "
                  "+ Br~2~.** The same anti addition now gives the (2R,3S) meso compound. Check by drawing the bromonium ion on one "
                  "face and opening it from the other: the relative positions of the two Br atoms invert with the alkene geometry."),
            ("warn", "Do not write “addition of Br~2~ gives the trans product”. It gives the anti addition; whether the final molecule is cis or trans, meso or racemic, depends on the alkene. Draw the bromonium ion every time — it is faster than remembering four cases."),
        ],
    },
    # ------------------------------------------------------------------ J-27
    {
        "id": "J-27",
        "title": "Counting every isomer: the full enumeration",
        "blocks": [
            ("h2", "5.11  The checklist"),
            ("num", [
                "Write the molecular formula and compute the degree of unsaturation.",
                "Enumerate the **structural** skeletons first (chains, then rings, then multiple bonds).",
                "For each skeleton, mark every geometrical centre and every stereocentre.",
                "Count the stereoisomers skeleton by skeleton; never add n's across skeletons.",
                "Report structural, geometrical and optical counts separately, then the total.",
            ]),
            ("h2", "5.12  Worked: C~5~H~11~Cl"),
            ("p", "Degree of unsaturation = 0, so the compound is acyclic and saturated (or a ring). Eight structural isomers "
                  "exist; the stereochemistry multiplies some of them."),
            ("table", ["Skeleton", "Structural isomers", "Stereoisomers", "Optically active?"], [
                ["n-pentane chain", "3 (1-, 2-, 3-chloro)", "1 + 2 + 2 = 5", "2-chloro and 3-chloro (each a pair)"],
                ["2-methylbutane", "4 (1-, 2-, 3-, 4-chloro)", "1 + 2 + 1 + 1 = 5", "2-chloro only"],
                ["2,2-dimethylpropane", "1 (1-chloro)", "1", "no"],
                ["cyclopentane", "1", "1", "no"],
                ["methylcyclobutane", "2", "2 + 2", "the 1-chloro-1-methyl isomer is achiral"],
                ["dimethylcyclopropanes", "4", "several", "check each for a plane"],
            ], [26, 26, 26, 24], "Table 5.6 — the enumeration skeleton by skeleton. Add the columns only after each row is justified."),
            ("p", "The exam-safe answer is to draw each skeleton, mark the stereocentres, and state the count for each. A single "
                  "total with no working is the commonest way to lose marks on this question, even when the number is right."),
            ("h2", "5.13  Worked: dichloro derivatives of butane"),
            ("p", "C~4~H~8~Cl~2~ has two structural families: the butane chain and the 2-methylpropane skeleton. On the butane chain "
                  "the chlorines can be 1,1; 1,2; 1,3; 1,4; 2,2; 2,3. Of these, 1,2 and 2,3 create stereocentres, and 2,3 also "
                  "gives a meso form; 1,3 has no stereocentre but can be chiral if the two ends differ (they do not here). On the "
                  "branched skeleton, 1,1; 1,2; 1,3 and 2,2 are possible, with 1,2 giving a stereocentre."),
            ("key", "Enumerate skeletons → place substituents → mark centres → test symmetry. Four steps, in that order, for every counting question. The formula sheet (J-29) is only a check on the result."),
            ("h2", "5.14  Separable fractions"),
            ("p", "A reaction that creates a stereocentre in an achiral environment gives a **racemic mixture**, which is optically "
                  "inactive and separable only by resolution. A reaction that creates a second stereocentre in a molecule that "
                  "already has one gives **diastereomers**, which are separable by ordinary methods. This single distinction "
                  "decides whether the phrase “the product is optically inactive” is a statement about the mechanism (racemic) or "
                  "about the substrate (meso)."),
            ("warn", "A meso product and a racemic product both rotate zero. The question usually tells you which one is being asked about by giving the alkene geometry or the substrate's chirality — read that first."),
        ],
    },
    # ------------------------------------------------------------------ J-28
    {
        "id": "J-28",
        "title": "Twenty traps and how to answer them",
        "blocks": [
            ("p", "These are the twenty statements that turn a correct idea into a wrong answer. Each is written as the trap, "
                  "followed by the correction."),
            ("num", [
                "“Geometrical isomerism needs a C=C.” **No** — a ring, a C=N or an N=N centre also works.",
                "“A molecule with two stereocentres is always chiral.” **No** — it may be meso.",
                "“A molecule with no stereocentre is achiral.” **No** — allenes, biphenyls, helicenes.",
                "“Enantiomers have different boiling points.” **No** — they differ only in the sign of rotation.",
                "“Diastereomers are mirror images.” **No** — that is the definition of enantiomers.",
                "“A racemic mixture is achiral.” **No** — it contains chiral molecules and is optically inactive by external compensation.",
                "“Meso compounds rotate light.” **No** — internal compensation, α = 0.",
                "“cis is always more polar.” Usually, but check the vectors; a cis isomer with cancelling moments can have μ = 0.",
                "“trans always has the higher boiling point.” **Usually not** — the cis isomer is more polar. Maleic/fumaric is the exception for melting point, not a rule for boiling point.",
                "“A 90° rotation of a Fischer projection is allowed.” **No** — it inverts every centre.",
                "“Swapping two groups twice changes the configuration.” **No** — two swaps restore it.",
                "“S~N~1 always gives exactly 50:50.” **No** — racemisation with inversion bias.",
                "“S~N~2 changes the R/S label.” Not necessarily — the priority order can change.",
                "“E2 gives the trans alkene.” It gives the anti-periplanar product; the geometry follows from the conformer.",
                "“Br~2~ addition gives the trans product.” It gives anti addition; meso or racemic depends on the alkene.",
                "“Hydrogenation always destroys optical activity.” Only if the chirality depended on the alkene.",
                "“D and L mean (+) and (−).” **No** — independent labels.",
                "“More stereocentres means more isomers.” Only up to symmetry; meso forms reduce the count.",
                "“A stereocentre must be carbon.” **No** — N, P, S and metal centres can be stereogenic.",
                "“If the mirror image looks the same, the compound is achiral.” Only if it is *superimposable* — “looks the same” after a rotation is exactly the test, but a reflection is not a rotation.",
            ]),
            ("key", "Most of these traps are the same mistake in different clothes: a rule about *one* example is being applied to *every* example. When a question looks familiar, check that the symmetry has not changed."),
        ],
    },
    # ------------------------------------------------------------------ J-29
    {
        "id": "J-29",
        "title": "One-page recall",
        "blocks": [
            ("h2", "Definitions in one line each"),
            ("bul", [
                "**Stereoisomers**: same connectivity, different arrangement in space.",
                "**Enantiomers**: non-superimposable mirror images; identical physical properties, opposite rotation.",
                "**Diastereomers**: stereoisomers that are not mirror images; different physical properties.",
                "**Meso**: achiral despite stereocentres, because of an internal plane or centre.",
                "**Racemic**: 1:1 mixture of enantiomers; inactive by external compensation.",
                "**Chirality**: the molecule is not superimposable on its mirror image.",
                "**Stereocentre**: an atom whose substituents can be interchanged to give a stereoisomer.",
                "**Optical purity / ee**: the fraction of the mixture that is one enantiomer, expressed as a percentage.",
            ]),
            ("h2", "The formulas"),
            ("eq", ["[α] = α / (l × c)     l in dm, c in g mL^−1^",
                    "ee = (observed [α] / [α] of pure enantiomer) × 100 %",
                    "geometrical: 2^n^ (dissimilar ends); (2^n^ + 2^ceil(n/2)^)/2 (similar ends)",
                    "optical: see Table 3.12 (J-19)"]),
            ("h2", "The symmetry test"),
            ("bul", [
                "σ present → achiral. i present → achiral. S~n~ (n even) → achiral.",
                "One stereocentre → always chiral.",
                "Two or more → test; symmetric chains may be meso.",
                "No stereocentre → still test for axial/planar chirality.",
            ]),
            ("h2", "The projection conventions"),
            ("bul", [
                "Fischer: vertical back, horizontal forward; 180° rotation allowed, 90° forbidden.",
                "Newman: front carbon = point, back = circle; θ = 0° eclipsed, 60° staggered.",
                "Sawhorse: side view; keep the viewing direction when converting.",
                "Wedge–dash: wedge = towards you, hash = away.",
            ]),
            ("h2", "The reaction rules"),
            ("bul", [
                "S~N~2: inversion, second-order, aprotic, primary.",
                "S~N~1: racemisation (with bias), first-order, protic, tertiary.",
                "E2: anti-periplanar, stereospecific, Zaitsev with small bases.",
                "cis alkene + syn addition → meso; + anti → racemic.",
                "trans alkene + syn → racemic; + anti → meso.",
            ]),
            ("h2", "The conformational ladder"),
            ("bul", [
                "anti > gauche > eclipsed (butane); chair > twist-boat > boat (cyclohexane).",
                "Flip: a ⇄ e, up stays up.",
                "1,2-cis = a,e; 1,3-cis = e,e; 1,4-cis = a,e (identical substituents).",
                "tert-Butyl locks the chair equatorial.",
            ]),
            ("key", "Draw the molecule, find the symmetry, then name it. Every question in this chapter is a version of that sequence."),
        ],
    },
]
