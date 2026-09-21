# Inorganic Chemistry — JEE (Main + Advanced)

One folder per NCERT chapter: the chapter PDF, any module PDF that has been
uploaded, and `notes.md` once written. Chapters are numbered in this branch's
own order (Class XI first, then Class XII, by NCERT unit).

| # | Chapter | Class | NCERT unit | Code | Edition | Needed for | Notes |
|---|---|---|---|---|---|---|---|
| 01 | [Classification of Elements and Periodicity in Properties](01-Classification-of-Elements-and-Periodicity-in-Properties) | 11 | 3 | `kech103` | rationalised | Main + Advanced | ⏳ pending |
| 02 | [Chemical Bonding and Molecular Structure](02-Chemical-Bonding-and-Molecular-Structure) | 11 | 4 | `kech104` | rationalised | Main + Advanced | ⏳ pending |
| 03 | [Hydrogen](03-Hydrogen) | 11 | 11 | `kech202` | legacy 2018-19 | **Advanced only** | ⏳ pending |
| 04 | [The s-Block Elements (Alkali and Alkaline Earth Metals)](04-The-s-Block-Elements) | 11 | 12 | `kech203` | legacy 2018-19 | **Advanced only** | ⏳ pending |
| 05 | [The p-Block Elements (Groups 13 and 14)](05-The-p-Block-Elements) | 11 | 13 | `kech204` | legacy 2018-19 | **Advanced only** | ⏳ pending |
| 06 | [Environmental Chemistry](06-Environmental-Chemistry) | 11 | 14 | `kech207` | legacy 2018-19 | **Advanced only** | ⏳ pending |
| 07 | [The d- and f-Block Elements](07-The-d-and-f-Block-Elements) | 12 | 4 | `lech104` | rationalised | Main + Advanced | [✅ notes.md](07-The-d-and-f-Block-Elements/notes.md) |
| 08 | [Coordination Compounds](08-Coordination-Compounds) | 12 | 5 | `lech105` | rationalised | Main + Advanced | [✅ notes.md](08-Coordination-Compounds/notes.md) |
| 09 | [The p-Block Elements (Groups 15 to 18)](09-The-p-Block-Elements) | 12 | 14 | `lech107` | legacy 2018-19 | **Advanced only** | ⏳ pending |

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
