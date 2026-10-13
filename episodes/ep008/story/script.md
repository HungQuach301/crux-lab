# Script — Episode 8 (format `lab`, C2 v1, WRITER, 2026-10-13)

Working title: *Is Rent Money Wasted? Rent vs Buy, Replayed Through Real US History* · Logline **L1** (C1, `gates/C1-logline.md`; lead renamed Nina). Hook used: **H-A "Câu hỏi của người xem"** (`hooks.md`). Format: **`lab`**.

**Checker (`python3 episodes/ep008/story/check_script.py episodes/ep008/story/script.md --cast Nina`, from the repo root, final run C2 v1 — exit 0):**

```
số cốt lõi share_buyer_ahead_10y: đọc ['S13.2'], nhắc bằng lời ['S14.1', 'S25.2', 'S32.2', 'S32.3']
móc script: M1 3.4 s ĐẠT · M2 24.7 s ĐẠT · M3 5.3 s ĐẠT · M4 8.6 s ĐẠT · M5 30.8 s ĐẠT · M6 0.0 s ĐẠT

96 câu, 1391 từ viết (1510 từ đọc), độ dài ước 10:29 (1510 / 2.4 từ/s, lab); trục mốc giây 9:47 (2.66 từ/s + hold 16.8 s + ident 3 s)
| Phần | Từ | Thời gian | Tỉ lệ | Khuôn lab | Δ |
| hook | 106 | 0:00–0:46 | 7.9 % | 8 % | -0.1 |
| concept | 303 | 0:46–2:45 | 20.2 % | 15 % | +5.2  ← > ±5 (THAM KHẢO, nêu ở C2) |
| experiment | 532 | 2:45–6:37 | 39.5 % | 45 % | -5.5  ← > ±5 (THAM KHẢO, nêu ở C2) |
| buyers | 325 | 6:37–8:58 | 24.0 % | 20 % | +4.0 |
| limits | 125 | 8:58–9:47 | 8.4 % | 12 % | -3.6 |
mid-roll: ĐỦ điều kiện theo độ dài ước 10:29 (cần ≥ 8:00 thật; ≥ 2 phút đầu/cuối; lặng ≥ 1 s) — chốt bằng độ dài thật sau khi sinh lời (≥ 8:10) và ở C5 (≥ 8:00)
mid-roll ≈ 2:45 sau S07.4 (hold 1.5 s), cách cuối 422 s: ĐẠT
mid-roll ≈ 6:37 sau S22.4 (hold 1.5 s), cách cuối 190 s: ĐẠT
beats.md: 32 nhịp đã kiểm số trên hình
hooks HA (4 câu riêng + S03 chung, phần riêng tới 24.1 s): M1 3.4 s ĐẠT · M2 24.1 s ĐẠT · M3 5.3 s ĐẠT · M4 6.4 s ĐẠT · M5 29.7 s ĐẠT · M6 0.0 s ĐẠT
hooks HB (5 câu riêng + S03 chung, phần riêng tới 28.6 s): M1 1.9 s ĐẠT · M2 28.6 s ĐẠT · M3 9.8 s ĐẠT · M4 6.4 s ĐẠT · M5 34.2 s ĐẠT · M6 0.0 s ĐẠT
hooks HC (4 câu riêng + S03 chung, phần riêng tới 26.7 s): M1 4.1 s ĐẠT · M2 26.7 s ĐẠT · M3 15.0 s ĐẠT · M4 6.4 s ĐẠT · M5 32.3 s ĐẠT · M6 0.0 s ĐẠT

ĐẠT
Cảnh báo (không chặn):
  mật độ: ≥ 3 số mới trong 8 s tại ~[229, 288, 358, 448] s
  khuôn tỉ lệ: concept lệch +5.2 điểm
  khuôn tỉ lệ: experiment lệch -5.5 điểm
  hooks HB: M2 = 28.6 s trong ±5 % ngưỡng 30 (nêu tên, CHARTER §4)
```

