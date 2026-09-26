# Project status: what we're doing, what's done, what's left

*Last updated: 2026-09-26. Update this file whenever a chapter is finished.*

## The goal

Turn this repo into a complete, consistent set of **JEE Main + Advanced chemistry notes** that
read well both on GitHub and as an **Obsidian vault**:

- One `notes.md` per chapter, built from the NCERT chapter plus the Allen module when one has been
  uploaded. Markers: 🅰 = Allen-only, 🆇 = extra JEE Advanced point, ⚠ = trap.
- Every note follows one spec, [`docs/NOTE-FORMATTING-RULEBOOK.md`](docs/NOTE-FORMATTING-RULEBOOK.md):
  tables, Mermaid flowcharts, a mindmap outline, flashcards and a Quick Revision Sheet.
- Chemical structures are drawn with the Obsidian **Chem** and **ChemEdit** plugins (rulebook
  R18). Each drawing is still a plain SVG, so it shows on GitHub too.

### The current overhaul (in this order)

| # | Chapter | Scope | Status |
|---|---|---|---|
| 1 | [Redox Reactions](Physical-Chemistry/05-Redox-Reactions/notes.md) | Rewrite to the rulebook, add Chem/ChemEdit structures | ✅ **Done** ([PR #4](https://github.com/SurajGupta2009/Chem_JEEAd_notes/pull/4)) |
| 2 | [Equilibrium, ionic part](Physical-Chemistry/04-Equilibrium/notes.md) (Part C, §13–22) | Same treatment. Stays in the **one** Equilibrium file | ⏳ Next |
| 3 | [Equilibrium, chemical part](Physical-Chemistry/04-Equilibrium/notes.md) (Parts A–B) | Same treatment, same file | ⏳ Pending |
| 4 | [Thermodynamics](Physical-Chemistry/03-Thermodynamics/) | **New, full** NCERT Unit 5 notes from `kech105.pdf`: first law, work and heat, ΔH, thermochemistry (Hess's law, bond and lattice enthalpies), entropy, Gibbs energy | ⏳ Pending, nothing written yet |

Working agreement: each chapter is committed and pushed when it's finished, and I check in with
you before starting the next one.

## Done

### Notes
| Chapter | Words | State |
|---|---|---|
| [Redox Reactions](Physical-Chemistry/05-Redox-Reactions/notes.md) | ≈14,900 | ✅ **Rulebook v1.1 format.** 22 sections, 7 Mermaid charts, 32 structure drawings with calculated oxidation states, [flashcards](Physical-Chemistry/05-Redox-Reactions/cards.md) (59), [chapter map](Physical-Chemistry/05-Redox-Reactions/figures/redox-map.md), NCERT Ex. 7.1–7.30 |
| [Equilibrium](Physical-Chemistry/04-Equilibrium/notes.md) | ≈15,200 | ✅ Written in the **old format** (no frontmatter, cards or structures). Overhaul pending |
| [Electrochemistry](Physical-Chemistry/08-Electrochemistry/notes.md) | ≈9,800 | ✅ Written in the old format |
| [d- and f-Block](Inorganic-Chemistry/07-The-d-and-f-Block-Elements/notes.md) | ≈9,900 | ✅ Written in the old format (Allen module used) |
| [Coordination Compounds](Inorganic-Chemistry/08-Coordination-Compounds/notes.md) | ≈4,700 | ✅ Written in the old format (Allen module used) |
| [Salt Analysis](Practical-Chemistry/Salt-Analysis/notes.md) | ≈6,600 | ✅ Written in the old format (Allen modules used) |

### Tooling and docs
- [`docs/OBSIDIAN-SETUP.md`](docs/OBSIDIAN-SETUP.md) is the plugin guide, including how Chem and
  ChemEdit share the work (§5.1a).
- [`docs/NOTE-FORMATTING-RULEBOOK.md`](docs/NOTE-FORMATTING-RULEBOOK.md) v1.1 is the formatting spec
  every note should follow.
- [`docs/OBSIDIAN-VAULT-PLAN.md`](docs/OBSIDIAN-VAULT-PLAN.md) is the phased plan for opening the
  repo as a vault. **Written, but not carried out yet.**
- [`scripts/render_structures.py`](scripts/render_structures.py) turns a chapter's
  `figures/structures.md` SMILES table into:
  - SVGs that ChemEdit can open for editing, with **oxidation states calculated from the bonds
    and checked** against the table;
  - a gallery and a Chem `smiles` block;
  - with `--library`, the combined [`docs/COMPOUND-LIBRARY.md`](docs/COMPOUND-LIBRARY.md).
- [`scripts/fetch_ncert_pdfs.py`](scripts/fetch_ncert_pdfs.py) (older) downloads the NCERT PDFs and
  generates every chapter `README.md` and the branch indexes.

## Left to do

### This overhaul
1. **Ionic Equilibrium** (Equilibrium Part C).
   - Tables, flowcharts, flashcards and a map.
   - Structures: conjugate acid–base pairs, oxyacid strength (Cl and P series), indicators
     (phenolphthalein, methyl orange), buffer components.
2. **Chemical Equilibrium** (Equilibrium Parts A–B), same treatment.
   - Add frontmatter and regenerate Contents for the whole file.
3. **Thermodynamics**: write the full notes from scratch (target 9,000–12,000 words, like the
   other chapters).

### After the overhaul
- **Bring the other four written chapters up to the rulebook format.** These are
  Electrochemistry, d- and f-Block, Coordination and Salt Analysis. Coordination is the best
  candidate for the isomerism mindmap and ChemEdit complexes.
- **Metallurgy** (`Physical-Chemistry/12-…Isolation-of-Elements`): the Allen module is uploaded,
  but no notes exist yet.
- **Chapters with no notes:** 25 of the 31 chapter folders. Organic chemistry is **on hold**
  because you paused it; it won't be written unless you ask.
- **Carry out the Obsidian vault plan** (`.obsidian` settings, CSS snippet, plugin list).

### Still to check in Obsidian (can't be tested from here)
- **The `smiles` code-block conflict:** both Chem and ChemEdit claim these blocks, and only one
  wins. Setup guide §5.1a covers load order.
- **Opening a drawing in Ketcher:** check whether double-clicking an embedded image in a note
  works. Right-clicking the SVG file → *Edit SVG in Ketcher* is the documented fallback.
- **Plugin settings:**
  - Chem: turn on **Inline SMILES** so the flashcard structures render.
  - ChemEdit: set **Compound Library File Path** to `docs/COMPOUND-LIBRARY.md`.

## Picking up where we left off

```bash
pip install rdkit                                   # only needed to redraw structures
python3 scripts/render_structures.py --all --library docs/COMPOUND-LIBRARY.md
```

To start a chapter:

1. Create `figures/structures.md` with its SMILES table.
2. Run the script.
3. Embed the generated `figures/mol/*.svg` in `notes.md` as image tables, following
   [Redox §5](Physical-Chemistry/05-Redox-Reactions/notes.md) as the model.
4. Go through the rulebook's pre-commit checklist (R32).
