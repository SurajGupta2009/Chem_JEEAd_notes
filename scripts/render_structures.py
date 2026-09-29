#!/usr/bin/env python3
"""Turn a chapter's structure table into ChemEdit-editable SVGs, a gallery and a Chem block.

Implements the structure pipeline of docs/NOTE-FORMATTING-RULEBOOK.md (R18/R19). ONE markdown
table per chapter, `<chapter>/figures/structures.md`, is the source of truth. From it this
script generates:

  1. `figures/mol/<ID>.svg` for every row: an RDKit drawing (renders on GitHub and in any
     viewer) that is ALSO a *Ketcher SVG*: the molfile is embedded, base64-encoded, in
         <desc id="ketcher-data" data-format="mol">...</desc>
     which is the format the Obsidian plugin ChemEdit (`chemedit`) reads. So the same file is
     a plain image on GitHub and a double-click-editable structure in Obsidian.
     Oxidation states are printed next to the atoms (computed; see below).
  2. The gallery table inside structures.md, between <!-- gallery:begin/end -->.
  3. The ```smiles block inside structures.md, between <!-- smiles:begin/end -->, which the
     Obsidian plugin Chem (`chem`) renders as a live grid.
  4. Optionally (--library), docs/COMPOUND-LIBRARY.md: every chapter's structures in one
     `| Name | SMILES | Chapter |` table, the format ChemEdit's "Compound Library File Path"
     setting reads (column 1 = name, column 2 = SMILES).

Source table (extra columns are ignored; the first table whose header has SMILES is used):

    | Label | SMILES | ID | O.S. | Check | Note |
    |---|---|---|---|---|---|
    | H₂SO₅ Caro's acid | `OOS(=O)(=O)O` | h2so5 | auto | S=+6 | one O–O |

  Label  display name (Unicode fine). Keep it the FIRST column and SMILES the SECOND, so the
         file also works as a ChemEdit compound library.
  SMILES may be wrapped in backticks (recommended: GitHub would turn `[Cr](=O)` into a link).
  ID     file stem for figures/mol/<ID>.svg (ASCII).
  O.S.   which oxidation-state labels to draw:
           auto          every atom except H, O at -2 and spectator metal ions
           H             also draw every hydrogen explicitly (combine: "auto H")
           -             no labels
           show:0,3      only these atom indices (SMILES order, 0-based)
           1:+6 3:-2     override the computed value for these atoms (combine with show:)
  Check  assertions, space-separated, checked against the computed/overridden values:
           S=+6          every S atom is +6
           S=+5,0        the set of distinct S values is exactly {+5, 0}
           S~+5/2        the average over S atoms is +5/2
           -             nothing to assert (the O.S. is the point of the drawing, not a number)
         The script exits non-zero on any failed check, so the drawings cannot silently
         disagree with the notes.
  Note   free text, shown in the gallery.

Oxidation states are computed the textbook way: every bond's electrons go to the more
electronegative atom (Pauling values), bonds between like atoms count 0, and the formal
charge is added. Three JEE conventions override Pauling (see MORE_EN): the non-metal wins
against H for P and Si (so SiH4 is Si -4 and H3PO2 is P +1), and N wins against Cl
(NCl3: N -3, Cl +1).

Usage:
    python scripts/render_structures.py <structures.md> [...] [--size 240x170]
    python scripts/render_structures.py --all [--library docs/COMPOUND-LIBRARY.md]
    python scripts/render_structures.py --all --validate     # no drawing, works anywhere

Requires RDKit (`pip install rdkit`), a dev-only dependency: readers of the notes never need
it, and scripts/fetch_ncert_pdfs.py does not use it. Drawing additionally needs RDKit's
Cairo/X11 backend; `--validate` deliberately uses only the chemistry core so the tables can be
checked on a machine (or in CI) where the drawing libraries are unavailable.
"""
import argparse
import base64
import re
import sys
from collections import Counter, OrderedDict
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARK = {k: ("<!-- %s:begin -->" % k, "<!-- %s:end -->" % k) for k in ("gallery", "smiles")}

