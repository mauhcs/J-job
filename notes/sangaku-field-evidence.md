---
id: note-sangaku-field-evidence
type: note
name: Does Japanese finance commission academic research? First pass, with the method's limits
status: researching
priority: 1
confidence: med
tags: [research, measurement, sangaku, evidence]
rel: [note-research-as-product, task-count-sangaku-prs, stream-publishing, stream-market, org-tuj, task-tuj-sangaku-capability]
links:
  - label: MEXT 令和5年度 産学連携等実施状況 (summary PDF)
    url: https://www.mext.go.jp/content/20251226-mxt_sanchi02-000040306_1-01-4.pdf
  - label: 一橋大学 金融戦略・経営財務プログラム — 寄付講座・寄附講義
    url: https://www.fs.hub.hit-u.ac.jp/education/endowed/
  - label: アセットマネジメントOne 寄附講義 at Hitotsubashi under a JFSA agreement
    url: https://prtimes.jp/main/html/rd/p/000000129.000138924.html
  - label: 三菱UFJ信託銀行 joint research report with Meiji and Seijo faculty
    url: https://prtimes.jp/main/html/rd/p/000000331.000036656.html
updated: 2026-09-22
---

## What the method can and cannot do — read this first

**PR TIMES keyword counts are unusable.** Searching 共同研究 銀行 returns "3,178件" and
産学連携 金融 returns "1,699件", but the search is loose full-text: inspecting the top 40 of
each showed the overwhelming majority were unrelated — startup events, carbon footprint
seminars, book launches. **Those totals must not be quoted as a measure of anything.**

**MEXT does not break 産学連携 down by academic field.** The FY2023 summary was downloaded
and searched directly: **zero occurrences** of 分野, 社会科学, 人文, 工学 or 医歯薬. The
survey reports by university type, contract size and region — not by discipline. So no
official field breakdown exists to compare against.

What follows is therefore a **purposive sample of 16 observations** found by targeted search,
recorded in `intake/sangaku-finance-prs.tsv`. It establishes **existence and pattern**. It is
not a count and gives no base rate. Treat every share below as illustrative.

## The national numbers, verified from MEXT's own summary (FY2023 / 令和5年度)

| | |
|---|---|
| All research funding into universities | **¥472.0bn** (+¥32.5bn, +7.4%) |
| From private companies (joint + commissioned + trials + IP) | **¥148.3bn** (+¥9.7bn, +7.0%) |
| 共同研究 (joint research) alone | **¥102.8bn** (+¥5.1bn, +5.2%) |
| Joint research contracts | **31,186** (+886, +2.9%) |
| Average per contract | **¥3,296k** (+¥71k, +2.2%) |
| Contracts of ¥10m or more | **¥59.5bn — 57.9% of all joint research value** |

Five-year per-contract trend (¥k): 2,721 → 2,941 → 3,012 → 3,226 → 3,296.
By sector: national universities 21,913 contracts / ¥82.4bn; public 2,178 / ¥4.0bn;
private 7,095 / ¥16.4bn.

**A derivation, clearly labelled as mine.** If the ¥10m+ band is ~4% of contracts (from an
older MEXT survey slide — confirm against a current year), that is ~1,247 contracts sharing
¥59.5bn, averaging ~¥47.7m. The remaining ~29,900 contracts then share ~¥43.3bn, averaging
**~¥1.4m each**. So the mean of ¥3.3m is pulled up by a small number of large contracts, and
**the typical contract is nearer ¥1.4m** — squarely marketing-budget scale, which is the
point of `note-research-as-product`.

## What the sample shows

**Finance does commission academic work, and it skews to the social sciences.** This
contradicts the earlier worry that 産学連携 is all engineering and medicine — that may hold
for the national aggregate, but not for the finance sector's own behaviour. Across 16
observations the faculties involved were management (4), finance (3), economics (2),
data science (2), commerce (2), and one each of law, medicine, behavioural finance and
financial engineering.

**Quant finance sits inside exactly those faculties**, and there is a dedicated institutional
home: 一橋大学's 金融戦略・経営財務プログラム runs a standing 寄付講座・寄附講義 programme.

## The five observations that matter most

1. **三菱UFJ信託銀行 × Meiji 商学部 and Seijo 法学部** — joint research on corporate–
   institutional investor dialogue, **published as a report and announced as a PR**. This is
   the proposition in its purest observed form: a bank pays social-science academics, and the
   output is a credibility artefact.
2. **三菱UFJ信託銀行 × Hokkaido University** — an 寄付講座 in the **economics faculty** plus
   joint research on transition technology evaluation. Endowed lecture and joint research used
   together.
3. **アセットマネジメントOne at 一橋大学** — 寄附講義 two years running, **under a
   JFSA–Hitotsubashi partnership agreement**. The regulator is party to the frame, which makes
   this the most interesting structure found: 産官学 rather than 産学.
4. **プルデンシャル生命** — 寄付講座（営業学）across **9+ universities since FY2015**, two
   more added in 2025. Sustained programme, not a one-off.
5. **Hokan Group × Drucker School (Prof Jeremy Hunter)** — an insurtech launching its own
   research institute with a named professor. Hokan is also a Fintech協会 member, so this is
   the closest analogue to the proposition at a company of reachable size.

Also notable: the 生命保険協会 and 日本FP協会 run 寄附講座 programmes at association level —
i.e. **an industry body can be the buyer**, which is a different and possibly easier sale
than one company.

## What this does and does not settle

**Settles:** the instrument exists in Japanese finance, is used repeatedly by the same firms,
runs through social-science faculties, and is announced publicly — which is the whole point,
since the announcement is the product.

**Does not settle:**
- **Base rate.** 16 purposive observations. Whether this is 20 firms a year or 500 is unknown.
- **Skew.** Almost every named buyer is a large institution — a trust bank, a major insurer,
  an asset manager. The reachable small and mid-size firms are the thin part of the sample
  (Hokan, Facilo, データビズラボ, ZENKIGEN), and those are mostly *management* research, not
  finance.
- **Price.** Not one observation disclosed a contract value.
- **Whether TUJ can play.** Still the blocker (`task-tuj-sangaku-capability`).

## The uncomfortable reading

If the buyers are overwhelmingly megabanks, major insurers and asset managers, then
research-as-product has **the same access problem as validation** — it just reaches them
through a different door, and a cheaper one. That would not be fatal, since a ¥1–3m
marketing-budget decision is far easier to reach than a risk-function procurement, and the
JFSA–Hitotsubashi structure shows the regulator legitimises the channel. But it does mean the
"small companies will buy research" assumption is **not yet supported by the evidence**, and
it should not be built on the way the SME wedge was.

`task-count-sangaku-prs` remains open: this pass found the pattern, not the base rate.
