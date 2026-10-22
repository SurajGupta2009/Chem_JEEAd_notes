# -*- coding: utf-8 -*-
"""Part I, sheets J-01 … J-08."""

SHEETS = [
    # ------------------------------------------------------------------ J-01
    {
        "id": "J-01",
        "title": "Cover and how to use these sheets",
        "blocks": [
            ("lead", "**Stereoisomerism** — a complete handwritten short-note set"),
            ("p", "Part I is the JEE Main and JEE Advanced core: geometrical, optical and conformational "
                  "isomerism, the counting rules, and the reaction stereochemistry JEE actually asks. "
                  "Part II is the JEE-Advanced-level extension — symmetry and S~n~, general counting, "
                  "ring junctions, quantitative conformational analysis, reaction design."),
            ("h2", "What is inside"),
            ("table", ["Section", "Sheets", "Theme"], [
                ["1. Foundations", "J-01 – J-02", "Isomerism map, vocabulary, why stereochemistry is tested"],
                ["2. Geometrical", "J-03 – J-09", "Conditions, E/Z, rings, cumulenes, counting, physical properties"],
                ["3. Optical", "J-10 – J-20", "Polarimetry, chirality, symmetry, meso, projections, R/S, counting"],
                ["4. Conformational", "J-21 – J-24", "Barriers, ethane and butane, cyclohexane"],
                ["5. Reactions", "J-25 – J-27", "S~N~1/S~N~2, E2, addition, worked enumeration"],
                ["6. Exam craft", "J-28 – J-29", "Twenty traps, one-page recall"],
            ], [22, 20, 58], "Table 0.1 — the route map for Part I."),
            ("h2", "How to read a page"),
            ("p", "Each sheet has one argument: a definition, the reason behind it, a worked example, then "
                  "the result to remember and the trap that follows from it. The colour carries the "
                  "meaning, so read the colour before the words."),
            ("bul", [
                "**Navy handwriting** — the explanation and the working.",
                "**Teal headings and teal panels** — the reason something is true (*why it works*).",
                "**Yellow panels** — KEY RESULT: the line to memorise, or the formula to reproduce.",
                "**Red panels** — TRAP: the mistake that examiners build options around.",
            ]),
            ("key", "If you remember only one sentence from the whole set, remember this: **stereochemistry is decided by the 3-D drawing, not by the name of the functional group.** Every line here is a shortcut for a question you could answer by drawing carefully."),
            ("h2", "Source and scope of these notes"),
            ("p", "Built from the supplied 57-lecture note file (NS Sir, Stereoisomerism) and checked against the "
                  "NCERT Class XI Unit 10 and Class XII Unit 10 stereochemistry content; Part II adds the JEE "
                  "Advanced statements of the same topics and nothing beyond. Where the source and a standard text "
                  "disagreed, the correction is recorded in SOURCE-AUDIT.md and the corrected statement is taught here."),
            ("note", "These are study notes, not a textbook. Values marked ≈ are typical textbook values quoted to fix "
                     "the order of magnitude; they are not measurements made for this set. Every structure was drawn and "
                     "checked by hand-encoded rules, but no claim of exhaustive chemical verification is made."),
            ("h2", "Printing"),
            ("p", "A4 portrait, 10 mm margins, nominal 300 dpi; print at 100 % (Fit, not Fill or Crop), one sheet per "
                  "page. The PNGs are 2480 × 3508 px. There is no Olympiad section: Part II stops at JEE Advanced."),
        ],
    },
    # ------------------------------------------------------------------ J-02
    {
        "id": "J-02",
        "title": "Isomerism map and the vocabulary",
        "blocks": [
            ("p", "Start every problem from the molecular formula. If two structures differ in which atom is joined "
                  "to which, they are **structural** isomers; if the connectivity is identical and only the "
                  "arrangement in space differs, they are **stereoisomers**. The whole chapter lives in the "
                  "right-hand branch of the map below."),
            ("h2", "1.1  The isomerism tree"),
            ("table", ["Level", "The question to ask", "Examples"], [
                ["Structural (constitutional)", "Is the connectivity different?", "butane / 2-methylpropane; propan-1-ol / methoxyethane"],
                ["chain, position, functional", "which carbon, which functional group?", "pentane isomers; butan-1-ol / butan-2-ol; ethanol / dimethyl ether"],
                ["Stereoisomer", "same connectivity, different 3-D arrangement", "see the next two rows"],
                ["Conformational", "can it interconvert without bond breaking?", "anti/gauche butane; chair/boat cyclohexane"],
                ["Configurational", "does it interconvert by rotation?", "cis/trans but-2-ene; (R)/(S) lactic acid"],
            ], [30, 34, 36], "Table 1.1 — the classification used throughout these notes. Structural is the left branch; stereoisomerism is everything below."),
            ("p", "Configurational isomers are further split into **geometrical** (cis/trans, E/Z, syn/anti) and "
                  "**optical** (enantiomers and diastereomers, including meso forms). Conformational isomers are the "
                  "subject of section 4."),
            ("h2", "1.2  Six words that must be exact"),
            ("num", [
                "**Stereocentre** — an atom bearing groups arranged so that interchanging two of them gives a stereoisomer. For carbon this usually means four different groups; it is a property of one atom.",
                "**Chiral** — the molecule is not superimposable on its mirror image. It is a property of the whole molecule, and it is the condition for optical activity.",
                "**Enantiomers** — a pair of stereoisomers that are non-superimposable mirror images. Identical physical properties, opposite rotation.",
                "**Diastereomers** — stereoisomers that are not mirror images. Different physical properties, separately isolable by ordinary means.",
                "**Meso** — a molecule with stereocentres that is nevertheless achiral because an internal plane (or centre) makes its mirror image superimposable.",
                "**Racemic** — a 1:1 mixture of two enantiomers, optically inactive by external compensation.",
            ]),
            ("key", "Chirality is decided by the molecule, not by the count of stereocentres. Meso compounds have stereocentres and are achiral; allenes and biphenyls can be chiral with no stereocentre at all. Both directions are examinable."),
            ("warn", "“Optically inactive” is **not** a synonym for “achiral”. A racemic mixture is optically inactive although both of its components are chiral. Quote the reason for inactivity: no chiral arrangement, internal compensation, or external compensation."),
            ("h2", "1.3  Why the topic is worth marks"),
            ("p", "Stereochemistry is the part of organic chemistry where a reaction can be right and still give the wrong "
                  "answer. S~N~2 gives inversion; S~N~1 gives racemisation; syn addition to an alkene gives a *meso* product "
                  "from one face and a racemic pair from the opposite faces; hydrogenation of an optically active alkene "
                  "can destroy the activity. JEE Advanced has repeatedly fused this chapter with S~N~1/S~N~2, addition and "
                  "hydrogenation rather than asking a definition directly."),
            ("p", "The drug thalidomide is the standard illustration: the (R) enantiomer is the sedative, the (S) enantiomer "
                  "is teratogenic, and under the racemisation conditions *in vivo* the two interconvert through the acidic "
                  "C–H next to the imide. The point is chemical, not pharmacological: a stereocentre next to an acidic C–H "
                  "is not configurationally stable."),
        ],
    },
    # ------------------------------------------------------------------ J-03
    {
        "id": "J-03",
        "title": "Geometrical isomerism: the two conditions",
        "blocks": [
            ("h2", "2.1  Why a C=C freezes the arrangement"),
            ("p", "The π bond is built from two p orbitals that overlap side-on. Twist the double bond by 90° and the "
                  "overlap falls to zero, so the π bond must break before the two ends can exchange places. The barrier "
                  "is about **250–270 kJ mol^−1^**, roughly twenty times the thermal energy available at room "
                  "temperature; a single C–C bond needs only 12–20 kJ mol^−1^ and rotates freely at 25 °C."),
            ("eq", ["E(π, C=C) ≈ 250–270 kJ mol^−1^",
                    "E(σ, C–C) ≈ 12–20 kJ mol^−1^"]),
            ("fig", "condition", "Fig. 2.1 — the two conditions are independent. Restricted rotation without two different groups at both ends gives no isomerism; two different groups without restricted rotation gives only conformers.", 0.20),
            ("h2", "2.2  Condition 1 — restricted rotation"),
            ("p", "Rotation must be blocked *in a way that survives at room temperature*. Three situations qualify: a π bond "
                  "(C=C, C=N, N=N), a ring (the two substituents are locked above and below the mean plane), and a "
                  "sterically locked single bond (the atropisomerism of section 6.11 in Part II, where the barrier is high "
                  "enough that the conformers can be isolated). A single bond that rotates freely never gives geometrical "
                  "isomers, however different the two drawings look."),
            ("h2", "2.3  Condition 2 — two different groups at each end"),
            ("p", "On the left carbon, call the groups a and b; on the right, x and y. Isomerism exists only if "
                  "**a ≠ b and x ≠ y**. This is why terminal alkenes (CH~2~=CHR) and geminally disubstituted alkenes "
                  "((CH~3~)~2~C=CH~2~) have no geometrical isomerism: one carbon carries two identical atoms, so "
                  "interchanging the two ends produces the same molecule."),
            ("table", ["Structure", "Left end", "Right end", "Geometrical?"], [
                ["CH~3~CH=CHCH~3~", "CH~3~, H", "CH~3~, H", "yes — cis and trans (2)"],
                ["CH~2~=CHCH~3~", "H, H", "—", "no (identical H on one carbon)"],
                ["(CH~3~)~2~C=CHCH~3~", "CH~3~, CH~3~", "CH~3~, H", "no (two CH~3~ on one carbon)"],
                ["CHCl=CHBr", "H, Cl", "H, Br", "yes — and cis/trans cannot name it; use E/Z"],
            ], [30, 22, 22, 26], "Table 2.1 — apply the test to each end separately."),
            ("key", "Two questions, two answers, one conclusion: **is rotation blocked?** and **are both ends unsymmetrical?** Only two yeses give a geometrical centre."),
            ("warn", "Do **not** count a C=C twice. One double bond is one geometrical centre, giving at most two isomers. The count 2^n^ uses *n = number of centres*, not number of atoms."),
            ("h2", "2.4  The four kinds of centre"),
            ("num", [
                "**C=C** in an open chain or a large ring; each sp^2^ carbon planar, each end unsymmetrical.",
                "**C=N** in oximes and imines: nitrogen is sp^2^ and carries a lone pair, so the nitrogen end is always unsymmetrical — only the carbon end needs checking.",
                "**N=N** in azo compounds and diazoates: each nitrogen carries one organic group plus a lone pair.",
                "**Ring carbons** of cycloalkanes: substituents are locked above/below the ring; the ring itself supplies the restricted rotation.",
            ]),
            ("p", "For a C=N centre the nitrogen lone pair occupies the third sp^2^ orbital. That lone pair counts as a "
                  "substituent both for the isomerism test and for naming (E/Z or syn/anti). The same is true of the N=N centre."),
            ("h2", "2.5  How oximes are made (the reaction behind the question)"),
            ("p", "R~2~C=O + NH~2~OH → R~2~C=N–OH + H~2~O (mild acid, pH 4–5). Aldehydes give aldoximes (RCH=NOH); "
                  "ketones give ketoximes (R~2~C=NOH). The reaction is reversible, so an oxime can be hydrolysed back to "
                  "the carbonyl compound, and hydroxylamine (or hydrazine) is the standard test that distinguishes a "
                  "carbonyl from an alcohol or ether."),
            ("table", ["Carbonyl compound", "Oxime stereoisomers", "Reason"], [
                ["HCHO", "1", "carbon bears two H"],
                ["RCHO (x ≠ y)", "2", "carbon bears H and R"],
                ["R~2~C=O with R ≠ R′", "2", "two different groups"],
                ["R~2~C=O with R = R′", "1", "two identical groups"],
                ["a diketone, two C=N formed", "up to 4", "each centre doubles the count; check symmetry"],
            ], [34, 22, 44], "Table 2.2 — the standard “number of products” question."),
            ("warn", "For a symmetric diketone such as butane-2,3-dione the two C=N centres are equivalent; syn,syn and anti,anti are two distinct compounds, but syn,anti is one compound, not two. Enumerate, then merge by symmetry."),
            ("h2", "2.6  The C=N family: hydrazones, imines and semicarbazones"),
            ("p", "Every reaction that condenses a carbonyl with an amine derivative makes a C=N centre, and every one of "
                  "them inherits the same stereochemistry. The table below is worth learning as a family, because the "
                  "question “how many isomers?” is identical for all four."),
            ("table", ["Reagent", "Product", "C=N formed", "Stereoisomers for RCHO"], [
                ["NH~2~OH", "oxime  RCH=N–OH", "yes", "2 (syn/anti, or E/Z)"],
                ["NH~2~NH~2~", 'hydrazone RCH=N–NH~2~', "yes", "2"],
                ["NH~2~NHR", "substituted hydrazone", "yes", "2"],
                ["NH~2~CONH~2~", 'semicarbazone RCH=N–NHCONH~2~', "yes", "2"],
                ["NH~2~C(=NH)NH~2~", "guanidine condensate", "yes", "2"],
            ], [22, 36, 18, 24], "Table 2.3 — all five families create the same kind of centre, so the counting rule is shared."),
            ("p", "For a ketone R~1~COR~2~ the count depends on whether the two groups differ: R~1~ ≠ R~2~ gives two "
                  "isomers, R~1~ = R~2~ gives one. For a diketone the centres are counted independently and then merged "
                  "by symmetry — butane-2,3-dione gives three (syn,syn; anti,anti; syn,anti), not four."),
            ("p", "The nitrogen substituent matters for naming but not for counting. In an oxime the –OH is the reference "
                  "group; in a hydrazone the –NH~2~ is. E/Z is assigned from the CIP priorities in each case, with the "
                  "nitrogen lone pair always lowest."),
            ("key", "Carbonyl + any NH~2~–X reagent → C=N centre. The number of stereoisomers depends only on the two groups on the carbonyl carbon, never on what X is."),
            ("warn", "Do not write “oximes show cis/trans”. The correct descriptors are syn/anti (with the reference group named) or E/Z. cis/trans needs a pair of comparable groups at both ends, and the nitrogen end carries a lone pair rather than a second carbon group."),
        ],
    },
    # ------------------------------------------------------------------ J-04
    {
        "id": "J-04",
        "title": "E/Z and the CIP priority rules",
        "blocks": [
            ("p", "cis/trans works only when each end of the double bond carries a pair of comparable groups. When the four "
                  "groups are all different — CHCl=CHBr, for example — there is no “same side” pair to name. The universal "
                  "descriptor is E/Z, built on the Cahn–Ingold–Prelog (CIP) priority rules."),
            ("h2", "2.7  E and Z"),
            ("p", "Assign priority 1 and 2 at the left carbon, then priority 1 and 2 at the right carbon. If the two "
                  "priority-1 groups lie on the **same side** of the double bond the descriptor is **Z** (*zusammen*, "
                  "together); if they lie on **opposite sides** it is **E** (*entgegen*, opposite)."),
            ("key", "E/Z compares priority-1 groups, not “like” groups. Two different alkenes can both be (E) even though their substituents are not the ones you would call cis/trans."),
            ("warn", "Priority 1 groups together = E. Priority 1 groups opposite = Z. This is the single most common slip; say the rule aloud once before you assign."),
            ("h2", "2.8  The CIP rules, in the order you apply them"),
            ("num", [
                "**Higher atomic number at the first atom.** I > Br > Cl > S > O > N > C > H. If the first atoms differ, stop here.",
                "**Compare the next layer.** List the atoms attached to the first atom in decreasing atomic number and compare the lists position by position (highest first). Do not jump to a deeper layer while the present layer is still undecided.",
                "**Same element, higher mass number wins.** D > H, T > D.",
                "**Lone pair is the lowest possible ligand.** A real atom to any atom always beats a lone pair.",
                "**Multiple bonds are expanded.** Each double bond counts as two single bonds to that atom; a triple bond counts as three. C=O is C bonded to (O, O, phantom O); C≡N is C bonded to (N, N, phantom N). This is bookkeeping, not a real structure.",
            ]),
            ("table", ["Group", "Layer 1", "Layer 2 (as written)", "Verdict"], [
                ["–CH~3~", "C", "H, H, H", "lowest carbon group"],
                ["–CH~2~Cl", "C", "Cl, H, H", "beats –CH~3~ at layer 2"],
                ["–CH~2~OH", "C", "O, H, H", "below –CH~2~Cl (O loses to Cl at layer 2)"],
                ["–CHO", "C", "O, O, H (one O phantom)", "beats –CH~2~OH"],
                ["–COOH", "C", "O, O, O (one O phantom, one OH)", "beats –CHO"],
                ["–C≡N", "C", "N, N, N (two phantom N)", "below –COOH (O beats N at layer 2)"],
                ["–C≡CH", "C", "C, C, H (two phantom C)", "ties with –CH=CH~2~ (same expansion)"],
            ], [16, 14, 34, 36], "Table 2.4 — expand multiple bonds before comparing anything to the right."),
            ("warn", "The commonest E/Z error is comparing the second atom of a group before checking the first atom of a multiple bond. Expand every multiple bond into phantom atoms **first**, then compare layer by layer."),
            ("h2", "2.9  Worked examples"),
            ("p", "**(a) 1-bromo-1-chloropropene, CH~3~CH=CBrCl.** At the left carbon CH~3~ beats H. At the right, Br beats "
                  "Cl. If the CH~3~ and Br are on the same side, the compound is (Z)-1-bromo-1-chloroprop-1-ene; if "
                  "opposite, (E). Note that “cis” would be meaningless here."),
            ("p", "**(b) But-2-enedioic acid, HOOC–CH=CH–COOH.** Both ends carry H and COOH, so cis/trans is available "
                  "(maleic = cis, fumaric = trans). The priority groups are COOH at both ends, so maleic acid is (Z) and "
                  "fumaric acid is (E). This pair is worth memorising because it reappears in the physical-property questions."),
            ("p", "**(c) An oxime.** For R~2~C=N–OH, the nitrogen ligands are –OH and the lone pair; oxygen beats the lone "
                  "pair, so –OH is priority 1 on nitrogen. On carbon the higher-priority carbon group is priority 1. If "
                  "the two priority-1 groups are on opposite sides the oxime is (E)."),
            ("p", "**(d) A diene with two centres.** Each double bond gets its own descriptor and its own locant: "
                  "(2E,4Z)-hexa-2,4-diene. Do not average or combine them."),
            ("h2", "2.10  cis/trans, syn/anti, E/Z — which name to use"),
            ("table", ["Descriptor", "Applies to", "Requirement", "Notes"], [
                ["cis / trans", "C=C, C=N rings", "a comparable pair of groups at the two ends", "relative, not universal"],
                ["syn / anti", "C=N, N=N", "the OH (or group) compared with a named group", "always quote the reference group"],
                ["E / Z", "any geometrical centre", "CIP priorities only", "universal; use it when in doubt"],
            ], [18, 22, 34, 26], "Table 2.5 — use E/Z for any centre with four different groups."),
            ("note", "Indian textbooks use “syn” for oximes in two different senses: sometimes “OH on the same side as H” and sometimes “OH on the same side as the named R”. Because the two conventions coexist, JEE has moved to E/Z for oximes. If a question uses syn/anti, state the reference group explicitly in your answer."),
            ("h2", "2.11  Four CIP drills with the reasoning written out"),
            ("p", "**(a) –CH(Br)CH~2~Br versus –CH~2~CH~2~Br.** Both start with C. Layer 2: (Br, H, C) versus (C, H, H). "
                  "Br wins at the first comparison, so –CH(Br)CH~2~Br is the higher priority group; the longer chain is "
                  "irrelevant because the decision was made at layer 2."),
            ("p", "**(b) –CH(OH)CH~3~ versus –CH(OH)CH~2~OH.** Layer 1: C versus C. Layer 2: (O, H, C) versus (O, H, C) — "
                  "still tied. Layer 3: the first group has (H, H, H) on its carbon, the second has (O, H, H), so the "
                  "second group wins. This is how the aldehyde end of a sugar is ranked above the alcohol end."),
            ("p", "**(c) –CHO versus –COOH.** Expand the multiple bonds. –CHO is C(O, O, H) because the C=O counts twice; "
                  "–COOH is C(O, O, O) because the C=O counts twice and the OH adds one O. Compare position by position: "
                  "both have O, O; the third ligand decides, O > H, so –COOH wins."),
            ("p", "**(d) –C≡N versus –C≡CH.** Expand: (N, N, N) versus (C, C, H). N beats C at the first position, so "
                  "–C≡N wins. Note that the two groups have the same formula weight — the decision is about atoms, never "
                  "about mass."),
            ("table", ["Comparison", "Decided at layer", "Winner"], [
                ["–Br vs –Cl", "1", "–Br"],
                ["–OH vs –NH~2~", "1", "–OH"],
                ["–CH~2~Cl vs –CH~3~", "2", "–CH~2~Cl"],
                ["–CH(CH~3~)~2~ vs –CH~2~CH~2~Br", "2", "–CH(CH~3~)~2~"],
                ["–CHO vs –CH~2~OH", "2", "–CHO"],
                ["–COOH vs –CHO", "3", "–COOH"],
                ["–C≡N vs –C≡CH", "3", "–C≡N (N beats C)"],
                ["–D vs –H", "mass", "–D"],
            ], [34, 20, 46], "Table 2.6 — check which layer settles each comparison before comparing further."),
            ("warn", "The single most expensive mistake in this table is comparing a later atom of one group with an earlier atom of the other. Compare layer by layer, position by position; a bromine three bonds away never beats an oxygen one bond away."),
        ],
    },
    # ------------------------------------------------------------------ J-05
    {
        "id": "J-05",
        "title": "Rings and small cycloalkenes",
        "blocks": [
            ("h2", "2.12  Why a ring is a geometrical centre"),
            ("p", "A cycloalkane is not flat for n ≥ 4, but every ring carbon still has one bond pointing to one face and "
                  "one to the other. Turning a substituent from “up” to “down” would require the ring to pass through "
                  "itself, so the up/down arrangement is configurationally locked. That is exactly the situation a C=C "
                  "provides electronically."),
            ("fig", "ringupdown", "Fig. 2.2 — cis-1,2-dimethylcyclopropane has a mirror plane through C3 and the C1–C2 bond; the trans isomer has none and exists as a pair of enantiomers.", 0.34),
            ("h2", "2.13  Counting substituent patterns on a small ring"),
            ("num", [
                "**Anchor one substituent up.** Turning the whole molecule over is allowed, so the all-up and all-down drawings are the same compound.",
                "**List the remaining up/down choices**, then delete duplicates produced by (i) rotating the ring and (ii) turning the whole molecule over.",
                "**Treat identical substituents as identical** — two Br atoms are not distinguishable, so swapping their labels is not a new isomer.",
                "**Test each surviving pattern for σ and i.** A pattern with a mirror plane is one achiral compound; a pattern without one is a pair of enantiomers and contributes 2 to the stereoisomer count.",
            ]),
            ("table", ["Ring compound", "Geometrical isomers", "Total stereoisomers", "Which are chiral"], [
                ["1,2-dimethylcyclopropane", "2 (cis, trans)", "3", "trans (pair); cis is meso"],
                ["1,2-dimethylcyclobutane", "2 (all-cis, one trans)", "4", "the one trans form (pair)"],
                ["1,3-dimethylcyclobutane (different groups)", "3", "6", "the Br-trans form (pair)"],
                ["1,2-dimethylcyclopentane", "3 (cis, trans, cis′)", "4", "cis′ is meso; trans has a pair"],
                ["1,3-dimethylcyclopentane", "3", "4", "trans′ (pair), cis has σ"],
                ["1,2-dimethylcyclohexane", "2", "3", "trans (pair); cis — both have σ"],
            ], [32, 26, 20, 22], "Table 2.8 — patterns worth recognising. Count geometrical isomers first, then split the chiral ones into pairs."),
            ("h2", "2.14  Worked enumeration: 1,2-dibromo-3-methylcyclopropane"),
            ("p", "Put Br at C1 and C2, CH~3~ at C3. Anchor Br(1) up. The Br(2) choice splits into same face (up) and "
                  "opposite face (down). With Br(1) = Br(2) = up, the CH~3~ has two choices, but turning the ring over "
                  "makes them identical, so Br(2) = down with CH~3~ up is the same compound as Br(2) = up with CH~3~ down "
                  "(relabel the bromines). That leaves three geometrical arrangements:"),
            ("bul", [
                "**all three up (or all three down)** — a mirror plane through C3 and the C1–C2 bond → achiral, 1 compound.",
                "**both Br on one face, CH~3~ on the other** — again a mirror plane bisecting the Br–Br bond → achiral, 1 compound.",
                "**the two Br on opposite faces, CH~3~ either up or down** — no plane, no centre → chiral, a pair, 2 compounds.",
            ]),
            ("key", "Three geometrical isomers become four stereoisomers: 1 + 1 + 2. Always report both numbers if the question allows it, and say which are optically active."),
            ("h2", "2.15  Double bonds inside small rings"),
            ("p", "A C=C built into a ring is forced to be *cis*: the ring chain leaves the two sp^2^ carbons on the same "
                  "side. A trans-cycloalkene would need the chain to cross to the other face of the double bond, which is "
                  "geometrically impossible for small rings. The rule of thumb is: rings up to seven members show only the "
                  "cis alkene; cyclooctene is the first that can accommodate a trans double bond, and trans-cyclooctene is "
                  "strained but isolable."),
            ("p", "Trans-cycloalkenes are also chiral. The twist of the ring destroys every mirror plane, so it exists as "
                  "two enantiomers that interconvert only slowly. That is a genuine JEE-Advanced-standard point, and it is "
                  "not “a dangerous half-truth”."),
            ("warn", "For a small-ring alkene, “how many geometrical isomers?” has answer 1, not 2. If the question asks for the number of *stereoisomers* and the compound also has stereocentres, count those separately."),
            ("h2", "2.16  A harder ring enumeration: 1,2,3,4-tetramethylcyclobutane"),
            ("p", "Four substituents, all identical, on a four-membered ring. Anchor one methyl at C1. The remaining "
                  "three positions have three choices, but the square has a four-fold rotation and a mirror symmetry, so "
                  "most of the 8 raw patterns collapse."),
            ("table", ["Pattern (relative to C1 up)", "Distinct?", "Symmetry", "Stereoisomers"], [
                ["up, up, up, up (all cis)", "yes", "σ and i", "1"],
                ["up, up, up, down", "yes", "σ", "1"],
                ["up, down, up, down (alternating)", "yes", "i, σ", "1"],
                ["up, down, up, down (alternating, other phase)", "same as above", "rotation by 60°", "—"],
                ["up, up, down, up", "same as up, up, up, down", "rotation", "—"],
                ["up, down, down, up", "same as up, up, down, down", "rotation", "—"],
            ], [34, 22, 20, 24], "Table 2.9 — six of the eight patterns reduce to three compounds."),
            ("p", "So 1,2,3,4-tetramethylcyclobutane has three stereoisomers, all achiral. The all-cis form has a plane "
                  "through the ring and a centre; the up-up-up-down form has a plane; the alternating up-down-up-down form "
                  "has a centre of symmetry. None is chiral, which is a good reminder that “many substituents” does not "
                  "mean “chiral”."),
            ("h2", "2.17  Why the up/down method always works"),
            ("p", "The method is a direct application of the definition of a stereoisomer: same connectivity, different "
                  "spatial arrangement. On a ring, the only spatial variable available to a substituent is which face it "
                  "occupies, so enumerating faces is a complete enumeration. What must be removed afterwards is duplication "
                  "by symmetry: ring rotation, reflection, and turning the whole molecule over."),
            ("key", "Enumerate in three stages: anchor one group → list the up/down words → delete words related by rotation or global flip. Then test each survivor for σ and i to decide chiral or achiral."),
        ],
    },
    # ------------------------------------------------------------------ J-06
    {
        "id": "J-06",
        "title": "Cumulenes, spiro compounds and the odd–even rule",
        "blocks": [
            ("h2", "2.18  Geometry of a cumulene"),
            ("p", "A cumulene has consecutive double bonds, C=C=C=… . Each inner carbon is sp hybridised and linear, and "
                  "its two π bonds use two different p orbitals, which are perpendicular. The consequence is that the "
                  "substituent planes at the two ends are either **perpendicular** or **coplanar**, depending on how many "
                  "double bonds lie between them."),
            ("fig", "cumulene", "Fig. 2.3 — in an allene the two end planes are perpendicular. Substituting both ends with two different groups each removes every mirror plane and leaves a chiral axis.", 0.30),
            ("table", ["Consecutive C=C", "Example", "End planes", "Result (both ends unsymmetrical)"], [
                ["2 (even)", "allene, CH~2~=C=CHCH~3~", "perpendicular", "no cis/trans; chiral (a pair of enantiomers)"],
                ["3 (odd)", "butatriene, CH~3~CH=C=C=CHCH~3~", "coplanar", "cis/trans (E/Z) pair; achiral"],
                ["4 (even)", "pentatetraene", "perpendicular", "chiral if both ends differ"],
            ], [24, 36, 18, 22], "Table 2.11 — the odd/even rule. Count the double bonds between the two end carbons, not the atoms."),
            ("key", "Odd number of consecutive double bonds → coplanar ends → geometrical isomerism. Even number → perpendicular ends → no geometrical isomerism, but a chiral axis if both ends carry two different groups."),
            ("h2", "2.19  Why perpendicular ends give chirality, not cis/trans"),
            ("p", "Take an allene with groups a, b at one end and x, y at the other. Because the two end planes are "
                  "perpendicular, swapping a and b at one end produces a structure that cannot be superimposed on the "
                  "original — but neither can it be called cis or trans, because there is no common reference plane. The "
                  "two arrangements are mirror images, and they are not interconvertible without breaking the π system. "
                  "That is a pair of enantiomers, and the molecule has **axial chirality** with no stereocentre anywhere."),
            ("p", "If either end carries two identical groups, a mirror plane appears through the axis and the molecule "
                  "becomes achiral. So the test is: **both ends unsymmetrical, even number of double bonds → chiral.**"),
            ("h2", "2.20  Rings count as double bonds"),
            ("p", "A ring also locks a plane, so for the odd/even count **each ring is equivalent to one double bond**. A "
                  "chain such as ring–C=C–ring therefore has three units (odd) and shows cis/trans-type isomerism; "
                  "ring=C (an exocyclic double bond on a ring) has two units (even) and behaves like an allene."),
            ("bul", [
                "Ring–C=C–ring: 1 + 1 + 1 = 3 units, odd → the two rings are coplanar → geometrical isomers exist.",
                "Ring=C(R)–R′: 1 + 1 = 2 units, even → perpendicular → no geometrical isomerism.",
                "Spiro compound: the spiro atom joins two rings in perpendicular planes — the same situation as an allene.",
            ]),
            ("h2", "2.21  Spiro compounds"),
            ("p", "Two rings sharing exactly one carbon lie in **perpendicular planes**, because that carbon uses two "
                  "bonds for one ring and two for the other, and tetrahedral geometry puts those pairs at right angles. "
                  "A spiro compound therefore behaves like an allene: no geometrical isomerism, but **axial chirality** if "
                  "each ring is unsymmetrically substituted. If either ring has a mirror plane of its own through the spiro "
                  "atom, the whole molecule has a plane and is achiral."),
            ("warn", "Do not call a spiro compound “cis/trans”. There is no double bond and no common plane; the correct vocabulary is chiral/achiral, and the stereoisomers are enantiomers."),
            ("p", "The classic example is 2,2′,6,6′-tetramethylbiphenyl-3,3′-dicarboxylic acid (the “Mills–Nixon” "
                  "molecule, whose two enantiomers were resolved in 1933 — the first proof that restricted rotation alone "
                  "can generate chirality). It sits in the same chapter because the argument is the same one used for "
                  "allenes: a locked axis, two unsymmetrical ends, no plane."),
        ],
    },
    # ------------------------------------------------------------------ J-07
    {
        "id": "J-07",
        "title": "Bicyclics, fused rings and ring junctions",
        "blocks": [
            ("h2", "2.22  Two rings sharing atoms"),
            ("p", "A bicyclic compound has two rings that share at least two atoms. In a fused system the two rings share one "
                  "bond (decalin); in a bridged system they share three or more atoms (bicyclo[2.2.1]heptane). The shared "
                  "atoms are the bridgeheads, and the key stereochemical question is whether the two bridgeheads can sit on "
                  "opposite faces."),
            ("p", "At a ring junction each bridgehead carbon carries one hydrogen. If both hydrogens are on the same face "
                  "the junction is **cis**; if they are on opposite faces it is **trans**. Cis and trans junctions are "
                  "diastereomers with different energies, and at least one of them changes the shape of the whole framework."),
            ("table", ["System", "cis/trans junction?", "Why"], [
                ["bicyclo[2.2.1]heptane (norbornane)", "no", "the one-carbon bridge is too short to reach the other face"],
                ["bicyclo[2.2.2]octane", "no", "bridges still too short; only the cis junction is geometrically possible"],
                ["decalin (bicyclo[4.4.0]decane)", "yes", "six-membered rings can close on either face; both isomers are stable"],
                ["hydrindane (bicyclo[4.3.0]nonane)", "yes", "one five- and one six-membered ring"],
                ["large-ring fused systems (≥ 10 atoms)", "yes", "enough flexibility to place the bridges on opposite faces"],
            ], [40, 18, 42], "Table 2.12 — the size rule is about the whole framework, not about a single ring."),
            ("note", "A popular shortcut says “a bicyclic compound shows geometrical isomerism only if it contains a ring of eight or more atoms”. That is not reliable: decalin shows cis/trans ring junctions with six-membered rings. Decide by asking whether the two bridges can reach opposite faces, and by drawing."),
            ("h2", "2.23  cis- and trans-decalin"),
            ("p", "In cis-decalin the two junction hydrogens are on the same face. The two rings are fused in a way that lets "
                  "the framework flex; the molecule is achiral (it has a mirror plane). In trans-decalin the hydrogens are on "
                  "opposite faces and the framework is rigid — the two rings are locked. Trans-decalin is the more stable "
                  "isomer because the ring strain is lower; it is also achiral, but for a different reason: it possesses a "
                  "centre of symmetry."),
            ("p", "The pair is diastereomeric, not enantiomeric. Both cis- and trans-decalin are achiral; they differ in "
                  "stability, density and physical properties, and they can be separated by distillation."),
            ("key", "Ring-junction stereochemistry is diastereomerism, not enantiomerism. Both cis- and trans-decalin are achiral; they differ in stability, shape and physical properties, and they can be separated (distillation, crystallisation)."),
            ("h2", "2.24  How to attack a bicyclic drawing"),
            ("num", [
                "Identify the two bridgeheads.",
                "Ask whether each bridge can reach the opposite face — draw the trans attempt and see whether a bond must pass through the ring.",
                "If both junctions are possible, count 2 stereoisomers (cis and trans) before looking for enantiomers.",
                "Check each for σ and i; a cis junction often has a plane, a trans junction often removes it.",
            ]),
            ("note", "Bicyclic systems also appear in the counting questions of section 6.14, where the two bridgeheads of a rigid ring must be counted as **one** stereocentre, because flipping one without the other is impossible."),
        ],
    },
    # ------------------------------------------------------------------ J-08
    {
        "id": "J-08",
        "title": "Counting geometrical isomers",
        "blocks": [
            ("h2", "2.25  The basic count"),
            ("p", "If a molecule has n independent geometrical centres and its two ends are constitutionally different, "
                  "every centre doubles the number of arrangements and no two arrangements are related by symmetry:"),
            ("eq", 'N~geo~ = 2^n^ (dissimilar ends; n = number of qualifying centres)'),
            ("p", "The formula fails in three situations, and each has its own treatment: symmetric (similar-ended) chains, "
                  "centres that cannot give two isomers (C=C in a small ring), and centres that are coupled (cumulenes, "
                  "where the whole chain counts as one)."),
            ("h2", "2.26  Symmetric chains"),
            ("p", "For a chain whose two ends are identical, the sequence of cis/trans descriptors read from left to right is "
                  "the same molecule as the sequence read from right to left. Patterns therefore merge. Counting the "
                  "distinct sequences is a symmetry problem, and the result is:"),
            ("eq", ['n odd: N = 2^(n−1)^ + 2^((n−1)/2)^',
                    'n even: N = 2^(n−1)^ + 2^(n/2 − 1)^',
                    'both: N = (2^n^ + 2^ceil(n/2)^) / 2']),
            ("table", ["n", "Raw 2^n^", "Distinct (similar ends)", "Formula check"], [
                ["1", "2", "2", "2^0^ + 2^0^ = 2 (but-2-ene: cis and trans)"],
                ["2", "4", "3", "2^1^ + 2^0^ = 3"],
                ["3", "8", "6", "2^2^ + 2^1^ = 6"],
                ["4", "16", "10", "2^3^ + 2^1^ = 10"],
                ["5", "32", "20", "2^4^ + 2^2^ = 20"],
                ["6", "64", "36", "2^5^ + 2^2^ = 36"],
            ], [10, 16, 28, 46], "Table 2.13 — symmetric polyenes. The n = 1 row is a reminder that a single centre with identical ends is not a centre at all."),
            ("p", "Derivation for n = 2: write the two descriptors as a pair. There are four pairs: (E,E), (E,Z), (Z,E), "
                  "(Z,Z). Reading the molecule from the other end swaps the pair, so (E,Z) and (Z,E) are the same compound; "
                  "the other three (E,E), (Z,Z) and (E,Z) survive. The formula gives 2^1^ + 2^0^ = 3."),
            ("p", "Derivation for n = 3 (orbit counting): eight sequences; the end-exchange operation reverses the sequence. "
                  "Four sequences are palindromes (E,E,E), (E,Z,E), (Z,E,Z), (Z,Z,Z) — each is its own reverse — and the other "
                  "four pair up into two orbits. Total orbits = (8 + 4)/2 = 6, which is 2^2^ + 2^1^ = 6. The same argument gives "
                  "(2^n^ + 2^ceil(n/2)^)/2 in every case, so you only need to remember one formula."),
            ("warn", "When a question says “structural, geometrical and optical”, count the skeletons first. Do not multiply 2^n^ by the optical count; some geometrical isomers are meso and contribute no active forms."),
            ("h2", "2.27  The traps in the count"),
            ("num", [
                "**Terminal CH~2~ never counts.** A double bond with two H on one carbon is not a centre.",
                "**Similar ends cut the count.** Apply the symmetric formula, not 2^n^.",
                "**A cumulene counts as one centre, not one per double bond.**",
                "**A ring junction counts as one centre if cis and trans are both possible.**",
                "**Symmetrical ends merge patterns; do not use 2^n^ blindly.**",
                "**Geometrical and optical counts are separate.** A molecule may have both; the total stereoisomer count is not simply the product of the two formulas.",
            ]),
            ("h2", "2.28  Worked examples"),
            ("p", "**(a) Hexa-2,4-diene, CH~3~CH=CH–CH=CHCH~3~.** Two centres, similar ends: 2^1^ + 2^0^ = 3 isomers: (E,E), "
                  "(E,Z) = (Z,E), (Z,Z) — the last being the same as (Z,E)."),
            ("p", "**(b) Octa-2,4,6-triene.** Three centres, similar ends: 2^2^ = 4 isomers: (E,E,E), (E,E,Z), (E,Z,E), "
                  "(Z,E,E) and their reverses are identical."),
            ("p", "**(c) CH~3~CH=CH–CH~2~–CH=CHCH~3~.** Two centres, dissimilar ends: 2^2^ = 4 isomers, because (E,Z) and "
                  "(Z,E) are different compounds (the ends are not equivalent)."),
            ("p", "**(d) Hexa-2,3-tetraene (an odd cumulene).** One centre only: 2 isomers, the cis and trans forms of the "
                  "whole cumulene."),
            ("key", "If the question asks for the number of stereoisomers rather than geometrical isomers, add the optical possibilities. Sheet J-19 works through the combination systematically."),
        ],
    },
]
