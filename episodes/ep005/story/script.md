# Script — Episode 5 (format `101`, C2 draft v2 (blind test C2 fixes), WRITER, 2026-10-06)

Working title: *10% Down and Mortgage Insurance: How Long Did It Last?* · Logline **L2** (C1). Hook used: **H-A "Câu hỏi của người xem"** (`hooks.md`).

**Line format.** `Sxx.n {role} [emotion] narration <!-- claims: id, id; hold: s -->`. One sentence per line. `{role}` (`hook` / `promise` / `question` / `constraint` / `define`) on every sentence that starts before 1:00. Emotion tags (eleven_v3, scene-level generation, G-015): **3**, key beats only (S01.2 `[curious]`, S17.1 `[serious]`, S20.1 `[thoughtful]`). No break tags, no "...", no speed. `hold` = silence in the edit after the sentence, not narration. Visuals, on-screen text and library templates: `beats.md` (same scene ids).

**Characters.** Grace (bought June 2014, the typical case), Owen (January 2004, fastest), Victor (October 2005, slowest) are **ILLUSTRATIVE** buyers built from real purchase months (`buyer_grace_*`, `buyer_owen_*`, `buyer_victor_*`); ILLUSTRATIVE badge on screen whenever they or their numbers appear. The $400,000 home / $360,000 loan / payment are ILLUSTRATIVE. No PMI premium amount anywhere (S04.3 says so).

**Fixed forms (said once, then recalled in words):** "about 8 years" (schedule to 80 %) · "23 months" (typical, on paper) · "about 1 in 7" (more than 5 years) · "15.6 percent" (at or below 75 % at two years) · "90.6 percent" (no later than the schedule) · "112 months" (October 2005). Percentages are spoken "percent"; "PMI" is said in full once ("private mortgage insurance, or PMI"); the index is "the Federal Housing Finance Agency's national index of home purchase prices".

**Core number** (schedule ≈ 8 years vs typical 23 months on paper) returns with new meaning: fact (S02.1 schedule; S11.1 typical) → comparison (S11.4 "the schedule's long road and the replay's typical one") → the stand-in for the typical case (S15.3, Grace) → threshold for the viewer (S18.3–S18.4: a plan that counts on "about two years") → outro (S20.2). Recalls are in words.

**Counts** (`check_script.py`, 2.4 words/s, numbers expanded as spoken, plus holds and a 3 s ident): see the act table printed by the checker; summary copied here after the last passing run:

| Part (story §4, `101`) | Scenes | Words | Est. time | Share | Template | Δ pts |
|---|---|---|---|---|---|---|
| Hook + promise + constraints (cold open + ident) | S01–S03 | 133 | 0:00–1:00 | 12.0 % | 8 % | +4.0 |
| Act 1 · concept (PMI, the 80/78 schedule) | S04–S09 | 318 | 1:00–3:24 | 28.9 % | 25 % | +3.9 |
| Act 2 · small experiment on real data | S10–S14 | 301 | 3:24–5:40 | 27.2 % | 30 % | −2.8 |
| Act 3 · three buyers + the viewer's comparison | S15–S18 | 274 | 5:40–7:43 | 24.6 % | 25 % | −0.4 |
| Limits + method (V7, 5 s read) + outro | S19–S20 | 70 | 7:43–8:19 | 7.2 % | 12 % | −4.8 |

Total narration **1,096 words** (≈ 1,136 read out), est. **≈ 8:19** incl. 23.5 s of holds and the 3 s ident; ≈ 8:37 with end screen. No part off by more than ±5 pts. Closest: limits **−4.8** — blind test C2 pre-registered fallback: S19 is one spoken sentence, the "not modeled" list moved to the V7 card and the description (B19); hook **+4.0** — the "on paper" gap (C1 blind, 6/6 readers) is explained inside the cold open by design.