# Pauling electronegativities, the real published values.
EN = {"H": 2.20, "Li": 0.98, "Be": 1.57, "B": 2.04, "C": 2.55, "N": 3.04, "O": 3.44, "F": 3.98,
      "Na": 0.93, "Mg": 1.31, "Al": 1.61, "Si": 1.90, "P": 2.19, "S": 2.58, "Cl": 3.16,
      "K": 0.82, "Ca": 1.00, "Ti": 1.54, "V": 1.63, "Cr": 1.66, "Mn": 1.55, "Fe": 1.83,
      "Co": 1.88, "Ni": 1.91, "Cu": 1.90, "Zn": 1.65, "As": 2.18, "Se": 2.55, "Br": 2.96,
      "Ag": 1.93, "Sn": 1.96, "I": 2.66, "Xe": 2.60, "Ba": 0.89, "Hg": 2.00, "Pb": 2.33}

# Pairs the JEE syllabus teaches the other way round from Pauling. They are listed as
# pairs rather than as fudged EN values so the table above stays the published data.
# Each value is the element that wins the bond: the non-metal keeps the bonding pair
# against H, which is what makes SiH4 Si -4 and PH3 P -3 rather than the Pauling +4 / +3.
MORE_EN = {frozenset(("P", "H")): "P",     # PH3 is P -3; H3PO2 is P +1
           frozenset(("Si", "H")): "Si",   # SiH4 is Si -4 (molecular hydride of a non-metal)
           frozenset(("N", "Cl")): "N"}    # NCl3 is N -3, Cl +1
SPECTATORS = {"Li", "Na", "K", "Rb", "Cs", "Mg", "Ca", "Sr", "Ba"}


def more_en(hi, lo):
    """Is `hi` the more electronegative of the pair? A JEE convention overrides Pauling."""
    win = MORE_EN.get(frozenset((hi, lo)))
    if win is not None:
        return win == hi
    return EN.get(hi, 1.5) > EN.get(lo, 1.5)


def fmt(v, unicode_minus=True):
    """+6 / −1 / 0 / +5⁄2 (unicode) or +6 / -1 (ascii, for RDKit's font)."""
    v = Fraction(v)
    sign = "" if v == 0 else ("+" if v > 0 else ("−" if unicode_minus else "-"))
    a = abs(v)
    body = str(a.numerator) if a.denominator == 1 else "%d⁄%d" % (a.numerator, a.denominator)
    return sign + body


def parse_value(s):
    return Fraction(s.replace("−", "-").replace("⁄", "/"))


def parse_table(md):
    rows, header = [], None
    for line in md.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            if header and rows:
                break
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if header is None:
            if any(c.upper() == "SMILES" for c in cells):
                header = [c.upper() for c in cells]
            continue
        if set("".join(cells)) <= set("-: "):
            continue
        r = dict(zip(header, cells))
        smi = r.get("SMILES", "").strip("` ")
        if smi and smi != "—":
            rows.append({"label": r.get("LABEL", ""), "smiles": smi, "id": r.get("ID", ""),
                         "os": r.get("O.S.", "auto") or "auto", "check": r.get("CHECK", ""),
                         "note": r.get("NOTE", "")})
    return rows


def oxidation_states(mol):
    from rdkit import Chem
    m = Chem.Mol(mol)
    if any(b.GetIsAromatic() for b in m.GetBonds()):
        # Kekulize() also recomputes the implicit hydrogens, and on a relaxed (never fully
        # validated) molecule that hands a phantom H to every double-bonded oxygen. Only
        # call it when there is actually something aromatic to kekulise.
        Chem.Kekulize(m, clearAromaticFlags=True)
    out = []
    for a in m.GetAtoms():
        sym = a.GetSymbol()
        v = Fraction(a.GetFormalCharge())
        for b in a.GetBonds():
            o = b.GetOtherAtom(a)
            osym = o.GetSymbol()
            if osym == sym:
                continue
            order = Fraction(b.GetBondTypeAsDouble())
            v += order if more_en(osym, sym) else (-order if more_en(sym, osym) else 0)
        if sym != "H":
            h = a.GetTotalNumHs()
            v += h if more_en("H", sym) else (-h if more_en(sym, "H") else 0)
        out.append(v)
    return out


