# checks/ report

root: `/home/user/crux-lab/episodes/ep001`  
lock: `beffb49be5917559419867513257b37c4ae827581db00039abb53804aaf2bb33`  
master SHA-256: `087830ea3c61968c7e04722fc4ad3b92f5e826588f3b5bf2663ac5577d5460aa`  
{'PASS': 52, 'FAIL': 30, 'MISSING': 0, 'ERROR': 0}

**Tập: TRƯỢT** (chỉ luật CHẶN làm trượt tập; luật CHÍNH không đạt cần bên dựng giải thích; luật THAM KHẢO chỉ báo số đo)

| cấp | luật | đạt | không đạt |
|---|---|---|---|
| CHẶN | 29 | 27 | S07 FAIL, S10 FAIL |
| CHÍNH | 11 | 7 | V08 FAIL, V09 FAIL, V11 FAIL, C05 FAIL |
| THAM KHẢO | 42 | 18 | A03 FAIL, A10 FAIL, A11 FAIL, A15 FAIL, A16 FAIL, S11 FAIL, S12 FAIL, S13 FAIL, S15 FAIL, R03 FAIL, R04 FAIL, R05 FAIL, R06 FAIL, V02 FAIL, V04 FAIL, V05 FAIL, V10 FAIL, C04 FAIL, C06 FAIL, C10 FAIL, C12 FAIL, C13 FAIL, T2 FAIL, T3 FAIL |

CHÍNH không đạt, chưa có giải thích trong `out/explanations.json`: V08, V09, V11, C05

## Chỉ số trong ±5% quanh ngưỡng

- A12 (THAM KHẢO) · accents on a cut (%) = 100.0 (ngưỡng >= 100.0, đạt)
- A18 (CHÍNH) · distinct voices (provider, voiceId, model) = 1 (ngưỡng <= 1, đạt)
- S03 (CHẶN) · files = 2 (ngưỡng >= 2, đạt)
- S04 (CHẶN) · series pairs = 1 (ngưỡng >= 1, đạt)
- S04 (CHẶN) · mortgage30 tolerance = 0.5 (ngưỡng <= 0.5, đạt)
- S06 (CHẶN) · coverage statements = 1 (ngưỡng >= 1, đạt)
- S06 (CHẶN) · case values shown in act3 = 3 (ngưỡng >= 3, đạt)
- S11 (THAM KHẢO) · cut_today scenes = 3 (ngưỡng >= 3, đạt)
- S11 (THAM KHẢO) · cut_today acts = 2 (ngưỡng >= 2, đạt)
- S11 (THAM KHẢO) · cut_today callbacks w/ distinct meaning = 3 (ngưỡng >= 3, đạt)
- S11 (THAM KHẢO) · cut36_median acts = 2 (ngưỡng >= 2, đạt)
- S11 (THAM KHẢO) · cut36_median callbacks w/ distinct meaning = 3 (ngưỡng >= 3, đạt)
- S14 (THAM KHẢO) · ad breaks = 2 (ngưỡng in [2, 3], đạt)
- S15 (THAM KHẢO) · total s = 591.31 (ngưỡng >= 600.0, không đạt)
- R01 (THAM KHẢO) · acts with climax peak = 3 (ngưỡng >= 3, đạt)
- R02 (THAM KHẢO) · longest stretch without a break s = 57.45 (ngưỡng <= 60.0, đạt)
- V04 (THAM KHẢO) · median shape share = 0.913295 (ngưỡng >= 0.95, không đạt)
- V09 (CHÍNH) · declared characters seen on screen = 3 (ngưỡng >= 3, đạt)
- P01 (THAM KHẢO) · thumb 1 token share (%) = 100.0 (ngưỡng >= 97.0, đạt)
- P01 (THAM KHẢO) · thumb 2 token share (%) = 100.0 (ngưỡng >= 97.0, đạt)
- P01 (THAM KHẢO) · thumb 3 token share (%) = 100.0 (ngưỡng >= 97.0, đạt)

