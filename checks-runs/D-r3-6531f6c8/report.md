# checks/ report

root: `/home/user/work/dbranch/out/m3/root`  
lock: `62b5206df11327e50f3cca6a5d902dc988efb0bd8d27b5322dcbdf77cc4fac96`  
master SHA-256: `6531f6c8e1d11473251156875ad5631ecc2b6768517eab47d4ab8756735e3b62`  
{'PASS': 59, 'FAIL': 16, 'MISSING': 0, 'ERROR': 0}

| rule | § | status | failing metrics |
|---|---|---|---|
| F01 | DX-F1, DX-F2 | PASS |  |
| F02 | DX-F1 | PASS |  |
| F03 | DX-F3 | PASS |  |
| F04 | DX-F2 | PASS |  |
| F05 | DX-F2 | PASS |  |
| F06 | DX-F4 | PASS |  |
| F07 | DX-S1 (CH §1 length) | PASS |  |
| F08 | DX-V5 | PASS |  |
| F09 | DX-F5 | PASS |  |
| F10 | DX-F6 | PASS |  |
| A01 | DX-A10 | PASS |  |
| A02 | DX-A10 | PASS |  |
| A03 | DX-A10 | PASS |  |
| A04 | DX-A10 | PASS |  |
| A05 | DX-A10 | PASS |  |
| A06 | DX-A10, DX-X5 | PASS |  |
| A07 | DX-A9 | PASS |  |
| A08 | DX-A9 | PASS |  |
| A09 | DX-R6 | PASS |  |
| A10 | DX-A5 | PASS |  |
| A11 | DX-A5 | PASS |  |
| A12 | DX-A3 | PASS |  |
| A13 | DX-A7 | PASS |  |
| A14 | DX-A7 | PASS |  |
| A15 | DX-A7 | FAIL | wpm act cold-open = 161.157025 (need in [150.0, 160.0]); wpm act act1 = 148.275018 (need in [150.0, 160.0]); wpm act act2 = 146.750146 (need in [150.0, 160.0]); wpm act act3 = 142.752562 (need in [150.0, 160.0]); wpm act method = 149.821641 (need in [150.0, 160.0]); wpm act outro = 161.538462 (need in [150.0, 160.0]); sentences > 175 wpm = 14 (need <= 0) |
| S01 | DX-H1 | PASS |  |
| S02 | DX-H1 | PASS |  |
| S03 | DX-H4 | PASS |  |
| S04 | DX-H5 | FAIL | used years missing in a source = 3 (need <= 0) |
| S05 | DX-H1, DX-H2 | PASS |  |
| S06 | DX-H6 | PASS |  |
| S07 | DX-H1, DX-H2 | PASS |  |
| S08 | DX-H2 | PASS |  |
| S09 | DX-H3 | PASS |  |
| S10 | DX-I1, DX-I2 | PASS |  |
| S11 | DX-S6 | PASS |  |
| S12 | DX-S7 | FAIL | max new numbers in a scene = 4 (need <= 2) |
| S13 | DX-S8 | PASS |  |
| S14 | DX-S10 | PASS |  |
| S15 | DX-S1 | PASS |  |
| R01 | DX-R1 | FAIL | false peaks = 2 (need <= 0); peaks without valley = 1 (need <= 0) |
| R02 | DX-R2 | PASS |  |
| R03 | DX-R3 | PASS |  |
| R04 | DX-R4 | PASS |  |
| R05 | DX-R5 | PASS |  |
| R06 | DX-V10 (picture check of cuts) | FAIL | cuts visible in picture (%) = 70.588235 (need >= 90.0) |
| V01 | DX-V12 | PASS |  |
| V02 | DX-V1 | PASS |  |
| V03 | DX-V3 | FAIL | text outside safe area = 32 (need <= 0) |
| V04 | DX-V4, DX-X3 | FAIL | 1966 colour share = 0.939977 (need >= 0.95) |
| V05 | DX-V8 | FAIL | worst ease ratio = 0.65 (need <= 0.4); overshoot > 8% = 3 (need <= 0) |
| V08 | DX-V6 | FAIL | worst text contrast = 1.02 (need >= 4.5); samples below 4.5:1 = 59 (need <= 0) |
| V09 | DX-V4, DX-X3 | PASS |  |
| V10 | DX-V10 | PASS |  |
| V11 | DX-V11 (C rule text-line-collision, upgraded to pixels) | FAIL | text collisions = 48 (need <= 0) |
| V12 | DX-V9 (replaces the camera-move exemption) | FAIL | text samples below NCC 0.97 = 110 (need <= 0) |
| V13 | DX-V9, DX-V8 (replaces the camera-move exemption) | PASS |  |
| C01 | DX-V11 (C rule scene-leak) | PASS |  |
| C02 | DX-V11 (C rule bg-over-data) | PASS |  |
| C03 | DX-V11 (C rule unlabelled-curve) | PASS |  |
| C04 | DX-V11 (C rule axis-anchors) | PASS |  |
| C05 | DX-V11, DX-X4 (C rule grey-emphasis) | PASS |  |
| C06 | DX-V11 (C rule number-colour) | PASS |  |
| C07 | DX-V11 (C rule bar-proportion) | FAIL | frames flagged = 40 (need <= 0) |
| C10 | DX-V1 (C rule level1) | PASS |  |
| C11 | DX-V11 (C rule layout-repeat) | PASS |  |
| C12 | DX-V11 (C rule split-view) | PASS |  |
| C13 | DX-V11 (number–voice sync ±250 ms) | FAIL | worst |offset| ms = 637 (need <= 250.0); pairs > 250 ms = 3 (need <= 0) |
| C14 | DX-V11, DX-X4 (legible at 25%) | PASS |  |
| C15 | DX-V5 (C rule tokens only) | PASS |  |
| P01 | DX-P2 | PASS |  |
| T1 | DX-A1 (sổ gu G-001) | FAIL | windows not audible = 306 (need <= 0); data sounds delivered as their own stem (sonify) = False (need == True) |
| T2 | DX-A2 (sổ gu G-002) | FAIL | repeated phrases (%) = 5.882353 (need <= 5.0) |
| T3 | DX-R6 (sổ gu G-003) | PASS |  |
| REG | CH §5, §4 khâu 3 (cổng hồi quy) | FAIL | regressions = 1 (need <= 0) |