def implicit_h_sum(mol):
    """Total O.S. carried by implicit hydrogens (+1 each on atoms more EN than H, −1 otherwise)."""
    s = 0
    for a in mol.GetAtoms():
        sym = a.GetSymbol()
        if sym != "H":
            s += a.GetTotalNumHs() * (1 if more_en(sym, "H") else (-1 if more_en("H", sym) else 0))
    return s


def apply_spec(mol, spec, values):
    """Return (values after overrides, indices to label)."""
    values = list(values)
    shown = None
    if spec.strip() == "-":
        return values, []
    for tok in spec.split():
        if tok in ("auto", "H"):
            continue
        if tok.startswith("show:"):
            shown = [int(i) for i in tok[5:].split(",") if i]
        elif re.fullmatch(r"\d+:[+\-−]?[\d/⁄]+", tok):
            i, val = tok.split(":")
            values[int(i)] = parse_value(val)
        else:
            raise ValueError("bad O.S. token %r" % tok)
    if shown is None:
        shown = []
        for a in mol.GetAtoms():
            i, sym = a.GetIdx(), a.GetSymbol()
            if sym == "H" or (sym == "O" and values[i] == -2):
                continue
            if sym in SPECTATORS and a.GetDegree() == 0:
                continue
            shown.append(i)
    return values, shown


def run_checks(mol, values, check):
    errors = []
    by_el = OrderedDict()
    for a in mol.GetAtoms():
        by_el.setdefault(a.GetSymbol(), []).append(values[a.GetIdx()])
    for tok in check.split():
        if tok in ("-", "—", "n/a", "N/A"):   # "nothing to assert" is a valid cell
            continue
        m = re.fullmatch(r"([A-Z][a-z]?)([=~])(.+)", tok)
        if not m:
            errors.append("bad check token %r" % tok)
            continue
        el, op, rhs = m.groups()
        vals = by_el.get(el)
        if not vals:
            errors.append("%s: no %s atom" % (tok, el))
            continue
        if op == "=":
            want = {parse_value(x) for x in rhs.split(",")}
            if set(vals) != want:
                errors.append("%s: got %s" % (tok, ",".join(fmt(v) for v in sorted(set(vals)))))
        else:
            avg = sum(vals) / len(vals)
            if avg != parse_value(rhs):
                errors.append("%s: average is %s" % (tok, fmt(avg)))
    return errors


def summary(mol, values, shown, explicit):
    """'S +6' / 'S −2, +6 (avg +2)' per element, over the labelled atoms only.
    The average is given only when the labels cover every atom of that element (not for O)."""
    by_el, count = OrderedDict(), Counter(a.GetSymbol() for a in mol.GetAtoms())
    for i in shown:
        by_el.setdefault(mol.GetAtomWithIdx(i).GetSymbol(), []).append(values[i])
    parts = []
    for el, vals in by_el.items():
        distinct = sorted(set(vals))
        s = "%s %s" % (el, ", ".join(fmt(v) for v in distinct))
        if len(distinct) > 1 and el != "O" and not explicit and len(vals) == count[el]:
            s += " (avg %s)" % fmt(sum(vals) / len(vals))
        parts.append(s)
    return " · ".join(parts)


