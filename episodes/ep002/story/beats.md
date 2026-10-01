# Episode 2 — Beat sheet (C2, WRITER, 2026-10-01)

Times are estimates at ~150 wpm from `script.md` (1,636 narration words). Claim IDs from `numbers.md`. Every loan number is ILLUSTRATIVE.

**Visual vocabulary (one system, proposed for C3):** the *fixed* loan is a flat, level bar; the *variable* loan is a lower bar floating on water whose level is the Treasury bill rate; the *head start* is a coloured bracket between the two bars at the start; a *stretch* is a 10-year frame that slides along a long ridge of rate history; each stretch's result is a *token* (red = variable cost more in total interest, plain = it did not) dropped into a tray split into two bins (1954–1980 left, 1981 on right); *total interest* is a coin pile; the *saving* built up while the variable rate sits below 9% is a "cushion" jar; the *worst case* is an extra block on top of the fixed coin pile. These objects are meant to carry the idea with the sound off and all text/numbers masked (lessons D1, G-011, G-012a).

## Beat table

| id | ~time | job of the beat | feeling | claims |
|---|---|---|---|---|
| B01 | 0:00 | Context in one line: from July 1, 2026, new grad students can't borrow Grad PLUS. | unease | `ctx_plus_end` |
| B02 · **KEY-1** | 0:07 | Leah at her laptop, two offers: fixed 9% vs variable starting lower at 7.5%; the variable rate can move; central question: how much lower does it have to start before the risk has been worth it? | "that's me" + curiosity | `fixed_rate`, `var_start` |
| B03 | 0:30 | What changed: Grad PLUS ended for new borrowers; continuing students keep it up to 3 more years; Direct Unsubsidized still $20,500 a year, $100,000 total; professional programs differ; the rest can come from private lenders (not everyone). | orientation | `ctx_plus_end`, `ctx_plus_exception`, `ctx_unsub_annual`, `ctx_unsub_aggregate` |
| B04 | 1:20 | Leah's loan made concrete: $50,000 over 10 years, ILLUSTRATIVE; first payments $593.51 vs $633.38. | the monthly pull of the lower number | `loan`, `term`, `var_first_payment`, `fixed_payment` |
| B05 | 1:40 | Fixed vs variable in plain words; the trade. | understanding | — |
| B06 · **KEY-2** | 2:05 | "Head start" defined: the distance between the two starting rates; Leah's is 1.5 points; real offers can be bigger, smaller, zero or negative. | clarity | `fixed_rate`, `var_start`, `gap_start` |
| B07 | 2:25 | Promise: replay Leah's loan through US rates since January 1954; how often costlier in total interest than the 9% fixed loan, how bad the worst; then move the head start from −1 to +3; a line any offer can be held against. "History, not a forecast." | anticipation | `first_start`, `gap_start`, `fixed_rate`, `spreadm1_share`, `spread3_share` |
| B08 | 3:05 | Index stand-in: SOFR too young; 3-month T-bill; 3.72% in August 2026; 7.5% = that + 3.78 points; rate moves month by month as the T-bill moved. | trust in the method | `index_today`, `var_start`, `margin` |
| B09 · **KEY-3** | 3:40 | The replay: start January 1954, run 10 years (no grace, fees or cap), compare interest with fixed; slide one month; to September 2016; 753 start months; overlapping, not independent; US only. | "I see how it's tested" | `first_start`, `term`, `fixed_rate`, `last_start`, `n_starts` |
| B10 | 4:20 | Bad-news half of the paradox: rate above 9% in about 3 in 4 stretches; payment above $633.38 in more than half; one payment reached $863.36. | worry | `share_rate_above_fixed`, `share_payment_above_fixed`, `fixed_payment`, `max_payment` |
| B11 · **KEY-4** | 4:50 | Turn: total interest costlier than the 9% fixed loan in about 1 in 7 stretches — more than 1 in 4 for 1954–1980 starts, about 1 in 30 from 1981 on; worst April 1977, +$11,219. | surprise, held in check | `share_all`, `share_early`, `share_late`, `worst_start`, `worst_diff`, `n_early`, `n_late` |
| B12 · **KEY-5** | 5:30 | Why both are true: the head start fills a cushion, fastest when the balance is biggest; later months above 9% must drain it; short spikes dent, long early climbs empty it. | "aha" | — |
| B13 | 6:15 | Two kinds of history: 1954–1980 rates climbed (28.4%); peak 16.30% May 1981; then mostly drifted down (3.5%); best August 1981, $15,295 less; median $3,832 less; worst from the first era. | perspective | `share_early`, `tb_peak`, `share_late`, `best_start`, `best_diff`, `n_starts`, `median_diff`, `worst_diff`, `worst_start` |
| B14 · **KEY-6** | 7:05 | The worst stretch, as Leah's loan: April 1977; ahead at first; rate to 19.3%; fixed interest $26,005, variable $11,219 more (43% on top); no cap in the replay; belongs to the "more than 1 in 4" era, not "about 1 in 30". | weight | `worst_start`, `var_start`, `worst_peak_rate`, `fixed_int`, `worst_diff`, `worst_share_of_fixed`, `share_early`, `share_late` |
| B15 · **KEY-7** | 7:55 | The self-check line: same replay with the fixed rate held at 9%, head start 0 / 1 / 1.5 / 2 / 3 / −1; each with both periods and the worst; slope; 1954–1980 never reaches zero. | the viewer locates their own offer | `spread0_share`, `gap00_*`, `spread1_share`, `gap10_*`, `spread15_share`, `spread2_share`, `gap20_*`, `spread3_share`, `gap30_*`, `spreadm1_share`, `gapm10_*`, all `gap*_early` |
| B16 | 9:45 | Answer to the central question in two halves: from 1981 on, 2 points was enough in every stretch; 1954–1980, even 3 points left 10.5% costlier, worst $6,033; which history comes next no replay can show. | sober clarity | `gap20_late`, `gap30_early`, `gap30_worst` |
| B17 | 10:15 | Back to Leah (illustrative) at 1.5 points; a real offer has its own head start and place on the line, plus what the replay leaves out. "History, not a forecast." | warm close | `gap_start`, `first_start` |
| B18 | 10:45 | End-screen tail, 15–20 s: assumptions in the description; another replay on screen; music only after. | release | — |

