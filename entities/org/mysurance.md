---
id: org-mysurance
name: Mysurance
name_ja: Mysurance株式会社
type: org
space: mrm
role: buyer
scope: company
country: JP
status: qualified
source: shotan-kyokai
first_seen: 2026-09-22
site: https://www.mysurance.co.jp/
confidence: med
size: sme
industry: [insurance]
priority: 2
pitch: Sompo's digital insurer — embedded, on-demand products whose pricing has almost no loss history.
tags: [target, insurtech, micro-insurance, pricing-model]
rel: [org-shogaku-tanki-hoken, note-sme-wedge]
links:
  - label: Mysurance
    url: https://www.mysurance.co.jp/
  - label: 日本少額短期保険協会 member list
    url: https://www.shougakutanki.jp/general/about/membership.html
updated: 2026-09-22
---

Sompo Holdings' digital insurance company, regular member of the association. Builds embedded
and on-demand cover — smartphone, travel, event-linked products sold at the point of another
transaction.

Embedded insurance prices short-duration, high-frequency, low-severity risks with very little
history and strong selection effects from *where* the product is embedded. That is a
modelling problem with real adverse-selection structure, and it is nothing like the life
actuarial work the parent group is set up for.

## Kept despite the captive filter

The bulk captive retirement removed Sompo, Tokio Marine, SBI, Aflac and similar group
subsidiaries on the reasoning that the FSA's own remedy — lean on the parent group — is
available to them. Mysurance is a Sompo subsidiary and would have been caught by that rule.

It is kept deliberately. The parent's actuarial bench is built for conventional general
insurance; embedded, on-demand, transaction-linked cover with almost no loss history and
strong selection effects from the embedding channel is not work that bench does. The group
provides capital and governance, not a validation capability for this product class.

That distinction — group *exists* versus group *covers this model* — is the test to apply
to every captive before accepting the retirement. See `task-recheck-retired-captives`.
