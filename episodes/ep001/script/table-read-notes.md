# Episode 1 — table read (M1 item 3): audio and list of fixes

- Audio: `review-m1/table-read-full.m4a` (10:09, every gap between sentences <= 0.75 s; 0.35 s inside an act, 0.75 s between acts). Voice: ElevenLabs Eric `eleven_v3` (V8), one take per sentence, no time stretching, no fallback model. Provisional voice, not decision #158.
- Credits: 84 takes, **4,292 characters** billed (sum of `character-cost` headers, `out/voice/el/*.json` + `work/replaced-takes/`).
- Measured with the builder's own ASR (faster-whisper small.en) per take. The owner listens by ear (DX-S9): the machine list below does not replace that.

## Pace (DX-A7: acts 150-160 wpm, every sentence 120-190)

| act | wpm |
|---|---|
| cold-open | 180.2 |
| act1 | 153.7 |
| act2 | 167.2 |
| act3 | 161.5 |
| method | 132.7 |
| outro | 173.7 |

16 sentences above 190 wpm and 6 under 120 wpm (times in the table read):

| sentence | at | wpm | fix at M2 |
|---|---|---|---|
| `co-bars.1` | 0:00.3 | 203.9 | new take; add a pause mark ("...") at the clause break |
| `a1-scope.1` | 0:20.5 | 115.8 | new take; remove a pause mark, the short line drags |
| `a1-q.1` | 1:01.9 | 101.5 | new take; remove a pause mark, the short line drags |
| `a1-count.1` | 1:46.0 | 113.4 | new take; remove a pause mark, the short line drags |
| `a1-median.1` | 1:56.3 | 116.4 | new take; remove a pause mark, the short line drags |
| `a1-boomcost.1` | 2:21.7 | 191.5 | new take; add a pause mark ("...") at the clause break |
| `a1-small.1` | 2:33.1 | 201.3 | new take; add a pause mark ("...") at the clause break |
| `a1-big.1` | 2:39.8 | 192.0 | new take; add a pause mark ("...") at the clause break |
| `a1-keep.1` | 2:46.3 | 198.2 | new take; add a pause mark ("...") at the clause break |
| `a2-s10.1` | 3:59.3 | 195.7 | new take; add a pause mark ("...") at the clause break |
| `a2-be10.1` | 4:03.6 | 208.7 | new take; add a pause mark ("...") at the clause break |
| `a2-s20.1` | 4:06.5 | 195.3 | new take; add a pause mark ("...") at the clause break |
| `a2-curve.1` | 4:10.5 | 239.3 | new take; add a pause mark ("...") at the clause break |
| `a2-cliff.1` | 4:14.3 | 115.4 | new take; remove a pause mark, the short line drags |
| `a2-payoff.1` | 5:22.8 | 206.9 | new take; add a pause mark ("...") at the clause break |
| `a2-hold.1` | 5:30.9 | 209.0 | new take; add a pause mark ("...") at the clause break |
| `a3-rules.1` | 6:07.7 | 201.8 | new take; add a pause mark ("...") at the clause break |
| `a3-80s.1` | 6:26.7 | 192.0 | new take; add a pause mark ("...") at the clause break |
| `a3-81.1` | 6:29.6 | 200.0 | new take; add a pause mark ("...") at the clause break |
| `m-costs.1` | 9:17.4 | 88.7 | new take; remove a pause mark, the short line drags |
| `o-bill.1` | 9:58.0 | 213.4 | new take; add a pause mark ("...") at the clause break |
| `o-sources.1` | 10:03.2 | 192.8 | new take; add a pause mark ("...") at the clause break |

## Words and meaning

| where | heard | fix |
|---|---|---|
| `co-question.1` (0:07.7) | "how far do **raids** have to fall" | a real mishearing risk on the open question: new take, or "interest rates" in the text |
| `a1-scope.1`, `a1-payoff.1`, `a2-be05.1`, `a3-range.1`, `o-close.1` | "U .S.", "break -even" | ASR token splits, not reading errors; the builder's matcher is fixed (`toolkit/voice/keywords.py`, hyphen glue). |
| numbers | 488,241 and 3,089,298 read in full ("four hundred eighty-eight thousand...") | long; M2 option: round in narration ("about 488,000") with a rounded claim, the exact count on screen |
| `a2-s05.1` | "zero point five points" | acceptable; alternative "half a point" needs a claim display that the ASR matches |

## Structure found on the read

- Cold open was 16.8 s on the first plan (> 15 s): the first line was shortened ("A lower rate cuts the monthly payment.", one new take), the picture lead is 1.2 s, and the silence after the question was dropped. Now 14.7 s: close to the limit; M2 must keep it.
- Rehook "By the end, you will see the exact rate drop that repays a typical refinance within 36 months, and how every rate drop since 1971 actually played out." sits at 0:30.4-0:42.9 in the planned edit.
- Method card reads slowly (132.7 wpm): fine for a card, but A15 counts it as an act: tighten at M2.
- DX-A7 at M2: v3 reads 180-240 wpm on short declaratives; the d_el_voice loop (4 takes, then multilingual_v2 with a speed setting) will be needed, at a higher credit cost (estimate 20-35k characters).
