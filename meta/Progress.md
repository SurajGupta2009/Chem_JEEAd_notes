# Chemistry progress

Open this page in Obsidian after installing and enabling **Dataview**.

```dataview
TABLE branch, chapter, status, words, updated
FROM "Physical-Chemistry" OR "Inorganic-Chemistry" OR "Organic-Chemistry" OR "Practical-Chemistry"
WHERE file.name = "notes"
SORT branch ASC, file.folder ASC
```

The other chapter folders are pending until they receive a `notes.md`. See the branch indexes for all 30 NCERT chapters.
