# p-Block Groups 15-18 — structure source

This table is the **single source** for every structure drawing in [`../notes.md`](../notes.md).
Edit a row, then regenerate:

```bash
python scripts/render_structures.py Inorganic-Chemistry/09-The-p-Block-Elements/figures/structures.md
```

| Label | SMILES | ID | O.S. | Check | Note |
|---|---|---|---|---|---|
| Ammonia NH₃ | N | nh3 | auto | N=-3 | pyramidal 107.8° |
| White phosphorus P₄ | P12P3P1P23 | p4 | auto | P=0 | tetrahedral 60° strained |
| Phosphine PH₃ | P | ph3 | auto | P=-3 | pyramidal 93.6° |
| Phosphorus trichloride PCl₃ | ClP(Cl)Cl | pcl3 | auto | P=+3 | pyramidal |
| Phosphorus pentachloride PCl₅ | ClP(Cl)(Cl)(Cl)Cl | pcl5 | auto | P=+5 | trigonal bipyramidal |
| Phosphorus trioxide P₄O₆ | O1P2OP3OP1OP2O3 | p4o6 | auto | P=+3 | adamantane 6 P-O-P |
| Phosphorus pentoxide P₄O₁₀ | O=P12OP3OP(=O)OP1OP2O3 | p4o10 | auto | P=+5 | 4 P=O + 6 P-O-P |
| Hypophosphorous acid H₃PO₂ | O=PO | h3po2 | auto | P=+1 | 2 P-H monobasic |
| Phosphorous acid H₃PO₃ | OP(O)O | h3po3 | auto | P=+3 | 1 P-H dibasic |
| Phosphoric acid H₃PO₄ | OP(O)(O)O | h3po4 | auto | P=+5 | tribasic PO(OH)3 |
| Nitrous oxide N₂O | [N-]=[N+]=O | n2o | auto | N=+1 avg | linear N-N-O |
| Nitric oxide NO | [N]=O | no | auto | N=+2 | paramagnetic odd e- |
| Nitrogen dioxide NO₂ | [N](=O)[O] | no2 | auto | N=+4 | angular odd e- dimerises |
| Dinitrogen pentoxide N₂O₅ | O=[N+]([O-])O[N+](=O)[O-] | n2o5 | auto | N=+5 | O2N-O-NO2 |
| Nitric acid HNO₃ | O[N+](=O)O | hno3 | auto | N=+5 | planar HO-NO2 |
| Ozone O₃ | O=[O+][O-] | o3 | auto | O=0 avg | bent 117° resonance |
| Sulphur dioxide SO₂ | O=S=O | so2 | auto | S=+4 | angular 119.5° |
| Sulphur trioxide SO₃ | O=S(=O)=O | so3 | auto | S=+6 | trigonal planar |
| Sulphuric acid H₂SO₄ | OS(O)(=O)=O | h2so4 | auto | S=+6 | tetrahedral (HO)2SO2 |
| Thiosulphuric acid H₂S₂O₃ | OS(=O)(=S)O | h2s2o3 | auto | S=+5,-2 | one S replaces O |
| Peroxodisulphuric acid H₂S₂O₈ | OS(=O)(=O)OOS(=O)(=O)O | h2s2o8 | auto | S=+6 | O-O Marshall |
| Chlorine monofluoride ClF | FCl | clf | auto | Cl=+1 | linear interhalogen |
| Chlorine trifluoride ClF₃ | FCl(F)F | clf3 | auto | Cl=+3 | T-shaped |
| Bromine pentafluoride BrF₅ | FBr(F)(F)(F)F | brf5 | auto | Br=+5 | square pyramidal |
| Iodine heptafluoride IF₇ | F[I](F)(F)(F)(F)(F)F | if7 | auto | I=+7 | pentagonal bipyramidal |
| Hypochlorous acid HOCl | OCl | hocl | auto | Cl=+1 | HO-Cl |
| Perchloric acid HClO₄ | OCl(=O)(=O)O | hclo4 | auto | Cl=+7 | tetrahedral HO-ClO3 |
| Xenon difluoride XeF₂ | F[Xe]F | xef2 | auto | Xe=+2 | linear sp3d 3lp eq |
| Xenon tetrafluoride XeF₄ | F[Xe](F)(F)F | xef4 | auto | Xe=+4 | square planar sp3d2 2lp axial |
| Xenon hexafluoride XeF₆ | F[Xe](F)(F)(F)(F)F | xef6 | auto | Xe=+6 | distorted octahedral sp3d3 1lp |
| Xenon trioxide XeO₃ | O=[Xe](=O)=O | xeo3 | auto | Xe=+6 | pyramidal sp3 1lp |
| Xenon oxytetrafluoride XeOF₄ | O=[Xe](F)(F)(F)F | xeof4 | auto | Xe=+6 | square pyramidal sp3d2 |