def draw(mol, values, shown, size):
    from rdkit import Chem
    from rdkit.Chem import rdDepictor
    from rdkit.Chem.Draw import rdMolDraw2D
    m = Chem.Mol(mol)
    rdDepictor.Compute2DCoords(m)
    for i in shown:
        m.GetAtomWithIdx(i).SetProp("atomNote", fmt(values[i], unicode_minus=False))
    w, h = size
    d = rdMolDraw2D.MolDraw2DSVG(w, h)
    o = d.drawOptions()
    o.bondLineWidth, o.padding = 2, 0.12
    o.fixedBondLength = 36          # same scale for every molecule (shrinks only if it can't fit)
    o.annotationFontScale = 0.8
    o.setAtomNoteColour((0.78, 0.08, 0.08, 1.0))  # O.S. labels in red
    o.useBWAtomPalette()            # black atoms, so the red O.S. labels are the only colour
    o.explicitMethyl = True
    d.DrawMolecule(m)
    d.FinishDrawing()
    svg = d.GetDrawingText()
    m.SetProp("_Name", "")
    molblock = Chem.MolToMolBlock(m)
    b64 = base64.b64encode(molblock.encode("utf-8")).decode("ascii")
    desc = '\n<desc id="ketcher-data" data-format="mol">%s</desc>\n' % b64
    return re.sub(r"(<svg[^>]*>)", lambda mm: mm.group(1) + desc, svg, count=1)


def replace_block(md, key, body):
    b, e = MARK[key]
    block = "%s\n%s\n%s" % (b, body, e)
    if b in md and e in md:
        return re.sub(re.escape(b) + r".*?" + re.escape(e), lambda _: block, md, flags=re.S)
    return md.rstrip("\n") + "\n\n" + block + "\n"


def parse_smiles(smi):
    """Keep explicit [H] atoms (e.g. the P–H bonds of H3PO3 are the point of the drawing).

    Falls back to a relaxed sanitisation for the genuinely hypervalent species this repo
    draws — ClF3, BrF5, IF7, HClO4 and B2H6. RDKit's default model allows a maximum
    valence of 7 for iodine and 6 for chlorine, so it rejects them, but the molecules
    are real and are exactly the ones the bonding chapter needs. Dropping only
    SANITIZE_PROPERTIES keeps ring perception, aromaticity and the bond graph, which
    is all the drawing and the oxidation-state calculation need.

    SANITIZE_CLEANUP cannot be skipped, and it is the step that repairs a hypervalent
    atom by rewriting the molecule: `O[Cl](=O)(=O)=O` comes back as Cl3+ on four single
    bonds. So whichever sanitisation succeeds, the molecule gets its charges and bond
    orders copied back from an untouched copy, which is what the table actually spells.
    """
    from rdkit import Chem
    from rdkit import RDLogger
    RDLogger.DisableLog("rdApp.*")   # the first attempt failing below is expected, not a warning
    ps = Chem.SmilesParserParams()
    ps.removeHs = False
    ref = Chem.MolFromSmiles(smi, raw_ps())        # exactly what the row spells, never validated
    mol = Chem.MolFromSmiles(smi, ps)
    if mol is not None and charges_agree(mol, ref):
        return mol
    if ref is None:
        return None
    for ops in (Chem.SANITIZE_ALL, Chem.SANITIZE_ALL ^ Chem.SANITIZE_PROPERTIES):
        mol, written = Chem.Mol(ref), Chem.Mol(ref)
        RDLogger.DisableLog("rdApp.*")
        try:
            Chem.SanitizeMol(mol, ops)
        except Exception:                          # still hypervalent: try the relaxed set
            continue
        RDLogger.EnableLog("rdApp.*")
        for a, w in zip(list(mol.GetAtoms()), list(written.GetAtoms())):
            a.SetFormalCharge(w.GetFormalCharge())
        for b, w in zip(list(mol.GetBonds()), list(written.GetBonds())):
            b.SetBondType(w.GetBondType())
        # and re-derive the implicit hydrogens, which were counted against the bond orders
        # sanitisation had just rewritten: otherwise HO-Cl(=O)3 gets drawn as Cl(OH)4.
        mol.UpdatePropertyCache(False)
        return mol
    return None


def charges_agree(mol, ref):
    """Did RDKit leave the formal charges the way the table wrote them?

    If it did, the fully validated molecule is the one to use. If it did not, RDKit has
    been editing the charges to make a hypervalent atom legal, and the unvalidated parse
    is the faithful reading of the row.
    """
    if ref is None:
        return True
    return [a.GetFormalCharge() for a in mol.GetAtoms()] == \
           [a.GetFormalCharge() for a in ref.GetAtoms()]


