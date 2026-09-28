# s-Block — structure source

This table is the **single source** for every structure drawing in [`../notes.md`](../notes.md).
Edit a row, then regenerate:

```bash
python scripts/render_structures.py Inorganic-Chemistry/04-The-s-Block-Elements/figures/structures.md
```

| Label | SMILES | ID | O.S. | Check | Note |
|---|---|---|---|---|---|
| Sodium oxide Na₂O | `[Na+].[Na+].[O-2]` | na2o | auto | Na=+1 O=-2 | normal oxide Li2O type |
| Sodium peroxide Na₂O₂ | `[Na+].[Na+].[O-][O-]` | na2o2 | auto | Na=+1 O=-1 | peroxide O-O |
| Potassium superoxide KO₂ | `[K+].[O-][O]` | ko2 | auto | K=+1 O=-1,0 O~-1/2 | superoxide: one unpaired e⁻, O at −1 and 0 |
| Sodium hydroxide NaOH | `[Na+].[OH-]` | naoh | auto | Na=+1 | strong base |
| Calcium oxide CaO | `[Ca+2].[O-2]` | cao | auto | Ca=+2 O=-2 | quick lime basic |
| Calcium hydroxide Ca(OH)₂ | `[Ca+2].[OH-].[OH-]` | caoh2 | auto | Ca=+2 | slaked lime |
| Calcium carbonate CaCO₃ | `[Ca+2].[O-]C([O-])=O` | caco3 | auto | Ca=+2 C=+4 | limestone |
| Calcium sulphate CaSO₄ | `[Ca+2].[O-]S([O-])(=O)=O` | caso4 | auto | Ca=+2 S=+6 | gypsum |
| Magnesium chloride MgCl₂ | `[Mg+2].[Cl-].[Cl-]` | mgcl2 | auto | Mg=+2 | ionic |
| Beryllium chloride BeCl₂ chain | `Cl[Be]Cl` | becl2 | auto | Be=+2 | covalent chain solid dimer vapour |
| Beryllium oxide BeO | `[Be+2].[O-2]` | beo | auto | Be=+2 O=-2 | amphoteric |
| Sodium carbonate Na₂CO₃ | `[Na+].[Na+].[O-]C([O-])=O` | na2co3 | auto | C=+4 | Solvay product |
| Sodium bicarbonate NaHCO₃ | `[Na+].OC(=O)[O-]` | nahco3 | auto | C=+4 | baking soda |
| Lithium nitride Li₃N | `[Li+].[Li+].[Li+].[N-3]` | li3n | auto | Li=+1 N=-3 | Li + N2 only alkali nitride |
| Magnesium nitride Mg₃N₂ | `[Mg+2].[Mg+2].[Mg+2].[N-3].[N-3]` | mg3n2 | auto | Mg=+2 N=-3 | Mg + N2 |

<!-- gallery:begin -->
| Structure | Species | O.S. on the drawing | Note |
|---|---|---|---|
| ![Sodium oxide Na₂O](mol/na2o.svg) | Sodium oxide Na₂O | — | normal oxide Li2O type |
| ![Sodium peroxide Na₂O₂](mol/na2o2.svg) | Sodium peroxide Na₂O₂ | O −1 | peroxide O-O |
| ![Potassium superoxide KO₂](mol/ko2.svg) | Potassium superoxide KO₂ | O −1, 0 | superoxide: one unpaired e⁻, O at −1 and 0 |
| ![Sodium hydroxide NaOH](mol/naoh.svg) | Sodium hydroxide NaOH | — | strong base |
| ![Calcium oxide CaO](mol/cao.svg) | Calcium oxide CaO | — | quick lime basic |
| ![Calcium hydroxide Ca(OH)₂](mol/caoh2.svg) | Calcium hydroxide Ca(OH)₂ | — | slaked lime |
| ![Calcium carbonate CaCO₃](mol/caco3.svg) | Calcium carbonate CaCO₃ | C +4 | limestone |
| ![Calcium sulphate CaSO₄](mol/caso4.svg) | Calcium sulphate CaSO₄ | S +6 | gypsum |
| ![Magnesium chloride MgCl₂](mol/mgcl2.svg) | Magnesium chloride MgCl₂ | Cl −1 | ionic |
| ![Beryllium chloride BeCl₂ chain](mol/becl2.svg) | Beryllium chloride BeCl₂ chain | Cl −1 · Be +2 | covalent chain solid dimer vapour |
| ![Beryllium oxide BeO](mol/beo.svg) | Beryllium oxide BeO | Be +2 | amphoteric |
| ![Sodium carbonate Na₂CO₃](mol/na2co3.svg) | Sodium carbonate Na₂CO₃ | C +4 | Solvay product |
| ![Sodium bicarbonate NaHCO₃](mol/nahco3.svg) | Sodium bicarbonate NaHCO₃ | C +4 | baking soda |
| ![Lithium nitride Li₃N](mol/li3n.svg) | Lithium nitride Li₃N | N −3 | Li + N2 only alkali nitride |
| ![Magnesium nitride Mg₃N₂](mol/mg3n2.svg) | Magnesium nitride Mg₃N₂ | N −3 | Mg + N2 |
<!-- gallery:end -->

<!-- smiles:begin -->
```smiles
[Na+].[Na+].[O-2]
[Na+].[Na+].[O-][O-]
[K+].[O-][O]
[Na+].[OH-]
[Ca+2].[O-2]
[Ca+2].[OH-].[OH-]
[Ca+2].[O-]C([O-])=O
[Ca+2].[O-]S([O-])(=O)=O
[Mg+2].[Cl-].[Cl-]
Cl[Be]Cl
[Be+2].[O-2]
[Na+].[Na+].[O-]C([O-])=O
[Na+].OC(=O)[O-]
[Li+].[Li+].[Li+].[N-3]
[Mg+2].[Mg+2].[Mg+2].[N-3].[N-3]
```
<!-- smiles:end -->
