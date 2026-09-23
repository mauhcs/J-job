---
id: task-altdata-01-build-harness
type: task
name: 1 — Build the harness, time-boxed to six weekends
status: idea
priority: 1
decides: Whether you can and want to do this work at all — at a cost of weekends, not a business.
owner: mau
due: 2026-11-30
confidence: high
tags: [altdata, build, foundation, sequence]
rel: [stream-data-offer, note-altdata-offer-design, note-altdata-action-plan, org-jpx-data]
links:
  - label: J-Quants API (Japanese market data)
    url: https://www.jpx.co.jp/markets/other-data-services/j-quants-api/index.html
updated: 2026-09-22
---

**Reframed 2026-09-23** (`note-do-i-have-an-edge`): this is no longer step one of a business.
It is a credential project with a hard limit — **six weekends, one artefact, then stop.** If it
runs past that, the work is too heavy to be worth doing on this basis and it gets abandoned
without regret.

Build the pipeline once, properly, against **free data** — J-Quants for Japanese prices and
fundamentals, plus any public alternative dataset. The point is not the finding; it is the
**harness**, which is reused on every paid engagement afterwards and is the only thing that
makes the second job cheaper than the first.

What it must do, in this order:

1. **Data integrity before signal.** Coverage, history length, latency, point-in-time
   correctness, revision history, survivorship. Most datasets die here, and saying so credibly
   is a large part of the value.
2. **Signal construction**, with the multiple-testing problem handled explicitly — deflated
   Sharpe or equivalent — not ignored.
3. **Orthogonalisation** against standard factors. A signal that is momentum in disguise is
   worth nothing to a desk that already runs momentum.
4. **Backtest with and without the dataset.** The incremental information ratio is the number
   the whole offer rests on.
5. **Risk and shock analysis.** Drawdown, regime conditioning, behaviour through a crisis and a
   liquidity event.
6. **Capacity and costs.** Turnover, transaction costs, the AUM at which the signal dies.

**Output: a template report**, with the sections fixed, so that a paid engagement is filling in
a known structure rather than inventing one under time pressure.

Budget it in weekends, not months. If it takes more than about six, the offer is too heavy to
sell at any plausible price.
