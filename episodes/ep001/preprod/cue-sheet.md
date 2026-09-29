# Episode 1 — cue sheet (Stage 4b, script v2)

Planned length **12.29 min** (737.2 s) from the V8 takes. Music is generated in code; no third-party audio.

## Music cues

| t (s) | end | layer | key | tempo | dramatic function |
|---|---|---|---|---|---|
| 0.0 | 26.6 | music | D minor | 72 | suspense under the open question: pad and low pulse, no melody |
| 26.6 | 29.6 | music | D minor | 72 | ident sting over the long rate-line tone |
| 29.6 | 219.7 | music | D minor | 84 | curious, light pulse; Nora's motif (piano) |
| 219.7 | 392.5 | music | D minor | 92 | build through the balance gap to the quarter-point climax (S19), release on the full point |
| 392.5 | 648.3 | music | F major | 88 | Walt (low plucks), Anjali (high bells); resolves on the three-line answer (S29) |
| 648.3 | 696.6 | music | F major | 70 | thin pad under the method cards |
| 696.6 | 737.2 | music | F major | 76 | resolved; three motifs together; tail into the end screen |
| 184.8 | 204.8 | music-dynamics | D minor | 84 | build to the act1 climax |
| 315.8 | 335.8 | music-dynamics | D minor | 92 | build to the act2 climax |
| 548.7 | 568.7 | music-dynamics | F major | 88 | build to the act3 climax |

## Intentional silences (script pauses; ~300 ms release in, room tone floor)

| t (s) | length | after | why |
|---|---|---|---|
| 131.64 | 1.0 s | `S09.2` | script pause after S09.2 |
| 200.26 | 1.0 s | `S12.4` | script pause after S12.4 |
| 218.57 | 1.2 s | `S13.5` | ad break |
| 288.68 | 1.0 s | `S16.1` | script pause after S16.1 |
| 308.81 | 1.0 s | `S17.1` | script pause after S17.1 |
| 329.17 | 1.0 s | `S18.2` | script pause after S18.2 |
| 343.23 | 1.2 s | `S19.1` | script pause after S19.1 |
| 352.79 | 1.0 s | `S20.1` | script pause after S20.1 |
| 380.44 | 1.0 s | `S21.3` | script pause after S21.3 |
| 391.34 | 1.2 s | `S21.6` | ad break |
| 422.32 | 1.0 s | `S22.5` | script pause after S22.5 |
| 446.31 | 1.0 s | `S23.3` | script pause after S23.3 |
| 461.77 | 1.0 s | `S24.2` | script pause after S24.2 |
| 478.17 | 1.0 s | `S25.1` | script pause after S25.1 |
| 502.42 | 1.0 s | `S26.1` | script pause after S26.1 |
| 554.22 | 1.0 s | `S28.1` | script pause after S28.1 |
| 596.50 | 1.0 s | `S29.7` | script pause after S29.7 |
| 624.68 | 1.0 s | `S30.3` | script pause after S30.3 |
| 631.18 | 1.0 s | `S31.1` | script pause after S31.1 |

Ad breaks: 219.1 s, 391.9 s (end of act 1, end of act 2).

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