**Summary.** Nina (ILLUSTRATIVE) rents in September 2026 and has saved enough for the down payment and closing costs on a $400,000 home; her question (S01.2): *"Is her rent money wasted?"* Two identical twins per start month, one buys, one rents and keeps the cash; 307 start months (January 1991 → July 2016) on one street, each followed ten years. Act 1: what each twin pays, the renter's cash sits still (C1 lesson, before any historical number), the one assumption on her door (the rent tag). Act 2: walking the street — the 1990s all lit, the dark stretch April 2001 → December 2007 (6 of 72 in 2002 through 2007), lit again 2009 → mid-2016; anchor 1 "about 3 in 4"; extremes April 2012 / June 2006 (anchor 2, peak); five / fifteen years. Act 3: Marcus and Priya (counterweights), the rent tag turns (anchor 3: 4 % → 64.2 %, 6 % → 92.2 %, Census range 73.6–87.3 %, flip below about 2.4 %, Treasury bill variant about 2 in 3), Nina's first month today (56.8 %, below every replayed month, first months only). Limits, then Nina's answer.

**Characters (all ILLUSTRATIVE, badge on every frame).** **Nina** = lead (story §2b; dossier situation 1 adapted: a renter with savings for 20 % down near the national median, card `viewer`). Own warm lamp (N3). Through the method: S04.3, S08.4 (her month sits past the end of the street), S22.4, S26.2, S29. **Marcus** (June 2006 start) and **Priya** (April 2012 start): counterweights in act 3 only (S23), no new numbers. No `promise_character` (M6 = 0).

**Core number:** `share_buyer_ahead_10y` — "about 3 in 4" in digits once (S13.2, fact, anchor 1), then in words: S14.1 "that lit share … a count of history, not a promise" (meaning), S25.2 "the share moves with the rent you assume" (comparison: it moves with the tag), S32.2 "most houses are lit … the lights move with the tag on her door" (callback), S32.3 Nina's answer "in most start months … depends on the rent she assumes" (her threshold).

