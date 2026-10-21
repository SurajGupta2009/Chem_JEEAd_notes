"""Generate index.html — the gallery and download page."""
from __future__ import annotations

import html
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

CSS = """
:root{--navy:#16254d;--teal:#0a6b62;--gold:#b8860b;--red:#b3261e;--ink:#1b2a4a;--paper:#fffdf8}
*{box-sizing:border-box}
body{margin:0;background:#f2efe6;color:var(--ink);font-family:Georgia,"Times New Roman",serif;line-height:1.45}
header{background:var(--navy);color:#fff;padding:30px 6vw 24px}
header h1{margin:0 0 8px;font-size:clamp(24px,3.4vw,40px)}
header p{margin:5px 0;color:#d8dfef;max-width:75ch}
.wrap{max-width:1180px;margin:0 auto;padding:0 20px 60px}
section{margin:38px 0}
h2{color:var(--navy);border-bottom:2px solid var(--gold);padding-bottom:6px;font-size:clamp(18px,2.2vw,26px)}
h3{color:var(--teal);margin:26px 0 10px}
.dl{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));margin:18px 0}
.card{background:var(--paper);border:1px solid #d9d3c2;border-left:5px solid var(--teal);border-radius:6px;padding:14px 16px}
.card b{display:block;color:var(--navy);margin-bottom:4px}
.card a{color:var(--teal)}
.card span{color:#5a6472;font-size:.9em}
table{border-collapse:collapse;width:100%;font-size:.93em;background:#fff}
th,td{border:1px solid #d9d3c2;padding:6px 8px;text-align:left;vertical-align:top}
th{background:#eef1f6;color:var(--navy)}
td.num{text-align:right;white-space:nowrap}
.grid{display:grid;gap:22px;grid-template-columns:repeat(auto-fill,minmax(240px,1fr))}
figure{margin:0;background:var(--paper);border:1px solid #d9d3c2;border-radius:6px;padding:8px;box-shadow:0 1px 2px rgba(0,0,0,.06)}
figure img{width:100%;height:auto;display:block;border:1px solid #eee}
figcaption{font-size:.82em;color:#3d4b66;margin-top:6px}
figcaption b{color:var(--navy)}
.tag{display:inline-block;font-size:.72em;letter-spacing:.04em;text-transform:uppercase;background:var(--teal);color:#fff;border-radius:3px;padding:1px 6px;margin-left:6px}
.note{background:#fff8e1;border-left:5px solid var(--gold);padding:12px 16px;border-radius:4px}
.warn{background:#fdecea;border-left:5px solid var(--red);padding:12px 16px;border-radius:4px}
footer{color:#5a6472;font-size:.88em;padding:24px 6vw 48px;border-top:1px solid #d9d3c2}
code{background:#eef1f6;padding:1px 4px;border-radius:3px;font-size:.92em}
"""


def esc(s):
    return html.escape(str(s), quote=True)


def write_index(parts, summary):
    galleries, rows = [], []
    for label, folder, pdf, ranges in parts:
        files = sorted(f for f in os.listdir(os.path.join(ROOT, folder)) if f.endswith(".png"))
        cards = []
        for sid, title, first, n in ranges:
            for k in range(n):
                page_no = first + k + 1
                fname = next(f for f in files if f.split("_")[1] == f"p{page_no:02d}")
                cards.append(
                    '<figure><a href="{folder}/{f}"><img loading="lazy" src="thumbs/{stem}.jpg" '
                    'alt="{sid} page {k1}"></a><figcaption><b>{sid}</b> \u2014 {title}<br>'
                    'page {k1} of {n} \u00b7 sheet {page_no}</figcaption></figure>'.format(
                        folder=folder, f=esc(fname), stem=esc(fname[:-4]), sid=esc(sid), k1=k + 1,
                        title=esc(title), n=n, page_no=page_no))
                rows.append((label, sid, title, k + 1, n))
        galleries.append(
            f'<h3>{esc(label)}<span class="tag">{sum(r[3] for r in ranges)} pages</span></h3>'
            '<div class="grid">' + "".join(cards) + "</div>")

    table_rows = "".join(
        '<tr><td>{l}</td><td>{s}</td><td>{t}</td><td class="num">{k}</td>'
        '<td class="num">{n}</td></tr>'.format(l=esc(l), s=esc(sid), t=esc(title), k=k, n=n)
        for l, sid, title, k, n in rows)
    total = sum(s[2] for s in summary)
    sheets = sum(s[1] for s in summary)

    body = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Stereoisomerism — handwritten short notes (JEE Main + Advanced)</title>
<style>{CSS}</style></head>
<body>
<header>
  <h1>Stereoisomerism — complete handwritten short notes</h1>
  <p>Part I: JEE Main + JEE Advanced core. Part II: extensions up to JEE Advanced
     (no Olympiad section). {sheets} sheets, {total} A4 portrait pages, 2480 × 3508 px, 300 dpi.</p>
  <p>Teacher-style: concept → reasoning → worked example → result to memorise → the trap that follows.
     Every page carries its part, sheet id and page number.</p>
