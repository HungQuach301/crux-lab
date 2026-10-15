# Script — Episode 9 (format `lab`, C2 v3, WRITER, 2026-10-15)

**C2 v4 (REVIEWER G1):** S01.1/S03.3 "almost nine times" (88.9 %; S01.1 still 11 words, "out of ten" → "in ten" to fit 5.0 s — re-check ASR); S17.5 rewritten as a replay statement + `share_buyer_ahead_stocks_5y/_10y/_15y`; S25.5 + `flip_yield_stocks_10y`; method round 2: S06.1 + S07.1 merged into one line S06.1 (S07 removed, "same costs as before" on card V7/B10 only, hold + mid-roll 1 now after S06.1; older notes citing S07.1 now mean S06.1/B10). `check_script.py` not run; needs a blind re-read of the method block.

**Table-read fix (Eric 0.9, `review-g1/table-read.json`):** cold open cut ≈ 12 s before the promise end — S01.1+S01.2 → one hook (S01.2 removed; expectation moved to S02.1 "So renting looks smart"), twins named inside S02.2, S03.3 promise reduced to the paradox only ("since 1991" + `n_10y` moved to S03.5), "9 in 10" → "nine times out of ten" (ASR heard "nine and ten"). Estimated (2.45 w/s, real gaps): S01.1 end ≈ 4.7 s · M7 third fact ≈ 30.0 s · M3 question ≈ 36.3 s · M2 promise ≈ 44.2 s. `check_script.py` not run (no shell).

**C2 v3 changes (blind read r2, "số dày" 4/6):** spoken figures thinned to words, exact figures kept on screen (B14 67.6 %, B15 16 start months, B16 none of 72 · 6 with cash, B17 $261,689, B18 183 of 307, B24 78.0 %, B24b 53.4 %): S10.1 "about two in three", S11.2 "a short run of start months around March 1999", S12.2 "none of them" (the one spoken count), S12.3 "a handful", S13.2 "more than a quarter of a million dollars", S14.2 "more than half the windows", S17.1 "nearly four times in five", S17.4 "a little more than half". No sentence cut, claim IDs unchanged; S04.2–S04.3 already separated by the 0.8 s anchor silence before S04.3; S15.2, peak and Nina's last line untouched. `check_script.py` not run (no shell).

**C2 v2 changes (blind read 6/6, method block BLOCKING).** S06–S08 cut from 12 spoken lines to 4: S06.1 competitor gap (one assumed growth rate vs the real monthly record, no channel named), S07.1 costs unchanged (the list moved to card B10), S08.1 rent tag (5 percent of the price a year, July 2026, an assumption that decides later), S08.2 act-2 question (was S08.4). "Before fees and taxes, dividends reinvested" and "buys every month, through every drop" are now on card B11 only (discipline is still spoken at S14.3–S14.5). The "last time" line in the method block is gone. Lit/dark are now defined at S03.5. S02.1 is split into two short sentences. S03.3 and S19.1 now say "about 9 in 10 times" (`share_stocks_beat_house_10y`). S18.1 and S18.5 are reworded in plain words (fifteen years: most lights go out; next: the rent tag). S22.3 and S22.4 are merged into one line (split near 5.1 percent, Census Bureau data on both sides; range on B30 only), and old S22.5 is now S22.4. Mid-roll 1 now comes after S07.1. **Not re-run in this pass:** shell access was denied, so `check_script.py` did not run. Hand count: about 1,270 spoken words, so the estimated length is about **8:50**, under the 9:00 `lab` floor. Per the brief, nothing was padded; this goes to G1. Hand-checked timing estimates: M2 ≈ 47.7 s, M3 ≈ 37.1 s, M7 ≈ 31.5 s, mid-roll 1 ≈ 2:17, mid-roll 2 ≈ 6:10 (≈ 133 s before the end). The checker block below is still the v1 output.
**C2 v2b:** S18.1 no longer says "fifteen"/"ten" (it had no claim). New S17.4–S17.5: the five-year result for Q2 ("a stay half as long", stocks 53.4 %, `share_buyer_ahead_stocks_5y`), so the stays run five → ten → fifteen. Old S17.4 is now S17.6. The five-year cash figure is left out because `share_buyer_ahead_cash_5y` is not in numbers.md. The word "five" is not spoken because no attached claim allows it.

