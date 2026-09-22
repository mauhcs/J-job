---
id: org-jpx-data
type: org
space: data
name: JPX (J-Quants / JPX Data Cloud)
name_ja: 日本取引所グループ
role: seller
country: JP
industry: [asset-mgmt, securities]
status: researching
priority: 2
confidence: high
tags: [altdata, japan, exchange, infrastructure]
rel: [stream-data-market, note-altdata-japan, org-nowcast]
links:
  - label: J-Quants API
    url: https://www.jpx.co.jp/markets/other-data-services/j-quants-api/index.html
  - label: J-Quants Pro (corporate data delivery)
    url: https://www.jpx.co.jp/corporate/news/news-releases/6020/20240215-01.html
  - label: JPxData Portal — data catalogue
    url: https://www.jpx.co.jp/markets/data-catalog/index.html
updated: 2026-09-22
---

The exchange operator is itself a data seller, through JPX Research: **J-Quants** (retail
API), **J-Quants Pro** (corporate delivery by API, CSV and **Snowflake**), **J-Quants
DataCube** (purchase rather than subscription), and the **JPxData Portal**, a catalogue
spanning JPX group companies *and partner companies*.

Two things follow. **The plumbing exists** — Snowflake delivery means Japanese market data is
already distributed the way global funds expect to consume it, removing a technical objection.
And the partner-company catalogue is **a published list of firms already selling data into
Japanese finance**, which is a target list worth harvesting into the pool.

J-Quants is also the cheapest credible source of Japanese market data for building the
backtesting infrastructure the offer depends on.
