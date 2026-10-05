# Script — Episode 3 (C2 draft v1, WRITER, 2026-10-04)

Working title (C1, A1): *Money You Won't Touch for 20 Years: Savings Bond or T-Bills?*

Format: `Sxx.n | narration | claim IDs | visual note`. Narration is US English for Eric (`eleven_v3`), generated **per scene** (each scene ≤ ~900 narration characters). Emotion tags sit at the start of the line (**7** in the episode, key beats only). No break tags, no "...", no speed.
Dana is an **ILLUSTRATIVE** character (badge on screen whenever she appears; the name is taste, C3).
Every result shown for a start month before May 2005 carries the fixed screen label **"IF today's guarantee had existed"**; the 17 real-guarantee start months are drawn differently (solid + outlined, own label "REAL guarantee").
Fixed forms used all episode: "52.3 percent, about half" · "93.1 percent, nearly always" · "5.0 percent, almost never" · "58.7 percent" · "58.0 percent" · "87.6 percent". Later recalls use the words only, never the number again.
Machine check: `python3 episodes/ep003/story/check_script.py` (counts below are from it and from the per-scene helper).

---

## S01 — Cold open: Dana, two paths, and the what-if rule · 850 chars, 158 words

S01.1 | [curious] Dana is in her forties, and she has a chunk of savings she has promised herself she won't touch for 20 years. | viewer_age_decade, horizon_years | KEY-1. Dana (ILLUSTRATIVE badge) at a kitchen table at night, laptop open; an envelope on the table reads "Later". No numbers on screen yet.
S01.2 | Right now it sits in 3-month Treasury bills, and every time one comes due, the money rolls into the next. | bill_term_months | Money drops into a short bill; the bill ends; the money hops into the next bill. The "chain of bills" path begins.
S01.3 | Lots of people have money like this, set aside for much later and parked where it earns whatever short-term rates pay. | — | Quick montage of other ILLUSTRATIVE savers' envelopes reading "Later"; back to Dana.
S01.4 | Tonight she has a different tab open: a US savings bond with a much simpler promise, that a bond held for 20 years is worth at least double what was paid. | ctx_guarantee, horizon_years | Second path appears above the chain: one long bar heading to a gate marked "×2 at year 20".
S01.5 | So which path would have left her better off, the promise or the roll? | — | Two paths side by side, Dana between them. Hold ≥ 1 s.
S01.6 | One catch before we look back: the doubling promise in its current form only began with bonds issued in May 2005, and earlier bonds came with different terms. | ctx_guarantee, guarantee_from, ctx_hypothetical | KEY-2. A long timeline from the 1930s to today slides in under the paths; a short solid segment starting "May 2005" lights up.
S01.7 | So for every year before that, we simply pretend today's promise already existed, and you'll see that marked each time it applies. | ctx_hypothetical | Everything left of May 2005 gets a hatched wash + the fixed label "IF today's guarantee had existed". This label stays on every pre-2005 result for the whole episode.

## S02 — The promise of the episode, and the bond's rule · 881 chars, 167 words

S02.1 | By the end, you'll know how often history let the roll beat double, when it fell short, and roughly where the line sits that your own 20 years would have to clear. | horizon_years | Title card (A1). Small tag "US only".
S02.2 | First, the bond. | — | The gate path comes forward.
S02.3 | It's a Series EE savings bond, sold by the US Treasury itself. | — | Plain bond icon, "Series EE".
S02.4 | For bonds issued May to October 2026, it earns a fixed 2.40 percent a year, and the rate for new bonds is reset every May and November. | ctx_ee_rate | On screen: "2.40% fixed" / "for bonds issued May to October 2026" (two lines, ≥ 40 px). Calendar ticks May · Nov.
S02.5 | That rate alone would not double the money in 20 years, so at the 20-year mark the Treasury tops the bond up to at least double. | ctx_ee_rate, ctx_guarantee, horizon_years | The bar grows slowly, stops short of the gate, then a top-up block snaps it to "×2".
S02.6 | The promise, as written, covers bonds held electronically, which is how the Treasury sells them now. | ctx_guarantee | Small tag "electronic bonds".
S02.7 | Spread over those 20 years, that doubling can also be written as one steady yearly rate, shown here on the gate. | horizon_years | Label on the gate, screen only and never spoken: "= 3.53% a year, compounded yearly" (screen claim: doubling_rate_pct_per_year).
S02.8 | And the double only arrives at 20 years: a bond cashed earlier earns just its fixed rate, and one cashed before five years also gives up 3 months of interest. | ctx_penalty, ctx_guarantee, horizon_years | The gate opens only at the end; earlier exits are side doors with a smaller bar.

