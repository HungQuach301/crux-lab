# Script — Episode 6 (format `101`, C2 v2, WRITER, 2026-10-08)

Working title: *Does a 2% Annuity Raise Really Keep Up With Prices?* · Logline **L1** (C1, `gates/C1-logline.md`). Hook used: **H-B "Nghịch lý"** (paradox on a present-day fact, `hooks.md`). Format proposed: **`101`** (`episode.yaml`).

**G1 (b) addition (new WRITER, 2026-10-08; owner chose (b) at G1, `gates/G1-answer.md`):** +93 spoken words → **1,279 spoken words, est. 8:27** (505 s target met; checker ĐẠT **without** `--g1-short`; timeline axis 8:14). Added: S16.3 (typical stretch in crates, no new number), **S24.4–S24.6** (Carl year by year in crates: his check bought less on every one of his 20 anniversaries; Ruth's climbed back early, his never did), **S27.4–S27.5** (Edna's 20 years end a few years into Carl's: the same years of prices close hers with 10 crates lit and open his), **S29.2** (crates at year 20: Edna full, Ruth about 9, Carl about 4; old S29.2 → S29.3, text unchanged). **One new number:** `worst_window_years_2pct_fell_20y` = 20 (numbers.md, model.py). Carl's "about 4" derives from 43.1 % (crates = round(10 × value)). Also edited to clear two `numbers_said.py` BLOCKs present in C2 v2: S06.2 "Over Ruth's 20 years" → "Over Ruth's 20-year stretch"; S28.2 "In the 12 months to this August" → "In the year to this August". Remaining warning: experiment −8.2 points vs the `101` template (reference only, story §4). The SHORTFALL note and checker block below describe C2 v2 before this addition.

**SHORTFALL (C2 v2, owner decides at G1; without `--g1-short` the checker FAILS on length only, 471 s < 495 s after the REVIEWER fixes — the flag is valid only after the owner picks option (a)):** REVIEWER G1 wording fixes applied (CHẶN-1: S08.1, S12.1, S12.2; CHÍNH-2: S04.3, S31.3) → now **1,186 spoken words, est. 7:50 (471 s), ≈ 61 words / 24 s short**. Before those fixes: 1,175 spoken words → est. **7:46** (466 s) vs target ≥ 8:15 (495 s): **≈ 72 words / 29 s short**. Reason: blind read round 1 (6/6 readers lost attention in S19–S20 and S22–S23); the pre-registered fallback (method-section pattern, story §3) cut S18–S23 from 12 spoken sentences to 3 (plus the act-3 question, kept), with the numbers moved to on-screen labels (B19, B21, B22), the V7 card (B31) and the description. Not padded back (story §4: `101` does not pad). Checker run with `--g1-short`; MR1 kept.

**C2 v2 changes (S18–S23, S30.5 only; everything else unchanged).** S18 (1 in 3 at ≥ 90 %) and S20 (94.8 %, 99.5 %) removed as spoken scenes → labels on B19 / description. S19.1 rewritten (no spoken number): "Even the stretches that ran through the gentler 2000s and 2010s, the years closest to Ruth's own, fell short." S21.1 "And over 25 years, not one stretch kept up." (the one new spoken number of the block: 25). S22.1 = one sentence, no digits (Social Security's index about the same; a gentler measure kept up more often but still fell short in most stretches); "21 of 715" and "19.2%" on B22 and the V7 card, "description" noted there; the "since 1959 / none" comparison dropped from narration and screen (description only). S23 = the act-3 question only (S23.4 → S23.1). S30.5 now: "this video doesn't say which check, or which raise, to choose" (no option named). Act 2 now −7.4 points and act 1 +5.8 vs the `101` template (reference only, story §4).

**Checker (`python3 episodes/ep006/story/check_script.py --cast Ruth,Carl,Edna --g1-short`, from the repo root, final run C2 v2 — exit 0):**

```
số cốt lõi windows_2pct_kept_up_20y: đọc ['S14.1'], nhắc bằng lời ['S15.1', 'S15.2', 'S27.1', 'S27.3', 'S29.1']
móc script: M1 4.7 s ĐẠT · M2 27.3 s ĐẠT · M3 13.8 s ĐẠT · M4 7.0 s ĐẠT · M5 39.6 s ĐẠT · M6 0.0 s ĐẠT

76 câu, 1132 từ viết (1175 từ đọc), độ dài ước 7:46 (1175 / 2.52 từ/s, 101); trục mốc giây 7:34 (2.75 từ/s + hold 24.5 s + ident 3 s)
| Phần | Từ | Thời gian | Tỉ lệ | Khuôn 101 | Δ |
| hook | 125 | 0:00–0:49 | 10.9 % | 8 % | +2.9 |
| concept | 358 | 0:49–3:09 | 30.8 % | 25 % | +5.8  ← > ±5 (THAM KHẢO, nêu ở C2) |
| experiment | 254 | 3:09–4:52 | 22.6 % | 30 % | -7.4  ← > ±5 (THAM KHẢO, nêu ở C2) |
| buyers | 279 | 4:52–6:44 | 24.6 % | 25 % | -0.4 |
| limits | 116 | 6:44–7:34 | 11.1 % | 12 % | -0.9 |
mid-roll ≈ 3:09 sau S12.4 (hold 1.5 s), cách cuối 265 s: ĐẠT
beats.md: 30 nhịp đã kiểm số trên hình
hooks HA (4 câu riêng + S03 chung, phần riêng tới 27.6 s): M1 4.7 s ĐẠT · M2 27.6 s ĐẠT · M3 13.5 s ĐẠT · M4 7.0 s ĐẠT · M5 40.0 s ĐẠT · M6 0.0 s ĐẠT
hooks HB (4 câu riêng + S03 chung, phần riêng tới 27.3 s): M1 4.7 s ĐẠT · M2 27.3 s ĐẠT · M3 13.8 s ĐẠT · M4 7.0 s ĐẠT · M5 39.6 s ĐẠT · M6 0.0 s ĐẠT
hooks HC (4 câu riêng + S03 chung, phần riêng tới 27.6 s): M1 4.7 s ĐẠT · M2 27.6 s ĐẠT · M3 11.6 s ĐẠT · M4 7.0 s ĐẠT · M5 40.0 s ĐẠT · M6 0.0 s ĐẠT

ĐẠT
Cảnh báo (không chặn):
  độ dài ước 466 s < đích 495 s — chủ dự án đã duyệt ở G1 (--g1-short)
  khuôn tỉ lệ: concept lệch +5.8 điểm
  khuôn tỉ lệ: experiment lệch -7.4 điểm
```

Summary (C2 v2): **M1 4.7 s · M2 27.3 s · M3 13.8 s · M4 7.0 s · M5 39.6 s · M6 0.0 s (no character promise), all ĐẠT** · **1,175 spoken words → est. 7:46** (2.52 words/s; target ≥ 8:15, max 9:00 — **short by ≈ 29 s, G1**) · act Δ vs the 101 template: hook +2.9 · concept +5.8 · experiment −7.4 · people −0.4 · limits −0.9 (concept and experiment beyond ±5, reference only) · MR1 ≈ 3:09 ĐẠT (265 s from the end).

**Line format.** `Sxx.n {role} [emotion] narration <!-- claims: id, id; hold: s -->`. One sentence per line. Roles on every sentence starting before 1:00. Emotion tags (3): S01.2 `[curious]`, S10.2 `[serious]` (the `{peak}` line), S32.1 `[thoughtful]`. `hold` = silence in the edit. Visuals and on-screen text: `beats.md` (same scene ids).

**Characters (all ILLUSTRATIVE, badge on every frame).** **Ruth** = lead (story §2b): first rising check August 2006 at 65 = the latest 20-year window (`guide_*`). Arc: at or above her first check's buying power on 12 of the first 15 anniversaries; Aug 2021 (age 80) 100.3 % (on screen); Aug 2022 94.5 %; Aug 2026 (age 85) 90.4 % (spoken as "about 9 crates for every 10"); level check 60.9 % ("about 6"). Counterweights in act 3 only: **Carl** (January 1966, worst stretch: 43.1 %, level 29.0 %, 6.38 % a year) and **Edna** (January 1949, last start that kept up). Carl's and Edna's ages are not stated (no claim). The suggested "1948 starter" became January 1949 because 1948 is not in numbers.md; `kept_up_last_start_20y` is.
- Ruth's question (S01.2): *"would 2 percent keep up with prices?"* → method: S13.2 "Ruth's is one of them: the most recent" (one of 715), S13.3 "we asked Ruth's question" → final line, hers (S32.3): *"Her answer: for 15 years, mostly yes, and at 85, her check buys about 9 crates for every 10 her first one bought."*
- Peak (S10.2, 14 words): *"Then, in a single year, it fell below, and it hasn't caught up since."*
- "Keep up" defined at S03.1 (= buys at least what its own first check bought), fixing C1 L2's confusion; "buys less than her first one" (S01.1, S07.1) fixes C1 L1's "below where it started".

**Core number:** `windows_2pct_kept_up_20y` — "17 of the 715" in digits once (S14.1, fact), then in words: S15.1–S15.2 "every one of those stretches … no starting month has kept up since" (when), S27.1/S27.3 Edna "the last starting month when a 2 percent raise kept up … that early handful" (a person), S29.1 "Edna kept up, Ruth fell short late" (comparison), with S30 turning it into the viewer's threshold (raise grid: 2 % vs 3 %, 3.1 %, 6.38 %, on screen B30).

**Claim-risk applied:** no choice advice (S03.4, S30.5: "doesn't say which check, or which raise, to choose"); pricing not modeled, never "which pays more" (S04.2–S04.3, S08.3, S17.3, S31.3); "history, not a forecast" (S03.3, S28.3, S32.1); "US only" (S03.3, S32.1); national average, not a retiree's basket, health care and housing (S06.3, S31.1); overlapping, not independent (S31.2); no 20-year window after Aug 2006: "ran through the gentler 2000s and 2010s" (S19.1, the span of 1990s starts; Ruth's 2006 start is the latest); 3.1 % "a median of the past, not an expectation" (S30.3); the latest 12-month 3.4 % is "one year of history, not a forecast" (S28.3); "we" = analysts only; no imperatives.

**Checker edits (`# TẬP` lines only):** CAST = Ruth, Carl, Edna · CORE = `windows_2pct_kept_up_20y` / `\b17\b` · FULL_FORM = PCE → "personal consumption expenditures", CPI → "consumer price index" (the abbreviation "CPI" is never spoken; "CPI-U"/"CPI-W" would trip the hyphenated-abbreviation ASR rule, so the narration says "the consumer price index" and "the index Social Security uses for its yearly raises") · WORD_EXEMPT = `\b2000s and 2010s\b` (decade names required by claim-risk wording; no 2010 token exists in numbers.md; the span follows from `by_decade_1990_*` starts 1990–1999 + 20 years). Constants unchanged.

**Statements without a numbers.md number (qualitative, for REVIEWER):** S05.2 Ruth's reasoning (ILLUSTRATIVE); S06.3 the index covers "rent to medical care to gasoline" (CPI-U all items, qualitative); S09.2 "slipped under in a few early years, then climbed back" (`guide_years_2pct_at_or_above_100` definition: below at years 2, 5, 6; sizes not in numbers.md, so not quantified); S19.1 "gentler" 2000s and 2010s (1990s starts typical 94.8 % vs 80.7 % overall, on screen B19); S22.1 "about the same" (2.9 % vs 2.4 %) and "gentler price measure … fell short in most stretches" (PCE 19.2 % kept up, typical 88.0 %, on screen B22); S31.1 health care and housing "can weigh differently" (claim-risk limit, no R-CPI-E number).

**Claims wanted:** none required. Optional for a later pass: Ruth's values at years 2, 5, 6 and 17–19 (would let S09.2 be exact); Carl's and Edna's crate counts as spoken numbers (`about 4 in 10` for 43.1 % is not a display form in numbers.md, so Carl's crates appear on screen only).

