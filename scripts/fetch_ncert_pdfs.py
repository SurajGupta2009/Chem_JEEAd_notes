#!/usr/bin/env python3
"""
Fetch NCERT Chemistry chapter PDFs for the JEE (Main + Advanced) syllabus and lay
them out as two branch folders -- Physical / Inorganic Chemistry -- each
holding one folder per chapter with the chapter PDF and its README.
Organic Chemistry has been removed as per user request.

    Physical-Chemistry/            Inorganic-Chemistry/
      01-Some-Basic-Concepts-...     01-Classification-...
        kech101.pdf                    kech103.pdf
        README.md                      README.md
      02-Structure-of-Atom           02-Chemical-Bonding-...
      ...                            ...
      07-Solutions                   07-Coordination-Compounds
      ...

Chapter numbering is per branch (in Class XI then Class XII order, by NCERT unit), so
the folder number is NOT the NCERT unit number -- the NCERT unit and class live in each
chapter's README and in the branch index. Move a chapter to another branch by editing
BRANCH_OF below and re-running: the script renumbers, regenerates every chapter README
and regenerates the three branch indexes (it never touches notes.md or module PDFs).

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
    python3 scripts/fetch_ncert_pdfs.py             # download + write READMEs + indexes
    python3 scripts/fetch_ncert_pdfs.py --verify    # check what is on disk
    python3 scripts/fetch_ncert_pdfs.py --layout    # print NCERT unit -> branch/folder
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
import urllib.parse
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# The branch folders the chapters are filed under - now only Physical + Inorganic.
BRANCHES = ("Physical", "Inorganic")
BRANCH_DIR = {b: REPO_ROOT / (b + "-Chemistry") for b in BRANCHES}

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
# Branch classification: (class, NCERT unit number) -> branch.
#
# The usual JEE split, with three deliberate judgement calls:
#   * Solid State, Surface Chemistry and Metallurgy are filed under Physical
#     (lattice / kinetic / process chemistry), not Inorganic.
#   * Chemical Bonding, Hydrogen and Environmental Chemistry stay Inorganic.
#   * Biomolecules, Polymers and Chemistry in Everyday Life go with Organic,
#     because the carbon chemistry is what the questions actually test.
# Move a chapter by editing its entry and re-running: folder numbering, the
# chapter READMEs and the three branch indexes all follow automatically.
# --------------------------------------------------------------------------
BRANCH_OF = {
    (11, 1): "Physical",    # Some Basic Concepts of Chemistry (mole concept)
    (11, 2): "Physical",    # Structure of Atom
    (11, 5): "Physical",    # Thermodynamics
    (11, 6): "Physical",    # Equilibrium (chemical + ionic)
    (11, 7): "Physical",    # Redox Reactions
    (11, 10): "Physical",   # States of Matter (Advanced only)
    (12, 1): "Physical",    # Solutions
    (12, 2): "Physical",    # Electrochemistry
    (12, 3): "Physical",    # Chemical Kinetics
    (12, 11): "Physical",   # The Solid State (Advanced only)
    (12, 12): "Physical",   # Surface Chemistry (Advanced only)
    (12, 13): "Physical",   # Isolation of Elements / Metallurgy (Advanced only)
    (11, 3): "Inorganic",   # Classification & Periodicity
    (11, 4): "Inorganic",   # Chemical Bonding & Molecular Structure
    (11, 11): "Inorganic",  # Hydrogen (Advanced only)
    (11, 12): "Inorganic",  # s-Block (Advanced only)
    (11, 13): "Inorganic",  # p-Block, groups 13-14 (Advanced only)
    (11, 14): "Inorganic",  # Environmental Chemistry (Advanced only)
    (12, 4): "Inorganic",   # d- and f-Block
    (12, 5): "Inorganic",   # Coordination Compounds
    (12, 14): "Inorganic",  # p-Block, groups 15-18 (Advanced only)
    # Organic chapters removed as per user request - only Physical + Inorganic notes needed
}

BRANCH_INDEX = {}


def apply_layout():
    """Give every chapter its branch and its branch-sequential folder number.

    The `folder` in the chapter tables above is the NCERT-style name, prefixed with
    the NCERT unit number ('06-Equilibrium' = Class XI Unit 6). That prefix is
    replaced by the chapter's position inside its branch, so each branch folder reads
    01..NN in teaching order while `num` still holds the NCERT unit -- which is what
    codes such as kech106 refer to.
    Only Physical + Inorganic branches are kept now.
    """
    per_branch = {b: [] for b in BRANCHES}
    for record in CHAPTERS:
        key = (record["class"], record["num"])
        branch = BRANCH_OF.get(key)
        if branch is None:
            # Organic chapters or unmapped - skip as per user request
            continue
        if branch not in BRANCHES:
            continue
        record["branch"] = branch
        record["name"] = re.sub(r"^\d+-", "", record["folder"])
        per_branch[branch].append(record)
    for branch, rows in per_branch.items():
        rows.sort(key=lambda r: (r["class"], r["num"]))
        for i, r in enumerate(rows, start=1):
            r["folder"] = "%02d-%s" % (i, r["name"])
            r["dir"] = BRANCH_DIR[branch] / r["folder"]
        BRANCH_INDEX[branch] = rows


apply_layout()


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
    return record["dir"] / (record["code"] + ".pdf")


def readme_path(record):
    return record["dir"] / "README.md"


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
    folder = readme_path(record).parent
    notes = folder / "notes.md"
    if notes.exists():
        notes_section = (
            "Combined NCERT + Allen notes for JEE Main + Advanced are in "
            "[`notes.md`](notes.md). Filed under %s Chemistry \u2014 see the "
            "[branch index](../README.md)." % record["branch"]
        )
    else:
        notes_section = "<!-- Add your notes for this chapter below (notes.md). -->"
    extra_lines = []
    if folder.exists():
        for extra in sorted(folder.iterdir()):
            if extra.suffix.lower() == ".pdf" and extra != pdf:
                href = urllib.parse.quote(extra.name)
                extra_lines.append("| Module PDF | [`%s`](%s) |" % (extra.name, href))
    body = f"""# {record['title']}