## S03 — The bill roll, and why today's rate doesn't settle it · 854 chars, 162 words

S03.1 | The T-bill path works the other way around: it makes no promise past three months. | bill_term_months | The chain of bills: links of different heights; only the first link is visible.
S03.2 | A bill is a short loan to the government: the buyer pays a bit less than the face amount and gets the full amount back when it comes due. | bill_term_months | One link drawn as a coin going in slightly smaller and coming out full size.
S03.3 | Over 20 years the money rolls through 80 bills, each paying whatever rate the market sets at the time. | bills_per_horizon, horizon_months, horizon_years | The chain extends to 80 links; links after the first are grey with "?".
S03.4 | In August 2026, the 3-month bill paid 3.72 percent. | tb3ms_latest_pct, tb3ms_latest_month | Link 1 gets a height: "3.72% · Aug 2026".
S03.5 | [thoughtful] It's tempting to set that next to the bond's doubling rate and call it settled. | tb3ms_latest_pct | KEY-3. The 3.72 link slides toward the gate (gate number not re-shown)… a "≠" appears with two lines: "measured differently" / "one month, not 20 years". The two rates are never shown together without this note.
S03.6 | But these rates aren't measured the same way, and bill rates are quoted on a scale where the doubling line sits a little lower. | — | The gate's line is re-drawn on the bill-rate scale, nudged down a little; no new number.
S03.7 | The bigger problem is time: that rate covers one bill, and the roll lives on 80 of them. | bills_per_horizon | Link 1 lit, 79 grey links.
S03.8 | What decides the race is the bill rate across all 20 years, and that is exactly what nobody knows in advance, us included. | horizon_years | Grey links stay grey; no forecast curve is drawn.
S03.9 | So instead of guessing, we went back and replayed history. | — | The timeline from S01 returns with the hatched pre-2005 label.

## S04 — The replay · 785 chars, 147 words

S04.1 | We took the actual 3-month bill rate for every month since 1934 and started a 20-year roll in each month from January 1934 to September 2006, the last start whose 20 years are complete. | first_start, last_start, horizon_years, latest_window_end, bill_term_months | One chain slides along the timeline from its start month; then the next start, and the next.
S04.2 | Each time a bill comes due, the money, interest and all, goes into the next bill at that month's rate. | bill_term_months | The chain grows link by link, each link's height set by that month's rate.
S04.3 | Each start is a saver like Dana putting money in and leaving it alone, and the results swing hard. | starts | Many small chains begin stacking; hatched label on.
S04.4 | A saver who started in May 1972 ended with 4.612 times the money; one who started in January 1934 ended with just 1.129 times. | max_tbill_multiple_20y, max_start, min_tbill_multiple_20y, min_start, ctx_hypothetical | New symbol "finish-line swarm" introduced: each finished chain becomes one dot on a horizontal money-multiple axis with a fixed "×2" gate. The two extremes drop first, far right and far left, labels "May 1972 · ×4.612" and "Jan 1934 · ×1.129" + hatched label.
S04.5 | Across all the start months there are 873 of these rolls. | starts | Counter "873 start months"; dots begin to rain onto the axis.
S04.6 | They overlap a lot, so together they amount to a few long stretches of history, not 873 separate tries. | starts, nonoverlap_periods | Overlapping chains drawn as long bands under the axis.
S04.7 | For each one there's a single question: did the roll end above double? US only, and history, not a forecast. | ctx_hypothetical | Gate glows; dots right of it vs left of it. On screen: "US only · history, not a forecast".

## S05 — The answer, and the only real-guarantee starts · 745 chars, 138 words

