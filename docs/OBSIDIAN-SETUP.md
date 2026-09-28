# Using this repository as an Obsidian vault

The repository is plain Markdown and PDF, so it opens directly as an Obsidian vault and
reads identically on GitHub. Obsidian's **core** already renders everything these notes
use — GFM tables, Mermaid, MathJax including mhchem `\ce{}`, and callouts. This page is
the short version: how to open the vault, what to install, and the one portability rule.

For the note format itself, see [`NOTE-FORMATTING-RULEBOOK.md`](NOTE-FORMATTING-RULEBOOK.md).

## 1. Open the vault

1. Install **Obsidian desktop** and **Git**, then clone this repository and choose
   **Open folder as vault** at the repository root — the folder containing `.obsidian/`.
2. Settings → Community plugins → turn off **Restricted mode**.
3. Under **Appearance → CSS snippets**, enable `chem-notes`.

On mobile, use a local clone or your preferred one-way sync. Do not run two sync engines
on the same folder.

## 2. Install plugins

Obsidian cannot install a plugin just because this repository mentions it, so
`.obsidian/community-plugins.json` deliberately starts empty — enabling a missing plugin
breaks the vault on first open. Install these from **Settings → Community plugins →
Browse**, then enable them.

| Priority | Plugin (community ID) | Use here |
|---|---|---|
| Required for the Git workflow | Git (`obsidian-git`) | Pull the AI-written notes, commit your own edits |
| Recommended | Dataview (`dataview`) | [Progress dashboard](../meta/Progress.md) |
| Recommended | Spaced Repetition (`obsidian-spaced-repetition`) | [Redox flashcards](../Physical-Chemistry/05-Redox-Reactions/cards.md) |
| Recommended for mobile | Scrolling (`scrolling`) | Stops long Latimer diagrams and calculations from wrapping |
| Recommended | Chem (`chem`) | Renders the SMILES blocks in the Redox gallery and cards (turn on **Inline SMILES** in its settings) |
| Desktop only | ChemEdit (`chemedit`) | Opens the committed SVGs in a Ketcher-compatible editor |
| Optional | Advanced Tables (`table-editor-obsidian`) | Editing the dense comparison tables |
| Optional | LaTeX Suite (`obsidian-latex-suite`) | Faster MathJax and `\ce{}` entry |
| Optional | Excalidraw (`obsidian-excalidraw-plugin`) | Curved-arrow mechanisms; save the SVG next to the source so GitHub still shows it |
| Optional | PDF++ (`pdf-plus`) | Annotates the NCERT and Allen PDFs that live in this vault |
| Optional | Templater (`templater-obsidian`) | Scaffolds new notes from `meta/templates` — set the template folder there |
| Optional | Omnisearch (`omnisearch`) | Typo-tolerant search across notes and PDFs |

**On Android, skip ChemEdit.** Use the built-in MathJax renderer for equations, Chem for
SMILES if your Obsidian version supports it, and Excalidraw only if its mobile UI works
for you. Do not install anything just to display a reaction: MathJax and mhchem ship with
Obsidian.

### Chem and ChemEdit together

Both claim the same `smiles` code blocks, and only one wins. **ChemEdit** opens the
committed `.svg` structure files for editing; **Chem** renders inline `smiles` blocks. If
your SMILES blocks come out blank, disable one of the two — ChemEdit is the one to drop on
mobile.

Opening a drawing in Ketcher: double-clicking an embedded image may not launch the editor.
Right-clicking the `.svg` file → **Edit SVG in Ketcher** is the documented fallback.

## 3. Git settings

`obsidian-git` is the bridge between the notes written in the repository and the vault you
read. Use these settings:

| Setting | Value | Why |
|---|---|---|
| Pull on startup | ✔ | so links resolve before Obsidian indexes the vault |
| Auto-pull interval | 10 min | picks up new notes without a manual pull |
| **Auto commit and sync** | **off** | review every diff before it leaves your machine |
| Commit message | `vault: {{date}}` | distinguishes your commits from the notes' own history |

Keep your vault on your own branch (normally `main`). Merge the Arena working branch by PR
first, then pull. **Never** let Obsidian Git auto-push to an Arena session branch.

## 4. What is tracked in `.obsidian/`

App settings and the CSS snippet are tracked so every machine looks the same. Personal
state and plugin code are ignored (`.gitignore`):

```gitignore
.obsidian/workspace*.json     # per-device layout
.obsidian/plugins/            # downloaded plugin code and settings — install locally
.obsidian/themes/
.obsidian/cache/
```

Never commit a plugin's settings file wholesale: `obsidian-git`, remote-sync and
API-backed plugins can hold an author name, a remote URL or an access token there. On a
second machine, install the plugins yourself and configure them locally.

## 5. The portability rule

`\ce{}` equation blocks and `[[wikilinks]]` are **Obsidian-only**. Anything committed to
this repository uses Unicode subscripts (`Na⁺`, `H₂SO₄`) and ordinary Markdown links, so it
renders on GitHub with no plugin at all. Use `\ce{}` only in files that are for your vault,
and keep the Unicode form in `notes.md`.

If Git reports a conflict, resolve it before committing — never force-push over another
editor's changes.

## 6. Dataview dashboard

[`meta/Progress.md`](../meta/Progress.md) is a live table of every chapter's branch, class,
unit, status, word count and last-updated date, built from the frontmatter of each
`notes.md`. It needs Dataview and nothing else.
