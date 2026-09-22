# J-job — working instructions

Business plan for **independent external verification of quantitative models**, focused on
Japan, Hong Kong and East Asia. Principal: Chief Scientist at IPOR Labs, Adjunct Assistant
Professor at Temple University Japan; background in HFT, quant trading and risk modelling.

**Git is the database.** Every organisation, person, venue, task and finding is one Markdown
file with YAML front-matter. `dashboard.html` is a generated read model, never edited by hand.

    python3 build.py        # rebuild dashboard.html; validates the tree, 0 warnings expected

Read `SCHEMA.md` for fields and `INTAKE.md` for the company pipeline.

## When asked to add, update or clean up companies

**Do not hand-write company cards, and do not mint a card per harvested row.** Both were
tried and both were wrong. Hand-typing is not repeatable and loses rows; bulk-minting fills
the repo with entries nobody has read and forces fake lifecycle events.

The universe from a source lives in `intake/<source-id>.tsv` (the **pool**, browsable in the
dashboard's Pool tab). A file under `entities/org/` means a human formed a judgement.

1. Register the source in `intake/sources.yaml`. Prefer `kind: register` (a regulator's own
   list of licensed entities) over `association`, both over `database` or `editorial`.
2. Harvest it **programmatically** into `intake/<source-id>.tsv`.
3. `python3 tools/intake.py <source-id>` to read the pool.
4. `python3 tools/intake.py <source-id> --promote <host>` for rows worth a card, then write
   the card properly and set `status: qualified`.
5. `python3 tools/intake.py <source-id> --exclude <host> "reason"` for rows that are not.
   The row keeps its reason in the TSV; no card is created.
6. `python3 build.py`, then commit.

**`url` / `site` must be the operating company, not a product page.** cashari is a product;
ガレージバンク株式会社 is the company, and the company is who signs a contract.

**Verify every URL before carding it** (`curl -s -o /dev/null -w "%{http_code}" -L <url>`).
A 200 proves the domain serves a page, not that it belongs to the company — say so when the
attribution is inferred rather than taken from the source's own listing. A 403 is usually a
bot block, not a dead site. If DNS does not resolve, card it flagged as unverified.

## Retire only what was really a target

    python3 tools/retire.py org-example "Acquired; now inside group MRM"

Retirement is a real event in a relationship — acquired, ceased, declined, thesis disproved.
It keeps the card searchable and drops it out of Targets, because later the useful question
is *why did this come off the list*.

**A company that never should have been carded is not a retirement, it is an intake
mistake**: delete the card and exclude the pool row with a reason. Automated rules (such as
the captive filter) belong at the pool level and must never touch a card a human wrote.

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
