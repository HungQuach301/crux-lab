# checks/ report

root: `/tmp/claude-0/-home-user-crux-lab/df7acaf1-1be7-5520-a20c-d80d630f692a/scratchpad/c5c_run/episodes/ep005`  
lock: `d93276a491dd366c08ea0464d8de23bca80d82082a0c7be66ea2d555fd366b4a`  
master SHA-256: `d2a04ca70015ec4d211f28495c0bd3d34bc979cb7ca7a8279cbc47cea0dc653a`  
{'PASS': 56, 'FAIL': 33, 'MISSING': 0, 'ERROR': 0}

**Tập: ĐẠT** (chỉ luật CHẶN làm trượt tập; luật CHÍNH không đạt cần bên dựng giải thích; luật THAM KHẢO chỉ báo số đo)

| cấp | luật | đạt | không đạt |
|---|---|---|---|
| CHẶN | 35 | 35 | — |
| CHÍNH | 11 | 9 | F07 FAIL, V11 FAIL |
| THAM KHẢO | 43 | 12 | A03 FAIL, A09 FAIL, A10 FAIL, A11 FAIL, A12 FAIL, A13 FAIL, A15 FAIL, A16 FAIL, A17 FAIL, S11 FAIL, S12 FAIL, S14 FAIL, S15 FAIL, S16 FAIL, R01 FAIL, R03 FAIL, R04 FAIL, R05 FAIL, R06 FAIL, V01 FAIL, V02 FAIL, V05 FAIL, V10 FAIL, C06 FAIL, C11 FAIL, C12 FAIL, C13 FAIL, C15 FAIL, P01 FAIL, T2 FAIL, T3 FAIL |

## Chỉ số trong ±5% quanh ngưỡng

- F07 (CHÍNH) · duration s = 465.666667 (ngưỡng in [480.0, 900.0], không đạt)
- A15 (THAM KHẢO) · wpm act cold-open = 167.782592 (ngưỡng in [150.0, 160.0], không đạt)
- A15 (THAM KHẢO) · wpm act act2 = 166.731818 (ngưỡng in [150.0, 160.0], không đạt)
- A18 (CHÍNH) · distinct voices (provider, voiceId, model) = 1 (ngưỡng <= 1, đạt)
- S04 (CHẶN) · mortgage30 tolerance = 0.5 (ngưỡng <= 0.5, đạt)
- S04 (CHẶN) · hpi_mom tolerance = 0.5 (ngưỡng <= 0.5, đạt)
- S06 (CHẶN) · case values shown in act2 = 307 (ngưỡng >= 307, đạt)
- S06 (CHẶN) · case values shown in act3 = 3 (ngưỡng >= 3, đạt)
- S11 (THAM KHẢO) · medianB_months_to80 acts = 2 (ngưỡng >= 2, đạt)
- S15 (THAM KHẢO) · ident s = 3.0 (ngưỡng <= 3.0, đạt)
- S15 (THAM KHẢO) · outro s = 19.9333 (ngưỡng >= 20.0, không đạt)
- V05 (THAM KHẢO) · overshoot in moves ≥1 s (%) = 28.571429 (ngưỡng >= 30.0, không đạt)
- V09 (CHÍNH) · declared characters seen on screen = 3 (ngưỡng >= 3, đạt)
- P01 (THAM KHẢO) · thumb 1 token share (%) = 100.0 (ngưỡng >= 97.0, đạt)
- P01 (THAM KHẢO) · thumb 2 token share (%) = 100.0 (ngưỡng >= 97.0, đạt)
- P01 (THAM KHẢO) · thumb 3 token share (%) = 100.0 (ngưỡng >= 97.0, đạt)
- L1 (CHÍNH) · voice/data 1–4 kHz ratio, 10th percentile (dB) = 20.348241 (ngưỡng >= 20.0, đạt)

