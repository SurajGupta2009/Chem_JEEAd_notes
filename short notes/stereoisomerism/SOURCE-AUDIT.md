# Source audit

What the source is, what was taken from it, where it contradicts itself, what was
corrected, and what remains uncertain. Nothing here is a claim that the chemistry has been
exhaustively verified.

## 1. The source

* **File:** `source/NS-Sir-Stereoisomerism-Complete-Notes.md` — 184,490 bytes, 2,355 lines.
* **What it claims to be:** a word-for-word reproduction of 57 lecture notes from a
  Stereoisomerism course (NS Sir, Mohit Tyagi channel / Competishun), each with a video id,
  duration and watch link. The header says so explicitly; this audit takes that claim at
  face value but did not verify it.
* **What was available:** the markdown only. The 57 videos were **not** watched, the
  embedded YouTube links were not opened, and no textbook edition was consulted. Any
  “standard value” below is a textbook range recalled from general chemistry knowledge, not
  a quotation from a named edition.
* **What was not available:** the source's own figures and hand-drawn structures (the
  notes describe them in words); the individual `lectures/NN-*.md` files the compilation
  refers to; any errata.

The chapter follows the source's **sequence and emphasis** but not its wording. Sheet
prose was written fresh; the boxes labelled "as the lecture puts it" paraphrase the
lecture's claim, they do not quote it. There are no quotation marks around source text
anywhere in the set, because none was copied verbatim.

## 2. Conflicts found inside the source

Each item below is a place where two parts of the source disagree, or where the source
disagrees with standard chemistry. The right-hand column is what the sheets do.

| # | Where | The conflict | Resolution used |
|---|---|---|---|
| 1 | Lec 6 table vs Lec 39 §2 | Lec 6: **even** number of consecutive C=C (allene, 2) → perpendicular end groups → optical isomerism. Lec 39: perpendicular when the number is **odd**, coplanar when even. | Followed **Lec 6**. Allene (2 C=C) is chiral; buta-1,2,3-triene (3 C=C) has coplanar ends and shows cis/trans. The parity label in Lec 39 is inverted; its chemistry (allene chiral) agrees with Lec 6, so only the label is wrong. X-02 extends the correct parity to five cumulative double bonds. |
| 2 | Lec 11 §1 | First sentence: “Number of geometrical isomers = 2ⁿ”, immediately followed by “Applies only to similar-ended chains” — which is exactly the case where 2ⁿ overcounts. | Treated 2ⁿ as the **dissimilar-ended** rule and the symmetry-corrected formula as the similar-ended rule. Both are on J-08 with the derivation, and X-07 derives the same result by orbit counting. |
| 3 | Lec 11 Example 2 | A two-centre symmetric diene (n = 2, even) gives 3 isomers, justified as “2²⁻¹ + 2⁰ = 3 ✓ (matches the odd/even formula)”. 2²⁻¹ + 2⁰ is the **odd-n** formula; the even-n formula is 2ⁿ⁻¹ + 2^((n−2)/2), which also equals 3. | The answer 3 is right; the justification in the source is the wrong branch. J-08 states the branch conditions explicitly and checks both n = 2 and n = 3 against the ladder 2, 3, 6, 10, 20, 36. |
| 4 | Lec 7 (bicyclics) | “geometrical isomerism at a ring junction only when a bridge/ring is large enough (≥ 8-membered ring equivalent) to be trans; small bridged systems are locked cis.” | Rejected as a general rule: **trans-decalin** is a fused 6,6 system with a genuine trans junction, and norbornane-type cages have fixed geometries that are neither cis nor trans in the alkene sense. J-07 and X-03 replace the shortcut with “draw the cage and check whether the two substituents can be on opposite faces”; the ≥ 8 ring-size limit is kept only for **trans-cycloalkenes** (X-03), where it belongs. |
| 5 | Lec 13 §2 vs key takeaway 3 | “fumaric (trans) has the higher boiling point — the standard JEE exception”, with the mechanism given as intermolecular H-bonding in fumaric acid. | Kept the **comparison** (maleic has the intramolecular H-bond, fumaric does not) but replaced the boiling-point claim. Fumaric acid sublimes and decomposes near 200 °C; it has no clean normal boiling point, so “higher bp” is not a safe exam answer. J-09 uses the melting point (fumaric ≈ 287 °C with decomposition, maleic ≈ 135 °C) and the solubility difference, and carries an explicit warning against extending the reversal to other cis/trans pairs. |
| 6 | Lec 3 §2 | Names maleic acid “but-2-ene-1,4-dioic acid”. The 1,4 locants double-count the carboxyl carbons. | Corrected to **but-2-enedioic acid** (maleic = Z, fumaric = E). Logged here rather than silently changed. |
| 7 | Lec 10 §2 | “(Z)-but-2-ene dioic acid type names” — a descriptive fragment, not an IUPAC name. | Not used as a name on any sheet; J-04 teaches the descriptor-plus-locant form. |
| 8 | Lec 6 §3 | Spiro “behaves like an allene (even number of double bonds)” although a spiro carbon has no double bond at all. | Kept the **geometry** (perpendicular rings) and dropped the “even number of double bonds” phrasing; X-02 and J-06 say the spiro carbon is the axis analogue, not a cumulene. |

