# Chem_JEEAd_notes

Chemistry notes for **JEE Main + JEE Advanced**.

## What is here

| Path | Contents |
|---|---|
| [`NCERT-Chemistry/`](NCERT-Chemistry/) | The NCERT chemistry chapter PDFs, one folder per chapter, with an [index](NCERT-Chemistry/README.md). |
| [`scripts/fetch_ncert_pdfs.py`](scripts/fetch_ncert_pdfs.py) | Re-downloads / re-checks every chapter PDF. |

```
NCERT-Chemistry/
├── README.md                 # index: chapter -> NCERT code -> edition -> exam
├── Class-11/                 # 14 chapters
│   ├── 01-Some-Basic-Concepts-of-Chemistry/
│   │   ├── kech101.pdf
│   │   └── README.md
│   └── ...
└── Class-12/                 # 16 chapters
    ├── 01-Solutions/
    │   ├── lech101.pdf
    │   └── README.md
    └── ...
```

## Why there are two NCERT editions

The two exams are not aligned on NCERT:

- **JEE Main** follows the **rationalised NCERT (2023+)** — 19 chemistry
  chapters (Class XI: 9, Class XII: 10).
- **JEE Advanced** still tests material that rationalisation deleted from the
  textbooks: States of Matter, Hydrogen, s-Block, p-Block, Environmental
  Chemistry, The Solid State, Surface Chemistry, Metallurgy, Polymers and
  Chemistry in Everyday Life. Those 11 chapters come from the
  **pre-rationalisation (2018-19) NCERT** and are marked *Advanced only* in the
  index.

19 + 11 = **30 chapter folders**.

Because the rationalised books are shorter, NCERT reused chapter codes —
`kech105` was *States of Matter* and is now *Thermodynamics*, `lech101` was
*The Solid State* and is now *Solutions*. Legacy PDFs are therefore named
`<code>-legacy.pdf`.

## Refreshing the PDFs

```bash
pip install pypdf                     # only needed for the verification step
python3 scripts/fetch_ncert_pdfs.py             # download (skips what is present)
python3 scripts/fetch_ncert_pdfs.py --force     # re-download everything
python3 scripts/fetch_ncert_pdfs.py --verify    # check the PDFs on disk
```

PDFs come from <https://ncert.nic.in/textbook.php> when it is reachable, and
otherwise from GitHub mirrors of the same NCERT files. Every downloaded file is
checked: it must be a valid PDF and its opening pages must contain the chapter
title. Set `GITHUB_TOKEN` to raise the API rate limit.

## Copyright

All PDFs are NCERT's own chapter files, published by the National Council of
Educational Research and Training, Government of India, and made freely
available for educational use — see <https://ncert.nic.in/copyright.php>.
