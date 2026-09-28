# checks/ report

root: `episodes/ep001/m0-sample (branch ep001, copied)`  
lock: `f9e24c91a464b1948f6eabb08d6da05d5867f78d2fe7ce1f818ec92009f0dcdd`  
master SHA-256: `None`  
{'PASS': 26, 'FAIL': 15, 'MISSING': 37, 'ERROR': 0}

| rule | § | status | failing metrics |
|---|---|---|---|
| F01 | DX-F1, DX-F2 | MISSING | artifact missing: out/video.mp4 |
| F02 | DX-F1 | MISSING | artifact missing: out/video.mp4 |
| F03 | DX-F3 | MISSING | artifact missing: out/video.mp4 |
| F04 | DX-F2 | MISSING | artifact missing: out/video.mp4 |
| F05 | DX-F2 | MISSING | artifact missing: out/video.mp4 |
| F06 | DX-F4 | MISSING | artifact missing: out/video.mp4 |
| F07 | DX-S1 (CH §1 length) | MISSING | artifact missing: out/video.mp4 |
| F08 | DX-V5 | MISSING | artifact missing: out/video.mp4 |
| F09 | DX-F5 | PASS |  |
| F10 | DX-F6 | MISSING | artifact missing: out/video.mp4 |
| F11 | CH §4 khâu 3 (hợp đồng tập, K2) | MISSING | artifact missing: contract.json: artefacts.M3 |
| A01 | DX-A10 | MISSING | artifact missing: out/video.mp4 |
| A02 | DX-A10 | MISSING | artifact missing: out/video.mp4 |
| A03 | DX-A10 | MISSING | artifact missing: out/video.mp4 |
| A04 | DX-A10 | MISSING | artifact missing: out/video.mp4 |
| A05 | DX-A10 | MISSING | artifact missing: out/video.mp4 |
| A06 | DX-A10, DX-X5 | MISSING | artifact missing: out/video.mp4 |
| A07 | DX-A9 | PASS |  |
| A08 | DX-A9 | FAIL | onsets measured = 1 (need >= 3) |
| A09 | DX-R6 | MISSING | artifact missing: out/video.mp4 |
| A10 | DX-A5 | FAIL | camera moves = 1 (need >= 5) |
| A11 | DX-A5 | FAIL | events measured = 2 (need >= 8); Pearson pan~x = None (need >= 0.7) |
| A12 | DX-A3 | FAIL | accents = 0 (need >= 5); accents on a cut (%) = None (need >= 100.0); accents confirmed by onset (%) = None (need >= 90.0); beats confirmed by onset (%) = 33.333333 (need >= 70.0) |
| A13 | DX-A7 | PASS |  |
| A14 | DX-A7 | MISSING | artifact missing: out/video.mp4 |
| A15 | DX-A7 | MISSING | artifact missing: out/video.mp4 |
| S01 | DX-H1 | MISSING | artifact missing: contract.json: model.kind |
| S02 | DX-H1 | FAIL | no-tax in method card = False (need == True); no-fee in method card = False (need == True); no-tax on screen elsewhere = False (need == True); no-fee on screen elsewhere = False (need == True) |
| S03 | DX-H4 | MISSING | artifact missing: contract.json: data.sources |
| S04 | DX-H5 | MISSING | artifact missing: contract.json: data.crosscheck |
| S05 | DX-H1, DX-H2 | MISSING | artifact missing: contract.json: model.kind |
| S06 | DX-H6 | MISSING | artifact missing: contract.json: coverage |
| S07 | DX-H1, DX-H2 | PASS |  |
| S08 | DX-H2 | PASS |  |
| S09 | DX-H3 | PASS |  |
| S10 | DX-I1, DX-I2 | FAIL | "US only" stated = False (need == True); "history, not a forecast" stated = False (need == True) |
| S11 | DX-S6 | MISSING | artifact missing: out/video.mp4 |
| S12 | DX-S7 | FAIL | new numbers = 4 (need <= 1.25); max new numbers in a scene = 4 (need <= 2) |
| S13 | DX-S8 (sổ gu G-009) | FAIL | sentence length CV (≥ 4 words) = 0.0 (need >= 0.35) |
| S14 | DX-S10 | MISSING | artifact missing: out/video.mp4 |
| S15 | DX-S1 | FAIL | act order = ['cold-open'] (need == ['cold-open', 'ident', 'act1', 'act2', 'act3', 'method', 'outro']); ident s = None (need <= 3.0); outro s = None (need >= 20.0); total s = 10.0 (need >= 600.0) |
| S16 | DX-S3, RUBRIC H4 (sổ gu G-008) | MISSING | artifact missing: contract.json: characters.maya.words |
| R01 | DX-R1 | FAIL | r cut rate = 0.0 (need >= 0.8); acts with climax peak = 0 (need >= 3) |
| R02 | DX-R2 | PASS |  |
| R03 | DX-R3 | MISSING | artifact missing: out/video.mp4 |
| R04 | DX-R4 | FAIL | cuts on beat/action (%) = None (need >= 70.0) |
| R05 | DX-R5 | FAIL | shot length CV = 0.0 (need >= 0.4); act-2 scenes before climax = 0 (need >= 6) |
| R06 | DX-V10 (picture check of cuts) | MISSING | artifact missing: out/video.mp4 |
| V01 | DX-V12 | PASS |  |
| V02 | DX-V1 | PASS |  |
| V03 | DX-V3 | PASS |  |
| V04 | DX-V4, DX-X3 | MISSING | artifact missing: design/tokens.json colour token "cmedian" (contract characters.maya.color) |
| V05 | DX-V8 | MISSING | artifact missing: out/video.mp4 |
| V08 | DX-V6 | PASS |  |
| V09 | DX-V4, DX-X3 | MISSING | artifact missing: design/tokens.json colour token "cmedian" (contract characters.maya.color) |
| V10 | DX-V10 | MISSING | artifact missing: out/video.mp4 |
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
| C13 | DX-V11 (number–voice sync ±250 ms) | MISSING | artifact missing: out/video.mp4 |
| C14 | DX-V11, DX-X4 (legible at 25%) | PASS |  |
| C15 | DX-V5 (C rule tokens only) | PASS |  |
| P01 | DX-P2 | MISSING | artifact missing: out/package/thumb-1.png |
| T1 | DX-A1 (sổ gu G-001, G-006) | MISSING | artifact missing: contract.json: sonification.bandsHz |
| T2 | DX-A2 (sổ gu G-002) | FAIL | phrases measured = 0 (need >= 8); repeated phrases (%) = None (need <= 5.0) |
| T3 | DX-R6 (sổ gu G-003) | MISSING | artifact missing: out/video.mp4 |
| L1 | DX-A1, DX-A9 (sổ gu G-006) | FAIL | voice/data 1–4 kHz ratio, 10th percentile (dB) = -17.911347 (need >= 20.0) |
| REG | CH §5, §4 khâu 3 (cổng hồi quy) | FAIL | regressions = 14 (need <= 0) |

## Metrics within 5% of a threshold

- A13 takes = 1 (threshold >= 1)
- V01 shots = 1 (threshold >= 1)
