# Chem_JEEAd_notes

Chemistry notes for **JEE Main + JEE Advanced**, organised by branch. Every NCERT chapter
lives in its own folder inside `Physical-Chemistry/`, `Inorganic-Chemistry/` or
`Organic-Chemistry/`, with the practical work in `Practical-Chemistry/`.

The notes are plain Markdown and PDF, so they read the same on GitHub and as an Obsidian
vault. One format spec governs every file:
[`docs/NOTE-FORMATTING-RULEBOOK.md`](docs/NOTE-FORMATTING-RULEBOOK.md).

## Status

**22 of 31 chapters written — 147,000 words, 159 Mermaid diagrams, 135 chemical structures.**

| Branch | Written | Total chapters | Words |
|---|---:|---:|---:|
| Physical Chemistry | 12 | 12 | 78,600 |
| Inorganic Chemistry | 9 | 9 | 55,600 |
| Practical Chemistry | 1 | 1 | 7,100 |
| Organic Chemistry | 0 | 9 | — |
| **Total** | **22** | **31** | **147,300** |

| Branch | Chapter | Words | Diagrams | Structures | Allen module |
|---|---|---:|---:|---:|---|
| Physical | [01 Some Basic Concepts of Chemistry](Physical-Chemistry/01-Some-Basic-Concepts-of-Chemistry/notes.md) | 5,186 | 6 | — | — |
| Physical | [02 Structure of Atom](Physical-Chemistry/02-Structure-of-Atom/notes.md) | 5,313 | 8 | — | — |
| Physical | [03 Thermodynamics](Physical-Chemistry/03-Thermodynamics/notes.md) | 5,487 | 5 | — | — |
| Physical | [04 Equilibrium](Physical-Chemistry/04-Equilibrium/notes.md) | 16,436 | 5 | — | — |
| Physical | [05 Redox Reactions](Physical-Chemistry/05-Redox-Reactions/notes.md) | 15,279 | 9 | 32 | — |
| Physical | [06 States of Matter](Physical-Chemistry/06-States-of-Matter/notes.md) | 5,608 | 6 | — | — |
| Physical | [07 Solutions](Physical-Chemistry/07-Solutions/notes.md) | 4,653 | 4 | — | — |
| Physical | [08 Electrochemistry](Physical-Chemistry/08-Electrochemistry/notes.md) | 10,732 | 4 | — | — |
| Physical | [09 Chemical Kinetics](Physical-Chemistry/09-Chemical-Kinetics/notes.md) | 3,661 | 4 | — | — |
| Physical | [10 The Solid State](Physical-Chemistry/10-The-Solid-State/notes.md) | 5,215 | 9 | — | — |
| Physical | [11 Surface Chemistry](Physical-Chemistry/11-Surface-Chemistry/notes.md) | 6,542 | 7 | — | — |
| Physical | [12 Isolation of Elements (Metallurgy)](Physical-Chemistry/12-General-Principles-and-Processes-of-Isolation-of-Elements/notes.md) | 5,508 | 7 | — | ✅ |
| Inorganic | [01 Classification & Periodicity](Inorganic-Chemistry/01-Classification-of-Elements-and-Periodicity-in-Properties/notes.md) | 5,415 | 9 | — | — |
| Inorganic | [02 Chemical Bonding & Structure](Inorganic-Chemistry/02-Chemical-Bonding-and-Molecular-Structure/notes.md) | 6,693 | 17 | 33 | ✅ |
| Inorganic | [03 Hydrogen](Inorganic-Chemistry/03-Hydrogen/notes.md) | 5,032 | 11 | 6 | ✅ |
| Inorganic | [04 s-Block Elements](Inorganic-Chemistry/04-The-s-Block-Elements/notes.md) | 4,672 | 8 | 15 | ✅ |
| Inorganic | [05 p-Block (Groups 13–14)](Inorganic-Chemistry/05-The-p-Block-Elements/notes.md) | 4,896 | 8 | 17 | ✅ |
| Inorganic | [06 Environmental Chemistry](Inorganic-Chemistry/06-Environmental-Chemistry/notes.md) | 2,615 | 6 | — | ✅ |
| Inorganic | [07 d- and f-Block](Inorganic-Chemistry/07-The-d-and-f-Block-Elements/notes.md) | 10,730 | 9 | — | ✅ |
| Inorganic | [08 Coordination Compounds](Inorganic-Chemistry/08-Coordination-Compounds/notes.md) | 5,541 | 6 | — | ✅ |
| Inorganic | [09 p-Block (Groups 15–18)](Inorganic-Chemistry/09-The-p-Block-Elements/notes.md) | 4,989 | 5 | 32 | ✅ |
| Practical | [Salt Analysis](Practical-Chemistry/Salt-Analysis/notes.md) | 7,129 | 4 | — | ✅ |
| Organic | All 9 chapters | — | — | — | — |

