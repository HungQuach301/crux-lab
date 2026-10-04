# Episode 2 — Script v3: what changed (C2, WRITER, 2026-10-01)

Source: the C2 blind read (`gates/C2-blind.md`). v2 is kept as `script-v2.md`. IDs below are **v3** IDs; v2 IDs are marked "v2".

| Metric | v2 | v3 |
|---|---|---|
| Narration words | 1,462 | **1,286** |
| Narration at 150 wpm | ≈ 9:45 | **≈ 8:34** |
| Runtime with gaps and end screen | — | ≈ 9:00–9:10 |
| Voice scenes | — | **13** |
| Largest scene | — | **728 characters** (S11); none over 900 |
| Emotion tags | 6 | 6 |

## Coordinator points 1–7

| # | Blind-read signal | Change | v3 IDs |
|---|---|---|---|
| 1 | Method passage lost 5/6 readers. | The method is now 7 plain sentences: a stand-in index in plain words, 10-year runs stepping month by month, set against the fixed loan, overlapping so not independent, and "the data is US only". The rest moved to an on-screen **method card** and the description: 3.72% in August 2026 (`index_today`), the 3.78-point margin (`margin`), 753 start months (`n_starts`), the zero floor, and no grace period, fees or cap. The cap and grace period are still spoken in S09.8 and S12.3. | S07.1–S07.7 |
| 2 | Slider run lost 5/6. | Only three stops are spoken: Leah's 1.5 as the anchor, 2 points and 3 points. Each carries both periods and the worst case. The 0-point, 1-point and −1 stops and every overall share are on screen only, with claim IDs in the picture column. The smaller or reversed side gets one sentence in words, with no figures. | S10.4–S10.6, S11.1 |
| 3 | "token" and "bin" leaked into narration (5/6). | Every sentence that referred to a picture device was removed, including v2 S04.11 ("Each start month becomes one token…"). A checker now scans the narration for token, bin, slider, jar, ridge, bead and rail and finds none. "Cushion" stays, because it is a story word and is explained in words in S06. | — |
| 4 | "plus a fixed 3.78 points" was unexplained (5/6). | It is now in plain words: "A real variable rate is the lender's own index plus a fixed margin…", and the replay "sets the margin so that Leah's rate starts at 7.5%". The figure appears only on the card. | S07.2–S07.3 |
| 5 | Fractions and percentages were mixed (3/6), and a double negative confused 1/6. | Each passage now uses one form. The contradiction and two-histories passages (S05, S08) use the "1 in N" wording. The head-start passage (S10) uses percentages, so Leah's anchor is "28.4% … 3.5%", the display values of `share_early` and `share_late`. v2 S08.11 "never fell to zero, even where none…" became "And at every head start tested, some of the 1954-to-1980 starts still cost more." (`min_gap_early`) | S05.4, S08.7, S10.4–S10.6, S11.3 |
| 6 | The paradox confused readers until the cushion came (5/6, intended). | The tension is kept but the gap is shorter. The method now comes **after** the cushion. The cushion scene (S06) follows the puzzle (S05) directly, about 30 s later instead of about 2.5 min. S05.5 bridges them: "The reason both are true is the head start." | S05–S07 order |
| 7 | Voice generation | The script is split into 13 scenes at paragraph breaks, each at most ~900 characters (the largest is 728). Every scene header shows its word and character count, and each scene is one TTS call. | S01–S13 |

## Other changes

- S08.1: "And that is where the two halves of the record differ" (v2 S05.8) became "And the two halves of the record are very different." It moved with the method reorder, because it now follows the method rather than the cushion.
- S10.4 "At Leah's 1.5 points…" opens the slider run. It replaces the v2 S08.6 wording, which was "brings that to" after the dropped 0-point stop.
- S11.6 merges the two halves of the answer into one sentence: none costlier at 2 points from 1981 on; even 3 points was not enough for 1954–1980, with the worst at $6,033.
- S12.1: Leah's place no longer repeats the percentages from S10.4. It now reads "short of that 2-point mark, where stretches from both halves of history still cost more and the worst was $11,219".
- The structure changed (promise → contradiction → cushion → method → history → worst → line → answer), so `beats.md` was updated and the key beats were renumbered. There are still 7. KEY-3 is the contradiction, KEY-4 the cushion and KEY-5 the replay.
- `cold-open-options.md` is unchanged; no fix applied to both versions. `treatment.md`: journey items 1–2 swapped (cushion before method), method card noted.

## Not taken, or open

- **Length:** 1,286 words is below the brief's 1,400–1,650, because the coordinator asked for cuts. At about 9:00 it is still inside the channel's 8–15 min range. I did not pad it back up. If length matters, the best candidate is a second worked stretch, from the 1981-on side (needs a claim), as a counterpart to April 1977.
- **"1 in N" vs percentages:** the same shares, more than 1 in 4 and about 1 in 30, appear as words in S05 and S08 and as 28.4% and 3.5% in S10. Each passage is consistent on its own, but a viewer hears both forms over the episode.
