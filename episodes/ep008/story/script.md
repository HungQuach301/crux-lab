# Script — Episode 8 (format `lab`, C2 v1, WRITER, 2026-10-13)

(header written after the checker passes)

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
