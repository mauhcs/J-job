---
id: note-job-staleness
type: note
name: Staleness — postings die, and the best one already had
status: confirmed
priority: 1
confidence: high
tags: [jobs, method, staleness, correction]
rel: [note-job-verification-standard, org-morgan-mckinley, stream-job-search]
updated: 2026-09-23
---

The Model Validation Quant Analyst role in Tokyo was rated the most on-profile role in the
search across two passes and made the top task in this project.

Opening it returns: **"This job opportunity is no longer available."**

It was carded from an aggregator listing, rated on its title, and built into a plan — without
anyone checking whether it was open. It is the clearest single illustration of why
`note-job-verification-standard` exists.

## What follows

**Check liveness before rating, not after.** A closed posting is worse than no posting: it
produces a confident plan aimed at nothing.

**Treat every card as decaying.** Each carries a `seen` date for that reason. Anything older
than a few weeks should be re-opened before it is acted on, and `listing-confirmed` cards that
have never been opened should be assumed at risk.

**A dead posting still carries one piece of information** — that the employer was building the
function. That is worth a recruiter conversation even when the role has gone, which is why
`task-job-call-recruiters` survived the deletion of the role that prompted it.
