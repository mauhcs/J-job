---
id: note-job-verification-standard
type: note
name: What counts as a job here — and what I got wrong
status: confirmed
priority: 1
confidence: high
tags: [jobs, method, correction, standard]
rel: [stream-job-search, job-gauntlet-credit-risk-researcher, job-imc-quant-researcher-hft-hk, note-job-market-size]
updated: 2026-09-23
---

## The correction

The first pass produced 27 "roles" scraped from aggregator listing pages. Most were not
opportunities:

- **Nine had no employer** — "Via Gravitas", "Via NLS", "Via Hays", "Via BAH Partners". Those
  are recruiters advertising their pipeline, not companies hiring.
- **Not one job description had been opened.** Every card was a title plus a line of scrape
  text, so nothing could be said about requirements, eligibility or level.
- **Almost none had an application link** — several pointed at a job board's homepage.
- **Staleness was unknown**; at least one had been posted two months earlier.
- **Fit ratings were invented** against a profile assembled from conversation fragments.
- **Proprietary trading firms were never searched at all** — the employers closest to an HFT
  background. That omission alone cost the best role in the search.

Fourteen cards were deleted rather than left standing.

## The standard now

A job card requires:

1. **A named employer.** No "via recruiter" placeholders.
2. **A direct link** — the posting or the employer's own careers page.
3. **A `verified` field**, one of:
   - `jd-read` — the full description was opened; requirements and compensation are quoted.
   - `listing-confirmed` — seen on the **employer's own site** or a board listing that names
     the employer, but the description has not been read.
4. **Location eligibility stated**, not assumed.
5. **The gap named**, not just the fit.

## Why it matters, in one example

`org-gauntlet` was rated a **strong fit** across two earlier passes on the strength of what the
firm does. Opening the posting showed **"Remote first — work from anywhere in the US & CAN"**
and a requirement for 3–6 years of *credit* risk — PD/LGD, ABS/CLO structuring, SPVs.

From Japan the role is closed without relocation, and the discipline is structured credit
rather than rates. Both facts were one click away and neither survived a scrape.

## What opening postings gained

**IMC Trading — Quantitative Researcher, HFT Commodity Futures, Hong Kong.** HFT quantitative
research, in Asia, at an established market maker. Found by going to IMC's own careers site.
No aggregator surfaced it.

**Polymarket** turned out to specify *mark price construction and funding rate design for
perpetual futures* — which is interest rate mechanism design, the IPOR skill set, at $250k–350k.
The title alone said none of that.
