# checks/ report

root: `/home/user/crux-lab/episodes/ep005`  
lock: `d93276a491dd366c08ea0464d8de23bca80d82082a0c7be66ea2d555fd366b4a`  
master SHA-256: `61289c0c0ed2897154cb084c4bbe8ed7c2349050ec7aa9213ac5e1baa41086a8`  
{'PASS': 27, 'FAIL': 22, 'MISSING': 40, 'ERROR': 0}

**Tập: TRƯỢT** (chỉ luật CHẶN làm trượt tập; luật CHÍNH không đạt cần bên dựng giải thích; luật THAM KHẢO chỉ báo số đo)

| cấp | luật | đạt | không đạt |
|---|---|---|---|
| CHẶN | 35 | 19 | F01 FAIL, F08 FAIL, F11 FAIL, F12 MISSING, S02 MISSING, S06 MISSING, S07 MISSING, S08 MISSING, S09 MISSING, S17 MISSING, SH01 MISSING, SH02 MISSING, SH03 MISSING, SH04 MISSING, SH05 MISSING, C07 MISSING |
| CHÍNH | 11 | 1 | F07 FAIL, V03 MISSING, V08 MISSING, V09 MISSING, V11 MISSING, V12 MISSING, C02 MISSING, C05 MISSING, C14 MISSING, L1 MISSING |
| THAM KHẢO | 43 | 7 | A03 FAIL, A09 FAIL, A10 MISSING, A11 FAIL, A12 FAIL, A13 FAIL, A15 FAIL, A16 FAIL, A17 FAIL, S11 MISSING, S12 MISSING, S15 FAIL, S16 FAIL, R01 MISSING, R03 FAIL, R04 FAIL, R05 FAIL, R06 FAIL, V01 FAIL, V02 MISSING, V04 MISSING, V05 MISSING, V10 FAIL, C01 MISSING, C03 MISSING, C04 MISSING, C06 MISSING, C10 MISSING, C11 FAIL, C12 MISSING, C13 MISSING, C15 MISSING, P01 MISSING, T1 MISSING, T2 FAIL, T3 MISSING |

## Chỉ số trong ±5% quanh ngưỡng

- F07 (CHÍNH) · duration s = 462.633333 (ngưỡng in [480.0, 900.0], không đạt)
- A15 (THAM KHẢO) · wpm act act2 = 167.014258 (ngưỡng in [150.0, 160.0], không đạt)
- A18 (CHÍNH) · distinct voices (provider, voiceId, model) = 1 (ngưỡng <= 1, đạt)
- S04 (CHẶN) · mortgage30 tolerance = 0.5 (ngưỡng <= 0.5, đạt)
- S04 (CHẶN) · hpi_mom tolerance = 0.5 (ngưỡng <= 0.5, đạt)
- S15 (THAM KHẢO) · ident s = 3.0 (ngưỡng <= 3.0, đạt)
- S15 (THAM KHẢO) · outro s = 19.9333 (ngưỡng >= 20.0, không đạt)

