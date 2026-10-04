# Episode 2 — Script v2: what changed (C2, WRITER, 2026-10-01)

v1 is kept as `script-v1.md`. IDs below are **v2** IDs unless marked v1. The narration is 1,462 words, down from 1,636, about 9:45 at 150 wpm. v2 uses 6 emotion tags, down from 7.

## Coordinator points 1–8

| # | Change | v2 sentence IDs |
|---|---|---|
| 1 | **S09 → S08: spoken figures cut from about 18 to 9 new ones**, plus the 1.5 anchor. The spoken stops are 0 (79% / 42%, $16,566), 1.5 (Leah, anchor), 2 (none / 20.4%, $9,472) and 3 (none / 10.5%, $6,033). The 1-point and −1 stops and every overall share (`spread*_share`) now appear only on the slider; their IDs are in the picture column. The point that lands: the 1981-on bin clears at 2 points, and the 1954–1980 bin never does. | S08.4–S08.11, S09.3–S09.4 |
| 2 | **Both-periods rule applied strictly.** S05.5 "and it didn't" (v1) is gone, and no line says or implies "variable usually wins". Each result share and each favourable case now sits in one sentence, or an adjacent pair, that gives both periods and the worst case. The pairs are: overall / periods / worst (S03.5+S03.6), best case (S06.5+S06.6), each slider stop (S08.4+S08.5, S08.6, S08.7, S08.8), "never fell to zero" (S08.11), the two-half answer (S09.3+S09.4) and Leah's place (S09.6+S09.7). The median $3,832 (v1 S07.6) was cut: it was favourable-only and the most clippable line. | listed |
| 3 | **"Worth it" defined once**: how often it cost more in total interest than the 9% fixed loan, and how much more at worst. The question is asked in S01.3, defined in S03.2 and reused in S09.2 to frame the answer. Leah's place is now spoken: 1.5 points, short of the 2-point mark that cleared every 1981-on start, with more than 1 in 4 of the 1954–1980 starts still costlier and the worst $11,219. | S01.3, S03.2, S09.1–S09.2, S09.6–S09.7 |
| 4 | **Unclaimed facts removed.** "SOFR is only a few years old" became "the replay needs a much longer record than [the lender's own] index has" (S04.2). Inflation is no longer given as a cause in v1 S07.1 or S08.3; v2 S06.1 and S07.3 describe only how the T-bill moved. The Grad PLUS exception now reads "up to 3 more academic years, or for the time left in their program if that is shorter" (S02.1, `ctx_plus_exception`). `tb_peak` is now 16.3%, `best_diff` "$15,295 less", and 0% is "none". New claims used: `first_payment_gap` (S02.6), `max_payment` with April 1977 (S07.5), `gap_worst_start_all` (S08.10) and `min_gap_early` (S08.11). | S02.1, S04.2, S06.1–S06.2, S07.3, S07.5, S08.10–S08.11 |
| 5 | The words **"US only"** now appear literally: "…and the data is US only." | S04.13 |
| 6 | **Cold open: two versions** in `cold-open-options.md`. CO-A is the default in the script: a dated line, then Leah, 60 words. CO-B puts Leah first, also 60 words. Neither uses the imperative "Picture Leah"; she is described. The **paradox tease moved into the promise**: `share_rate_above_fixed` vs `share_all`, with both periods and the worst in the next sentence. | S01.1–S01.3, S03.3–S03.7 |
| 7 | **Visual collisions fixed** (`beats.md`). Amber now means only "rate above 9%" and red only "costlier in total". Coins mean only interest paid; the cushion is a green jar of liquid. The ridge is the only rate metaphor, and all the water is gone. The bead rides a track shaped like the ridge. The two bins sit under the two halves of the ridge, and tokens drop straight down into them, so a viewer can read the era from shape, not text. There are still 7 KEY beats, each with a one-line masked-read idea. | beats.md, picture column throughout |
| 8 | **Trim and split.** v1 S02.1–S02.18 (18 lines, 288 words) became S02.1–S02.12 (224 words). The first policy fact is no longer said twice. Repeated restatements of "1 in 4 / 1 in 30" were cut from v1 S07.2, S07.4, S08.9 and S09.8. The remaining ones are each required by the both-periods rule. Long sentences were split: v1 S04.7 became S04.7 + S04.8, v1 S05.7 became S03.5 + S03.6, and v1 S09.8 became S08.6, a single line of 20 words. S03.8 now states the slider's direction unambiguously ("from a variable rate 3 points under the fixed rate to one 1 point over it"). S02.11 was added: "A point here means one percentage point of interest." | listed |

Also new: S04.6 speaks the zero floor of the index, which v1 had only on the description card. S04.11 explains that tokens are sorted by half. S06.3 states the "same loan, different start" contrast.

## Structure changes

The paradox moved from v1 S05 into the promise (S03). v1 S05 and S06 merged into one "why both are true" scene (S05). The worst stretch is S07, the line S08, and the answer and close S09. Updated to match: `beats.md` (vocabulary, 12 beats, 7 KEY) and `treatment.md` (v2).

## Critic points not taken, or taken differently

- **Critic fix 2, "delete S01.1 and open on the moment":** not taken as the default. The coordinator ruled that this is a taste call. CO-A keeps the dated line first, per G-009 and the Ep 1 precedent. The critic's version is CO-B.
- **"S08.8 cap: cite `cap12_worst` $6,590":** not taken. There is no 1981-on claim for caps, so a capped worst case can't be spoken under the both-periods rule. Caps stay in words in S07.8 (`cap*_late` is requested in `needs-claims.md`).
- **"Aim for ~1,450–1,500 words":** met at 1,462. Some restatements of 1 in 4 / 1 in 30 remain (S03.6, S06.6, S08.6, S09.7). Each one is there because the strict both-periods rule requires it next to a favourable case or a result. This is a known tension with the critic's "no restatement" note, and I chose the hard rule.
- **Critic H5, "S04 method before any payoff":** partly taken. The paradox now lands before the method (S03), but the method stays a full scene. Its limits are hard-rule content, and KEY-4 relies on it.
- **Critic alt-B suggestion, "show the line early in S03":** taken in words only (S03.8–S03.9: "the replay moves the head start… a line"). The bracket and ruler appear on screen, but no 0-point numbers are moved forward.
- **Treatment length:** treatment.md is about 790 words, above the ~700 guide, because v2 adds the promise/paradox section. It is left as is for the owner's read.

## Still open

- `first_payment_gap` "about $40 less a month" sits next to the two exact payment figures in S02.6. CO-B would drop it from S02.
- S08 still speaks 9 new figures. The stop at 0 could go to the slider too, which would leave about 6, if the C2 blind read still finds S08 dense.