## Key beats — what a viewer must read with the sound off and all text/numbers masked

Target (PLAN Q3): ≥ 70% read correctly at C4, with a control.

| key | script lines | idea the viewer must read out | picture that carries it (objects/motion, not a labelled chart) |
|---|---|---|---|
| **KEY-1** | S01.3–S01.4 | "Someone is choosing between a loan cost that stays flat and one that starts lower but can move up and down." | Two bars on a desk: one rigid and level; one lower, floating on water that begins to swell and fall, the bar riding it. The gap between them glows. |
| **KEY-2** | S02.16–S02.18 | "The gap between the two starting levels is the thing being measured — and it can be big, small, none, or reversed." | A coloured bracket snaps between the two bar heights at the start; it stretches, shrinks, closes to nothing, then flips as the floating bar rises above the flat one. |
| **KEY-3** | S04.7–S04.11 | "The same loan is replayed over and over, starting at each moment in a long history." | A 10-year frame lands on the far left of a long ridge, then steps right notch by notch, faster and faster, each stop dropping a token into a tray; neighbouring frames visibly overlap. |
| **KEY-4** | S05.2–S05.8 | "The variable rate goes above the fixed one in most replays, but ends up costing more overall in only a minority — and far more often in the earlier half." | Most frames show the floating bar poking above the flat line (red flashes); then the flashes stop and the tray settles with only a few red tokens; the tray splits and the left bin is visibly redder than the right. |
| **KEY-5** | S06.2–S06.5 | "A lower start saves money early, and that saving has to be used up before the variable loan loses." | Coins drop into a jar while the floating bar is below the flat one, fastest at the start beside a tall debt stack; when the bar pokes above, coins leave the jar; a brief spike barely dents it, a long early climb empties it. |
| **KEY-6** | S08.1–S08.7 | "In the worst replay, rates climbed for years and the variable loan ended up costing a lot more — close to half again the fixed loan's interest." | The frame lands on a steep climbing section of the ridge; the floating bar rises far above the flat one; the jar empties; an extra block stacks on top of the fixed coin pile, reaching a bit under half its height. |
| **KEY-7** | S09.3–S09.15 | "The bigger the head start, the fewer losing replays and the smaller the worst one — but in the earlier half of history, some losses never go away." | A slider widens the bracket from reversed to wide; red tokens drain out of both bins as it moves; the right bin goes fully clear partway; the left bin always keeps a thin red layer; the worst-case block shrinks but never vanishes. |

Notes for C3/C4:
- The token tray is the one recurring object for results: the two bins make "both periods" visible every time a result appears, and the dark token (worst) stays in the left bin.
- Text on screen stays large (≥ 40 px floor, G-014): at most one number per moment (e.g. "1.5 points", "about 1 in 7"), plus the ILLUSTRATIVE badge.
