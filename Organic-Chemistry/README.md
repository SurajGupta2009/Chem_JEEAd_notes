# Organic Chemistry — JEE (Main + Advanced)

One folder per NCERT chapter: the chapter PDF, any module PDF that has been
uploaded, and `notes.md` once written. Chapters are numbered in this branch's
own order (Class XI first, then Class XII, by NCERT unit).

| # | Chapter | Class | NCERT unit | Code | Edition | Needed for | Notes |
|---|---|---|---|---|---|---|---|
| 01 | [Organic Chemistry: Some Basic Principles and Techniques](01-Organic-Chemistry-Some-Basic-Principles-and-Techniques) | 11 | 8 | `kech202` | rationalised | Main + Advanced | ⏳ pending |
| 02 | [Hydrocarbons](02-Hydrocarbons) | 11 | 9 | `kech203` | rationalised | Main + Advanced | ⏳ pending |
| 03 | [Haloalkanes and Haloarenes](03-Haloalkanes-and-Haloarenes) | 12 | 6 | `lech201` | rationalised | Main + Advanced | ⏳ pending |
| 04 | [Alcohols, Phenols and Ethers](04-Alcohols-Phenols-and-Ethers) | 12 | 7 | `lech202` | rationalised | Main + Advanced | ⏳ pending |
| 05 | [Aldehydes, Ketones and Carboxylic Acids](05-Aldehydes-Ketones-and-Carboxylic-Acids) | 12 | 8 | `lech203` | rationalised | Main + Advanced | ⏳ pending |
| 06 | [Amines](06-Amines) | 12 | 9 | `lech204` | rationalised | Main + Advanced | ⏳ pending |
| 07 | [Biomolecules](07-Biomolecules) | 12 | 10 | `lech205` | rationalised | Main + Advanced | ⏳ pending |
| 08 | [Polymers](08-Polymers) | 12 | 15 | `lech207` | legacy 2018-19 | **Advanced only** | ⏳ pending |
| 09 | [Chemistry in Everyday Life](09-Chemistry-in-Everyday-Life) | 12 | 16 | `lech208` | legacy 2018-19 | **Advanced only** | ⏳ pending |

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