Working title: *Rent and Invest the Difference: Every Month Since 1991, Replayed* · Logline **L1** (C1). Hook used: **H-B "Nghịch lý"** (`hooks.md`). Sequel of Episode 8; answers its hand-off S33.1.

**Checker (`python3 episodes/ep009/story/check_script.py episodes/ep009/story/script.md`, repo root, run 3 — exit 0, no `--g1-short`):**

```
số cốt lõi share_buyer_ahead_stocks_10y: đọc ['S15.2'], nhắc bằng lời ['S15.4', 'S17.2', 'S19.1', 'S22.2', 'S22.5', 'S25.2', 'S25.5']
móc script: M1 4.5 s ĐẠT · M2 47.3 s ĐẠT · M3 37.5 s ĐẠT · M4 5.2 s ĐẠT · M5 4.5 s ĐẠT · M6 0.0 s ĐẠT · M7 31.9 s ĐẠT · M8 1.0 câu ĐẠT
93 câu, 1314 từ viết (1393 từ đọc), độ dài ước 9:40 (1393 / 2.4 từ/s, lab); trục mốc giây 9:09
| hook 13.1 % (+5.1) | concept 18.5 % (+3.5) | experiment 43.2 % (-1.8) | buyers 17.4 % (-2.6) | limits 7.8 % (-4.2) |
mid-roll ≈ 2:53 sau S07.4 (hold 1.5 s): ĐẠT · mid-roll ≈ 6:51 sau S18.5 (hold 1.5 s), cách cuối 138 s: ĐẠT
beats.md: 36 nhịp · hooks HA/HB/HC: M1–M8 ĐẠT (M2 41.7 / 47.0 / 41.7 s)
ĐẠT — cảnh báo: khuôn tỉ lệ hook +5.1 điểm
```
**Named for C2 (THAM KHẢO):** hook share +5.1 points, because the cold open carries the pile definition (S03.6–S03.7, C1 finding) so act 1 can open on a result; M2 47.3 s is within 5 % of 50 s (named, CHARTER §4); M8 = 1 sentence (at the limit). Checker rule note: era years (2002, 2009, 1990s) cannot be matched because they live only in claim ids — handled with WORD_EXEMPT (narration) and unquoted era labels (beats), as Episode 8 did.

