# Episode 2 — Beat sheet v3 (C2, WRITER, 2026-10-01)

Times are estimates at ~150 wpm from `script.md` v3 (1,286 narration words; 13 voice scenes, max 728 characters). Claim IDs from `numbers.md`. Every loan number is ILLUSTRATIVE.

## Visual vocabulary (one meaning per object, one colour per meaning)

| meaning | object | rule |
|---|---|---|
| The rate (the only rate metaphor) | **The ridge**: the T-bill line through history drawn as a terrain edge. No water anywhere. | Leah's variable rate is a **bead** riding a track that has the ridge's shape, a fixed distance above it. |
| The fixed rate | A level **rail** at 9%. | Never moves. |
| Rate above 9% at some point | The rail segment glows **amber** wherever the bead is over it. | Amber is used for nothing else. |
| Costlier in total interest | A **red token**. | Red is used for nothing else. Not costlier = plain grey token. |
| Interest paid | **Coin piles**. | Coins mean interest paid, nothing else. |
| The saving built by the head start (the cushion) | A **green jar of liquid** that fills and drains. | Not coins. |
| Head start | A coloured **bracket** between rail and bead at the start line. | — |
| The two eras | Two **bins sitting directly under the two halves of the ridge**: left under the climbing half (1954–1980), right under the falling half (1981 on). Each 10-year frame drops its token straight down into the bin beneath where it started. | A muted viewer reads the era from the ridge shape above the bin, without text. |
| The worst case | A **dark token** that stays in one spot in the left bin; an extra block on top of the fixed coin pile. | — |

**Rule (v3, from the C2 blind read):** none of these object names is ever spoken. Narration says "stretches", "the 1954-to-1980 starts", "the cushion" (a story word, not a picture device) — never token, bin, slider, jar, ridge, bead or rail.

## Beat table

| id | ~time | scene | job of the beat | feeling | claims |
|---|---|---|---|---|---|
| B01 · **KEY-1** | 0:00 | S01 | CO-A: dated context line; Leah (illustrative), 9% fixed vs 7.5% variable; the central question. | "that's me" + curiosity | `ctx_plus_end`, `fixed_rate`, `var_start` |
| B02 | 0:24 | S02 | Who keeps Grad PLUS; basic federal loan $20,500 a year / $100,000 total; professional limits higher; the rest can come from a private lender. | orientation | `ctx_plus_exception`, `ctx_unsub_annual`, `ctx_unsub_aggregate` |
| B03 · **KEY-2** | 1:02 | S03 | $50,000, 10 years, illustrative; $593.51 vs $633.38 (about $40 less); fixed vs variable; head start defined; Leah's 1.5 points; can be bigger, smaller, zero, negative. | the pull of the lower bill; clarity | `loan`, `term`, `var_first_payment`, `first_payment_gap`, `fixed_payment`, `fixed_rate`, `var_start`, `gap_start` |
| B04 | 1:53 | S04 | Promise: every 10-year stretch since January 1954; "worth it" defined; the head start will move (3 under → 1 over); a line any offer can be held against; history, not a forecast. | anticipation | `first_start`, `term`, `fixed_rate`, `spread3_share`, `spreadm1_share` |
| B05 · **KEY-3** | 2:32 | S05 | The contradiction: above 9% in about 3 in 4; costlier in total in about 1 in 7; more than 1 in 4 / about 1 in 30; worst $11,219. The reason is the head start. | surprise | `share_rate_above_fixed`, `share_all`, `share_early`, `share_late`, `worst_diff` |
| B06 · **KEY-4** | 3:00 | S06 | The cushion, right after the puzzle: fills fastest on the biggest balance; months above 9% drain it; short jumps dent it; falling stretches keep filling it. | "aha" | — |
| B07 · **KEY-5** | 3:41 | S07 | The replay in plain words: lender index + fixed margin; T-bill stand-in with the margin set so Leah starts at 7.5%; 10-year runs stepping month by month from January 1954 to September 2016; overlapping, not independent; US only. Method card carries the rest. | trust | `var_start`, `first_start`, `term`, `last_start`, `fixed_rate`; card: `index_today`, `margin`, `n_starts` |
| B08 | 4:34 | S08 | Two kinds of history: climbing to 1980, peak 16.3% May 1981, drifting down; best August 1981 ($15,295 less) paired with both periods and the worst. | perspective | `tb_peak`, `best_start`, `best_diff`, `share_early`, `share_late`, `worst_start`, `worst_diff` |
| B09 · **KEY-6** | 5:25 | S09 | The worst stretch as Leah's loan: April 1977, 19.3%, $863.36 vs $633.38, $11,219 more than $26,005 (43%); no cap in the replay. | weight | `worst_start`, `var_start`, `worst_peak_rate`, `max_payment`, `fixed_payment`, `fixed_int`, `worst_diff`, `worst_share_of_fixed` |
| B10 · **KEY-7** | 6:11 | S10 | The line: fixed held at 9%; spoken stops only Leah's 1.5 (28.4% / 3.5%, $11,219), 2 (none / 20.4%, $9,472) and 3 (none / 10.5%, $6,033). | the viewer locates an offer | `share_early`, `share_late`, `worst_diff`, `gap20_*`, `gap30_*`; screen: `spread2_share`, `spread3_share` |
| B11 | 6:55 | S11 | Smaller or reversed head starts in words only (figures on screen); worst always April 1977; some 1954–1980 starts always costlier; the answer in two halves; no replay shows what comes next. | sober clarity | `gap_worst_start_all`, `min_gap_early`, `gap20_late`, `gap30_early`, `gap30_worst`; screen: `spread1_share`, `gap10_*`, `spread0_share`, `gap00_*`, `spreadm1_share`, `gapm10_*` |
| B12 | 7:50 | S12 | Leah at 1.5, short of the 2-point mark, worst $11,219; what the replay leaves out; "History, not a forecast." | warm close | `gap_start`, `share_early`, `share_late`, `worst_diff` |
| B13 | 8:27 | S13 | End-screen tail, 15–20 s. | release | — |