</header>
<div class="wrap">

<section>
  <h2>Download</h2>
  <div class="dl">
    <div class="card"><b><a href="downloads/stereoisomerism-complete-png.zip">Complete PNG set (ZIP)</a></b>
      <span>All {total} pages, Part I first, plus both PDFs. 2,480 × 3,508 px, 300 dpi.</span></div>
    <div class="card"><b><a href="downloads/stereoisomerism-part1-jee-png.zip">Part I — JEE PNGs (ZIP)</a></b>
      <span>J-01 … J-29 · {summary[0][2]} pages.</span></div>
    <div class="card"><b><a href="downloads/stereoisomerism-part2-extensions-png.zip">Part II — extension PNGs (ZIP)</a></b>
      <span>X-01 … X-12 · {summary[1][2]} pages.</span></div>
    <div class="card"><b><a href="pdf/stereoisomerism-complete.pdf">Complete PDF (A4, bookmarked)</a></b>
      <span>Part I then Part II, one sheet per page, a bookmark per sheet.</span></div>
    <div class="card"><b><a href="pdf/stereoisomerism-jee.pdf">Part I PDF</a></b>
      <span>{summary[0][2]} A4 pages, bookmarked.</span></div>
    <div class="card"><b><a href="pdf/stereoisomerism-extensions.pdf">Part II PDF</a></b>
      <span>{summary[1][2]} A4 pages, bookmarked.</span></div>
  </div>
  <div class="note"><b>Printing.</b> A4 portrait, <b>one sheet per page</b>, scale <b>Fit</b> —
  not <i>Fill</i> and not <i>Crop</i>. The PNGs are already exactly A4 at 300 dpi, so printing
  them at 100 % and at “Fit” gives the same result. Details in
  <a href="PRINTING.txt">PRINTING.txt</a>.</div>
</section>

<section>
  <h2>What is inside</h2>
  <p><b>Part I (29 sheets)</b> — the isomerism map and the vocabulary; geometrical isomerism
  (the two conditions, C=N centres and the oxime family, E/Z and CIP, rings, cumulenes, spiro,
  bicyclics, counting, physical properties); optical isomerism (the polarimeter and specific
  rotation, chirality and the σ/i/S<sub>n</sub> test, meso and racemic, resolution,
  projections, R/S, D/L, <i>threo</i>/<i>erythro</i>, chirality without a stereocentre,
  counting, relation questions); conformational analysis (barriers, ethane and butane,
  cyclohexane, substituted cyclohexanes); reaction stereochemistry (S<sub>N</sub>1/S<sub>N</sub>2,
  E2, syn/anti addition, hydrogenation); the C<sub>5</sub>H<sub>11</sub>Cl enumeration;
  twenty traps; and a one-page recall sheet.</p>
  <p><b>Part II (12 sheets)</b> — symmetry rigorously (five operations, the S<sub>1</sub> = σ and
  S<sub>2</sub> = i identities, point groups of ethane conformers, a chirality decision tree),
  axial chirality, ring junctions, trans-cycloalkenes and Bredt's rule, quantitative
  conformational analysis (A-values, 1,3-diaxial interactions, the anomeric effect), the
  ring-flip path, stereospecific versus stereoselective reactions and the Cram/Felkin–Anh
  models, enumeration by orbit counting (Burnside), topicity and pseudoasymmetry, ee and
  chiroptical methods, eight solved Advanced problems, applications, and a final audit.</p>
  <p><a href="SCOPE.md">SCOPE.md</a> maps every lecture of the source to a sheet and classifies
  each sheet as core / advanced / support. <a href="SOURCE-AUDIT.md">SOURCE-AUDIT.md</a> records
  the conflicts found inside the source, the corrections made, and exactly what was and was
  not verified.</p>
</section>

<section>
  <h2>Page index</h2>
  <table><thead><tr><th>Part</th><th>Sheet</th><th>Title</th>
  <th class="num">Page in sheet</th><th class="num">Pages</th></tr></thead>
  <tbody>{table_rows}</tbody></table>
</section>

<section>
  <h2>Gallery</h2>
  {''.join(galleries)}
</section>

</div>
<footer>
  Built from <code>content/</code> by <code>build/build.py</code> and <code>build/package.py</code>
  (PyMuPDF), checked by <code>checks/verify.py</code>. Source lecture notes:
  <code>source/NS-Sir-Stereoisomerism-Complete-Notes.md</code>. Numerical values are textbook
  ranges, not measurements; no claim of exhaustive chemical verification is made — see
  SOURCE-AUDIT.md.
</footer>
</body></html>
"""
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(body)
    return len(rows)
