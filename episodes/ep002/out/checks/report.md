# checks/ report

root: `/home/user/crux-lab/episodes/ep002`  
lock: `2fcc9fcc9a94b73084c43ba59970d88f539cd29363334faf52b0640efc2cc801`  
master SHA-256: `fdfa3d47d6ee1069a23b30d52a4044fa2f9209e1b9a0c02852e059170e2480a4`  
{'PASS': 59, 'FAIL': 23, 'MISSING': 0, 'ERROR': 0}

**Tập: ĐẠT** (chỉ luật CHẶN làm trượt tập; luật CHÍNH không đạt cần bên dựng giải thích; luật THAM KHẢO chỉ báo số đo)

| cấp | luật | đạt | không đạt |
|---|---|---|---|
| CHẶN | 29 | 29 | — |
| CHÍNH | 11 | 11 | — |
| THAM KHẢO | 42 | 19 | A03 FAIL, A08 FAIL, A10 FAIL, A11 FAIL, A15 FAIL, A16 FAIL, A17 FAIL, S11 FAIL, S12 FAIL, S15 FAIL, R02 FAIL, R03 FAIL, R05 FAIL, R06 FAIL, V02 FAIL, V05 FAIL, V10 FAIL, C10 FAIL, C12 FAIL, C13 FAIL, P01 FAIL, T2 FAIL, T3 FAIL |

## Chỉ số trong ±5% quanh ngưỡng