**Mid-roll:** MR1 ≈ 3:09, in the 1.5 s hold after S12.4 (end of act 1, act-2 question open); 265 s from the end.

**Act questions / turns.**
- Act 1: *What does a 2 % raise add up to against prices?* Turn S10: Ruth's check, still at her first check's buying power at 80, falls below in one year and stays there (peak).
- Act 2: *Was Ruth's stretch unusual?* Turn S14–S15: 17 of 715, all starting 1947 to 1949; counterweights S17.3 (own start, not dollars), S22.1 (other indexes move the line, not the result; one sentence, numbers on screen).
- Act 3: *Why did the same raise land so differently?* Turn S29: same raise, three start months. Answers the cold-open question in S32 with the same words ("keep up with prices"), the last sentence Ruth's.

---

=== COLD OPEN ===

## S01 — Ruth's check, and her question

S01.1 {hook} Ruth's check rises every year, and it buys less than her first one. <!-- claims: guide_real_2pct_end_pct -->
S01.2 {question} [curious] At 65, she chose the smaller annuity check that rises 2 percent a year, and asked one thing: would 2 percent keep up with prices? <!-- claims: guide_start, two_pct_growth_20y_pct -->

## S02 — Twenty years on, and the promise

S02.1 {hook} Her twentieth year of checks ended this August. <!-- claims: latest_end, index_last_month -->
S02.2 {promise} We tested that raise against every 20-year stretch of US prices since 1947, to see how often it kept its buying power, and how much it usually kept. <!-- claims: windows_20y, median_real_value_2pct_payment_after_20y_pct -->

