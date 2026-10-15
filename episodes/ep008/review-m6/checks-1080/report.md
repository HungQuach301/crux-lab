# checks/ report

root: `/home/user/chk-ep008/episodes/ep008`  
lock: `b45516422eb936f244f7e5f5c77504974a94a6b0fec19e05254a0126f0c7f9d6`  
master SHA-256: `98833a2a1f3fd8c882841aa0f86bdae3beb187dd042733feef6a51aefe89fb0e`  
{'PASS': 57, 'FAIL': 43, 'MISSING': 4, 'ERROR': 1}

**Tập: TRƯỢT** (chỉ luật CHẶN làm trượt tập; luật CHÍNH không đạt cần bên dựng giải thích; luật THAM KHẢO chỉ báo số đo)

| cấp | luật | đạt | không đạt | lỗi thật | pháp lý | thủ tục |
|---|---|---|---|---|---|---|
| CHẶN | 37 | 32 | A14 FAIL, S01 MISSING, S03 FAIL, S04 MISSING, S05 MISSING | A14 | S03 | S01, S04, S05 |
| CHÍNH | 17 | 10 | F15 FAIL, S21 FAIL, V03 FAIL, V09 ERROR, V11 FAIL, V12 FAIL, L1 FAIL | F15, S21, V03, V11, V12, L1 | — | V09 |
| THAM KHẢO | 51 | 15 | A03 FAIL, A09 FAIL, A10 FAIL, A11 FAIL, A12 FAIL, A15 FAIL, A16 FAIL, A17 FAIL, S11 FAIL, S12 FAIL, S15 FAIL, S16 FAIL, S18 FAIL, R01 FAIL, R02 FAIL, R03 FAIL, R04 FAIL, R05 FAIL, R07 FAIL, R09 FAIL, V01 FAIL, V02 FAIL, V04 FAIL, V05 FAIL, V10 FAIL, V14 FAIL, V17 FAIL, C04 FAIL, C06 FAIL, C11 FAIL, C13 FAIL, C15 FAIL, T1 MISSING, T2 FAIL, T3 FAIL, T4 FAIL | A03, A09, A10, A11, A12, A15, A16, A17, S11, S12, S15, S16, S18, R01, R02, R03, R04, R05, R07, R09, V01, V02, V04, V05, V10, V14, V17, C04, C06, C11, C13, C15, T2, T3, T4 | — | T1 |

CHÍNH không đạt, chưa có giải thích trong `out/explanations.json`: F15, S21, V03, V09, V11, V12, L1

## Chỉ số trong ±5% quanh ngưỡng

- A15 (THAM KHẢO) · wpm act cold-open = 164.571128 (ngưỡng in [150.0, 160.0], không đạt)
- A15 (THAM KHẢO) · wpm act act1 = 163.695401 (ngưỡng in [150.0, 160.0], không đạt)
- A15 (THAM KHẢO) · wpm act act2 = 165.414661 (ngưỡng in [150.0, 160.0], không đạt)
- A18 (CHÍNH) · distinct voices (provider, voiceId, model) = 1 (ngưỡng <= 1, đạt)
- S06 (CHẶN) · coverage statements = 1 (ngưỡng >= 1, đạt)
- S06 (CHẶN) · year values shown in act2 = 26 (ngưỡng >= 26, đạt)
- S11 (THAM KHẢO) · core claims = 1 (ngưỡng >= 1, đạt)
- S15 (THAM KHẢO) · ident s = 3.0 (ngưỡng <= 3.0, đạt)
- SH06 (CHÍNH) · hooks = 1 (ngưỡng >= 1, đạt)
- V05 (THAM KHẢO) · worst ease ratio = 0.39 (ngưỡng <= 0.4, đạt)
- T4 (THAM KHẢO) · most events in 10 s = 6 (ngưỡng <= 6, đạt)

