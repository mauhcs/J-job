---
id: note-altdata-offer-design
type: note
name: Offer design — where there is room beside Exabel
status: researching
priority: 1
confidence: low
tags: [altdata, offer, positioning, differentiation]
rel: [stream-data-offer, org-exabel, org-eagle-alpha, org-battlefin, note-altdata-evaluation-gap, note-altdata-japan]
updated: 2026-09-22
---

The proposition — *"give me access to your data and I will find something meaningful"*, sold
to the data owner as sales collateral — is sound in its economics and **already productised**
by `org-exabel`. This note is about whether anything is left, and it is deliberately
unflattering before it is encouraging.

## Where a platform structurally cannot go

1. **Beyond equities and consensus KPIs.** Exabel's proof of value is benchmarked against
   Visible Alpha ground truth — i.e. equity revenue and KPI consensus. Datasets relevant to
   **rates, FX, commodities, credit and crypto** have no such ground truth, so the platform
   approach does not transfer. **This is the strongest gap, and it happens to be the
   profile's home ground.**
2. **Incremental value against an existing book.** A platform answers "does this dataset
   predict something". A trading desk asks a harder question: *"does it add anything to what I
   already run?"* Orthogonality to existing factors, marginal contribution to a live strategy,
   capacity, turnover and transaction costs are bespoke analysis, not a product feature.
   **This is the stated methodology — with and without the dataset — and it is the correct
   question.**
3. **Shock and regime analysis.** Whether a signal survives a crisis, a regime change, or a
   liquidity shock is exactly what a desk's risk officer will ask and exactly what a
   standardised backtest does not show. An HFT and risk-modelling background is the credential
   for that conversation, and it is a scarce one.
4. **Vendors upstream of a platform.** A corporate with raw exhaust data does not know whether
   there is a product in it at all. That is a discovery question, not an evaluation question,
   and it is unsuited to a self-serve platform.
5. **Japan.** Japanese-language data, Japanese vendors, Japanese corporate relationships, and a
   local shortage of people who can do the work. See `note-altdata-japan`.

## What the offer could therefore be

**"Independent scoping of a dataset's trading value, for owners who want to sell it."**

A fixed-scope engagement producing a report the vendor can hand to a desk:

- What is in the data, its coverage, history, latency, point-in-time integrity and survivorship
  properties — the things that kill a dataset before any signal test.
- Candidate signals, constructed and tested honestly, with the multiple-testing problem
  addressed rather than ignored.
- **A strategy backtest with and without the dataset**, with risk parameters, drawdown, and
  shock and regime conditioning.
- An honest statement of capacity, decay and what the dataset does *not* do.

**The credibility of the negative is the product.** A report that says "this adds nothing to a
momentum book but is genuinely orthogonal for a consumer-sector desk" is worth more to a buyer,
and therefore to the vendor, than a promotional backtest — and it is the thing a platform
optimising for vendor satisfaction is least able to say.

## The distribution half, honestly

The idea of offering data sellers a small buyer network runs straight into `org-battlefin`,
which already runs curated Discovery Days with pre-scheduled one-to-one meetings between vetted
vendors and institutional buyers, and into Neudata and Eagle Alpha, who do introductions as
their core business.

**Do not compete on distribution.** Be the researcher whose report a vendor brings *to* those
meetings. Referral in the other direction is the realistic relationship: brokers have vendors
who cannot close, and those vendors need evidence.

## What has to be true for this to work

- Data vendors have a pre-sales budget and spend it on outside research. **Unknown.**
- They will pay enough to cover weeks of quant work. **Unknown, and the same trap as the last
  venture — do not assume a price.**
- An independent report from an unknown researcher carries weight with a desk. This is where
  the academic affiliation does real work, and it is worth more here than in model validation.
- The work is repeatable enough to compound: a reusable evaluation harness, applied to many
  datasets, rather than bespoke every time. **This is the difference between a business and a
  job**, and it should be built into the first engagement.

## The thing to do first

Not build the harness. **Talk to three data vendors and ask what they currently do to prove
their data works, what it costs them, and what happens when a fund says no.** That is
`task-altdata-vendor-interviews`, and it is the same lesson as last time: verify the demand
before designing the product.