## S03 — What "keep up" means, and the limits (shared continuation for all three hooks)

S03.1 {define} Here, keeping up means a check still buys at least what its own first check bought. <!-- claims: — -->
S03.2 {hook} Ruth is an illustrative retiree, built on real US prices, and today her check falls short of that. <!-- claims: guide_real_2pct_end_pct -->
S03.3 {constraint} This is US only, and it's history, not a forecast. <!-- claims: — -->
S03.4 {constraint} It doesn't say which check to choose. <!-- claims: —; hold: 0.8 -->

=== IDENT (3 s, no narration) ===

=== ACT 1 — CONCEPT: two checks, buying power, and Ruth's twenty years ===

## S04 — Two checks

S04.1 {hook} At 65, an income annuity can pay a bigger check that never changes, or a smaller check that rises by the same percentage every year. <!-- claims: guide_start -->
S04.2 {constraint} How much smaller the rising check starts depends on the insurer, and this video doesn't model it. <!-- claims: — -->
S04.3 {constraint} So it can't compare the dollars both checks pay out over a lifetime. <!-- claims: — -->
S04.4 What it measures is buying power: what each check can buy, compared with what its own first check bought. <!-- claims: — -->

## S05 — Ruth's reasoning

S05.1 Ruth took her first rising check in August 2006. <!-- claims: guide_start -->
S05.2 Her reasoning was simple: prices go up, and her check goes up too. <!-- claims: — -->
S05.3 So what does a raise of 2 percent a year add up to? <!-- claims: two_pct_growth_20y_pct; hold: 0.8 -->