| rule | tier | § | status | failing metrics |
|---|---|---|---|---|
| F01 | CHẶN | DX-F1, DX-F2 | FAIL | size = 960x540 (need == 1920x1080) |
| F02 | CHẶN | DX-F1 | PASS |  |
| F03 | CHẶN | DX-F3 | PASS |  |
| F04 | CHẶN | DX-F2 | PASS |  |
| F05 | CHẶN | DX-F2 | PASS |  |
| F06 | CHẶN | DX-F4 | PASS |  |
| F07 | CHÍNH | DX-S1 (CH §1 length) | FAIL | duration s = 462.633333 (need in [480.0, 900.0]) |
| F08 | CHẶN | DX-V5 | FAIL | worst banding (%) = 69.823785 (need <= 5.0) |
| F09 | CHẶN | DX-F5 | PASS |  |
| F10 | CHẶN | DX-F6 | PASS |  |
| F11 | CHẶN | CH §4 khâu 3 (hợp đồng tập, K2) | FAIL | declared artefacts not delivered = 7 (need <= 0) |
| F12 | CHẶN | DX-A3 (sổ giấy phép), CH §5 (K3: quyền tài sản; K3.1: tài sản hình) | MISSING | artifact missing: out/checks/page.json |
| A01 | CHẶN | DX-A10 | PASS |  |
| A02 | CHẶN | DX-A10 | PASS |  |
| A03 | THAM KHẢO | DX-A10 | FAIL | LRA LU = 3.5 (need in [6.0, 10.0]) |
| A04 | CHẶN | DX-A10 | PASS |  |
| A05 | CHẶN | DX-A10 | PASS |  |
| A06 | CHẶN | DX-A10, DX-X5 | PASS |  |
| A07 | THAM KHẢO | DX-A9 | PASS |  |
| A08 | THAM KHẢO | DX-A9 | PASS |  |
| A09 | THAM KHẢO | DX-R6 | FAIL | silences 0.8-1.5 s = 0 (need >= 3) |
| A10 | THAM KHẢO | DX-A5 | MISSING | artifact missing: out/camera.json |
| A11 | THAM KHẢO | DX-A5 | FAIL | Pearson pan~x = None (need >= 0.7) |
| A12 | THAM KHẢO | DX-A3 | FAIL | accents = 0 (need >= 5); accents on a cut (%) = None (need >= 100.0); accents confirmed by onset (%) = None (need >= 90.0) |
| A13 | THAM KHẢO | DX-A7 | FAIL | max |stretch-1| = 79.95167 (need <= 0.1) |
| A14 | CHẶN | DX-A7 | PASS |  |
| A15 | THAM KHẢO | DX-A7 | FAIL | wpm act cold-open = 168.31292 (need in [150.0, 160.0]); wpm act act1 = 181.073975 (need in [150.0, 160.0]); wpm act act2 = 167.014258 (need in [150.0, 160.0]); wpm act act3 = 173.076923 (need in [150.0, 160.0]); wpm act method = 203.007519 (need in [150.0, 160.0]); wpm act outro = 194.376528 (need in [150.0, 160.0]); sentences > 175 wpm = 42 (need <= 0) |
| A16 | THAM KHẢO | DX-A7 (K3, cảnh báo) | FAIL | fake break marks = 8 (need <= 0); sentences with a fake break = 8 (need <= 0) |
| A17 | THAM KHẢO | DX-A7, DX-R6 (K3, cảnh báo) | FAIL | abnormal sentences share = 0.285714 (need <= 0.1); abnormal gaps share = 0.42 (need <= 0.1) |
| A18 | CHÍNH | DX-A8 (K3, cảnh báo) | PASS |  |
| S01 | CHẶN | DX-H1 | PASS |  |
| S02 | CHẶN | DX-H1 | MISSING | artifact missing: out/checks/page.json |
| S03 | CHẶN | DX-H4 | PASS |  |
| S04 | CHẶN | DX-H5 | PASS |  |
| S05 | CHẶN | DX-H1, DX-H2 | PASS |  |
| S06 | CHẶN | DX-H6 | MISSING | artifact missing: out/checks/page.json |
| S07 | CHẶN | DX-H1, DX-H2 | MISSING | artifact missing: out/checks/page.json |
| S08 | CHẶN | DX-H2 | MISSING | artifact missing: out/checks/page.json |
| S09 | CHẶN | DX-H3 | MISSING | artifact missing: out/checks/page.json |
| S10 | CHẶN | DX-I1, DX-I2 | PASS |  |
| S11 | THAM KHẢO | DX-S6 | MISSING | artifact missing: out/checks/page.json |
| S12 | THAM KHẢO | DX-S7 | MISSING | artifact missing: out/checks/page.json |
| S13 | THAM KHẢO | DX-S8 (sổ gu G-009) | PASS |  |
| S14 | THAM KHẢO | DX-S10 | PASS |  |
| S15 | THAM KHẢO | DX-S1 | FAIL | outro s = 19.9333 (need >= 20.0) |
| S16 | THAM KHẢO | DX-S3, RUBRIC H4 (sổ gu G-008) | FAIL | share tied to a character or scenario = 0.25 (need >= 0.75) |
| S17 | CHẶN | DX-H2 (claim), checks-appeal A1 | MISSING | artifact missing: out/checks/page.json |
| S18 | THAM KHẢO | DX-S3, DX-S4 (story.md §1), checks-appeal A2 | PASS |  |
| SH01 | CHẶN | D-006 Q3, checks-appeal A5 | MISSING | artifact missing: contract.json: shorts = [{file}] |
| SH02 | CHẶN | D-006 Q3, checks-appeal A5 | MISSING | artifact missing: contract.json: shorts = [{file}] |
| SH03 | CHẶN | DX-A10, checks-appeal A5 | MISSING | artifact missing: contract.json: shorts = [{file}] |
| SH04 | CHẶN | DX-A10, checks-appeal A5 | MISSING | artifact missing: contract.json: shorts = [{file}] |
| SH05 | CHẶN | DX-I1, DX-I2 (CHARTER §4 protected genes), checks-appeal A5 | MISSING | artifact missing: contract.json: shorts = [{file}] |
| R01 | THAM KHẢO | DX-R1 | MISSING | artifact missing: out/audio/stems/whoosh.wav|flac |
| R02 | THAM KHẢO | DX-R2 | PASS |  |
| R03 | THAM KHẢO | DX-R3 | FAIL | shortest pause s = 0.0 (need >= 1.0); pauses < 1.0 s = 3 (need <= 0) |
| R04 | THAM KHẢO | DX-R4 | FAIL | cuts on beat/action (%) = 33.333333 (need >= 70.0) |
| R05 | THAM KHẢO | DX-R5 | FAIL | shots > 12 s = 17 (need <= 0); act-2 scenes before climax = 0 (need >= 6) |
| R06 | THAM KHẢO | DX-V10 (picture check of cuts) | FAIL | cuts visible in picture (%) = 0.0 (need >= 90.0) |
| V01 | THAM KHẢO | DX-V12 | FAIL | scenes without a shot = 2 (need <= 0); storyboard present = False (need == True); colour script present = False (need == True) |
| V02 | THAM KHẢO | DX-V1 | MISSING | artifact missing: out/checks/page.json |
| V03 | CHÍNH | DX-V3 | MISSING | artifact missing: out/checks/page.json |
| V04 | THAM KHẢO | DX-V4, DX-X3 | MISSING | artifact missing: contract.json: characters.owen.color |
| V05 | THAM KHẢO | DX-V8 | MISSING | artifact missing: out/camera.json |
| V08 | CHÍNH | DX-V6 | MISSING | artifact missing: out/checks/page.json |
| V09 | CHÍNH | DX-V4, DX-X3 | MISSING | artifact missing: contract.json: characters.owen.color |
| V10 | THAM KHẢO | DX-V10 | FAIL | verified match cuts = 2 (need >= 5); verified J/L cuts = 0 (need >= 4) |
| V11 | CHÍNH | DX-V11 (C rule text-line-collision, upgraded to pixels) | MISSING | artifact missing: out/checks/page.json |
| V12 | CHÍNH | DX-V9 (replaces the camera-move exemption) | MISSING | artifact missing: out/checks/page.json |
| V13 | THAM KHẢO | DX-V9, DX-V8 (replaces the camera-move exemption) | PASS |  |
| C01 | THAM KHẢO | DX-V11 (C rule scene-leak) | MISSING | artifact missing: out/checks/page.json |
| C02 | CHÍNH | DX-V11 (C rule bg-over-data) | MISSING | artifact missing: out/checks/page.json |
| C03 | THAM KHẢO | DX-V11 (C rule unlabelled-curve) | MISSING | artifact missing: out/checks/page.json |
| C04 | THAM KHẢO | DX-V11 (C rule axis-anchors) | MISSING | artifact missing: out/checks/page.json |
| C05 | CHÍNH | DX-V11, DX-X4 (C rule grey-emphasis) | MISSING | artifact missing: out/checks/page.json |
| C06 | THAM KHẢO | DX-V11 (C rule number-colour) | MISSING | artifact missing: out/checks/page.json |
| C07 | CHẶN | DX-V11 (C rule bar-proportion) | MISSING | artifact missing: out/checks/page.json |
| C10 | THAM KHẢO | DX-V1 (C rule level1) | MISSING | artifact missing: out/checks/page.json |
| C11 | THAM KHẢO | DX-V11 (C rule layout-repeat) | FAIL | layout repeats >2 in 90 s = 19 (need <= 0) |
| C12 | THAM KHẢO | DX-V11 (C rule split-view) | MISSING | artifact missing: out/checks/page.json |
| C13 | THAM KHẢO | DX-V11 (number–voice sync ±250 ms) | MISSING | artifact missing: out/checks/page.json |
| C14 | CHÍNH | DX-V11, DX-X4 (legible at 25%) | MISSING | artifact missing: out/checks/page.json |
| C15 | THAM KHẢO | DX-V5 (C rule tokens only) | MISSING | artifact missing: out/checks/page.json |
| P01 | THAM KHẢO | DX-P2 | MISSING | artifact missing: out/package/thumb-1.png |
| T1 | THAM KHẢO | DX-A1 (sổ gu G-001, G-006) | MISSING | artifact missing: contract.json: sonification.bandsHz |
| T2 | THAM KHẢO | DX-A2 (sổ gu G-002) | FAIL | repeated phrases (%) = 12.962963 (need <= 5.0); longest run of repeated phrases = 2 (need <= 1) |
| T3 | THAM KHẢO | DX-R6 (sổ gu G-003) | MISSING | artifact missing: out/audio/stems/whoosh.wav|flac |
| L1 | CHÍNH | DX-A1, DX-A9 (sổ gu G-006) | MISSING | artifact missing: out/audio/stems/whoosh.wav|flac |
| REG | CHẶN | CH §5, §4 khâu 3 (cổng hồi quy) | PASS | first version: nothing to compare |
