# Episode 1 — cue sheet (Stage 4b, script v2)

Planned length **12.36 min** (741.5 s) from the V8 takes. Music is generated in code; no third-party audio.

## Music cues

| t (s) | end | layer | key | tempo | dramatic function |
|---|---|---|---|---|---|
| 0.0 | 21.9 | music | D minor | 72 | suspense under the open question: pad and low pulse, no melody |
| 21.9 | 24.9 | music | D minor | 72 | ident sting over the long rate-line tone |
| 24.9 | 219.2 | music | D minor | 84 | curious, light pulse; Nora's motif (piano) |
| 219.2 | 396.5 | music | D minor | 92 | build through the balance gap to the quarter-point climax (S19), release on the full point |
| 396.5 | 652.6 | music | F major | 88 | Walt (low plucks), Anjali (high bells); resolves on the three-line answer (S29) |
| 652.6 | 701.0 | music | F major | 70 | thin pad under the method cards |
| 701.0 | 741.5 | music | F major | 76 | resolved; three motifs together; tail into the end screen |
| 184.3 | 204.3 | music-dynamics | D minor | 84 | build to the act1 climax |
| 318.2 | 338.2 | music-dynamics | D minor | 92 | build to the act2 climax |
| 553.3 | 573.3 | music-dynamics | F major | 88 | build to the act3 climax |

## Intentional silences (script pauses; ~300 ms release in, room tone floor)

| t (s) | length | after | why |
|---|---|---|---|
| 126.77 | 1.0 s | `S09.2` | script pause after S09.2 |
| 199.77 | 1.0 s | `S12.4` | script pause after S12.4 |
| 218.08 | 1.2 s | `S13.5` | ad break |
| 288.94 | 1.0 s | `S16.1` | script pause after S16.1 |
| 309.27 | 1.0 s | `S17.1` | script pause after S17.1 |
| 330.16 | 1.0 s | `S18.2` | script pause after S18.2 |
| 345.38 | 1.2 s | `S19.1` | script pause after S19.1 |
| 355.66 | 1.0 s | `S20.1` | script pause after S20.1 |
| 384.46 | 1.0 s | `S21.3` | script pause after S21.3 |
| 395.36 | 1.2 s | `S21.6` | ad break |
| 426.34 | 1.0 s | `S22.5` | script pause after S22.5 |
| 450.33 | 1.0 s | `S23.3` | script pause after S23.3 |
| 465.79 | 1.0 s | `S24.2` | script pause after S24.2 |
| 482.19 | 1.0 s | `S25.1` | script pause after S25.1 |
| 506.94 | 1.0 s | `S26.1` | script pause after S26.1 |
| 558.78 | 1.0 s | `S28.1` | script pause after S28.1 |
| 601.06 | 1.0 s | `S29.7` | script pause after S29.7 |
| 629.24 | 1.0 s | `S30.3` | script pause after S30.3 |
| 635.51 | 1.0 s | `S31.1` | script pause after S31.1 |

Ad breaks: 218.6 s, 395.9 s (end of act 1, end of act 2).

## Data sonification plan (sổ gu G-001, G-005, G-006)

Timbre: **S2**, palette `minimal` of `toolkit/audio/sonify_palettes.py` (owner's pick, 2026-09-28): soft filtered tick (4.5-7 kHz) + low pulse (MIDI 36-60). Bands for T1: 60-270 Hz + 4.5-7 kHz.

| element | timbre | value mapping | pan | timing | scenes using it |
|---|---|---|---|---|---|
| bar | S2 'minimal' (owner's pick, 2026-09-28): a soft low pulse at the value's pitch (MIDI 36-60, D minor pentatonic) with a soft filtered tick (4.5-7 kHz) at the start | pitch = bar value on one fixed scale for the film, snapped to the music key; lasts while the bar grows | x of the bar | starts when the bar starts to grow (moved into the nearest syllable gap if the voice is sounding) | 11 |
| line | S2: soft low pulses on eighth notes while the tip moves, pitch following the slope, each with a faint filtered tick | pitch follows the slope at the drawing tip (rising line = higher) | x of the tip | while the tip moves; notes land in syllable gaps | 5 |
| dot | S2: one deeper pulse, pitch from the dot height, plus a soft filtered tick | pitch from the dot height on screen | x of the dot | on the frame the dot appears (nearest syllable gap, -60..+120 ms) | 12 |
| counter | S2: a soft filtered tick per value change; above 8 changes/s the ticks merge into a soft roll | one event per value change | x of the counter | on the digit change | 5 |

### Heard without covering the voice

- Owner, 2026-09-28 (sổ gu G-006): the voice comes first; the data sounds must not cover it; never solved by raising the level.
- Side-chain: the whole data layer ducks 8 dB while the voice is active (20 ms attack, 250 ms release).
- Band: while the voice is active the data layer loses 1-4 kHz (the speech band) almost entirely.
- Timing: notes that would start while a syllable sounds move to the quietest instant within -60..+120 ms.
- Level: -16 dB under the voice before the side-chain (toolkit/audio/sonify_palettes.py); never raised.
