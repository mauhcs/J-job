---
id: task-measure-real-validation-effort
type: task
name: Find out what a validation actually takes — in days
status: idea
priority: 1
owner: mau
due: 2026-11-30
confidence: high
tags: [delivery, effort, pricing, falsification]
rel: [note-deliverable-spec, note-correction-invented-numbers, note-unit-economics, task-subcontractor-registration]
updated: 2026-09-22
---

Every fee in this repo was wrong because the effort behind it was guessed. No published data
on validation duration was found, so it has to be obtained directly.

Three ways, cheapest first:

1. **Buy the answer.** Book an expert-network call with someone who runs model validation at a
   bank or a Big 4 practice and ask directly: for a mid-complexity credit scorecard, how many
   person-days across scoping, understanding, data, replication, testing and write-up? What
   fraction goes to understanding and data? An hour and a few hundred dollars.
2. **Do one and time it.** Write a full validation of a publicly documented model, against the
   SR 11-7 three-component structure, and record the hours honestly. This doubles as the
   methodology piece behind `artifact-flagship-paper` and as a work sample for
   `task-subcontractor-registration`.
3. **Subcontract once** and observe it from inside a firm that already knows.

Until one of these is done, **quote nothing**. A fixed-fee quote on a guessed effort is how a
first engagement becomes an unpaid quarter.