## 3. Corrections made to the sheets during the audit

These are errors in this chapter's own first draft, found by re-reading the pages against
the counting rules. They are listed because the set is meant to be trustworthy, not because
the source caused them.

| Where | Was | Now | Why |
|---|---|---|---|
| Table 3.13, trihydroxyglutaric acid | 8 total (6 active + 2 meso) | 4 total (2 active + 2 meso) | HOOC–CH(OH)–CH(OH)–CH(OH)–COOH has similar ends and n = 3 odd: active = 2² − 2¹ = 2, meso = 2¹ = 2. |
| X-10 problem 8 | “n = 3 with similar ends: active 6, meso 2” | active 2, meso 2, total 4, with the pseudoasymmetric pair named | same error, same fix; the two meso forms (R,r,S) and (R,s,S) are diastereomers, not one compound. |
| X-03 §6.14 | worked claim “n = 3 stereoisomers” for 2,5-disubstituted norbornane | “draw the cage, do not quote n” | the naive 2ⁿ count is not valid in a rigid cage; no numeric answer is defensible without drawing every case. |
| X-07 table | “(8 + 4)/2 → 6 = 4 active + 2 meso?” (a question mark left in the table) | “8 strings → 4: 2 active + 2 meso (pseudoasymmetric)” | the odd-n row of the orbit count is 4, and the table must agree with Table 3.13. |
| extra block on J-04 | table numbered 2.5b | renumbered 2.7 | 2.5b was already used on J-05; the whole chapter was later renumbered in reading order (see §3a). |

### 3a. Manual numbering

After the corrections above, every chapter (2, 3, 4, 5, 6) had its table numbers reassigned
**in reading order**, so a reader never meets Table 6.10 before Table 6.9b, and no lettered
suffix is needed. Section numbers keep their lettered “b” continuations because those are
genuine insertions after a named section; table numbers no longer need them. The one
cross-reference in the text (“see Table 3.12 (J-19)”) was updated with the renumbering and
is checked by `checks/verify.py` indirectly, through the uniqueness of all table numbers.

## 4. What was checked, and how

**Machine-checked** (`python3 checks/verify.py`, all passing at the last run): every
promised file exists; the two part PDFs are A4 and their page counts equal the planner's;
the combined PDF has both parts in order with one bookmark per sheet; all 67 PNGs are
2480 × 3508 at 300 dpi with parseable names and contiguous page numbers; one thumbnail per
PNG; each ZIP opens, passes its CRC test and contains exactly the expected entries; every
PNG is linked from `index.html`; every page carries its part, sheet id and page label;
table numbers are unique within each part and section numbers sit in the right chapter.