<!-- gallery:begin -->
| ID | Structure | Label |
|---|---|---|
| nh3 | ![nh3](mol/nh3.svg) | Ammonia NH₃ |
| p4 | ![p4](mol/p4.svg) | White phosphorus P₄ |
| ph3 | ![ph3](mol/ph3.svg) | Phosphine PH₃ |
| pcl3 | ![pcl3](mol/pcl3.svg) | Phosphorus trichloride PCl₃ |
| pcl5 | ![pcl5](mol/pcl5.svg) | Phosphorus pentachloride PCl₅ |
| p4o6 | ![p4o6](mol/p4o6.svg) | Phosphorus trioxide P₄O₆ |
| p4o10 | ![p4o10](mol/p4o10.svg) | Phosphorus pentoxide P₄O₁₀ |
| h3po2 | ![h3po2](mol/h3po2.svg) | Hypophosphorous acid H₃PO₂ |
| h3po3 | ![h3po3](mol/h3po3.svg) | Phosphorous acid H₃PO₃ |
| h3po4 | ![h3po4](mol/h3po4.svg) | Phosphoric acid H₃PO₄ |
| n2o | ![n2o](mol/n2o.svg) | Nitrous oxide N₂O |
| no | ![no](mol/no.svg) | Nitric oxide NO |
| no2 | ![no2](mol/no2.svg) | Nitrogen dioxide NO₂ |
| n2o5 | ![n2o5](mol/n2o5.svg) | Dinitrogen pentoxide N₂O₅ |
| hno3 | ![hno3](mol/hno3.svg) | Nitric acid HNO₃ |
| o3 | ![o3](mol/o3.svg) | Ozone O₃ |
| so2 | ![so2](mol/so2.svg) | Sulphur dioxide SO₂ |
| so3 | ![so3](mol/so3.svg) | Sulphur trioxide SO₃ |
| h2so4 | ![h2so4](mol/h2so4.svg) | Sulphuric acid H₂SO₄ |
| hocl | ![hocl](mol/hocl.svg) | Hypochlorous acid HOCl |
| hclo4 | ![hclo4](mol/hclo4.svg) | Perchloric acid HClO₄ |
| xef2 | ![xef2](mol/xef2.svg) | Xenon difluoride XeF₂ |
| xef4 | ![xef4](mol/xef4.svg) | Xenon tetrafluoride XeF₄ |
| xef6 | ![xef6](mol/xef6.svg) | Xenon hexafluoride XeF₆ |
| xeo3 | ![xeo3](mol/xeo3.svg) | Xenon trioxide XeO₃ |
| xeof4 | ![xeof4](mol/xeof4.svg) | Xenon oxytetrafluoride XeOF₄ |
<!-- gallery:end -->

<!-- smiles:begin -->
```smiles
N nh3 Ammonia NH₃
P12P3P1P23 p4 White phosphorus P₄
P ph3 Phosphine PH₃
ClP(Cl)Cl pcl3 Phosphorus trichloride PCl₃
ClP(Cl)(Cl)(Cl)Cl pcl5 Phosphorus pentachloride PCl₅
O1P2OP3OP1OP2O3 p4o6 Phosphorus trioxide P₄O₆
O=P12OP3OP(=O)OP1OP2O3 p4o10 Phosphorus pentoxide P₄O₁₀
O=PO h3po2 Hypophosphorous acid H₃PO₂
OP(O)O h3po3 Phosphorous acid H₃PO₃
OP(O)(O)O h3po4 Phosphoric acid H₃PO₄
[N-]=[N+]=O n2o Nitrous oxide N₂O
[N]=O no Nitric oxide NO
[N](=O)[O] no2 Nitrogen dioxide NO₂
O=[N+]([O-])O[N+](=O)[O-] n2o5 Dinitrogen pentoxide N₂O₅
O[N+](=O)O hno3 Nitric acid HNO₃
O=[O+][O-] o3 Ozone O₃
O=S=O so2 Sulphur dioxide SO₂
O=S(=O)=O so3 Sulphur trioxide SO₃
OS(O)(=O)=O h2so4 Sulphuric acid H₂SO₄
OCl hocl Hypochlorous acid HOCl
OCl(=O)(=O)O hclo4 Perchloric acid HClO₄
F[Xe]F xef2 Xenon difluoride XeF₂
F[Xe](F)(F)F xef4 Xenon tetrafluoride XeF₄
F[Xe](F)(F)(F)(F)F xef6 Xenon hexafluoride XeF₆
O=[Xe](=O)=O xeo3 Xenon trioxide XeO₃
O=[Xe](F)(F)(F)F xeof4 Xenon oxytetrafluoride XeOF₄
```
<!-- smiles:end -->