S05.1 | Across all of them, the roll ended above double 52.3 percent of the time, about half. | share_tbills_above_double_pct, starts, ctx_hypothetical | KEY-4. All 873 dots settled; about half right of the gate. "52.3%" + hatched label.
S05.2 | But for starts from 1950 to 1989 it was 93.1 percent, nearly always, and for starts from 1990 on, just 5.0 percent, almost never. | share_above_double_1950_1989_pct, share_tbills_above_double_starts_since_1990_pct, mid_from, mid_to, since_1990_from | Swarm splits into three era rows. Middle row piles right of the gate, bottom row piles left; "93.1%" and "5.0%" next to their rows.
S05.3 | [surprised] Starts from 1934 to 1949 never got there at all, so about half is really separate eras stitched together. | share_above_double_1934_1949_pct, early_from, early_to, share_tbills_above_double_pct | Top row all left of the gate; "0.0%" on screen only.
S05.4 | For a saver in Dana's chair, the decade they happened to start in made almost all the difference. | share_above_double_1950_1989_pct, share_tbills_above_double_starts_since_1990_pct | Era rows glow in turn; no new numbers.
S05.5 | [serious] Now, the only starts where the promise was real rather than pretend: the 17 months from May 2005 to September 2006. | starts_with_guarantee, guarantee_from, last_start | KEY-5. The last 17 dots of the bottom row turn solid + outlined, label "REAL guarantee". "52.3% overall" stays in the corner through S05.7 (P1, §6.6 after REVIEWER: both labels on screen together with "0 of 17").
S05.6 | Not one of those 17 rolls reached double; they ended between 1.378 and 1.388 times the money. | share_above_double_guarantee_starts_pct, min_multiple_guarantee_starts, max_multiple_guarantee_starts, starts_with_guarantee | Tight cluster of 17 solid dots left of the gate: "0 of 17" and "×1.378 to ×1.388"; tag "small sample · one era" appears on the cluster now (P1, §6.6).
S05.7 | But that is a small sample from a single era, so it shows what happened once, not what a guarantee does in general. | starts_with_guarantee, share_tbills_above_double_pct | Tag "small sample · one era" stays on the cluster; "52.3% overall" stays in the corner. Hold ≥ 1 s.

## S06 — What separated the eras · 604 chars, 117 words

S06.1 | What separated those eras was the path bill rates took after each start. | — | Swarm rows stay, small.
S06.2 | For starts from 1990 on, the average bill rate over the following 20 years ended below the rate in the starting month 87.6 percent of the time. | share_since_1990_avg_below_start_pct, since_1990_from, horizon_years | For one start: a "first month" marker, then a "20-year average" marker landing below it; quick repeats across starts; "87.6%".
S06.3 | When the rate starts high and drifts down, the average sinks below where it began, and the roll ends up earning less than its first bill suggested. | — | The chain's link heights step down over time; the average marker sinks below link 1.
S06.4 | In other words, the rate on the day a roll begins has been a poor guide to the decades that follow. | — | Link 1 of the chain next to the average of all 80 links: they don't match.
S06.5 | The early eras just ran the other way more often. | — | Middle row of the swarm pulses once.
S06.6 | That is not a reason to pick either path; it is what history did with this pair of rules. | — | Counterweight on screen: "Not a pick. Real rates, what-if bond." Hold ≥ 1 s at the end state.

## S07 — Double is a promise about dollars · 696 chars, 122 words

S07.1 | [thoughtful] There's something else double never promised: what the money will buy. | ctx_guarantee | KEY-6. New symbol "price shadow": the ×2 bar, and behind it a ghost bar = what the original money bought, growing with consumer prices over the same years.
S07.2 | Over 20 years prices rise, sometimes slowly and sometimes fast. | horizon_years | The shadow bar grows at different speeds in two quick examples (no numbers).
S07.3 | To check it, we compared each doubled amount with how far consumer prices rose over the same 20 years. | real_windows, horizon_years | Shadow grows start by start; bar vs shadow.
S07.4 | The doubled amount kept its buying power in 58.7 percent of starts. | share_double_beat_prices_pct, real_windows, ctx_hypothetical | Counter of bars ending above their shadow: "58.7%". Hatched label.
S07.5 | The worst start, January 1966, ended with a double that bought only 58.0 percent of what the original money had bought. | worst_real_value_double_pct, worst_real_start, ctx_hypothetical | Zoom on Jan 1966: shadow towers over the bar; "58.0% of the original buying power".
S07.6 | For Dana's savings, a start like that would mean twice the dollars buying only a little more than half of what the original sum did. | worst_real_value_double_pct, worst_real_start, ctx_guarantee | Dana (ILLUSTRATIVE) holding a doubled stack that fits into a shopping bag barely more than half full. No new number.
S07.7 | So double is a promise about dollars, not about groceries, and the bill roll lives with the same prices, which this replay doesn't score. | — | Both paths under one price shadow; small note "bill roll: not scored against prices".

## S08 — The line your own 20 years would have to clear · 831 chars, 159 words