## S06 — Raises against prices

S06.1 After 20 raises, a check is 48.6 percent bigger than its first one. <!-- claims: two_pct_growth_20y_pct -->
S06.2 Over Ruth's 20-year stretch, the consumer price index rose 64.3 percent. <!-- claims: latest_window_price_rise_pct, latest_window_real_value_2pct_payment_pct; hold: 1 -->
S06.3 That index is a national average of what urban households pay for, from rent to medical care to gasoline, not any one person's own basket. <!-- claims: — -->

## S07 — The crates

S07.1 Her check grew, but prices grew more, so today it buys less than her first check did. <!-- claims: guide_real_2pct_end_pct -->
S07.2 If her first check bought 10 crates of everything the index tracks, her check today buys about 9. <!-- claims: guide_real_2pct_end_pct, latest_window_real_value_2pct_payment_pct; hold: 1 -->

## S08 — The check she turned down

S08.1 Measured against its own first check, the bigger level check she turned down would buy about 6 in 10 today. <!-- claims: guide_real_level_end_pct, latest_window_real_value_level_payment_pct -->
S08.2 So the raise slowed the loss. <!-- claims: — -->
S08.3 That's measured against each check's own start, and the level check started bigger, by an amount this video doesn't model. <!-- claims: — -->

## S09 — Year by year