**Statements without a numbers.md claim (qualitative, flagged for REVIEWER):** S04.1 "lenders usually require [PMI] on a conventional loan with less than 20 percent down" (general practice, no source in the dossier); S13.3 the slow months "sit together … just before and during the national price slump" (WRITER recomputed with `model/model.py`: all 45 set-B months over 60 months are purchases from 2005 through 2009; not in numbers.md, so no year is spoken); S17.2 Victor's index "rose a little, then fell for years" (same recomputation: peak +4.3 % at month 20, low −18.8 % at month 75, claims `buyer_victor_index_peak` / `buyer_victor_index_trough`; on screen only "still below").

**Mid-roll:** **MR1 ≈ 3:27**, end of Act 1, inside the 1.5 s hold after S09.4 (act-2 question left open). ≥ 120 s from start and 295 s from the end (last two minutes start ≈ 6:22).

**Act questions / turns.**
- Act 1: *When does the insurance end?* Turn (S08.3–S09.2): both legal dates come from the schedule alone and ignore the house's value; value is the other road.
- Act 2: *How fast did rising prices really get 10 % down buyers to 80 % on paper?* Turn (S11): typical 23 months vs the schedule's ≈ 8 years; counterweight S12 (on paper ≠ removal) and the tail S13–S14.
- Act 3: *Why did the same rule give such different answers?* Turn (S17): Victor, the year after Owen, slower than his own schedule. Answers the cold-open question in S20 with the same words ("how long … last").

---

=== COLD OPEN ===

## S01 — The viewer's question

S01.1 {hook} You've saved 10 percent of a home's price. <!-- claims: ex_extra_down_for_20 -->
S01.2 {question} [curious] Do you buy now and pay mortgage insurance, or keep renting until you reach 20 percent? <!-- claims: ex_extra_down_for_20 -->

## S02 — The stake and the promise

S02.1 {hook} On the schedule alone, you can't even ask to cancel it for about 8 years. <!-- claims: sched80_months_latest, rate_latest; hold: 1 -->
S02.2 {promise} We replayed real US prices and rates month by month, so you'll see how long it took on paper, typically and in slow cases. <!-- claims: nB, medianB_months_to80, maxB_months_to80 -->

## S03 — What "on paper" means, right away

S03.1 {define} On paper means the loan is 80 percent of the home's value by a national price index. <!-- claims: medianB_months_to80 -->
S03.2 {hook} That's not the same as getting the insurance removed. <!-- claims: — -->
S03.3 {define} Removal on today's value, when you ask, is the loan owner's rule; for Fannie Mae loans, that's a waiting period and a 75 percent bar. <!-- claims: value_removal_rule, value_removal_ltv_early, value_removal_seasoning_years; label: "Fannie Mae: wait ≥ {value_removal_seasoning_years} years · loan ≤ {value_removal_ltv_early}" (B+2) -->
S03.4 {promise} You'll also meet three illustrative buyers who got very different answers. <!-- claims: buyer_owen_*, buyer_grace_*, buyer_victor_* -->
S03.5 {constraint} It's US only, history, not a forecast, and it won't say whether to buy or wait. <!-- claims: —; hold: 0.8 -->

=== IDENT (3 s, no narration) ===

=== ACT 1 — CONCEPT: what the insurance is, and the schedule's two dates ===

## S04 — What the insurance is

S04.1 {define} Private mortgage insurance, or PMI, is a policy lenders usually require on a conventional loan with less than 20 percent down. <!-- claims: pmi_required_below20 -->
S04.2 It protects the lender if the loan goes bad, but the borrower pays for it, month after month, on top of the mortgage. <!-- claims: — -->
S04.3 What it costs depends on the loan and the borrower, so this video puts no dollar figure on it. <!-- claims: pmi_premium -->
S04.4 What we can measure is how long it lasts. <!-- claims: — -->
S04.5 So when does it end? <!-- claims: —; hold: 0.8 -->

## S05 — One illustrative loan

S05.1 Here's an illustrative example: a $400,000 home, a little under the national median price of new homes sold from April through June. <!-- claims: ex_price, mspus_latest -->
S05.2 With 10 percent down, that leaves a $360,000 loan. <!-- claims: ex_loan, ex_extra_down_for_20; hold: 1 -->

## S06 — The rate and the payment

