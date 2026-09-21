# Physical Chemistry — JEE (Main + Advanced)

One folder per NCERT chapter: the chapter PDF, any module PDF that has been
uploaded, and `notes.md` once written. Chapters are numbered in this branch's
own order (Class XI first, then Class XII, by NCERT unit).

| # | Chapter | Class | NCERT unit | Code | Edition | Needed for | Notes |
|---|---|---|---|---|---|---|---|
| 01 | [Some Basic Concepts of Chemistry](01-Some-Basic-Concepts-of-Chemistry) | 11 | 1 | `kech101` | rationalised | Main + Advanced | ⏳ pending |
| 02 | [Structure of Atom](02-Structure-of-Atom) | 11 | 2 | `kech102` | rationalised | Main + Advanced | ⏳ pending |
| 03 | [Thermodynamics](03-Thermodynamics) | 11 | 5 | `kech105` | rationalised | Main + Advanced | ⏳ pending |
| 04 | [Equilibrium](04-Equilibrium) | 11 | 6 | `kech106` | rationalised | Main + Advanced | [✅ notes.md](04-Equilibrium/notes.md) |
| 05 | [Redox Reactions](05-Redox-Reactions) | 11 | 7 | `kech201` | rationalised | Main + Advanced | [✅ notes.md](05-Redox-Reactions/notes.md) |
| 06 | [States of Matter](06-States-of-Matter) | 11 | 10 | `kech105` | legacy 2018-19 | **Advanced only** | ⏳ pending |
| 07 | [Solutions](07-Solutions) | 12 | 1 | `lech101` | rationalised | Main + Advanced | ⏳ pending |
| 08 | [Electrochemistry](08-Electrochemistry) | 12 | 2 | `lech102` | rationalised | Main + Advanced | [✅ notes.md](08-Electrochemistry/notes.md) |
| 09 | [Chemical Kinetics](09-Chemical-Kinetics) | 12 | 3 | `lech103` | rationalised | Main + Advanced | ⏳ pending |
| 10 | [The Solid State](10-The-Solid-State) | 12 | 11 | `lech101` | legacy 2018-19 | **Advanced only** | ⏳ pending |
| 11 | [Surface Chemistry](11-Surface-Chemistry) | 12 | 12 | `lech105` | legacy 2018-19 | **Advanced only** | ⏳ pending |
| 12 | [General Principles and Processes of Isolation of Elements (Metallurgy)](12-General-Principles-and-Processes-of-Isolation-of-Elements) | 12 | 13 | `lech106` | legacy 2018-19 | **Advanced only** | ⏳ pending |

The `#` column is this branch's own order. The NCERT unit number keeps its own
column because that is what the NCERT codes mean: `kech1xx` = Class XI Part I,
`kech2xx` = Class XI Part II, `lech1xx` / `lech2xx` likewise for Class XII.
The rationalised books are shorter, so NCERT reused codes — `kech105` was
*States of Matter* and is now *Thermodynamics*; `lech101` was *The Solid State*
and is now *Solutions*. Legacy chapter PDFs are therefore named
`<code>-legacy.pdf`. Full layout and notes conventions: [repo
README](../README.md).

Refresh with `python3 scripts/fetch_ncert_pdfs.py` (`--verify` checks the PDFs on
disk, `--layout` prints the NCERT-unit → branch mapping).