Organic Chemistry has no notes yet. Every other chapter has a `notes.md` that passes
`scripts/check_notes.py` (see [Quality gate](#quality-gate)).

## Layout

```text
Physical-Chemistry/            12 chapters    Inorganic-Chemistry/   9 chapters
├── README.md                  branch index   ├── README.md          branch index
├── 01-Some-Basic-Concepts-of-Chemistry/       │   └── … 9 chapter folders
│   ├── kech101.pdf            NCERT chapter
│   ├── README.md              chapter card (generated — never hand-edit)
│   ├── notes.md               the notes themselves
│   └── figures/               structures.md + mol/*.svg (only where drawn)
├── …
└── 12-General-Principles-and-Processes-of-Isolation-of-Elements/

Organic-Chemistry/             9 chapters, no notes yet
Practical-Chemistry/
└── Salt-Analysis/             not an NCERT chapter
```

- **Chapter numbers are per branch**, in Class XI → Class XII NCERT unit order. So
  `Physical-Chemistry/04-Equilibrium` is NCERT Class XI **Unit 6** — the folder number is
  *not* the unit number. Each chapter `README.md` and branch index carry the real unit and
  the NCERT code (`kech1xx`/`kech2xx` = Class XI, `lech1xx`/`lech2xx` = Class XII).
- **One `notes.md` per chapter**, written from the NCERT chapter *and* the Allen module when
  one is present. Markers: 🅰 = Allen-only, 🆇 = extra JEE Advanced point, ⚠ = trap.
- **Branch ownership** is one dict, `BRANCH_OF` in
  [`scripts/fetch_ncert_pdfs.py`](scripts/fetch_ncert_pdfs.py). Three deliberate calls:
  Solid State, Surface Chemistry and Metallurgy sit under **Physical**; Biomolecules,
  Polymers and Chemistry in Everyday Life sit with **Organic**; Chemical Bonding, Hydrogen
  and Environmental Chemistry stay **Inorganic**. To move a chapter, edit `BRANCH_OF` and
  re-run the script with `--layout`, then `git mv` the folder.

## NCERT editions — why there are two

- **JEE Main** follows the **rationalised NCERT (2023+)** — 19 chemistry chapters
  (Class XI: 9, Class XII: 10).
- **JEE Advanced** still tests material rationalisation deleted: States of Matter, Hydrogen,
  s-Block, p-Block, Environmental Chemistry, The Solid State, Surface Chemistry, Metallurgy,
  Polymers and Chemistry in Everyday Life. Those come from the **pre-rationalisation
  (2018-19) NCERT** and are marked *Advanced only* in the branch indexes
  ([Physical](Physical-Chemistry/README.md), [Inorganic](Inorganic-Chemistry/README.md),
  [Organic](Organic-Chemistry/README.md)).

19 + 11 = **30 NCERT chapters**, plus Salt Analysis in `Practical-Chemistry/`.

> **Careful with NCERT codes.** Rationalisation made the books shorter, so NCERT reused
> codes — `kech105` was *States of Matter* and is now *Thermodynamics*; `lech101` was
> *The Solid State* and is now *Solutions*. Legacy PDFs are therefore `<code>-legacy.pdf`.

## Reading and writing these notes

- [`docs/NOTE-FORMATTING-RULEBOOK.md`](docs/NOTE-FORMATTING-RULEBOOK.md) — **the spec**:
  folder contents, frontmatter, Contents anchors, notation, tables, Mermaid house style,
  structures, the Quick Revision Sheet, and the pre-commit checklist.
- [`docs/OBSIDIAN-SETUP.md`](docs/OBSIDIAN-SETUP.md) — open the repository root as an
  Obsidian vault and which plugins to install.
- [`docs/COMPOUND-LIBRARY.md`](docs/COMPOUND-LIBRARY.md) — every structure drawn in the
  notes (generated); point ChemEdit's compound-library setting at it.
- [`meta/Progress.md`](meta/Progress.md) — Dataview dashboard of every chapter's status.
- [`meta/templates/chapter-notes.md`](meta/templates/chapter-notes.md) — the skeleton a new
  note starts from.

## Quality gate

`scripts/check_notes.py` is the linter the rulebook's R33 asks for. It checks frontmatter
and `words:`, H1/H2 numbering, Contents anchors against GitHub's slug algorithm, internal
links, table integrity, Mermaid house style, and the Quick Revision Sheet. **All 22 written
chapters pass with zero findings.**

```bash
python3 scripts/check_notes.py             # every notes.md
python3 scripts/check_notes.py Inorganic-Chemistry/02-*/notes.md   # just one
```

`scripts/quote_mermaid_labels.py` is the mechanical half of the Mermaid rule: it quotes
every unquoted node, edge and subgraph label, and is safe to re-run.

```bash
python3 scripts/quote_mermaid_labels.py           # rewrite
python3 scripts/quote_mermaid_labels.py --check   # dry run
```

## Chemical structures

Structure drawings live in a chapter's `figures/structures.md` (a SMILES table) and are
rendered into `figures/mol/*.svg` with oxidation states computed from the bonds and checked
against the table (rulebook R18). The SVGs are plain files, so they show on GitHub *and*
open in Ketcher/ChemEdit.

```bash
pip install rdkit                                # dev-only; readers never need it
python3 scripts/render_structures.py --all       # redraw every chapter
python3 scripts/render_structures.py --all --validate   # check SMILES and SVGs, draw nothing
python3 scripts/render_structures.py --all --library docs/COMPOUND-LIBRARY.md
```

`--validate` needs no RDKit and reports a missing or stale SVG next to a bad SMILES string,
so it is the cheap way to confirm a chapter is in sync.

## Refreshing the NCERT PDFs

```bash
pip install pypdf                              # only for --verify
python3 scripts/fetch_ncert_pdfs.py            # download + regenerate all READMEs/indexes
python3 scripts/fetch_ncert_pdfs.py --force    # re-download everything
python3 scripts/fetch_ncert_pdfs.py --verify   # check the PDFs on disk
python3 scripts/fetch_ncert_pdfs.py --layout   # print NCERT unit -> branch/folder
```

PDFs come from <https://ncert.nic.in/textbook.php> when reachable, otherwise from GitHub
mirrors of the same files. Every download is checked: it must be a valid PDF whose opening
pages contain the chapter title. Set `GITHUB_TOKEN` to raise the API rate limit.

> The script owns the three branch indexes and every chapter `README.md`, and it is what
> keeps the chapter numbering consistent. It **never** touches `notes.md` or the Allen
> module PDFs — so never hand-edit a generated `README.md`.

## Copyright

All NCERT PDFs are NCERT's own chapter files, published by the National Council of
Educational Research and Training, Government of India, and made freely available for
educational use — see <https://ncert.nic.in/copyright.php>. Allen module PDFs are study
material owned by ALLEN Career Institute Pvt. Ltd., kept here for personal study only.