S08.1 | [warm] So where would your own 20 years fall? | horizon_years | KEY-7. A plain bill-rate scale, horizontal.
S08.2 | Here is a line to measure them against. | — | Empty scale; a gate line fades in, unlabelled for a beat.
S08.3 | Averaged over every month since 1934, the 3-month bill paid 3.42 percent. | mean_tb3ms_all_pct, first_start, tb3ms_latest_month | Marker "3.42% · average since 1934".
S08.4 | For a roll to end above double, the bill rate has to average about 3.47 percent a year across all 20 years, which is the bond's doubling measured the way bill rates are quoted, so the long-run average sat just under the line. | steady_breakeven_tb3ms_pct, doubling_rate_pct_per_year, mean_tb3ms_all_pct, horizon_years | Gate label on the bill-rate scale: "3.47% · bill-rate basis = ×2 in 20 years", just right of the 3.42 marker. If 3.53 is shown, it sits on a separate small tag "3.53% = same ×2, compounded yearly", never on this scale. Swarm in miniature: dots either side.
S08.5 | The middle roll of all 873 ended at 2.097 times the money, barely over the line. | median_tbill_multiple_20y, starts, ctx_hypothetical | One dot in the middle of the swarm highlighted at the gate: "middle roll ×2.097".
S08.6 | For money like Dana's, the question isn't the rate on the day it starts; it's whether the bill rate averages above that line over all 80 bills, a rule that matched the result in every one of the 873 starts. | bills_per_horizon, steady_breakeven_tb3ms_pct, share_avg_rule_agrees_pct, starts, ctx_hypothetical | The 80-link chain collapses into one average marker that slides to each side of the gate in turn; it does not stop on either side.
S08.7 | Nobody can say where that average will land, and today's rate can't either. | — | Today's rate as one small dot labelled "one month", fading.
S08.8 | The line doesn't say which to pick; it says what the roll has to do to beat the promise. | — | Counterweight on screen: "What the roll must do. Not a pick."

## S09 — How we know this (method card, V7) · 118 chars, 22 words

S09.1 | How the replay was built, and what it leaves out, like taxes and purchase limits, is on screen and in the description. | nonoverlap_periods, near_double_starts, near_double_band_pct, guarantee_from, ctx_hypothetical, bill_term_months, horizon_years | V7 card "How we know this" (≥ 40 px; hold long enough to read every line): (1) "Monthly average 3-month bill rate (discount basis) ÷ 12, compounded monthly" (2) "Taxes ignored: bills taxed federally each year; EE tax-deferred; both state-tax exempt" (3) "Full 20-year hold; purchase limits ignored" (4) "Overlapping windows ≈ 4 separate 20-year periods" (5) "6 start months end within 0.5% of double" (6) "Before May 2005: IF today's guarantee had existed". Source lines: "Federal Reserve Board (H.15) via FRED" · "U.S. Bureau of Labor Statistics via FRED".

## S10 — Back to Dana · 679 chars, 133 words

S10.1 | [warm] Back at Dana's table, the two paths look the same as they did at the start: a promise of double, or a roll with no promise past three months. | ctx_guarantee, bill_term_months | Dana (ILLUSTRATIVE) between the gate path and the chain path, as in S01.
S10.2 | History doesn't choose for her. | — | Hold on Dana; neither path highlighted.
S10.3 | It doesn't know what she needs the money for, or what else she owns, and it can't see the 20 years ahead of her. | horizon_years | Dana's envelope "Later"; grey links.
S10.4 | What it shows is a roll that beat double about half the time, nearly always for starts from 1950 to 1989 and almost never for starts since 1990, with today's promise imagined for every start before May 2005. | share_tbills_above_double_pct, share_above_double_1950_1989_pct, share_tbills_above_double_starts_since_1990_pct, ctx_hypothetical, guarantee_from | Recall in words only (numbers not repeated); swarm rows small behind Dana, hatched label on.
S10.5 | It shows that double was a promise about dollars, not about what they buy. | ctx_guarantee | Price shadow returns, small.
S10.6 | And it shows a line that depends on a path of rates nobody can see yet. | — | Grey future links of the chain.
S10.7 | US only, and history, not a forecast. | — | On screen: "US only · history, not a forecast".

## S11 — End screen (15–20 s) · 93 chars, 16 words

S11.1 | That's the replay. The next episode, another question about money and time, is on screen now. | — | End-screen layout (next-episode slot + channel slot); music carries the remaining time. No imperatives.
