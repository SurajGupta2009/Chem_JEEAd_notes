# Redox — structure source

This table is the **single source** for every structure drawing in [`../notes.md`](../notes.md).
Edit a row, then regenerate:

```
python scripts/render_structures.py Physical-Chemistry/05-Redox-Reactions/figures/structures.md
```

That rewrites `mol/<ID>.svg` (one Ketcher SVG per row: a plain image on GitHub, and a
double-click-editable structure in Obsidian with **ChemEdit**), the gallery below, and the
`smiles` block at the bottom (a live grid with the **Chem** plugin). The red numbers on each
drawing are oxidation states, **computed from the bonds**. The `Check` column is asserted on
every run, so a drawing can never disagree with the notes. Column meanings are in the script's
docstring; rulebook R18–R19.

> **Edited a structure in Ketcher?** ChemEdit saves straight into `mol/<ID>.svg`, which the next
> script run overwrites. Right-click the drawing → *Copy SMILES*, paste it into the table here,
> and rerun.

| Label | SMILES | ID | O.S. | Check | Note |
|---|---|---|---|---|---|
| H₂SO₅ Caro's acid | `OOS(=O)(=O)O` | h2so5 | auto | S=+6 O=-2,-1 | peroxide O–O: blind "O = −2" would give S +8 |
| H₂S₂O₈ Marshall's acid | `OS(=O)(=O)OOS(=O)(=O)O` | h2s2o8 | auto | S=+6 O=-2,-1 | one O–O bridge: S +6, not +7 |
| H₂S₂O₇ pyrosulphuric acid | `OS(=O)(=O)OS(=O)(=O)O` | h2s2o7 | auto | S=+6 | NCERT Ex. 7.1(g): S–O–S, no peroxide |
| CrO₅ butterfly | `O=[Cr]12(OO1)OO2` | cro5 | auto | Cr=+6 | two O–O: Cr +6, not +10 |
| Cr₂O₇²⁻ dichromate | `[O-][Cr](=O)(=O)O[Cr](=O)(=O)[O-]` | cr2o7 | auto | Cr=+6 | NCERT Ex. 7.5: Cr–O–Cr bridge |
| S₂O₃²⁻ thiosulphate | `[O-]S(=O)(=S)[O-]` | s2o3 | 1:+6 3:-2 | S~+2 S=+6,-2 | labels = the conventional JEE split; only the average +2 is unambiguous |
| S₄O₆²⁻ tetrathionate | `[O-]S(=O)(=O)SSS(=O)(=O)[O-]` | s4o6 | auto | S=+5,0 S~+5/2 | S–S bonds count 0 |
| HN₃ hydrazoic acid | `[H]N=[N+]=[N-]` | hn3 | auto | N~-1/3 N=-1,+1 | fractional average, integer atoms |
| I₃⁻ (KI₃) as I₂·I⁻ | `II.[I-]` | i3 | auto | I~-1/3 I=0,-1 | NCERT Ex. 7.2(a) |
| NH₄NO₃ | `[NH4+].[O-][N+](=O)[O-]` | nh4no3 | auto | N=-3,+5 N~+1 | two different N: the average +1 hides them |
| CaOCl₂ bleaching powder | `[Ca+2].[O-]Cl.[Cl-]` | caocl2 | auto | Cl=+1,-1 | Ca(OCl)Cl: mixed, not "Cl 0" |
| H₃PO₂ hypophosphorous | `O=P([H])([H])O` | h3po2 | auto | P=+1 | two P–H: monobasic |
| H₃PO₃ phosphorous | `OP([H])(=O)O` | h3po3 | auto | P=+3 | one P–H: dibasic |
| H₃PO₄ phosphoric | `OP(=O)(O)O` | h3po4 | auto | P=+5 | tribasic |
| H₄P₂O₅ pyrophosphorous | `OP([H])(=O)OP([H])(=O)O` | h4p2o5 | auto | P=+3 | P–O–P bridge |
| H₄P₂O₆ hypophosphoric | `OP(=O)(O)P(=O)(O)O` | h4p2o6 | auto | P=+4 | P–P bond counts 0 |
| H₄P₂O₇ pyrophosphoric | `OP(=O)(O)OP(=O)(O)O` | h4p2o7 | auto | P=+5 | NCERT Ex. 7.1(c) |
| OF₂ | `FOF` | of2 | auto | O=+2 | F always wins |
| O₂F₂ | `FOOF` | o2f2 | auto | O=+1 | O–O counts 0 |
| KO₂ superoxide | `[K+].[O-][O]` | ko2 | auto | O~-1/2 | O₂⁻ carries one unpaired electron |
| NaBH₄ | `[Na+].[BH4-]` | nabh4 | auto | B=+3 | H is −1 (hydride) |
| CH₄ methane | `C` | ch4 | auto H | C=-4 | carbon ladder, NCERT Ex. 7.7 |
| CH₃OH methanol | `CO` | ch3oh | auto H | C=-2 | carbon ladder |
| HCHO formaldehyde | `C=O` | hcho | auto H | C=0 | carbon ladder |
| HCOOH formic acid | `OC=O` | hcooh | auto H | C=+2 | carbon ladder |
| CO₂ | `O=C=O` | co2 | auto | C=+4 | carbon ladder |
| CH₃CH₂OH ethanol | `CCO` | ethanol | auto H | C=-3,-1 C~-2 | NCERT Ex. 7.2(d) |
| CH₃COOH acetic acid | `CC(=O)O` | acetic | auto H | C=-3,+3 C~0 | NCERT Ex. 7.2(e) |
| C₆H₅CH₃ toluene | `Cc1ccccc1` | toluene | show:0 | | NCERT Ex. 7.12(a): the CH₃ carbon is oxidised |
| C₆H₅COO⁻ benzoate | `[O-]C(=O)c1ccccc1` | benzoate | show:1 | | CH₃ (−3) → COO⁻ (+3): 6 e⁻ |
| hydroquinone | `Oc1ccc(O)cc1` | hydroquinone | show:1,4 | | NCERT Ex. 7.13(a): photographic developer |
| p-benzoquinone | `O=C1C=CC(=O)C=C1` | quinone | show:1,4 | | two C go +1 → +2: 2 e⁻ in total |

