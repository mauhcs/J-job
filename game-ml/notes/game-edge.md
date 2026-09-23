---
id: note-game-edge
type: note
name: Strengths — what actually transfers, and what does not
status: researching
priority: 1
confidence: med
tags: [game, positioning, strengths, honesty]
rel: [note-game-usecases, note-game-regulation, note-game-risks, note-game-competitors, stream-game-offer]
updated: 2026-09-23
---

Written against the pattern from the other two projects, where "edges" turned out to be
hypotheses. Marked accordingly.

## Transfers well, and is genuinely scarce

**Adversarial detection.** HFT and trading surveillance is the discipline of spotting an
opponent who is deliberately hiding inside normal-looking activity, in sequence data, with
asymmetric error costs. Cheat, bot and RMT detection is the same discipline. The Japanese
material notes cheaters now embed AI to **mimic the rhythm of real players** — an arms race
against an adapting adversary, which is exactly what market manipulation detection is. Almost
nobody selling ML to game studios has done this; almost everyone selling it to banks has.

**Verification of stochastic claims.** `note-game-regulation`. The gacha disclosure regime is
model validation with different vocabulary, and the `model-validation` project's entire
methodology transfers.

**Estimation discipline under censoring and selection.** Churn and LTV are survival problems,
and the published failure modes are survivorship bias and wrong cohort windows. A risk
modeller's instincts are the differentiator, not the algorithm choice.

**Virtual economies.** A gacha game runs a closed economy with faucets, sinks, inflation and a
grey secondary market. It is macro plus microstructure with perfect observability. Very few ML
consultants think in those terms; it is a quant's native language.

## Transfers weakly

Computer vision, generative models, LLM application work. Competent but unremarkable, and
this is where every competitor and every in-house team is already strong.

## Does not transfer at all, and this is the binding one

**No game industry track record.** No shipped title, no studio reference, no CEDEC talk, no
understanding of how a Japanese studio is organised or how a live-ops team actually works
week to week. Everything above is *why the skills should work*, not evidence that they have.

The other two projects died on precisely this. It should be assumed to be the deciding factor
here too until something disproves it.

## The one asset that is not a hypothesis

The **academic affiliation**, and it matters more here than it did elsewhere — because this
industry demonstrably buys university research. Square Enix partnered with the University of
Tokyo's Matsuo-Iwasawa lab for QA automation; the University of Tokyo runs a game AI research
group. **A Japanese game company accepting a university collaboration is a documented,
repeated behaviour**, which is more than could be said for any buyer in the other projects.

That suggests the entry is a **research collaboration or a CEDEC talk**, not a consulting
pitch — which is the same conclusion `note-research-as-product` reached in the other project,
arriving here with better evidence behind it.
