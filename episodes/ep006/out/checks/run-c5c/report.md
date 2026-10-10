# checks/ report

root: `/home/user/chk-c5/episodes/ep006`  
lock: `4d688acd8e9b756a805597384c393704312ae1569edc3367ce387e24f4d8f969`  
master SHA-256: `e6bd91367519b49184cbaafb772d5e8f1450b94c8692aa0cdc8139e92548a9c6`  
{'PASS': 64, 'FAIL': 33, 'MISSING': 1, 'ERROR': 1}

**Tập: ĐẠT** (chỉ luật CHẶN làm trượt tập; luật CHÍNH không đạt cần bên dựng giải thích; luật THAM KHẢO chỉ báo số đo)

| cấp | luật | đạt | không đạt |
|---|---|---|---|
| CHẶN | 36 | 36 | — |
| CHÍNH | 13 | 12 | V11 FAIL |
| THAM KHẢO | 50 | 16 | A03 FAIL, A10 FAIL, A11 FAIL, A12 ERROR, A13 FAIL, A15 FAIL, A16 FAIL, A17 FAIL, S11 FAIL, S12 FAIL, S15 FAIL, S16 FAIL, S22 FAIL, R01 MISSING, R02 FAIL, R03 FAIL, R04 FAIL, R05 FAIL, R07 FAIL, R08 FAIL, V01 FAIL, V02 FAIL, V04 FAIL, V05 FAIL, V10 FAIL, V14 FAIL, V17 FAIL, C06 FAIL, C11 FAIL, C12 FAIL, C13 FAIL, C15 FAIL, P01 FAIL, T1 FAIL |

## Chỉ số trong ±5% quanh ngưỡng

