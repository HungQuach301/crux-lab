# Episode 1 — cue sheet (M1 plan)

Planned length **10.49 min** (629.1 s) from the table-read takes. Music is generated in code (toolkit/audio/d_m2_audio.py, one reverb space, per-act arrangement); no third-party audio.

## Music cues

| t (s) | end | layer | key | tempo | dramatic function |
|---|---|---|---|---|---|
| 0.0 | 14.7 | music | A minor | 72 | suspense under the open question; pad + pulse, no melody |
| 14.7 | 17.7 | music | A minor | 72 | ident sting |
| 17.7 | 177.7 | music | C major | 84 | curious, light pulse; the three households get motifs (Dan: low plucks, Maya: piano, Priya: high bells) |
| 177.7 | 337.1 | music | D minor | 92 | building to the thesis (a2-real: 24 becomes 30), valley after it; re-voiced at Dan's and Priya's positions |
| 337.1 | 537.2 | music | F major | 88 | history: darker at the further-drop turn, resolves on the answer |
| 537.2 | 580.5 | music | F major | 70 | thin pad under the method card |
| 580.5 | 629.1 | music | C major | 76 | resolved; both motifs together |
| 84.2 | 104.2 | music-dynamics | C major | 84 | build to the act1 climax (+6 dB over 20 s) |
| 197.4 | 217.4 | music-dynamics | D minor | 92 | build to the act2 climax (+6 dB over 20 s) |
| 453.8 | 473.8 | music-dynamics | F major | 88 | build to the act3 climax (+6 dB over 20 s) |

## Intentional silences (DX-R6: ~300 ms release in, room tone floor, back in 200 ms)

| t (s) | length | after | why |
|---|---|---|---|
| 68.62 | 1.2 s | `a1-median.1` | Maya's bill is the national median: let it land |
| 175.92 | 1.6 s | `a1-payoff.1` | end of act 1: ad break |
| 222.59 | 1.3 s | `a2-real.1` | the thesis lands: 24 becomes 30 |
| 335.24 | 1.6 s | `a2-payoff.1` | end of act 2: ad break |
| 482.87 | 1.3 s | `a3-answer2.1` | the answer lands |

Ad breaks (DX-S10): 176.7 s, 336.0 s, inside the act1|act2 and act2|act3 silences.

## Sound design

- whoosh per camera move, level from peak speed (A10); riser into each reveal; impact on the decisive numbers (`cost_med`, `sp36_mid`); room tone throughout.
- every spoken number: music and sfx dip from 0.5 s before to 1.6 s after (DX-A6); the data sounds follow the voice side-chain below.

## Data sonification plan (DX-A1, sổ gu G-001, G-005, G-006), per element type

Timbre: **S2**, chosen by the owner in the blind test on a phone speaker (sổ gu G-005, 2026-09-28): palette `minimal` of `toolkit/audio/sonify_palettes.py`, soft filtered tick + low pulse. "S2 không lấn lời."

| element | timbre | value mapping | pan | timing | scenes using it |
|---|---|---|---|---|---|
| bar | S2 (owner's pick, 2026-09-28): a soft low pulse at the value's pitch (MIDI 36-60, D minor pentatonic) with a soft filtered tick (4.5-7 kHz) at the start | pitch = bar value on one fixed scale for the film, snapped to the music key; lasts while the bar grows | x of the bar | starts when the bar starts to grow (moved into the nearest syllable gap if the voice is sounding) | 19 |
| line | S2: soft low pulses on eighth notes of the music tempo while the tip moves, pitch following the slope, each with a faint filtered tick | pitch follows the slope at the drawing tip (rising line = higher), snapped to the music key | x of the tip | while the tip moves; discrete notes of a run land in syllable gaps | 9 |
| dot | S2: one deeper pulse, pitch from the dot height, plus a soft filtered tick | pitch from the dot height on screen (higher = higher) | x of the dot | on the frame the dot appears (nearest syllable gap, -60..+120 ms, when the voice is sounding) | 20 |
| counter | S2: a soft filtered tick per value change; above 8 changes/s the ticks merge into a soft roll | one soft event per value change; > 8 changes/s merge into one roll whose density follows the rate of change | x of the counter | on the digit change | 15 |

### Heard without covering the voice

- Owner, 2026-09-28 (sổ gu G-006): the voice comes first; the data sounds must not cover it; never solved by raising the level (no +10 dB).
- Side-chain: the whole data layer ducks 8 dB while the voice is active (20 ms attack, 250 ms release).
- Band: while the voice is active the data layer loses 1-4 kHz (the speech band) almost entirely; its energy there stays 31-56 dB under the voice on the sample.
- Timing: notes that would start while a syllable sounds move to the quietest instant within -60..+120 ms (a gap between syllables); decisive numbers still appear on the frame they are spoken (C13 +-250 ms); line draws start in the breath before the sentence.
- Level: loudness-matched at -16 dB under the voice (before the side-chain), about -21 dB overall on the sample; final level set by the owner's ear.
- Conflict noted: rule T1 (>= 1 dB lift in 1.5-8 kHz inside spoken-number windows) is not met this way; for Episode 1 the owner's taste wins (episodes/ep001/checks-notes.md).

Measured on the 10 s sample, blind palettes (review-m1/sonify-metrics.json): data layer about -21 dB under the voice; 1-4 kHz while speaking 31-56 dB under the voice; T1-style lift median 0 dB (up to 6.6 dB in voice pauses). The m0 version at +10 dB (-6 dB under the voice) was judged by the owner to cover the voice.
