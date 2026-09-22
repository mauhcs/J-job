# J-job — working instructions

Business plan for **independent external verification of quantitative models**, focused on
Japan, Hong Kong and East Asia. Principal: Chief Scientist at IPOR Labs, Adjunct Assistant
Professor at Temple University Japan; background in HFT, quant trading and risk modelling.

**Git is the database.** Every organisation, person, venue, task and finding is one Markdown
file with YAML front-matter. `dashboard.html` is a generated read model, never edited by hand.

    python3 build.py        # rebuild dashboard.html; validates the tree, 0 warnings expected

Read `SCHEMA.md` for fields and `INTAKE.md` for the company pipeline.

## When asked to add, update or clean up companies

**Do not hand-write company cards. Use the intake pipeline.** Hand-typing is not repeatable,
it loses rows, and it leaves no provenance. The loop:

1. Pick or add a source in `intake/sources.yaml`. Prefer `kind: register` (a regulator's own
   list of licensed entities) over `association`, and both over `database` or `editorial`.
2. Harvest it into `intake/<source-id>.tsv` — header row, required columns `name` and `url`;
   optional `name_ja`, `size`, `country`, `industry`, `captive`, `note`.
   **Harvest programmatically.** The first pass at `shotan-kyokai` was transcribed by hand and
   silently lost a row (`task-reharvest-shotan`).
3. `python3 tools/intake.py <source-id>` — dry run, then `--write`. It dedupes on id and on
   website host, and never overwrites an existing card.
4. Review each `status: candidate` stub: write the pitch and body, set `size` and `priority`,
   move to `status: qualified`. Only qualified and beyond appear in the Targets view.
5. `python3 build.py`, then commit.

**`url` / `site` must be the operating company, not a product page.** cashari is a product;
ガレージバンク株式会社 is the company, and the company is who signs a contract. When a source
gives a product page, find the corporate entity before qualifying the card.

**Verify every URL before carding it** (`curl -s -o /dev/null -w "%{http_code}" -L <url>`).
A 200 proves the domain serves a page, not that it belongs to the company — say so when the
attribution is inferred rather than taken from the source's own listing. A 403 is usually a
bot block, not a dead site. If DNS does not resolve, card it flagged as unverified.

## Never delete a company

    python3 tools/retire.py org-example "Acquired; now inside group MRM"

Retire instead — acquired, ceased, out of scope, no longer model-dependent, captive, or a
poor fit. The card stays searchable and drops out of Targets. The reason is the point: later
the useful question is *why did this come off the list*, and a deleted file cannot answer it.
Auto-retirement rules (such as the captive filter) may only ever touch `status: candidate`
cards — never one a human has qualified.

## Evidence rules

- Every sourced claim carries its link in a `## Sources` section. An unsourced claim is a
  hypothesis and the card must say `confidence: low`.
- **Never invent people.** Named individuals enter the repo only with a public source; until
  then use an `archetype` card describing the profile to look for.
- Say plainly which facts came from a page you actually opened versus a search-result
  summary. They are not the same evidence.

## Current shape of the plan

Four workstreams in `streams/`: market, 顧問 (advisor), publishing, positioning. The market is
tiered `startup -> sme -> mid -> large -> mega` and worked **upward** — below the JFSA
Principles' scope the buyer is not the regulator but the warehouse lender, securitisation
investor, bank partner or VC in diligence. See `notes/sme-wedge.md`. Match the 顧問 to the
buyer tier, not the prestige ladder.