| | |
|---|---|
| Branch | {record['branch']} Chemistry |
| Class | {record['class']} |
| NCERT unit | Unit {record['num']} (Class {record['class']}) |
| NCERT code | `{record['code'].split('-')[0]}` |
| NCERT edition | {EDITION_LABEL[record['edition']]} |
| Needed for | {", ".join(record['exams'])} |
| PDF | [`{pdf.name}`]({pdf.name}) |
{chr(10).join(extra_lines) if extra_lines else "| Module PDF | _not uploaded yet_ |"}
| {src_label} | {src_value} |
| Mirror used | `{repo}` -> `{path}` |

## Why this edition

{rationale(record)}

## Notes

{notes_section}
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
    """Write one index README into each branch folder."""
    for branch, rows in BRANCH_INDEX.items():
        lines = [
            "# %s Chemistry \u2014 JEE (Main + Advanced)" % branch.capitalize(),
            "",
            "One folder per NCERT chapter: the chapter PDF, any module PDF that has been",
            "uploaded, and `notes.md` once written. Chapters are numbered in this branch's",
            "own order (Class XI first, then Class XII, by NCERT unit).",
            "",
            "| # | Chapter | Class | NCERT unit | Code | Edition | Needed for | Notes |",
            "|---|---|---|---|---|---|---|---|",
        ]
        for c in rows:
            edition = "rationalised" if c["edition"] == "rationalised" else "legacy 2018-19"
            exams = "Main + Advanced" if "JEE Main" in c["exams"] else "**Advanced only**"
            has_notes = (c["dir"] / "notes.md").exists()
            notes = "[\u2705 notes.md](%s/notes.md)" % c["folder"] if has_notes else "\u23f3 pending"
            lines.append("| %s | [%s](%s) | %d | %d | `%s` | %s | %s | %s |"
                         % (c["folder"][:2], c["title"], c["folder"], c["class"], c["num"],
                            c["code"].split("-")[0], edition, exams, notes))
        lines += [
            "",
            "The `#` column is this branch's own order. The NCERT unit number keeps its own",
            "column because that is what the NCERT codes mean: `kech1xx` = Class XI Part I,",
            "`kech2xx` = Class XI Part II, `lech1xx` / `lech2xx` likewise for Class XII.",
            "The rationalised books are shorter, so NCERT reused codes \u2014 `kech105` was",
            "*States of Matter* and is now *Thermodynamics*; `lech101` was *The Solid State*",
            "and is now *Solutions*. Legacy chapter PDFs are therefore named",
            "`<code>-legacy.pdf`. Full layout and notes conventions: [repo",
            "README](../README.md).",
            "",
            "Refresh with `python3 scripts/fetch_ncert_pdfs.py` (`--verify` checks the PDFs on",
            "disk, `--layout` prints the NCERT-unit \u2192 branch mapping).",
            "",
        ]
        (BRANCH_DIR[branch] / "README.md").write_text("\n".join(lines), encoding="utf-8")


def print_layout():
    print("NCERT chapter -> where it lives in this repo\n")
    for branch, rows in BRANCH_INDEX.items():
        print("%s-Chemistry/" % branch)
        for c in rows:
            print("  %-56s <- Class %d Unit %d (%s)"
                  % (c["folder"], c["class"], c["num"], c["code"]))
        print()


# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--verify", action="store_true", help="verify PDFs already on disk")
    ap.add_argument("--no-official", action="store_true", help="skip ncert.nic.in")
    ap.add_argument("--no-mirror", action="store_true", help="skip GitHub mirrors")
    ap.add_argument("--force", action="store_true", help="re-download existing files")
    ap.add_argument("--layout", action="store_true",
                    help="print the NCERT-unit -> branch/folder mapping and exit")
    args = ap.parse_args()

    if args.layout:
        print_layout()
        return 0

    ok = 0
    failures = []
    total = 0

    # Only process Physical + Inorganic chapters now
    active_chapters = [r for r in CHAPTERS if r.get("branch") in BRANCHES]

    for record in active_chapters:
        pdf = pdf_path(record)
        pdf.parent.mkdir(parents=True, exist_ok=True)
        label = "%s-Chemistry/%s" % (record["branch"], record["folder"])

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
              % (ok, len(active_chapters), total / 1e6))
    else:
        write_index()
        for record in active_chapters:
            record["dir"].mkdir(parents=True, exist_ok=True)
            if pdf_path(record).exists():
                write_chapter_readme(record)
        print("\n%d/%d chapters downloaded and verified" % (ok, len(active_chapters)))

    if failures:
        print("Problems:")
        for f in failures:
            print("  -", f)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
