# Stereoisomerism — handwritten short notes (JEE Main + Advanced)

A complete, self-contained image set of teacher-style short notes for the
stereoisomerism chapter: **Part I** covers the JEE Main + Advanced core, **Part II**
extends to the JEE Advanced edge of the syllabus. There is **no Olympiad section**
(chemistry chapters are capped at JEE Advanced, per the project rule).

* **41 sheets, 67 A4 pages**, 2480 × 3508 px PNGs at nominal 300 dpi.
* Part I: J-01 … J-29 — 51 pages. Part II: X-01 … X-12 — 16 pages.
* Every page carries `Part · sheet id · page k of n` in the header and `page N` in
  the footer, so a printed page can never be separated from its sheet.
* One idea per screen: statement → reason → worked example → result to memorise →
  the trap that follows.

## Start here

| File | What it is |
|---|---|
| `index.html` | Gallery of all 67 pages + every download in one place |
| `downloads/stereoisomerism-complete-png.zip` | All 67 PNGs (Part I first) + both part PDFs |
| `downloads/stereoisomerism-part1-jee-png.zip` | Part I PNGs only |
| `downloads/stereoisomerism-part2-extensions-png.zip` | Part II PNGs only |
| `pdf/stereoisomerism-complete.pdf` | A4 PDF, Part I then Part II, bookmark per sheet |
| `pdf/stereoisomerism-jee.pdf`, `pdf/stereoisomerism-extensions.pdf` | The two part PDFs |
| `PRINTING.txt` | A4 portrait, one sheet per page, scale **Fit** — not Fill, not Crop |
| `SCOPE.md` | What is in, what is out, which source lecture feeds which sheet |
| `SOURCE-AUDIT.md` | Conflicts inside the source, corrections made, what was and was not verified |

## How the chapter is organised

**Part I — core (29 sheets).** The isomerism map and vocabulary (J-02); geometrical
isomerism from the two conditions through E/Z and CIP, C=N, azo, rings, cumulenes,
spiro and bicyclics, counting, and the physical-property consequences (J-03 … J-09);
optical isomerism from the polarimeter through symmetry tests, meso/racemic,
resolution, projections, R/S, D/L, *threo*/*erythro*, chirality without a stereocentre,
counting and relation questions (J-10 … J-20); configuration versus conformation,
ethane/butane profiles, the cyclohexane chair and substituted cyclohexanes (J-21 … J-24);
reaction stereochemistry — S<sub>N</sub>1/S<sub>N</sub>2/E2, syn and anti addition,
hydrogenation (J-25, J-26); the full C<sub>5</sub>H<sub>11</sub>Cl enumeration (J-27);
twenty traps (J-28); a two-page recall sheet (J-29).

**Part II — extensions to the Advanced edge (12 sheets).** Symmetry treated properly —
five operations, S<sub>1</sub> = σ, S<sub>2</sub> = i, point-group thinking, a chirality
decision tree (X-01); axial chirality and atropisomerism with barriers (X-02); ring
junctions, trans-cycloalkenes, Bredt's rule, steroids (X-03); quantitative conformational
analysis — Boltzmann populations, A-values, 1,3-diaxial decomposition, the anomeric
effect (X-04); the ring-flip path and fused systems (X-05); stereospecific versus
stereoselective, Cram and Felkin–Anh (X-06); enumeration by orbit counting (X-07);
prochirality, topicity and pseudoasymmetry (X-08); optical purity, kinetic resolution,
ORD/CD (X-09); eight solved Advanced problems (X-10); applications (X-11); a final
pitfall audit (X-12).

## Rebuilding

```bash
python3 -m venv /tmp/venv && /tmp/venv/bin/pip install pymupdf pillow
/tmp/venv/bin/python build/build.py            # both PDFs
/tmp/venv/bin/python build/package.py          # PNGs, thumbs, ZIPs, combined PDF, index.html
/tmp/venv/bin/python checks/verify.py          # 60+ structural checks
/tmp/venv/bin/python checks/page_report.py     # ink coverage per page
```

The PNGs, thumbnails and ZIPs are **build products and are not committed** (about 100 MB
of rasters); the PDFs are. A fresh clone therefore has the sources, the PDFs and the
scripts, and gets the image set back with:

```bash
/tmp/venv/bin/python build/package.py   # needs pdf/ from build.py first
```

Content lives in `content/jee_1..4.py` (Part I), `content/ext_1.py`, `content/ext_2.py`
(Part II) and `content/extra_blocks.py` (blocks appended to a named sheet). Each sheet is
a dict `{"id", "title", "blocks": [(kind, …), …]}`; the block kinds are documented at the
top of `build/pagelib.py`. Editing text and re-running the two commands above regenerates
everything; no page is hand-placed.

Fonts: Kalam and Caveat (SIL OFL) for the handwritten prose and headings, DejaVu Serif for
mathematics and Greek — see `assets/fonts/`. Colours: navy prose, teal headings, yellow
key results, red warnings.

## Honest status

Structure, pagination, filenames, ZIP contents, bookmarks and links are machine-checked by
`checks/verify.py`. The chemistry was read sheet by sheet and the source's internal
conflicts are logged in `SOURCE-AUDIT.md`, but **no claim of exhaustive chemical
verification is made**: numerical values are textbook ranges, some conventions
(syn/anti for C=N, CIP rules for axes) vary between books, and the source videos were not
watched — only its markdown transcript was available.
