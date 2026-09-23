# Notes Made — List of Chapters

**Focus: Physical Chemistry + Inorganic Chemistry only (Organic removed)**

Generated on: 2026-05-13 (auto-check of `notes.md` files)

## Summary Counts

| Branch | Total Chapters | ✅ Notes Completed | ⏳ Pending | Completion % |
|---|---|---|---|---|
| **Physical-Chemistry** | 12 | 3 | 9 | 25.0% |
| **Inorganic-Chemistry** | 9 | 2 | 7 | 22.2% |
| **Total (P + I)** | **21** | **5** | **16** | **23.8%** |
| Practical-Chemistry (extra) | 1 | 1 | 0 | 100% |
| **Grand Total** | **22** | **6** | **16** | **27.3%** |

## ✅ Completed Notes (6 total)

### Physical Chemistry — 3 notes

| # | Chapter | Folder | Notes File | Allen Module |
|---|---|---|---|---|
| P-04 | Equilibrium (Chemical + Ionic) | `Physical-Chemistry/04-Equilibrium/` | [`notes.md`](Physical-Chemistry/04-Equilibrium/notes.md) | _none_ |
| P-05 | Redox Reactions | `Physical-Chemistry/05-Redox-Reactions/` | [`notes.md`](Physical-Chemistry/05-Redox-Reactions/notes.md) | _none_ |
| P-08 | Electrochemistry | `Physical-Chemistry/08-Electrochemistry/` | [`notes.md`](Physical-Chemistry/08-Electrochemistry/notes.md) | _none_ |

### Inorganic Chemistry — 2 notes

| # | Chapter | Folder | Notes File | Allen Module |
|---|---|---|---|---|
| I-07 | The d- and f-Block Elements | `Inorganic-Chemistry/07-The-d-and-f-Block-Elements/` | [`notes.md`](Inorganic-Chemistry/07-The-d-and-f-Block-Elements/notes.md) | `d-Block_Theory_26.pdf` |
| I-08 | Coordination Compounds | `Inorganic-Chemistry/08-Coordination-Compounds/` | [`notes.md`](Inorganic-Chemistry/08-Coordination-Compounds/notes.md) | `3-JAEIC-Coordination Compound_Eng.pdf.pdf` |

### Practical Chemistry — 1 note

| Chapter | Folder | Notes File | Allen Module |
|---|---|---|---|
| Salt Analysis | `Practical-Chemistry/Salt-Analysis/` | [`notes.md`](Practical-Chemistry/Salt-Analysis/notes.md) | `Salt Analysis_Theory_26.pdf` + `Reaction of Salt Analysis_Theory_26.pdf` |

---

## ⏳ Pending Notes (16 chapters)

### Physical Chemistry — 9 pending

| # | Chapter | Class | NCERT Code | Edition | Needed For |
|---|---|---|---|---|---|
| 01 | Some Basic Concepts of Chemistry | 11 | `kech101` | rationalised | Main + Advanced |
| 02 | Structure of Atom | 11 | `kech102` | rationalised | Main + Advanced |
| 03 | Thermodynamics | 11 | `kech105` | rationalised | Main + Advanced |
| 06 | States of Matter | 11 | `kech105-legacy` | legacy 2018-19 | Advanced only |
| 07 | Solutions | 12 | `lech101` | rationalised | Main + Advanced |
| 09 | Chemical Kinetics | 12 | `lech103` | rationalised | Main + Advanced |
| 10 | The Solid State | 12 | `lech101-legacy` | legacy 2018-19 | Advanced only |
| 11 | Surface Chemistry | 12 | `lech105-legacy` | legacy 2018-19 | Advanced only |
| 12 | General Principles and Processes of Isolation of Elements (Metallurgy) | 12 | `lech106-legacy` | legacy 2018-19 | Advanced only |

### Inorganic Chemistry — 7 pending

| # | Chapter | Class | NCERT Code | Edition | Needed For |
|---|---|---|---|---|---|
| 01 | Classification of Elements and Periodicity in Properties | 11 | `kech103` | rationalised | Main + Advanced |
| 02 | Chemical Bonding and Molecular Structure | 11 | `kech104` | rationalised | Main + Advanced |
| 03 | Hydrogen | 11 | `kech202-legacy` | legacy 2018-19 | Advanced only |
| 04 | The s-Block Elements | 11 | `kech203-legacy` | legacy 2018-19 | Advanced only |
| 05 | The p-Block Elements (Groups 13 and 14) | 11 | `kech204-legacy` | legacy 2018-19 | Advanced only |
| 06 | Environmental Chemistry | 11 | `kech207-legacy` | legacy 2018-19 | Advanced only |
| 09 | The p-Block Elements (Groups 15 to 18) | 12 | `lech107-legacy` | legacy 2018-19 | Advanced only |

---

## Removed — Organic Chemistry (9 chapters)

These chapters were deleted from this repo as per user request to focus only on Physical + Inorganic:

| # | Chapter | Class | Code |
|---|---|---|---|
| 01 | Organic Chemistry: Some Basic Principles and Techniques | 11 | `kech202` |
| 02 | Hydrocarbons | 11 | `kech203` |
| 03 | Haloalkanes and Haloarenes | 12 | `lech201` |
| 04 | Alcohols, Phenols and Ethers | 12 | `lech202` |
| 05 | Aldehydes, Ketones and Carboxylic Acids | 12 | `lech203` |
| 06 | Amines | 12 | `lech204` |
| 07 | Biomolecules | 12 | `lech205` |
| 08 | Polymers (Advanced only) | 12 | `lech207-legacy` |
| 09 | Chemistry in Everyday Life (Advanced only) | 12 | `lech208-legacy` |

> If you need Organic back, restore from `main` branch: `git checkout main -- Organic-Chemistry` and add back entries in `scripts/fetch_ncert_pdfs.py`.

---

## How to check

```bash
find . -name "notes.md" | sort
python3 scripts/fetch_ncert_pdfs.py --verify
python3 scripts/fetch_ncert_pdfs.py --layout
```