S09.1 Year by year, Ruth's check bought at least what her first one did on 12 of its first 15 anniversaries. <!-- claims: guide_years_2pct_at_or_above_100 -->
S09.2 It slipped under in a few early years, then climbed back each time. <!-- claims: guide_years_2pct_at_or_above_100; hold: 1 -->

## S10 — The turn

S10.1 In August 2021, at 80, her check still bought a little more than her first one did. <!-- claims: guide_last_year_2pct_at_or_above_100 -->
S10.2 {peak} [serious] Then, in a single year, it fell below, and it hasn't caught up since. <!-- claims: guide_real_2pct_2022_pct; hold: 1.2 -->

## S11 — Where she stands now

S11.1 By August 2022, it bought 94.5 percent of what her first check did. <!-- claims: guide_real_2pct_2022_pct -->

## S12 — How fast the level check got there

S12.1 Measured against its own start, the level check she turned down fell that far much sooner. <!-- claims: guide_year_level_reaches_2pct_end -->
S12.2 By year 5, it was already down to about 9 in 10. <!-- claims: guide_year_level_reaches_2pct_end, latest_window_real_value_2pct_payment_pct -->
S12.3 Her rising check stands there now, after 20 years. <!-- claims: guide_real_2pct_end_pct, latest_window_real_value_2pct_payment_pct -->
S12.4 So was Ruth's stretch unusual, or is this what a 2 percent raise usually did? <!-- claims: two_pct_growth_20y_pct; hold: 1.5 -->

>>> MID-ROLL MR1 (in the 1.5 s hold after S12.4; act boundary) <<<

=== ACT 2 — SMALL EXPERIMENT: every 20-year stretch since 1947 ===

## S13 — The replay

S13.1 We took every starting month from January 1947 to August 2006, and followed prices for 20 years after each one. <!-- claims: windows_20y -->
S13.2 That's 715 stretches, and Ruth's is one of them: the most recent. <!-- claims: windows_20y, latest_start -->
S13.3 For each one, we asked Ruth's question: did a check rising 2 percent a year still buy at least what its first check bought? <!-- claims: windows_20y, two_pct_growth_20y_pct -->
S13.4 Each tile here is one stretch, lined up by the month it started. <!-- claims: windows_20y -->

## S14 — The answer

S14.1 It kept up in 17 of the 715. <!-- claims: windows_2pct_kept_up_20y, windows_20y; hold: 1.2 -->
S14.2 That's about 1 in 42. <!-- claims: share_2pct_kept_up_20y_pct -->

## S15 — All from one short window

