# Episode 2 — Script v1 (C2, WRITER, 2026-10-01)

Working title (C1, A1): *Need Private Grad Loans? Variable vs Fixed Through History*

Format: `id | narration (US English) | claim IDs (numbers.md) | picture note`. One sentence per line. Emotion tags (eleven_v3, Eric) are written inline at the start of the line they colour; 7 in total. No break/pause tags, no "...", no speed. Voice generated **per scene**.

Period labels "1954 to 1980" / "1981 on" are the model's split (`n_early`, `n_late`). Numbers in narration are written as the `Hiển thị` column or the `Lời (gợi ý)` column of `numbers.md`. Every loan number is ILLUSTRATIVE (badge on screen whenever Leah's loan is shown). Model limits are spoken in S04/S08 and repeated on the method card (description + S04 lower third).

Leah is an illustrative character (name is a taste call for the owner at C2).

---

## S01 — Cold open (~0:00–0:30)

S01.1 | Starting July 1, 2026, a new graduate student in the US can no longer borrow a federal Grad PLUS loan. | ctx_plus_end | Calendar page flips to July 1, 2026; a federal loan form slides into a drawer that closes.
S01.2 | Picture Leah, weeks before her first spring term, with two private loan offers open on her laptop. | — | Night desk, laptop glow, two offer cards side by side. ILLUSTRATIVE badge.
S01.3 | One rate is fixed at 9%; the other is variable, and it starts lower, at 7.5%. | fixed_rate, var_start | Left card: a flat steel bar, level. Right card: a lower bar resting on water, gently bobbing.
S01.4 | [curious] But a variable rate can move, so how much lower does it have to start than a fixed one before that risk has been worth it? | — | The water swells and falls; the bar rides it. The gap between the two bars glows; a question mark forms in the gap. Title card. (KEY-1)

## S02 — What changed, and what Leah is weighing (~0:30–2:25)

S02.1 | First, why Leah is looking at private loans at all. | — | Back to the drawer from S01.1.
S02.2 | Graduate students who needed more than the basic federal loan used to have a second federal loan, Grad PLUS. | — | Two federal forms stacked; the top one labelled PLUS.
S02.3 | For new borrowers, that option ended on July 1, 2026. | ctx_plus_end | The PLUS form slides into the drawer; drawer shuts.
S02.4 | Students already enrolled and borrowing before July 2026 keep it for up to 3 more years, or until their program ends if that comes sooner. | ctx_plus_exception | A second student figure keeps a PLUS form; small hourglass beside it.
S02.5 | A new student like Leah can still borrow the basic federal loan, a Direct Unsubsidized loan, up to $20,500 a year and $100,000 total. | ctx_unsub_annual, ctx_unsub_aggregate | One federal form with two big figures, one at a time.
S02.6 | Professional programs, like medicine or law, have higher limits, but the same question can come up there. | — | Brief glance at a second desk; no numbers on screen.
S02.7 | When a program costs more than that, after grants and other aid, the rest can come from private lenders. | — | A cost bar taller than the federal block; the remaining slice is filled by a private-lender block.
S02.8 | That's where Leah's two offers come from. | — | Private block splits into the two offer cards from S01.
S02.9 | Both are for $50,000 over 10 years, illustrative numbers, not a real lender's offer. | loan, term | Same $50,000 stack under each card; "ILLUSTRATIVE" badge pulses once.
S02.10 | The first variable payment is $593.51 a month, and the fixed payment is $633.38. | var_first_payment, fixed_payment | Two envelopes; the variable envelope is visibly thinner.
S02.11 | Private lenders usually offer these two kinds of rate. | — | Two cards again.
S02.12 | A fixed rate is set on day one and never changes, so the monthly payment never changes either. | — | Flat bar; a row of identical envelopes.
S02.13 | A variable rate is tied to a market interest rate that moves every month. | — | Water level under the variable bar.
S02.14 | When market rates rise, the variable rate and the payment rise too; when they fall, both fall. | — | Water rises, bar and envelopes thicken; water falls, both thin.
S02.15 | That's the trade: a variable rate can start lower, but nobody knows where it goes next. | — | Water surface goes foggy ahead of the bar.
S02.16 | The distance between the two starting rates is what this video calls the head start. | — | A bracket snaps between the two bar heights at the start; the bracket fills with colour. (KEY-2)
S02.17 | Leah's fixed rate is 9% and her variable rate starts at 7.5%, so her head start is 1.5 points. | fixed_rate, var_start, gap_start | Bracket labelled "1.5 points".
S02.18 | Real offers differ, so a head start can be bigger, smaller, zero, or even negative, with the variable rate starting higher. | — | Bracket stretches, shrinks, closes, then flips with the variable bar above the fixed one.

