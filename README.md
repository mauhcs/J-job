# J-job — two ventures, one workbench

Working repo for two separate business ideas, kept in one system because they share a
principal, a network and a set of constraints.

- **`mrm`** — independent external verification of quantitative models; Japan, Hong Kong,
  East Asia.
- **`data`** — signal research on alternative datasets, sold to the data owner as the
  evidence a trading desk needs before buying.
- **`shared`** — profile-level material bearing on both.

Principal: Mauricio — Chief Scientist, IPOR Labs; Adjunct Assistant Professor, Temple
University Japan. Background in HFT, quant trading and risk modelling.

## How this repo works

Git is the database. Every fact, organisation, person, venue, task and finding is one
Markdown file with YAML front-matter. `build.py` walks the tree, validates it, and
inlines the whole graph into `dashboard.html` for browsing.

    python3 build.py          # rebuild dashboard.html from entities/, notes/, tasks/, streams/

See `SCHEMA.md` for the field definitions.

## Workstreams

**data**

| id | stream | question it answers |
|----|--------|---------------------|
| `stream-data-market` | Market | Who sells, who buys, who evaluates, and where does a quant get paid? |
| `stream-data-offer` | Offer | What exactly is sold, and is it defensible beside Exabel? |

**mrm**

| id | stream | question it answers |
|----|--------|---------------------|
| `stream-market` | Market | Who sells this service, who buys it, and at what price? |
| `stream-advisor` | 顧問 | Who opens doors, and how do we reach them? |
| `stream-publishing` | Publishing | Where do we publish/present, what is the state of the art, what do we write? |
| `stream-positioning` | Positioning | What exactly are we selling, under which vehicle? |

## Status

Bootstrap pass, 2026-09-22. Seeded from a first research sweep; every claim carries its
source. Entries marked `confidence: low` are hypotheses, not findings.
