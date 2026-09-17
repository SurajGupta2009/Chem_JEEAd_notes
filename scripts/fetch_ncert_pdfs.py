#!/usr/bin/env python3
"""
Fetch NCERT Chemistry chapter PDFs for the JEE (Main + Advanced) syllabus and lay
them out one folder per chapter.

    NCERT-Chemistry/
        Class-11/
            01-Some-Basic-Concepts-of-Chemistry/
                kech101.pdf
                README.md
            ...
        Class-12/
            ...

Two NCERT editions are involved, because the two exams are not aligned:

  * JEE Main 2026 is based on the *rationalised* NCERT (2023+) -- 19 chemistry
    chapters (Class XI: 9, Class XII: 10).
  * JEE Advanced still tests topics that rationalisation deleted from the
    textbooks (States of Matter, Solid State, Surface Chemistry, Hydrogen,
    s-Block, p-Block, Metallurgy, Environmental Chemistry, Polymers,
    Chemistry in Everyday Life). Those come from the pre-rationalisation
    (2018-19) NCERT.

Sources, in order of preference:

  1. ncert.nic.in   -- the canonical publisher.
  2. GitHub mirrors -- used when ncert.nic.in is unreachable (e.g. a sandboxed
     network). Every mirrored file is the corresponding NCERT chapter PDF.

Usage:
    python3 scripts/fetch_ncert_pdfs.py             # download + write READMEs
    python3 scripts/fetch_ncert_pdfs.py --verify    # check what is on disk
    python3 scripts/fetch_ncert_pdfs.py --no-mirror # official source only

Set GITHUB_TOKEN / GH_TOKEN to raise the GitHub API rate limit (60 -> 5000/hr).
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_ROOT = REPO_ROOT / "NCERT-Chemistry"

OFFICIAL_BASE = "https://ncert.nic.in/textbook/pdf/"

# Mirrors that host the NCERT chapter PDFs verbatim.
MIRROR_RATIONALISED = "AnonymousCoder-hub/NCERT-Textbooks-Physics-Chemistry-Biology"
MIRROR_XI_LEGACY = "palhiman/ncert"
MIRROR_XII_LEGACY = "manisoni28/books"

# Both exams need these.
BOTH = ("JEE Main", "JEE Advanced")
# Deleted from the rationalised NCERT; still in the JEE Advanced syllabus.
ADV = ("JEE Advanced",)


def ch(cls, num, folder, title, code, edition, exams, mirror, probes, ncert_title):
    """Build one chapter record."""
    return {
        "class": cls,
        "num": num,
        "folder": folder,
        "title": title,
        "code": code,
        "edition": edition,
        "exams": exams,
        "mirror": mirror,
        "probes": probes,
        "ncert_title": ncert_title,
    }


# --------------------------------------------------------------------------
# Class XI -- rationalised NCERT (JEE Main syllabus). kech1 = Part I, kech2 = II
# --------------------------------------------------------------------------
CLASS11 = [
    ch(11, 1, "01-Some-Basic-Concepts-of-Chemistry", "Some Basic Concepts of Chemistry",
       "kech101", "rationalised", BOTH,
       (MIRROR_RATIONALISED, "Chemistry_11_Part1/Chapter_01.pdf"),
       ["Basic Concepts", "Chemistry"], "Some Basic Concepts of Chemistry"),
    ch(11, 2, "02-Structure-of-Atom", "Structure of Atom",
       "kech102", "rationalised", BOTH,
       (MIRROR_RATIONALISED, "Chemistry_11_Part1/Chapter_02.pdf"),
       ["Structure", "Atom"], "Structure of Atom"),
    ch(11, 3, "03-Classification-of-Elements-and-Periodicity-in-Properties",
       "Classification of Elements and Periodicity in Properties",
       "kech103", "rationalised", BOTH,
       (MIRROR_RATIONALISED, "Chemistry_11_Part1/Chapter_03.pdf"),
       ["Classification", "Periodicity"], "Classification of Elements and Periodicity in Properties"),
    ch(11, 4, "04-Chemical-Bonding-and-Molecular-Structure",
       "Chemical Bonding and Molecular Structure",
       "kech104", "rationalised", BOTH,
       (MIRROR_RATIONALISED, "Chemistry_11_Part1/Chapter_04.pdf"),
       ["Chemical Bonding", "Molecular Structure"], "Chemical Bonding and Molecular Structure"),
    ch(11, 5, "05-Thermodynamics", "Thermodynamics",
       "kech105", "rationalised", BOTH,
       (MIRROR_RATIONALISED, "Chemistry_11_Part1/Chapter_05.pdf"),
       ["Thermodynamics"], "Thermodynamics"),
    ch(11, 6, "06-Equilibrium", "Equilibrium",
       "kech106", "rationalised", BOTH,
       (MIRROR_RATIONALISED, "Chemistry_11_Part1/Chapter_06.pdf"),
       ["Equilibrium"], "Equilibrium"),
    ch(11, 7, "07-Redox-Reactions", "Redox Reactions",
       "kech201", "rationalised", BOTH,
       (MIRROR_RATIONALISED, "Chemistry_11_Part2/Chapter_01.pdf"),
       ["Redox"], "Redox Reactions"),
    ch(11, 8, "08-Organic-Chemistry-Some-Basic-Principles-and-Techniques",
       "Organic Chemistry: Some Basic Principles and Techniques",
       "kech202", "rationalised", BOTH,
       (MIRROR_RATIONALISED, "Chemistry_11_Part2/Chapter_02.pdf"),
       ["Organic Chemistry", "Basic Principles"], "Organic Chemistry - Some Basic Principles and Techniques"),
    ch(11, 9, "09-Hydrocarbons", "Hydrocarbons",
       "kech203", "rationalised", BOTH,
       (MIRROR_RATIONALISED, "Chemistry_11_Part2/Chapter_03.pdf"),
       ["Hydrocarbon"], "Hydrocarbons"),
]

# --------------------------------------------------------------------------
# Class XI -- pre-rationalisation NCERT, JEE Advanced only
# --------------------------------------------------------------------------
CLASS11_LEGACY = [
    ch(11, 10, "10-States-of-Matter", "States of Matter",
       "kech105-legacy", "legacy-2018", ADV,
       (MIRROR_XI_LEGACY, "XI/Chemistry-1/kech105.pdf"),
       ["States of Matter"], "States of Matter : Gases and Liquids"),
    ch(11, 11, "11-Hydrogen", "Hydrogen",
       "kech202-legacy", "legacy-2018", ADV,
       (MIRROR_XI_LEGACY, "XI/Chemistry-2/kech202.pdf"),
       ["Hydrogen"], "Hydrogen"),
    ch(11, 12, "12-The-s-Block-Elements", "The s-Block Elements (Alkali and Alkaline Earth Metals)",
       "kech203-legacy", "legacy-2018", ADV,
       (MIRROR_XI_LEGACY, "XI/Chemistry-2/kech203.pdf"),
       ["Block"], "The s-Block Elements"),
    ch(11, 13, "13-The-p-Block-Elements", "The p-Block Elements (Groups 13 and 14)",
       "kech204-legacy", "legacy-2018", ADV,
       (MIRROR_XI_LEGACY, "XI/Chemistry-2/kech204.pdf"),
       ["Block"], "Some p-Block Elements"),
    ch(11, 14, "14-Environmental-Chemistry", "Environmental Chemistry",
       "kech207-legacy", "legacy-2018", ADV,
       (MIRROR_XI_LEGACY, "XI/Chemistry-2/kech207.pdf"),
       ["Environmental"], "Environmental Chemistry"),
]

# --------------------------------------------------------------------------
# Class XII -- rationalised NCERT (JEE Main syllabus). lech1 = Part I, lech2 = II
# --------------------------------------------------------------------------
CLASS12 = [
    ch(12, 1, "01-Solutions", "Solutions",
       "lech101", "rationalised", BOTH,
       (MIRROR_RATIONALISED, "Chemistry_12_Part1/Chapter_01.pdf"),
       ["Solution"], "Solutions"),
    ch(12, 2, "02-Electrochemistry", "Electrochemistry",
       "lech102", "rationalised", BOTH,
       (MIRROR_RATIONALISED, "Chemistry_12_Part1/Chapter_02.pdf"),
       ["Electrochemistr"], "Electrochemistry"),
    ch(12, 3, "03-Chemical-Kinetics", "Chemical Kinetics",
       "lech103", "rationalised", BOTH,
       (MIRROR_RATIONALISED, "Chemistry_12_Part1/Chapter_03.pdf"),
       ["Kinetics"], "Chemical Kinetics"),
    ch(12, 4, "04-The-d-and-f-Block-Elements", "The d- and f-Block Elements",
       "lech104", "rationalised", BOTH,
       (MIRROR_RATIONALISED, "Chemistry_12_Part1/Chapter_04.pdf"),
       ["Block", "Elements"], "The d- and f-Block Elements"),
    ch(12, 5, "05-Coordination-Compounds", "Coordination Compounds",
       "lech105", "rationalised", BOTH,
       (MIRROR_RATIONALISED, "Chemistry_12_Part1/Chapter_05.pdf"),
       ["Coordination"], "Coordination Compounds"),
    ch(12, 6, "06-Haloalkanes-and-Haloarenes", "Haloalkanes and Haloarenes",
       "lech201", "rationalised", BOTH,
       (MIRROR_RATIONALISED, "Chemistry_12_Part2/Chapter_01.pdf"),
       ["Haloalkanes", "Haloarenes"], "Haloalkanes and Haloarenes"),
    ch(12, 7, "07-Alcohols-Phenols-and-Ethers", "Alcohols, Phenols and Ethers",
       "lech202", "rationalised", BOTH,
       (MIRROR_RATIONALISED, "Chemistry_12_Part2/Chapter_02.pdf"),
       ["Alcohols", "Phenols"], "Alcohols, Phenols and Ethers"),
    ch(12, 8, "08-Aldehydes-Ketones-and-Carboxylic-Acids",
       "Aldehydes, Ketones and Carboxylic Acids",
       "lech203", "rationalised", BOTH,
       (MIRROR_RATIONALISED, "Chemistry_12_Part2/Chapter_03.pdf"),
       ["Aldehydes", "Ketones"], "Aldehydes, Ketones and Carboxylic Acids"),
    ch(12, 9, "09-Amines", "Amines",
       "lech204", "rationalised", BOTH,
       (MIRROR_RATIONALISED, "Chemistry_12_Part2/Chapter_04.pdf"),
       ["Amines"], "Amines"),
    ch(12, 10, "10-Biomolecules", "Biomolecules",
       "lech205", "rationalised", BOTH,
       (MIRROR_RATIONALISED, "Chemistry_12_Part2/Chapter_05.pdf"),
       ["Biomolecule"], "Biomolecules"),
]

# --------------------------------------------------------------------------
# Class XII -- pre-rationalisation NCERT, JEE Advanced only.
# Sourced from manisoni28/books (epathshala 2018-19 chapter PDFs).
# --------------------------------------------------------------------------
_XII = "books/"
CLASS12_LEGACY = [
    ch(12, 11, "11-The-Solid-State", "The Solid State",
       "lech101-legacy", "legacy-2018", ADV,
       (MIRROR_XII_LEGACY, _XII + "ta20181001153836870112ChemistryNcertChapter1.pdf"),
       ["Solid State"], "The Solid State"),
    ch(12, 12, "12-Surface-Chemistry", "Surface Chemistry",
       "lech105-legacy", "legacy-2018", ADV,
       (MIRROR_XII_LEGACY, _XII + "ta20181001153836887712ChemistryNcertChapter5.pdf"),
       ["Surface Chemistry"], "Surface Chemistry"),
    ch(12, 13, "13-General-Principles-and-Processes-of-Isolation-of-Elements",
       "General Principles and Processes of Isolation of Elements (Metallurgy)",
       "lech106-legacy", "legacy-2018", ADV,
       (MIRROR_XII_LEGACY, _XII + "ta20181001153836891912ChemistryNcertChapter6.pdf"),
       ["Isolation"], "General Principles and Processes of Isolation of Elements"),
    ch(12, 14, "14-The-p-Block-Elements", "The p-Block Elements (Groups 15 to 18)",
       "lech107-legacy", "legacy-2018", ADV,
       (MIRROR_XII_LEGACY, _XII + "ta20181001153836896212ChemistryNcertChapter7.pdf"),
       ["Block"], "The p-Block Elements"),
    ch(12, 15, "15-Polymers", "Polymers",
       "lech207-legacy", "legacy-2018", ADV,
       (MIRROR_XII_LEGACY, _XII + "ta20181001153836925812ChemistryNcertChapter15.pdf"),
       ["Polymer"], "Polymers"),
    ch(12, 16, "16-Chemistry-in-Everyday-Life", "Chemistry in Everyday Life",
       "lech208-legacy", "legacy-2018", ADV,
       (MIRROR_XII_LEGACY, _XII + "ta20181001153836929512ChemistryNcertChapter16.pdf"),
       ["Everyday"], "Chemistry in Everyday Life"),
]

CHAPTERS = CLASS11 + CLASS11_LEGACY + CLASS12 + CLASS12_LEGACY


# --------------------------------------------------------------------------
# Download helpers
# --------------------------------------------------------------------------
def _gh_token():
    return os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or ""


def _get(url, headers=None, timeout=120):
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def fetch_official(code):
    """ncert.nic.in/textbook/pdf/<code>.pdf  (legacy files are not served here)."""
    base = code.split("-")[0]
    return _get(OFFICIAL_BASE + base + ".pdf",
                headers={"User-Agent": "Mozilla/5.0 (ncert-jee-fetcher)"})


def fetch_mirror(repo, path):
    """Fetch a file straight out of a GitHub repo via the git-blobs API."""
    tok = _gh_token()
    headers = {"Accept": "application/vnd.github+json",
               "User-Agent": "ncert-jee-fetcher",
               "X-GitHub-Api-Version": "2022-11-28"}
    if tok:
        headers["Authorization"] = "Bearer " + tok
    meta = json.loads(_get(
        "https://api.github.com/repos/%s/contents/%s" % (repo, path), headers))
    sha = meta["sha"]
    headers["Accept"] = "application/vnd.github.raw"
    return _get("https://api.github.com/repos/%s/git/blobs/%s" % (repo, sha), headers)


def is_pdf(data):
    return data[:5] == b"%PDF-" and data.rstrip()[-5:].find(b"%%EOF") != -1


def download(record, dest, use_official=True, use_mirror=True):
    errors = []
    if use_official and record["edition"] == "rationalised":
        try:
            data = fetch_official(record["code"])
            if is_pdf(data) and len(data) > 200_000:
                dest.write_bytes(data)
                return "ncert.nic.in"
            errors.append("official: not a PDF (%d bytes)" % len(data))
        except (urllib.error.URLError, OSError, TimeoutError) as exc:
            errors.append("official: %s" % exc)
    if use_mirror:
        repo, path = record["mirror"]
        try:
            data = fetch_mirror(repo, path)
            if not is_pdf(data):
                raise ValueError("not a PDF (%d bytes)" % len(data))
            dest.write_bytes(data)
            return "github:" + repo
        except (urllib.error.URLError, OSError, ValueError, KeyError, TimeoutError) as exc:
            errors.append("mirror: %s" % exc)
    raise RuntimeError("; ".join(errors) or "no source attempted")


# --------------------------------------------------------------------------
# Verification: pull text out of the PDF and look for the chapter title.
# --------------------------------------------------------------------------
def pdf_info(path):
    """Return (pages, first_pages_text)."""
    from pypdf import PdfReader

    reader = PdfReader(str(path))
    pages = len(reader.pages)
    text = []
    for page in reader.pages[:4]:
        try:
            text.append(page.extract_text() or "")
        except Exception:
            text.append("")
    return pages, "\n".join(text)


def verify(record):
    pdf = pdf_path(record)
    if not pdf.exists():
        return False, "MISSING", 0
    try:
        pages, text = pdf_info(pdf)
    except Exception as exc:  # corrupt / truncated
        return False, "UNREADABLE: %s" % exc, 0
    flat = re.sub(r"\s+", " ", text).lower()
    hit = next((p for p in record["probes"] if p.lower() in flat), None)
    if hit is None:
        return False, "title not found on first pages", pages
    return True, "ok (matched %r)" % hit, pages


def pdf_path(record):
    return OUT_ROOT / ("Class-%d" % record["class"]) / record["folder"] / (record["code"] + ".pdf")


def readme_path(record):
    return OUT_ROOT / ("Class-%d" % record["class"]) / record["folder"] / "README.md"


# --------------------------------------------------------------------------
# Per-chapter README + top-level index
# --------------------------------------------------------------------------
EDITION_LABEL = {
    "rationalised": "Rationalised NCERT (2023 onwards)",
    "legacy-2018": "Pre-rationalisation NCERT (2018-19 edition)",
}


def source_line(record):
    """Where this chapter's PDF legitimately comes from today.

    Rationalised chapters are still on ncert.nic.in under their code. Legacy
    chapters are not: NCERT dropped them in 2023, and several codes were
    reused by the shorter rationalised books, so the same code now points at
    a different chapter.
    """
    base = record["code"].split("-")[0]
    if record["edition"] == "rationalised":
        return "Official URL", OFFICIAL_BASE + base + ".pdf"
    clash = next((c for c in CHAPTERS
                  if c["edition"] == "rationalised"
                  and c["code"].split("-")[0] == base), None)
    if clash:
        note = ("no longer published - removed in the 2023 rationalisation. "
                "`%s.pdf` on ncert.nic.in is now *%s*, not this chapter"
                % (base, clash["title"]))
    else:
        note = ("no longer published - removed in the 2023 rationalisation, "
                "and the code `%s` no longer exists in the current book" % base)
    return "Official URL", note


def write_chapter_readme(record):
    pdf = pdf_path(record)
    size = pdf.stat().st_size if pdf.exists() else 0
    repo, path = record["mirror"]
    src_label, src_value = source_line(record)
    body = f"""# {record['title']}