## S03 — The promise (~2:25–3:05)

S03.1 | So this video replays Leah's illustrative loan through US interest rates going back to January 1954. | first_start | Leah's two bars lift off the desk onto the long ridge.
S03.2 | How often did a variable rate with her 1.5-point head start end up costing more in total interest than the 9% fixed loan, and how bad did the worst stretch get? | gap_start, fixed_rate | Two coin piles (total interest) side by side, heights unknown, covered.
S03.3 | Then it moves the head start, from 1 point above the fixed rate to 3 points below, to see where the history changes. | spreadm1_share, spread3_share | The head-start bracket slides along a ruler from negative to wide.
S03.4 | [warm] By the end there's a line that any real offer can be held up against, including yours. | — | A ruler line lies across the screen; a blank offer card floats toward it.
S03.5 | One thing first: this is history, not a forecast. | — | Ridge behind; the space to the right of today is empty.

## S04 — How the replay works (~3:05–4:20)

S04.1 | Here's how the replay works. | — | Workbench view of the ridge.
S04.2 | Real private variable rates follow an index called SOFR, but SOFR is only a few years old. | — | A short ribbon labelled SOFR next to the long ridge.
S04.3 | So the replay uses a stand-in with a far longer record, the rate on 3-month US Treasury bills. | — | The long ridge brightens: T-bill.
S04.4 | In August 2026, that rate was 3.72%. | index_today | Marker at the right end of the ridge.
S04.5 | Leah's variable rate starts at 7.5%, which is that rate plus a fixed add-on of 3.78 points. | var_start, index_today, margin | Bar = water level + a fixed block on top.
S04.6 | From there, each month her rate moves up or down by exactly as much as the Treasury bill rate moved in the same month of history. | — | The ridge's month-to-month steps are copied onto the bar's path.
S04.7 | The first replay starts the loan in January 1954 and runs it for 10 years, 120 monthly payments, beginning right away, with no grace period, no fees and no rate cap. | first_start, term | A 10-year frame lands on the left end of the ridge. Method lower third: "T-bill stand-in · no cap · no grace period · no fees" (description card also notes: the index is never allowed below zero).
S04.8 | It adds up the interest and sets it next to the 9% fixed loan over the same 10 years. | fixed_rate, term | Two coin piles grow inside the frame.
S04.9 | Then it starts again one month later, and again, all the way to September 2016, the last start with a full 10 years of data. | last_start, term | The frame steps right one notch at a time, speeding up. (KEY-3)
S04.10 | That's 753 starting months, each one a 10-year stretch of real rate history. | n_starts, term | Each stop drops one token into a long tray below the ridge.
S04.11 | The stretches overlap, so they are not 753 independent tries, and they are US rates only. | n_starts | Neighbouring frames overlap, shared months shaded; US outline stamped on the ridge's corner.

## S05 — The part that looks like bad news (~4:20–5:30)

S05.1 | [curious] The first thing the replay shows looks like bad news for the variable loan. | — | Tokens in the tray flip over one by one.
S05.2 | In about 3 in 4 of those stretches, Leah's variable rate climbed above 9% at some point. | share_rate_above_fixed, fixed_rate | Per stretch, the bar's path pokes above the fixed line; those tokens flash red at the poke.
S05.3 | In more than half, her monthly payment rose above the fixed payment of $633.38. | share_payment_above_fixed, fixed_payment | Envelopes thicken past the fixed envelope.
S05.4 | In one stretch, the payment reached $863.36 a month. | max_payment | One envelope swells far past the rest.
S05.5 | It would be easy to guess the variable loan usually cost more in the end, and it didn't. | — | Red flashes everywhere, then stop.
S05.6 | Counting every dollar of interest over the full 10 years, the variable loan cost more than the 9% fixed loan in about 1 in 7 stretches. | term, fixed_rate, share_all | Tokens settle: about one in seven stays red. (KEY-4)
S05.7 | That overall share hides two very different histories: for loans starting from 1954 to 1980 it was more than 1 in 4, and for loans starting from 1981 on it was about 1 in 30. | share_early, share_late, n_early, n_late | Tray splits into two bins; left bin visibly redder.
S05.8 | And in the worst stretch, which began in April 1977, the variable loan cost $11,219 more. | worst_start, worst_diff | One left-bin token glows dark.
S05.9 | So how can a rate climb above 9% that often, yet cost more in total so much less often? | fixed_rate | Red pokes and the settled tray shown together.

## S06 — Why both things are true (~5:30–6:15)

