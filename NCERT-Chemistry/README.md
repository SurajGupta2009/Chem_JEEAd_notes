# NCERT Chemistry for JEE (Main + Advanced)

One folder per NCERT chemistry chapter, each holding the chapter PDF.

- **JEE Main** follows the **rationalised NCERT (2023+)**: 19 chemistry chapters (Class XI: 9, Class XII: 10).
- **JEE Advanced** additionally covers topics that rationalisation deleted from the textbooks. Those 11 chapters are included from the **pre-rationalisation (2018-19) NCERT** and are marked *Advanced only*.

Total: **30 chapters** (Class XI: 14, Class XII: 16).

> **Careful with the NCERT codes.** The rationalised books are shorter, so codes were reused: `kech105` was *States of Matter* and is now *Thermodynamics*; `lech101` was *The Solid State* and is now *Solutions*. Legacy files are named `<code>-legacy.pdf` to keep the two apart.

Re-fetch or check everything with:

```bash
python3 scripts/fetch_ncert_pdfs.py            # download
python3 scripts/fetch_ncert_pdfs.py --verify   # check PDFs on disk
```

## Class 11

| # | Chapter | NCERT code | Edition | Needed for |
|---|---|---|---|---|
| 1 | [Some Basic Concepts of Chemistry](Class-11/01-Some-Basic-Concepts-of-Chemistry) | `kech101` | rationalised | Main + Advanced |
| 2 | [Structure of Atom](Class-11/02-Structure-of-Atom) | `kech102` | rationalised | Main + Advanced |
| 3 | [Classification of Elements and Periodicity in Properties](Class-11/03-Classification-of-Elements-and-Periodicity-in-Properties) | `kech103` | rationalised | Main + Advanced |
| 4 | [Chemical Bonding and Molecular Structure](Class-11/04-Chemical-Bonding-and-Molecular-Structure) | `kech104` | rationalised | Main + Advanced |
| 5 | [Thermodynamics](Class-11/05-Thermodynamics) | `kech105` | rationalised | Main + Advanced |
| 6 | [Equilibrium](Class-11/06-Equilibrium) | `kech106` | rationalised | Main + Advanced |
| 7 | [Redox Reactions](Class-11/07-Redox-Reactions) | `kech201` | rationalised | Main + Advanced |
| 8 | [Organic Chemistry: Some Basic Principles and Techniques](Class-11/08-Organic-Chemistry-Some-Basic-Principles-and-Techniques) | `kech202` | rationalised | Main + Advanced |
| 9 | [Hydrocarbons](Class-11/09-Hydrocarbons) | `kech203` | rationalised | Main + Advanced |
| 10 | [States of Matter](Class-11/10-States-of-Matter) | `kech105` | legacy 2018-19 | **Advanced only** |
| 11 | [Hydrogen](Class-11/11-Hydrogen) | `kech202` | legacy 2018-19 | **Advanced only** |
| 12 | [The s-Block Elements (Alkali and Alkaline Earth Metals)](Class-11/12-The-s-Block-Elements) | `kech203` | legacy 2018-19 | **Advanced only** |
| 13 | [The p-Block Elements (Groups 13 and 14)](Class-11/13-The-p-Block-Elements) | `kech204` | legacy 2018-19 | **Advanced only** |
| 14 | [Environmental Chemistry](Class-11/14-Environmental-Chemistry) | `kech207` | legacy 2018-19 | **Advanced only** |

## Class 12

| # | Chapter | NCERT code | Edition | Needed for |
|---|---|---|---|---|
| 1 | [Solutions](Class-12/01-Solutions) | `lech101` | rationalised | Main + Advanced |
| 2 | [Electrochemistry](Class-12/02-Electrochemistry) | `lech102` | rationalised | Main + Advanced |
| 3 | [Chemical Kinetics](Class-12/03-Chemical-Kinetics) | `lech103` | rationalised | Main + Advanced |
| 4 | [The d- and f-Block Elements](Class-12/04-The-d-and-f-Block-Elements) | `lech104` | rationalised | Main + Advanced |
| 5 | [Coordination Compounds](Class-12/05-Coordination-Compounds) | `lech105` | rationalised | Main + Advanced |
| 6 | [Haloalkanes and Haloarenes](Class-12/06-Haloalkanes-and-Haloarenes) | `lech201` | rationalised | Main + Advanced |
| 7 | [Alcohols, Phenols and Ethers](Class-12/07-Alcohols-Phenols-and-Ethers) | `lech202` | rationalised | Main + Advanced |
| 8 | [Aldehydes, Ketones and Carboxylic Acids](Class-12/08-Aldehydes-Ketones-and-Carboxylic-Acids) | `lech203` | rationalised | Main + Advanced |
| 9 | [Amines](Class-12/09-Amines) | `lech204` | rationalised | Main + Advanced |
| 10 | [Biomolecules](Class-12/10-Biomolecules) | `lech205` | rationalised | Main + Advanced |
| 11 | [The Solid State](Class-12/11-The-Solid-State) | `lech101` | legacy 2018-19 | **Advanced only** |
| 12 | [Surface Chemistry](Class-12/12-Surface-Chemistry) | `lech105` | legacy 2018-19 | **Advanced only** |
| 13 | [General Principles and Processes of Isolation of Elements (Metallurgy)](Class-12/13-General-Principles-and-Processes-of-Isolation-of-Elements) | `lech106` | legacy 2018-19 | **Advanced only** |
| 14 | [The p-Block Elements (Groups 15 to 18)](Class-12/14-The-p-Block-Elements) | `lech107` | legacy 2018-19 | **Advanced only** |
| 15 | [Polymers](Class-12/15-Polymers) | `lech207` | legacy 2018-19 | **Advanced only** |
| 16 | [Chemistry in Everyday Life](Class-12/16-Chemistry-in-Everyday-Life) | `lech208` | legacy 2018-19 | **Advanced only** |

## Sources

All PDFs are NCERT's own chapter files, published by the National Council of Educational Research and Training, Government of India, and made freely available for educational use. See <https://ncert.nic.in/copyright.php>.

They are fetched from <https://ncert.nic.in/textbook.php> when reachable, otherwise from GitHub mirrors of the same files (listed per chapter in each chapter README).
