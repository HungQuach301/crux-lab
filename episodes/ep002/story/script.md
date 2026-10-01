# Episode 2 — Script v4 (C2, WRITER, 2026-10-01)

Working title (C1, A1): *Need Private Grad Loans? Variable vs Fixed Through History*. v1–v3 kept as `script-v1.md`, `script-v2.md`, `script-v3.md`; changes in `changes-v2.md`–`changes-v4.md`.

Format: `id | narration (US English) | claim IDs (numbers.md) | picture note`. One sentence per line. **Each scene `Snn` is one voice (TTS) call, at most ~800 characters of narration** (count shown per scene, tags excluded). Emotion tags (eleven_v3, Eric) sit at the start of the line they colour; 6 in total. No break/pause tags, no "...", no speed.

Narration never refers to picture devices; it must make sense with eyes closed. Numbers are written as the `Hiển thị` or `Lời (gợi ý)` column of `numbers.md`. Number form (fixed for the whole episode): every share with a spoken wording is said as "display, wording" — "76.2%, about 3 in 4", "14.2%, about 1 in 7", "28.4%, more than 1 in 4", "3.5%, about 1 in 30"; other shares as the display only (20.4%, 10.5%); 0% as "none". Leah's full set (28.4% / 3.5% / $11,219) is stated once, in S05; later sentences recall it in words only (owner rule, C2). Period labels "1954 to 1980" / "1981 on" are the model's split (`n_early`, `n_late`). Every loan number is ILLUSTRATIVE (badge on screen whenever Leah's loan is shown). One mechanism sentence comes before the first result (S04.2); the method passage ("How we know this") comes after the answer. Model limits not spoken (index value, margin, 753 starts, zero floor, no grace/fees/cap) are on its method card and in the description.

**Visual system (see `beats.md`; picture notes only, never spoken):** the rate is one object, the *ridge* (T-bill history); Leah's variable rate is a *bead* on a track shaped like the ridge; the fixed rate is a level *rail* at 9%. Amber rail = rate above 9%. Red token = costlier in total. Coins = interest paid. Green jar = the cushion. Two bins sit under the two halves of the ridge (left 1954–1980, right 1981 on).

Cold open: default **CO-A**; alternative CO-B in `cold-open-options.md`.

---

## S01 — Cold open, CO-A (60 words, 331 chars)

S01.1 | From July 1, 2026, new graduate students in the US can no longer borrow federal Grad PLUS loans. | ctx_plus_end | Calendar leaf turns to July 1, 2026; a federal form slides into a drawer that shuts.
S01.2 | Leah, an illustrative student weeks from her first spring term, has two private offers on her laptop: 9% fixed, or variable starting lower, at 7.5%. | fixed_rate, var_start | Night desk, laptop. A level rail (fixed) and, just below it, a bead on a short wavy track (variable). ILLUSTRATIVE badge.
S01.3 | [curious] How much lower does a variable rate have to start before that risk has been worth it? | — | The track ahead of the bead wavers; the gap between bead and rail glows. Title card. (KEY-1)

## S02 — Why private loans (96 words, 540 chars)

S02.1 | Students already enrolled and borrowing before July 2026 keep Grad PLUS for up to 3 more academic years, or for the time left in their program if that is shorter. | ctx_plus_exception | A second student keeps a PLUS form; an hourglass beside it.
S02.2 | New students like Leah still have the basic federal loan, a Direct Unsubsidized loan, up to $20,500 a year and $100,000 total, with higher limits in professional programs like medicine or law. | ctx_unsub_annual, ctx_unsub_aggregate | One federal form; one big figure at a time.
S02.3 | When a program costs more than that after other aid, the rest can come from a private lender, and that's where Leah's two offers come from. | — | A cost bar taller than the federal block; the remaining slice becomes a private-lender block that splits into the two offers.
S02.4 | Same lender, same amount, two kinds of rate. | — | The two offers side by side.

## S03 — Leah's loan and the head start (128 words, 719 chars)

S03.1 | Both are for $50,000 over 10 years, illustrative numbers, not a real lender's offer. | loan, term | $50,000 stack under each offer; ILLUSTRATIVE badge pulses once.
S03.2 | The variable loan's first payment is $593.51, about $40 less a month than the fixed $633.38. | var_first_payment, first_payment_gap, fixed_payment | Two envelopes; the variable one visibly thinner.
S03.3 | A fixed rate never changes, so neither does the payment. | — | The level rail; a row of identical envelopes.
S03.4 | A variable rate follows a market interest rate, so the rate and the payment rise and fall with it, and nobody knows where it goes next. | — | The bead rides its track up and down; envelopes thicken and thin; the track ahead fades out.
S03.5 | The head start is the fixed rate minus the variable rate's starting rate; it is negative when the variable rate starts higher. | — | A coloured bracket snaps between rail and bead at the start line. (KEY-2)
S03.6 | Leah's fixed rate is 9% and her variable rate starts at 7.5%, so her head start is 1.5 points. | fixed_rate, var_start, gap_start | Bracket labelled "1.5 points".
S03.7 | A point here means one percentage point of interest. | — | —
S03.8 | Real offers differ, so a head start can be bigger, smaller, zero, or negative. | — | Bracket widens, narrows, closes, then flips with the bead starting above the rail.

## S04 — The promise (120 words, 653 chars)

S04.1 | This video replays Leah's illustrative loan through every 10-year stretch of US interest rates since January 1954. | first_start, term | The short track stretches left into a long ridge of rate history.
S04.2 | Each replay moves her rate up and down exactly as much as the 3-month Treasury bill rate moved in that stretch of history, and the data is US only. | — | The bead's track takes the ridge's month-to-month steps inside a 10-year frame.
S04.3 | "Worth it" gets one plain meaning here: how often the variable loan cost more in total interest than the 9% fixed loan, and how much more at worst. | fixed_rate | Two coin piles (interest paid), fixed and variable, side by side.
S04.4 | Then the replay moves the head start, from 3 points down to minus 1 point, to see where that history changes. | spread3_share, spreadm1_share | The bracket slides along a ruler.
S04.5 | By the end there's a line that any real offer can be held up against, including yours. | — | A ruler across the screen; a blank offer card floats toward it.
S04.6 | This is history, not a forecast. | — | The ridge ends at today; empty space to its right.

## S05 — The contradiction (79 words, 397 chars)

S05.1 | [curious] And the first result looks like a contradiction. | — | —
S05.2 | Leah's variable rate rose above 9% at some point in 76.2% of stretches, about 3 in 4. | share_rate_above_fixed, fixed_rate | Stretch after stretch: the rail lights amber wherever the bead is above it; amber nearly everywhere.
S05.3 | Yet it cost more in total interest in 14.2%, about 1 in 7. | share_all | Tokens drop into the two bins under the ridge; only some turn red.
S05.4 | That 1 in 7 is made of two very different parts: 28.4%, more than 1 in 4, for starts from 1954 to 1980, and 3.5%, about 1 in 30, from 1981 on; the worst stretch, from April 1977, cost $11,219 more. | share_early, share_late, n_early, n_late, worst_start, worst_diff | Left bin (under the climbing half) clearly redder than the right; one dark token in the left bin. (KEY-3)
S05.5 | The reason both are true is the head start. | — | Bracket returns.

## S06 — The cushion (102 words, 550 chars)

S06.1 | Every month the variable rate sits below 9%, Leah pays less interest than on the fixed loan, and that saving builds a cushion. | fixed_rate | A green jar fills while the bead is under the rail. (KEY-4)
S06.2 | The cushion grows fastest at the start, when she owes the most, so every point of rate is charged on the biggest balance. | — | The debt stack is tallest at the left; the jar fills fastest there.
S06.3 | When the rate later climbs above 9%, the extra interest has to use up that cushion before the variable loan has cost more overall. | fixed_rate | Rail lights amber; the jar drains.
S06.4 | A short jump above 9% only dents it; emptying it needs rates that rise early and stay high for years. | fixed_rate | Two runs: a brief amber blip barely lowers the jar; a long early climb drains it dry.
S06.5 | In a stretch where rates drift down, the cushion just keeps growing. | — | Bead sinks under the rail; jar keeps filling.

## S07 — Two kinds of history (121 words, 677 chars)

S07.1 | And the two halves of the record are very different. | — | Camera pulls back to the whole ridge with its two bins.
S07.2 | From 1954 to 1980, the Treasury bill rate mostly climbed, in waves. | n_early | Left half of the ridge rises in waves above the left bin.
S07.3 | It peaked at 16.3% in May 1981, then mostly drifted down over the following decades, with big swings. | tb_peak | Summit marked; the right half slopes down above the right bin.
S07.4 | Same loan, same head start; the only difference is where in history it began. | — | Two identical beads set on the two halves of the ridge.
S07.5 | Loans started in the climbing years often met rates that rose early and stayed high, and loans started after the peak mostly rode rates down. | — | Left: bead climbs, jar drains. Right: bead sinks, jar fills.
S07.6 | The best stretch began in August 1981, near that peak, and cost $15,295 less than the fixed loan. | best_start, best_diff | One right-bin token glows bright; its jar brims.
S07.7 | It belongs to the falling half, while the worst, April 1977, belongs to the climbing half, where far more of Leah's stretches cost more. | worst_start | Camera swings from the bright token in the right bin to the dark token in the left bin. On screen (recall, no new figures): Leah's two shares.

## S08 — The worst stretch (120 words, 654 chars)

S08.1 | [serious] Here is Leah's same loan, started in April 1977. | worst_start | The 10-year frame lands on a steep climbing section of the ridge; Leah's desk appears inside it. (KEY-6)
S08.2 | It begins at 7.5%, like every replay, and for a while her cushion grows. | var_start | Jar fills a little.
S08.3 | Then the Treasury bill rate climbs year after year, and her rate follows it, to 19.3% at its highest. | worst_peak_rate | Bead far above the rail; the rail glows amber for years.
S08.4 | The cushion from her first months is soon gone, and every further month above 9% adds to what she owes in interest. | fixed_rate | Jar empty; coins keep adding to her pile.
S08.5 | Her payment reaches $863.36 a month, against the fixed $633.38. | max_payment, fixed_payment | Her envelope swells well past the fixed one.
S08.6 | Over 10 years, the fixed loan charges $26,005 in interest, in dollars of the day. | term, fixed_int | Fixed coin pile.
S08.7 | Leah's variable loan charges 43% more interest than the fixed loan, the worst stretch in the whole replay. | worst_share_of_fixed | Variable pile = fixed pile + an extra block reaching a bit under half its height; on screen: "+$11,219" (`worst_diff`).
S08.8 | This replay has no rate cap; a real loan's cap, if low enough, would have made this worst case smaller. | — | A ceiling line drawn over the bead, then lowered; the extra block trims.

## S09 — Moving the head start (101 words, 546 chars)

S09.1 | So far, every result has been for one pair of rates, 7.5% against 9%. | var_start, fixed_rate | Leah's bracket.
S09.2 | So the replay ran again, holding the fixed rate at 9% and moving only where the variable rate starts. | fixed_rate | A slider under the bracket; the rail pinned. (KEY-7 begins)
S09.3 | Each starting point is a different offer someone could be holding. | — | Offer cards line up along the slider.
S09.4 | Leah's 1.5 points gives the split already heard, with her April 1977 worst. | gap_start, worst_start | Leah's card clicks onto the slider; her bins as before (no new figures).
S09.5 | At 2 points, none of the starts from 1981 on cost more, but 20.4% of the 1954-to-1980 starts still did, the worst by $9,472. | gap20_late, gap20_early, n_early, n_late, gap20_worst | Right bin goes fully grey; left bin keeps a red layer. On screen only: "8.8%" (`spread2_share`).
S09.6 | [thoughtful] At 3 points, still none from 1981 on, but 10.5% of the 1954-to-1980 starts cost more, the worst by $6,033. | gap30_late, gap30_early, n_early, n_late, gap30_worst | Slider at the far end; left bin still holds a thin red layer; small extra block remains. On screen only: "4.5%" (`spread3_share`).

## S10 — Other offers, and the answer (136 words, 728 chars)

S10.1 | With a smaller head start, or a variable rate that starts higher, more stretches cost more in both halves, and the worst gets bigger. | — | Slider sweeps back through 1 point and 0 to −1; both bins fill red, extra block grows. On screen only, one figure per moment: 1 point "31.3%" (`spread1_share`), "54.9% / 13.5% / +$12,983" (`gap10_early`, `gap10_late`, `gap10_worst`); 0 points "57.9%" (`spread0_share`), "79% / 42% / +$16,566" (`gap00_early`, `gap00_late`, `gap00_worst`); −1 point "72.9%" (`spreadm1_share`), "92.9% / 57.8% / +$20,217" (`gapm10_early`, `gapm10_late`, `gapm10_worst`).
S10.2 | At every head start tested, the worst stretch began in April 1977. | gap_worst_start_all | The dark token never leaves its spot in the left bin.
S10.3 | And at every head start tested, some of the 1954-to-1980 starts still cost more. | min_gap_early, n_early | Left bin's red layer never clears.
S10.4 | So, back to the question: how much lower does a variable rate have to start before the risk has been worth it? | — | The question from S01 over the ruler.
S10.5 | Measured as how often it cost more in total interest than the 9% fixed loan, and how much more at worst, history gives two answers. | fixed_rate | Two bins under the two halves of the ridge.
S10.6 | From 1981 on, a 2-point head start was enough every time; from 1954 to 1980, even 3 points was not, and the worst still cost $6,033 more. | gap20_late, n_late, gap30_early, n_early, gap30_worst | Right bin clear at the 2-point mark; left bin with a thin red layer at the 3-point mark.
S10.7 | Which kind of history comes next is something no replay can show. | — | The ridge ends at today; the space to its right stays empty.

## S11 — How we know this (1 sentence; method card)

S11.1 | The replay uses the 3-month Treasury bill rate as a stand-in for the lender's index; how it was built is on screen and in the description. | var_start, first_start, last_start, term, fixed_rate | METHOD CARD (C2b, chủ dự án): toàn bộ phần phương pháp cũ S11.2–S11.6 lên thẻ + mô tả — lender index + fixed margin; T-bill stand-in, margin set so Leah starts at 7.5% (`var_start`); first replay January 1954, then monthly to September 2016 (`first_start`, `last_start`), each 10 years (`term`) against 9% fixed (`fixed_rate`); neighbouring stretches overlap, not independent; US only. Giữ nguyên nội dung thẻ cũ: Workbench view of the ridge. METHOD CARD (on screen, and in the description): "3-month T-bill stands in for the lender's index · 3.72% in August 2026" (`index_today`) · "margin 3.78 points" (`margin`) · "753 start months" (`n_starts`) · "index never below 0" · "no grace period · no fees · no rate cap". · **Đọc được ở 25% (G-014, sàn 40 px @1080) và hiện đủ lâu để đọc: ≥ 1 s mỗi 3 từ của thẻ, kéo sang đầu S12 nếu cần (P đo ở C4).**

## S12 — Where an offer falls (94 words, 513 chars)

S12.1 | [warm] Leah's illustrative offer sits at 1.5 points, short of that 2-point mark; at her point, starts from both halves of history still cost more, including her April 1977 worst. | gap_start, gap20_late, n_early, n_late, worst_start | Leah's card on the ruler, ILLUSTRATIVE badge, just left of the 2-point tick.
S12.2 | A real offer has its own two rates, its own head start and its own place on the line. | — | Blank offer card hovers above the ruler, not placed.
S12.3 | It also has what this replay leaves out: the lender's real index, a rate cap, a grace period, fees, and the borrower's own budget. | — | Five plain objects around the card (index ribbon, ceiling, hourglass, receipt, wallet).
S12.4 | The line doesn't say which offer is better; it shows what each head start meant in each kind of history. | — | Ruler with both bins at every mark.
S12.5 | [calm] History, not a forecast. | — | Ridge fades; empty space to the right of today.

## S13 — End screen tail (15–20 s) (19 words, 116 chars)

S13.1 | Every assumption behind this replay is listed in the description. | — | End-screen layout; ridge as a quiet background.
S13.2 | Another replay from this channel is on screen now. | — | Video element slot; remaining ~12 s music only.

---

### Totals
Narration: 1,295 words (tags excluded) ≈ 8:38 at 150 wpm; with scene gaps and the ~12 s music-only end-screen tail ≈ 9:05–9:15. Max narration per scene: 728 characters. Scene starts (150 wpm): S01 0:00 · S02 0:24 · S03 1:02 · S04 1:53 · S05 2:41 · S06 3:13 · S07 3:54 · S08 4:42 · S09 5:30 · S10 6:10 · S11 7:05 · S12 7:52 · S13 8:30.

### Tag map (6)
S01.3 `[curious]` · S05.1 `[curious]` · S08.1 `[serious]` · S09.6 `[thoughtful]` · S12.1 `[warm]` · S12.5 `[calm]`