S06.1 | The answer is the head start, and when it does its work. | — | Head-start bracket returns.
S06.2 | Every month the variable rate sits below 9%, Leah pays less interest than she would on the fixed loan, and that saving piles up. | fixed_rate | Each early month drops a coin into a "cushion" jar beside the loan. (KEY-5)
S06.3 | It piles up fastest at the start, when she owes the most, so every point of rate is charged on the biggest balance. | — | The debt stack is tallest at the left; coins drop fastest there.
S06.4 | When the rate later climbs above 9%, the extra interest has to drain that pile before the variable loan has cost more overall. | fixed_rate | Rate pokes above the fixed line; coins leave the jar.
S06.5 | A short jump above 9% dents the pile, but emptying it needs rates that rise early and stay high for years. | fixed_rate | Two runs: a brief spike barely dents the jar; a long early climb empties it.
S06.6 | That kind of history happened mostly in one part of the record. | — | Camera pulls back to the whole ridge.

## S07 — Two kinds of history (~6:15–7:05)

S07.1 | From 1954 to 1980, the Treasury bill rate mostly climbed, in waves, as inflation built up. | n_early | Left half of the ridge rises in waves.
S07.2 | For loans started in those years, the variable loan cost more in total interest than the 9% fixed loan in 28.4% of stretches, more than 1 in 4. | fixed_rate, share_early | Left bin: red tokens counted.
S07.3 | Then the Treasury bill rate peaked at 16.30% in May 1981, and over the following decades it mostly drifted down, with big swings. | tb_peak | Ridge summit marked; right half slopes down with swings.
S07.4 | For starts from 1981 on, the variable loan cost more in 3.5% of stretches, about 1 in 30. | share_late, n_late | Right bin: very few red tokens.
S07.5 | The best stretch began in August 1981, right near that peak, and cost $15,295 less in interest than the fixed loan. | best_start, best_diff | One right-bin token glows bright; its jar overflows.
S07.6 | Across all 753 stretches, the middle one, the median, cost $3,832 less. | n_starts, median_diff | Tokens line up in order; the middle one lifts.
S07.7 | But the worst stretch, $11,219 more, came from the first era, in April 1977. | worst_diff, worst_start | Camera swings back to the dark token in the left bin.

## S08 — The worst stretch (~7:05–7:55)

S08.1 | [serious] Here is Leah's same loan, started in April 1977, the worst stretch in the replay. | worst_start | The 10-year frame lands on 1977; Leah's desk reappears inside it. (KEY-6)
S08.2 | It begins at 7.5%, like every replay, and for a while she's ahead. | var_start | Cushion jar fills a little.
S08.3 | Then inflation pushes interest rates up year after year, and her rate follows. | — | The water rises steadily; the bar rides up.
S08.4 | At its highest, her variable rate reaches 19.3%. | worst_peak_rate | Bar far above the fixed line; the cushion jar empties and extra coins stack on her pile.
S08.5 | Over the full 10 years, the fixed loan charges $26,005 in interest. | term, fixed_int | Fixed coin pile, solid.
S08.6 | Leah's variable loan charges $11,219 more than that. | worst_diff | Variable pile = fixed pile + an extra block.
S08.7 | That's 43% on top of the fixed loan's interest. | worst_share_of_fixed | The extra block measured against the fixed pile: a bit under half its height.
S08.8 | Real variable loans have a rate cap and this replay has none; a low enough cap would have shrunk this worst case. | — | A ceiling line drawn above the bar, then lowered; the extra block trims. Method lower third.
S08.9 | The worst stretch belongs to the era when more than 1 in 4 stretches cost more, not the era when about 1 in 30 did. | share_early, share_late | Dark token sits in the redder left bin.

## S09 — Moving the head start (~7:55–9:45)

