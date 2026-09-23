---
id: note-game-regulation
type: note
name: Gacha disclosure — a regulated quantitative claim nobody independently checks
status: researching
priority: 1
confidence: med
tags: [game, regulation, gacha, opportunity, differentiation]
rel: [note-game-usecases, note-game-edge, stream-game-offer, org-joga, org-cesa, task-game-gacha-verification]
links:
  - label: JOGA online game safety declaration (PDF)
    url: https://japanonlinegame.org/wp-content/uploads/2017/06/JOGA120801.pdf
  - label: CEDEC 2024 — 景品表示法 lessons from past enforcement (4Gamer report)
    url: https://www.4gamer.net/games/999/G999905/20240827021/
  - label: 消費者庁 — オンラインゲームの動向整理 (PDF)
    url: https://www.caa.go.jp/policies/policy/consumer_policy/caution/internet/assets/consumer_policy_cms106_220630_08.pdf
  - label: MCF・CESA・JOGA blockchain game guidelines (gamebiz)
    url: https://gamebiz.jp/news/298708
updated: 2026-09-23
---

**The most interesting finding in this project, and the one nobody else is positioned for.**

## The rule

Industry self-regulation through **JOGA** and **CESA** requires disclosure of **drop rates for
every item a gacha can produce**. Operators choose among several compliance routes, including
keeping the **expected spend to obtain a rare item within ¥50,000**, or publishing upper and
lower bounds on appearance probabilities.

Behind that sits the **景品表示法 (Act against Unjustifiable Premiums and Misleading
Representations)**, enforced by the **消費者庁**, which has issued administrative guidance
against gacha mechanics — most famously complete-gacha style designs where collecting items
unlocks an advantageous exchange. CEDEC 2024 ran a session drawing lessons from past
enforcement, so the industry treats this as a live compliance risk, not a theoretical one.

## Why this is a model validation problem wearing different clothes

A published drop rate is a **quantitative claim about a stochastic system, made to consumers,
enforceable by a regulator.** Verifying it means asking exactly the questions asked of a risk
model:

- Does the implemented sampler actually produce the disclosed distribution? Pity timers,
  ceilings, step-ups, duplicate-conversion and per-user state all distort the naive rate.
- Is the **expected value** calculation correct under the real mechanic, including the ¥50,000
  ceiling where that route is chosen?
- Do the disclosed bounds hold across the live population, not just in theory?
- Is there drift between the design document, the implementation and the disclosure?

That is verification of an implemented stochastic model against a stated specification. It is
the entire `model-validation` skillset, in an industry with more of these systems than finance
has, and — as far as this sweep found — **no independent verification practice at all**.

## Why a studio would buy it

Not enthusiasm for rigour. **Downside.** A 消費者庁 action over a misstated probability is a
reputational event in a consumer business, and the disclosure is public and checkable by
players, who do check and do publish their own counts. An independent verification is cheap
insurance against a discrepancy being found by a hostile audience first.

## Open questions, and they are large

- Has any studio ever been sanctioned specifically over a *wrong* probability, as opposed to
  the mechanic itself? If not, the risk may be perceived as theoretical.
- Do studios already verify internally, via QA or audit?
- Would a studio let an outsider inspect gacha implementation code? This is commercially
  sensitive, and the answer may simply be no — in which case the offer must be restructured
  around outputs (sampled logs) rather than code.
- Is there an existing auditor, law firm or QA vendor covering this?

**`task-game-gacha-verification` exists to answer these before any of it is believed.**
