---
id: note-sme-wedge
type: note
name: The SME wedge — go down-market, and who actually forces the purchase
status: confirmed
priority: 1
confidence: med
tags: [strategy, targeting, thesis, sme, wedge]
rel: [stream-market, stream-positioning, stream-advisor, org-jp-alt-lenders, org-jp-ai-credit-vendors, org-shogaku-tanki-hoken, org-garage-bank, person-archetype-fintech-operator, note-competitive-landscape, note-open-questions]
updated: 2026-09-22
---

The bootstrap research aimed at banks because that is where the regulation is. That was the
wrong end to start from, and this note records the correction.

## The problem with starting at the top

Megabanks have internal MRM teams (they built them after JFSA's 2021 Principles), the
longest procurement cycles in the market, the deepest vendor relationships, and an absolute
requirement for a domestic credibility signal we do not yet have. They are the hardest sale
available and they are the one everybody aims at.

## Who actually forces a purchase, by tier

This is the part that changes the plan. **At the SME and startup tier, the regulator is not
the buyer's motivation.** JFSA's Principles target major institutions; a 40-person lender is
not being examined against them. So the demand comes from somewhere else:

- **The warehouse lender.** Fintech lenders scale on warehouse facilities, then move loans
  off-book through whole-loan sales or securitisation. Setup runs through due diligence and
  documentation, and organised underwriting files and performance history speed lender review
  materially. An independent model opinion is a due-diligence accelerant with a direct cost
  of capital consequence.
- **The securitisation investor.** Japan's risk-retention rule requires bank investors to
  conduct extensive due diligence, confirming compliance not only at acquisition but each
  time capital is calculated. The originator's credit model is what that diligence is about.
- **The bank or insurer client.** For a model *vendor* (`org-jp-ai-credit-vendors`,
  `org-credit-engine`), the customer is a regulated institution whose own third-party model
  risk obligations — flagged as a weak area in the BoJ's August 2026 survey — flow straight
  back up to the vendor's model.
- **The VC in diligence.** A credit model is the core asset of a lending startup and the
  thing a Series B investor is least equipped to assess.

**The consequence:** at this tier we are not selling compliance. We are selling **cheaper
capital, faster diligence, and a closed sale** — which are easier things to sell, to a person
who can decide over coffee.

## The exception: regulated small institutions

`org-shogaku-tanki-hoken` is the one SME segment where the regulator *is* the driver, and it
may be the best of the lot. 少額短期保険業者 are licensed and supervised, **41% have fewer
than 10 employees and two-thirds fewer than 20**, and their own association presented on
internal audit sophistication to the FSA's working group in March 2025.

The FSA's broader internal-audit work says the same thing in general terms: small financial
institutions **cannot staff internal audit adequately**, and the suggested remedies are
leaning on a parent group's resources or peer-to-peer cooperation between similar
institutions. For an independent firm with no parent group, neither remedy is available.
That is a regulator-stated capability gap with no regulator-endorsed solution.

## Validation as a wedge, not a product

External validation is a **small, bounded, credible first engagement** — an unusually good
wedge because the buyer can say yes to it without a budget cycle, and because doing it
requires us to understand their model better than anyone outside the company. What follows
naturally is model redevelopment, risk framework build-out, pricing work, data strategy,
fractional CRO — i.e. consultancy, at consultancy rates.

Sell the wedge honestly: it is genuinely useful on its own, and a validation that exists only
to generate follow-on work will be seen through immediately.

## What this changes

1. **Tier the market explicitly** — startup → SME → mid → large → mega, and work upward.
   Each tier's reference case is what makes the next tier possible.
2. **Match the 顧問 to the tier.** An ex-megabank CRO cannot reach a 30-person lender. This
   creates `person-archetype-fintech-operator` and demotes the senior archetypes to year two.
3. **Reframe the pitch by tier.** Cost of capital and diligence speed at the bottom;
   supervisory expectation at the top.
4. **Start with the warm one.** `org-garage-bank` is a former employer with a genuinely
   novel model and no standard playbook to validate it.

## Sources

- [Alternative lending startups in Japan (Tracxn)](https://tracxn.com/d/explore/alternative-lending-startups-in-japan/__RpbITwnFhX7vmsyCXWmV0lJsCUhicLYtNSnNuATU_uQ/companies)
- [金融庁: 金融機関の内部監査高度化に関する懇談会 報告書 (2025)](https://www.fsa.go.jp/singi/naibukansa/siryou/20250620/houkokusho.pdf)
- [日本少額短期保険協会: 内部監査高度化に向けた認識と取組状況](https://www.fsa.go.jp/singi/naibukansa/siryou/20250319/03_shotan.pdf)
- [K&L Gates: New Japanese securitization risk retention rule](https://www.klgates.com/New-Japanese-Securitization-Risk-Retention-Rule-and-Its-Impact-on-CLO-Investors-in-Japan-05-22-2019)
- [Clifford Chance: Securitised origination warehouse financing](https://www.cliffordchance.com/content/dam/cliffordchance/briefings/2016/11/securitised-origination-warehouse-financing-a-flexible-funding-tool.pdf)
- [BoJ FSR Annex on generative AI](https://www.boj.or.jp/en/research/brp/fsr/fsrb260824.htm)
