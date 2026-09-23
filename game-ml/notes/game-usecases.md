---
id: note-game-usecases
type: note
name: Use cases — mapped against what a quant can actually do
status: researching
priority: 1
confidence: med
tags: [game, usecases, ml, positioning]
rel: [stream-game-offer, note-game-edge, note-game-adoption, note-game-regulation, org-square-enix]
links:
  - label: CEDEC 2026 — game QA with video and generative AI
    url: https://cedec.cesa.or.jp/2026/timetable/detail/s6985e6f038961/
  - label: CEDEC 2026 — mathematical optimisation and ML for multi-player imperfect-information game AI
    url: https://cedec.cesa.or.jp/2026/timetable/detail/s698912371e49f/
  - label: AI活用事例 — NPC生成・自動デバッグ・不正検知
    url: https://ai-revolution.co.jp/media/ai-in-gaming/
  - label: AntiCheatPT — transformer-based cheat detection (arXiv)
    url: https://arxiv.org/pdf/2508.06348
updated: 2026-09-23
---

The industry's own reading is that the areas where AI is **most mature in production** are
**QA automation, asset draft generation, customer-support automation and fraud/cheat
detection**. Sorting the full landscape by whether an outside quant has anything to add:

## Strong fit — the adversarial and quantitative corner

| use case | what it really is | why the background transfers |
|---|---|---|
| **Cheat / bot / RMT detection** | Adversarial sequence anomaly detection against an opponent who adapts | This is **market surveillance**. Spoofing, layering and wash-trade detection are the same problem class, and the false-positive economics are identical — banning a paying player wrongly costs more than missing a cheat |
| **Gacha probability & expected-value verification** | Verifying a regulated quantitative claim | See `note-game-regulation`. Closest thing to model validation in a new industry |
| **Virtual economy modelling** | Currency sinks and faucets, inflation, secondary markets | Market microstructure and monetary dynamics, applied to a closed economy with full observability |
| **Churn and LTV** | Survival analysis with censoring and cohort bias | The literature explicitly warns about **survivorship bias in training data** and measuring the wrong cohort — a risk-modelling reflex, and a common failure for generalist ML teams |
| **Matchmaking and rating** | Bayesian skill inference and balanced-pairing optimisation | Systems weigh 50+ variables to target ~50% win probability. Elo/TrueSkill are inference problems |
| **Real-time inference at scale** | Low-latency serving | HFT is the most latency-critical production ML that exists |

## Weak fit — crowded, and the incumbents are better placed

Image and asset generation, story and dialogue generation, coding assistance, NPC behaviour
authoring, voice synthesis, upscaling. All generative, all where the 85.8% adoption already
sits, all better served by studios' own teams or by vendors with deep CV/NLP benches.

## Genuinely uncertain

**QA and debugging automation** is the hottest area — Square Enix is targeting **70% automation
of QA and debug work by end of 2027** through joint research with the University of Tokyo's
Matsuo-Iwasawa lab, and CEDEC 2026 had sessions on video-plus-generative-AI QA. Video
recognition for bug detection is a real, live problem.

But it is a **vision and LLM problem**, not a quantitative one, and the largest publisher in
Japan has already partnered with the country's most prominent AI lab to solve it. Entering
there means competing with that. The exception worth exploring: the *statistical* side of QA —
test coverage, defect prediction, deciding where to spend limited test capacity — which is an
estimation problem rather than a perception one.

## The synthesis

Lead with **cheat/RMT detection and gacha verification**. Both are adversarial or regulated,
both punish being wrong in ways a studio feels immediately, and both are closer to financial
surveillance than to anything a generative-AI vendor sells.