| | |
|---|---|
| Class | {record['class']} |
| NCERT code | `{record['code'].split('-')[0]}` |
| NCERT edition | {EDITION_LABEL[record['edition']]} |
| Needed for | {", ".join(record['exams'])} |
| PDF | [`{pdf.name}`]({pdf.name}) |
| {src_label} | {src_value} |
| Mirror used | `{repo}` -> `{path}` |

## Why this edition

{rationale(record)}

## Notes

<!-- Add your notes for this chapter below. -->
"""
    readme_path(record).write_text(body, encoding="utf-8")


def rationale(record):
    if record["edition"] == "rationalised":
        return (
            "This chapter is in the current (rationalised) NCERT textbook, which is "
            "what the JEE Main syllabus is based on. JEE Advanced tests it too."
        )
    return (
        "This chapter was **removed** from the NCERT textbook during rationalisation "
        "(2023), but it is **still in the JEE Advanced syllabus** and is not asked in "
        "JEE Main. The PDF is therefore the pre-rationalisation (2018-19) NCERT "
        "chapter, since no current NCERT chapter covers this material."
    )


def write_index():
    lines = [
        "# NCERT Chemistry for JEE (Main + Advanced)",
        "",
        "One folder per NCERT chemistry chapter, each holding the chapter PDF.",
        "",
        "- **JEE Main** follows the **rationalised NCERT (2023+)**: 19 chemistry "
        "chapters (Class XI: 9, Class XII: 10).",
        "- **JEE Advanced** additionally covers topics that rationalisation deleted "
        "from the textbooks. Those 11 chapters are included from the "
        "**pre-rationalisation (2018-19) NCERT** and are marked *Advanced only*.",
        "",
        "Total: **30 chapters** (Class XI: 14, Class XII: 16).",
        "",
        "> **Careful with the NCERT codes.** The rationalised books are shorter, so "
        "codes were reused: `kech105` was *States of Matter* and is now "
        "*Thermodynamics*; `lech101` was *The Solid State* and is now *Solutions*. "
        "Legacy files are named `<code>-legacy.pdf` to keep the two apart.",
        "",
        "Re-fetch or check everything with:",
        "",
        "```bash",
        "python3 scripts/fetch_ncert_pdfs.py            # download",
        "python3 scripts/fetch_ncert_pdfs.py --verify   # check PDFs on disk",
        "```",
        "",
    ]
    for cls in (11, 12):
        group = [c for c in CHAPTERS if c["class"] == cls]
        lines += ["## Class %d" % cls, "",
                  "| # | Chapter | NCERT code | Edition | Needed for |",
                  "|---|---|---|---|---|"]
        for c in group:
            rel = "Class-%d/%s" % (cls, c["folder"])
            edition = "rationalised" if c["edition"] == "rationalised" else "legacy 2018-19"
            exams = "Main + Advanced" if "JEE Main" in c["exams"] else "**Advanced only**"
            lines.append("| %d | [%s](%s) | `%s` | %s | %s |"
                         % (c["num"], c["title"], rel,
                            c["code"].split("-")[0], edition, exams))
        lines.append("")
    lines += [
        "## Sources",
        "",
        "All PDFs are NCERT's own chapter files, published by the National Council of "
        "Educational Research and Training, Government of India, and made freely "
        "available for educational use. See "
        "<https://ncert.nic.in/copyright.php>.",
        "",
        "They are fetched from <https://ncert.nic.in/textbook.php> when reachable, "
        "otherwise from GitHub mirrors of the same files (listed per chapter in each "
        "chapter README).",
        "",
    ]
    (OUT_ROOT / "README.md").write_text("\n".join(lines), encoding="utf-8")


# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--verify", action="store_true", help="verify PDFs already on disk")
    ap.add_argument("--no-official", action="store_true", help="skip ncert.nic.in")
    ap.add_argument("--no-mirror", action="store_true", help="skip GitHub mirrors")
    ap.add_argument("--force", action="store_true", help="re-download existing files")
    args = ap.parse_args()

    ok = 0
    failures = []
    total = 0

    for record in CHAPTERS:
        pdf = pdf_path(record)
        pdf.parent.mkdir(parents=True, exist_ok=True)
        label = "Class-%d/%s" % (record["class"], record["folder"])

        if args.verify:
            good, detail, pages = verify(record)
            size = pdf.stat().st_size if pdf.exists() else 0
            total += size
            print("%-6s %-62s %5d pp  %7.1f MB  %s"
                  % ("OK" if good else "FAIL", label, pages, size / 1e6, detail))
            ok += bool(good)
            if not good:
                failures.append(label)
            continue

        if pdf.exists() and not args.force:
            src = "cached"
        else:
            try:
                src = download(record, pdf,
                               use_official=not args.no_official,
                               use_mirror=not args.no_mirror)
            except RuntimeError as exc:
                print("FAIL  %-60s %s" % (label, exc))
                failures.append(label)
                continue
        good, detail, pages = verify(record)
        print("%-6s %-62s %5d pp  %7.1f MB  via %s"
              % ("OK" if good else "FAIL", label, pages,
                 pdf.stat().st_size / 1e6, src))
        ok += bool(good)
        if not good:
            failures.append(label + " (" + detail + ")")

    if args.verify:
        print("\n%d/%d chapters verified, %.1f MB on disk"
              % (ok, len(CHAPTERS), total / 1e6))
    else:
        write_index()
        for record in CHAPTERS:
            if pdf_path(record).exists():
                write_chapter_readme(record)
        print("\n%d/%d chapters downloaded and verified" % (ok, len(CHAPTERS)))

    if failures:
        print("Problems:")
        for f in failures:
            print("  -", f)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
