---
id: note-deliverable-spec
type: note
space: mrm
name: What the deliverable actually is, and why effort is the open question
status: researching
priority: 1
confidence: med
tags: [delivery, methodology, product, effort]
rel: [note-correction-invented-numbers, note-unit-economics, org-jfsa, org-hkma, artifact-flagship-paper, stream-positioning]
updated: 2026-09-22
---

Nothing in this repo had specified the product. Without a defined deliverable there is no
work breakdown, no effort estimate, and therefore no price — which is how the fabricated
numbers in `note-correction-invented-numbers` happened.

## The report structure is not a matter of opinion

SR 11-7 — the template JFSA's Principles and HKMA's SPM both follow — defines validation as
**three components**, and a validation report is organised around them:

1. **Conceptual soundness.** Is the model design and construction defensible? Review of
   documentation and of the empirical evidence supporting the methods used and the variables
   selected. This is the judgement-heavy part and the part that cannot be automated.
2. **Ongoing monitoring.** Does it still perform as intended in production, is it being used
   for what it was built for, and are the limits and assumptions still holding?
3. **Outcomes analysis.** Testing that the results are appropriate — backtesting and
   performance testing. Where a model leans on expert judgement, quantitative outcomes
   analysis is what substitutes for that judgement being unexaminable.

The same guidance decomposes a model into **input, estimation, and reporting** components,
and each gets reviewed separately. HKMA adds two usable constraints: validation **must not be
limited to back-testing**, and institutions must maintain a **model inventory** with scope,
materiality and methodology per model.

So the deliverable is specifiable: a report covering three components across three model
layers, with findings rated by severity, limitations stated, and a conclusion on fitness for
the declared use.

## The part that is genuinely unknown: effort

**No published data was found on how long a model validation takes.** Industry material says
only that validation is "time-consuming and resource intensive" and that duration varies with
model complexity, data preparation, portfolio size and model type. Vendors sell automation to
reduce it, which tells you it is large, and tells you nothing about how large.

The realistic shape of the work, with honest unknowns:

| stage | what it involves | effort |
|---|---|---|
| Scoping | what the model decides, materiality, declared use | days |
| Understanding | documentation, code, data dictionary, interviews with the builder | **unknown — plausibly weeks** |
| Data | obtaining it, checking quality, reconstructing the development sample | unknown, often the worst part |
| Replication | rebuilding enough of the model to test it independently | unknown |
| Testing | backtesting, stability, sensitivity, benchmark comparison | unknown |
| Write-up | findings, severity ratings, limitations, conclusion | days |

**Understanding and data are the dominant costs, and they do not shrink with the size of the
client.** A ten-person lender's model can take as long to understand as a bank's — sometimes
longer, because it is less documented. That is precisely why the startup tier's economics
fail: the effort floor is set by the model, not by the buyer's budget.

## What this implies

- **Price cannot be set until one has been done.** The first engagement is the measurement.
- **Repeatability is the whole margin.** Same model class, second time: the protocol, test
  suite and report skeleton already exist. Different class every time: no leverage ever.
- **Scope must be bounded contractually** — one named model, declared use, fixed deliverable,
  stated exclusions — or "understanding the model" consumes the engagement.

## Open questions

- What does a real validation report look like? Obtain a redacted example, or write one
  against a public model, and time it honestly.
- How many days does a competent validator spend on a mid-complexity credit scorecard?
  Ask someone who does this for a living — an expert-network call is a legitimate way to buy
  that answer.

## Sources

- [Federal Reserve SR 11-7 / revised guidance](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.pdf)
- [SR 11-7 three core elements of validation](https://www.datavisor.com/blog/model-validation-3-core-elements-for-sr-11-7-compliance)
- [Delta Capita on validation effort and automation](https://www.deltacapita.com/insights/innovating-model-validation-processes-for-retail-credit-risk-models-embracing-automation-and-efficiency)
- [PwC HK: validation should not be limited to back-testing](https://www.pwchk.com/en/financial-services/publications/model-risk-management-achieving-better-compliance-jul2024.pdf)