S06.1 At September's average mortgage rate, 6.86 percent, the monthly payment for principal and interest is the figure on screen. <!-- claims: rate_month_latest, rate_latest, ex_payment_pi -->
S06.2 Taxes, home insurance and the mortgage insurance all come on top of it. <!-- claims: — -->
S06.3 Each payment pays the balance down a little, slowly at first, and faster later on. <!-- claims: — -->

## S07 — The law's first date: you can ask

S07.1 By federal law, the borrower can ask to cancel the insurance once the schedule says the loan is down to 80 percent of the original value, here $320,000. <!-- claims: ex_target80, sched80_months_latest, borrower_request_conditions; hold: 1 -->
S07.2 On this loan, that's payment 99, the date this video opened with. <!-- claims: sched80_months_latest -->
S07.3 That request comes with conditions, such as being current on payments. <!-- claims: borrower_request_conditions -->

## S08 — The law's second date: it ends on its own

S08.1 And the insurance has to end automatically when the schedule reaches 78 percent, as long as payments are current. <!-- claims: sched78_months_latest, ex_target78 -->
S08.2 Here, that's about 9.5 years in. <!-- claims: sched78_months_latest; hold: 1 -->
S08.3 Both dates come from the schedule alone, and both ignore what the house is worth. <!-- claims: — -->

## S09 — The other road: the home's value

S09.1 Lenders, and the investors who own loans, can also drop the insurance based on the home's current value. <!-- claims: value_removal_rule -->
S09.2 If prices rise, the same balance becomes a smaller share of the home, and 80 percent can arrive sooner, on paper. <!-- claims: sched80_months_latest -->
S09.3 That's what on paper means in this video, and a lender's request, appraisal and minimum time still come after it. <!-- claims: value_removal_rule -->
S09.4 So how fast did rising prices actually get 10 percent down buyers there? <!-- claims: medianB_months_to80; hold: 1.5 -->

>>> MID-ROLL MR1 (≈ 3:27, in the 1.5 s hold after S09.4; act boundary) <<<

=== ACT 2 — SMALL EXPERIMENT: the replay ===

## S10 — Setting up the replay

S10.1 We took every purchase month from January 1991 to July 2016. <!-- claims: nB -->
S10.2 For each one, we set up the same 10 percent down loan at that month's average rate. <!-- claims: nB, ex_extra_down_for_20 -->
S10.3 And we let the home's value move exactly like the Federal Housing Finance Agency's national index of home purchase prices. <!-- claims: nB -->
S10.4 Every month after that, we compare the balance with the value, and stop the clock the first time the loan is 80 percent or less. <!-- claims: medianB_months_to80 -->
S10.5 Each bar here is one purchase month, and its height shows how long that took. <!-- claims: — -->

## S11 — The typical answer

S11.1 The typical answer: 23 months. <!-- claims: medianB_months_to80; hold: 1.2 -->
S11.2 Half of the purchase months got there sooner, and half took longer. <!-- claims: medianB_months_to80 -->
S11.3 And in 90.6 percent of them, prices got the loan to 80 percent on paper no later than the schedule would have. <!-- claims: shareB_le_sched80; hold: 1 -->
S11.4 That's the gap between the schedule's long road and the replay's typical one. <!-- claims: — -->

## S12 — But "on paper" is not removal

S12.1 But that's on paper. <!-- claims: — -->
S12.2 We also checked a larger set: every purchase month since January 1991 with two years of prices after it. <!-- claims: nA -->
S12.3 Two years after purchase, only 15.6 percent of them were at or below the 75 percent bar Fannie Mae sets for its loans when a borrower asks to cancel on today's value, a separate route from the law's schedule. <!-- claims: shareA_ltv24_le75, nA, value_removal_ltv_early, value_removal_rule; hold: 1 -->
S12.4 So reaching 80 percent on paper in about two years was common in this history, while clearing that early bar by then was not. <!-- claims: medianB_months_to80, shareA_ltv24_le75 -->

## S13 — The slow tail

