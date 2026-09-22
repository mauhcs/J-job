---
id: org-crezit
name: Crezit Holdings
name_ja: Crezit Holdings株式会社
type: org
role: buyer
scope: company
country: JP
industry: [banking]
size: sme
status: qualified
source: manual
first_seen: 2026-09-22
site: https://crezit-holdings.com/
confidence: med
priority: 1
pitch: Credit-as-a-Service — their underwriting model is embedded in other companies' products, so its credibility is their product.
tags: [target, fintech, credit-model, vendor, caas]
rel: [org-jp-alt-lenders, org-jp-ai-credit-vendors, note-sme-wedge, org-credit-engine]
links:
  - label: Crezit Holdings (corporate site — unverified, see note)
    url: https://crezit-holdings.com/
  - label: CaaS 与信プラットフォーム「ZEN」 teaser announcement (PR TIMES)
    url: https://prtimes.jp/main/html/rd/p/000000025.000043526.html
  - label: NIKKEI COMPASS company record
    url: https://www.nikkei.com/compass/company/kCWs4fdgX3o2jNuXX8jiZC
updated: 2026-09-22
---

**Recarded 2026-09-22.** This was previously carded as "Crezit", a consumer credit startup,
pointing at the product domain. The operating company is **Crezit Holdings株式会社**, founded
10 July 2020 (subsidiary Crezit株式会社 founded 8 March 2019), Roppongi, Minato-ku, CEO
矢部寿明 — and the business is not consumer lending.

**It is a credit infrastructure platform.** Crezit builds **CaaS (Credit as a Service)**, a
SaaS credit platform providing underwriting capability to any service wanting to enter
consumer credit, with a product line branded ZEN.

**That changes which thesis it belongs to.** This is not a lender with a model; it is a
**model sold as infrastructure to other companies' products** — the same structure as
`org-jp-ai-credit-vendors` and `org-credit-engine`, and the strongest shape in
`note-sme-wedge`. Every service embedding Crezit's underwriting inherits its model risk, and
any regulated institution in that chain has third-party model obligations that run back to
Crezit. An independent validation is a sales asset they can put in front of every prospect.

Consumer credit in Japan is 貸金業-regulated, so the licensing perimeter is real.

## Unverified

`crezit-holdings.com` did not resolve from the research environment — no A record returned.
The domain is listed as theirs in search results and the NIKKEI COMPASS record exists, but
**confirm the corporate site is live before using it.** It may have moved, or DNS may simply
be blocked from here.
