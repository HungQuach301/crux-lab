# Episode 1 — cue sheet (M1 plan)

Planned length **10.65 min** (639.3 s) from the table-read takes. Music is generated in code (toolkit/audio/d_m2_audio.py, one reverb space, per-act arrangement); no third-party audio.

## Music cues

| t (s) | end | layer | key | tempo | dramatic function |
|---|---|---|---|---|---|
| 0.0 | 14.7 | music | A minor | 72 | suspense under the open question; pad + pulse, no melody |
| 14.7 | 17.7 | music | A minor | 72 | ident sting |
| 17.7 | 202.7 | music | C major | 84 | curious, light pulse; the SMALL and LARGE motifs introduced (amber: low plucks, blue: high bells) |
| 202.7 | 368.2 | music | D minor | 92 | building: the pulse tightens toward the cliff (a2-cliff), valley after it; re-voiced at the loan-size turn |
| 368.2 | 558.8 | music | F major | 88 | history: darker at the further-drop turn, resolves on the answer |
| 558.8 | 597.0 | music | F major | 70 | thin pad under the method card |
| 597.0 | 639.3 | music | C major | 76 | resolved; both motifs together |
| 133.0 | 153.0 | music-dynamics | C major | 84 | build to the act1 climax (+6 dB over 20 s) |
| 244.4 | 264.4 | music-dynamics | D minor | 92 | build to the act2 climax (+6 dB over 20 s) |
| 480.1 | 500.1 | music-dynamics | F major | 88 | build to the act3 climax (+6 dB over 20 s) |

## Intentional silences (DX-R6: ~300 ms release in, room tone floor, back in 200 ms)

| t (s) | length | after | why |
|---|---|---|---|
| 129.25 | 1.2 s | `a1-median.1` | let the median bill land |
| 200.92 | 1.6 s | `a1-after.1` | end of act 1: ad break |
| 272.61 | 1.0 s | `a2-cliff.1` | let the steep part of the curve sink in |
| 366.36 | 1.6 s | `a2-reset2.1` | end of act 2: ad break |
| 508.59 | 1.3 s | `a3-answer2.1` | the answer lands |

Ad breaks (DX-S10): 201.7 s, 367.2 s, inside the act1|act2 and act2|act3 silences.

## Sound design

- whoosh per camera move, level from peak speed (A10); riser into each reveal; impact on the decisive numbers (`cost_med`, `sp36_mid`); room tone throughout.
- every spoken number: music and sfx dip from 0.5 s before to 1.6 s after (DX-A6); the data sounds follow the voice side-chain below.

## Data sonification plan (DX-A1, sổ gu G-001, G-005, G-006), per element type

Timbre: **not chosen yet**, left empty until the owner picks S1, S2 or S3 (`review-m1/sonify-S1.mp4`, `-S2`, `-S3`; blind names).

| element | timbre | value mapping | pan | timing | scenes using it |
|---|---|---|---|---|---|
| bar | (chờ chọn) | pitch = bar value on one fixed scale for the film, snapped to the music key; lasts while the bar grows | x of the bar | starts when the bar starts to grow (moved into the nearest syllable gap if the voice is sounding) | 18 |
| line | (chờ chọn) | pitch follows the slope at the drawing tip (rising line = higher), snapped to the music key | x of the tip | while the tip moves; discrete notes of a run land in syllable gaps | 13 |
| dot | (chờ chọn) | pitch from the dot height on screen (higher = higher) | x of the dot | on the frame the dot appears (nearest syllable gap, -60..+120 ms, when the voice is sounding) | 28 |
| counter | (chờ chọn) | one soft event per value change; > 8 changes/s merge into one roll whose density follows the rate of change | x of the counter | on the digit change | 11 |

### Heard without covering the voice

- Owner, 2026-09-28 (sổ gu G-006): the voice comes first; the data sounds must not cover it; never solved by raising the level (no +10 dB).
- Side-chain: the whole data layer ducks 8 dB while the voice is active (20 ms attack, 250 ms release).
- Band: while the voice is active the data layer loses 1-4 kHz (the speech band) almost entirely; its energy there stays 31-56 dB under the voice on the sample.
- Timing: notes that would start while a syllable sounds move to the quietest instant within -60..+120 ms (a gap between syllables); decisive numbers still appear on the frame they are spoken (C13 +-250 ms); line draws start in the breath before the sentence.
- Level: loudness-matched at -16 dB under the voice (before the side-chain), about -21 dB overall on the sample; final level set by the owner's ear.
- Conflict noted: rule T1 (>= 1 dB lift in 1.5-8 kHz inside spoken-number windows) is not met this way; for Episode 1 the owner's taste wins (episodes/ep001/checks-notes.md).

Measured on the 10 s sample, blind palettes (review-m1/sonify-metrics.json): data layer about -21 dB under the voice; 1-4 kHz while speaking 31-56 dB under the voice; T1-style lift median 0 dB (up to 6.6 dB in voice pauses). The m0 version at +10 dB (-6 dB under the voice) was judged by the owner to cover the voice.
