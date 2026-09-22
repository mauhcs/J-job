---
id: stream-advisor
type: stream
name: 顧問 — the door-opener
status: researching
priority: 1
confidence: med
tags: [advisor, network, japan, komon]
rel: [stream-market, person-archetype-ex-regulator, person-archetype-ex-cro, person-archetype-academic-bridge,
      person-academic-advisor-au, org-komon-bank, org-komon-meikan, org-visasq, note-komon-market-mechanics]
updated: 2026-09-22
---

## Question

Who is the senior **Japanese business** figure whose name on the masthead makes a megabank
or a regional bank take a first meeting — and how do we reach them without a cold approach?

## Why this stream exists

In Japan, independent verification is a trust product before it is a technical product.
A foreign principal with strong quant credentials but no domestic track record does not
clear procurement on merit alone. The 顧問 is not decoration: they are the mechanism by
which the buyer's risk of hiring an unknown is transferred to someone they already trust.

## Structure

- **Profile first, names second.** Three archetypes are carded (`person-archetype-*`).
  Decide which archetype the vehicle needs before collecting names.
- **Channels** — the routes by which an introduction can actually happen: TUJ's board and
  alumni, IPOR Labs' network, JAFEE membership, CFA Society Japan, FINOLAB, the Tokyo
  and Osaka foreign-financial-firm support desks.
- **Approach design** — what we offer the 顧問. Equity? Retainer? Co-authorship on a
  paper? The publishing stream is the cheapest and most natural pretext for a first
  contact, and that is deliberate.

## Current state (updated 2026-09-22)

**The academic leg is already secured** — a strong advisor relationship is in place, based
in Australia (`person-academic-advisor-au`). That closes the research and co-authorship
need and removes the reason the academic archetype was sequenced first. The remaining gap
is specifically a Japanese *business* contact, so `person-archetype-ex-cro` is now the
stream's target.

**Japan has a commoditised market for exactly this.** 顧問 matching services run pools in
the tens of thousands — 顧問名鑑 43,000+, HiPro Biz 39,302, プロシェアリング 33,999,
顧問バンク 10,000 — split between エージェント型 (brief a consultant, they assign) and
プラットフォーム型 (search yourself). Market rate is roughly **¥200,000–350,000/month**.
See `note-komon-market-mechanics` for the full structure, prices and caveats.

Two things temper it. These pools are **generalist** — none advertises financial-sector
ex-executives as a speciality, though 顧問名鑑's registrant base is described as including
megabank and securities alumni. And a 業務委託 contract needs a contracting entity on our
side, which the vehicle question has not yet settled.

## Sequencing now

1. **Free reconnaissance first** (`task-komon-platform-recon`). 顧問バンク is self-serve
   with a ¥0 trial. Look at the pool before paying anyone, and find out whether
   ex-risk-officer profiles exist in it at all.
2. **Invert the research dependency** (`task-visasq-expert-registration`). Register as a
   VisasQ expert and get paid to have the conversations that would otherwise require an
   introduction. This is the highest-leverage item in the stream.
3. **Design the offer before the approach** (`task-komon-comp-structure`). At ¥300k/month
   market rate, the structure — success fee, equity, 社外取締役 seat — matters more than
   the shortlist.

## Open questions

- Does Japan's 顧問 pool actually contain financial-risk executives, or only generalist
  corporate officers? Recon answers this.
- Which archetype does a Japanese bank's procurement respond to — ex-regulator or ex-CRO?
- Is a 社外取締役 seat a materially stronger signal than 顧問, and worth incorporating for?