## Key beats — what a viewer must read with sound off and all text/numbers masked

Target (PLAN Q3): ≥ 70% read correctly at C4, with a control.

| key | script lines | idea a muted, text-masked viewer must read | picture that carries it |
|---|---|---|---|
| **KEY-1** | S01.2–S01.3 | "Someone is weighing a cost that stays level against one that starts lower but wanders up and down." | A level rail; just below it a bead on a short wavy track; the track ahead wavers; the gap between bead and rail glows. |
| **KEY-2** | S03.5–S03.8 | "The size of the starting gap is the thing being measured, and it can be big, small, none or reversed." | A coloured bracket snaps between rail and bead at the start line, then widens, narrows, closes, and flips as the bead starts above the rail. |
| **KEY-3** | S05.2–S05.4 | "The variable rate goes above the fixed rate in most replays, yet ends up costing more overall in only a few — far more often in the earlier half of history." | Frame after frame the rail glows amber over most of its length; then tokens drop into the two bins under the ridge: only a few turn red, and the left bin (under the climbing half) is clearly redder. Amber and red never share an object. |
| **KEY-4** | S06.1–S06.5 | "Starting lower builds up savings early, and that saving has to be used up before the variable loan comes out worse." | A green jar fills while the bead is under the rail, fastest beside the tallest debt stack; amber rail → jar drains; a brief amber blip barely lowers it; a long early climb drains it dry; on a falling stretch it keeps filling. |
| **KEY-5** | S07.5–S07.7 | "The same loan is replayed over and over, starting at each moment in a long history, and each result is sorted by where in history it started." | A 10-year frame steps right along the ridge, notch by notch, faster and faster; each stop drops a token straight down into the bin beneath it; neighbouring frames visibly overlap. |
| **KEY-6** | S09.1–S09.7 | "In the worst replay, rates climbed for years and the variable loan cost a lot more — close to half again the fixed loan's interest." | The frame lands on the steepest climb of the left half; the bead rises far above the rail; amber for years; the jar empties; an extra block grows on the fixed coin pile to a bit under half its height. |
| **KEY-7** | S10.4–S11.3 | "A bigger starting gap means fewer losing replays and a smaller worst case — the later half of history clears completely, the earlier half never does." | A slider widens the bracket; red drains out of both bins; the right bin goes fully grey partway; the left bin always keeps a thin red layer; the extra block shrinks but never vanishes; sweeping back the other way, both bins refill. |

Notes for C3/C4:
- Text on screen stays large (≥ 40 px floor, G-014): at most one number per moment, plus the ILLUSTRATIVE badge. The S07 method card and the S11 slider carry the unspoken figures (claim IDs in the script picture column); on the card, one line at a time.
- The bins sit under the two halves of the ridge, so "both periods" is visible every time a result appears.