def raw_ps():
    """Parser settings for a molecule RDKit has not validated yet."""
    from rdkit import Chem
    ps = Chem.SmilesParserParams()
    ps.sanitize = False
    ps.removeHs = False
    return ps


def validate(src):
    """Check every row's SMILES and O.S. assertions without drawing anything.

    Needs RDKit's chemistry core only (no X11 / Cairo), so it runs on any machine and in
    CI even where the SVG backend cannot be loaded.
    """
    from rdkit import Chem
    rows = parse_table(src.read_text(encoding="utf-8"))
    if not rows:
        return ["no table with a SMILES column"], 0
    errors, svgdir = [], src.parent / "mol"
    have = {p.stem for p in svgdir.glob("*.svg")} if svgdir.is_dir() else set()
    for r in rows:
        mol = parse_smiles(r["smiles"])
        if mol is None:
            errors.append("%s: RDKit rejects the SMILES %r (explicit valence?)" % (r["label"], r["smiles"]))
            continue
        if not re.fullmatch(r"[a-z0-9][a-z0-9\-]*", r["id"] or ""):
            errors.append("%s: ID must be lowercase ASCII, got %r" % (r["label"], r["id"]))
        if r["id"] not in have:
            errors.append("%s: no drawing at mol/%s.svg — run the renderer" % (r["label"], r["id"]))
        if "H" in r["os"].split():
            mol = Chem.AddHs(mol)
        try:
            values, _ = apply_spec(mol, r["os"], oxidation_states(mol))
        except ValueError as exc:
            errors.append("%s: %s" % (r["label"], exc))
            continue
        total = sum(values) + implicit_h_sum(mol)
        charge = sum(a.GetFormalCharge() for a in mol.GetAtoms())
        if total != charge:
            errors.append("%s: O.S. sum %s ≠ charge %d" % (r["label"], fmt(total), charge))
        errors += ["%s: %s" % (r["label"], e) for e in run_checks(mol, values, r["check"])]
    for stale in sorted(have - {r["id"] for r in rows}):
        errors.append("mol/%s.svg is not in the table (stale drawing)" % stale)
    return errors, len(rows)


def process(src, size):
    from rdkit import Chem
    md = src.read_text(encoding="utf-8")
    rows = parse_table(md)
    if not rows:
        sys.exit("no table with a SMILES column in %s" % src)
    outdir = src.parent / "mol"
    outdir.mkdir(exist_ok=True)
    gallery = ["| Structure | Species | O.S. on the drawing | Note |", "|---|---|---|---|"]
    failures, written = [], set()
    for r in rows:
        mol = parse_smiles(r["smiles"])
        if mol is None:
            failures.append("%s: unparseable SMILES %s" % (r["label"], r["smiles"]))
            continue
        if not re.fullmatch(r"[a-z0-9][a-z0-9\-]*", r["id"] or ""):
            failures.append("%s: ID must be lowercase ASCII, got %r" % (r["label"], r["id"]))
            continue
        if "H" in r["os"].split():
            mol = Chem.AddHs(mol)   # draw every H (carbon ladder: count the C–H bonds)
        values, shown = apply_spec(mol, r["os"], oxidation_states(mol))
        charge = sum(a.GetFormalCharge() for a in mol.GetAtoms())
        total = sum(values) + implicit_h_sum(mol)
        if total != charge:
            failures.append("%s: O.S. sum %s ≠ charge %d" % (r["label"], fmt(total), charge))
        failures += ["%s: %s" % (r["label"], e) for e in run_checks(mol, values, r["check"])]
        (outdir / (r["id"] + ".svg")).write_text(draw(mol, values, shown, size), encoding="utf-8")
        written.add(r["id"] + ".svg")
        gallery.append("| ![%s](mol/%s.svg) | %s | %s | %s |" % (
            r["label"], r["id"], r["label"], summary(mol, values, shown, "show:" in r["os"]) or "—", r["note"] or "—"))
    for stale in outdir.glob("*.svg"):
        if stale.name not in written:
            stale.unlink()
            print("  removed stale %s" % stale.relative_to(ROOT))
    md = replace_block(md, "gallery", "\n".join(gallery))
    md = replace_block(md, "smiles", "```smiles\n%s\n```" % "\n".join(r["smiles"] for r in rows))
    src.write_text(md, encoding="utf-8")
    print("%s: %d structures -> %s/" % (src.relative_to(ROOT), len(written), outdir.relative_to(ROOT)))
    return rows, failures


