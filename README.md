# Chem_JEEAd_notes — Physical + Inorganic Only

Chemistry notes for **JEE Main + JEE Advanced**, focused on **Physical and Inorganic Chemistry only**. Organic Chemistry chapters have been removed as per current study focus. Every NCERT chapter lives inside `Physical-Chemistry/` or `Inorganic-Chemistry/`.

## Layout

Each chapter has **one folder** holding everything for that chapter — no Class-11/Class-12 level; the class and the NCERT unit number are recorded inside each chapter's `README.md` and in the branch index.

```
Physical-Chemistry/           # 12 chapters   Inorganic-Chemistry/  # 9
├── README.md                 # index         ├── README.md
├── 01-Some-Basic-Concepts-of-Chemistry/      ├── 01-Classification-of-Elements-and-Periodicity-in-Properties/
├── 02-Structure-of-Atom/                    ├── 02-Chemical-Bonding-and-Molecular-Structure/
├── 03-Thermodynamics/                       ├── 03-Hydrogen/   # Advanced-only
├── 04-Equilibrium/          ← chemical + ionic equilibrium  ├── 04-The-s-Block-Elements/
│   ├── kech106.pdf         # the NCERT chapter PDF         ├── 05-The-p-Block-Elements/ (13-14)
│   ├── README.md           # chapter card                  ├── 06-Environmental-Chemistry/
│   └── notes.md            # combined NCERT + Allen notes  ├── 07-The-d-and-f-Block-Elements/
├── 05-Redox-Reactions/                          │   ├── lech104.pdf
├── 06-States-of-Matter/     # Advanced-only (legacy NCERT)  │   ├── d-Block_Theory_26.pdf
├── 07-Solutions/                                │   └── notes.md
├── 08-Electrochemistry/                         ├── 08-Coordination-Compounds/
├── 09-Chemical-Kinetics/                        └── 09-The-p-Block-Elements/ (15-18)
├── 10-The-Solid-State/      ├── Practical-Chemistry/
├── 11-Surface-Chemistry/    │   └── Salt-Analysis/   (not an NCERT chapter, but kept)
└── 12-General-Principles-and-Processes-of-Isolation-of-Elements/
```

- **Chapter numbers are per branch**, in Class XI → Class XII order by NCERT unit. So `04-Equilibrium` here is NCERT Class XI **Unit 6** — the folder number is *not* the NCERT unit number. Each `README.md` and each branch index carry the real unit number and the NCERT code, and the codes are what NCERT itself uses (`kech1xx` = Class XI Part I, `kech2xx` = Class XI Part II, `lech1xx`/`lech2xx` likewise for Class XII).
- **Notes convention:** one single `notes.md` per chapter, written from **both** the NCERT chapter and the Allen module, re-checked against the JEE Main → JEE Advanced syllabus so nothing is left out. Diagrams are inline (ASCII + Mermaid). `🅰` marks a point that comes from the Allen module and not NCERT, `🆇` marks an extra JEE Advanced point; `⚠` marks a trap.
- **Which branch owns which chapter** is one dict — `BRANCH_OF` in [`scripts/fetch_ncert_pdfs.py`](scripts/fetch_ncert_pdfs.py):

  | Branch | Chapters |
  |---|---|
  | **Physical** | Some Basic Concepts, Structure of Atom, Thermodynamics, Equilibrium, Redox Reactions, States of Matter · Solutions, Electrochemistry, Chemical Kinetics, The Solid State, Surface Chemistry, Isolation of Elements (Metallurgy) |
  | **Inorganic** | Classification & Periodicity, Chemical Bonding, Hydrogen, s-Block, p-Block (13–14), Environmental Chemistry · d- and f-Block, Coordination Compounds, p-Block (15–18) |

  Two judgement calls are deliberate: Solid State, Surface Chemistry and Metallurgy are filed under **Physical** (lattice/kinetic/process chemistry); Chemical Bonding, Hydrogen and Environmental Chemistry stay **Inorganic**. To move a chapter, edit `BRANCH_OF` and re-run the script — it prints the new numbering with `--layout`; you then `git mv` the folder and fix the (rare) cross-chapter links.

## Notes status — Physical + Inorganic Only

**Total chapters in repo now: 21 (12 Physical + 9 Inorganic)**

| Branch | Total Chapters | Notes Made | Notes Pending |
|---|---|---|---|
| Physical Chemistry | 12 | 3 | 9 |
| Inorganic Chemistry | 9 | 2 | 7 |
| **Total** | **21** | **5** | **16** |
| Practical Chemistry (extra) | 1 (Salt Analysis) | 1 | 0 |
| **Grand Total with Practical** | **22** | **6** | **16** |

### Detailed Notes List

