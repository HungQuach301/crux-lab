# Episode 2 — Script v2 (C2, WRITER, 2026-10-01)

Working title (C1, A1): *Need Private Grad Loans? Variable vs Fixed Through History*. v1 kept as `script-v1.md`; changes in `changes-v2.md`.

Format: `id | narration (US English) | claim IDs (numbers.md) | picture note`. One sentence per line. Emotion tags (eleven_v3, Eric) sit at the start of the line they colour; 6 in total. No break/pause tags, no "...", no speed. Voice generated **per scene**.

Numbers are written as the `Hiển thị` or `Lời (gợi ý)` column of `numbers.md`. Period labels "1954 to 1980" / "1981 on" are the model's split (`n_early`, `n_late`). Every loan number is ILLUSTRATIVE (badge on screen whenever Leah's loan is shown).

**Visual system (see `beats.md`):** the rate is ONE object, the *ridge* (the T-bill line through history); Leah's variable rate is a *bead* riding a track shaped like the ridge; the fixed rate is a level *rail* at 9%. Rate above 9% = the rail segment lights **amber** where the bead is over it. Costlier in total = a **red token**. Interest paid = **coin piles** (coins mean interest paid, nothing else). The early saving = a **green jar of liquid** (the cushion). Results fall into **two bins sitting directly under the two halves of the ridge** (left under 1954–1980, right under 1981 on).