## Metrics within 5% of a threshold

- A12 accents on a cut (%) = 100.0 (threshold >= 100.0)
- A15 wpm act cold-open = 161.157025 (threshold in [150.0, 160.0])
- A15 wpm act act1 = 148.275018 (threshold in [150.0, 160.0])
- A15 wpm act act2 = 146.750146 (threshold in [150.0, 160.0])
- A15 wpm act act3 = 142.752562 (threshold in [150.0, 160.0])
- A15 wpm act method = 149.821641 (threshold in [150.0, 160.0])
- A15 wpm act outro = 161.538462 (threshold in [150.0, 160.0])
- S04 stocks tolerance pp = 0.5 (threshold <= 0.5)
- S05 geomean claims shown = 2 (threshold >= 2)
- S06 start years shown in act 3 = 69 (threshold >= 69)
- S11 core claims = 1 (threshold >= 1)
- S11 g1966 callbacks w/ distinct meaning = 3 (threshold >= 3)
- S14 ad breaks = 2 (threshold in [2, 3])
- S15 cold open s = 14.83 (threshold <= 15.0)
- R01 acts with climax peak = 3 (threshold >= 3)
- R05 act-2 last/first mean = 0.777353 (threshold <= 0.8)
- V04 sides used = 1 (threshold <= 1)
- V04 1966 colour share = 0.939977 (threshold >= 0.95)
- P01 thumb 1 token share (%) = 100.0 (threshold >= 97.0)
- P01 thumb 2 token share (%) = 100.0 (threshold >= 97.0)
- P01 thumb 3 token share (%) = 100.0 (threshold >= 97.0)
- T2 longest run of repeated phrases = 1 (threshold <= 1)
