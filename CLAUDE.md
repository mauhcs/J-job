# J-job — working instructions

**Separate projects live in this repo, as separate databases.** Principal for both:
Chief Scientist at IPOR Labs, Adjunct Assistant Professor at Temple University Japan;
background in HFT, quant trading and risk modelling.

    model-validation/    independent external verification of quantitative models
    data-signal/         scoping the trading value of a dataset for its owner
    game-ml/             applied machine learning for Japanese game companies
    jobs/                roles that fit the profile

To add a project: create the directory tree and add an entry to `PROJECTS` in `build.py`.

**They never mix.** Each has its own `entities/`, `notes/`, `tasks/`, `streams/`, `intake/`
and its own generated `dashboard.html`, published as its own artifact. A card lives in exactly
one project; there is no shared space and no cross-project `rel` edge — `build.py` reads one
tree at a time and drops any reference pointing outside it. Material about the principal
(affiliations, capacity, the sales constraint) is a topic **inside model-validation**, not a
third thing.

When asked to work on something, establish which project it belongs to first, and stay in
that tree.

**Git is the database.** Every organisation, person, venue, task and finding is one Markdown
file with YAML front-matter. Dashboards are generated and never edited by hand.

    python3 build.py                   # rebuild both dashboards; 0 warnings expected
    python3 tools/check_dashboard.py   # static-check both BEFORE publishing

**Always run the checker before publishing.** A JavaScript error blanks every view at once
and the page still looks like a valid HTML file — it happened when a top-level `let` was used
before its declaration. The checker catches syntax errors, missing element ids, and
use-before-declaration.

Read `SCHEMA.md` for fields and `INTAKE.md` for the company pipeline.

**Keep each project actionable or it is noise.** Each dashboard lands on a **Do next** list
built from its priority-1 tasks, so:

- **Priority 1 means live work, about three per project.** Adding a fourth means something
  drops to 2. `build.py` warns past four.
- **Every priority-1 task needs a `decides:` line** — one sentence on what answering it
  settles. The build fails without it. A task that settles nothing is not a task.
- Notes and organisations are background *for* those decisions, not actions. Adding research
  without changing what to do next makes the plan less usable, not more.

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

## Job cards (`jobs/`)

A listing on an aggregator is not a job. A card requires a **named employer**, a **direct
link**, and a `verified` value — `jd-read` (description opened, requirements and pay quoted) or
`listing-confirmed` (seen on the employer's own site or a board naming the employer, but the
description is unread). `build.py` fails without a link.

**Go to employers, not aggregators.** ATS boards render for fetching — `jobs.lever.co/<co>`,
`job-boards.greenhouse.io/<co>`, `jobs.ashbyhq.com/<co>` — and employer career sites carry
roles the aggregators never surface. The best role in the jobs project was found on IMC's own
site after aggregators had been scraped for two passes.

**Open the description before rating fit.** Gauntlet was rated a strong fit twice on what the
firm does; the posting says remote is US and Canada only, and the role wants structured credit,
not rates. Both facts were one click away. State location eligibility and the gap, never just
the fit.

## Evidence rules

- Every sourced claim carries its link in a `## Sources` section. An unsourced claim is a
  hypothesis and the card must say `confidence: low`.
- **Never invent people.** Named individuals enter the repo only with a public source; until
  then use an `archetype` card describing the profile to look for.
- Say plainly which facts came from a page you actually opened versus a search-result
  summary. They are not the same evidence.

## Current focus

`game-ml` is newest. `data-signal` was reduced to a time-boxed credential project after its
business case failed on funded incumbents, small buyer budgets and no track record — see
`data-signal/notes/do-i-have-an-edge.md`, which also records the pattern across all three:
every idea so far has died on needing to acquire clients without a track record. Weigh any new
idea against that first.

`data-signal` previously ran a four-step sequence: build the evaluation harness on free data,
publish one worked example, take it to three vendors, then decide the unit of sale. The first
two steps need no client, introduction, entity or permission — deliberately.

`model-validation` is **parked**. Its four workstreams — market, 顧問 (advisor), publishing,
positioning — The market is
tiered `startup -> sme -> mid -> large -> mega` and worked **upward** — below the JFSA
Principles' scope the buyer is not the regulator but the warehouse lender, securitisation
investor, bank partner or VC in diligence. See `notes/sme-wedge.md`. Match the 顧問 to the
buyer tier, not the prestige ladder.