**Read by hand:** every sheet was read for the argument, not just the arithmetic. The
counting results on J-08, J-19, X-07 and X-10 were recomputed from the formulas and, where
small enough, enumerated by hand (tartaric acid 3; the C₅H₁₁Cl set; the n = 1…6 ladder).
The Burnside identity N = (2ⁿ + 2^⌈n/2⌉)/2 was checked against the ladder for n = 1…6 and
against the tartaric-acid case. The cis/trans × syn/anti table on J-26 and X-06 was checked
on all four combinations.

**Spot-checked:** numerical values were compared with standard textbook ranges and are
quoted as ranges or with “≈”, never as measured data. Deliberately approximate:
C=C rotation barrier 250–270 kJ mol⁻¹, ethane 12.5 (≈12.1 in modern measurements),
gauche CH₃/CH₃ 3.8, chair → twist-boat ≈23, ring flip ≈45, A(CH₃) 7.3, A(t-Bu) ≈20,
biphenyl ortho-substituted barrier 80–160 kJ mol⁻¹, trans-cyclooctene ≈50 kJ mol⁻¹ above
cis, RT at 298 K = 2.48 kJ mol⁻¹.

## 5. What remains uncertain

Stated plainly so that nothing here is over-claimed:

1. **The source's provenance is unverified.** The compilation says it reproduces 57 videos
   word for word. It was not compared with the videos, and the individual lecture files it
   cites were not available.
2. **No edition of any textbook was checked.** Statements such as “standard value” or
   “textbooks give” are generic, not citations. No page numbers, editions or quotations are
   claimed anywhere.
3. **syn/anti for C=N and N=N** is used in the source's sense: *syn* = the two groups on the
   same side of the C=N (or N=N) bond. Some books define it relative to the lone pair
   instead, which flips the labels for oximes. The sheets say which convention they use;
   an exam that uses the other one will expect the opposite word for the same drawing.
4. **CIP rules for axes and planes** (allenes, biphenyls) are summarised at the level JEE
   needs: the sheet tells you to assign the axis by the two groups at each end and to use
   the aR/aS convention, but the full sequence-rule formalities for axes (Rule 5) are not
   reproduced. A question that asks for a full aR/aS name with a long substituent chain is
   beyond what the sheets prove.
5. **A-values and Boltzmann numbers** are rounded textbook values at 298 K. The
   anomeric-effect explanation is given as a stabilising stereoelectronic preference, not
   with a quantitative energy, because the numbers vary strongly with solvent.
6. **Reaction stereochemistry** (J-25, J-26, X-06) is presented as the examinable pattern,
   not as a mechanistic study: no rate data, no stereochemical excess for specific
   substrates, no solvent-effect table. “S<sub>N</sub>2 gives inversion” is a rule with
   known exceptions (e.g. neighbouring-group participation), which the sheets flag but do
   not enumerate.
7. **Structures were drawn with the chapter's own vector primitives**, not with a
   chemical drawing package. Tetrahedral centres, chairs, Fischer and Newman projections
   were checked by eye for connectivity and for correct up/down relationships, but the set
   was not round-tripped through a molecular editor or a structure validator. A bond that
   looks like a wedge is a drawing decision, not a crystallographic fact.
8. **No claim is made that every JEE Advanced question type is covered.** The set is
   complete against the source and against the topics listed in `SCOPE.md`; a paper that
   invents a new combination still has to be answered by drawing.

## 6. Where each correction is visible

| Correction | Sheet |
|---|---|
| allene/cumulene parity | J-06, J-18, X-02 |
| 2ⁿ vs symmetry-corrected counting | J-08, X-07 |
| trihydroxyglutaric acid count | J-19 (Table 3.13), X-10 |
| fumaric acid boiling point | J-09 |
| but-2-enedioic acid naming | J-09 |
| bicyclic “≥ 8-membered ring” shortcut | J-07, X-03 |
| norbornane counting | X-03 |
| syn/anti convention | J-03, J-17, X-12 |
| CIP for axes, what is not covered | X-02, X-12 |
