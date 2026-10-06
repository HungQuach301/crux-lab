# checks/ report

root: `/home/user/crux-lab/episodes/ep004`  
lock: `250ab298de4f912d34fdd02474aaa1af843ea9115e36fd0675630fcdcd1641de`  
master SHA-256: `839a96671e8fc3ca0a3565eb07e126780d2adcc6406d84d1c2660b8243b78b06`  
{'PASS': 30, 'FAIL': 15, 'MISSING': 43, 'ERROR': 1}

**Tập: TRƯỢT** (chỉ luật CHẶN làm trượt tập; luật CHÍNH không đạt cần bên dựng giải thích; luật THAM KHẢO chỉ báo số đo)

| cấp | luật | đạt | không đạt |
|---|---|---|---|
| CHẶN | 35 | 24 | F11 FAIL, F12 MISSING, S02 MISSING, S03 FAIL, S04 FAIL, S06 MISSING, S07 MISSING, S08 MISSING, S09 MISSING, S17 MISSING, C07 MISSING |
| CHÍNH | 11 | 1 | F07 FAIL, V03 MISSING, V08 MISSING, V09 MISSING, V11 MISSING, V12 MISSING, C02 MISSING, C05 MISSING, C14 MISSING, L1 MISSING |
| THAM KHẢO | 43 | 5 | A03 FAIL, A09 FAIL, A10 MISSING, A11 MISSING, A12 MISSING, A13 ERROR, A15 FAIL, A16 FAIL, A17 FAIL, S11 MISSING, S12 MISSING, S14 FAIL, S15 FAIL, S16 FAIL, R01 MISSING, R02 MISSING, R03 FAIL, R04 MISSING, R05 FAIL, R06 MISSING, V01 MISSING, V02 MISSING, V04 MISSING, V05 MISSING, V10 MISSING, C01 MISSING, C03 MISSING, C04 MISSING, C06 MISSING, C10 MISSING, C11 FAIL, C12 MISSING, C13 MISSING, C15 MISSING, P01 MISSING, T1 MISSING, T2 MISSING, T3 MISSING |

## Chỉ số trong ±5% quanh ngưỡng

- F04 (CHẶN) · video Mbps = 16.606816 (ngưỡng >= 16.0, đạt)
- F06 (CHẶN) · audio kbps = 280.238725 (ngưỡng >= 272.0, đạt)
- F07 (CHÍNH) · duration s = 477.504 (ngưỡng in [480.0, 900.0], không đạt)
- A18 (CHÍNH) · distinct voices (provider, voiceId, model) = 1 (ngưỡng <= 1, đạt)
- S15 (THAM KHẢO) · outro s = 19.6 (ngưỡng >= 20.0, không đạt)

