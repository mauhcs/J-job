---
id: task-recheck-retired-captives
type: task
name: Re-check the auto-retired captives against the right test
status: idea
priority: 3
owner: claude
due: 2026-12-31
confidence: med
tags: [intake, targeting, data-quality]
rel: [org-shogaku-tanki-hoken, org-mysurance, note-sme-wedge]
updated: 2026-09-22
---

31 micro-insurers were retired in bulk as captives — group subsidiaries of Tokio Marine,
SBI, Aflac, Chubb, Zurich, Rakuten, au, AEON, 積水, 東急, ヤマダ and similar. The reasoning
was that the FSA's own remedy for small institutions, leaning on a parent group's resources,
is available to them.

**That rule is a first-pass heuristic and it is too blunt.** The right test is not whether a
parent group exists but whether the parent's risk and actuarial function actually covers
*this subsidiary's model class*. `org-mysurance` was kept for exactly that reason: Sompo's
bench is built for conventional general insurance, not for embedded on-demand cover with no
loss history.

Re-check the retired set against that sharper test, particularly the insurtech-flavoured
subsidiaries of large groups. Un-retiring is just editing the card back to `candidate` — the
history stays in git either way, which is the point of retiring rather than deleting.