S15.1 Every one of those stretches started between September 1947 and January 1949. <!-- claims: windows_2pct_kept_up_20y, kept_up_first_start_20y, kept_up_last_start_20y -->
S15.2 Since then, no starting month has kept up, including Ruth's. <!-- claims: windows_2pct_kept_up_20y, kept_up_last_start_20y; hold: 1 -->

## S16 — The typical stretch

S16.1 In the typical stretch, prices rose 3.1 percent a year. <!-- claims: median_inflation_20y_pct_per_year -->
S16.2 So after 20 raises, the rising check typically bought 80.7 percent of what its first check bought. <!-- claims: median_real_value_2pct_payment_after_20y_pct; hold: 1 -->
S16.3 In crates, the typical rising check ended with most of its 10 still lit. <!-- claims: median_real_value_2pct_payment_after_20y_pct -->

## S17 — The level check in the typical stretch

S17.1 A level check, over the same stretches, typically kept 54.3 percent, about half. <!-- claims: median_real_value_level_payment_after_20y_pct -->
S17.2 And typically, the level check had already sunk to where the rising check would end by about year 8. <!-- claims: median_year_level_reaches_2pct_end_median -->
S17.3 Again, that's buying power against each check's own start, not dollars paid. <!-- claims: — -->

## S19 — Even the calmer decades

S19.1 Even the stretches that ran through the gentler 2000s and 2010s, the years closest to Ruth's own, fell short. <!-- claims: by_decade_1990_median_real_2pct, by_decade_2000_kept, median_real_value_2pct_payment_after_20y_pct -->

## S21 — Longer retirements

S21.1 And over 25 years, not one stretch kept up. <!-- claims: windows_25y, windows_2pct_kept_up_25y; hold: 1 -->

## S22 — Other price measures

S22.1 We also ran it on the index Social Security uses for its yearly raises, with about the same result; on a gentler price measure, the raise kept up more often but still fell short in most stretches. <!-- claims: robust_cpiw_share_kept_up_20y_pct, share_2pct_kept_up_20y_pct, robust_pce_share_kept_up_20y_pct, robust_pce_median_real_2pct_pct, median_real_value_2pct_payment_after_20y_pct -->

## S23 — The act-3 question

S23.1 Then why did the same raise land so differently from one start to another? <!-- claims: —; hold: 1 -->

=== ACT 3 — PEOPLE: the same raise, three starting months ===

## S24 — Carl, the worst start

S24.1 Ruth isn't the worst case, and she isn't the best. <!-- claims: — -->
S24.2 Carl, also illustrative, took the same kind of rising check in January 1966. <!-- claims: worst_window_start_year_20y -->
S24.3 His 20 years had the fastest price rise of any stretch: 6.38 percent a year. <!-- claims: raise_needed_all_20y_pct; hold: 1 -->
S24.4 Like Ruth's, his first check bought a row of 10 crates. <!-- claims: worst_window_years_2pct_fell_20y -->
S24.5 On every one of his 20 anniversaries, his check bought less than it had the year before. <!-- claims: worst_window_years_2pct_fell_20y -->
S24.6 Ruth's check climbed back in her early years; Carl's never did. <!-- claims: guide_years_2pct_at_or_above_100, worst_window_years_2pct_fell_20y; hold: 1 -->

## S25 — Carl's end

S25.1 After 20 raises, his check bought 43.1 percent of what his first check bought. <!-- claims: worst_real_value_2pct_payment_after_20y_pct -->
S25.2 A level check, in his stretch, would have bought 29 percent. <!-- claims: worst_real_value_level_payment_after_20y_pct -->
S25.3 His raise helped, and it still left him with less than half. <!-- claims: worst_real_value_2pct_payment_after_20y_pct; hold: 1 -->

## S26 — Not a freak

S26.1 He wasn't alone: stretches that began in the 1960s typically ended at 44.3 percent. <!-- claims: by_decade_1960_median_real_2pct -->

## S27 — Edna, the last one that kept up

