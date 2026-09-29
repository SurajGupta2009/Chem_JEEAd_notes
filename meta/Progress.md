# Chemistry progress

Open this page in Obsidian after installing and enabling **Dataview** — it needs no other
plugin and never needs hand-editing, because every column comes from the frontmatter of the
`notes.md` files themselves.

```dataview
TABLE branch, chapter, class, ncert_unit, status, words, updated
FROM "Physical-Chemistry" OR "Inorganic-Chemistry" OR "Organic-Chemistry" OR "Practical-Chemistry"
WHERE file.name = "notes"
SORT branch ASC, file.folder ASC
```

A chapter appears here only once it has a `notes.md`, so **Organic Chemistry (9 chapters) and
every chapter not yet listed are simply absent** — the branch indexes carry the full list of
all 30 NCERT chapters plus Salt Analysis. The same table, with word, diagram and structure
counts, is in the root [`README.md`](../README.md#status).

To check a note against the format spec:

```bash
python3 scripts/check_notes.py
```