- A15 (THAM KHẢO) · wpm act act2 = 165.82679 (ngưỡng in [150.0, 160.0], không đạt)
- A15 (THAM KHẢO) · wpm act act3 = 162.640959 (ngưỡng in [150.0, 160.0], không đạt)
- A15 (THAM KHẢO) · wpm act outro = 167.808219 (ngưỡng in [150.0, 160.0], không đạt)
- A18 (CHÍNH) · distinct voices (provider, voiceId, model) = 1 (ngưỡng <= 1, đạt)
- S04 (CHẶN) · series pairs = 1 (ngưỡng >= 1, đạt)
- S04 (CHẶN) · cpi_yoy tolerance = 0.5 (ngưỡng <= 0.5, đạt)
- S06 (CHẶN) · coverage statements = 1 (ngưỡng >= 1, đạt)
- S06 (CHẶN) · case values shown in act2 = 715 (ngưỡng >= 715, đạt)
- S11 (THAM KHẢO) · windows_20y acts = 2 (ngưỡng >= 2, đạt)
- S11 (THAM KHẢO) · windows_2pct_kept_up_20y scenes = 3 (ngưỡng >= 3, đạt)
- S11 (THAM KHẢO) · guide_real_2pct_end_pct scenes = 3 (ngưỡng >= 3, đạt)
- S11 (THAM KHẢO) · guide_real_2pct_end_pct acts = 2 (ngưỡng >= 2, đạt)
- S11 (THAM KHẢO) · raise_needed_half_20y_pct acts = 2 (ngưỡng >= 2, đạt)
- S13 (THAM KHẢO) · sentence length CV (≥ 4 words) = 0.362272 (ngưỡng >= 0.35, đạt)
- S15 (THAM KHẢO) · ident s = 3.0 (ngưỡng <= 3.0, đạt)
- S15 (THAM KHẢO) · outro s = 19.8333 (ngưỡng >= 20.0, không đạt)
- V09 (CHÍNH) · declared characters seen on screen = 3 (ngưỡng >= 3, đạt)
- P01 (THAM KHẢO) · thumb 1 token share (%) = 98.707257 (ngưỡng >= 97.0, đạt)
- P01 (THAM KHẢO) · thumb 2 token share (%) = 98.707257 (ngưỡng >= 97.0, đạt)
- P01 (THAM KHẢO) · thumb 3 token share (%) = 100.0 (ngưỡng >= 97.0, đạt)
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
| A03 | THAM KHẢO | DX-A10 | FAIL | LRA LU = 3.7 (need in [6.0, 10.0]) |
| A04 | CHẶN | DX-A10 | PASS |  |
| A05 | CHẶN | DX-A10 | PASS |  |
| A06 | CHẶN | DX-A10, DX-X5 | PASS |  |
| A07 | THAM KHẢO | DX-A9 | PASS |  |
| A08 | THAM KHẢO | DX-A9 | PASS |  |
| A09 | THAM KHẢO | DX-R6 | PASS |  |
| A10 | THAM KHẢO | DX-A5 | FAIL | Spearman speed~whoosh = -0.366644 (need >= 0.6); fast moves without whoosh = 30 (need <= 0) |
| A11 | THAM KHẢO | DX-A5 | FAIL | Pearson pan~x = None (need >= 0.7) |
| A12 | THAM KHẢO | DX-A3 | ERROR | TypeError: unsupported operand type(s) for -: 'float' and 'dict' |
| A13 | THAM KHẢO | DX-A7 | FAIL | max |stretch-1| = 165.74415 (need <= 0.1) |
| A14 | CHẶN | DX-A7 | PASS |  |
| A15 | THAM KHẢO | DX-A7 | FAIL | wpm act cold-open = 186.673199 (need in [150.0, 160.0]); wpm act act1 = 169.055549 (need in [150.0, 160.0]); wpm act act2 = 165.82679 (need in [150.0, 160.0]); wpm act act3 = 162.640959 (need in [150.0, 160.0]); wpm act method = 189.774697 (need in [150.0, 160.0]); wpm act outro = 167.808219 (need in [150.0, 160.0]); sentences > 175 wpm = 37 (need <= 0) |
| A16 | THAM KHẢO | DX-A7 (K3, cảnh báo) | FAIL | fake break marks = 14 (need <= 0); sentences with a fake break = 14 (need <= 0) |
| A17 | THAM KHẢO | DX-A7, DX-R6 (K3, cảnh báo) | FAIL | abnormal sentences share = 0.253012 (need <= 0.1); abnormal gaps share = 0.320755 (need <= 0.1) |
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
| S11 | THAM KHẢO | DX-S6 | FAIL | windows_20y callbacks w/ distinct meaning = 0 (need >= 3); windows_2pct_kept_up_20y acts = 1 (need >= 2); windows_2pct_kept_up_20y callbacks w/ distinct meaning = 0 (need >= 3); share_2pct_kept_up_20y_pct scenes = 1 (need >= 3); share_2pct_kept_up_20y_pct acts = 1 (need >= 2); share_2pct_kept_up_20y_pct callbacks w/ distinct meaning = 0 (need >= 3); median_real_value_2pct_payment_after_20y_pct scenes = 2 (need >= 3); median_real_value_2pct_payment_after_20y_pct acts = 1 (need >= 2); median_real_value_2pct_payment_after_20y_pct callbacks w/ distinct meaning = 0 (need >= 3); worst_real_value_2pct_payment_after_20y_pct scenes = 2 (need >= 3); worst_real_value_2pct_payment_after_20y_pct acts = 1 (need >= 2); worst_real_value_2pct_payment_after_20y_pct callbacks w/ distinct meaning = 0 (need >= 3); guide_real_2pct_end_pct callbacks w/ distinct meaning = 0 (need >= 3); raise_needed_half_20y_pct scenes = 2 (need >= 3); raise_needed_half_20y_pct callbacks w/ distinct meaning = 0 (need >= 3) |
| S12 | THAM KHẢO | DX-S7 | FAIL | new numbers = 72 (need <= 67.075); max new numbers in a scene = 9 (need <= 2); axis claims shown outside axes = 19 (need <= 0) |
| S13 | THAM KHẢO | DX-S8 (sổ gu G-009) | PASS |  |
| S14 | THAM KHẢO | DX-S10 | PASS |  |
| S15 | THAM KHẢO | DX-S1 | FAIL | outro s = 19.8333 (need >= 20.0) |
| S16 | THAM KHẢO | DX-S3, RUBRIC H4 (sổ gu G-008) | FAIL | share tied to a character or scenario = 0.5 (need >= 0.75) |
| S17 | CHẶN | DX-H2 (claim), checks-appeal A1 | PASS |  |
| S18 | THAM KHẢO | DX-S3, DX-S4 (story.md §1), checks-appeal A2 | PASS |  |
| S19 | CHẶN | DX-H1, DX-H4 (claim-risk), checks-appeal A20 | PASS |  |
| S20 | CHÍNH | DX-S7 (lời mang số), checks-appeal A17 | PASS |  |
| S21 | CHÍNH | DX-H1 (lỗi số = 0 cả ngoài video), cine-lab BAI-HOC-LL #53, checks-appeal A25 | PASS |  |
| S22 | THAM KHẢO | DX-H2 (claim-risk), cine-lab BAI-HOC-LL #62, checks-appeal A26 | FAIL | units mixing sources or periods = 2 (need <= 0) |
| SH01 | CHẶN | D-006 Q3, checks-appeal A5 | PASS |  |
| SH02 | CHẶN | D-006 Q3, checks-appeal A5 | PASS |  |
| SH03 | CHẶN | DX-A10, checks-appeal A5 | PASS |  |
| SH04 | CHẶN | DX-A10, checks-appeal A5 | PASS |  |
| SH05 | CHẶN | DX-I1, DX-I2 (CHARTER §4 protected genes), checks-appeal A5 | PASS |  |
| R01 | THAM KHẢO | DX-R1 | MISSING | artifact missing: out/tension-map.png |
| R02 | THAM KHẢO | DX-R2 | FAIL | longest stretch without a break s = 157.717 (need <= 60.0) |
| R03 | THAM KHẢO | DX-R3 | FAIL | shortest pause s = 0.0 (need >= 1.0); pauses < 1.0 s = 5 (need <= 0) |
| R04 | THAM KHẢO | DX-R4 | FAIL | cuts on beat/action (%) = 0.0 (need >= 70.0) |
| R05 | THAM KHẢO | DX-R5 | FAIL | shots > 12 s = 22 (need <= 0); act-2 scenes before climax = 0 (need >= 6) |
| R06 | THAM KHẢO | DX-V10 (picture check of cuts) | PASS |  |
| R07 | THAM KHẢO | DX-R (đồng bộ hình–lời), D-010 §6, checks-appeal A14 | FAIL | visual cues within ±0.2 s (%) = 70.338983 (need >= 92.0) |
| R08 | THAM KHẢO | tổng kết Tập 5 §3.2 (nhịp, đo trước render), checks-appeal A23 | FAIL | still stretches > 8 s = 7 (need <= 0); longest still stretch s = 11.28 (need <= 8.0) |
| V01 | THAM KHẢO | DX-V12 | FAIL | scenes without a shot = 7 (need <= 0); storyboard present = False (need == True); colour script present = False (need == True) |
| V02 | THAM KHẢO | DX-V1 | FAIL | level-1 samples = 0 (need >= 1); level-1 placed (%) = None (need >= 90.0) |
| V03 | CHÍNH | DX-V3 | PASS |  |
| V04 | THAM KHẢO | DX-V4, DX-X3 | FAIL | carl colour share = 0.900969 (need >= 0.95); carl shape share = 0.900969 (need >= 0.95); edna colour share = 0.810573 (need >= 0.95); edna shape share = 0.810573 (need >= 0.95) |
| V05 | THAM KHẢO | DX-V8 | FAIL | anticipation in moves ≥1 s (%) = 0.0 (need >= 30.0); overshoot in moves ≥1 s (%) = 0.0 (need >= 30.0); overshoot > 8% = 4 (need <= 0); peak |a| fw/s² = 39.81 (need <= 8.0) |
| V08 | CHÍNH | DX-V6 | PASS |  |
| V09 | CHÍNH | DX-V4, DX-X3 | PASS |  |
| V10 | THAM KHẢO | DX-V10 | FAIL | verified match cuts = 0 (need >= 5); verified J/L cuts = 0 (need >= 4) |
| V11 | CHÍNH | DX-V11 (C rule text-line-collision, upgraded to pixels) | FAIL | text collisions = 32 (need <= 0) |
| V12 | CHÍNH | DX-V9 (replaces the camera-move exemption) | PASS |  |
| V13 | THAM KHẢO | DX-V9, DX-V8 (replaces the camera-move exemption) | PASS |  |
| V14 | THAM KHẢO | D-010 quy tắc 1/2/3/7 (đoạn thế giới), checks-appeal A18 | FAIL | first-5 s beats not in the world = 1 (need <= 0) |
| V15 | THAM KHẢO | D-010 quy tắc 5 (không quay lại thẻ chữ), checks-appeal A13 | PASS |  |
| V17 | THAM KHẢO | DX-V (đọc kịp), lessons T5-2, checks-appeal A24 | FAIL | labels on screen too short to read = 18 (need <= 0) |
| C01 | THAM KHẢO | DX-V11 (C rule scene-leak) | PASS |  |
| C02 | CHÍNH | DX-V11 (C rule bg-over-data) | PASS |  |
| C03 | THAM KHẢO | DX-V11 (C rule unlabelled-curve) | PASS |  |
| C04 | THAM KHẢO | DX-V11 (C rule axis-anchors) | PASS |  |
| C05 | CHÍNH | DX-V11, DX-X4 (C rule grey-emphasis) | PASS |  |
| C06 | THAM KHẢO | DX-V11 (C rule number-colour) | FAIL | frames flagged = 3281 (need <= 0) |
| C07 | CHẶN | DX-V11 (C rule bar-proportion) | PASS |  |
| C10 | THAM KHẢO | DX-V1 (C rule level1) | PASS |  |
| C11 | THAM KHẢO | DX-V11 (C rule layout-repeat) | FAIL | layout repeats >2 in 90 s = 29 (need <= 0) |
| C12 | THAM KHẢO | DX-V11 (C rule split-view) | FAIL | split-view runs = 2 (need <= 0) |
| C13 | THAM KHẢO | DX-V11 (number–voice sync ±250 ms) | FAIL | worst |offset| ms = 20900 (need <= 250.0); pairs > 250 ms = 41 (need <= 0) |
| C14 | CHÍNH | DX-V11, DX-X4 (legible at 25%) | PASS |  |
| C15 | THAM KHẢO | DX-V5 (C rule tokens only) | FAIL | frames flagged = 38335 (need <= 0) |
| P01 | THAM KHẢO | DX-P2 | FAIL | thumb texts below 90 px = 5 (need <= 0) |
| T1 | THAM KHẢO | DX-A1 (sổ gu G-001, G-006) | FAIL | share of slots heard in a pause = 0.357576 (need >= 0.6) |
| T2 | THAM KHẢO | DX-A2 (sổ gu G-002) | PASS |  |
| T3 | THAM KHẢO | DX-R6 (sổ gu G-003) | PASS |  |
| T4 | THAM KHẢO | D-010 §6 (lượt đạo diễn: sfx dày), checks-appeal A19 | PASS |  |
| L1 | CHÍNH | DX-A1, DX-A9 (sổ gu G-006) | PASS |  |
| REG | CHẶN | CH §5, §4 khâu 3 (cổng hồi quy) | PASS | first version: nothing to compare |
