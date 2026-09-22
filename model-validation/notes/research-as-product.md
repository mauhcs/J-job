---
id: note-research-as-product
type: note
name: Selling research — the market exists, is growing, and is sized like a marketing budget
status: researching
priority: 1
confidence: med
tags: [strategy, research, sangaku, revenue, marketing]
rel: [stream-positioning, stream-publishing, note-sales-routes, note-model-building, org-tuj, artifact-flagship-paper, task-count-sangaku-prs, task-tuj-sangaku-capability, note-sangaku-field-evidence]
updated: 2026-09-22
---

The question was whether companies pay for research, and whether university partnerships are
in effect bought credibility. **Japan publishes official statistics on exactly this, and the
answer is yes at scale.**

## The market, from MEXT's annual 産学連携 survey

Research funding flowing from private companies into Japanese universities:

Updated 2026-09-22 with FY2023 (令和5年度) figures read directly from MEXT's summary PDF.

| | amount | note |
|---|---|---|
| FY2023, all private-sector research income | **¥148.3bn** | joint + commissioned research, trials, IP; **+¥9.7bn (+7.0%) YoY** |
| FY2023, 共同研究 (joint research) alone | **¥102.8bn** | **+¥5.1bn (+5.2%) YoY**, across **31,186 contracts** |
| FY2023, contracts of ¥10m+ | **¥59.5bn** | **57.9% of all joint research value** |
| FY2014 → FY2023, joint research | ¥41.6bn / 19,070 contracts → ¥102.8bn / 31,186 | value up ~2.5x in nine years |

This is not a niche. It is a ¥100bn-a-year flow, growing at high single digits, with tens of
thousands of individual contracts.

## The contract size is the interesting part

**FY2023 average per joint-research contract: ¥3,296k**, rising steadily (¥k): 2,721 → 2,941
→ 3,012 → 3,226 → 3,296 over five years. The distribution (MEXT, older survey — confirm
against a current year) is heavily skewed small:

| contract value | share of contracts |
|---|---|
| under ¥1m | 48% |
| ¥1m – ¥3m | 37% |
| ¥3m – ¥5m | 7% |
| ¥5m – ¥10m | 4% |
| ¥10m and over | 4% |

**85% of Japanese industry-university joint research contracts are under ¥3m**, and because
57.9% of the total value sits in the ¥10m+ band, the mean of ¥3.3m overstates the typical
contract. Backing that band out suggests the **typical contract is nearer ¥1.4m** — see the
derivation in `note-sangaku-field-evidence`. MEXT and METI
treat this as a *problem* — overseas university collaborations commonly run ¥10m+ per contract,
and Japan's small ticket sizes are explicitly flagged in the 産学官連携ガイドライン as something
to fix. Large contracts (¥10m+) doubled in number between 2014 and 2018 and now represent more
than half of total value despite being a small share of the count.

**Read this from the seller's side rather than the policy side.** A ¥1–3m contract is not an
R&D procurement — it is small enough to come out of a marketing, communications or
business-development budget, and it does not go through the procurement gauntlet that killed
the validation sale. That is precisely the hypothesis: **companies buy research partly for
credibility, and credibility is a marketing line item.**

## The demand-side evidence

The Edelman 2025 B2B Thought Leadership Impact Report finds **73% of decision-makers say
thought leadership is a more trustworthy way to assess a company's capabilities than
traditional marketing materials**. Industry practice is explicit that sponsored research is
legitimate *provided the conclusion follows the evidence* — which is the constraint that makes
this compatible with an academic affiliation rather than corrosive to it.

## Why this fits better than validation

- **The buyer is different.** Marketing/comms or the CEO, not risk or procurement. Faster,
  less gated, and reachable without a 顧問.
- **The ticket matches the buyer.** ¥1–3m is a normal marketing spend; ¥3m for a validation
  report was not a normal risk spend for the same company.
- **It is the publishing stream, paid for.** One piece of work that is simultaneously revenue,
  the client's credibility asset, and your own publication record — instead of publishing
  being an unpaid third job.
- **No independence problem.** Research collaboration carries no conflict with later work for
  the same client, unlike building a model you might later be asked to validate.
- **It is the credential that unlocks everything else.** A publication record with named
  institutional partners is what the validation business needed and did not have.

## The heavier instruments, for later

- **共同研究講座 / 寄付講座** — a company funds a named research unit inside a university.
  Tokyo Science University (formerly Tokyo Tech) quotes **¥30m+ per year** for a 共同研究講座;
  smaller universities structure it as direct cost plus ~30% indirect. This is the
  fully-developed version of the same instinct and is years away, but it is the ceiling.

## The blockers, unresolved

1. **Can TUJ be the counterparty?** MEXT's statistics cover 大学等 in Japan. TUJ is a foreign
   university's Japan campus, and whether it can sign a 共同研究契約, whether it has an
   industry-liaison office and an indirect-cost policy, and what an adjunct may do under its
   own rules are all unknown. **This is the blocker for the whole idea** —
   `task-tuj-sangaku-capability`. If TUJ cannot, the fallback is contracting personally and
   using the affiliation only as a byline, which is weaker but not worthless.
2. **Does finance do this?** *Partly answered, 2026-09-22.* Yes — and through social-science
   faculties (commerce, law, economics, management), not engineering. 一橋大学 runs a standing
   finance 寄付講座 programme, and アセットマネジメントOne teaches there under a
   **JFSA–Hitotsubashi partnership agreement**. But every clearly identified buyer is a large
   institution, and **the assumption that small companies will buy research is not yet
   supported**. See `note-sangaku-field-evidence` — it found the pattern, not the base rate.
3. **Is ¥1–3m worth the days?** At that ticket, a contract must be weeks of work, not months,
   or it prices below the day rate in `note-unit-economics`.

## Sources

- [MEXT: 令和5年度 大学等における産学連携等実施状況について](https://www.mext.go.jp/a_menu/shinkou/sangaku/1413730_00004.html)
- [MEXT: 平成30年度 産学連携等実施状況](https://www.mext.go.jp/a_menu/shinkou/sangaku/1413730_00005.htm)
- [MEXT contract-size distribution (survey material)](https://www.mext.go.jp/b_menu/shingi/gijyutu/gijyutu2/090/shiryo/__icsFiles/afieldfile/2017/10/13/1397197_6_1.pdf)
- [文科省・経産省: 産学官連携による共同研究強化のためのガイドライン 追補版](https://www.mext.go.jp/content/20230329-mxt_sanchi02-000020147_01-2.pdf)
- [経団連・経産省・文科省: 大学ファクトブック2025](https://www.meti.go.jp/policy/innovation_corp/sangakurenkei/fb2025_hajimeni_ranking.pdf)
- [東京科学大学: 共同研究講座 (¥30m+/year)](https://www.ori.titech.ac.jp/sangaku/l-research-contract/collaborative-r-programs/)
- [Edelman 2025 B2B Thought Leadership Impact Report, via Content Marketing Institute](https://contentmarketinginstitute.com/content-marketing-strategy/thought-leadership-asset)