S13.1 The typical case also hides a long tail. <!-- claims: — -->
S13.2 About 1 in 7 purchase months took more than 5 years. <!-- claims: shareB_over60; hold: 1 -->
S13.3 They sit together in one stretch of the grid, the months just before and during the national price slump. <!-- claims: shareB_over60, slowB_n, slowB_years, hpi_peak_month, hpi_trough_month -->

## S14 — The slowest month

S14.1 The slowest was October 2005: 112 months on paper. <!-- claims: maxB_start, maxB_months_to80; hold: 1.2 -->
S14.2 That's longer than the schedule itself took at that month's rate. <!-- claims: buyer_victor_* -->
S14.3 And this is a national average: no single home tracks it, and a local market can do much better or much worse. <!-- claims: — -->
S14.4 So why did the same rule give such different answers? <!-- claims: —; hold: 1 -->

=== ACT 3 — HOW IT DIFFERED: three illustrative buyers, and the viewer's comparison ===

## S15 — Grace, the typical case

S15.1 Three illustrative buyers, each with 10 percent down, show why. <!-- claims: buyer_owen_*, buyer_grace_*, buyer_victor_* -->
S15.2 Grace bought in June 2014, at 4.16 percent. <!-- claims: buyer_grace_* -->
S15.3 Her loan reached 80 percent on paper right at the middle of the replay: she is the typical case from before. <!-- claims: buyer_grace_*, medianB_months_to80 -->
S15.4 Her own schedule would have taken several years longer. <!-- claims: buyer_grace_* -->

## S16 — Owen, the fastest

S16.1 Owen bought in January 2004, while prices were climbing fast. <!-- claims: buyer_owen_* -->
S16.2 He reached 80 percent on paper in 13 months, the fastest in the replay. <!-- claims: buyer_owen_*, minB_months_to80; hold: 1 -->
S16.3 Rising prices did most of that work, not his payments. <!-- claims: buyer_owen_* -->

## S17 — Victor, the slowest

S17.1 [serious] Victor bought the year after Owen, in October 2005: the slowest month in the replay. <!-- claims: buyer_victor_*, buyer_owen_*, maxB_start -->
S17.2 Prices rose a little, then fell for years, and even when he finally reached 80 percent on paper, the index was still below where it started. <!-- claims: buyer_victor_*, buyer_victor_index_peak, buyer_victor_index_trough -->
S17.3 He got there by paying the loan down, and his own schedule, at his lower rate of 6.07 percent, reached 80 percent of the original price first, at payment 90. <!-- claims: buyer_victor_*; hold: 1 -->
S17.4 Whether a lender would have dropped his insurance at that point, this data can't show. <!-- claims: — -->

## S18 — What a viewer can hold a plan against

S18.1 Same rule, same national index: what differed was the month they started, and what prices did next. <!-- claims: buyer_owen_*, buyer_victor_* -->
S18.2 So a plan can be measured against two benchmarks from this history. <!-- claims: sched80_months_latest, medianB_months_to80 -->
S18.3 One is the schedule the law uses, which on the example loan runs most of a decade. <!-- claims: sched80_months_latest, sched78_months_latest -->
S18.4 The other is history on paper: a plan that counts on about two years matched the typical month, not the slow ones, and not the lender's step. <!-- claims: medianB_months_to80, shareB_over60 -->
S18.5 On the illustrative $400,000 home, the other path, 20 percent down, means $40,000 more up front. <!-- claims: ex_price, ex_extra_down_for_20; hold: 1 -->
S18.6 This video doesn't weigh that against renting or waiting; it measures how long the insurance math took. <!-- claims: — -->

=== LIMITS + METHOD + OUTRO ===

## S19 — Limits and method

S19.1 How we know this, and what this video leaves out, is on this card and in the description. <!-- claims: —; hold: 5 -->

## S20 — Outro: back to the opening question

S20.1 [thoughtful] So how long does the insurance last? <!-- claims: — -->
S20.2 On the schedule, the answer is set the day the loan starts; on paper, history gave answers from about a year to more than 9 years, and on paper is never the same as removed. <!-- claims: sched80_months_latest, minB_months_to80, maxB_months_to80 -->
S20.3 This is US only, and it's history, not a forecast. <!-- claims: —; hold: 2 -->