## Gallery (generated)

<!-- gallery:begin -->
| Structure | Species | O.S. on the drawing | Note |
|---|---|---|---|
| ![H₂SO₅ Caro's acid](mol/h2so5.svg) | H₂SO₅ Caro's acid | O −1 · S +6 | peroxide O–O: blind "O = −2" would give S +8 |
| ![H₂S₂O₈ Marshall's acid](mol/h2s2o8.svg) | H₂S₂O₈ Marshall's acid | S +6 · O −1 | one O–O bridge: S +6, not +7 |
| ![H₂S₂O₇ pyrosulphuric acid](mol/h2s2o7.svg) | H₂S₂O₇ pyrosulphuric acid | S +6 | NCERT Ex. 7.1(g): S–O–S, no peroxide |
| ![CrO₅ butterfly](mol/cro5.svg) | CrO₅ butterfly | Cr +6 · O −1 | two O–O: Cr +6, not +10 |
| ![Cr₂O₇²⁻ dichromate](mol/cr2o7.svg) | Cr₂O₇²⁻ dichromate | Cr +6 | NCERT Ex. 7.5: Cr–O–Cr bridge |
| ![S₂O₃²⁻ thiosulphate](mol/s2o3.svg) | S₂O₃²⁻ thiosulphate | S −2, +6 (avg +2) | labels = the conventional JEE split; only the average +2 is unambiguous |
| ![S₄O₆²⁻ tetrathionate](mol/s4o6.svg) | S₄O₆²⁻ tetrathionate | S 0, +5 (avg +5⁄2) | S–S bonds count 0 |
| ![HN₃ hydrazoic acid](mol/hn3.svg) | HN₃ hydrazoic acid | N −1, +1 (avg −1⁄3) | fractional average, integer atoms |
| ![I₃⁻ (KI₃) as I₂·I⁻](mol/i3.svg) | I₃⁻ (KI₃) as I₂·I⁻ | I −1, 0 (avg −1⁄3) | NCERT Ex. 7.2(a) |
| ![NH₄NO₃](mol/nh4no3.svg) | NH₄NO₃ | N −3, +5 (avg +1) | two different N: the average +1 hides them |
| ![CaOCl₂ bleaching powder](mol/caocl2.svg) | CaOCl₂ bleaching powder | Cl −1, +1 (avg 0) | Ca(OCl)Cl: mixed, not "Cl 0" |
| ![H₃PO₂ hypophosphorous](mol/h3po2.svg) | H₃PO₂ hypophosphorous | P +1 | two P–H: monobasic |
| ![H₃PO₃ phosphorous](mol/h3po3.svg) | H₃PO₃ phosphorous | P +3 | one P–H: dibasic |
| ![H₃PO₄ phosphoric](mol/h3po4.svg) | H₃PO₄ phosphoric | P +5 | tribasic |
| ![H₄P₂O₅ pyrophosphorous](mol/h4p2o5.svg) | H₄P₂O₅ pyrophosphorous | P +3 | P–O–P bridge |
| ![H₄P₂O₆ hypophosphoric](mol/h4p2o6.svg) | H₄P₂O₆ hypophosphoric | P +4 | P–P bond counts 0 |
| ![H₄P₂O₇ pyrophosphoric](mol/h4p2o7.svg) | H₄P₂O₇ pyrophosphoric | P +5 | NCERT Ex. 7.1(c) |
| ![OF₂](mol/of2.svg) | OF₂ | F −1 · O +2 | F always wins |
| ![O₂F₂](mol/o2f2.svg) | O₂F₂ | F −1 · O +1 | O–O counts 0 |
| ![KO₂ superoxide](mol/ko2.svg) | KO₂ superoxide | O −1, 0 | O₂⁻ carries one unpaired electron |
| ![NaBH₄](mol/nabh4.svg) | NaBH₄ | B +3 | H is −1 (hydride) |
| ![CH₄ methane](mol/ch4.svg) | CH₄ methane | C −4 | carbon ladder, NCERT Ex. 7.7 |
| ![CH₃OH methanol](mol/ch3oh.svg) | CH₃OH methanol | C −2 | carbon ladder |
| ![HCHO formaldehyde](mol/hcho.svg) | HCHO formaldehyde | C 0 | carbon ladder |
| ![HCOOH formic acid](mol/hcooh.svg) | HCOOH formic acid | C +2 | carbon ladder |
| ![CO₂](mol/co2.svg) | CO₂ | C +4 | carbon ladder |
| ![CH₃CH₂OH ethanol](mol/ethanol.svg) | CH₃CH₂OH ethanol | C −3, −1 (avg −2) | NCERT Ex. 7.2(d) |
| ![CH₃COOH acetic acid](mol/acetic.svg) | CH₃COOH acetic acid | C −3, +3 (avg 0) | NCERT Ex. 7.2(e) |
| ![C₆H₅CH₃ toluene](mol/toluene.svg) | C₆H₅CH₃ toluene | C −3 | NCERT Ex. 7.12(a): the CH₃ carbon is oxidised |
| ![C₆H₅COO⁻ benzoate](mol/benzoate.svg) | C₆H₅COO⁻ benzoate | C +3 | CH₃ (−3) → COO⁻ (+3): 6 e⁻ |
| ![hydroquinone](mol/hydroquinone.svg) | hydroquinone | C +1 | NCERT Ex. 7.13(a): photographic developer |
| ![p-benzoquinone](mol/quinone.svg) | p-benzoquinone | C +2 | two C go +1 → +2: 2 e⁻ in total |
<!-- gallery:end -->

## Live structures for the Chem plugin (generated)

<!-- smiles:begin -->
```smiles
OOS(=O)(=O)O
OS(=O)(=O)OOS(=O)(=O)O
OS(=O)(=O)OS(=O)(=O)O
O=[Cr]12(OO1)OO2
[O-][Cr](=O)(=O)O[Cr](=O)(=O)[O-]
[O-]S(=O)(=S)[O-]
[O-]S(=O)(=O)SSS(=O)(=O)[O-]
[H]N=[N+]=[N-]
II.[I-]
[NH4+].[O-][N+](=O)[O-]
[Ca+2].[O-]Cl.[Cl-]
O=P([H])([H])O
OP([H])(=O)O
OP(=O)(O)O
OP([H])(=O)OP([H])(=O)O
OP(=O)(O)P(=O)(O)O
OP(=O)(O)OP(=O)(O)O
FOF
FOOF
[K+].[O-][O]
[Na+].[BH4-]
C
CO
C=O
OC=O
O=C=O
CCO
CC(=O)O
Cc1ccccc1
[O-]C(=O)c1ccccc1
Oc1ccc(O)cc1
O=C1C=CC(=O)C=C1
```
<!-- smiles:end -->
