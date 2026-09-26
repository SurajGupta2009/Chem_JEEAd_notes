# Obsidian plugin catalogue for this vault

**Scope:** every Obsidian plugin worth knowing about for *making and studying these chemistry
notes*, where the notes are written as markdown files by **Arena AI** and read/revised by you in
Obsidian. Plugin IDs below were checked against the official community registry
([obsidianstats.com](https://www.obsidianstats.com), Sep 2026) — a few are marked
*(search by name)* where the ID is unstable; install those from
**Settings → Community plugins → Browse** using the display name.

---

## 0. TL;DR — the ten to install today

| # | Plugin | ID | What it does for *this* repo |
|---|---|---|---|
| 1 | **Git** | `obsidian-git` | The Arena AI bridge: auto-pull AI-written `notes.md`, commit/push your edits. 3.2 M downloads |
| 2 | **Dataview** | `dataview` | Live "which chapters have notes / how long / what's pending" dashboard (§12) |
| 3 | **Advanced Tables** | `table-editor-obsidian` | These notes are table-dense (rule sets, formula banks). Tab-through cells, auto-align, sort |
| 4 | **LaTeX Suite** | `obsidian-latex-suite` | Snippet expansion for fast LaTeX/`\ce{}` typing; auto-fraction, matrix Tab navigation |
| 5 | **Excalidraw** | `obsidian-excalidraw-plugin` | Hand-drawn reaction mechanisms; saves as `.excalidraw.md` so it stays text-diffable in git. Most-downloaded plugin on the store (8.1 M) |
| 6 | **ChemEdit** | `chemedit` | Real Ketcher structure/reaction editor in-vault; opens `.mol` and ChemDraw `.cdxml`; offline mode |
| 7 | **PDF++** | `pdf-plus` | The NCERT + Allen PDFs live *in* this vault — this turns highlights into markdown links back into the notes |
| 8 | **Spaced Repetition** | `obsidian-spaced-repetition` | `Question::Answer` flashcards + scheduled re-reading of whole notes |
| 9 | **Templater** | `templater-obsidian` | One command to scaffold a new chapter `notes.md` in the repo's house style (§13) |
| 10 | **Omnisearch** | `omnisearch` | Typo-tolerant BM25 search across notes *and* PDFs (pair with Text Extractor) |

Everything else below is optional or special-purpose.

---

## 1. The authoring loop this vault is built for

```
Arena AI ──writes──▶ notes.md · README.md · cards.md   (markdown in the repo, on this branch)
                            │
                            │  git pull   ← obsidian-git (auto, every N minutes)
                            ▼
                     Obsidian vault  ──renders──▶  MathJax + mhchem · Mermaid · GFM tables · callouts
                            │
                            ├── ChemEdit / Excalidraw ──▶ you add drawn mechanisms
                            ├── PDF++ ──▶ you annotate kech202.pdf beside the notes
                            ├── Spaced Repetition ──▶ you convert notes to cards
                            └── Dataview ──▶ live progress board
                            │
                            │  git commit + push   ← obsidian-git
                            ▼
              Arena AI reads your edits on the next turn
```

`obsidian-git` is the keystone: without it you are copy-pasting between a browser and a folder.
With it, Arena AI's output simply *appears* in your vault, and your hand edits travel back.

Settings that matter: **Pull on startup** ✔ · **Auto-pull interval** 10 min ·
**Auto-commit-and-sync interval** 30 min · **Commit message** `vault: {{date}}` ·
**Pull changes on startup** before Obsidian indexes, so links resolve.

---

## 2. What needs **zero** plugins

Obsidian core already renders the entire convention used in these notes:

| Used in these notes | Core support | Where it appears |
|---|---|---|
| GFM tables | ✅ | Every branch index, every chapter card, every rule/comparison table |
| ` ```mermaid ` flowcharts | ✅ (Mermaid bundled) | Equilibrium §8, Redox §1/§6/§15, Electrochemistry §4, d-block §9, Coordination §5 |
| `$…$` and `$$…$$` LaTeX | ✅ (MathJax bundled) | Nernst, Kp/Kc, ΔG, Kohlrausch derivations |
| **`\ce{…}` (mhchem)** | ✅ **mhchem ships with Obsidian** | e.g. `$\ce{H2SO4 + 2NaOH -> Na2SO4 + 2H2O}$` — no plugin needed |
| ASCII structures in fenced blocks | ✅ | `CrO₅` butterfly, `H₂SO₅`, sawhorse/Newman sketches |
| `> **⚠ …**` blockquote traps | ✅ | All six existing `notes.md` |
| `> [!warning]` callouts | ✅ Obsidian only | **Not rendered on GitHub** — see the trap below |
| Relative markdown links | ✅ | Chapter cross-links |
| PDF reader | ✅ core *PDF viewer* | NCERT + Allen PDFs, one click from the chapter card |
| Canvas, Backlinks, Outline, Tags, Word count, **Bases** (Obsidian ≥ 1.9) | ✅ core plugins | Enable in *Settings → Core plugins* |

> **⚠ The one GitHub-vs-Obsidian trap.** GitHub renders `$$…$$` but does **not** load mhchem,
> so `\ce{…}` shows as raw source on github.com. That is exactly why the existing notes write
> formulas with Unicode subscripts in prose (`K₂Cr₂O₇`, `MnO₄⁻`, `H₂SO₄`) and reserve LaTeX for
> genuinely mathematical expressions. Keep that split for anything that must read well in both
> places; use `\ce{}` freely in *personal* study files such as `cards.md`.
> Same rule for `[[wikilinks]]` and Dataview blocks — Obsidian-only syntax.

---

## 3. Category A — Sync, version control, and the AI loop

| Plugin | ID | Notes |
|---|---|---|
| **Git** | `obsidian-git` | ⭐ Source-control view, staging, diffs, history, branch/remote switching, inline added/removed line markers, GitHub file links. The one to install |
| Git Changelog | `git-changelog` | Sidebar changelog: lines added/deleted, renames, per-note edit history. Nice for "what did AI change this week?" |
| Show Diff | `show-diff` | Renders a git diff *inside a note* — e.g. an auto "today's changes" block |
| Fit | `fit` | One-click GitHub sync incl. **mobile** (pure JS, no system git needed) + conflict resolution |
| Git Integration | `git-integration` | Minimal init/commit/push panel |
| Cicada Synchronizer | `cicada-sync` | Single-button sync + easy branch switching (relevant: this repo uses per-session branches) |
| GitHobs | `githobs` | Create/manage repos, embed code snippets from GitHub |
| Git Url | `git-url` | Insert remote file URLs |
| Remotely Save | `remotely-save` | Sync via S3 / Dropbox / OneDrive / Drive / WebDAV with E2E encryption — an alternative if you don't want git on your phone |
| BRAT | `obsidian42-brat` *(search by name)* | Install beta/unlisted plugins straight from a GitHub repo |

---

## 4. Category B — Markdown authoring quality

| Plugin | ID | Notes |
|---|---|---|
| **Advanced Tables** | `table-editor-obsidian` | ⭐ Excel-style navigation, auto-format pipes, sort by column, CSV export, table formulas |
| **Linter** | `obsidian-linter` | Configurable rules for headings/YAML/spacing/footnotes + a **diff preview** before applying. Run it *manually*, not on save — otherwise it fights the fetch script's generated READMEs |
| **Templater** | `templater-obsidian` | Scripting templates (JS, prompts, system commands). Template for a new chapter in §13 |
| **QuickAdd** | `quickadd` | Templates + captures + **macros**: one command that makes the chapter folder, runs the Templater template and opens the PDF |
| Outliner | `obsidian-outliner` | Workflowy-style list manipulation, indent guides, drag-drop — good for building the `## Contents` tree |
| Editing Toolbar | `editing-toolbar` | Word-processor toolbar (colours, alignment, headings) + focus modes |
| Any Block | `any-block` | Converts lists/quotes into blocks and **list → table** conversions |
| Sheets Extended | `sheets` | Cell merging, vertical headers, per-cell CSS in markdown tables |
| Table Generator | `obsidian-table-generator` | Typora-style quick table insertion |
| JSON table | `json-table` | JSON ⇄ markdown table |
| Markdown table checkboxes | `table-checkboxes` | Makes `- [ ]` clickable *inside* tables (useful for a revision checklist table) |
| CSV Table | `obsidian-csv-table` | Render a `.csv` as a sortable/filterable table — e.g. a bond-length/bond-enthalpy data file |
| Tabsdown | `tabsdown` | Tabbed content blocks via markdown fences; tabs can contain math, Mermaid, callouts |
| Importer | `obsidian-importer` | Migrate from Notion/Evernote/OneNote/Apple Notes/CSV/HTML if you have old notes elsewhere |
| Consistent Attachments and Links | *(search by name)* | Keeps relative links intact when a chapter folder is moved — matters if you ever edit `BRANCH_OF` in `scripts/fetch_ncert_pdfs.py` and `git mv` a chapter |

---

## 5. Category C — Chemistry rendering (the interesting one)

### 5.1 Structures, reactions and SMILES

| Plugin | ID | Notes |
|---|---|---|
| **ChemEdit** | `chemedit` | ⭐ Full **Ketcher** editor embedded: draw structures & reactions, natively render/edit `.mol` and ChemDraw `.cdxml`, double-click a rendered molecule to edit, auto-saves to disk, adapts to light/dark, offline mode. Also supports simple electronic lab notebooks |
| **Chem** | `chem` | ⭐ Renders **SMILES** locally (SmilesDrawer + RDKit.js) in code blocks *and* inline; scale/theme/export options; Dataview integration. No server, no network |
| Ketcher | `ketcher` | The sketcher on its own (view/draw structures & reactions). Redundant if you have ChemEdit |
| Chemical Structure Renderer | `chemical-structure-renderer` | SMILES → PNG/SVG via a Ketcher + **Indigo web service** (custom server allowed). Use if you prefer service rendering |
| ChemSearch | `chem-search` | Vault-wide **substructure search**: draw a fragment, find every note containing a matching SMILES; also lab-inventory/stock tracking. Needs ChemEdit for the drawing UI |
| Periodic Table | `periodic-table` | Interactive periodic table in the sidebar with element properties — handy beside the Inorganic p-/d-block notes |
| ChemEdit Universal | *(search by name)* | ChemEdit variant that also works on mobile |

**SMILES in practice** (works with `chem`, and ChemEdit can render the same strings):

````markdown
```smiles
CC(=O)O
```
````
→ acetic acid drawn properly. For organic chapters this beats ASCII structures every time —
and it is plain text, so Arena AI can write it and git can diff it.

### 5.1a Chem + ChemEdit together (how this repo uses them)

Install **both**. They split the work (rulebook R18):

| You see | Where | Plugin that makes it interactive |
|---|---|---|
| Structure drawings with red oxidation states | `notes.md` → `figures/mol/*.svg` | **ChemEdit**: the SVGs carry their molfile, so Ketcher can open them |
| A live grid of every structure in a chapter | `figures/structures.md` (```` ```smiles ```` block) | **Chem** |
| Molecules drawn inside flashcards | `cards.md` (`` `$smiles=…` `` in the question) | **Chem** (Settings → Chem → turn on **Inline SMILES**) |
| "Insert SMILES from Library" | [`COMPOUND-LIBRARY.md`](COMPOUND-LIBRARY.md) | **ChemEdit** (Settings → ChemEdit → **Compound Library File Path** = `docs/COMPOUND-LIBRARY.md`) |

**Setup, once:**

1. Install and enable **Chem** first, then **ChemEdit**.
2. **Both plugins register the ```` ```smiles ```` code block, and only one can own it.**
   If the gallery in `structures.md` renders as a Ketcher viewer instead of a Chem grid (or
   not at all), disable ChemEdit, reload, and re-enable it so it loads after Chem. The
   developer console (Ctrl+Shift+I) shows an error mentioning `smiles` for the plugin that
   lost. ChemEdit registers `smiles` as its last step, so losing it costs ChemEdit nothing
   else. Either renderer draws the gallery, so this is cosmetic.
3. Chem → renderer **RDKit.js** (handles ions like `[NH4+]` and `[O-]` better than
   SmilesDrawer).
4. ChemEdit → set the compound-library path as above.

**Editing a structure in Ketcher.** Open the SVG itself (click it in the file explorer, or
right-click → *Edit SVG in Ketcher*; double-clicking the embedded image in a note works where
ChemEdit recognises the embed). Ketcher saves in its own drawing style **without the red O.S.
labels**, and the next `render_structures.py` run overwrites the file anyway. So treat the
table as the source: right-click the structure → *Copy SMILES*, paste it into
`figures/structures.md`, and rerun the script (rulebook R18). A "Not a Ketcher SVG" message
means the SVG was not made by the script (e.g. an old export); regenerate it.

### 5.2 Equations and typesetting

| Plugin | ID | Notes |
|---|---|---|
| **mhchem** | *built into Obsidian core* | `\ce{}` — no install |
| **LaTeX Suite** | `obsidian-latex-suite` | Snippet engine: `sqx`→`\sqrt{x}`, `a/b`→`\frac{a}{b}`, auto-fraction, matrix Tab/Enter navigation, bracket colouring, conceal mode, visual snippets (`C` = cancel a term). Add your own `\ce` snippets for repeated reactions |
| TikZJax | `tikzjax` | Compiles real **TikZ / `chemfig`** in-note → publication-grade skeletal formulas, orbital diagrams, Born–Haber cycles. Powerful but heavy; only if you know TikZ |
| SwiftLaTeX Render | `swiftlatex-render` | `latex` / `latexsvg` code blocks → PDF or SVG via a WASM LaTeX compiler |
| Extended MathJax | *(search by name)* | Loads a custom MathJax **preamble** at startup (add `mhchem`, `bussproofs`, physics packages). Usually unnecessary — mhchem is already bundled |
| Image2LaTeX | *(search by name)* | Clipboard **image of a formula → markdown/LaTeX**. Great for converting a screenshot of an Allen-module equation |
| Copy as LaTeX / Export to TeX | *(search by name)* | Push notes *out* to LaTeX for a printed revision booklet |

---

## 6. Category D — Diagrams

| Plugin | ID | Notes |
|---|---|---|
| **Mermaid** | *core* | Already used by six of these notes |
| **Excalidraw** | `obsidian-excalidraw-plugin` | ⭐ Sketching canvas: mechanisms, energy-profile diagrams, crystal-field splitting sketches. Embeds in notes, links both ways, exports synced PNG/SVG, LaTeX inside drawings, OCR, script engine (ExcalidrawAutomate), templates. 100 % local |
| Excalidraw Extras | *(companion, search by name)* | Pulls heavy deps out of Excalidraw: MathJax→SVG, Mermaid conversion, PDF printing |
| Mermaid Tools | `mermaid-tools` | Toolbar of Mermaid shapes/arrows so you don't memorise syntax; custom elements |
| Mermaid Link Navigator | `mermaid-link-nav` | Renders Mermaid flowcharts with **clickable wikilink nodes**, plus a visual editor that writes changes back into the source block; SVG/PNG export; offline Mermaid 11. Turn a reaction-map flowchart into a navigable map of your vault |
| Mermaid Popup | `mermaid-popup` | View large Mermaid diagrams in a popup (these notes' flowcharts get wide) |
| draw.io | `drawio` | Full draw.io editor inside Obsidian, local, interactive diagrams in reading mode, native Mermaid + LaTeX, Canvas placement |
| Export Graph View | `export-graph-view` | Export vault metadata as `.mmd` (Mermaid) or `.dot` (GraphViz) |
| Markmind | `obsidian-markmind` | Mind maps + outlines + PDF annotation in one; embed mind maps in markdown, convert outlines to tables, export to image/PDF. Good for a whole-chapter mind map (e.g. "all named reactions in Alcohols/Phenols/Ethers") |

---

## 7. Category E — PDFs: the NCERT chapters and Allen modules live here

This vault keeps ~40 PDFs next to the notes, so this category matters more than usual.

| Plugin | ID | Notes |
|---|---|---|
| **PDF++** | `pdf-plus` | ⭐ Turns **links to PDF text selections into visible highlights**; write highlights/links back into the PDF; backlinks with page filtering; hover sync; embedded page regions in a note; better copy tools. Read `kech106.pdf` and the notes side by side, linked |
| **Marker PDF to MD** | `marker-api` | ⭐ **PDF → rich markdown** with OCR, formula detection, table extraction and image handling; hosted API or self-hosted. This is how you get an Allen module's text into markdown for Arena AI to work from |
| Text Extractor | `text-extractor` | Extracts text (OCR) from PDFs/images/Office docs and **caches** it — this is what lets Omnisearch and other plugins search inside your PDFs |
| Extract PDF Annotations | `obsidian-extract-pdf-annotations` | Batch-extract highlights/comments from PDFs into notes, grouped by topic, templated output |
| Annotator | `obsidian-annotator` | Older PDF/EPUB annotator storing annotations as markdown; Dataview-integrated. PDF++ supersedes it |
| Better PDF | `better-pdf-plugin` | Legacy syntax for embedding PDF pages |
| PDF2Image | `pdf2img` | Convert PDF pages to images and insert them — capture a mechanism figure from a module |
| Slide Note | `slide-note` | Link plaintext notes to specific slide/PDF pages with a drawboard — built for lecture slides |
| PDF Folder to Markdowns | `pdf-folder-to-markdowns` | Convert a whole folder of PDFs into markdown notes, each embedding its PDF |
| LLM Summary | `llm-summary` | GPT summaries of PDF files + "define concept from selection" |
| Enhancing Export | `obsidian-enhancing-export` | Pandoc export → **PDF / DOCX / HTML / LaTeX** with media bundled. This is how you print a Quick Revision Sheet |
| PDF Break Page | `break-page` | Insert page breaks (`/break`) so exported PDFs paginate properly |

---

## 8. Category F — Turning notes into memory

| Plugin | ID | Card syntax / model | Notes |
|---|---|---|---|
| **Spaced Repetition** | `obsidian-spaced-repetition` | `Question::Answer`, multi-line, reversed, cloze `{{…}}`, `#flashcards` tag or folder-scoped | ⭐ Easiest start. Also schedules **whole-note review**, and renders LaTeX/code/images/audio in cards |
| **Aosr** | `aosr` | `#Q`-tagged sections; single/multi-line/cloze; audio; minute-level intervals | "Explore Hard Cards" mode; DB serialisation is explicitly **Git-plugin friendly**; folder/file exclusions |
| **Flashcards** | `flashcards-obsidian` | `Question::Answer`, `#card`, `#card-reverse`, `#card-spaced`, cloze (highlight or bracket) | Syncs into **Anki** via AnkiConnect; keeps LaTeX, images, audio, code highlighting, note refs |
| **Yanki** | `yanki` | Plain markdown, no special syntax; folder tree → Anki decks | Basic/Reversed/Cloze/Type-in; safe namespacing; smart sync; AnkiWeb compatible |
| **LearnKit** | `learnkit` | Cloze, reversed, MCQ, **image occlusion** | FSRS scheduling, note-review mode, TTS, analytics (charts/heatmaps/retention), Anki import+export, and an AI companion that generates cards/tests and critiques note quality |
| Come Through | `come-through` | Custom code blocks with shared IDs | FSRS; cards can span multiple notes |
| Decks | `decks` | Heading-paragraph or tag format | FSRS in-vault |
| Repeat | `repeat-plugin` | `repeat: every week` frontmatter | Spaced/periodic **note** review with natural-language scheduling |
| Better Recall · Auto Anki · Anki Integration · Sprout · The Queue · Flashcards LLM | *(search by name)* | — | Alternatives: Anki-style UI in-vault; LLM-generated cards; FSRS + image occlusion + TTS; randomised note revisit |

**Recommended pattern for this repo** — keep cards in a sibling file so the fetch script, the
GitHub view and Arena AI's notes stay clean:

```
Organic-Chemistry/02-Hydrocarbons/
├── notes.md      ← the notes (Arena AI writes these)
├── cards.md      ← your flashcards (Spaced Repetition / Aosr read these)
├── kech203.pdf
└── README.md     ← generated by scripts/fetch_ncert_pdfs.py
```

```markdown
<!-- cards.md -->
#flashcards/organic/hydrocarbons

Order of reactivity of 1° : 2° : 3° H towards free-radical chlorination?::≈ 1 : 3.8 : 5 — set by C–H bond dissociation enthalpy, not by statistics.

::
Why does the peroxide (Kharasch) effect work for HBr but not HCl or HI?
::
Both propagation steps must be exothermic and fast. H–Cl is too strong (H-abstraction is
endothermic); H–I is too weak and I• adds reversibly to the π bond, so no chain builds up.
```

Add `cards.md` to `.gitignore` if you want them purely personal — or commit them and ask
Arena AI to generate a card deck for each new chapter.

---

## 9. Category G — Progress tracking, navigation, search

| Plugin | ID | Use here |
|---|---|---|
| **Dataview** | `dataview` | ⭐ Query the vault like a database (DQL + inline JS). Builds the "what's left to write" dashboard in §12 — computed from the files, so it can never go stale like a hand-maintained table |
| **Tasks** | `obsidian-tasks-plugin` | Every `- [ ]` in the vault, collected with due/scheduled/done dates, recurrence, grouping, and status toggling from the query view |
| **Kanban** | `obsidian-kanban` | A markdown-backed board: *Module uploaded → Drafted → Reviewed → Revised*. Drag-and-drop mirror of the root README's Notes-status table |
| TaskNotes | `tasknotes` | One note per task + Bases-powered list/kanban/calendar/agenda views, Pomodoro, dependencies, calendar sync |
| **Omnisearch** | `omnisearch` | ⭐ BM25 relevance-ranked, typo-tolerant search across notes **and PDFs/Office/images** (needs Text Extractor for PDF content); insert links from results; optional local query server |
| Tag Wrangler | `tag-wrangler` *(search by name)* | Rename/merge `#flashcards/organic/...` in bulk |
| Iconize | `obsidian-icon-folder` | ⚗ icons per branch folder, ✅ on chapters that have notes |
| Homepage | `homepage` | Open on your dashboard note (`Progress.md`) at launch |
| Calendar | `calendar` | Sidebar calendar over daily notes — revision log |
| Bases | *core, Obsidian ≥ 1.9* | Native database views over note properties — a lighter Dataview alternative for the progress board |
| Waypoint / Folder notes / Breadcrumbs | *(search by name)* | Auto-generated folder landing pages and hierarchy trails for the 36 chapter folders |

---

## 10. Category H — AI inside Obsidian (optional)

Arena AI is already the authoring engine for these files, so in-vault AI is for *asking questions
while revising*, not for writing the notes.

| Plugin | ID | Notes |
|---|---|---|
| Claudian | `realclaudian` | AI chat in-vault for Claude and other providers (Codex, Grok, Opencode, Pi); `@`-mention notes/folders/files, **MCP servers**, plan mode, forked sessions, shared prompt templates. 2.2 M downloads |
| Copilot | `copilot` | Chat with your notes, vault-wide QA, quick edits on selected text, ingests web/YouTube/images/**PDFs**/EPUB; Plus adds an agent that calls tools |
| Smart Composer · Text Generator · Smart Connections | *(search by name)* | Cursor-style @-mention chat with semantic vault search; prompt templates; embedding-based "related notes" |

> **Which PDF-aware AI plugin?** If you want to ask questions *of* the Allen module PDFs,
> **Copilot** ingests PDFs directly. Otherwise convert once with **Marker PDF to MD** and let
> Arena AI work on the resulting markdown — better for a git-based workflow, since the text
> becomes diffable and reusable.

---

## 11. Category I — Appearance and printing

| Plugin | ID | Notes |
|---|---|---|
| Minimal Theme Settings | `obsidian-minimal-settings` | Colour schemes, fonts, widths for the Minimal theme |
| Style Settings | `obsidian-style-settings` | Exposes CSS-snippet/theme options as a settings pane. Use it to give **🆇 / 🅰 / ⚠ markers distinct colours** so Advanced-only points and traps pop |
| Enhancing Export | `obsidian-enhancing-export` | Pandoc → PDF/DOCX/HTML for printing revision sheets |
| PDF Break Page | `break-page` | Page breaks in exported PDFs |

A CSS snippet that colours the house markers (`.obsidian/snippets/markers.css`):

```css
/* @settings
name: Chemistry note markers
id: chem-markers
settings:
  - { id: chem-marker-on, title: Highlight 🆇 / 🅰 / ⚠ markers, type: class-toggle, default: true }
*/
body.chem-marker-on {
  --chem-adv: #f59e0b;   /* 🆇 JEE Advanced */
  --chem-allen: #3b82f6; /* 🅰 Allen-only   */
  --chem-trap: #ef4444;  /* ⚠ trap          */
}
```

---

## 12. Dataview dashboard — "what's left to write"

Put this in a root `Progress.md`. It reads files, not READMEs, so it is always current:

````markdown
```dataview
TABLE WITHOUT ID
  file.folder                 AS "Chapter",
  round(file.size / 1024, 1)  AS "KB",
  file.mtime                  AS "Last edited"
FROM ""
WHERE file.name = "notes"
SORT file.folder ASC
```

**Chapters still pending:**

```dataviewjs
// DQL has no file.content field, so this needs DataviewJS (enable it in Dataview settings)
const cards = dv.pages('"Physical-Chemistry" or "Inorganic-Chemistry" or "Organic-Chemistry"')
  .where(p => p.file.name === "README" && p.file.folder.split("/").length === 2)
  .sort(p => p.file.folder);
const pending = [];
for (const p of cards) {
  const body = await dv.io.load(p.file.path);
  if (body.includes("Add your notes for this chapter below")) pending.push(p.file.link);
}
dv.header(4, `${pending.length} chapters pending`);
dv.list(pending);
```
````

The second query keys off the exact placeholder that `scripts/fetch_ncert_pdfs.py` writes into a
chapter card when `notes.md` does not exist — so the list is derived from the same fact the
script uses.

---

## 13. Templater template in this repo's house style

Save as `_templates/chapter-notes.md`, then run *Templater → Create new note from template*
inside a chapter folder:

````markdown
---
created: <% tp.date.now("YYYY-MM-DD") %>
branch: <% tp.file.path(true).split("/")[0] %>
chapter: <% tp.file.folder(true) %>
status: draft
---

# <% tp.file.folder(true).replace(/^\d+-/, "").replace(/-/g, " ") %> — JEE Main + Advanced Notes

> **Sources merged into these notes**
> | Source | File |
> |---|---|
> | NCERT chapter PDF | []( ) |
> | Allen module for this chapter | _not uploaded yet — drop it in this folder and the 🅰 tags below get filled in_ |
>
> Section numbers below follow the NCERT unit exactly, so you can read the PDF and these notes
> side by side. 🅰 = Allen-only · 🆇 = extra JEE-Advanced point · ⚠ = trap that appears in papers.

## Contents

- [Part A — ](#part-a--)
  1. [](#)

---

# Part A —

## 1.  (NCERT §)

---

## Quick Revision Sheet

-

---

*Cross-links:* [branch index](../README.md)
````

| Marker | Meaning (house convention) |
|---|---|
| 🅰 | Point from the **Allen module**, not NCERT |
| 🆇 | Point **beyond NCERT** needed for JEE Advanced |
| ⚠ | Trap / common wrong answer |
| `(8.7.5)` | NCERT's own section number, so notes and PDF line up |

---

## 14. Vault settings for this repo

| Setting | Value | Why |
|---|---|---|
| Files & Links → **Use [[Wikilink]]** | **off** | The repo uses relative markdown links so every file also renders on GitHub |
| Files & Links → New link format | Relative path to file | Survives `git mv` of a chapter folder |
| Files & Links → Default attachment location | *In subfolder under current folder* → `figures` | Pasted images/exports land in `figures/`, which the fetch script does not scan. Allen module PDFs are still dropped by hand into the chapter folder itself — that is how the script detects them as `Module PDF` rows |
| Editor → **Strict line breaks** | **on** | The notes hard-wrap prose at ~100 columns. GitHub joins those lines into one paragraph; Obsidian only does so with this **on** (off = every wrapped line becomes a visible break) |
| Editor → Line wrap | on | Long tables and ASCII blocks stay scannable |
| Editor → Properties in document | Source or hidden | Chapter cards use metadata *tables*, not YAML — keep them readable |
| Core plugins → PDF viewer, Canvas, Backlinks, Outline, Tags, Bases | on | Canvas is genuinely good for a chapter map |

### `.gitignore` additions

The full, final version (with the whitelist of shareable plugin settings) is in
[`OBSIDIAN-VAULT-PLAN.md`](OBSIDIAN-VAULT-PLAN.md) Phase 1.

```gitignore
# Obsidian — share the plugin list, ignore personal state
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.obsidian/plugins/*/*
.obsidian/cache/
.trash/
```

### Ready-to-paste `community-plugins.json` (verified IDs only)

```json
[
  "obsidian-git",
  "dataview",
  "table-editor-obsidian",
  "obsidian-latex-suite",
  "obsidian-excalidraw-plugin",
  "chemedit",
  "pdf-plus",
  "obsidian-spaced-repetition",
  "templater-obsidian",
  "omnisearch"
]
```

---

## 15. Arena-AI playbook — prompts that exploit these plugins

| You want | Ask Arena AI for |
|---|---|
| Notes that render in Obsidian *and* GitHub | "Keep Unicode subscripts in prose; use LaTeX only for real maths; markdown links, no wikilinks" |
| Personal study files with full Obsidian syntax | "Write `cards.md` using `\ce{}`, `> [!warning]` callouts and `Question::Answer` cards" |
| Real structures instead of ASCII | "Give me SMILES strings for every compound in this section so ChemEdit/Chem can render them" |
| Mechanisms you can draw over | "Add an Excalidraw placeholder + a numbered arrow-pushing sequence I can sketch" |
| Feed a module PDF to the AI | Convert with **Marker PDF to MD** (`marker-api`), drop the `.md` in the chapter folder, then ask Arena AI to merge it into `notes.md` with 🅰 tags |
| Live progress | "Add `Progress.md` with the Dataview queries from §12" |
| Printable revision | "Export the Quick Revision Sheets of the finished chapters to one PDF" (Enhancing Export + break-page) |

---

## 16. Full index of every plugin mentioned (alphabetical, with IDs)

`advanced tables → table-editor-obsidian` · `anki integration (search)` · `annotator → obsidian-annotator` ·
`any block → any-block` · `aosr → aosr` · `auto anki (search)` · `bases (core ≥1.9)` ·
`better pdf → better-pdf-plugin` · `better recall (search)` · `breadcrumbs (search)` · `brat → obsidian42-brat (verify)` ·
`calendar → calendar` · `chem → chem` · `chemedit → chemedit` · `chemedit universal (search)` ·
`chemical structure renderer → chemical-structure-renderer` · `chemsearch → chem-search` ·
`cicada synchronizer → cicada-sync` · `claudian → realclaudian` · `come through → come-through` ·
`consistent attachments and links (search)` · `copilot → copilot` · `copy as latex (search)` ·
`csv table → obsidian-csv-table` · `dataview → dataview` · `decks → decks` · `downloadpdf → downloadpdf` ·
`draw.io → drawio` · `editing toolbar → editing-toolbar` · `enhancing export → obsidian-enhancing-export` ·
`excalidraw → obsidian-excalidraw-plugin` · `excalidraw extras (search)` · `export graph view → export-graph-view` ·
`export to tex (search)` · `extended mathjax (search)` · `extract pdf annotations → obsidian-extract-pdf-annotations` ·
`fit → fit` · `flashcards → flashcards-obsidian` · `flashcards llm (search)` · `folder notes (search)` ·
`git → obsidian-git` · `git changelog → git-changelog` · `git integration → git-integration` ·
`git url → git-url` · `githobs → githobs` · `homepage → homepage` · `iconize → obsidian-icon-folder` ·
`image2latex (search)` · `importer → obsidian-importer` · `json table → json-table` ·
`kanban → obsidian-kanban` · `ketcher → ketcher` · `latex suite → obsidian-latex-suite` ·
`learnkit → learnkit` · `linter → obsidian-linter` · `llm summary → llm-summary` ·
`marker pdf to md → marker-api` · `markmind → obsidian-markmind` · `mermaid (core)` ·
`mermaid link navigator → mermaid-link-nav` · `mermaid popup → mermaid-popup` · `mermaid tools → mermaid-tools` ·
`mhchem (core)` · `minimal theme settings → obsidian-minimal-settings` · `omnisearch → omnisearch` ·
`outliner → obsidian-outliner` · `pdf break page → break-page` · `pdf++ → pdf-plus` · `pdf2image → pdf2img` ·
`pdf folder to markdowns → pdf-folder-to-markdowns` · `periodic table → periodic-table` ·
`quickadd → quickadd` · `remotely save → remotely-save` · `repeat → repeat-plugin` ·
`sheets extended → sheets` · `show diff → show-diff` · `slide note → slide-note` ·
`smart composer (search)` · `smart connections (search)` · `spaced repetition → obsidian-spaced-repetition` ·
`sprout (search)` · `style settings → obsidian-style-settings` · `swiftlatex render → swiftlatex-render` ·
`table checkboxes → table-checkboxes` · `table generator → obsidian-table-generator` · `tabsdown → tabsdown` ·
`tag wrangler (search)` · `tasknotes → tasknotes` · `tasks → obsidian-tasks-plugin` ·
`templater → templater-obsidian` · `text extractor → text-extractor` · `text generator (search)` ·
`the queue (search)` · `tikzjax → tikzjax` · `waypoint (search)` · `yanki → yanki`

**96 entries catalogued** — 73 with registry-verified IDs, 23 install-by-name, 3 of them Obsidian
*core* features (mhchem, Mermaid, Bases). **10 recommended** in §0. The single most important
finding: rendering these notes needs **no plugin at all** — `\ce{}` (mhchem), Mermaid and MathJax
are bundled with Obsidian core.
