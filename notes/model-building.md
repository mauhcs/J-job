---
id: note-model-building
type: note
name: Building models instead of validating them — easier to sell, lower ceiling
status: researching
priority: 1
confidence: med
tags: [strategy, positioning, alternative, delivery]
rel: [stream-positioning, note-sales-routes, note-research-as-product, note-deliverable-spec, org-jp-ai-credit-vendors, org-garage-bank, note-unit-economics]
updated: 2026-09-22
---

The alternative proposition: help companies **build** their models rather than audit them.

## What changes in your favour

- **The client already knows they need it.** Validation requires convincing someone that an
  invisible risk is worth paying to examine. Building answers a need they can already name —
  and `note-correction-invented-numbers` records that the demand premise behind validation was
  never verified, while demand for model-building obviously exists.
- **No independence requirement.** Validation needs the validator to be outside the
  institution, which raises the domestic-entity-of-record problem
  (`task-jp-foreign-validator-legality`). Building has no such constraint. A foreign expert
  building your model is unremarkable.
- **No regulatory gatekeeping.** Nobody needs a supervisor's blessing to hire a modeller.
- **Scoping is easier.** The client hands you the problem. In validation, the first and
  largest cost is understanding a model someone else built, badly documented
  (`note-deliverable-spec`).

## What changes against you

- **The price ceiling is set by the alternative, and the alternative is cheap.** The buyer's
  comparison is not "what is independence worth" but "what would a contract data scientist
  cost" — and in Japan that comparison drags toward the contractor rate, the bottom of the
  ten-fold gap in `note-unit-economics`.
- **You compete with products, not just people.** `org-jp-ai-credit-vendors` — Money Forward X,
  Quants, SXI — sell working credit models as a product. A buyer choosing between bespoke
  development and a deployed vendor engine will often take the engine.
- **It burns the independence asset for that client.** You cannot validate what you built. Each
  build converts a potential validation client into one you are disqualified from.
- **It does not compound.** Bespoke builds are bespoke. The repeatable protocol that makes a
  second validation half the work of the first has no equivalent here.

## Where an independent actually wins

Not in commodity credit scorecards — vendors and hires own that. The defensible ground is
**model classes where no product exists and no hire is available**:

- Residual-value and recovery models (`org-garage-bank` — no standard playbook exists).
- Market microstructure, execution and latency-sensitive pricing — the HFT background, and
  genuinely scarce in Japan.
- On-chain rate and oracle models — scarce anywhere.
- Insurance pricing for products with no loss history — embedded, on-demand, behaviour-based.

In each, the buyer cannot compare you to a vendor because there is no vendor, and cannot hire
the skill because it is not in the local market.

## The likely synthesis

Build and validate are not a choice between two businesses. Ordered properly:

1. **Paid research** (`note-research-as-product`) — a marketing-budget-sized ticket, a
   non-procurement buyer, and it manufactures the publication record.
2. **Model building** in the scarce classes above — easy to sell, funds the practice, builds
   the reference cases and the domain depth.
3. **Validation** — the highest-status and highest-rate work, but it requires the credential
   and the independence story that the first two produce. It is the destination, not the
   entry point.

The original plan attempted step 3 first, with neither the credential nor the demand evidence
in place.

## Open questions

- What does a Japanese fintech pay a contract quant or data scientist? That is the price
  ceiling and it is not yet known.
- Does building for one client genuinely disqualify validation work for others, or only for
  that client? Almost certainly only that client — but worth confirming, since the Big 4 build
  and validate for different clients routinely.
