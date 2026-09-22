---
id: org-medical-ssi
type: org
name: メディカル少額短期保険
name_ja: メディカル少額短期保険（株）
role: buyer
scope: company
country: JP
industry: [insurance]
size: sme
status: candidate
confidence: low
source: shotan-kyokai
first_seen: 2026-09-22
site: http://medical-ssi.co.jp/
tags: [target, candidate, shotan-kyokai]
rel: []
links:
  - label: Corporate site
    url: http://medical-ssi.co.jp/
updated: 2026-09-22
---

Candidate, harvested from **日本少額短期保険協会 — 会員一覧** on 2026-09-22. Not yet reviewed.

To qualify this card, establish and write up:

- Is `site` the operating company, or did the source give a product page? Find the company.
- What model does the business actually depend on, and what does it decide?
- Is it licensed or supervised, and under which regime?
- Who would ask them for an independent opinion — a regulator, a funding counterparty, a
  bank or insurer partner, or an investor?
- Roughly what size, and can they pay?

Then set `size`, `priority` and a one-line `pitch`, replace this body, and move `status` to
`qualified`. If it does not fit, retire it with a reason rather than deleting it:

    python3 tools/retire.py org-medical-ssi "reason"
