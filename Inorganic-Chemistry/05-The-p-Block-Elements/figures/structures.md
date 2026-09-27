# p-Block Groups 13-14 — structure source

This table is the **single source** for every structure drawing in [`../notes.md`](../notes.md).
Edit a row, then regenerate:

```bash
python scripts/render_structures.py Inorganic-Chemistry/05-The-p-Block-Elements/figures/structures.md
```

| Label | SMILES | ID | O.S. | Check | Note |
|---|---|---|---|---|---|
| Boron trifluoride BF₃ | FB(F)F | bf3 | auto | B=+3 | trigonal planar, Lewis acid |
| Boron trichloride BCl₃ | ClB(Cl)Cl | bcl3 | auto | B=+3 | trigonal planar |
| Aluminium chloride dimer Al₂Cl₆ | Cl[Al](Cl)Cl[Al](Cl)Cl | al2cl6 | auto | Al=+3 | halogen bridged dimer tetrahedral |
| Diborane B₂H₆ | [BH2]1[H][BH2][H]1 | b2h6 | auto | B=+3 | banana bonds 2c-2e + 3c-2e |
| Boric acid H₃BO₃ | OB(O)O | h3bo3 | auto | B=+3 | layered H-bonded BO3 triangles |
| Borax anion [B₄O₅(OH)₄]²⁻ | O[B-]1OB2OB(O)OB(O2)O1 | borax | auto | B=+3 | tetranuclear actual borax |
| Borazine B₃N₃H₆ | B1NBNBN1 | borazine | auto | B=+3 N=-3 | inorganic benzene planar |
| Boron nitride BN | B#N | bn | auto | B=+3 N=-3 | hexagonal graphite-like |
| Carbon monoxide CO | [C-]#[O+] | co | auto | C=+2 | :C≡O: 112.8 pm toxic |
| Carbon dioxide CO₂ | O=C=O | co2 | auto | C=+4 | linear 115 pm |
| Silicon dioxide SiO₂ | O=[Si]=O | sio2 | auto | Si=+4 | 3D tetrahedral network quartz |
| Silicon tetrachloride SiCl₄ | [Si](Cl)(Cl)(Cl)Cl | sicl4 | auto | Si=+4 | tetrahedral hydrolysed |
| Silicate tetrahedron SiO₄⁴⁻ | [Si]([O-])([O-])([O-])[O-] | sio4 | auto | Si=+4 | basic unit |
| Methane CH₄ | C | ch4 | auto | C=-4 | tetrahedral |
| Silane SiH₄ | [SiH4] | sih4 | auto | Si=-4 | tetrahedral |
| Graphite fragment C₆ | c1ccccc1 | benzene | - | - | sp2 hexagonal layer model |
| Fullerene C60 fragment | c1ccccc1 | c60frag | - | - | truncated icosahedron model |

<!-- gallery:begin -->
| ID | Structure | Label |
|---|---|---|
| bf3 | ![bf3](mol/bf3.svg) | Boron trifluoride BF₃ |
| bcl3 | ![bcl3](mol/bcl3.svg) | Boron trichloride BCl₃ |
| al2cl6 | ![al2cl6](mol/al2cl6.svg) | Aluminium chloride dimer Al₂Cl₆ |
| b2h6 | ![b2h6](mol/b2h6.svg) | Diborane B₂H₆ |
| h3bo3 | ![h3bo3](mol/h3bo3.svg) | Boric acid H₃BO₃ |
| borax | ![borax](mol/borax.svg) | Borax anion [B₄O₅(OH)₄]²⁻ |
| borazine | ![borazine](mol/borazine.svg) | Borazine B₃N₃H₆ |
| bn | ![bn](mol/bn.svg) | Boron nitride BN |
| co | ![co](mol/co.svg) | Carbon monoxide CO |
| co2 | ![co2](mol/co2.svg) | Carbon dioxide CO₂ |
| sio2 | ![sio2](mol/sio2.svg) | Silicon dioxide SiO₂ |
| sicl4 | ![sicl4](mol/sicl4.svg) | Silicon tetrachloride SiCl₄ |
| sio4 | ![sio4](mol/sio4.svg) | Silicate tetrahedron SiO₄⁴⁻ |
| ch4 | ![ch4](mol/ch4.svg) | Methane CH₄ |
| sih4 | ![sih4](mol/sih4.svg) | Silane SiH₄ |
<!-- gallery:end -->

<!-- smiles:begin -->
```smiles
FB(F)F bf3 Boron trifluoride BF₃
ClB(Cl)Cl bcl3 Boron trichloride BCl₃
Cl[Al](Cl)Cl[Al](Cl)Cl al2cl6 Aluminium chloride dimer Al₂Cl₆
[BH2]1[H][BH2][H]1 b2h6 Diborane B₂H₆
OB(O)O h3bo3 Boric acid H₃BO₃
O[B-]1OB2OB(O)OB(O2)O1 borax Borax anion [B₄O₅(OH)₄]²⁻
B1NBNBN1 borazine Borazine B₃N₃H₆
B#N bn Boron nitride BN
[C-]#[O+] co Carbon monoxide CO
O=C=O co2 Carbon dioxide CO₂
O=[Si]=O sio2 Silicon dioxide SiO₂
[Si](Cl)(Cl)(Cl)Cl sicl4 Silicon tetrachloride SiCl₄
[Si]([O-])([O-])([O-])[O-] sio4 Silicate tetrahedron SiO₄⁴⁻
C ch4 Methane CH₄
[SiH4] sih4 Silane SiH₄
```
<!-- smiles:end -->