**Summary.** Cold open (stands alone, no "last time"): 0:00 paradox — over ten years, stocks outgrew home prices about 9 in 10 times (S01.1), so the viewer expects renting and investing to come out ahead (S01.2); Nina rents with $92,000 saved; one twin buys, one rents (S02.1); three facts that push against that expectation — with the renting twin holding cash, the buyer ended ahead about 3 in 4 times (S02.2, Nina-tied) · with the same money in stocks, only about half (S02.3) · over fifteen years cash kept the buyer ahead every time, stocks only about 1 in 5 (S03.1); Nina's question (S03.2, audience Q4); the promise as a paradox (S03.3); one spoken limit (S03.4); the street, lit/dark defined (S03.5); the renter's pile defined in one sentence + picture (S03.6–S03.7, C1 finding). Act 1: the first house, January 1991 — first spoken result 4 s after S03 (S04.2), then why (stocks almost quintupled, the pile = $92,000 + monthly gap), the competitor gap (one line), the costs (one line, list on card), the rent tag (one line), all after the first result. Act 2: walking the street with the pile in stocks — 1990s mostly lit, January 1991 the darkest, 16 starts around March 1999 where stocks lost, 2002 through 2007 none of 72, June 2006 darker; the pile sank below its start in 183 of 307 windows (peak: $54,310, she kept investing); the count 152 of 307 (core), 80 switched, none back; April 2012 still lit; 2009 through mid-2016 78 percent lit; over fifteen years most lights go out. Act 3: the paradox resolved (the house grows on all $400,000, the pile starts at $92,000; the renter's catch-up = monthly gap + time) → no monthly gap: about 2 in 3; 1 percent fee: 55 percent; the rent tag decides (flip at about 5.1 percent, right on the 5 percent assumption; Census range on screen). Limits, scoreboard, the 0:00 street returns, hand-off to an open question, Nina's answer last.

**Characters (ILLUSTRATIVE, badge on every frame).** **Nina** = lead (dossier situation 1, as Episode 8). Cold open S02.1, S02.2, S03.2; through the method S09.4 (her month is not on the street), S14 (the renting twin who kept investing), S22.1 (the tag on her door), S25 (answer). No counterweight characters (the two Episode 8 houses, June 2006 and April 2012, act as counterweights without new people). No `promise_character` (M6 = 0).

**Core number:** `share_buyer_ahead_stocks_10y` — in digits once, S15.2 "152 of the 307, about half" (fact). Recalled in words (claim on the line, no digits): S15.4 "that half is a count … not a promise" (meaning) · S17.2 "the half isn't spread evenly" (comparison across eras) · S19.1 the paradox question (stocks outgrow homes, yet half) · S22.2 / S22.4 "at 5 percent … almost exactly in half … the answer sits on the rent tag" (threshold: the half sits on the assumption) · S25.2 scoreboard · S25.5 Nina's "coin flip". Said in words in the cold open too (S02.3, S03.3, before the digits).

**Peak** (S14.3, `{peak}`, 11 words): *"One renting twin's pile sank to $54,310, and she kept investing."*
**Nina's answer (answers S03.2, last line):** S25.5 *"Nina's answer: investing the difference made her street a coin flip, and her rent tag tips it."*
**Hand-off (story §1c, next topic not approved):** S25.4 *"What no house on this street can show is how long Nina herself will stay."* — open question, no episode named, no date; picture: Nina's bare lot past the end of the street (B37).

**The paradox (promise S03.3):** *"stocks outgrew the house about 9 in 10 times, yet buying still came out ahead in half."* (worded without "buyer" so the checker does not read it as a character promise) Resolved S19 (base: $400,000 vs $92,000) + S20 (without the monthly gap the buyer leads about 2 in 3) + S22 (where the half falls depends on the rent tag).

**Act questions / turns.**
- Act 1: *What changes when the renter's pile is invested?* Turn S04.3 (the same first house flips from $48,410 ahead to $485,063 behind).
- Act 2: *How much of the street stays lit?* Turns S12.2 (none of 72), S14.3 (peak: the pile sinks, she keeps going), S15.2 (core: about half), S18.3 (fifteen years: about one in five).
- Act 3: *Why does the house still hold half, and what tips it?* Turns S19.2 (the base), S20.2 (no monthly gap), S22.3 (the tag, Census range on screen); S25 answers S03.2.

**First spoken result after the cold open (owner rule 15/10, T8-2):** **S04.2** ("…finished ten years $48,410 ahead"), estimated start ≈ 3 s ident + 3.4 s (S04.1) ≈ **6–7 s after the end of S03** (≤ 60 s). Costs, assumption and data source come after it (S06.1, S07.1, S08.1 + cards B09–B11).

**Viewer questions answered (dossier): 4 of 5, main = Q4.**
- **Q4** (is the renter's money invested, and does it beat home equity?) → S03.6–S03.7 (the pile, invested), S04–S05 (first house), S09–S18 (the whole street, 10 and 15 years), S19–S21 (why; lump variant; fees), S25.
- **Q1** (cost once interest, taxes, insurance, maintenance count) → S07.1 (all counted), card B10.
- **Q2** (different rates, prices, rents) → real rates/prices replayed S09–S17 (eras), S22 (the rent tag turned; Census range on screen).
- **Q3** (hidden costs) → S07.1 + card B10 (closing, selling 6%), S21.1–S21.2 (fees on the renter's side), S24.1 (taxes not counted).
- **Q5** (non-financial) → S23.2: named as not measured.

**Competitor gap (one beat, no channel named):** S06.1 — one assumed growth rate → every month replayed from the real record (B09).

**Claim-risk applied (`numbers.md` "Luật nói"):** no advice: no imperatives, conclusions as "in X of Y start months, the buyer ended ahead" + counterweight (S04.4, S11.3, S15.4, S17.2, S21.3, S23.1); on screen B03 "Not advice to buy, rent or invest"; "history, not a forecast": S03.4 (only spoken limit in 0:00–1:00), S24.1; "US only": S24.1 + corner tag from B01; stocks "the whole US stock market", no index brand, "before fees and taxes" card B09/B11 + fee variant S21; no capital-gains or home taxes S24.1; discipline is an assumption: S03.7, card B11, S14.4–S14.5; lump variant S20; rent tag is an assumption S08.1, S22.4; Census range on screen only (B33); stocks pile ≠ advice to buy stocks S23.1; illustrative people: badge + B03 "Nina and her twins: ILLUSTRATIVE · prices, rents, rates, stock returns: real"; episode not called "first"; Episode 8 referenced only as "last time" after the cold open (S13.1, S16.1).

**Advice-like word list:** none of should / need to / have to / better off / worth it / pays off / wins / beat / safe / risky / consider / make sure in narration or on screen. "invests"/"investing" only as description of the replay (S03.2 question, S14.3, S20.1, S25.5).

**Statements without a numbers.md number (qualitative, for REVIEWER):** S05.3 pile mechanics; S06.1 competitor weakness; S11.3 the buyer kept paying down her loan; S12.4 buyers paid near the peak of home prices; twins kept buying through the market's fall; S16.3 April 2012 bought after prices had fallen; S17.3 low prices and rates at start; S18.4 longer stays give the pile time to compound; S19.3–S19.4 base effect; S21.3 any renter-side cost moves houses back toward the buyer (direction shown by the fee variant).

**Checker notes:** `# TẬP:` lines only — CORE = `share_buyer_ahead_stocks_10y` / `\b152\b`; WORD_EXEMPT = era names `2002 through 2007`, `2009 through mid-2016`, `1990s` (the years live in claim ids `era_*`, not in the value column, so the checker cannot match them); FULL_FORM empty (no abbreviation spoken; CRSP on screen only). CAST/BANNED_NAMES unchanged.

**Line format.** As Episode 8. Emotion tags (3): S03.2 `[worried]`, S14.3 `[serious]` (`{peak}`), S25.5 `[thoughtful]`. ASR: no hyphenated year ranges, no "%", no "minus"; "Census Bureau" in full.

---

=== COLD OPEN ===

>>> CHAPTER 1: "Two piles, one street" (on screen + YouTube chapter)

## S01 — The paradox (hook)

S01.1 {hook} Over ten years, stocks outgrew homes almost nine times in ten. <!-- claims: share_stocks_beat_house_10y, n_10y -->

## S02 — Nina, and two facts

S02.1 {hook} So renting looks smart. Nina rents, with $92,000 saved. <!-- claims: savings_usd -->
S02.2 {fact} If her renting twin held cash, her buying twin ended ahead about 3 in 4 times. <!-- claims: share_buyer_ahead_cash_10y -->
S02.3 {fact} With that cash in stocks instead, the buyer led only about half the time. <!-- claims: share_buyer_ahead_stocks_10y -->

## S03 — Fact three, the question, the promise, the street (shared continuation for all three hooks)

S03.1 {fact} Over fifteen years, cash kept the buyer ahead every time; stocks, only about 1 in 5. <!-- claims: share_buyer_ahead_cash_15y, share_buyer_ahead_stocks_15y -->
S03.2 {question} [worried] So if Nina rents and invests the difference, does she end up ahead of owning? <!-- claims: — -->
S03.3 {promise} Stocks outgrew the house almost nine times out of ten, yet buying still came out ahead in half. <!-- claims: share_stocks_beat_house_10y, share_buyer_ahead_stocks_10y -->
S03.4 {constraint} It's history, not a forecast. <!-- claims: — -->
S03.5 {hook} We replayed every start month since 1991 as a house on one long street: lit if the buyer ends ahead, dark if not. <!-- claims: n_10y -->
S03.6 {define} The renting twin's pile is the $92,000, plus whatever owning would have cost each month beyond her rent. <!-- claims: savings_usd -->
S03.7 {hook} All of it goes into the whole US stock market, every month, through every drop. <!-- claims: —; hold: 0.8 -->

=== IDENT (3 s, no narration) ===

=== ACT 1 — CONTEXT: one change on the same street ===

>>> CHAPTER 2: "The first house" (on screen + YouTube chapter)

## S04 — The first house (first spoken result; Q4)

S04.1 The first house on that street is January 1991. <!-- claims: n_10y -->
S04.2 With the renting twin's pile kept in cash, the buyer finished ten years $48,410 ahead. <!-- claims: adv_1991-01_cash_10y, n_10y -->
S04.3 With the pile in stocks, the same buyer finished $485,063 behind. <!-- claims: adv_1991-01_stocks_10y; hold: 1.5 -->
S04.4 Same house, same mortgage, same rent; the only thing that moved was the renter's pile. <!-- claims: — -->

## S05 — Almost five times

S05.1 In those ten years, a dollar in the whole US stock market grew almost five times. <!-- claims: stocks_growth_1991-01_10y, n_10y -->
S05.2 And the renter's pile was never a single dollar: it was the $92,000 on day one, plus a deposit every month. <!-- claims: savings_usd -->
S05.3 Whenever owning cost more than renting that month, the gap went into her pile, and the market grew that too. <!-- claims: — -->
S05.4 So one change, stocks instead of cash, turned the first house from lit to dark. <!-- claims: —; hold: 0.8 -->

## S06 — One growth rate, or the real record (competitor gap; Q2)

S06.1 A lot of rent-versus-buy math assumes one growth rate; this replays what actually happened, month by month. <!-- claims: —; hold: 1.5 -->

>>> MID-ROLL 1 (in the 1.5 s hold after S06.1; costs on card B10/V7 only; end of act 1, act-2 question opens at S08.2)

=== ACT 2 — JOURNEY: walking the street with the pile in stocks ===

>>> CHAPTER 3: "The lights go out" (on screen + YouTube chapter)

## S08 — The tag on the door

S08.1 The renting twin's rent is an assumption, the tag on her door: 5 percent of the price a year, as of July 2026, and later, that tag decides. <!-- claims: yield_anchor_pct, hpi_last -->
S08.2 So, with the pile in stocks, how much of the street stays lit? <!-- claims: —; hold: 1.0 -->

## S09 — The street

S09.1 After ten years, a house is lit if the buying twin's equity, after selling costs, is bigger than the renting twin's pile. <!-- claims: n_10y -->
S09.2 If the pile is bigger, the door goes dark. <!-- claims: — -->
S09.3 That's 307 houses, from January 1991 to the last start with ten full years of data, July 2016. <!-- claims: n_10y, last_10y -->
S09.4 Nina's own month isn't on the street; its ten years are still ahead of her. <!-- claims: n_10y; hold: 0.5 -->

## S10 — The 1990s

S10.1 Most of the 1990s houses stay lit: about two in three of them. <!-- claims: era_1990s_share_stocks -->
S10.2 But the darkest house on the whole street is the very first one, January 1991. <!-- claims: worst_start_stocks_10y -->
S10.3 Its renting twin caught the long stock boom from its first month. <!-- claims: — -->

## S11 — Where stocks went nowhere

S11.1 A few years later, the market itself stalled. <!-- claims: — -->
S11.2 In a short run of start months around March 1999, a dollar in stocks was worth less than a dollar ten years on. <!-- claims: n_stocks_lost_10y, stocks_growth_worst_start_10y, n_10y -->
S11.3 Those houses stay lit: the pile lost ground while the buyer kept paying down her loan. <!-- claims: — -->

## S12 — 2002 through 2007

S12.1 Then the street goes dark, and stays dark. <!-- claims: — -->
S12.2 For starts from 2002 through 2007, the buyer ended ahead in none of them. <!-- claims: era_2002-2007_share_stocks; hold: 1.0 -->
S12.3 With cash, a handful of them had stayed lit; with stocks, those lights go out too. <!-- claims: era_2002-2007_share_cash -->
S12.4 These buyers paid near the peak of home prices, while their twins kept buying stocks through the market's fall and rebound. <!-- claims: — -->

## S13 — The darkest house from last time

S13.1 June 2006 was the darkest house last time, with the pile in cash. <!-- claims: adv_2006-06_cash_10y -->
S13.2 With stocks, that buyer ends ten years more than a quarter of a million dollars behind. <!-- claims: adv_2006-06_stocks_10y, n_10y; hold: 1.5 -->
S13.3 The dark house got darker. <!-- claims: —; hold: 0.5 -->

>>> CHAPTER 4: "The pile that sank" (on screen + YouTube chapter)

## S14 — Below where she started (discipline)

S14.1 Dark doors don't mean the renting twins had an easy ride. <!-- claims: — -->
S14.2 In more than half the windows, the stock pile dipped below the $92,000 it started with. <!-- claims: n_pot_below_start_stocks_10y, savings_usd -->
S14.3 {peak} [serious] One renting twin's pile sank to $54,310, and she kept investing. <!-- claims: min_pot_stocks_10y; hold: 1.5 -->
S14.4 The replay assumes every renting twin did exactly that, every month, through every drop. <!-- claims: — -->
S14.5 Real people sometimes stop, and a renter who sells in a crash is not on this street. <!-- claims: —; hold: 0.5 -->

## S15 — The count (core number)

S15.1 So, after the whole walk, how many houses are lit? <!-- claims: — -->
S15.2 Lit: 152 of the 307, about half. <!-- claims: share_buyer_ahead_stocks_10y; hold: 1.5 -->
S15.3 80 start months switched from the buyer to the renter, and not one switched the other way. <!-- claims: n_flip_to_renter_10y, n_flip_to_buyer_10y -->
S15.4 That half is a count of what already happened, not a promise about Nina's month. <!-- claims: share_buyer_ahead_stocks_10y -->

## S16 — The brightest house from last time

S16.1 April 2012 was the brightest house last time, and it still glows. <!-- claims: adv_2012-04_cash_10y -->
S16.2 With stocks, that buyer still ends $237,632 ahead. <!-- claims: adv_2012-04_stocks_10y -->
S16.3 She bought after prices had fallen, and her house rose on its whole price, not just on her $92,000. <!-- claims: price, savings_usd -->

## S17 — Lit again

S17.1 Starts from 2009 through mid-2016 are lit nearly four times in five. <!-- claims: era_2009-2016_share_stocks -->
S17.2 So the half isn't spread evenly: whole stretches are lit, and one long stretch is dark. <!-- claims: share_buyer_ahead_stocks_10y -->
S17.3 Those buyers started with lower prices and low mortgage rates, and that held the lights on. <!-- claims: — -->
S17.4 Over a stay half as long, with the pile in stocks, the buyer was ahead a little more than half the time. <!-- claims: share_buyer_ahead_stocks_5y -->
S17.5 In this replay, the longer the stay, the more often the pile finished ahead. <!-- claims: share_buyer_ahead_stocks_5y, share_buyer_ahead_stocks_10y, share_buyer_ahead_stocks_15y -->
S17.6 Half a street, lit in stretches; now, a longer stay. <!-- claims: —; hold: 0.5 -->

## S18 — Fifteen years

S18.1 Stay longer still, and with stocks, most of the lights go out. <!-- claims: — -->
S18.2 With cash, every one of the 247 fifteen-year starts left the buyer ahead. <!-- claims: n_15y, share_buyer_ahead_cash_15y -->
S18.3 With stocks, only about one in five did. <!-- claims: share_buyer_ahead_stocks_15y -->
S18.4 The longer the stay, the longer the pile has to compound, and the further it pulls ahead. <!-- claims: — -->
S18.5 Longer stays favored the pile; the rent tag is the one assumption left to test. <!-- claims: —; hold: 1.5 -->

>>> MID-ROLL 2 (in the 1.5 s hold after S18.5; end of act 2, act-3 question open)

=== ACT 3 — ANSWER: why the house still holds half, and what tips it ===

>>> CHAPTER 5: "Why the house holds half" (on screen + YouTube chapter)

## S19 — The paradox, resolved

S19.1 So how can stocks outgrow home prices about 9 in 10 times, and the buyer still finish ahead in half? <!-- claims: share_stocks_beat_house_10y, share_buyer_ahead_stocks_10y -->
S19.2 Because the buyer's house grows on all $400,000 of it, while the renter's pile starts at $92,000. <!-- claims: price, savings_usd -->
S19.3 The mortgage lets a slower thing grow on a much bigger base. <!-- claims: — -->
S19.4 The renter catches up only through the monthly gap, and through time. <!-- claims: —; hold: 0.5 -->

## S20 — Without the monthly gap (Q4)

S20.1 So what if nobody saves that gap, and only the $92,000 is invested? <!-- claims: savings_usd -->
S20.2 Then the buyer is ahead in about 2 in 3 start months. <!-- claims: share_buyer_ahead_lump_10y; hold: 1.0 -->
S20.3 The monthly habit, not the one big deposit, did most of the renter's catching up. <!-- claims: — -->

## S21 — Fees

S21.1 The pile in this replay also pays no fees and no taxes. <!-- claims: — -->
S21.2 With 1 percent a year taken out, the lit share rises to 55 percent. <!-- claims: fee_pct, share_buyer_ahead_stocks_fee_10y -->
S21.3 Each real cost on the renter's side moves houses back toward the buyer. <!-- claims: —; hold: 0.5 -->

>>> CHAPTER 6: "The tag on her door" (on screen + YouTube chapter)

## S22 — The rent tag decides

S22.1 And then there's the tag on Nina's door. <!-- claims: — -->
S22.2 At 5 percent, the street splits almost exactly in half. <!-- claims: yield_anchor_pct, share_buyer_ahead_stocks_10y -->
S22.3 The split sits near 5.1 percent, and public rent data from the Census Bureau falls on both sides of it. <!-- claims: flip_yield_stocks_10y, hvs_yield_2025Q4, hvs_yield_2026Q1; hold: 1.0 -->
S22.4 So the answer sits on the rent tag, and the tag is an assumption. <!-- claims: share_buyer_ahead_stocks_10y; hold: 1.5 -->

## S23 — What the street can't count (Q5)

S23.1 None of this ranks stocks above a house, or a house above stocks. <!-- claims: — -->
S23.2 A home is also stability and control, and no street of numbers counts those. <!-- claims: —; hold: 0.5 -->

=== LIMITS ===

## S24 — Limits and method

S24.1 The rest of the limits are on the card: US only, history, not a forecast, no taxes on gains or on the home, and renters who never skip a month. <!-- claims: —; hold: 0.8 -->

## S25 — Nina's answer (scoreboard on screen, B36)

S25.1 So, back to Nina's question. <!-- claims: — -->
S25.2 With the pile in cash, most of her street was lit; in stocks, about half; over fifteen years, most of it dark. <!-- claims: share_buyer_ahead_cash_10y, share_buyer_ahead_stocks_10y, share_buyer_ahead_stocks_15y -->
S25.3 It's the same street as at the start, read again with the pile in the market. <!-- claims: — -->
S25.4 What no house on this street can show is how long Nina herself will stay. <!-- claims: —; hold: 1.0 -->
S25.5 [thoughtful] Nina's answer: investing the difference made her street a coin flip, and her rent tag tips it. <!-- claims: share_buyer_ahead_stocks_10y, flip_yield_stocks_10y; hold: 1.5 -->
