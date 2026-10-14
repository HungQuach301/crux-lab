# checks/ report

root: `/var/tmp/f15/chk1080/episodes/ep007`  
lock: `dc4981b3f63e1f86872706fc73102794822ff75dbc65196dd3c0d87cebcab3d0`  
master SHA-256: `ed09a1cc514035cc314c3b7966ca2008c63cff624bee25b0baa639ab25011c2f`  
{'PASS': 55, 'FAIL': 43, 'MISSING': 1, 'ERROR': 1}

**Tập: TRƯỢT** (chỉ luật CHẶN làm trượt tập; luật CHÍNH không đạt cần bên dựng giải thích; luật THAM KHẢO chỉ báo số đo)

| cấp | luật | đạt | không đạt |
|---|---|---|---|
| CHẶN | 36 | 31 | A14 FAIL, S02 FAIL, S07 FAIL, S09 FAIL, C07 FAIL |
| CHÍNH | 14 | 9 | V08 FAIL, V09 FAIL, V11 FAIL, V12 FAIL, L1 FAIL |
| THAM KHẢO | 50 | 15 | A03 FAIL, A10 FAIL, A11 FAIL, A12 ERROR, A13 FAIL, A15 FAIL, A16 FAIL, A17 FAIL, S11 FAIL, S12 FAIL, S15 FAIL, S16 FAIL, R01 FAIL, R02 FAIL, R03 FAIL, R04 FAIL, R05 FAIL, R07 FAIL, R08 FAIL, V01 FAIL, V02 FAIL, V04 FAIL, V05 FAIL, V10 FAIL, V14 FAIL, V17 FAIL, C04 FAIL, C06 FAIL, C11 FAIL, C12 FAIL, C13 FAIL, C15 FAIL, P01 MISSING, T1 FAIL, T3 FAIL |

CHÍNH không đạt, chưa có giải thích trong `out/explanations.json`: V08, V09, V11, V12, L1

## Chỉ số trong ±5% quanh ngưỡng