S09.1 | So far, every result has been about one pair, 7.5% against 9%, but a real offer has its own head start. | var_start, fixed_rate | Leah's two bars, head-start bracket; Blank offer cards float in, each with a different bracket.
S09.2 | So the replay ran again, holding the fixed rate at 9% and moving only the variable start. | fixed_rate | A slider under the bracket; the fixed bar is pinned.
S09.3 | With no head start at all, both loans begin at 9%. | spread0_share, fixed_rate | Bracket closes to nothing. (KEY-7 begins)
S09.4 | Then the variable loan cost more in total interest in 57.9% of stretches. | spread0_share, fixed_rate | Two bins fill heavily red.
S09.5 | That's 79.0% of starts from 1954 to 1980 and 42.0% from 1981 on, and the worst stretch cost $16,566 more. | gap00_early, gap00_late, gap00_worst, n_early, n_late | Left bin mostly red, right bin less; worst block tall.
S09.6 | With a 1-point head start, it cost more in 31.3% of stretches. | spread1_share | Slider moves; red tokens fade out of both bins.
S09.7 | That's 54.9% of the 1954-to-1980 starts and 13.5% from 1981 on, with the worst at $12,983 more. | gap10_early, gap10_late, gap10_worst, n_early, n_late, fixed_rate | Right bin thins quickly, left bin slowly; worst block shrinks.
S09.8 | Leah's 1.5 points gives the result from before: about 1 in 7 overall, more than 1 in 4 before 1981, about 1 in 30 after, $11,219 at worst. | gap_start, spread15_share, share_all, share_early, share_late, worst_diff, n_late | Leah's card clicks into place on the slider.
S09.9 | At a 2-point head start, none of the stretches starting in 1981 or later cost more. | gap20_late, n_late, spread2_share | Right bin goes fully clear.
S09.10 | But 20.4% of the 1954-to-1980 starts still did, 8.8% of all stretches, and the worst still cost $9,472 more. | gap20_early, spread2_share, gap20_worst, n_early | Left bin keeps a red layer.
S09.11 | [thoughtful] Even with a 3-point head start, 10.5% of the 1954-to-1980 starts cost more, none from 1981 on, 4.5% overall, and the worst was still $6,033 more. | gap30_early, gap30_late, spread3_share, gap30_worst, n_early, n_late | Slider at the far end; left bin still holds a thin red layer; worst block small but present.
S09.12 | The head start can also run the other way, with the variable rate starting 1 point above the fixed one. | spreadm1_share | Slider passes zero; the variable bar rises above the fixed bar.
S09.13 | Then it cost more in 72.9% of stretches: 92.9% of the 1954-to-1980 starts, 57.8% from 1981 on, and the worst cost $20,217 more. | spreadm1_share, gapm10_early, gapm10_late, gapm10_worst, n_early, n_late, fixed_rate | Both bins almost fully red; worst block tallest.
S09.14 | Lined up, those points make a slope: a bigger head start, fewer costlier stretches, a smaller worst case. | — | Slider sweeps end to end; the bins and the worst block move together.
S09.15 | But across every head start tested, the 1954-to-1980 starts never fell to zero. | gapm10_early, gapm05_early, gap00_early, gap05_early, gap10_early, gap15_early, gap20_early, gap25_early, gap30_early, n_early | Left bin's red layer never clears, even at the far end.

## S10 — Where an offer falls (~9:45–10:45)

S10.1 | So how much lower does a variable rate have to start before the risk has been worth it, in history? | — | The question from S01.8 returns over the ruler.
S10.2 | For stretches that began in 1981 or later, a 2-point head start was enough in every one. | gap20_late, n_late, spread2_share | Right bin, clear, at the 2-point mark.
S10.3 | For stretches that began from 1954 to 1980, even 3 points was not: 10.5% still cost more, and the worst by $6,033. | gap30_early, gap30_worst, n_early | Left bin at the 3-point mark, thin red layer.
S10.4 | Which kind of history comes next is something no replay can show. | — | Ridge ends at today; the space to the right stays empty.
S10.5 | [warm] Leah's offer sits at 1.5 points on that line, and Leah is illustrative. | gap_start | Leah's card on the ruler, ILLUSTRATIVE badge.
S10.6 | A real offer has its own two rates, its own head start and its own place on the line. | — | Blank offer card hovers above the ruler, not placed.
S10.7 | It also has what this replay leaves out: a real index, a rate cap, a grace period, fees, and the borrower's own budget. | — | Five plain objects appear around the card (index ribbon, ceiling, hourglass, receipt, wallet).
S10.8 | The line shows how each head start held up across US rate history since January 1954. | first_start | Full ruler with both bins at every mark.
S10.9 | [calm] History, not a forecast. | — | Ridge fades; empty space to the right of today.

## S11 — End screen tail (~10:45–11:03, 15–20 s)

S11.1 | Every assumption behind this replay is listed in the description. | — | End-screen layout; ridge as a quiet background; music carries.
S11.2 | Another replay from this channel is on screen now. | — | Video element slot; remaining ~12 s music only, no narration.

---

### Totals
Narration: 1,636 words (S01–S11, tags excluded) ≈ 10:54 at 150 wpm; plus scene gaps and ~12 s music-only end-screen tail ≈ 11:10–11:20 total.
Cold open S01 = 79 words ≈ 30 s (context line before the character, per G-009; longer than the 15 s S15 reference, same kind of exemption as Ep 1's 20 s; flagged for the owner).

### Tag map (7)
S01.4 `[curious]` · S03.4 `[warm]` · S05.1 `[curious]` · S08.1 `[serious]` · S09.11 `[thoughtful]` · S10.5 `[warm]` · S10.9 `[calm]`
