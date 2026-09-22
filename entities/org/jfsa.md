---
id: org-jfsa
type: org
name: Financial Services Agency (JFSA)
name_ja: 金融庁
role: regulator
country: JP
industry: [regulator, banking, securities, insurance]
status: confirmed
priority: 1
confidence: high
tags: [mrm, regulation, driver, ai]
rel: [stream-market, note-jp-regulatory-driver, org-boj]
links:
  - label: Principles for Model Risk Management (English announcement, Nov 2021)
    url: https://www.fsa.go.jp/en/news/2021/2021112en.html
  - label: モデル・リスク管理に関する原則 (JP, 令和3年11月12日)
    url: https://www.fsa.go.jp/common/law/ginkou/pdf_02.pdf
  - label: AI Discussion Paper v1.0 (March 2025, EN)
    url: https://www.fsa.go.jp/en/news/2025/20250304/aidp_en.pdf
  - label: AI Discussion Paper v1.1 (March 2026)
    url: https://www.fsa.go.jp/en/news/2026/20260303/aidp.html
updated: 2026-09-22
---

The single most important entity in the market stream: JFSA creates the demand.

**Principles for Model Risk Management**, published 12 November 2021 after a consultation
that drew 87 comments from 61 respondents, is Japan's answer to the US Federal Reserve's
SR 11-7. It covers credit and market risk models, valuation models and stress testing,
and — critically for us — sets an expectation of **validation independent of model
development**. It applies in the first instance to the largest institutions, which is why
the megabanks built internal MRM teams; the pressure has since diffused outward to
institutions with no such team.

The **AI Discussion Paper** line (v1.0 March 2025, v1.1 March 2026) is the second wave.
It extends the same governance logic to generative and AI-driven models, where the
existing validation playbook does not straightforwardly apply — the gap our publishing
stream should aim at.

## Why it matters commercially

Regulatory expectation is what converts "nice to have" into a budget line. Every buyer
card in this repo should name the specific JFSA expectation that puts them under
pressure. Where we cannot name one, the buyer is speculative.

## Sources

- [FSA: Principles for Model Risk Management, English announcement](https://www.fsa.go.jp/en/news/2021/2021112en.html)
- [金融庁: モデル・リスク管理に関する原則 (PDF)](https://www.fsa.go.jp/common/law/ginkou/pdf_02.pdf)
- [FSA AI Discussion Paper v1.1 (March 2026)](https://www.fsa.go.jp/en/news/2026/20260303/aidp.html)
