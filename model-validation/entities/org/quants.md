---
id: org-quants
name: Quants株式会社
name_ja: Quants株式会社
type: org
role: buyer
scope: company
country: JP
status: qualified
source: manual
first_seen: 2026-09-22
site: https://www.quants-grp.co.jp/
confidence: med
size: sme
industry: [banking]
priority: 2
pitch: Scores borrowers with no published financials — a model built precisely where validation data is thinnest.
tags: [target, ai, credit-model, vendor]
rel: [org-jp-ai-credit-vendors, note-ai-validation-gap]
links:
  - label: Quants — 二十一式人工知能付自動与信審査回路
    url: https://www.quants-grp.co.jp/fimple-credit/
  - label: Quants (corporate)
    url: https://www.quants-grp.co.jp/
updated: 2026-09-22
---

AI **qualitative** credit scoring for receivables delay and default risk, explicitly aimed at
ventures, new firms and individuals **with no published financial statements**.

**The technical reason this is a good target.** A model that scores counterparties with no
financials is, by construction, trained on sparse and proxy data — the hardest possible
setting to demonstrate that a model generalises, and exactly where JFSA's AI guidance on
explainability bites. If they sell into regulated lenders, their clients will eventually ask
how they know it works. It is a genuinely interesting validation problem as well as a sale.
