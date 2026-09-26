# Open this repository as an Obsidian vault

1. Install **Obsidian desktop**, Git, then clone this repository and choose **Open folder as vault** at the repository root (the folder containing `.obsidian/`). On mobile use a local clone or your preferred one-way sync; do not run two sync engines on the same folder.
2. Settings → Community plugins → disable Restricted mode → Browse and install the plugins below. Obsidian cannot automatically install plugins merely because they are mentioned in this repository; `.obsidian/community-plugins.json` intentionally starts empty to avoid enabling missing plugins.
3. Enable `chem-notes` under Settings → Appearance → CSS snippets. Open [Redox reaction gallery](../Physical-Chemistry/05-Redox-Reactions/figures/reactions.md) in Reading view. `\ce` rendering is **built into Obsidian**; no chemistry plugin is required to typeset an ionic equation. For SMILES structure drawings install **Chem**; ChemEdit is desktop-only on many Android devices.
4. Install **Git** (`obsidian-git`): pull on startup, auto-pull every 10 minutes if you want, but leave auto-commit-and-sync **off**. Commit and push manually after reviewing diffs. Keep your local vault on your own branch (normally `main`); merge the Arena working branch by PR first, then pull your branch. Do not have Obsidian Git auto-push to an Arena session branch.

## Plugins to install

| Priority | Plugin (community ID) | Use here |
|---|---|---|
| Required for Git workflow | Git (`obsidian-git`) | Pull, inspect diffs, manually commit/push |
| Recommended | Chem (`chem`) | Render SMILES blocks in redox structure gallery and cards |
| Desktop only | ChemEdit (`chemedit`) | Edit Ketcher-compatible SVGs; **not required or recommended on Android** |
| Recommended | Dataview (`dataview`) | [Progress dashboard](Progress.md) |
| Recommended | Spaced Repetition (`obsidian-spaced-repetition`) | [Redox flashcards](../Physical-Chemistry/05-Redox-Reactions/cards.md) |
| Optional | LaTeX Suite (`obsidian-latex-suite`) | Faster entry of MathJax and `\ce` reaction equations |
| Optional | Excalidraw (`obsidian-excalidraw-plugin`) | Curved-arrow mechanisms; export SVG alongside editable source for GitHub |
| Optional | Advanced Tables (`table-editor-obsidian`) | Edit dense comparison tables |
| Optional | PDF++ (`pdf-plus`) | Annotate NCERT PDFs in the vault |
| Optional | Templater (`templater-obsidian`) | Scaffold future notes from `meta/templates` (set template folder there) |

**On Android, skip ChemEdit.** Use the built-in MathJax renderer for equations, Chem for SMILES (if compatible with your Obsidian version), and Excalidraw only if its mobile UI works for you. **Do not install a plugin just to display the reaction gallery:** MathJax/mhchem ships with Obsidian. The Redox note now uses `\ce` too; GitHub may show those equations as raw source. [Full plugin catalogue](../docs/OBSIDIAN-SETUP.md) covers additional options; those are not prerequisites.

## Git safety

`.obsidian/` shared app settings and snippets are tracked. Workspace layouts and downloaded plugin code/settings are ignored to avoid merge noise and accidental secret leaks. The vault is still ordinary Markdown and PDF; no files moved and the NCERT fetch script can still regenerate chapter cards. On a second machine, install plugins yourself and configure their settings locally. If Git reports conflicts, resolve them before committing; never force-push over another editor's changes.
