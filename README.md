# J-job — Quantitative Model External Verification

Working repo for building a business plan around **independent external verification of
quantitative models**, focused on Japan, Hong Kong and East Asia.

Principal: Mauricio — Chief Scientist, IPOR Labs; Adjunct Assistant Professor, Temple
University Japan. Background in HFT, quant trading and risk modelling.

## How this repo works

Git is the database. Every fact, organisation, person, venue, task and finding is one
Markdown file with YAML front-matter. `build.py` walks the tree, validates it, and
inlines the whole graph into `dashboard.html` for browsing.

    python3 build.py          # rebuild dashboard.html from entities/, notes/, tasks/, streams/

See `SCHEMA.md` for the field definitions.

## Workstreams

| id | stream | question it answers |
|----|--------|---------------------|
| `stream-market` | Market | Who sells this service, who buys it, and at what price? |
| `stream-advisor` | 顧問 | Who opens doors, and how do we reach them? |
| `stream-publishing` | Publishing | Where do we publish/present, what is the state of the art, what do we write? |
| `stream-positioning` | Positioning | What exactly are we selling, under which vehicle? |

## Status

Bootstrap pass, 2026-09-22. Seeded from a first research sweep; every claim carries its
source. Entries marked `confidence: low` are hypotheses, not findings.