**Peak** (S17.2, `{peak}`, 10 words): *"Ten years on, the June 2006 buyer was $82,385 behind."*
**Final line (Nina's, answers S01.2):** S32.3 *"Nina's answer: her rent isn't wasted by rule; renting cost more than buying in most start months, and how many depends on the rent she assumes."*

**Claim-risk applied (`topics-r2/machine/rent-buy-1/claim-risk.md` + `numbers.md` "Luật nói"):** no advice — S03.3 "Nothing here says whether to buy or to keep renting", no imperatives, conclusions only as "in X of Y start months, the buyer ended ahead" + counterweight (S13.3, S14.1, S16.2, S19.3, S22.4, S26.2, S30.3); never "buying wins" — S25.2 "the share moves with the rent you assume"; "history, not a forecast" + "US only" — S03.2, S31.4, fog past July 2016 (N5); national index, not one house — S19.3, S31.2; starting rent is an assumption — S06.4, S07.1–S07.2, S24.1, S31.2; CPI rent follows sitting tenants, can understate market rent growth — S31.3; renter's cash in cash / Treasury bill variant, not stocks, viewer question 4 not answered — S05.1–S05.5 (before the first historical number); no income taxes / deduction / refinancing / moving costs / renter's insurance — S05.6, S31.4, V7; "today" = first month only, not a forecast, 2026 is not 2006 — S30.3; `worst_price_change_10y` used only as "the window of the worst start" (S19.1); illustrative people — S03.1, S23.2, badges; not called "first" (description cites Beracha & Johnson 2012).

**Advice-like word list (13/10):** none of should / need to / have to / better off / worth it / pays off / wins / beat / safe / risky / the bar / the test / threshold / consider / make sure in narration or on screen. "wasted" only in Nina's question (S01.2, B32) and in her answer's negation (S32.3). "Throwing money away" appears only in hook H-B (unused), as a quote followed by its counterweight.

**Checker edits:** `# TẬP:` lines — CAST = Nina · CORE = `share_buyer_ahead_10y` / `3 in 4` · FULL_FORM = CPI → "consumer price index" · WORD_EXEMPT = `\b2002 through 2007\b` (era name; the years are in the claim id `era_2002-2007_*`, not in its value column). BANNED_NAMES unchanged (Nina, Marcus, Priya not in it). **One non-`TẬP` line changed, flagged:** the `numbers.md` table regex — Episode 8's `numbers.md` has 4 columns (no source column) and the template regex needed 5, so it read **0 claims**; the 5th column is now optional (`(?: ([^|\n]*) \|)?`, `g or ''`). Nothing else changed.

**Claims wanted (blocking for the C1 wording, not for the checker):** `numbers.md` has no rows for the savings ($92,000), the down payment ($80,000, 20 %), closing costs ($12,000, 3 %), selling cost (6 %) or ownership costs (2.5 % a year = property tax 1.0 + insurance 0.5 + repairs 1.0). Rule "every spoken or on-screen number is a `numbers.md` claim" → the script names these costs **without figures** (S01.3, S04.2–S04.3, S13.4) and keeps down payment and closing costs as **two separate labelled stacks** (B02). When ANALYST adds the rows, drop-in lines: S01.3 → *"She has saved $92,000: $80,000 for a down payment on a $400,000 home, and $12,000 for closing costs."*; S04.3 + *"Property tax, insurance and repairs come to 2.5 percent of the price a year, and selling costs 6 percent."* (+ ≈ 20 words; scene density re-checked).

**Statements without a numbers.md number (qualitative, for REVIEWER):** S05.2–S05.3 the renter's pile = down payment + closing costs + monthly savings (card `renter`); S06.1–S06.2 competitor weakness (dossier: 3 of 6 top videos use fixed assumptions; no channel named); S07.3 / S24.2 mechanism of the rent tag (rent level sets the monthly saving); S09.3 / S11.2 / S12.2 why eras differ (prices climbing / the national price fall / lower prices and rates at start — read off the replay inputs, no figure); S21.2 five years leaves little time to cover buying and selling costs; S23.6 neither could see the outcome at purchase. B13 anchor object "232 lit / 75 dark" = 307 − 75 (not on screen as text).

**Mid-roll:** MR1 ≈ 2:45 (axis), in the 1.5 s hold after S07.4 (end of act 1, act-2 question open); MR2 ≈ 6:37, in the 1.5 s hold after S22.4 (end of act 2), 190 s from the end.

**Act questions / turns.**
- Act 1: *What does each twin actually pay, and what is assumed?* Turn S05.1 (the renter's money sits in cash, not stocks) and S07.1 (the one assumption hangs on her door).
- Act 2: *How often did the buying twin end up ahead?* Turn S13.2 (anchor 1, about 3 in 4) and S17.2 (peak, June 2006); S20–S22 holding period.
- Act 3: *What made one house bright and another dark?* Turn S23.5 (only the month differed), S24.4–S25.2 (the street follows the tag); S29–S30 Nina's own month; S32 answers the cold-open question with the same words ("rent money wasted"), the last sentence hers.

**Line format.** `Sxx.n {role} [emotion] narration <!-- claims: id, id; hold: s -->`. Emotion tags (4): S01.2 `[worried]`, S17.2 `[serious]` (`{peak}`), S25.2 `[thoughtful]`, S32.3 `[thoughtful]`. ASR hotwords: **Nina**, Marcus, Priya, "Treasury bill" (never "T-bill" spoken), "CPI" after its full form (S31.3); no hyphenated year ranges ("2002 through 2007", "2009 to mid-2016"), no "%" in narration.

---

=== COLD OPEN ===

## S01 — Nina's question

S01.1 {hook} It's September 2026, and Nina pays rent again. <!-- claims: rate_month_latest -->
S01.2 {question} [worried] Is her rent money wasted? <!-- claims: —; hold: 0.6 -->
S01.3 {hook} She has saved enough for the down payment and the closing costs on a $400,000 home. <!-- claims: price -->

## S02 — The promise

S02.1 {promise} We replayed her choice in every month since 1991, one twin buying and one renting, to see whether renting cost more than buying over ten years, and when it didn't. <!-- claims: first_10y, n_10y; hold: 0.5 -->

## S03 — Who Nina is, the limits (shared continuation for all three hooks)

S03.1 {hook} Nina and her twin are illustrative; the home prices, rents and mortgage rates are real. <!-- claims: — -->
S03.2 {constraint} US only, and history, not a forecast. <!-- claims: — -->
S03.3 {constraint} Nothing here says whether to buy or to keep renting. <!-- claims: — -->
S03.4 {hook} What it shows Nina is a whole street of answers, one house for each month. <!-- claims: —; hold: 0.5 -->

=== IDENT (3 s, no narration) ===

=== ACT 1 — CONTEXT: two twins, one street, one assumption on the door ===

## S04 — What each twin pays (viewer questions 1 and 3)

S04.1 {question} So what does each twin actually pay? <!-- claims: — -->
S04.2 {define} The twin who buys pays the down payment and the closing costs, then takes a 30-year fixed mortgage at that month's average rate. <!-- claims: rate_latest -->
S04.3 {hook} Every month after that, Nina's buying twin pays interest, property tax, insurance and repairs, and at the end, the cost of selling. <!-- claims: — -->
S04.3b {define} Property tax, insurance and repairs come to 2.5 percent of the home's value a year, and selling costs 6 percent. <!-- claims: owner_cost_pct, sell_pct -->
S04.4 The twin who rents moves into an equivalent home and keeps the same savings. <!-- claims: — -->

## S05 — The renter's cash sits still (C1 blind-read lesson; viewer question 4 not answered)

S05.1 Here is the part most people picture differently: the renting twin's savings sit in cash, not in stocks. <!-- claims: — -->
S05.2 That pile starts as the down payment and closing costs that never went into a house. <!-- claims: — -->
S05.3 Whatever renting saves each month is added to the same pile. <!-- claims: — -->
S05.4 In one variant, the cash earns Treasury bill interest, and nothing more. <!-- claims: — -->
S05.5 So whether investing the difference would have done better is a different question, and this episode doesn't answer it. <!-- claims: — -->
S05.6 It also leaves out moving costs, renter's insurance, income taxes and the mortgage interest deduction, and nobody refinances. <!-- claims: —; hold: 0.5 -->

## S06 — One assumption, in plain sight (competitor weakness, anchor gap)

S06.1 Most rent or buy math picks one growth rate for prices and one for rents, then shows a single answer. <!-- claims: — -->
S06.2 It doesn't show how that answer moves when the assumptions move, and it doesn't replay what actually happened in the US. <!-- claims: — -->
S06.3 Here, prices, rents and mortgage rates come from the real monthly US record. <!-- claims: — -->
S06.4 One thing can't come from that record: the rent level the renting twin starts at. <!-- claims: — -->

## S07 — The rent tag

S07.1 So it hangs on the apartment door as a tag: a starting rent of 5 percent of the home's price a year. <!-- claims: yield_anchor_pct -->
S07.2 On a $400,000 home, that's $1,667 a month today, carried back through history with the government's rent index. <!-- claims: price, today_rent_month1 -->
S07.3 The tag matters because the rent decides how much the renting twin sets aside each month, and so how big that cash pile grows. <!-- claims: — -->
S07.4 Later, the tag turns, and the answer turns with it. <!-- claims: —; hold: 1.5 -->

>>> MID-ROLL 1 (in the 1.5 s hold after S07.4; end of act 1, act-2 question open)

=== ACT 2 — JOURNEY: walking the street, 1991 to 2016 ===

## S08 — The street

S08.1 So what does the real record say about the twins? <!-- claims: — -->
S08.2 Each start month gets one identical house on a long street, January 1991 on the left, July 2016 on the right. <!-- claims: first_10y, last_10y -->
S08.3 That's 307 houses, and each one is followed for ten years. <!-- claims: n_10y -->
S08.4 Nina's own month sits past the end of the street, in the fog, because its ten years haven't happened. <!-- claims: n_10y -->
S08.5 After ten years, a house lights up when the buying twin's equity, after the cost of selling, is bigger than the renting twin's cash. <!-- claims: n_10y -->
S08.6 When the cash is bigger, its door goes dark. <!-- claims: —; hold: 0.5 -->

## S09 — The 1990s

S09.1 So, walking the street from 1991, how often did the buying twin end up ahead? <!-- claims: first_10y -->
S09.2 Through the 1990s, every house lights up. <!-- claims: era_1990s_share -->
S09.3 Prices climbed, the loan balance shrank, and by year ten the buyer's equity was ahead of the renter's cash, start after start. <!-- claims: n_10y -->

## S10 — The dark stretch

S10.1 Then, from April 2001, doors start going dark. <!-- claims: renter_first_10y -->
S10.2 Every house where the renting twin came out ahead sits between April 2001 and December 2007. <!-- claims: renter_first_10y, renter_last_10y -->

## S11 — 2002 through 2007

S11.1 Of the 72 start months from 2002 through 2007, the buyer ended ahead in just 6. <!-- claims: era_2002-2007_n, era_2002-2007_share -->
S11.2 Those starts ran straight into the fall in national home prices. <!-- claims: — -->

## S12 — Lit again

S12.1 Then the street lights up again: every start from 2009 to mid-2016 ended with the buyer ahead. <!-- claims: era_2009-2016_share -->
S12.2 Those buyers started from lower prices and lower mortgage rates. <!-- claims: — -->

## S13 — The count (anchor 1: the lights)

S13.1 Counted along the whole street, the picture is this. <!-- claims: —; hold: 0.8 -->
S13.2 In about 3 in 4 of the 307 start months, the buyer ended ahead. <!-- claims: share_buyer_ahead_10y, n_10y; hold: 1.5 -->
S13.3 In the other 75, the renter did. <!-- claims: n_renter_ahead_10y -->
S13.4 That count already includes interest, property tax, insurance, repairs, and the cost of buying and of selling. <!-- claims: — -->

## S14 — A count, not a promise

S14.1 That lit share is a count of history, not a promise for any one month. <!-- claims: share_buyer_ahead_10y -->
S14.2 In the middle start month, the buyer ended about $157,000 ahead. <!-- claims: median_adv_10y -->
S14.3 But the spread around that middle is wide. <!-- claims: — -->

## S15 — The brightest house

S15.1 The brightest house is April 2012: ten years later, the buyer was about $484,000 ahead. <!-- claims: best_start_10y, best_adv_10y, n_10y -->

## S16 — Why it shone

S16.1 That loan started at 3.91 percent, and national prices more than doubled over the window. <!-- claims: best_rate_10y, best_price_change_10y -->
S16.2 It's one month at the very top of the range, not a typical one. <!-- claims: — -->

## S17 — The darkest house (anchor 2: two stacks; peak)

S17.1 And the darkest house is June 2006. <!-- claims: worst_start_10y; hold: 0.8 -->
S17.2 {peak} [serious] Ten years on, the June 2006 buyer was $82,385 behind. <!-- claims: worst_start_10y, worst_adv_10y, n_10y; hold: 1.5 -->

## S18 — Two stacks

S18.1 Beside that house stand a pair of stacks: the buyer's equity, $115,374, and the renter's cash, $197,760. <!-- claims: worst_equity_10y, worst_pot_10y -->

## S19 — Why it went dark

S19.1 National prices rose only 3.2 percent in those ten years, while the buyer paid interest, tax, insurance and repairs the whole way. <!-- claims: worst_price_change_10y, n_10y -->
S19.2 And that loan started at 6.68 percent. <!-- claims: worst_rate_10y -->
S19.3 That's the national index, not one house; a single home in a single city could have done much better or much worse. <!-- claims: —; hold: 0.5 -->

## S20 — Five years (viewer question 2)

S20.1 Does the length of the stay change the picture? <!-- claims: — -->
S20.2 Over five years instead of ten, the buyer ended ahead in 74.4 percent of start months. <!-- claims: share_buyer_ahead_5y, worst_start_5y, n_10y -->

## S21 — The worst five-year start

S21.1 The worst five-year start, May 2006, left the buyer $149,392 behind. <!-- claims: worst_start_5y, worst_adv_5y -->
S21.2 Five years leaves little time to cover the cost of buying and then selling. <!-- claims: worst_start_5y -->

## S22 — Fifteen years

S22.1 Over 15 years, every start month that history allows ended with the buyer ahead. <!-- claims: n_15y, share_buyer_ahead_15y -->
S22.2 Even the weakest of them left the buyer $79,829 ahead. <!-- claims: worst_adv_15y -->
S22.3 From five years to ten to fifteen, the dark doors thin out, and then they're gone. <!-- claims: worst_start_5y, n_10y -->
S22.4 Fifteen years is a long stay, and this street says nothing about how long Nina stays. <!-- claims: n_15y; hold: 1.5 -->

>>> MID-ROLL 2 (in the 1.5 s hold after S22.4; end of act 2, act-3 question open)

=== ACT 3 — ANSWER: two neighbors, the rent tag turns, and Nina's own month ===

## S23 — Two neighbors (counterweights, ILLUSTRATIVE)

S23.1 What made one house bright and another dark? <!-- claims: — -->
S23.2 A pair of illustrative neighbors on that street show what the month alone did. <!-- claims: — -->
S23.3 Marcus bought in June 2006, at the darkest house, and ten years later his renting twin was ahead. <!-- claims: worst_start_10y, n_10y -->
S23.4 Priya bought in April 2012, at the brightest, and ended far ahead of hers. <!-- claims: best_start_10y -->
S23.5 Same rent tag, same costs, same street; only the month was different. <!-- claims: — -->
S23.6 And on the day each of them bought, neither could see which house they were standing in. <!-- claims: —; hold: 0.5 -->

## S24 — The tag turns (anchor 3: the rent tag)

S24.1 So far, every house used the same tag: a starting rent of 5 percent of the price a year. <!-- claims: yield_anchor_pct -->
S24.2 A higher starting rent means a pricier rental, so the renting twin sets aside less each month. <!-- claims: — -->
S24.3 What happens to the street when the tag turns? <!-- claims: —; hold: 0.8 -->
S24.4 At 4 percent, the buyer ended ahead in 64.2 percent of start months. <!-- claims: share_yield4pct_10y -->

## S25 — Six percent

S25.1 At 6 percent, 92.2 percent. <!-- claims: share_yield6pct_10y; hold: 1.0 -->
S25.2 [thoughtful] The share moves with the rent you assume. <!-- claims: share_buyer_ahead_10y -->

## S26 — The public range

S26.1 For reference, the Census Bureau's vacancy survey puts asking rents between 4.83 and 5.59 percent of asking prices a year in its latest reports. <!-- claims: hvs_yield_2025Q4, hvs_yield_2026Q1 -->
S26.2 Those are different baskets of empty homes, so it's a reference range, not Nina's own rent. <!-- claims: — -->

## S27 — Across that range

S27.1 Across that range, the buyer ended ahead in 73.6 to 87.3 percent of start months. <!-- claims: share_hvs_2025Q4_10y, share_hvs_2026Q1_10y -->

## S28 — Where it flips, and the Treasury bill variant

S28.1 The majority flips to the renter only when the tag drops below about 2.4 percent. <!-- claims: flip_yield_10y -->
S28.2 And if the renter's cash earns Treasury bill interest, the buyer's share falls to about 2 in 3. <!-- claims: share_tbills_10y; hold: 0.5 -->

## S29 — Nina's month today

S29.1 And Nina's own month, out in the fog? <!-- claims: — -->
S29.2 History can't finish it, but it can set her first month beside the others. <!-- claims: — -->
S29.3 At 6.86 percent, the September 2026 average, her buying twin's first month costs $2,933. <!-- claims: rate_latest, today_buyer_month1 -->

## S30 — First months only

S30.1 Her assumed rent, $1,667, is 56.8 percent of that. <!-- claims: today_rent_month1, today_rent_to_outlay -->
S30.2 That's lower than in any start month on the street; the lowest was 57.9 percent, in July 2006. <!-- claims: rent_to_outlay_min_10y, rent_to_outlay_min_start_10y -->
S30.3 It compares first months only: it doesn't say how a 2026 start ends, and it doesn't make 2026 another 2006. <!-- claims: rate_month_latest, rent_to_outlay_min_start_10y; hold: 1.0 -->

=== LIMITS ===

## S31 — Limits and method

S31.1 The limits, briefly. <!-- claims: — -->
S31.2 The house is a national price index, not one home, and the starting rent is an assumption. <!-- claims: — -->
S31.3 The rent history comes from the consumer price index for rent, CPI, which follows sitting tenants and can understate how fast market rents grew. <!-- claims: — -->
S31.4 No income taxes, no mortgage interest deduction, no refinancing; US only, and history, not a forecast. <!-- claims: — -->
S31.5 The full method is in the description. <!-- claims: —; hold: 0.8 -->

## S32 — Nina's answer

S32.1 So, back to the question Nina started with. <!-- claims: — -->
S32.2 On her street, most houses are lit, a dark stretch sits in the middle, and the lights move with the tag on her door. <!-- claims: share_buyer_ahead_10y -->
S32.3 [thoughtful] Nina's answer: her rent isn't wasted by rule; renting cost more than buying in most start months, and how many depends on the rent she assumes. <!-- claims: share_buyer_ahead_10y; hold: 1.5 -->