| rule | tier | § | status | failing metrics |
|---|---|---|---|---|
| F01 | CHẶN | DX-F1, DX-F2 | PASS |  |
| F02 | CHẶN | DX-F1 | PASS |  |
| F03 | CHẶN | DX-F3 | PASS |  |
| F04 | CHẶN | DX-F2 | PASS |  |
| F05 | CHẶN | DX-F2 | PASS |  |
| F06 | CHẶN | DX-F4 | PASS |  |
| F07 | CHÍNH | DX-S1 (CH §1 length) | PASS |  |
| F08 | CHẶN | DX-V5 | PASS |  |
| F09 | CHẶN | DX-F5 | PASS |  |
| F10 | CHẶN | DX-F6 | PASS |  |
| F11 | CHẶN | CH §4 khâu 3 (hợp đồng tập, K2) | PASS |  |
| F12 | CHẶN | DX-A3 (sổ giấy phép), CH §5 (K3: quyền tài sản; K3.1: tài sản hình) | PASS |  |
| A01 | CHẶN | DX-A10 | PASS |  |
| A02 | CHẶN | DX-A10 | PASS |  |
| A03 | THAM KHẢO | DX-A10 | FAIL | LRA LU = 3.7 (need in [6.0, 10.0]) |
| A04 | CHẶN | DX-A10 | PASS |  |
| A05 | CHẶN | DX-A10 | PASS |  |
| A06 | CHẶN | DX-A10, DX-X5 | PASS |  |
| A07 | THAM KHẢO | DX-A9 | PASS |  |
| A08 | THAM KHẢO | DX-A9 | PASS |  |
| A09 | THAM KHẢO | DX-R6 | PASS |  |
| A10 | THAM KHẢO | DX-A5 | FAIL | camera moves = 3 (need >= 5) |
| A11 | THAM KHẢO | DX-A5 | FAIL | events measured = 0 (need >= 8); Pearson pan~x = None (need >= 0.7) |
| A12 | THAM KHẢO | DX-A3 | PASS |  |
| A13 | THAM KHẢO | DX-A7 | PASS |  |
| A14 | CHẶN | DX-A7 | PASS |  |
| A15 | THAM KHẢO | DX-A7 | FAIL | wpm act cold-open = 184.514722 (need in [150.0, 160.0]); wpm act act1 = 175.488 (need in [150.0, 160.0]); wpm act act2 = 182.24809 (need in [150.0, 160.0]); wpm act act3 = 188.28999 (need in [150.0, 160.0]); wpm act method = 171.888988 (need in [150.0, 160.0]); wpm act outro = 187.660668 (need in [150.0, 160.0]); sentences > 175 wpm = 68 (need <= 0) |
| A16 | THAM KHẢO | DX-A7 (K3, cảnh báo) | FAIL | fake break marks = 14 (need <= 0); sentences with a fake break = 14 (need <= 0) |
| A17 | THAM KHẢO | DX-A7, DX-R6 (K3, cảnh báo) | PASS |  |
| A18 | CHÍNH | DX-A8 (K3, cảnh báo) | PASS |  |
| S01 | CHẶN | DX-H1 | PASS |  |
| S02 | CHẶN | DX-H1 | PASS |  |
| S03 | CHẶN | DX-H4 | PASS |  |
| S04 | CHẶN | DX-H5 | PASS |  |
| S05 | CHẶN | DX-H1, DX-H2 | PASS |  |
| S06 | CHẶN | DX-H6 | PASS |  |
| S07 | CHẶN | DX-H1, DX-H2 | FAIL | unsourced non-illustrative claims = 4 (need <= 0) |
| S08 | CHẶN | DX-H2 | PASS |  |
| S09 | CHẶN | DX-H3 | PASS |  |
| S10 | CHẶN | DX-I1, DX-I2 | FAIL | advice sentences = 1 (need <= 0) |
| S11 | THAM KHẢO | DX-S6 | FAIL | cut_today callbacks unverified = 1 (need <= 0); cost_median callbacks unverified = 1 (need <= 0) |
| S12 | THAM KHẢO | DX-S7 | FAIL | max new numbers in a scene = 22 (need <= 2) |
| S13 | THAM KHẢO | DX-S8 (sổ gu G-009) | FAIL | staccato passages = 1 (need <= 0) |
| S14 | THAM KHẢO | DX-S10 | PASS |  |
| S15 | THAM KHẢO | DX-S1 | FAIL | act order = ['cold-open', 'act1', 'act2', 'act3', 'method', 'outro'] (need == ['cold-open', 'ident', 'act1', 'act2', 'act3', 'method', 'outro']); cold open s = 55.67 (need <= 15.0); ident s = None (need <= 3.0); total s = 591.31 (need >= 600.0) |
| S16 | THAM KHẢO | DX-S3, RUBRIC H4 (sổ gu G-008) | PASS |  |
| R01 | THAM KHẢO | DX-R1 | PASS |  |
| R02 | THAM KHẢO | DX-R2 | PASS |  |
| R03 | THAM KHẢO | DX-R3 | FAIL | shortest pause s = 0.0 (need >= 1.0); pauses < 1.0 s = 4 (need <= 0) |
| R04 | THAM KHẢO | DX-R4 | FAIL | cuts on beat/action (%) = 63.333333 (need >= 70.0) |
| R05 | THAM KHẢO | DX-R5 | FAIL | shots > 12 s = 18 (need <= 0); shot length CV = 0.365716 (need >= 0.4); act-2 scenes before climax = 3 (need >= 6) |
| R06 | THAM KHẢO | DX-V10 (picture check of cuts) | FAIL | cuts visible in picture (%) = 73.333333 (need >= 90.0) |
| V01 | THAM KHẢO | DX-V12 | PASS |  |
| V02 | THAM KHẢO | DX-V1 | FAIL | level-1 placed (%) = 0.0 (need >= 90.0) |
| V03 | CHÍNH | DX-V3 | PASS |  |
| V04 | THAM KHẢO | DX-V4, DX-X3 | FAIL | median shape share = 0.913295 (need >= 0.95); small shape share = 0.599415 (need >= 0.95); large shape share = 0.747178 (need >= 0.95); character pairs on the wrong or on both sides = 3 (need <= 0) |
| V05 | THAM KHẢO | DX-V8 | FAIL | camera moves = 3 (need >= 5); anticipation in moves ≥1 s (%) = 0.0 (need >= 30.0); overshoot in moves ≥1 s (%) = 0.0 (need >= 30.0); camera~picture Spearman = 0.13265 (need >= 0.3) |
| V08 | CHÍNH | DX-V6 | FAIL | worst text contrast = 2.37 (need >= 4.5); samples below 4.5:1 = 349 (need <= 0) |
| V09 | CHÍNH | DX-V4, DX-X3 | FAIL | median/small ΔE2000 protanopia = 11.80888 (need >= 20.0); median/small ΔE2000 deuteranopia = 18.161131 (need >= 20.0); median/small grey contrast = 1.268686 (need >= 1.5); median/large ΔE2000 deuteranopia = 11.511445 (need >= 20.0); small/large ΔE2000 deuteranopia = 18.067456 (need >= 20.0) |
| V10 | THAM KHẢO | DX-V10 | FAIL | verified J/L cuts = 0 (need >= 4) |
| V11 | CHÍNH | DX-V11 (C rule text-line-collision, upgraded to pixels) | FAIL | text collisions = 715 (need <= 0) |
| V12 | CHÍNH | DX-V9 (replaces the camera-move exemption) | PASS |  |
| V13 | THAM KHẢO | DX-V9, DX-V8 (replaces the camera-move exemption) | PASS |  |
| C01 | THAM KHẢO | DX-V11 (C rule scene-leak) | PASS |  |
| C02 | CHÍNH | DX-V11 (C rule bg-over-data) | PASS |  |
| C03 | THAM KHẢO | DX-V11 (C rule unlabelled-curve) | PASS |  |
| C04 | THAM KHẢO | DX-V11 (C rule axis-anchors) | FAIL | frames flagged = 1091 (need <= 0) |
| C05 | CHÍNH | DX-V11, DX-X4 (C rule grey-emphasis) | FAIL | frames flagged = 1344 (need <= 0) |
| C06 | THAM KHẢO | DX-V11 (C rule number-colour) | FAIL | frames flagged = 449 (need <= 0) |
| C07 | CHẶN | DX-V11 (C rule bar-proportion) | PASS |  |
| C10 | THAM KHẢO | DX-V1 (C rule level1) | FAIL | scenes failing = 20 (need <= 0) |
| C11 | THAM KHẢO | DX-V11 (C rule layout-repeat) | PASS |  |
| C12 | THAM KHẢO | DX-V11 (C rule split-view) | FAIL | split-view runs = 2 (need <= 0) |
| C13 | THAM KHẢO | DX-V11 (number–voice sync ±250 ms) | FAIL | worst |offset| ms = 34625 (need <= 250.0); pairs > 250 ms = 56 (need <= 0) |
| C14 | CHÍNH | DX-V11, DX-X4 (legible at 25%) | PASS |  |
| C15 | THAM KHẢO | DX-V5 (C rule tokens only) | PASS |  |
| P01 | THAM KHẢO | DX-P2 | PASS |  |
| T1 | THAM KHẢO | DX-A1 (sổ gu G-001, G-006) | PASS |  |
| T2 | THAM KHẢO | DX-A2 (sổ gu G-002) | FAIL | repeated phrases (%) = 28.985507 (need <= 5.0); longest run of repeated phrases = 5 (need <= 1) |
| T3 | THAM KHẢO | DX-R6 (sổ gu G-003) | FAIL | entries outside 150–400 ms = 3 (need <= 0) |
| L1 | CHÍNH | DX-A1, DX-A9 (sổ gu G-006) | PASS |  |
| REG | CHẶN | CH §5, §4 khâu 3 (cổng hồi quy) | PASS | first version: nothing to compare |
