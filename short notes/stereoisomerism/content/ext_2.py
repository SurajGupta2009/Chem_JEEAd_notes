# -*- coding: utf-8 -*-
"""Part II, sheets X-07 … X-12 — JEE Advanced extensions."""

SHEETS = [
    # ------------------------------------------------------------------ X-07
    {
        "id": "X-07",
        "title": "General enumeration: counting without guessing",
        "blocks": [
            ("p", "Part I counted stereoisomers with two formulas. Those formulas are special cases of one idea — counting orbits under a "
                  "symmetry group — and once you have the idea you can count cases the formulas do not cover: rings, polyenes, and "
                  "molecules with several kinds of centre."),
            ("h2", "6.26  Why the formulas fail"),
            ("p", "The formulas assume a chain whose only symmetry is the exchange of its two ends. A ring has rotational symmetry; a "
                  "branched chain has a different automorphism group; a molecule with two different kinds of centre has none of the "
                  "simple structure. The general method — count arrangements, then divide out the symmetry — works in every case."),
            ("h2", "6.27  Burnside's lemma in one line"),
            ("p", "The number of distinct objects is the average number of arrangements fixed by each symmetry operation:"),
            ("eq", ["N = (1/|G|) Σ~g~ |Fix(g)|"]),
            ("p", "For a symmetric chain the group has two elements: the identity, which fixes all 2^n^ arrangements, and the end-exchange, "
                  "which fixes only the arrangements that read the same from both ends. That gives N = (2^n^ + F)/2, where F is the number "
                  "of palindromic arrangements. For a chain the exchange reverses the sequence and inverts every descriptor, so F = "
                  "2^ceil(n/2)^."),
            ("eq", ["N = (2^n^ + 2^ceil(n/2)^) / 2"]),
            ("table", ["n", "2^n^", "2^ceil(n/2)^", "N", "matches Part I?"], [
                ["1", "2", "2", "2", "yes (but-2-ene)"],
                ["2", "4", "2", "3", "yes (tartaric acid)"],
                ["3", "8", "4", "6", "yes"],
                ["4", "16", "4", "10", "yes"],
                ["5", "32", "8", "20", "yes"],
                ["6", "64", "8", "36", "yes"],
            ], [8, 20, 24, 16, 32], "Table 6.13 — Burnside reproduces every row of the Part I table."),
            ("key", "For an even-n symmetric chain, N = (2^n^ + 2^(n/2)^)/2, identical to the table in Part I. Burnside explains why the formulas have that shape."),
            ("h2", "6.28  Counting stereoisomers of a symmetric molecule"),
            ("p", "**Tartaric acid (n = 2, ends exchanged by a C~2~-type operation).** The identity fixes all four configurations; the exchange "
                  "fixes the two strings that read the same from both ends, (R,S) and (S,R) — the anti-palindromes — so the orbit count is "
                  "(4 + 2)/2 = 3 stereoisomers: the active pair (R,R)/(S,S) and the meso compound (R,S) ≡ (S,R)."),
            ("p", "**A trisubstituted benzene.** Positions 1, 3, 5 with three different substituents: the ring has a C~3~ axis and three "
                  "mirror planes. There is no stereocentre and no chiral arrangement, so the count is the number of positional isomers, "
                  "which is an orbit count of the substitutions under the ring's symmetry — three distinct isomers for three identical "
                  "substituents on 1,3,5, and more when they differ."),
            ("h2", "6.29  Polysubstituted rings"),
            ("table", ["Ring", "Substitution", "Distinct positional isomers", "Method"], [
                ["benzene", "C~6~H~4~Cl~2~", "3", "ortho, meta, para"],
                ["benzene", "C~6~H~3~Cl~3~", "3", "1,2,3; 1,2,4; 1,3,5"],
                ["benzene", "C~6~H~2~Cl~4~", "3", "1,2,3,4; 1,2,3,5; 1,2,4,5"],
                ["cyclopropane", "C~3~H~4~Cl~2~", "2", "1,1 and 1,2"],
                ["cyclobutane", "C~4~H~6~Cl~2~", "3", "1,1; 1,2; 1,3"],
            ], [20, 22, 24, 34], "Table 6.14 — positional isomerism is an orbit count, not a stereochemistry question."),
            ("warn", "Do not apply the stereoisomer formulas to a positional-isomer question. “How many dichlorobenzenes?” is a symmetry count on the ring; “how many stereoisomers of 1,2-dichlorocyclohexane?” is a stereochemistry count. Read which one is asked."),
        ],
    },
    # ------------------------------------------------------------------ X-08
    {
        "id": "X-08",
        "title": "Prochirality and enantiotopic groups",
        "blocks": [
            ("h2", "6.30  Faces and groups"),
            ("p", "A carbonyl carbon is planar; its two faces are **enantiotopic** if the molecule has no other stereocentre, because attack on "
                  "one face gives one enantiomer and attack on the other gives the other. The faces are labelled Re and Si. An enzyme can "
                  "distinguish them, which is why biological reductions are stereospecific."),
            ("p", "Two identical groups on a tetrahedral carbon are **enantiotopic** if replacing one or the other by a different group gives "
                  "enantiomers, and **diastereotopic** if it gives diastereomers. In ethanol the two H on CH~2~ are enantiotopic; in "
                  "(R)-butan-2-ol the two H on C1 are diastereotopic, which is why they show different NMR signals."),
            ("table", ["Relationship", "Replacement gives", "NMR: same signal?"], [
                ["homotopic", "the same compound", "yes"],
                ["enantiotopic", "enantiomers", "yes in an achiral solvent"],
                ["diastereotopic", "diastereomers", "no — different chemical shifts"],
            ], [24, 30, 46], "Table 6.16 — the three relationships between “identical” groups."),
            ("h2", "6.31  Why this matters for mechanism"),
            ("p", "Every stereospecific enzyme reaction is a statement about enantiotopic groups: the enzyme recognises one of two otherwise "
                  "identical groups or faces. In the laboratory, an achiral reagent cannot distinguish enantiotopic faces, so it gives a "
                  "racemic mixture — which is exactly why asymmetric catalysis is hard and why it won a Nobel prize."),
            ("h2", "6.32  Pseudoasymmetric centres"),
            ("p", "A carbon attached to two groups that are themselves chiral, and mirror images of each other (one R, one S), plus two other "
                  "different groups, is **pseudoasymmetric**. It is labelled r or s (lower case) and it is not a stereocentre in the usual "
                  "sense: the molecule containing it is achiral."),
            ("p", "The standard example is meso-tartaric acid: the central C2–C3 bond has (R) on one side and (S) on the other, and the two "
                  "carbons are pseudoasymmetric. This is why the meso form of a three-centre chain can exist in two diastereomeric forms "
                  "(R,r,S) and (R,s,S) — a subtlety JEE Advanced has used more than once."),
            ("key", "Pseudoasymmetric centre: two ligands are enantiomorphic (R and S), the other two differ. The centre is labelled r/s and the molecule stays achiral. It is what makes the odd-n meso row of the counting table read 2^((n−1)/2)^ rather than 1."),
            ("warn", "An r/s centre is not a stereocentre and does not make the molecule chiral. If a question asks “how many stereocentres?”, do not count it; if it asks “how many stereoisomers?”, it is exactly the subtlety that decides the answer."),
        ],
    },
    # ------------------------------------------------------------------ X-09
    {
        "id": "X-09",
        "title": "Optical purity, resolution engineering and chiroptical methods",
        "blocks": [
            ("h2", "6.33  Descriptors of purity"),
            ("table", ["Quantity", "Definition", "Range", "Use"], [
                ["optical purity", "observed [α] / [α] of pure enantiomer", "0–100 %", "historical; equals ee for two-component mixtures"],
                ["enantiomeric excess (ee)", "([R] − [S]) / ([R] + [S])", "0–100 %", "modern standard"],
                ["diastereomeric excess (de)", "([major] − [minor]) / total", "0–100 %", "for reactions creating a second centre"],
                ["enantiomeric ratio (er)", "[R] : [S]", "1:1 to ∞", "used in catalysis papers"],
            ], [28, 40, 14, 18], "Table 6.17 — four numbers, one idea: how far from racemic."),
            ("p", "The relation between ee and the observed rotation is linear: ee = α~obs~/α~pure~. That is why polarimetry was the standard "
                  "method for a century, and why it fails when an achiral impurity changes the concentration or when the sample contains a "
                  "meso form."),
            ("h2", "6.34  Kinetic resolution"),
            ("p", "If the two enantiomers react at different rates with a chiral reagent or enzyme, stopping the reaction at partial conversion "
                  "leaves the slower enantiomer enriched and converts the faster one into a product. The enantiomeric excess of the recovered "
                  "starting material rises with conversion; at 50 % conversion the theoretical maximum is 100 % of the slower enantiomer, but "
                  "the yield is only 50 %."),
            ("eq", ["ee of recovered substrate rises as conversion increases",
                    "ee of product falls as conversion increases"]),
            ("p", "Dynamic kinetic resolution combines racemisation of the substrate with selective reaction, so both enantiomers are funnelled "
                  "into one product and the yield can exceed 50 %."),
            ("h2", "6.35  Chiroptical methods"),
            ("p", "Optical rotatory dispersion (ORD) plots [α] against wavelength; circular dichroism (CD) measures the different absorption of "
                  "left- and right-circularly polarised light. Both give a spectrum, not a single number, and both can identify a chromophore's "
                  "handedness — which is how the absolute configuration of complex natural products is assigned. They are outside the JEE "
                  "syllabus but explain why “specific rotation” is only the simplest chiroptical measurement."),
            ("key", "ee is the number, [α] is the measurement, and ORD/CD are the spectra. For JEE, ee = α~obs~/α~pure~ and the sign of α tells you which enantiomer is in excess — not the configuration."),
        ],
    },
    # ------------------------------------------------------------------ X-10
    {
        "id": "X-10",
        "title": "Advanced problem set (with full solutions)",
        "blocks": [
            ("h2", "6.36  Problems"),
            ("num", [
                "How many stereoisomers does 1,2-dimethylcyclopropane have, and which are optically active?",
                "Assign R/S to both centres of meso-tartaric acid and explain why the molecule is achiral.",
                "trans-2-Butene reacts with Br~2~. Give the product, its stereochemistry, and whether the product mixture is optically active.",
                "How many stereoisomers does 1,2,3-tribromocyclopropane have?",
                "A sample of 2-butanol shows [α] = +3.4°, and the pure enantiomer has [α] = +13.5°. What is the ee and the composition?",
                "Why is trans-cyclooctene chiral while cis-cyclooctene is not?",
                "S~N~1 hydrolysis of (R)-2-bromobutane gives a product of [α] = −2.0° while pure (S)-2-butanol has [α] = −13.5°. What is the ee, and what does it tell you about the mechanism?",
                "How many stereoisomers does 2,3,4-trihydroxypentanedioic acid have?",
            ]),
            ("h2", "6.37  Solutions"),
            ("p", "**(1)** Three: cis (achiral, a plane through C3 and the C1–C2 bond) and a trans pair (chiral). Active: the trans pair, 2 of the 3."),
            ("p", "**(2)** (2R,3S). Each centre has OH > COOH > H; reading the Fischer with H horizontal reverses the apparent direction. The "
                  "molecule has a plane through the middle of the C2–C3 bond, so the two halves are mirror images and the mirror image of the "
                  "whole is itself."),
            ("p", "**(3)** Anti addition gives the meso (2R,3S) dibromide — one compound, achiral, so the product is optically inactive (and not "
                  "because it is racemic: it is a single achiral compound)."),
            ("p", "**(4)** Three geometrical arrangements (all-cis; one trans; the 1,2-trans-3-cis pattern) collapse to four stereoisomers: "
                  "all-cis is achiral (plane), the other two arrangements are chiral pairs except where a plane survives. Draw each and "
                  "check: the answer is 4, of which 2 are active."),
            ("p", "**(5)** ee = 3.4/13.5 = 25 %; the sample is 62.5 % of the (+) enantiomer and 37.5 % of the (−) enantiomer."),
            ("p", "**(6)** The trans double bond forces the ring above and below the alkene plane, so the molecule has no mirror plane and is "
                  "chiral; the cis alkene leaves a plane through the ring and the double bond, so cis-cyclooctene is achiral."),
            ("p", "**(7)** ee = 2.0/13.5 = 15 %. The product is mostly the (S) enantiomer, which is the *inverted* product, but only 15 % ee "
                  "means the reaction is close to racemic — consistent with S~N~1 through a planar carbocation, with a small excess of "
                  "inversion because the leaving group shields one face briefly."),
            ("p", "**(8)** n = 3 with similar ends: active 2^2^ − 2^1^ = 2, meso 2^1^ = 2, total 4. The active pair is (R,R,R)/(S,S,S); "
                  "the two meso forms have an (R) and an (S) end and a pseudoasymmetric middle carbon, so (R,r,S) and (R,s,S) are "
                  "diastereomers, not the same compound."),
            ("key", "Every solution above reduces to one of four moves: count centres, test symmetry, assign CIP, or convert a rotation into an ee. If a solution needs a fifth move, the question is testing a definition you have not stated."),
        ],
    },
    # ------------------------------------------------------------------ X-11
    {
        "id": "X-11",
        "title": "Where stereochemistry meets the rest of chemistry",
        "blocks": [
            ("h2", "6.38  Organic synthesis"),
            ("p", "Every asymmetric synthesis is an answer to the question “how do you make one enantiomer?”. The strategies are: use a chiral "
                  "starting material from the chiral pool (amino acids, sugars, terpenes); use a chiral auxiliary that is removed afterwards; "
                  "use a chiral catalyst (organocatalyst or transition-metal complex); or resolve at the end. The first three are "
                  "stereoselective, the fourth is a separation."),
            ("p", "The contraceptive pill, statins, and most modern drugs are single enantiomers because the wrong enantiomer can be inactive or "
                  "harmful. That commercial fact is why asymmetric catalysis is a large industry, and why the vocabulary of this chapter "
                  "(ee, de, enantioselective) appears in every process chemistry paper."),
            ("h2", "6.39  Polymers"),
            ("p", "The stereochemistry of a polymer chain decides whether it crystallises. Isotactic polypropene (all methyls on one side, made "
                  "with a Ziegler–Natta catalyst) is crystalline and rigid; atactic polypropene (random) is amorphous and rubbery. The "
                  "monomer is achiral, but the polymer is not — tacticity is stereochemistry at the level of a chain."),
            ("h2", "6.40  Biochemistry"),
            ("p", "Life is homochiral: proteins are made of L-amino acids and nucleic acids of D-ribose. An enzyme's active site is itself chiral, "
                  "so it recognises one enantiomer of a substrate — which is why (R)-thalidomide is sedating and (S)-thalidomide is "
                  "teratogenic, and why drug regulators now require single-enantiomer data."),
            ("h2", "6.41  Materials and photochemistry"),
            ("p", "Chiral liquid crystals, chiral dopants for displays, and photoresponsive switches all use the same ideas. Azobenzene is the "
                  "standard switch: trans is flat and mesogenic, cis is bent and disrupts the phase; irradiation at one wavelength switches "
                  "the shape, and the thermal back-reaction restores it."),
            ("h2", "6.42  Inorganic chemistry"),
            ("p", "Tris-chelate complexes [M(en)~3~]^n+^ are chiral (Λ/Δ), as are many octahedral complexes with bidentate ligands. Coordination "
                  "chemistry also supplies examples of stereochemistry without carbon (sulfoxides, phosphines), and of fluxional molecules "
                  "whose stereochemistry averages on the NMR timescale."),
            ("key", "Stereochemistry is not a chapter of organic chemistry; it is a way of describing shape that reappears in polymers, enzymes, materials and coordination compounds. The vocabulary is the transferable part."),
        ],
    },
    # ------------------------------------------------------------------ X-12
    {
        "id": "X-12",
        "title": "Extension pitfalls and a final checklist",
        "blocks": [
            ("h2", "6.43  The five-question audit"),
            ("num", [
                "**Have I drawn the molecule?** Every error in this chapter starts with an unexamined drawing.",
                "**Have I tested symmetry before counting?** A plane or a centre removes half the count.",
                "**Have I asked whether the ends are identical?** It changes the counting row and the existence of meso forms.",
                "**Have I checked whether the barrier makes the arrangement configurational?** Atropisomers and amides are configurations; ethane conformers are not.",
                "**Have I stated the mechanism before the stereochemical outcome?** Inversion, racemisation, syn and anti are consequences of mechanism, not facts to recall.",
            ]),
            ("h2", "6.44  Extension-level traps"),
            ("bul", [
                "A twist-boat is chiral but a cyclohexane sample is not — the chiral conformation is not long-lived.",
                "Two enantiomers of a biphenyl are atropisomers only if the barrier is above ~80 kJ mol^−1^.",
                "trans-Cyclooctene is chiral; cis-cyclooctene is not. The double bond geometry, not the ring size, does the work.",
                "Pseudoasymmetric centres (r/s) are not stereocentres but they change the stereoisomer count.",
                "Burnside counting needs the *whole* symmetry group, not just the end exchange; for a ring the rotations matter.",
                "The anomeric effect can override a steric preference; do not quote A-values alone for a pyranose.",
                "Stereospecific and stereoselective are not synonyms; examiners award marks for the distinction.",
            ]),
            ("h2", "6.45  What remains uncertain"),
            ("p", "Three things in this set are worth flagging honestly. First, numerical energy values (barriers, A-values, strain energies) are "
                  "quoted from standard textbook ranges; different texts differ in the second digit, so use them to fix order of magnitude, "
                  "not to settle a tie. Second, the syn/anti convention for oximes is not uniform across Indian textbooks, and the notes "
                  "therefore teach E/Z as the primary descriptor. Third, the CIP rules for axes and for pseudoasymmetric centres are stated "
                  "here in outline only; the full IUPAC blue-book rules include several tie-breaking refinements that are beyond the JEE "
                  "syllabus."),
            ("key", "A full-mark answer names the idea, shows the drawing, and states the conclusion in the vocabulary the question used. Everything else is detail."),
            ("p", "This is the end of Part II. Part I (J-01 to J-29) covers the JEE Main and JEE Advanced core; the source map, the corrections "
                  "made and the verification status are in SCOPE.md and SOURCE-AUDIT.md, and the printable PNGs and PDFs are indexed in "
                  "index.html."),
        ],
    },
]
