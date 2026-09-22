---
id: task-reharvest-shotan
type: task
name: Re-harvest the 少額短期保険協会 member list programmatically
status: idea
priority: 2
owner: claude
due: 2026-10-31
confidence: high
tags: [intake, data-quality]
rel: [org-shogaku-tanki-hoken, note-sme-wedge]
updated: 2026-09-22
---

`intake/shotan-kyokai.tsv` was transcribed by hand from a fetched copy of the association's
member page and captured **122 of 123 正会員** — one row was lost and has not been
reconciled. Hand transcription is not a repeatable intake method and should not be the
precedent this pipeline sets.

Write a small fetch-and-parse step that reads the page and emits the TSV directly, then
re-run `python3 tools/intake.py shotan-kyokai` and confirm the count reconciles to the
association's own figure. The 準会員 and 30 賛助会員 are also not yet captured; 賛助会員 are
service providers to the segment and are a separate, interesting list — they know which
members are model-dependent.
