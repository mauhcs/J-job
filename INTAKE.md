# Intake & lifecycle

How companies enter this repo, move through the pipeline, and leave it without being deleted.

## The loop

    source (authoritative register or association list)
      -> intake/<source-id>.tsv        harvested rows, one company per line
      -> python3 tools/intake.py <source-id>
      -> entities/org/*.md             stubs, status: candidate, provenance recorded
      -> review pass                   write pitch + body, set size/priority
      -> status: qualified             now visible in the Targets view
      -> contacted -> engaged -> client
      -> or: python3 tools/retire.py <id> "reason"

Nothing is ever deleted. A company that falls out of the path is **retired** with a dated
reason, stays searchable in Browse, and disappears from the Targets view unless you ask to
see it. Git keeps the history; the card keeps the judgement.

## Adding a source

Register it in `intake/sources.yaml` first — id, name, url, kind, jurisdiction, authority,
cadence. `kind` records what it actually is, because that determines how much the rows can
be trusted:

| kind | what it means | trust |
|---|---|---|
| `register` | a regulator's own list of licensed entities | highest — licensing is a fact |
| `association` | an industry body's member list | high — public, current, self-selecting |
| `award` | finalist/winner lists | medium — pre-qualified but incomplete |
| `database` | commercial startup databases | medium — coverage unknown, may be stale |
| `editorial` | articles, comparison blogs | low — second-hand, use only to find names |

Then produce `intake/<source-id>.tsv` with a header row. Required columns: `name`, `url`.
Optional: `name_ja`, `size`, `country`, `industry`, `note`, `licence`.

## Running intake

    python3 tools/intake.py shotan-kyokai            # dry run, reports what would happen
    python3 tools/intake.py shotan-kyokai --write    # actually mint the stubs

It dedupes on id **and on website host**, so re-running a source after it updates only adds
what is genuinely new. Companies already carded are reported as known and left untouched —
intake never overwrites a card you have written.

## Lifecycle states

Buyer companies use a pipeline; everything else uses the general states.

| state | meaning |
|---|---|
| `candidate` | harvested, not yet reviewed. No pitch, no judgement, not in Targets |
| `qualified` | reviewed and it fits. Has `pitch`, `size`, `priority`. In Targets |
| `contacted` | we have reached out |
| `engaged` | in conversation or scoping |
| `client` | paid work |
| `retired` | out of the path. Requires `retired_reason` and `retired_on` |

## Retiring

    python3 tools/retire.py org-example "Acquired by a megabank; now inside group MRM"

Retire rather than delete whenever a company stops being a target — acquired, licence
surrendered, wound down, no longer model-dependent, or simply judged a poor fit. The reason
is the point: in six months the useful question is not *who is on the list* but *why did we
take this one off*, and a deleted file cannot answer that.

Reasons worth recording explicitly: `acquired`, `ceased`, `out-of-scope`, `no-model`,
`captive` (parent group provides the function), `unreachable`, `declined`.