def write_library(path, sources):
    lines = ["# Compound library", "",
             "Generated by `scripts/render_structures.py --library`; do not edit by hand. Every",
             "structure drawn anywhere in the notes, one row each. Point ChemEdit's **Compound Library",
             "File Path** setting at this file to insert any of them with *Insert SMILES from Library*.",
             "", "SMILES are written raw, without backticks, because ChemEdit reads column 2 verbatim. On",
             "GitHub a SMILES containing `](` (e.g. `[Cr](=O)`) therefore displays as a link; the text",
             "in the file is still correct.",
             "", "| Name | SMILES | Chapter |", "|---|---|---|"]
    n = 0
    for src in sources:
        chapter = src.parent.parent
        rel = Path("..") / src.relative_to(ROOT)
        for r in parse_table(src.read_text(encoding="utf-8")):
            lines.append("| %s | %s | [%s](%s) |" % (r["label"], r["smiles"], chapter.name,
                                                   rel.as_posix()))
            n += 1
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("%s: %d compounds" % (path.relative_to(ROOT), n))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("sources", nargs="*", type=Path)
    ap.add_argument("--all", action="store_true", help="every */figures/structures.md in the repo")
    ap.add_argument("--validate", action="store_true",
                    help="check the tables' SMILES and O.S. assertions only; draw nothing")
    ap.add_argument("--size", default="240x170", help="WxH of each drawing in px")
    ap.add_argument("--library", type=Path, help="also write the combined compound library here")
    args = ap.parse_args()

    if args.validate:
        srcs = [p.resolve() for p in args.sources]
        if args.all or not srcs:
            srcs += sorted(p for p in ROOT.glob("*/*/figures/structures.md") if p not in srcs)
        if not srcs:
            ap.error("give a structures.md path or --all")
        bad, total = [], 0
        for s in srcs:
            errs, n = validate(s)
            total += n
            print("%-62s %3d structures  %s"
                  % (s.relative_to(ROOT), n, "OK" if not errs else f"{len(errs)} PROBLEM(S)"))
            bad += ["  %s: %s" % (s.relative_to(ROOT), e) for e in errs]
        if bad:
            print("\nFAILED CHECKS:\n" + "\n".join(bad), file=sys.stderr)
            sys.exit(1)
        print("\n%d structures validated, all SMILES parse and every assertion holds" % total)
        return

    try:
        from rdkit.Chem import rdDepictor
        from rdkit.Chem.Draw import rdMolDraw2D  # noqa: F401  (fails early if drawing is broken)
    except ImportError as e:
        sys.exit("RDKit drawing unavailable (%s): pip install rdkit" % e)
    rdDepictor.SetPreferCoordGen(True)  # CoordGen: textbook layouts (e.g. the CrO5 butterfly)

    sources = [p.resolve() for p in args.sources]
    if args.all:
        sources += sorted(p for p in ROOT.glob("*/*/figures/structures.md") if p not in sources)
    if not sources:
        ap.error("give a structures.md path or --all")
    size = tuple(int(x) for x in args.size.lower().split("x"))
    failures = []
    for src in sources:
        failures += process(src, size)[1]
    if args.library:
        write_library((ROOT / args.library) if not args.library.is_absolute() else args.library,
                      sorted(ROOT.glob("*/*/figures/structures.md")))
    if failures:
        print("\nFAILED CHECKS:\n  " + "\n  ".join(failures), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