- A12 (THAM KHẢO) · accents on a cut (%) = 100.0 (ngưỡng >= 100.0, đạt)
- A15 (THAM KHẢO) · wpm act cold-open = 158.878885 (ngưỡng in [150.0, 160.0], đạt)
- A15 (THAM KHẢO) · wpm act act1 = 163.16604 (ngưỡng in [150.0, 160.0], không đạt)
- A15 (THAM KHẢO) · wpm act act2 = 166.880616 (ngưỡng in [150.0, 160.0], không đạt)
- A15 (THAM KHẢO) · wpm act act3 = 161.534102 (ngưỡng in [150.0, 160.0], không đạt)
- A18 (CHÍNH) · distinct voices (provider, voiceId, model) = 1 (ngưỡng <= 1, đạt)
- S03 (CHẶN) · files = 2 (ngưỡng >= 2, đạt)
- S04 (CHẶN) · series pairs = 1 (ngưỡng >= 1, đạt)
- S06 (CHẶN) · coverage statements = 1 (ngưỡng >= 1, đạt)
- S06 (CHẶN) · case values shown in act3 = 3 (ngưỡng >= 3, đạt)
- S11 (THAM KHẢO) · share_early acts = 2 (ngưỡng >= 2, đạt)
- S14 (THAM KHẢO) · ad breaks = 2 (ngưỡng in [2, 3], đạt)
- S15 (THAM KHẢO) · total s = 585.6 (ngưỡng >= 600.0, không đạt)
- S16 (THAM KHẢO) · decisive sentences = 1 (ngưỡng >= 1, đạt)
- R01 (THAM KHẢO) · acts with climax peak = 3 (ngưỡng >= 3, đạt)
- V09 (CHÍNH) · declared characters seen on screen = 1 (ngưỡng >= 1, đạt)
- P01 (THAM KHẢO) · thumb 1 token share (%) = 99.99924 (ngưỡng >= 97.0, đạt)
- P01 (THAM KHẢO) · thumb 2 token share (%) = 99.99924 (ngưỡng >= 97.0, đạt)
- P01 (THAM KHẢO) · thumb 3 token share (%) = 99.99924 (ngưỡng >= 97.0, đạt)
- T1 (THAM KHẢO) · share of slots heard in a pause = 0.613924 (ngưỡng >= 0.6, đạt)

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
| A03 | THAM KHẢO | DX-A10 | FAIL | LRA LU = 3.1 (need in [6.0, 10.0]) |
| A04 | CHẶN | DX-A10 | PASS |  |
| A05 | CHẶN | DX-A10 | PASS |  |
| A06 | CHẶN | DX-A10, DX-X5 | PASS |  |
| A07 | THAM KHẢO | DX-A9 | PASS |  |
| A08 | THAM KHẢO | DX-A9 | FAIL | median 1-4 kHz drop dB = 4.366425 (need >= 6.0) |
| A09 | THAM KHẢO | DX-R6 | PASS |  |
| A10 | THAM KHẢO | DX-A5 | FAIL | camera moves = 0 (need >= 5) |
| A11 | THAM KHẢO | DX-A5 | FAIL | events measured = 0 (need >= 8); Pearson pan~x = None (need >= 0.7) |
| A12 | THAM KHẢO | DX-A3 | PASS |  |
| A13 | THAM KHẢO | DX-A7 | PASS |  |
| A14 | CHẶN | DX-A7 | PASS |  |
| A15 | THAM KHẢO | DX-A7 | FAIL | wpm act act1 = 163.16604 (need in [150.0, 160.0]); wpm act act2 = 166.880616 (need in [150.0, 160.0]); wpm act act3 = 161.534102 (need in [150.0, 160.0]); wpm act method = 190.709046 (need in [150.0, 160.0]); wpm act outro = 182.380216 (need in [150.0, 160.0]); sentences > 175 wpm = 27 (need <= 0) |
| A16 | THAM KHẢO | DX-A7 (K3, cảnh báo) | FAIL | fake break marks = 15 (need <= 0); sentences with a fake break = 15 (need <= 0) |
| A17 | THAM KHẢO | DX-A7, DX-R6 (K3, cảnh báo) | FAIL | abnormal gaps share = 0.111111 (need <= 0.1) |
| A18 | CHÍNH | DX-A8 (K3, cảnh báo) | PASS |  |
| S01 | CHẶN | DX-H1 | PASS |  |
| S02 | CHẶN | DX-H1 | PASS |  |
| S03 | CHẶN | DX-H4 | PASS |  |
| S04 | CHẶN | DX-H5 | PASS |  |
| S05 | CHẶN | DX-H1, DX-H2 | PASS |  |
| S06 | CHẶN | DX-H6 | PASS |  |
| S07 | CHẶN | DX-H1, DX-H2 | PASS |  |
| S08 | CHẶN | DX-H2 | PASS |  |
| S09 | CHẶN | DX-H3 | PASS |  |
| S10 | CHẶN | DX-I1, DX-I2 | PASS |  |
| S11 | THAM KHẢO | DX-S6 | FAIL | share_all scenes = 1 (need >= 3); share_all acts = 1 (need >= 2); share_all callbacks w/ distinct meaning = 0 (need >= 3); share_early scenes = 2 (need >= 3); share_early callbacks w/ distinct meaning = 2 (need >= 3); share_late scenes = 1 (need >= 3); share_late acts = 1 (need >= 2); share_late callbacks w/ distinct meaning = 1 (need >= 3); worst_diff scenes = 1 (need >= 3); worst_diff acts = 1 (need >= 2); worst_diff callbacks w/ distinct meaning = 1 (need >= 3) |
| S12 | THAM KHẢO | DX-S7 | FAIL | max new numbers in a scene = 20 (need <= 2) |
| S13 | THAM KHẢO | DX-S8 (sổ gu G-009) | PASS |  |
| S14 | THAM KHẢO | DX-S10 | PASS |  |
| S15 | THAM KHẢO | DX-S1 | FAIL | act order = ['cold-open', 'act1', 'act2', 'act3', 'method', 'outro'] (need == ['cold-open', 'ident', 'act1', 'act2', 'act3', 'method', 'outro']); cold open s = 26.967 (need <= 15.0); ident s = None (need <= 3.0); total s = 585.6 (need >= 600.0) |
| S16 | THAM KHẢO | DX-S3, RUBRIC H4 (sổ gu G-008) | PASS |  |
| R01 | THAM KHẢO | DX-R1 | PASS |  |
| R02 | THAM KHẢO | DX-R2 | FAIL | longest stretch without a break s = 67.333 (need <= 60.0) |
| R03 | THAM KHẢO | DX-R3 | FAIL | shortest pause s = 0.0 (need >= 1.0); pauses < 1.0 s = 3 (need <= 0) |
| R04 | THAM KHẢO | DX-R4 | PASS |  |
| R05 | THAM KHẢO | DX-R5 | FAIL | shots > 12 s = 11 (need <= 0); shot length CV = 0.336149 (need >= 0.4); act-2 scenes before climax = 3 (need >= 6) |
| R06 | THAM KHẢO | DX-V10 (picture check of cuts) | FAIL | cuts visible in picture (%) = 25.806452 (need >= 90.0) |
| V01 | THAM KHẢO | DX-V12 | PASS |  |
| V02 | THAM KHẢO | DX-V1 | FAIL | level-1 samples = 0 (need >= 1); level-1 placed (%) = None (need >= 90.0) |
| V03 | CHÍNH | DX-V3 | PASS |  |
| V04 | THAM KHẢO | DX-V4, DX-X3 | PASS |  |
| V05 | THAM KHẢO | DX-V8 | FAIL | camera moves = 0 (need >= 5); worst ease ratio = None (need <= 0.4); anticipation in moves ≥1 s (%) = None (need >= 30.0); overshoot in moves ≥1 s (%) = None (need >= 30.0); peak |a| fw/s² = None (need <= 8.0); camera~picture Spearman = nan (need >= 0.3) |
| V08 | CHÍNH | DX-V6 | PASS |  |
| V09 | CHÍNH | DX-V4, DX-X3 | PASS |  |
| V10 | THAM KHẢO | DX-V10 | FAIL | verified J/L cuts = 0 (need >= 4) |
| V11 | CHÍNH | DX-V11 (C rule text-line-collision, upgraded to pixels) | PASS |  |
| V12 | CHÍNH | DX-V9 (replaces the camera-move exemption) | PASS |  |
| V13 | THAM KHẢO | DX-V9, DX-V8 (replaces the camera-move exemption) | PASS |  |
| C01 | THAM KHẢO | DX-V11 (C rule scene-leak) | PASS |  |
| C02 | CHÍNH | DX-V11 (C rule bg-over-data) | PASS |  |
| C03 | THAM KHẢO | DX-V11 (C rule unlabelled-curve) | PASS |  |
| C04 | THAM KHẢO | DX-V11 (C rule axis-anchors) | PASS |  |
| C05 | CHÍNH | DX-V11, DX-X4 (C rule grey-emphasis) | PASS |  |
| C06 | THAM KHẢO | DX-V11 (C rule number-colour) | PASS |  |
| C07 | CHẶN | DX-V11 (C rule bar-proportion) | PASS |  |
| C10 | THAM KHẢO | DX-V1 (C rule level1) | FAIL | scenes failing = 13 (need <= 0) |
| C11 | THAM KHẢO | DX-V11 (C rule layout-repeat) | PASS |  |
| C12 | THAM KHẢO | DX-V11 (C rule split-view) | FAIL | split-view runs = 18 (need <= 0) |
| C13 | THAM KHẢO | DX-V11 (number–voice sync ±250 ms) | FAIL | worst |offset| ms = 52860 (need <= 250.0); pairs > 250 ms = 37 (need <= 0) |
| C14 | CHÍNH | DX-V11, DX-X4 (legible at 25%) | PASS |  |
| C15 | THAM KHẢO | DX-V5 (C rule tokens only) | PASS |  |
| P01 | THAM KHẢO | DX-P2 | FAIL | thumb texts below 90 px = 3 (need <= 0) |
| T1 | THAM KHẢO | DX-A1 (sổ gu G-001, G-006) | PASS |  |
| T2 | THAM KHẢO | DX-A2 (sổ gu G-002) | FAIL | repeated phrases (%) = 19.71831 (need <= 5.0); longest run of repeated phrases = 3 (need <= 1) |
| T3 | THAM KHẢO | DX-R6 (sổ gu G-003) | FAIL | entries outside 150–400 ms = 2 (need <= 0) |
| L1 | CHÍNH | DX-A1, DX-A9 (sổ gu G-006) | PASS |  |
| REG | CHẶN | CH §5, §4 khâu 3 (cổng hồi quy) | PASS | first version: nothing to compare |