| rule | tier | § | status | loại (A40) | failing metrics |
|---|---|---|---|---|---|
| F01 | CHẶN | DX-F1, DX-F2 | PASS |  |  |
| F02 | CHẶN | DX-F1 | PASS |  |  |
| F03 | CHẶN | DX-F3 | PASS |  |  |
| F04 | CHẶN | DX-F2 | PASS |  |  |
| F05 | CHẶN | DX-F2 | PASS |  |  |
| F06 | CHẶN | DX-F4 | PASS |  |  |
| F07 | CHÍNH | DX-S1 (CH §1 length) | PASS |  |  |
| F08 | CHẶN | DX-V5 | PASS |  |  |
| F09 | CHẶN | DX-F5 | PASS |  |  |
| F10 | CHẶN | DX-F6 | PASS |  |  |
| F11 | CHẶN | CH §4 khâu 3 (hợp đồng tập, K2; K4.1: danh sách của nhà máy, checks-appeal A10, A16) | PASS |  |  |
| F12 | CHẶN | DX-A3 (sổ giấy phép), CH §5 (K3: quyền tài sản; K3.1: tài sản hình) | PASS |  |  |
| F13 | CHẶN | checks-appeal A39 (+ A44), RIGHTS.md §F (D-013, chủ dự án 13/10/2026), cine-lab rights_check | PASS |  |  |
| F15 | CHÍNH | checks-appeal A39 (CHÍNH: trung thực footage), RIGHTS.md §F3–F4 (D-013) | FAIL | lỗi thật | illustrative footage without label or with a claim number = 1 (need <= 0) |
| A01 | CHẶN | DX-A10 | PASS |  |  |
| A02 | CHẶN | DX-A10 | PASS |  |  |
| A03 | THAM KHẢO | DX-A10 | FAIL | lỗi thật | LRA LU = 3.6 (need in [6.0, 10.0]) |
| A04 | CHẶN | DX-A10 | PASS |  |  |
| A05 | CHẶN | DX-A10 | PASS |  |  |
| A06 | CHẶN | DX-A10, DX-X5 | PASS |  |  |
| A07 | THAM KHẢO | DX-A9 | PASS |  |  |
| A08 | THAM KHẢO | DX-A9 | PASS |  |  |
| A09 | THAM KHẢO | DX-R6 | FAIL | lỗi thật | silences 0.8-1.5 s = 2 (need >= 3) |
| A10 | THAM KHẢO | DX-A5 | FAIL | lỗi thật | Spearman speed~whoosh = 0.397941 (need >= 0.6); fast moves without whoosh = 34 (need <= 0) |
| A11 | THAM KHẢO | DX-A5 | FAIL | lỗi thật | Pearson pan~x = None (need >= 0.7) |
| A12 | THAM KHẢO | DX-A3 | FAIL | lỗi thật | accents = 3 (need >= 5); accents on a cut (%) = 0.0 (need >= 100.0); accents confirmed by onset (%) = 66.666667 (need >= 90.0) |
| A13 | THAM KHẢO | DX-A7 | PASS |  |  |
| A14 | CHẶN | DX-A7 | FAIL | lỗi thật | key words missing = 1 (need <= 0) |
| A15 | THAM KHẢO | DX-A7 | FAIL | lỗi thật | wpm act cold-open = 164.571128 (need in [150.0, 160.0]); wpm act act1 = 163.695401 (need in [150.0, 160.0]); wpm act act2 = 165.414661 (need in [150.0, 160.0]); wpm act act3 = 169.844358 (need in [150.0, 160.0]); wpm act method = 176.348813 (need in [150.0, 160.0]); sentences > 175 wpm = 42 (need <= 0) |
| A16 | THAM KHẢO | DX-A7 (K3, cảnh báo) | FAIL | lỗi thật | fake break marks = 14 (need <= 0); sentences with a fake break = 14 (need <= 0) |
| A17 | THAM KHẢO | DX-A7, DX-R6 (K3, cảnh báo) | FAIL | lỗi thật | abnormal sentences share = 0.23913 (need <= 0.1); abnormal gaps share = 0.271186 (need <= 0.1) |
| A18 | CHÍNH | DX-A8 (K3, cảnh báo) | PASS |  |  |
| S01 | CHẶN | DX-H1 | MISSING | thủ tục | artifact missing: an independent re-computation for model kind "rent-buy-twin-replay" (checks/py/r_model.py KINDS: ['fixed-cap-vs-index-growth', 'fixed-raise-vs-index-windows', 'float-vs-fixed-replay', 'lock-vs-roll-replay', 'ltv-first-passage', 'refinance-breakeven', 'retirement-6040', 'term-pair-weekly-replay']); the checking session writes it |
| S02 | CHẶN | DX-H1 | PASS |  |  |
| S03 | CHẶN | DX-H4 | FAIL | pháp lý | cross-check on a declared host = False (need == True) |
| S04 | CHẶN | DX-H5 | MISSING | thủ tục | artifact missing: contract.json: data.crosscheck |
| S05 | CHẶN | DX-H1, DX-H2 | MISSING | thủ tục | artifact missing: an independent re-computation for model kind "rent-buy-twin-replay" (checks/py/r_model.py KINDS: ['fixed-cap-vs-index-growth', 'fixed-raise-vs-index-windows', 'float-vs-fixed-replay', 'lock-vs-roll-replay', 'ltv-first-passage', 'refinance-breakeven', 'retirement-6040', 'term-pair-weekly-replay']); the checking session writes it |
| S06 | CHẶN | DX-H6 | PASS |  |  |
| S07 | CHẶN | DX-H1, DX-H2 | PASS |  |  |
| S08 | CHẶN | DX-H2 | PASS |  |  |
| S09 | CHẶN | DX-H3 | PASS |  |  |
| S10 | CHẶN | DX-I1, DX-I2 | PASS |  |  |
| S11 | THAM KHẢO | DX-S6 | FAIL | lỗi thật | share_buyer_ahead_10y callbacks w/ distinct meaning = 0 (need >= 3) |
| S12 | THAM KHẢO | DX-S7 | FAIL | lỗi thật | max new numbers in a scene = 15 (need <= 2) |
| S13 | THAM KHẢO | DX-S8 (sổ gu G-009) | PASS |  |  |
| S14 | THAM KHẢO | DX-S10 | PASS |  |  |
| S15 | THAM KHẢO | DX-S1 | FAIL | lỗi thật | act order = ['cold-open', 'ident', 'act1', 'act2', 'act3', 'method'] (need == ['cold-open', 'ident', 'act1', 'act2', 'act3', 'method', 'outro']); outro s = None (need >= 20.0) |
| S16 | THAM KHẢO | DX-S3, RUBRIC H4 (sổ gu G-008) | FAIL | lỗi thật | share tied to a character or scenario = 0.0 (need >= 0.75) |
| S17 | CHẶN | DX-H2 (claim), checks-appeal A1 | PASS |  |  |
| S18 | THAM KHẢO | DX-S3, DX-S4 (story.md §1), checks-appeal A2 | FAIL | lỗi thật | promise ends s = 39.247 (need <= 30.0) |
| S19 | CHẶN | DX-H1, DX-H4 (claim-risk), checks-appeal A20 | PASS |  | contract.json declares no claims.forbiddenAmounts: nothing to check |
| S20 | CHÍNH | DX-S7 (lời mang số), checks-appeal A17 | PASS |  |  |
| S21 | CHÍNH | DX-H1 (lỗi số = 0 cả ngoài video), cine-lab BAI-HOC-LL #53, checks-appeal A25 | FAIL | lỗi thật | numbers in the description without a claim = 1 (need <= 0) |
| S22 | THAM KHẢO | DX-H2 (claim-risk), cine-lab BAI-HOC-LL #62, checks-appeal A26 | PASS |  |  |
| S23 | CHÍNH | checks-appeal A45 (ep008 A41; chủ dự án 13/10, luật tạm), DX-I1 | PASS |  |  |
| SH01 | CHẶN | D-006 Q3, checks-appeal A5 | PASS |  |  |
| SH02 | CHẶN | D-006 Q3, checks-appeal A5 | PASS |  |  |
| SH03 | CHẶN | DX-A10, checks-appeal A5 | PASS |  |  |
| SH04 | CHẶN | DX-A10, checks-appeal A5 | PASS |  |  |
| SH05 | CHẶN | DX-I1, DX-I2 (CHARTER §4 protected genes), checks-appeal A5 | PASS |  |  |
| SH06 | CHÍNH | D-006 Q3, lessons T6-10, checks-appeal A30 | PASS |  |  |
| SH07 | CHÍNH | chủ dự án 13/10/2026 (1 Short per episode from Episode 8; D-006 Q3 2–3 before) | PASS |  |  |
| R01 | THAM KHẢO | DX-R1 | FAIL | lỗi thật | r cut rate = 0.023327 (need >= 0.8); r audio density = -0.003574 (need >= 0.6); acts with climax peak = 0 (need >= 3) |
| R02 | THAM KHẢO | DX-R2 | FAIL | lỗi thật | longest stretch without a break s = 266.1 (need <= 60.0) |
| R03 | THAM KHẢO | DX-R3 | FAIL | lỗi thật | shortest pause s = 0.0 (need >= 1.0); pauses < 1.0 s = 4 (need <= 0) |
| R04 | THAM KHẢO | DX-R4 | FAIL | lỗi thật | cuts on beat/action (%) = 20.0 (need >= 70.0) |
| R05 | THAM KHẢO | DX-R5 | FAIL | lỗi thật | shots > 12 s = 25 (need <= 0); act-2 scenes before climax = 0 (need >= 6) |
| R06 | THAM KHẢO | DX-V10 (picture check of cuts) | PASS |  |  |
| R07 | THAM KHẢO | DX-R (đồng bộ hình–lời), D-010 §6, checks-appeal A14 | FAIL | lỗi thật | visual cues within ±0.2 s (%) = 58.666667 (need >= 92.0) |
| R08 | THAM KHẢO | tổng kết Tập 5 §3.2 (nhịp, đo trước render), checks-appeal A23 | PASS |  |  |
| R09 | THAM KHẢO | checks-appeal A41 (b) (bản đồ liền mạch, chỉ báo tới khi hiệu chuẩn), BAN-DO-LIEN-MACH luật 1 và 4 | FAIL | lỗi thật | act turns with a hard cut = 5 (need <= 0); most used view share (%) = 30.995985 (need <= 20.0) |
| V01 | THAM KHẢO | DX-V12 | FAIL | lỗi thật | scenes without a shot = 14 (need <= 0); storyboard present = False (need == True); colour script present = False (need == True) |
| V02 | THAM KHẢO | DX-V1 | FAIL | lỗi thật | level-1 samples = 0 (need >= 1); level-1 placed (%) = None (need >= 90.0) |
| V03 | CHÍNH | DX-V3 | FAIL | lỗi thật | text outside safe area = 405 (need <= 0) |
| V04 | THAM KHẢO | DX-V4, DX-X3 | FAIL | lỗi thật | nina main colour is the declared #C9D3E2 = False (need == True); marcus main colour is the declared #E2D3C2 = False (need == True); priya main colour is the declared #D3E2C9 = False (need == True) |
| V05 | THAM KHẢO | DX-V8 | FAIL | lỗi thật | anticipation in moves ≥1 s (%) = 18.181818 (need >= 30.0); overshoot in moves ≥1 s (%) = 12.121212 (need >= 30.0); overshoot > 8% = 2 (need <= 0); peak |a| fw/s² = 33.66 (need <= 8.0) |
| V08 | CHÍNH | DX-V6 | PASS |  |  |
| V09 | CHÍNH | DX-V4, DX-X3 | ERROR | thủ tục | ValueError: invalid literal for int() with base 16: 'nu' |
| V10 | THAM KHẢO | DX-V10 | FAIL | lỗi thật | verified match cuts = 0 (need >= 5); verified J/L cuts = 0 (need >= 4) |
| V11 | CHÍNH | DX-V11 (C rule text-line-collision, upgraded to pixels) | FAIL | lỗi thật | text collisions = 1156 (need <= 0) |
| V12 | CHÍNH | DX-V9 (replaces the camera-move exemption) | FAIL | lỗi thật | text samples below NCC 0.97 = 7 (need <= 0) |
| V13 | THAM KHẢO | DX-V9, DX-V8 (replaces the camera-move exemption) | PASS |  |  |
| V14 | THAM KHẢO | D-010 quy tắc 1/2/3/7 (đoạn thế giới), checks-appeal A18 | FAIL | lỗi thật | first-5 s beats not in the world = 3 (need <= 0) |
| V15 | THAM KHẢO | D-010 quy tắc 5 (không quay lại thẻ chữ), checks-appeal A13 | PASS |  |  |
| V17 | THAM KHẢO | DX-V (đọc kịp), lessons T5-2, checks-appeal A24 | FAIL | lỗi thật | labels on screen too short to read = 15 (need <= 0) |
| C01 | THAM KHẢO | DX-V11 (C rule scene-leak) | PASS |  |  |
| C02 | CHÍNH | DX-V11 (C rule bg-over-data) | PASS |  |  |
| C03 | THAM KHẢO | DX-V11 (C rule unlabelled-curve) | PASS |  |  |
| C04 | THAM KHẢO | DX-V11 (C rule axis-anchors) | FAIL | lỗi thật | frames flagged = 139594 (need <= 0) |
| C05 | CHÍNH | DX-V11, DX-X4 (C rule grey-emphasis) | PASS |  |  |
| C06 | THAM KHẢO | DX-V11 (C rule number-colour) | FAIL | lỗi thật | frames flagged = 279 (need <= 0) |
| C07 | CHẶN | DX-V11 (C rule bar-proportion) | PASS |  |  |
| C10 | THAM KHẢO | DX-V1 (C rule level1) | PASS |  |  |
| C11 | THAM KHẢO | DX-V11 (C rule layout-repeat) | FAIL | lỗi thật | layout repeats >2 in 90 s = 32 (need <= 0) |
| C12 | THAM KHẢO | DX-V11 (C rule split-view) | PASS |  |  |
| C13 | THAM KHẢO | DX-V11 (number–voice sync ±250 ms) | FAIL | lỗi thật | worst |offset| ms = 17846 (need <= 250.0); pairs > 250 ms = 30 (need <= 0); spoken numbers not in ASR = 1 (need <= 0) |
| C14 | CHÍNH | DX-V11, DX-X4 (legible at 25%) | PASS |  |  |
| C15 | THAM KHẢO | DX-V5 (C rule tokens only) | FAIL | lỗi thật | frames flagged = 39904 (need <= 0) |
| P01 | THAM KHẢO | DX-P2 | PASS |  | no thumbnail in the delivery (package.thumbnails 0, or Episode 8 on: chủ dự án 13/10) |
| T1 | THAM KHẢO | DX-A1 (sổ gu G-001, G-006) | MISSING | thủ tục | artifact missing: contract.json: sonification.bandsHz |
| T2 | THAM KHẢO | DX-A2 (sổ gu G-002) | FAIL | lỗi thật | repeated phrases (%) = 13.114754 (need <= 5.0); longest run of repeated phrases = 2 (need <= 1) |
| T3 | THAM KHẢO | DX-R6 (sổ gu G-003) | FAIL | lỗi thật | entries outside 150–400 ms = 2 (need <= 0) |
| T4 | THAM KHẢO | D-010 §6 (lượt đạo diễn: sfx dày), checks-appeal A19 | FAIL | lỗi thật | segments over a density limit = 1 (need <= 0); highest share on plain words (%) = 55.6 (need <= 50.0) |
| L1 | CHÍNH | DX-A1, DX-A9 (sổ gu G-006) | FAIL | lỗi thật | voice/data 1–4 kHz ratio, 10th percentile (dB) = 18.535723 (need >= 20.0) |
| REG | CHẶN | CH §5, §4 khâu 3 (cổng hồi quy) | PASS |  |  |
