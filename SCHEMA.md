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
| `name` | yes | display name |
| `name_ja` | no | Japanese name |
| `role` | no | org: `regulator` `seller` `buyer` `channel` · person: `advisor` `contact` `archetype` · venue: `conference` `journal` `seminar` `media` |
| `country` | no | `JP` `HK` `SG` `KR` `TW` `CN` `APAC` `GLOBAL` |
| `industry` | no | list: `banking` `securities` `insurance` `asset-mgmt` `crypto` `regulator` `academia` `consulting` |
| `status` | yes | `idea` `researching` `confirmed` `contacted` `active` `parked` `done` |
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
