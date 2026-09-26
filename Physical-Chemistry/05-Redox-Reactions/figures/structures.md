# Redox — structure source (the species whose O.S. needs a drawing)

This file is the **single source** for the structure drawings in [`../notes.md`](../notes.md) §5.
Edit the table, then regenerate:

```
python scripts/render_structures.py Physical-Chemistry/05-Redox-Reactions/figures/structures.md
```

That rewrites [`structures.svg`](structures.svg) (embedded in the notes; renders on GitHub and
in Obsidian with no plugin) and the `smiles` block at the bottom of this file (rendered live by
the Obsidian **Chem** plugin, `chem`). Rulebook R18 rungs 4–5, fallback per R19.

| Label | SMILES | Note |
|---|---|---|
| H₂SO₅ Caro's acid | OOS(=O)(=O)O | S +6 · one O–O |
| H₂S₂O₈ Marshall's acid | OS(=O)(=O)OOS(=O)(=O)O | S +6 · one O–O |
| CrO₅ butterfly | O=[Cr]12(OO1)OO2 | Cr +6 · two O–O |
| S₂O₃²⁻ thiosulphate | [O-]S(=O)(=S)[O-] | S +6 / −2 (avg +2) |
| S₄O₆²⁻ tetrathionate | [O-]S(=O)(=O)SSS(=O)(=O)[O-] | S +5,0,0,+5 (avg +2.5) |
| HN₃ hydrazoic acid | [H]N=[N+]=[N-] | N avg −⅓ |
| H₃PO₂ hypophosphorous | O[PH2]=O | P +1 · monobasic |
| H₃PO₃ phosphorous | O[PH](=O)O | P +3 · dibasic |
| H₄P₂O₅ pyrophosphorous | O[PH](=O)O[PH](=O)O | P +3 · P–O–P |
| H₄P₂O₆ hypophosphoric | OP(=O)(O)P(=O)(O)O | P +4 · P–P bond |
| NH₄NO₃ | [NH4+].[O-][N+](=O)[O-] | N −3 and +5 |
| CaOCl₂ bleaching powder | [Ca+2].[O-]Cl.[Cl-] | Cl +1 and −1 |

<!-- smiles:begin -->
```smiles
OOS(=O)(=O)O
OS(=O)(=O)OOS(=O)(=O)O
O=[Cr]12(OO1)OO2
[O-]S(=O)(=S)[O-]
[O-]S(=O)(=O)SSS(=O)(=O)[O-]
[H]N=[N+]=[N-]
O[PH2]=O
O[PH](=O)O
O[PH](=O)O[PH](=O)O
OP(=O)(O)P(=O)(O)O
[NH4+].[O-][N+](=O)[O-]
[Ca+2].[O-]Cl.[Cl-]
```
<!-- smiles:end -->