S27.1 Edna, also illustrative, started in January 1949, the last starting month when a 2 percent raise kept up. <!-- claims: kept_up_last_start_20y, windows_2pct_kept_up_20y -->
S27.2 Twenty years later, her check still bought at least what her first one did. <!-- claims: kept_up_last_start_20y, windows_20y -->
S27.3 She is part of that early handful, and nobody who started after her got that answer. <!-- claims: windows_2pct_kept_up_20y -->
S27.4 Her 20 years ended a few years into Carl's. <!-- claims: kept_up_last_start_20y, worst_window_start_year_20y, windows_20y -->
S27.5 The same few years of prices that ended her stretch with all 10 crates lit began his. <!-- claims: kept_up_last_start_20y, worst_window_start_year_20y, worst_window_years_2pct_fell_20y; hold: 1 -->

## S28 — Ruth, this year

S28.1 And Ruth, at 85, is still losing ground. <!-- claims: guide_real_2pct_end_pct -->
S28.2 In the year to this August, prices rose 3.4 percent, more than her 2 percent raise. <!-- claims: cpi_yoy_latest_pct, index_last_month, two_pct_growth_20y_pct -->
S28.3 That's one year of history, not a forecast for the year after it. <!-- claims: —; hold: 1 -->

## S29 — Same raise, three starts

S29.1 Same raise, same rule: Edna kept up, Ruth fell short late, and Carl fell far behind. <!-- claims: windows_2pct_kept_up_20y, guide_last_year_2pct_at_or_above_100, worst_real_value_2pct_payment_after_20y_pct -->
S29.2 In crates, Edna's row ended full, Ruth's at about 9, and Carl's at about 4. <!-- claims: kept_up_last_start_20y, guide_real_2pct_end_pct, latest_window_real_value_2pct_payment_pct, worst_window_years_2pct_fell_20y -->
S29.3 What differed was the month each one started, and what prices did after that. <!-- claims: —; hold: 1 -->

## S30 — What raise history kept up with

S30.1 So what raise did keep up, in this history? <!-- claims: — -->
S30.2 A raise of 3 percent a year kept up in 42.4 percent of the 20-year stretches. <!-- claims: raise_grid_3pct -->
S30.3 About 3.1 percent kept up in half: that's the typical rate from before, a median of the past, not an expectation. <!-- claims: raise_needed_half_20y_pct, median_inflation_20y_pct_per_year -->
S30.4 Keeping up in every stretch took the rate of Carl's years. <!-- claims: raise_needed_all_20y_pct -->
S30.5 These rates describe what prices did; this video doesn't say which check, or which raise, to choose. <!-- claims: —; hold: 1 -->

=== LIMITS + METHOD + OUTRO ===

## S31 — Limits and method

S31.1 The consumer price index is a national average, not a retiree's own basket, and health care and housing can weigh differently for someone Ruth's age. <!-- claims: — -->
S31.2 The 715 stretches overlap, so they're not 715 separate tests. <!-- claims: windows_20y -->
S31.3 And because annuity pricing isn't modeled, nothing here compares the dollars both checks pay out over a lifetime. <!-- claims: — -->
S31.4 How we know this, and what's left out, is on this card and in the description. <!-- claims: —; hold: 5 -->

## S32 — Outro: back to Ruth's question

S32.1 [thoughtful] This is US only, and it's history, not a forecast. <!-- claims: — -->
S32.2 Twenty years ago, Ruth asked whether 2 percent a year would keep up with prices. <!-- claims: latest_window_real_value_2pct_payment_pct, two_pct_growth_20y_pct -->
S32.3 Her answer: for 15 years, mostly yes, and at 85, her check buys about 9 crates for every 10 her first one bought. <!-- claims: guide_last_year_2pct_at_or_above_100, guide_real_2pct_end_pct, latest_window_real_value_2pct_payment_pct; hold: 2 -->
