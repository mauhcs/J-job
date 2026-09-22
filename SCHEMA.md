# Schema

One entity per file. YAML front-matter, then free Markdown prose for the body.

    entities/org/      organisations: regulators, sellers, buyers, channels
    entities/person/   advisor (顧問) candidates, contacts, archetypes
    entities/venue/    conferences, journals, seminars, media
    entities/artifact/ things we produce: papers, decks, whitepapers
    notes/             research findings
    tasks/             actionable items
    streams/           workstream definitions

## Fields

| field | required | values |
|-------|----------|--------|
| `id` | yes | unique slug, prefixed by type: `org-`, `person-`, `venue-`, `artifact-`, `note-`, `task-`, `stream-` |
| `type` | yes | `org` `person` `venue` `artifact` `note` `task` `stream` |
| `space` | yes | `mrm` · `data` · `profile` — exactly one; spaces never bleed |
| `decides` | P1 tasks | one sentence on what answering this settles. Required on priority-1 tasks |
| `name` | yes | display name |
| `name_ja` | no | Japanese name |
| `role` | no | org: `regulator` `seller` `buyer` `channel` · person: `advisor` `contact` `archetype` · venue: `conference` `journal` `seminar` `media` |
| `country` | no | `JP` `HK` `SG` `KR` `TW` `CN` `APAC` `GLOBAL` |
| `industry` | no | list: `banking` `securities` `insurance` `asset-mgmt` `crypto` `regulator` `academia` `consulting` |
| `size` | buyers | `startup` `sme` `mid` `large` `mega` — the target tier; drives the Targets view |
| `pitch` | buyers | one line: why *this* tier buys. Shown on the target card |
| `scope` | buyers | `company` (a real counterparty, runs the pipeline) or `segment` (an aggregate) |
| `site` | companies | the **operating company's** URL, not a product page. cashari is a product; ガレージバンク株式会社 is the company, and the company signs the contract |
| `source` | companies | the `intake/sources.yaml` id this came from, or `manual`. Provenance, permanently |
| `first_seen` | companies | ISO date the company entered the repo |
| `retired_on` / `retired_reason` | retired | required together. Set by `tools/retire.py` |
| `status` | yes | general: `idea` `researching` `confirmed` `contacted` `active` `parked` `done` · buyer companies use the pipeline instead: `researching` `qualified` `contacted` `engaged` `client` `retired` (see INTAKE.md) |
| `priority` | no | `1` high · `2` medium · `3` low |
| `confidence` | no | `low` `med` `high` — how much we trust what the body claims |
| `tags` | no | free list |
| `rel` | no | list of other `id`s — this is what makes the files a graph |
| `links` | no | list of `{label, url}` |
| `owner` | no | who acts on it |
| `due` | no | ISO date (tasks) |
| `updated` | yes | ISO date of last edit |

## Conventions

- **Sources go in the body**, as a `## Sources` section with links. A claim without a
  source is a hypothesis and the file must say `confidence: low`.
- **Do not invent people.** Named individuals are only added with a public source
  (company page, paper, conference programme). Until then use an `archetype` card that
  describes the profile to look for.
- `rel` edges are undirected in the dashboard — declaring it on one side is enough.
- **The pool is not the repo.** Harvested rows live in `intake/*.tsv`; a card under
  `entities/org/` means someone formed a judgement. Promote with `tools/intake.py`.
- **Retire only what was really a target** — `python3 tools/retire.py <id> "reason"`.
  In six months the useful question is not who is on the list but why someone came off it.
- **`site` is the operating company, never a product page.** Adding companies is a pipeline,
  not typing: harvest a source into `intake/<id>.tsv`, then `python3 tools/intake.py <id>`.
  See INTAKE.md.
- **Every `role: buyer` card needs `size` and `pitch`.** Without `size` it does not appear in
  the Targets view; the tiers run `startup` → `sme` → `mid` → `large` → `mega` and we work
  upward, each tier's reference case unlocking the next.
