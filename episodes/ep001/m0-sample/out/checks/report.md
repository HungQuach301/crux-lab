# checks/ report

root: `/home/user/crux-lab/episodes/ep001/m0-sample`  
lock: `b97bfc6bb6524e9fd108e708aa96a01c19c965b42cf9bcda9d2e9d7ce738fe74`  
master SHA-256: `82ba6767b35660de440150eecf3a12c9a37b3b5dade5ffc0126d7d318df8be70`  
{'PASS': 41, 'FAIL': 29, 'MISSING': 5, 'ERROR': 0}

| rule | § | status | failing metrics |
|---|---|---|---|
| F01 | DX-F1, DX-F2 | PASS |  |
| F02 | DX-F1 | PASS |  |
| F03 | DX-F3 | PASS |  |
| F04 | DX-F2 | PASS |  |
| F05 | DX-F2 | PASS |  |
| F06 | DX-F4 | PASS |  |
| F07 | DX-S1 (CH §1 length) | FAIL | duration s = 10.0 (need >= 600.0) |
| F08 | DX-V5 | PASS |  |
| F09 | DX-F5 | PASS |  |
| F10 | DX-F6 | FAIL | chapters = 1 (need >= 3) |
| A01 | DX-A10 | PASS |  |
| A02 | DX-A10 | PASS |  |
| A03 | DX-A10 | FAIL | LRA LU = 2.5 (need in [6.0, 10.0]) |
| A04 | DX-A10 | PASS |  |
| A05 | DX-A10 | PASS |  |
| A06 | DX-A10, DX-X5 | PASS |  |
| A07 | DX-A9 | PASS |  |
| A08 | DX-A9 | FAIL | onsets measured = 1 (need >= 3) |
| A09 | DX-R6 | FAIL | silences 0.8-1.5 s = 0 (need >= 3) |
| A10 | DX-A5 | FAIL | camera moves = 1 (need >= 5) |
| A11 | DX-A5 | FAIL | events measured = 2 (need >= 8); Pearson pan~x = None (need >= 0.7) |
| A12 | DX-A3 | FAIL | accents = 0 (need >= 5); accents on a cut (%) = None (need >= 100.0); accents confirmed by onset (%) = None (need >= 90.0); beats confirmed by onset (%) = 33.333333 (need >= 70.0) |
| A13 | DX-A7 | PASS |  |
| A14 | DX-A7 | PASS |  |
| A15 | DX-A7 | FAIL | wpm act cold-open = 149.122807 (need in [150.0, 160.0]) |
| S01 | DX-H1 | MISSING | artifact missing: out/model.json |
| S02 | DX-H1 | FAIL | no-tax in method card = False (need == True); no-fee in method card = False (need == True); no-tax on screen elsewhere = False (need == True); no-fee on screen elsewhere = False (need == True) |
| S03 | DX-H4 | MISSING | artifact missing: data/sources.json |
| S04 | DX-H5 | MISSING | artifact missing: data/sources.json |
| S05 | DX-H1, DX-H2 | MISSING | artifact missing: data/normalized/annual.csv |
| S06 | DX-H6 | FAIL | start years shown in act 3 = 0 (need >= 69) |
| S07 | DX-H1, DX-H2 | PASS |  |
| S08 | DX-H2 | PASS |  |
| S09 | DX-H3 | PASS |  |
| S10 | DX-I1, DX-I2 | FAIL | "US only" stated = False (need == True); "history, not a forecast" stated = False (need == True) |
| S11 | DX-S6 | FAIL | core claims = 0 (need >= 1) |
| S12 | DX-S7 | FAIL | new numbers = 4 (need <= 1.25); max new numbers in a scene = 4 (need <= 2) |
| S13 | DX-S8 | FAIL | sentence length CV = 0.0 (need >= 0.35) |
| S14 | DX-S10 | FAIL | ad breaks = 0 (need in [2, 3]) |
| S15 | DX-S1 | FAIL | act order = ['cold-open'] (need == ['cold-open', 'ident', 'act1', 'act2', 'act3', 'method', 'outro']); ident s = None (need <= 3.0); outro s = None (need >= 20.0); total s = 10.0 (need >= 600.0) |
| R01 | DX-R1 | FAIL | r cut rate = 0.0 (need >= 0.8); acts with climax peak = 0 (need >= 3) |
| R02 | DX-R2 | PASS |  |
| R03 | DX-R3 | FAIL | shortest pause s = 0.54 (need >= 1.0); pauses < 1.0 s = 1 (need <= 0) |
| R04 | DX-R4 | FAIL | cuts on beat/action (%) = None (need >= 70.0) |
| R05 | DX-R5 | FAIL | shot length CV = 0.0 (need >= 0.4); act-2 scenes before climax = 0 (need >= 6) |
| R06 | DX-V10 (picture check of cuts) | FAIL | cuts = 0 (need >= 1); cuts visible in picture (%) = None (need >= 90.0) |
| V01 | DX-V12 | PASS |  |
| V02 | DX-V1 | PASS |  |
| V03 | DX-V3 | PASS |  |
| V04 | DX-V4, DX-X3 | FAIL | both characters seen = False (need == True); side samples = 0 (need >= 1) |
| V05 | DX-V8 | FAIL | camera moves = 1 (need >= 5); anticipation in moves ≥1 s (%) = None (need >= 30.0); overshoot in moves ≥1 s (%) = None (need >= 30.0) |
| V08 | DX-V6 | PASS |  |
| V09 | DX-V4, DX-X3 | FAIL | both characters seen on screen = False (need == True) |
| V10 | DX-V10 | FAIL | verified match cuts = 0 (need >= 5); verified J/L cuts = 0 (need >= 4) |
| V11 | DX-V11 (C rule text-line-collision, upgraded to pixels) | PASS |  |
| V12 | DX-V9 (replaces the camera-move exemption) | PASS |  |
| V13 | DX-V9, DX-V8 (replaces the camera-move exemption) | PASS |  |
| C01 | DX-V11 (C rule scene-leak) | PASS |  |
| C02 | DX-V11 (C rule bg-over-data) | PASS |  |
| C03 | DX-V11 (C rule unlabelled-curve) | PASS |  |
| C04 | DX-V11 (C rule axis-anchors) | PASS |  |
| C05 | DX-V11, DX-X4 (C rule grey-emphasis) | PASS |  |
| C06 | DX-V11 (C rule number-colour) | PASS |  |
| C07 | DX-V11 (C rule bar-proportion) | PASS |  |
| C10 | DX-V1 (C rule level1) | PASS |  |
| C11 | DX-V11 (C rule layout-repeat) | PASS |  |
| C12 | DX-V11 (C rule split-view) | PASS |  |
| C13 | DX-V11 (number–voice sync ±250 ms) | PASS |  |
| C14 | DX-V11, DX-X4 (legible at 25%) | PASS |  |
| C15 | DX-V5 (C rule tokens only) | PASS |  |
| P01 | DX-P2 | MISSING | artifact missing: out/package/thumb-1.png |
| T1 | DX-A1 (sổ gu G-001) | FAIL | windows not audible = 1 (need <= 0) |
| T2 | DX-A2 (sổ gu G-002) | FAIL | phrases measured = 0 (need >= 8); repeated phrases (%) = None (need <= 5.0) |
| T3 | DX-R6 (sổ gu G-003) | FAIL | silences measured = 0 (need >= 1) |
| REG | CH §5, §4 khâu 3 (cổng hồi quy) | PASS | first version: nothing to compare |

## Metrics within 5% of a threshold

- F10 shortest chapter s = 10.0 (threshold >= 10.0)
- A13 takes = 1 (threshold >= 1)
- A15 wpm act cold-open = 149.122807 (threshold in [150.0, 160.0])
- R03 decisive claims = 1 (threshold >= 1)
- V01 shots = 1 (threshold >= 1)