- A09 (THAM KHẢO) · silences 0.8-1.5 s = 3 (ngưỡng >= 3, đạt)
- A15 (THAM KHẢO) · wpm act cold-open = 167.900582 (ngưỡng in [150.0, 160.0], không đạt)
- A15 (THAM KHẢO) · wpm act act1 = 152.987806 (ngưỡng in [150.0, 160.0], đạt)
- A15 (THAM KHẢO) · wpm act act3 = 167.767741 (ngưỡng in [150.0, 160.0], không đạt)
- A15 (THAM KHẢO) · wpm act limits = 163.834951 (ngưỡng in [150.0, 160.0], không đạt)
- A18 (CHÍNH) · distinct voices (provider, voiceId, model) = 1 (ngưỡng <= 1, đạt)
- S04 (CHẶN) · mortgage30 tolerance = 0.5 (ngưỡng <= 0.5, đạt)
- S04 (CHẶN) · mortgage15 tolerance = 0.5 (ngưỡng <= 0.5, đạt)
- S06 (CHẶN) · coverage statements = 1 (ngưỡng >= 1, đạt)
- S06 (CHẶN) · case values shown in act2 = 1833 (ngưỡng >= 1833, đạt)
- S11 (THAM KHẢO) · pay15_now acts = 2 (ngưỡng >= 2, đạt)
- S11 (THAM KHẢO) · extra_vs15_month_now scenes = 3 (ngưỡng >= 3, đạt)
- S11 (THAM KHẢO) · extra_vs15_total_now scenes = 3 (ngưỡng >= 3, đạt)
- S11 (THAM KHẢO) · extra_vs15_total_now acts = 2 (ngưỡng >= 2, đạt)
- S11 (THAM KHẢO) · share_extra_ge_now scenes = 3 (ngưỡng >= 3, đạt)
- S11 (THAM KHẢO) · share_extra_ge_now acts = 2 (ngưỡng >= 2, đạt)
- S11 (THAM KHẢO) · bar_now scenes = 3 (ngưỡng >= 3, đạt)
- S15 (THAM KHẢO) · ident s = 3.0 (ngưỡng <= 3.0, đạt)
- S18 (THAM KHẢO) · promise ends s = 28.693 (ngưỡng <= 30.0, đạt)
- T2 (THAM KHẢO) · longest run of repeated phrases = 1 (ngưỡng <= 1, đạt)
- T4 (THAM KHẢO) · most events in 10 s = 6 (ngưỡng <= 6, đạt)

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
| F11 | CHẶN | CH §4 khâu 3 (hợp đồng tập, K2; K4.1: danh sách của nhà máy, checks-appeal A10, A16) | PASS |  |
| F12 | CHẶN | DX-A3 (sổ giấy phép), CH §5 (K3: quyền tài sản; K3.1: tài sản hình) | PASS |  |
| A01 | CHẶN | DX-A10 | PASS |  |
| A02 | CHẶN | DX-A10 | PASS |  |
| A03 | THAM KHẢO | DX-A10 | FAIL | LRA LU = 3.6 (need in [6.0, 10.0]) |
| A04 | CHẶN | DX-A10 | PASS |  |
| A05 | CHẶN | DX-A10 | PASS |  |
| A06 | CHẶN | DX-A10, DX-X5 | PASS |  |
| A07 | THAM KHẢO | DX-A9 | PASS |  |
| A08 | THAM KHẢO | DX-A9 | PASS |  |
| A09 | THAM KHẢO | DX-R6 | PASS |  |
| A10 | THAM KHẢO | DX-A5 | FAIL | Spearman speed~whoosh = 0.075535 (need >= 0.6); fast moves without whoosh = 25 (need <= 0) |
| A11 | THAM KHẢO | DX-A5 | FAIL | Pearson pan~x = None (need >= 0.7) |
| A12 | THAM KHẢO | DX-A3 | ERROR | TypeError: unsupported operand type(s) for -: 'float' and 'dict' |
| A13 | THAM KHẢO | DX-A7 | FAIL | max |stretch-1| = 223.504638 (need <= 0.1) |
| A14 | CHẶN | DX-A7 | FAIL | key words missing = 2 (need <= 0) |
| A15 | THAM KHẢO | DX-A7 | FAIL | wpm act cold-open = 167.900582 (need in [150.0, 160.0]); wpm act act2 = 169.887019 (need in [150.0, 160.0]); wpm act act3 = 167.767741 (need in [150.0, 160.0]); wpm act limits = 163.834951 (need in [150.0, 160.0]); sentences > 175 wpm = 30 (need <= 0) |
| A16 | THAM KHẢO | DX-A7 (K3, cảnh báo) | FAIL | fake break marks = 15 (need <= 0); sentences with a fake break = 15 (need <= 0) |
| A17 | THAM KHẢO | DX-A7, DX-R6 (K3, cảnh báo) | FAIL | abnormal sentences share = 0.148148 (need <= 0.1); abnormal gaps share = 0.1875 (need <= 0.1) |
| A18 | CHÍNH | DX-A8 (K3, cảnh báo) | PASS |  |
| S01 | CHẶN | DX-H1 | PASS |  |
| S02 | CHẶN | DX-H1 | FAIL | us-only in method card = False (need == True); history-not-forecast in method card = False (need == True) |
| S03 | CHẶN | DX-H4 | PASS |  |
| S04 | CHẶN | DX-H5 | PASS |  |
| S05 | CHẶN | DX-H1, DX-H2 | PASS |  |
| S06 | CHẶN | DX-H6 | PASS |  |
| S07 | CHẶN | DX-H1, DX-H2 | FAIL | unregistered numbers in narration = 52 (need <= 0) |
| S08 | CHẶN | DX-H2 | PASS |  |
| S09 | CHẶN | DX-H3 | FAIL | money claims without basis = 29 (need <= 0); frames missing basis on screen = 2384 (need <= 0) |
| S10 | CHẶN | DX-I1, DX-I2 | PASS |  |
| S11 | THAM KHẢO | DX-S6 | FAIL | pay15_now scenes = 2 (need >= 3); pay15_now callbacks w/ distinct meaning = 0 (need >= 3); pay30on15_now scenes = 1 (need >= 3); pay30on15_now acts = 1 (need >= 2); pay30on15_now callbacks w/ distinct meaning = 0 (need >= 3); extra_vs15_month_now callbacks w/ distinct meaning = 0 (need >= 3); extra_vs15_total_now callbacks w/ distinct meaning = 0 (need >= 3); extra_total_median scenes = 1 (need >= 3); extra_total_median acts = 1 (need >= 2); extra_total_median callbacks w/ distinct meaning = 0 (need >= 3); share_extra_ge_now callbacks w/ distinct meaning = 0 (need >= 3); bar_now callbacks w/ distinct meaning = 0 (need >= 3) |
| S12 | THAM KHẢO | DX-S7 | FAIL | max new numbers in a scene = 6 (need <= 2) |
| S13 | THAM KHẢO | DX-S8 (sổ gu G-009) | PASS |  |
| S14 | THAM KHẢO | DX-S10 | PASS |  |
| S15 | THAM KHẢO | DX-S1 | FAIL | act order = ['cold-open', 'ident', 'act1', 'act2', 'act3', 'limits'] (need == ['cold-open', 'ident', 'act1', 'act2', 'act3', 'method', 'outro']); outro s = None (need >= 20.0) |
| S16 | THAM KHẢO | DX-S3, RUBRIC H4 (sổ gu G-008) | FAIL | share tied to a character or scenario = 0.428571 (need >= 0.75) |
| S17 | CHẶN | DX-H2 (claim), checks-appeal A1 | PASS |  |
| S18 | THAM KHẢO | DX-S3, DX-S4 (story.md §1), checks-appeal A2 | PASS |  |
| S19 | CHẶN | DX-H1, DX-H4 (claim-risk), checks-appeal A20 | PASS | contract.json declares no claims.forbiddenAmounts: nothing to check |
| S20 | CHÍNH | DX-S7 (lời mang số), checks-appeal A17 | PASS |  |
| S21 | CHÍNH | DX-H1 (lỗi số = 0 cả ngoài video), cine-lab BAI-HOC-LL #53, checks-appeal A25 | PASS |  |
| S22 | THAM KHẢO | DX-H2 (claim-risk), cine-lab BAI-HOC-LL #62, checks-appeal A26 | PASS |  |
| SH01 | CHẶN | D-006 Q3, checks-appeal A5 | PASS |  |
| SH02 | CHẶN | D-006 Q3, checks-appeal A5 | PASS |  |
| SH03 | CHẶN | DX-A10, checks-appeal A5 | PASS |  |
| SH04 | CHẶN | DX-A10, checks-appeal A5 | PASS |  |
| SH05 | CHẶN | DX-I1, DX-I2 (CHARTER §4 protected genes), checks-appeal A5 | PASS |  |
| SH06 | CHÍNH | D-006 Q3, lessons T6-10, checks-appeal A30 | PASS |  |
| R01 | THAM KHẢO | DX-R1 | FAIL | r cut rate = -0.040936 (need >= 0.8); r audio density = 0.095885 (need >= 0.6); acts with climax peak = 0 (need >= 3) |
| R02 | THAM KHẢO | DX-R2 | FAIL | longest stretch without a break s = 252.14 (need <= 60.0) |
| R03 | THAM KHẢO | DX-R3 | FAIL | shortest pause s = 0.0 (need >= 1.0); pauses < 1.0 s = 6 (need <= 0) |
| R04 | THAM KHẢO | DX-R4 | FAIL | cuts on beat/action (%) = 0.0 (need >= 70.0) |
| R05 | THAM KHẢO | DX-R5 | FAIL | shots > 12 s = 23 (need <= 0); act-2 scenes before climax = 0 (need >= 6) |
| R06 | THAM KHẢO | DX-V10 (picture check of cuts) | PASS |  |
| R07 | THAM KHẢO | DX-R (đồng bộ hình–lời), D-010 §6, checks-appeal A14 | FAIL | visual cues within ±0.2 s (%) = 71.698113 (need >= 92.0) |
| R08 | THAM KHẢO | tổng kết Tập 5 §3.2 (nhịp, đo trước render), checks-appeal A23 | FAIL | still stretches > 8 s = 1 (need <= 0); longest still stretch s = 9.19 (need <= 8.0) |
| V01 | THAM KHẢO | DX-V12 | FAIL | scenes without a shot = 12 (need <= 0); storyboard present = False (need == True); colour script present = False (need == True) |
| V02 | THAM KHẢO | DX-V1 | FAIL | level-1 samples = 0 (need >= 1); level-1 placed (%) = None (need >= 90.0) |
| V03 | CHÍNH | DX-V3 | PASS |  |
| V04 | THAM KHẢO | DX-V4, DX-X3 | FAIL | tessa seen = False (need == True); leo seen = False (need == True) |
| V05 | THAM KHẢO | DX-V8 | FAIL | worst ease ratio = 0.78 (need <= 0.4); anticipation in moves ≥1 s (%) = 0.0 (need >= 30.0); overshoot in moves ≥1 s (%) = 0.0 (need >= 30.0); peak |a| fw/s² = 8.97 (need <= 8.0) |
| V08 | CHÍNH | DX-V6 | FAIL | worst text contrast = 1.01 (need >= 4.5); samples below 4.5:1 = 1 (need <= 0) |
| V09 | CHÍNH | DX-V4, DX-X3 | FAIL | declared characters seen on screen = 0 (need >= 2) |
| V10 | THAM KHẢO | DX-V10 | FAIL | verified match cuts = 0 (need >= 5); verified J/L cuts = 0 (need >= 4) |
| V11 | CHÍNH | DX-V11 (C rule text-line-collision, upgraded to pixels) | FAIL | text collisions = 285 (need <= 0) |
| V12 | CHÍNH | DX-V9 (replaces the camera-move exemption) | FAIL | text samples below NCC 0.97 = 17 (need <= 0) |
| V13 | THAM KHẢO | DX-V9, DX-V8 (replaces the camera-move exemption) | PASS |  |
| V14 | THAM KHẢO | D-010 quy tắc 1/2/3/7 (đoạn thế giới), checks-appeal A18 | FAIL | first-5 s beats not in the world = 2 (need <= 0) |
| V15 | THAM KHẢO | D-010 quy tắc 5 (không quay lại thẻ chữ), checks-appeal A13 | PASS |  |
| V17 | THAM KHẢO | DX-V (đọc kịp), lessons T5-2, checks-appeal A24 | FAIL | labels on screen too short to read = 3 (need <= 0) |
| C01 | THAM KHẢO | DX-V11 (C rule scene-leak) | PASS |  |
| C02 | CHÍNH | DX-V11 (C rule bg-over-data) | PASS |  |
| C03 | THAM KHẢO | DX-V11 (C rule unlabelled-curve) | PASS |  |
| C04 | THAM KHẢO | DX-V11 (C rule axis-anchors) | FAIL | frames flagged = 2175 (need <= 0) |
| C05 | CHÍNH | DX-V11, DX-X4 (C rule grey-emphasis) | PASS |  |
| C06 | THAM KHẢO | DX-V11 (C rule number-colour) | FAIL | frames flagged = 5287 (need <= 0) |
| C07 | CHẶN | DX-V11 (C rule bar-proportion) | FAIL | frames flagged = 122 (need <= 0) |
| C10 | THAM KHẢO | DX-V1 (C rule level1) | PASS |  |
| C11 | THAM KHẢO | DX-V11 (C rule layout-repeat) | FAIL | layout repeats >2 in 90 s = 32 (need <= 0) |
| C12 | THAM KHẢO | DX-V11 (C rule split-view) | FAIL | split-view runs = 2 (need <= 0) |
| C13 | THAM KHẢO | DX-V11 (number–voice sync ±250 ms) | FAIL | worst |offset| ms = 21240 (need <= 250.0); pairs > 250 ms = 50 (need <= 0) |
| C14 | CHÍNH | DX-V11, DX-X4 (legible at 25%) | PASS |  |
| C15 | THAM KHẢO | DX-V5 (C rule tokens only) | FAIL | frames flagged = 43516 (need <= 0) |
| P01 | THAM KHẢO | DX-P2 | MISSING | artifact missing: out/package/thumb-1.json |
| T1 | THAM KHẢO | DX-A1 (sổ gu G-001, G-006) | FAIL | share of slots heard in a pause = 0.313673 (need >= 0.6) |
| T2 | THAM KHẢO | DX-A2 (sổ gu G-002) | PASS |  |
| T3 | THAM KHẢO | DX-R6 (sổ gu G-003) | FAIL | entries outside 150–400 ms = 1 (need <= 0) |
| T4 | THAM KHẢO | D-010 §6 (lượt đạo diễn: sfx dày), checks-appeal A19 | PASS |  |
| L1 | CHÍNH | DX-A1, DX-A9 (sổ gu G-006) | FAIL | voice/data 1–4 kHz ratio, 10th percentile (dB) = 17.432024 (need >= 20.0) |
| REG | CHẶN | CH §5, §4 khâu 3 (cổng hồi quy) | PASS |  |
