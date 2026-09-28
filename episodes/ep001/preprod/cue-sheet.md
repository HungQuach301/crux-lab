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
- every spoken number: music and sfx dip from 0.5 s before to 1.6 s after (DX-A6). The data sounds are NOT dipped there (see below).

## Data sonification plan (DX-A1, sổ gu G-001), per element type

| element | sound | band | pan | timing | scenes using it |
|---|---|---|---|---|---|
| bar | rising bright tone into its pitch while the bar grows; pitch = value on one fixed scale for the film (MIDI 72-96, D minor pentatonic); lasts the growth | partials 2-5 at 1.5-6 kHz; fundamental 0.5-1.2 kHz | x of the bar | starts on the frame the bar starts to grow | 18 |
| line | continuous tone, pitch follows the slope at the drawing tip (rising line = higher), light 6 Hz shimmer; one run per drawing stroke | partials at 2-6 kHz, fundamental 0.8-1.6 kHz | x of the tip | starts on the frame the line appears; stops when the tip stops | 13 |
| dot | short bright pluck (110 ms decay), pitch from the dot height (higher on screen = higher) | partials 2-5 kHz | x of the dot | on the frame the dot appears | 28 |
| counter | tick (30 ms click, 3-8 kHz) per value change; above 8 changes/s the ticks merge into a soft roll whose density follows the rate of change | 3-8 kHz | x of the counter | each tick on the frame the digit changes | 11 |

### Heard without covering the voice

- Frequency: the data sounds carry their energy in 1.5-8 kHz but mostly ABOVE the voice formants (2.5-6 kHz partials, fundamentals kept high), so they sit beside the voice rather than on it.
- Mix carve, while a data sound plays (side-chain from the sonify stem, 20 ms attack, 120 ms release): music -9 dB in 1.5-8 kHz; voice -3 dB in 2.5-6 kHz only (a narrow, short dip, not a duck of the whole voice). The voice stays the loudest element (DX-A9).
- Timing without breaking C13: the decisive numbers still appear on the frame they are spoken (+-250 ms). Other chart changes that do not carry a spoken number start on the nearest gap between words (ASR word timings; gaps >= 80 ms within +-200 ms of the planned frame); line draws start in the breath before the sentence (the picture leads the words, DX-S3).
- Inside spoken-number windows the checker asks >= 1 dB lift, elsewhere >= 3 dB; level not final: the owner sets it by ear on a phone speaker (H8).
- Built at M2 in toolkit/audio/d_m2_audio.py (sonify stem, band dip); measured before the owner listens with the builder's own T1-style measure.

Measured at A-M0 on the 10 s sample (builder's own T1-style measure): with the data sounds 6 dB under the voice, the lift in 1.5-8 kHz was 1.4-7.9 dB during speech and 17-28 dB in pauses. The band carve above is new at M1 and is measured at M2 before the owner listens.
