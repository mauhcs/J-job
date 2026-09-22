---
id: task-count-sangaku-prs
type: task
name: Count industry-university research PRs in Japanese finance — the credibility-spend proxy
status: researching
priority: 3
owner: claude
due: 2026-10-31
confidence: high
tags: [research, measurement, falsification, sangaku]
rel: [note-research-as-product, note-sangaku-field-evidence, stream-market, stream-publishing, org-fintech-kyokai, org-jp-ai-credit-vendors]
updated: 2026-09-22
---

**The measurement the whole research-as-product idea rests on**, and it is cheap.

MEXT's statistics prove Japanese companies fund university research at ¥97.7bn a year across
tens of thousands of contracts — but most 産学連携 by volume is engineering and medical.
Whether *financial institutions and fintechs* commission academic research at any meaningful
rate is unestablished, and it is the difference between a market and a wish.

## First pass done 2026-09-22 — pattern found, base rate not

Results in `note-sangaku-field-evidence`; 16 observations in
`intake/sangaku-finance-prs.tsv`. Two method findings that constrain the rest of this task:

- **PR TIMES keyword totals are noise.** 共同研究 銀行 reports 3,178件 and 産学連携 金融
  reports 1,699件, but the top 40 of each was overwhelmingly unrelated. Do not quote them.
- **MEXT has no field breakdown at all** — the FY2023 summary contains zero occurrences of
  分野 or any discipline name. An official comparison does not exist; the sample is the only
  source of a field split.

## What a real count still needs

- Systematic retrieval rather than targeted search: PR TIMES topic/keyword pages
  (`prtimes.jp/topics/keywords/共同研究`, `/寄付講座`) paged through and filtered by
  industry, or company newsroom sweeps for a defined list of firms.
- A defined denominator — e.g. every Fintech協会 member and every 少額短期保険協会 member,
  checked for any research PR. That converts "how many exist" into "what share of reachable
  firms do this", which is the decision-relevant number.
- The counts by year, to show whether it is growing.

## Method

Press releases are the proxy, because a company that commissions research for credibility
will announce it — announcing it is the point.

1. Search PR TIMES (and company newsrooms) for announcements pairing a Japanese financial
   institution, insurer or fintech with a university or professor: 共同研究, 産学連携, 寄付講座,
   共同研究講座, 実証実験, 〜大学と, 〜教授と.
2. Cover the last three to five years. Record per hit: company, university, named academic,
   topic, date, stated purpose, and whether a paper or only a press release resulted.
3. Classify the intent — genuine R&D, regulatory credibility, product marketing, or recruiting.

## What the answer means

- **Many hits, small companies among them** → the market is real and reachable, and the hit
  list is also a target list and a list of academics already doing this (who are 顧問 and
  co-author candidates).
- **Few hits, all megabank-and-University-of-Tokyo** → it is a large-institution prestige
  ritual, not a reachable market, and the idea should be dropped rather than nursed.
- **Hits concentrated in AI and data science rather than finance theory** → the topic matters
  more than the affiliation, which changes what to propose.

Also record the *academics*: anyone who has done this repeatedly knows how the contracts are
structured, what they are worth, and how the companies approached them. One conversation with
such a person is worth more than the count itself.