| rule | tier | § | status | failing metrics |
|---|---|---|---|---|
| F01 | CHẶN | DX-F1, DX-F2 | PASS |  |
| F02 | CHẶN | DX-F1 | PASS |  |
| F03 | CHẶN | DX-F3 | PASS |  |
| F04 | CHẶN | DX-F2 | PASS |  |
| F05 | CHẶN | DX-F2 | PASS |  |
| F06 | CHẶN | DX-F4 | PASS |  |
| F07 | CHÍNH | DX-S1 (CH §1 length) | FAIL | duration s = 465.666667 (need in [480.0, 900.0]) |
| F08 | CHẶN | DX-V5 | PASS |  |
| F09 | CHẶN | DX-F5 | PASS |  |
| F10 | CHẶN | DX-F6 | PASS |  |
| F11 | CHẶN | CH §4 khâu 3 (hợp đồng tập, K2) | PASS |  |
| F12 | CHẶN | DX-A3 (sổ giấy phép), CH §5 (K3: quyền tài sản; K3.1: tài sản hình) | PASS |  |
| A01 | CHẶN | DX-A10 | PASS |  |
| A02 | CHẶN | DX-A10 | PASS |  |
| A03 | THAM KHẢO | DX-A10 | FAIL | LRA LU = 3.6 (need in [6.0, 10.0]) |
| A04 | CHẶN | DX-A10 | PASS |  |
| A05 | CHẶN | DX-A10 | PASS |  |
| A06 | CHẶN | DX-A10, DX-X5 | PASS |  |
| A07 | THAM KHẢO | DX-A9 | PASS |  |
| A08 | THAM KHẢO | DX-A9 | PASS |  |
| A09 | THAM KHẢO | DX-R6 | FAIL | silences 0.8-1.5 s = 0 (need >= 3) |
| A10 | THAM KHẢO | DX-A5 | FAIL | Spearman speed~whoosh = 0.021107 (need >= 0.6); fast moves without whoosh = 26 (need <= 0) |
| A11 | THAM KHẢO | DX-A5 | FAIL | Pearson pan~x = None (need >= 0.7) |
| A12 | THAM KHẢO | DX-A3 | FAIL | accents = 0 (need >= 5); accents on a cut (%) = None (need >= 100.0); accents confirmed by onset (%) = None (need >= 90.0) |
| A13 | THAM KHẢO | DX-A7 | FAIL | max |stretch-1| = 80.485062 (need <= 0.1) |
| A14 | CHẶN | DX-A7 | PASS |  |
| A15 | THAM KHẢO | DX-A7 | FAIL | wpm act cold-open = 167.782592 (need in [150.0, 160.0]); wpm act act1 = 179.758201 (need in [150.0, 160.0]); wpm act act2 = 166.731818 (need in [150.0, 160.0]); wpm act act3 = 176.162562 (need in [150.0, 160.0]); wpm act method = 203.007519 (need in [150.0, 160.0]); wpm act outro = 201.77665 (need in [150.0, 160.0]); sentences > 175 wpm = 42 (need <= 0) |
| A16 | THAM KHẢO | DX-A7 (K3, cảnh báo) | FAIL | fake break marks = 8 (need <= 0); sentences with a fake break = 8 (need <= 0) |
| A17 | THAM KHẢO | DX-A7, DX-R6 (K3, cảnh báo) | FAIL | abnormal sentences share = 0.228571 (need <= 0.1); abnormal gaps share = 0.34 (need <= 0.1) |
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
| S11 | THAM KHẢO | DX-S6 | FAIL | sched80_months_latest scenes = 2 (need >= 3); sched80_months_latest acts = 1 (need >= 2); sched80_months_latest callbacks w/ distinct meaning = 0 (need >= 3); shareA_ltv24_le75 scenes = 1 (need >= 3); shareA_ltv24_le75 acts = 1 (need >= 2); shareA_ltv24_le75 callbacks w/ distinct meaning = 0 (need >= 3); medianB_months_to80 scenes = 2 (need >= 3); medianB_months_to80 callbacks w/ distinct meaning = 0 (need >= 3); shareB_over60 scenes = 1 (need >= 3); shareB_over60 acts = 1 (need >= 2); shareB_over60 callbacks w/ distinct meaning = 0 (need >= 3); maxB_months_to80 scenes = 1 (need >= 3); maxB_months_to80 acts = 1 (need >= 2); maxB_months_to80 callbacks w/ distinct meaning = 0 (need >= 3); shareB_le_sched80 scenes = 1 (need >= 3); shareB_le_sched80 acts = 1 (need >= 2); shareB_le_sched80 callbacks w/ distinct meaning = 0 (need >= 3); ex_extra_down_for_20 scenes = 1 (need >= 3); ex_extra_down_for_20 acts = 1 (need >= 2); ex_extra_down_for_20 callbacks w/ distinct meaning = 0 (need >= 3) |
| S12 | THAM KHẢO | DX-S7 | FAIL | new numbers = 75 (need <= 58.2083625); max new numbers in a scene = 12 (need <= 2) |
| S13 | THAM KHẢO | DX-S8 (sổ gu G-009) | PASS |  |
| S14 | THAM KHẢO | DX-S10 | FAIL | ad breaks = 0 (need == 1) |
| S15 | THAM KHẢO | DX-S1 | FAIL | outro s = 19.9333 (need >= 20.0) |
| S16 | THAM KHẢO | DX-S3, RUBRIC H4 (sổ gu G-008) | FAIL | share tied to a character or scenario = 0.0 (need >= 0.75) |
| S17 | CHẶN | DX-H2 (claim), checks-appeal A1 | PASS |  |
| S18 | THAM KHẢO | DX-S3, DX-S4 (story.md §1), checks-appeal A2 | PASS |  |
| SH01 | CHẶN | D-006 Q3, checks-appeal A5 | PASS |  |
| SH02 | CHẶN | D-006 Q3, checks-appeal A5 | PASS |  |
| SH03 | CHẶN | DX-A10, checks-appeal A5 | PASS |  |
| SH04 | CHẶN | DX-A10, checks-appeal A5 | PASS |  |
| SH05 | CHẶN | DX-I1, DX-I2 (CHARTER §4 protected genes), checks-appeal A5 | PASS |  |
| R01 | THAM KHẢO | DX-R1 | FAIL | r cut rate = 0.01133 (need >= 0.8); r audio density = 0.224327 (need >= 0.6); acts with climax peak = 0 (need >= 3); peaks without valley = 2 (need <= 0) |
| R02 | THAM KHẢO | DX-R2 | PASS |  |
| R03 | THAM KHẢO | DX-R3 | FAIL | shortest pause s = 0.0 (need >= 1.0); pauses < 1.0 s = 2 (need <= 0) |
| R04 | THAM KHẢO | DX-R4 | FAIL | cuts on beat/action (%) = 0.0 (need >= 70.0) |
| R05 | THAM KHẢO | DX-R5 | FAIL | shots > 12 s = 17 (need <= 0); act-2 scenes before climax = 0 (need >= 6) |
| R06 | THAM KHẢO | DX-V10 (picture check of cuts) | FAIL | cuts visible in picture (%) = 0.0 (need >= 90.0) |
| V01 | THAM KHẢO | DX-V12 | FAIL | scenes without a shot = 1 (need <= 0); storyboard present = False (need == True); colour script present = False (need == True) |
| V02 | THAM KHẢO | DX-V1 | FAIL | level-1 samples = 0 (need >= 1); level-1 placed (%) = None (need >= 90.0) |
| V03 | CHÍNH | DX-V3 | PASS |  |
| V04 | THAM KHẢO | DX-V4, DX-X3 | PASS |  |
| V05 | THAM KHẢO | DX-V8 | FAIL | worst ease ratio = 0.46 (need <= 0.4); anticipation in moves ≥1 s (%) = 7.142857 (need >= 30.0); overshoot in moves ≥1 s (%) = 28.571429 (need >= 30.0); overshoot > 8% = 2 (need <= 0); peak |a| fw/s² = 59.65 (need <= 8.0) |
| V08 | CHÍNH | DX-V6 | PASS |  |
| V09 | CHÍNH | DX-V4, DX-X3 | PASS |  |
| V10 | THAM KHẢO | DX-V10 | FAIL | verified match cuts = 2 (need >= 5); verified J/L cuts = 0 (need >= 4) |
| V11 | CHÍNH | DX-V11 (C rule text-line-collision, upgraded to pixels) | FAIL | text collisions = 2612 (need <= 0) |
| V12 | CHÍNH | DX-V9 (replaces the camera-move exemption) | PASS |  |
| V13 | THAM KHẢO | DX-V9, DX-V8 (replaces the camera-move exemption) | PASS |  |
| C01 | THAM KHẢO | DX-V11 (C rule scene-leak) | PASS |  |
| C02 | CHÍNH | DX-V11 (C rule bg-over-data) | PASS |  |
| C03 | THAM KHẢO | DX-V11 (C rule unlabelled-curve) | PASS |  |
| C04 | THAM KHẢO | DX-V11 (C rule axis-anchors) | PASS |  |
| C05 | CHÍNH | DX-V11, DX-X4 (C rule grey-emphasis) | PASS |  |
| C06 | THAM KHẢO | DX-V11 (C rule number-colour) | FAIL | frames flagged = 1157 (need <= 0) |
| C07 | CHẶN | DX-V11 (C rule bar-proportion) | PASS |  |
| C10 | THAM KHẢO | DX-V1 (C rule level1) | PASS |  |
| C11 | THAM KHẢO | DX-V11 (C rule layout-repeat) | FAIL | layout repeats >2 in 90 s = 19 (need <= 0) |
| C12 | THAM KHẢO | DX-V11 (C rule split-view) | FAIL | split-view runs = 1 (need <= 0) |
| C13 | THAM KHẢO | DX-V11 (number–voice sync ±250 ms) | FAIL | worst |offset| ms = 27913 (need <= 250.0); pairs > 250 ms = 29 (need <= 0) |
| C14 | CHÍNH | DX-V11, DX-X4 (legible at 25%) | PASS |  |
| C15 | THAM KHẢO | DX-V5 (C rule tokens only) | FAIL | frames flagged = 25028 (need <= 0) |
| P01 | THAM KHẢO | DX-P2 | FAIL | thumb texts below 90 px = 4 (need <= 0) |
| T1 | THAM KHẢO | DX-A1 (sổ gu G-001, G-006) | PASS |  |
| T2 | THAM KHẢO | DX-A2 (sổ gu G-002) | FAIL | repeated phrases (%) = 9.259259 (need <= 5.0); longest run of repeated phrases = 2 (need <= 1) |
| T3 | THAM KHẢO | DX-R6 (sổ gu G-003) | FAIL | silences measured = 0 (need >= 1) |
| L1 | CHÍNH | DX-A1, DX-A9 (sổ gu G-006) | PASS |  |
| REG | CHẶN | CH §5, §4 khâu 3 (cổng hồi quy) | PASS |  |