Cold open: default **CO-A** below; alternative CO-B in `cold-open-options.md` (owner's taste call).

---

## S01 — Cold open, CO-A (~0:00–0:24)

S01.1 | From July 1, 2026, new graduate students in the US can no longer borrow federal Grad PLUS loans. | ctx_plus_end | Calendar leaf turns to July 1, 2026; a federal form slides into a drawer that shuts.
S01.2 | Leah, an illustrative student weeks from her first spring term, has two private offers on her laptop: 9% fixed, or variable starting lower, at 7.5%. | fixed_rate, var_start | Night desk, laptop. On screen: a level rail (fixed) and, just below it, a bead on a short wavy track (variable). ILLUSTRATIVE badge.
S01.3 | [curious] How much lower does a variable rate have to start before that risk has been worth it? | — | The track ahead of the bead wavers up and down; the gap between bead and rail glows. Title card. (KEY-1)

## S02 — Leah's situation (~0:24–1:53)

S02.1 | Students already enrolled and borrowing before July 2026 keep Grad PLUS for up to 3 more academic years, or for the time left in their program if that is shorter. | ctx_plus_exception | A second student keeps a PLUS form; an hourglass beside it.
S02.2 | New students like Leah still have the basic federal loan, a Direct Unsubsidized loan, up to $20,500 a year and $100,000 total, with higher limits in professional programs like medicine or law. | ctx_unsub_annual, ctx_unsub_aggregate | One federal form; one big figure at a time.
S02.3 | When a program costs more than that after other aid, the rest can come from a private lender, and that's where Leah's two offers come from. | — | A cost bar taller than the federal block; the remaining slice becomes a private-lender block that splits into the two offers.
S02.4 | Same lender, same amount, two kinds of rate. | — | The two offers side by side.
S02.5 | Both are for $50,000 over 10 years, illustrative numbers, not a real lender's offer. | loan, term | $50,000 stack under each offer; ILLUSTRATIVE badge pulses once.
S02.6 | The variable loan's first payment is $593.51, about $40 less a month than the fixed $633.38. | var_first_payment, first_payment_gap, fixed_payment | Two envelopes; the variable one visibly thinner.
S02.7 | A fixed rate never changes, so neither does the payment. | — | The level rail; a row of identical envelopes.
S02.8 | A variable rate follows a market interest rate, so the rate and the payment rise and fall with it, and nobody knows where it goes next. | — | The bead rides its track up and down; envelopes thicken and thin; the track ahead fades out.
S02.9 | The distance between the two starting rates is what this video calls the head start. | — | A coloured bracket snaps between rail and bead at the start line. (KEY-2)
S02.10 | Leah's fixed rate is 9% and her variable rate starts at 7.5%, so her head start is 1.5 points. | fixed_rate, var_start, gap_start | Bracket labelled "1.5 points".
S02.11 | A point here means one percentage point of interest. | — | —
S02.12 | Real offers differ: a head start can be bigger, smaller, zero, or negative, with the variable rate starting higher. | — | Bracket widens, narrows, closes, then flips with the bead starting above the rail.

## S03 — The promise and the contradiction (~1:53–3:04)

S03.1 | This video replays Leah's illustrative loan through every 10-year stretch of US interest rates since January 1954. | first_start, term | The short track stretches left into a long ridge of rate history.
S03.2 | "Worth it" gets one plain meaning here: how often the variable loan cost more in total interest than the 9% fixed loan, and how much more at worst. | fixed_rate | Two coin piles (interest paid), fixed and variable, side by side.
S03.3 | [curious] And the first result looks like a contradiction. | — | —
S03.4 | Leah's variable rate rose above 9% at some point in about 3 in 4 stretches. | share_rate_above_fixed, fixed_rate | Stretch after stretch: the rail lights amber wherever the bead is above it; amber nearly everywhere.
S03.5 | Yet it cost more in total interest in about 1 in 7. | share_all | Tokens drop into the two bins under the ridge; only some turn red.
S03.6 | That's more than 1 in 4 for starts from 1954 to 1980 and about 1 in 30 from 1981 on, and the worst stretch cost $11,219 more. | share_early, share_late, n_early, n_late, worst_diff | Left bin (under the climbing half) clearly redder than the right; one dark token in the left bin. (KEY-4)
S03.7 | Both are true at the same time, and the reason is the key to reading any offer. | — | Amber rail above, red tokens below, held in one frame.
S03.8 | Then the replay moves the head start, from a variable rate 3 points under the fixed rate to one 1 point over it, to see where that history changes. | spread3_share, spreadm1_share | The bracket slides along a ruler.
S03.9 | By the end there's a line that any real offer can be held up against, including yours. | — | A ruler across the screen; a blank offer card floats toward it.
S03.10 | This is history, not a forecast. | — | The ridge ends at today; empty space to its right.

## S04 — How the replay works (~3:04–4:26)

S04.1 | Here's how the replay works. | — | Workbench view of the ridge.
S04.2 | A real variable rate follows the lender's own index, and the replay needs a much longer record than that index has. | — | A short ribbon beside the long ridge.
S04.3 | So it uses a stand-in with a long US record: the rate on 3-month Treasury bills. | — | The long ridge brightens.
S04.4 | In August 2026, that rate was 3.72%, so Leah's 7.5% is that rate plus a fixed 3.78 points. | index_today, var_start, margin | Ridge end marker; the bead's track sits a fixed distance above the ridge.
S04.5 | Each month after that, her rate moves up or down exactly as much as the Treasury bill rate moved in the same month of history. | — | The ridge's month-to-month steps are copied onto the bead's track.
S04.6 | If history would push the index below zero, the replay stops it at zero. | — | The ridge floor drawn as a hard line; the bead's track never dips under it.
S04.7 | The first replay starts her loan in January 1954 and runs it for 10 years, 120 monthly payments. | first_start, term | A 10-year frame lands on the far left of the ridge.
S04.8 | Repayment starts right away, with no grace period, no fees and no rate cap. | — | Method lower third: "T-bill stand-in · no cap · no grace period · no fees" (description card adds: the index is never allowed below zero).
S04.9 | The replay adds up the interest and sets it next to the 9% fixed loan's. | fixed_rate | Two coin piles grow inside the frame.
S04.10 | Then it starts again one month later, and again, up to September 2016, the last start with a full 10 years of data. | last_start, term | The frame steps right notch by notch, speeding up; each stop drops a token straight down into the bin under that part of the ridge. (KEY-3)
S04.11 | Each start month becomes one token, sorted into the bin under the half of history where it began. | — | Tokens fall straight down into the left or right bin.
S04.12 | That's 753 starting months. | n_starts | Both bins full of tokens.
S04.13 | The stretches overlap, so they are not 753 independent tries, and the data is US only. | n_starts | Neighbouring frames overlap, shared months shaded; US outline stamped in the corner.

## S05 — Why both results are true (~4:26–5:20)

S05.1 | So how can both of those results be true? | — | Amber rail and red tokens side by side.
S05.2 | The answer is the head start, and when it does its work. | — | Bracket returns.
S05.3 | Every month the variable rate sits below 9%, Leah pays less interest than on the fixed loan, and that saving builds a cushion. | fixed_rate | A green jar fills while the bead is under the rail. (KEY-5)
S05.4 | The cushion grows fastest at the start, when she owes the most, so every point of rate is charged on the biggest balance. | — | The debt stack is tallest at the left; the jar fills fastest there.
S05.5 | When the rate later climbs above 9%, the extra interest has to use up that cushion before the variable loan has cost more overall. | fixed_rate | Rail lights amber; the jar drains.
S05.6 | A short jump above 9% only dents it; emptying it needs rates that rise early and stay high for years. | fixed_rate | Two runs: a brief amber blip barely lowers the jar; a long early climb drains it dry.
S05.7 | In a stretch where rates drift down, the cushion just keeps growing. | — | Bead sinks under the rail; jar keeps filling.
S05.8 | And that is where the two halves of the record differ. | — | Camera pulls back to the whole ridge with its two bins.

## S06 — Two kinds of history (~5:20–6:06)

S06.1 | From 1954 to 1980, the Treasury bill rate mostly climbed, in waves. | n_early | Left half of the ridge rises in waves above the left bin.
S06.2 | It peaked at 16.3% in May 1981, then mostly drifted down over the following decades, with big swings. | tb_peak | Summit marked; the right half slopes down above the right bin.
S06.3 | Same loan, same head start; the only difference is where in history it began. | — | Two identical beads set on the two halves of the ridge.
S06.4 | Loans started in the climbing years often met rates that rose early and stayed high, and loans started after the peak mostly rode rates down. | — | Frames on the left: bead climbs, jar drains. Frames on the right: bead sinks, jar fills.
S06.5 | The best stretch began in August 1981, near that peak, and cost $15,295 less than the fixed loan. | best_start, best_diff | One right-bin token glows bright; its jar brims.
S06.6 | But across the 1954-to-1980 starts more than 1 in 4 cost more, against about 1 in 30 from 1981 on, and the worst, from April 1977, cost $11,219 more. | share_early, share_late, n_early, n_late, worst_start, worst_diff | Camera swings to the dark token in the left bin.

## S07 — The worst stretch (~6:06–6:52)

S07.1 | [serious] Here is Leah's same loan, started in April 1977. | worst_start | The 10-year frame lands on a steep climbing section of the ridge; Leah's desk appears inside it. (KEY-6)
S07.2 | It begins at 7.5%, like every replay, and for a while her cushion grows. | var_start | Jar fills a little.
S07.3 | Then the Treasury bill rate climbs year after year, and her rate follows it, to 19.3% at its highest. | worst_peak_rate | Bead far above the rail; the rail glows amber for years; the jar drains dry.
S07.4 | The cushion from her first months is soon gone, and every further month above 9% adds to what she owes in interest. | fixed_rate | Jar empty; amber rail; coins keep adding to her pile.
S07.5 | Her payment reaches $863.36 a month, against the fixed $633.38. | max_payment, fixed_payment | Her envelope swells well past the fixed one.
S07.6 | Over 10 years, the fixed loan charges $26,005 in interest. | term, fixed_int | Fixed coin pile.
S07.7 | Leah's variable loan charges $11,219 more than that, 43% on top. | worst_diff, worst_share_of_fixed | Variable pile = fixed pile + an extra block reaching a bit under half its height.
S07.8 | This replay has no rate cap; a real loan's cap, if low enough, would have made this worst case smaller. | — | A ceiling line drawn over the bead, then lowered; the extra block trims.

## S08 — Moving the head start (~6:52–8:13)

S08.1 | So far, every result has been for one pair of rates, 7.5% against 9%. | var_start, fixed_rate | Leah's bracket.
S08.2 | So the replay ran again, holding the fixed rate at 9% and moving only where the variable rate starts. | fixed_rate | A slider under the bracket; the rail pinned. (KEY-7 begins)
S08.3 | Each stop on this slider is a different offer someone could be holding. | — | Offer cards line up along the slider.
S08.4 | With no head start, both loans starting at 9%, the variable loan cost more in 79% of the 1954-to-1980 starts and 42% from 1981 on. | gap00_early, gap00_late, n_early, n_late, fixed_rate | Slider at 0. Both bins heavily red, left more. On screen only: overall "57.9%" (`spread0_share`).
S08.5 | The worst of those stretches cost $16,566 more. | gap00_worst | Extra block on the fixed coin pile, tall.
S08.6 | Leah's 1.5 points brings that to more than 1 in 4 and about 1 in 30, with the worst at $11,219. | gap_start, share_early, share_late, n_early, n_late, worst_diff | Slider passes 1 point (on screen only: "31.3%" `spread1_share`; "54.9% / 13.5% / +$12,983" `gap10_early`, `gap10_late`, `gap10_worst`), then Leah's card clicks in at 1.5 (on screen: "14.2%" `spread15_share`).
S08.7 | At 2 points, none of the starts from 1981 on cost more, but 20.4% of the 1954-to-1980 starts still did, and the worst cost $9,472 more. | gap20_late, gap20_early, n_early, n_late, gap20_worst | Right bin goes fully clear; left bin keeps a red layer. On screen only: "8.8%" (`spread2_share`).
S08.8 | [thoughtful] At 3 points, still none from 1981 on, but 10.5% of the 1954-to-1980 starts cost more, and the worst was $6,033 more. | gap30_late, gap30_early, n_early, n_late, gap30_worst | Slider at the far end; the left bin still holds a thin red layer; small extra block remains. On screen only: "4.5%" (`spread3_share`).
S08.9 | Every stop in between follows the same slope: a bigger head start, fewer costlier stretches, a smaller worst case. | — | Slider sweeps back past zero to −1 (on screen only: "72.9%" `spreadm1_share`; "92.9% / 57.8% / +$20,217" `gapm10_early`, `gapm10_late`, `gapm10_worst`), then forward again; bins and block move together.
S08.10 | At every head start tested, the worst stretch began in April 1977. | gap_worst_start_all | The dark token never leaves the same spot in the left bin.
S08.11 | And for the 1954-to-1980 starts, the share that cost more never fell to zero, even where none of the 1981-on starts did. | min_gap_early, n_early, gap20_late, gap25_late, gap30_late, n_late | Left bin's red layer never clears.

## S09 — The answer, and where an offer falls (~8:13–9:37)

S09.1 | So, back to the question: how much lower does a variable rate have to start before the risk has been worth it? | — | The question from S01.3 over the ruler.
S09.2 | Measured the way this video measures it, how often it cost more in total interest than the 9% fixed loan and how much more at worst, history gives two answers. | fixed_rate | Two bins under the two halves of the ridge.
S09.3 | For starts from 1981 on, none cost more once the head start reached 2 points. | gap20_late, n_late | Right bin clear at the 2-point mark.
S09.4 | For starts from 1954 to 1980, even 3 points left 10.5% costlier, the worst by $6,033. | gap30_early, n_early, gap30_worst | Left bin with a thin red layer at the 3-point mark.
S09.5 | Which kind of history comes next is something no replay can show. | — | The ridge ends at today; the space to its right stays empty.
S09.6 | [warm] Leah's illustrative offer sits at 1.5 points, short of the 2-point mark where none of the 1981-on starts cost more. | gap_start, gap20_late, n_late | Leah's card on the ruler, ILLUSTRATIVE badge, just left of the 2-point tick.
S09.7 | At her point, more than 1 in 4 of the 1954-to-1980 starts and about 1 in 30 of the later ones still cost more, the worst by $11,219. | share_early, share_late, n_early, n_late, worst_diff | Her two bins: left red layer clearly visible, right a few tokens.
S09.8 | A real offer has its own two rates, its own head start and its own place on the line. | — | Blank offer card hovers above the ruler, not placed.
S09.9 | It also has what this replay leaves out: the lender's real index, a rate cap, a grace period, fees, and the borrower's own budget. | — | Five plain objects around the card (index ribbon, ceiling, hourglass, receipt, wallet).
S09.10 | The line doesn't say which offer is better; it shows what each head start meant in each kind of history. | — | Ruler with both bins at every mark.
S09.11 | [calm] History, not a forecast. | — | Ridge fades; empty space to the right of today.

## S10 — End screen tail (~9:37–10:00, 15–20 s)

S10.1 | Every assumption behind this replay is listed in the description. | — | End-screen layout; ridge as a quiet background.
S10.2 | Another replay from this channel is on screen now. | — | Video element slot; remaining ~12 s music only.

---

### Totals
Narration: 1,462 words (S01–S10, tags excluded) ≈ 9:45 at 150 wpm; with scene gaps and the ~12 s music-only end-screen tail ≈ 10:00–10:15 total.
Cold open CO-A = 60 words ≈ 24 s (CO-B in `cold-open-options.md`).

### Tag map (6)
S01.3 `[curious]` · S03.3 `[curious]` · S07.1 `[serious]` · S08.8 `[thoughtful]` · S09.6 `[warm]` · S09.11 `[calm]`
