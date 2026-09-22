# Intake & lifecycle

How companies enter this repo, and how they leave it.

## The distinction that matters

**A harvested row is not a company we are pursuing.** A source gives us a universe — 123
micro-insurers, 39 alternative lenders, eight digital banks. Most of them we will never
approach, and until someone has looked at one there is nothing to say about it.

So the universe lives in `intake/<source-id>.tsv`, committed to git and browsable in the
dashboard's **Pool** tab. A file under `entities/org/` means something stronger: a human
looked at this company and formed a judgement worth writing down.

Minting a card per harvested row was the first design and it was wrong. It filled the repo
with 86 near-empty entries that duplicated the TSV and added nothing, and it forced a fake
lifecycle event — 31 companies "retired" within minutes of being created, having never been
targets at all. Filtering at intake is not retirement.

## The loop

    1. register the source        intake/sources.yaml
    2. harvest it, programmatically   -> intake/<source-id>.tsv
    3. read the pool              python3 tools/intake.py <source-id>
    4. promote what is worth it   python3 tools/intake.py <source-id> --promote <host>
    5. write the card             entities/org/<host>.md, status: qualified
    6. rebuild                    python3 build.py

Rows you decide against never become cards:

    python3 tools/intake.py <source-id> --exclude <host> "pet cover only, no underwriting model"

The row stays in the TSV with its reason, visible in the Pool tab under "show excluded".
Nothing is lost and nothing is cluttered.

## Pool states

| state | meaning |
|---|---|
| `pool` | harvested, nobody has looked yet. The default |
| `carded` | promoted; `card` holds the org id |
| `excluded` | judged not worth a card. `reason` required |

## Card lifecycle

Only companies someone has judged. A card never starts as an empty stub.

| status | meaning |
|---|---|
| `researching` | promoted, being written up. Not yet in Targets |
| `qualified` | it fits. Has `pitch`, `size`, `priority`. Appears in Targets |
| `contacted` | we have reached out |
| `engaged` | in conversation or scoping |
| `client` | paid work |
| `retired` | **was** a target and fell out. Requires `retired_reason` and `retired_on` |

Retirement is for companies that were genuinely in the pipeline: acquired, ceased, licence
surrendered, declined, or a thesis that turned out to be wrong. It is a real event in the
relationship, and the reason is worth keeping —

    python3 tools/retire.py org-example "Acquired by a megabank; now inside group MRM"

If a company never should have been carded, that is an intake mistake: delete the card and
exclude the row with a reason. Do not retire it — a retirement that never happened is noise
in the record.

## Sources

Register a source in `intake/sources.yaml` before harvesting. `kind` records what it is,
because that determines how far the rows can be trusted:

| kind | what it is | trust |
|---|---|---|
| `register` | a regulator's own list of licensed entities | highest — licensing is a fact |
| `association` | an industry body's member list | high — public, current, self-selecting |
| `award` | finalist and winner lists | medium — pre-qualified but incomplete |
| `database` | commercial startup databases | medium — coverage unknown, may be stale |
| `editorial` | articles, comparison blogs | low — second-hand; use to find names only |

Harvest **programmatically**. The first `shotan-kyokai` pass was transcribed by hand from a
fetched page and silently lost one of 123 rows (`task-reharvest-shotan`).

TSV columns: `name` and `url` required, then `name_ja`, `country`, `industry`, `size`,
`captive`, `note`, and the managed three — `state`, `reason`, `card`.

**`url` is the operating company, never a product page.** cashari is the product,
ガレージバンク株式会社 is the company, and the company signs the contract.
