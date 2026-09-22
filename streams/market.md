---
id: stream-market
type: stream
space: mrm
name: Market — who sells, who buys, at what price
status: researching
priority: 1
confidence: med
tags: [market, competitive-landscape]
rel: [stream-positioning, note-jp-regulatory-driver, note-competitive-landscape, note-sme-wedge,
      org-jp-alt-lenders, org-jp-ai-credit-vendors, org-shogaku-tanki-hoken, org-garage-bank]
updated: 2026-09-22
---

## Question

Who currently sells independent quantitative model validation in Japan / HK / East Asia,
who buys it, what does an engagement look like, and where is the gap a one-person-plus-
network boutique can actually fill?

## Structure

Three layers, researched separately:

1. **Demand drivers** — regulation is the forcing function. JFSA *Principles for Model
   Risk Management* (Nov 2021) for Japan, HKMA SPM modules for Hong Kong, MAS AI Risk
   Management Guidelines (final expected mid-2026) for Singapore. The 2025–26 AI wave
   adds a second driver on top of the Basel/FRTB/IFRS9 baseline.
2. **Supply** — Big 4 Japan practices, global strategy firms, domestic think-tank
   consultancies (NRI, ABeam, MURC, MHRI), and specialist/boutique validators.
3. **Buyers** — segmented by country × institution type. Megabanks have large internal
   MRM teams and buy *capacity and independence*; regional banks and insurers lack teams
   entirely and buy *the whole function*; funds and crypto venues buy *credibility*.

## Current state (updated 2026-09-22)

**Re-aimed down-market.** The first sweep targeted banks because that is where the
regulation is, which pointed the plan at the hardest buyers in the market. The corrected
view is in `note-sme-wedge`: work the tiers from the bottom, because at the startup and SME
tier the purchase is forced not by the supervisor but by **warehouse lenders, securitisation
investors, bank partners and VCs in diligence** — buyers who decide in weeks and whose
motivation is cost of capital rather than compliance.

Three segments now lead: Japanese alternative lenders (39 firms, 24 funded), AI credit-model
vendors selling into regulated institutions (whose clients' third-party model risk flows back
to them), and 少額短期保険業者 — licensed, supervised, and with 41% under ten employees, the
one small segment where the regulator *is* the driver.

The regulatory picture remains solid and sourced. The commercial picture — fee levels,
procurement route, whether a foreign principal can be validator of record — is still the
highest-value gap, and `task-garage-bank-conversation` is the fastest cheap test of it.

## Open questions

- What is a typical engagement worth at each tier, and is it procured as consulting, audit,
  or an outsourced function?
- Do Japanese buyers accept a non-Japanese principal as "independent validator" of record,
  or does independence have to be a domestic legal entity?
- **Has any funding counterparty actually asked a Japanese fintech lender for an independent
  model opinion?** If not, demand at the startup tier is latent rather than real.

## Parked 2026-09-22

Focus moved to the `data` space. This stream is kept intact, not deleted — the regulatory
research and the named target lists stay valid, and the sales-constraint findings carried over.
Nothing here is live work.