| rule | tier | § | status | failing metrics |
|---|---|---|---|---|
| F01 | CHẶN | DX-F1, DX-F2 | PASS |  |
| F02 | CHẶN | DX-F1 | PASS |  |
| F03 | CHẶN | DX-F3 | PASS |  |
| F04 | CHẶN | DX-F2 | PASS |  |
| F05 | CHẶN | DX-F2 | PASS |  |
| F06 | CHẶN | DX-F4 | PASS |  |
| F07 | CHÍNH | DX-S1 (CH §1 length) | FAIL | duration s = 477.504 (need in [480.0, 900.0]) |
| F08 | CHẶN | DX-V5 | PASS |  |
| F09 | CHẶN | DX-F5 | PASS |  |
| F10 | CHẶN | DX-F6 | PASS |  |
| F11 | CHẶN | CH §4 khâu 3 (hợp đồng tập, K2) | FAIL | declared artefacts not delivered = 1 (need <= 0); release files not declared = 17 (need <= 0) |
| F12 | CHẶN | DX-A3 (sổ giấy phép), CH §5 (K3: quyền tài sản; K3.1: tài sản hình) | MISSING | artifact missing: out/checks/page.json |
| A01 | CHẶN | DX-A10 | PASS |  |
| A02 | CHẶN | DX-A10 | PASS |  |
| A03 | THAM KHẢO | DX-A10 | FAIL | LRA LU = 3.9 (need in [6.0, 10.0]) |
| A04 | CHẶN | DX-A10 | PASS |  |
| A05 | CHẶN | DX-A10 | PASS |  |
| A06 | CHẶN | DX-A10, DX-X5 | PASS |  |
| A07 | THAM KHẢO | DX-A9 | PASS |  |
| A08 | THAM KHẢO | DX-A9 | PASS |  |
| A09 | THAM KHẢO | DX-R6 | FAIL | silences 0.8-1.5 s = 0 (need >= 3) |
| A10 | THAM KHẢO | DX-A5 | MISSING | artifact missing: out/camera.json |
| A11 | THAM KHẢO | DX-A5 | MISSING | artifact missing: out/sfx-events.json |
| A12 | THAM KHẢO | DX-A3 | MISSING | artifact missing: out/tempo-map.json |
| A13 | THAM KHẢO | DX-A7 | ERROR | KeyError: 'raw' |
| A14 | CHẶN | DX-A7 | PASS |  |
| A15 | THAM KHẢO | DX-A7 | FAIL | wpm act cold-open = 171.364049 (need in [150.0, 160.0]); wpm act act1 = 170.748752 (need in [150.0, 160.0]); wpm act act2 = 169.475755 (need in [150.0, 160.0]); wpm act act3 = 170.001771 (need in [150.0, 160.0]); wpm act method = 235.135135 (need in [150.0, 160.0]); wpm act outro = 175.129219 (need in [150.0, 160.0]); sentences > 175 wpm = 30 (need <= 0) |
| A16 | THAM KHẢO | DX-A7 (K3, cảnh báo) | FAIL | fake break marks = 8 (need <= 0); sentences with a fake break = 8 (need <= 0) |
| A17 | THAM KHẢO | DX-A7, DX-R6 (K3, cảnh báo) | FAIL | abnormal sentences share = 0.27027 (need <= 0.1); abnormal gaps share = 0.363636 (need <= 0.1) |
| A18 | CHÍNH | DX-A8 (K3, cảnh báo) | PASS |  |
| S01 | CHẶN | DX-H1 | PASS |  |
| S02 | CHẶN | DX-H1 | MISSING | artifact missing: out/checks/page.json |
| S03 | CHẶN | DX-H4 | FAIL | cross-check on a declared host = False (need == True) |
| S04 | CHẶN | DX-H5 | FAIL | series pairs = 0 (need >= 1) |
| S05 | CHẶN | DX-H1, DX-H2 | PASS |  |
| S06 | CHẶN | DX-H6 | MISSING | artifact missing: out/checks/page.json |
| S07 | CHẶN | DX-H1, DX-H2 | MISSING | artifact missing: out/checks/page.json |
| S08 | CHẶN | DX-H2 | MISSING | artifact missing: out/checks/page.json |
| S09 | CHẶN | DX-H3 | MISSING | artifact missing: out/checks/page.json |
| S10 | CHẶN | DX-I1, DX-I2 | PASS |  |
| S11 | THAM KHẢO | DX-S6 | MISSING | artifact missing: out/checks/page.json |
| S12 | THAM KHẢO | DX-S7 | MISSING | artifact missing: out/checks/page.json |
| S13 | THAM KHẢO | DX-S8 (sổ gu G-009) | PASS |  |
| S14 | THAM KHẢO | DX-S10 | FAIL | breaks without ≥1 s silence = 2 (need <= 0) |
| S15 | THAM KHẢO | DX-S1 | FAIL | act order = ['cold-open', 'act1', 'act2', 'act3', 'method', 'outro'] (need == ['cold-open', 'ident', 'act1', 'act2', 'act3', 'method', 'outro']); ident s = None (need <= 3.0); outro s = 19.6 (need >= 20.0); total s = 477.5999 (need >= 540.0) |
| S16 | THAM KHẢO | DX-S3, RUBRIC H4 (sổ gu G-008) | FAIL | share tied to a character or scenario = 0.0 (need >= 0.75) |
| S17 | CHẶN | DX-H2 (claim), checks-appeal A1 | MISSING | artifact missing: out/checks/page.json |
| S18 | THAM KHẢO | DX-S3, DX-S4 (story.md §1), checks-appeal A2 | PASS |  |
| SH01 | CHẶN | D-006 Q3, checks-appeal A5 | PASS |  |
| SH02 | CHẶN | D-006 Q3, checks-appeal A5 | PASS |  |
| SH03 | CHẶN | DX-A10, checks-appeal A5 | PASS |  |
| SH04 | CHẶN | DX-A10, checks-appeal A5 | PASS |  |
| SH05 | CHẶN | DX-I1, DX-I2 (CHARTER §4 protected genes), checks-appeal A5 | PASS |  |
| R01 | THAM KHẢO | DX-R1 | MISSING | artifact missing: out/tension-map.json |
| R02 | THAM KHẢO | DX-R2 | MISSING | artifact missing: out/cues.json |
| R03 | THAM KHẢO | DX-R3 | FAIL | decisive claims = 0 (need >= 1); shortest pause s = None (need >= 1.0) |
| R04 | THAM KHẢO | DX-R4 | MISSING | artifact missing: out/transitions.json |
| R05 | THAM KHẢO | DX-R5 | FAIL | shots > 12 s = 17 (need <= 0); shot length CV = 0.268313 (need >= 0.4); act-2 scenes before climax = 0 (need >= 6) |
| R06 | THAM KHẢO | DX-V10 (picture check of cuts) | MISSING | artifact missing: out/transitions.json |
| V01 | THAM KHẢO | DX-V12 | MISSING | artifact missing: preprod/shotlist.json |
| V02 | THAM KHẢO | DX-V1 | MISSING | artifact missing: out/checks/page.json |
| V03 | CHÍNH | DX-V3 | MISSING | artifact missing: out/checks/page.json |
| V04 | THAM KHẢO | DX-V4, DX-X3 | MISSING | artifact missing: out/checks/page.json |
| V05 | THAM KHẢO | DX-V8 | MISSING | artifact missing: out/camera.json |
| V08 | CHÍNH | DX-V6 | MISSING | artifact missing: out/checks/page.json |
| V09 | CHÍNH | DX-V4, DX-X3 | MISSING | artifact missing: out/checks/page.json |
| V10 | THAM KHẢO | DX-V10 | MISSING | artifact missing: out/transitions.json |
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
| C11 | THAM KHẢO | DX-V11 (C rule layout-repeat) | FAIL | layout repeats >2 in 90 s = 17 (need <= 0) |
| C12 | THAM KHẢO | DX-V11 (C rule split-view) | MISSING | artifact missing: out/checks/page.json |
| C13 | THAM KHẢO | DX-V11 (number–voice sync ±250 ms) | MISSING | artifact missing: out/checks/page.json |
| C14 | CHÍNH | DX-V11, DX-X4 (legible at 25%) | MISSING | artifact missing: out/checks/page.json |
| C15 | THAM KHẢO | DX-V5 (C rule tokens only) | MISSING | artifact missing: out/checks/page.json |
| P01 | THAM KHẢO | DX-P2 | MISSING | artifact missing: out/package/thumb-1.png |
| T1 | THAM KHẢO | DX-A1 (sổ gu G-001, G-006) | MISSING | artifact missing: out/sonify-events.json or out/checks/page.json chartEvents |
| T2 | THAM KHẢO | DX-A2 (sổ gu G-002) | MISSING | artifact missing: out/tempo-map.json |
| T3 | THAM KHẢO | DX-R6 (sổ gu G-003) | MISSING | artifact missing: out/audio/stems/sfx.wav|flac |
| L1 | CHÍNH | DX-A1, DX-A9 (sổ gu G-006) | MISSING | artifact missing: out/audio/stems/sonify.wav|flac |
| REG | CHẶN | CH §5, §4 khâu 3 (cổng hồi quy) | PASS |  |
