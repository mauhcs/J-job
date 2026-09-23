---
id: note-game-risks
type: note
name: Risks — including the one that killed the last two projects
status: confirmed
priority: 1
confidence: high
tags: [game, risk, kill-criteria]
rel: [stream-game-offer, note-game-edge, note-game-competitors, note-game-adoption, note-game-business-model]
updated: 2026-09-23
---

Stated at the start this time, not after a full research pass.

## 1. No track record — the recurring one

Three projects, same constraint: acquiring clients in a market where there is no reference
and no appetite for business development. Nothing about game companies makes this easier;
Japanese studios are relationship-driven and conservative about who touches live systems.

**This is the deciding risk.** The only mitigations that have ever looked credible are
(a) somebody else owning the client relationship, and (b) publishing something that makes the
approach unnecessary. Both are in `note-game-business-model`.

## 2. The window may already be closing on the obvious work

Adoption went 51% → 85.8% in a year. Whatever is easy is being done. Arriving with generative
AI services in 2026 is arriving late, which is why the offer is deliberately elsewhere.

## 3. Access to the systems that matter

Cheat detection and gacha verification both require access to **live production data or
implementation code** — telemetry, ban decisions, sampler internals. These are commercially
sensitive and security-relevant. A studio may simply refuse an outsider, and the whole offer
then has to be restructured around whatever can be shared.

## 4. Language and organisational distance

Live-ops, QA and security teams at Japanese studios work in Japanese. This is deliverable-heavy
work requiring sustained contact with engineers, not a report handed over at the end.

## 5. The domestic vendors

`note-game-competitors`. Deep, funded, domestic, and in HEROZ's case already spanning game and
finance AI.

## 6. The regulatory idea may be a solution to a problem nobody feels

`note-game-regulation` is the most differentiated idea here, and it rests on an assumption that
studios feel exposed on probability disclosure. If enforcement has only ever targeted mechanics
rather than misstated rates, the perceived risk may be near zero. **Untested.**

## 7. Reputational asymmetry

Being the person who audits gacha odds could read as adversarial to the industry it sells to.
Worth thinking about how that is framed before it is built — the same tension as independent
model validation, in a more consumer-visible setting.

## Kill criteria, set in advance

Abandon if, after `task-game-survey-usecases` and `task-game-approach-vendors`:

- studios handle quantitative work entirely in-house and never outsource it; **or**
- domestic AI vendors are not asked for this kind of brief; **or**
- nobody will grant an outsider access to telemetry or sampler code.

Any one of those makes the project unsellable regardless of skill fit.