| # | Chapter folder | Allen module in the folder | Notes |
|---|---|---|---|
| P-04 | [`Physical-Chemistry/04-Equilibrium`](Physical-Chemistry/04-Equilibrium/notes.md) | _none uploaded yet_ | ✅ written (NCERT + 🆇 extras; covers chemical **and** ionic equilibrium) |
| P-05 | [`Physical-Chemistry/05-Redox-Reactions`](Physical-Chemistry/05-Redox-Reactions/notes.md) | _none uploaded yet_ | ✅ written (NCERT + 🆇 extras) |
| P-08 | [`Physical-Chemistry/08-Electrochemistry`](Physical-Chemistry/08-Electrochemistry/notes.md) | _none uploaded yet_ | ✅ written (NCERT + 🆇 extras) |
| I-07 | [`Inorganic-Chemistry/07-The-d-and-f-Block-Elements`](Inorganic-Chemistry/07-The-d-and-f-Block-Elements/notes.md) | `d-Block_Theory_26.pdf` | ✅ written |
| I-08 | [`Inorganic-Chemistry/08-Coordination-Compounds`](Inorganic-Chemistry/08-Coordination-Compounds/notes.md) | `3-JAEIC-Coordination Compound_Eng.pdf.pdf` | ✅ written |
| Prac | [`Practical-Chemistry/Salt-Analysis`](Practical-Chemistry/Salt-Analysis/notes.md) | `Salt Analysis_Theory_26.pdf` + `Reaction of Salt Analysis_Theory_26.pdf` | ✅ written |

**Pending Notes (16 chapters):**

*Physical-Chemistry (9 pending):*
- 01-Some-Basic-Concepts-of-Chemistry
- 02-Structure-of-Atom
- 03-Thermodynamics
- 06-States-of-Matter (Advanced only)
- 07-Solutions
- 09-Chemical-Kinetics
- 10-The-Solid-State (Advanced only)
- 11-Surface-Chemistry (Advanced only)
- 12-General-Principles-and-Processes-of-Isolation-of-Elements (Advanced only)

*Inorganic-Chemistry (7 pending):*
- 01-Classification-of-Elements-and-Periodicity-in-Properties
- 02-Chemical-Bonding-and-Molecular-Structure
- 03-Hydrogen (Advanced only)
- 04-The-s-Block-Elements (Advanced only)
- 05-The-p-Block-Elements (Groups 13-14) (Advanced only)
- 06-Environmental-Chemistry (Advanced only)
- 09-The-p-Block-Elements (Groups 15-18) (Advanced only)

Where no Allen module exists yet, `notes.md` is built from the NCERT chapter alone and every beyond-NCERT point is marked 🆇 instead of 🅰. New Allen modules should be dropped into the matching chapter folder as they are uploaded.

For a quick auto-generated summary, see [`NOTES_LIST.md`](NOTES_LIST.md).

## NCERT editions — why there are two

The two exams are not aligned on NCERT:

- **JEE Main** follows the **rationalised NCERT (2023+)** — originally 19 chemistry chapters (Class XI: 9, Class XII: 10). In this repo we now keep **12** of those (8 Physical + 4 Inorganic).
- **JEE Advanced** still tests material that rationalisation deleted from the textbooks: States of Matter, Hydrogen, s-Block, p-Block, Environmental Chemistry, The Solid State, Surface Chemistry, Metallurgy. Those come from the **pre-rationalisation (2018-19) NCERT** and are marked *Advanced only* in the branch indexes ([Physical](Physical-Chemistry/README.md), [Inorganic](Inorganic-Chemistry/README.md)). We keep **9** legacy chapters (4 Physical + 5 Inorganic).

**Now: 21 chapters total (12 rationalised + 9 legacy). Previously 30 with Organic, now 21 without.**

> **Careful with the NCERT codes.** Because the rationalised books are shorter, NCERT reused codes — `kech105` was *States of Matter* and is now *Thermodynamics*, `lech101` was *The Solid State* and is now *Solutions*. Legacy PDFs are therefore named `<code>-legacy.pdf`.

## Refreshing the NCERT PDFs

```bash
pip install pypdf                     # only needed for the verification step
python3 scripts/fetch_ncert_pdfs.py             # download + regenerate all READMEs/indexes
python3 scripts/fetch_ncert_pdfs.py --force     # re-download everything
python3 scripts/fetch_ncert_pdfs.py --verify    # check the PDFs on disk
python3 scripts/fetch_ncert_pdfs.py --layout    # print NCERT unit -> branch/folder
```

PDFs come from <https://ncert.nic.in/textbook.php> when it is reachable, and otherwise from GitHub mirrors of the same NCERT files. Every downloaded file is checked: it must be a valid PDF and its opening pages must contain the chapter title. Set `GITHUB_TOKEN` to raise the API rate limit.

> The script owns the two branch indexes and every chapter `README.md`, and it is what keeps the chapter numbering consistent. It **never** touches the `notes.md` files or the Allen module PDFs. Organic chapters are now excluded by design.

## Copyright

All NCERT PDFs are NCERT's own chapter files, published by the National Council of Educational Research and Training, Government of India, and made freely available for educational use — see <https://ncert.nic.in/copyright.php>.
Allen module PDFs are study material owned by ALLEN Career Institute Pvt. Ltd., kept here for personal study only.
