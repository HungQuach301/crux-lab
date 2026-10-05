# checks/ report

root: `/tmp/claude-0/-home-user-crux-lab/7feba40e-1932-5b7d-90df-5c7e79c0113c/scratchpad/lc1/episodes/ep003`  
lock: `a20c6878c0dc1c1e9320db4553c92144ed4a9c46cd69ad4c20c9899696483791`  
master SHA-256: `3b8978adb4e1695e64f2b752dbbfff37b04744dc97d18fd31b27bc143d2444dc`  
{'PASS': 19, 'FAIL': 21, 'MISSING': 42, 'ERROR': 0}

**Tập: TRƯỢT** (chỉ luật CHẶN làm trượt tập; luật CHÍNH không đạt cần bên dựng giải thích; luật THAM KHẢO chỉ báo số đo)

| cấp | luật | đạt | không đạt |
|---|---|---|---|
| CHẶN | 29 | 12 | F01 FAIL, F04 FAIL, F05 FAIL, F06 FAIL, F09 FAIL, F10 MISSING, F11 MISSING, F12 MISSING, A14 FAIL, S02 MISSING, S03 FAIL, S04 FAIL, S06 MISSING, S07 MISSING, S08 MISSING, S09 MISSING, C07 MISSING |
| CHÍNH | 11 | 3 | V03 MISSING, V08 MISSING, V09 MISSING, V11 MISSING, V12 MISSING, C02 MISSING, C05 MISSING, C14 MISSING |
| THAM KHẢO | 42 | 4 | A03 FAIL, A08 FAIL, A09 FAIL, A10 MISSING, A11 MISSING, A12 FAIL, A13 MISSING, A15 FAIL, A16 FAIL, A17 FAIL, S11 MISSING, S12 MISSING, S14 MISSING, S15 FAIL, S16 FAIL, R01 MISSING, R02 MISSING, R03 FAIL, R04 MISSING, R05 FAIL, R06 MISSING, V01 MISSING, V02 MISSING, V04 MISSING, V05 MISSING, V10 MISSING, C01 MISSING, C03 MISSING, C04 MISSING, C06 MISSING, C10 MISSING, C12 MISSING, C13 MISSING, C15 MISSING, P01 MISSING, T1 MISSING, T2 FAIL, T3 FAIL |

CHÍNH không đạt, chưa có giải thích trong `out/explanations.json`: V03, V08, V09, V11, V12, C02, C05, C14

## Chỉ số trong ±5% quanh ngưỡng

- A08 (THAM KHẢO) · median 1-4 kHz drop dB = 5.735748 (ngưỡng >= 6.0, không đạt)
- A18 (CHÍNH) · distinct voices (provider, voiceId, model) = 1 (ngưỡng <= 1, đạt)
- S03 (CHẶN) · files = 2 (ngưỡng >= 2, đạt)
- S15 (THAM KHẢO) · total s = 570.0 (ngưỡng >= 600.0, không đạt)

| rule | tier | § | status | failing metrics |
|---|---|---|---|---|
| F01 | CHẶN | DX-F1, DX-F2 | FAIL | size = 1280x720 (need == 1920x1080) |
| F02 | CHẶN | DX-F1 | PASS |  |
| F03 | CHẶN | DX-F3 | PASS |  |
| F04 | CHẶN | DX-F2 | FAIL | video Mbps = 0.097165 (need >= 16.0) |
| F05 | CHẶN | DX-F2 | FAIL | color_primaries = None (need == bt709); color_transfer = None (need == bt709); color_space = None (need == bt709); color_range = None (need == tv) |
| F06 | CHẶN | DX-F4 | FAIL | audio kbps = 195.369207 (need >= 272.0) |
| F07 | CHÍNH | DX-S1 (CH §1 length) | PASS |  |
| F08 | CHẶN | DX-V5 | PASS |  |
| F09 | CHẶN | DX-F5 | FAIL | lines > 42 chars = 63 (need <= 0); cues outside 1-7 s = 28 (need <= 0) |
| F10 | CHẶN | DX-F6 | MISSING | artifact missing: out/package/description.md |
| F11 | CHẶN | CH §4 khâu 3 (hợp đồng tập, K2) | MISSING | artifact missing: contract.json: artefacts.M3 |
| F12 | CHẶN | DX-A3 (sổ giấy phép), CH §5 (K3: quyền tài sản; K3.1: tài sản hình) | MISSING | artifact missing: out/rights.json |
| A01 | CHẶN | DX-A10 | PASS |  |
| A02 | CHẶN | DX-A10 | PASS |  |
| A03 | THAM KHẢO | DX-A10 | FAIL | LRA LU = 3.4 (need in [6.0, 10.0]) |
| A04 | CHẶN | DX-A10 | PASS |  |
| A05 | CHẶN | DX-A10 | PASS |  |
| A06 | CHẶN | DX-A10, DX-X5 | PASS |  |
| A07 | THAM KHẢO | DX-A9 | PASS |  |
| A08 | THAM KHẢO | DX-A9 | FAIL | median 1-4 kHz drop dB = 5.735748 (need >= 6.0) |
| A09 | THAM KHẢO | DX-R6 | FAIL | silences 0.8-1.5 s = 0 (need >= 3) |
| A10 | THAM KHẢO | DX-A5 | MISSING | artifact missing: out/camera.json |
| A11 | THAM KHẢO | DX-A5 | MISSING | artifact missing: out/sfx-events.json |
| A12 | THAM KHẢO | DX-A3 | FAIL | accents on a cut (%) = 0.0 (need >= 100.0) |
| A13 | THAM KHẢO | DX-A7 | MISSING | artifact missing: S01.0e27330e.seed1.mp3 |
| A14 | CHẶN | DX-A7 | FAIL | key words missing = 1 (need <= 0) |
| A15 | THAM KHẢO | DX-A7 | FAIL | wpm act cold-open = 169.731259 (need in [150.0, 160.0]); wpm act act1 = 177.306208 (need in [150.0, 160.0]); wpm act act2 = 170.055923 (need in [150.0, 160.0]); wpm act act3 = 174.627732 (need in [150.0, 160.0]); wpm act method = 180.327869 (need in [150.0, 160.0]); wpm act outro = 176.875957 (need in [150.0, 160.0]); sentences > 175 wpm = 34 (need <= 0) |
| A16 | THAM KHẢO | DX-A7 (K3, cảnh báo) | FAIL | fake break marks = 11 (need <= 0); sentences with a fake break = 11 (need <= 0) |
| A17 | THAM KHẢO | DX-A7, DX-R6 (K3, cảnh báo) | FAIL | abnormal sentences share = 0.147059 (need <= 0.1) |
| A18 | CHÍNH | DX-A8 (K3, cảnh báo) | PASS |  |
| S01 | CHẶN | DX-H1 | PASS |  |
| S02 | CHẶN | DX-H1 | MISSING | artifact missing: out/checks/page.json |
| S03 | CHẶN | DX-H4 | FAIL | cross-check on a declared host = False (need == True) |
| S04 | CHẶN | DX-H5 | FAIL | series pairs = 0 (need >= 1) |
| S05 | CHẶN | DX-H1, DX-H2 | PASS |  |
| S06 | CHẶN | DX-H6 | MISSING | artifact missing: contract.json: coverage |
| S07 | CHẶN | DX-H1, DX-H2 | MISSING | artifact missing: out/checks/page.json |
| S08 | CHẶN | DX-H2 | MISSING | artifact missing: out/checks/page.json |
| S09 | CHẶN | DX-H3 | MISSING | artifact missing: out/checks/page.json |
| S10 | CHẶN | DX-I1, DX-I2 | PASS |  |
| S11 | THAM KHẢO | DX-S6 | MISSING | artifact missing: out/checks/page.json |
| S12 | THAM KHẢO | DX-S7 | MISSING | artifact missing: out/checks/page.json |
| S13 | THAM KHẢO | DX-S8 (sổ gu G-009) | PASS |  |
| S14 | THAM KHẢO | DX-S10 | MISSING | artifact missing: out/adbreaks.json |
| S15 | THAM KHẢO | DX-S1 | FAIL | act order = ['cold-open', 'act1', 'act2', 'act3', 'method', 'outro'] (need == ['cold-open', 'ident', 'act1', 'act2', 'act3', 'method', 'outro']); cold open s = 64.457 (need <= 15.0); ident s = None (need <= 3.0); total s = 570.0 (need >= 600.0) |
| S16 | THAM KHẢO | DX-S3, RUBRIC H4 (sổ gu G-008) | FAIL | share tied to a character or scenario = 0.0 (need >= 0.75) |
| R01 | THAM KHẢO | DX-R1 | MISSING | artifact missing: out/tension-map.json |
| R02 | THAM KHẢO | DX-R2 | MISSING | artifact missing: out/cues.json |
| R03 | THAM KHẢO | DX-R3 | FAIL | decisive claims = 0 (need >= 1); shortest pause s = None (need >= 1.0) |
| R04 | THAM KHẢO | DX-R4 | MISSING | artifact missing: out/transitions.json |
| R05 | THAM KHẢO | DX-R5 | FAIL | shots > 12 s = 8 (need <= 0); shot length CV = 0.374802 (need >= 0.4); act-2 scenes before climax = 0 (need >= 6) |
| R06 | THAM KHẢO | DX-V10 (picture check of cuts) | MISSING | artifact missing: out/transitions.json |
| V01 | THAM KHẢO | DX-V12 | MISSING | artifact missing: preprod/shotlist.json |
| V02 | THAM KHẢO | DX-V1 | MISSING | artifact missing: out/checks/page.json |
| V03 | CHÍNH | DX-V3 | MISSING | artifact missing: out/checks/page.json |
| V04 | THAM KHẢO | DX-V4, DX-X3 | MISSING | artifact missing: design/tokens.json colour token "ink" (contract characters.dana.color) |
| V05 | THAM KHẢO | DX-V8 | MISSING | artifact missing: out/camera.json |
| V08 | CHÍNH | DX-V6 | MISSING | artifact missing: out/checks/page.json |
| V09 | CHÍNH | DX-V4, DX-X3 | MISSING | artifact missing: design/tokens.json colour token "ink" (contract characters.dana.color) |
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
| C11 | THAM KHẢO | DX-V11 (C rule layout-repeat) | PASS |  |
| C12 | THAM KHẢO | DX-V11 (C rule split-view) | MISSING | artifact missing: out/checks/page.json |
| C13 | THAM KHẢO | DX-V11 (number–voice sync ±250 ms) | MISSING | artifact missing: out/checks/page.json |
| C14 | CHÍNH | DX-V11, DX-X4 (legible at 25%) | MISSING | artifact missing: out/checks/page.json |
| C15 | THAM KHẢO | DX-V5 (C rule tokens only) | MISSING | artifact missing: out/checks/page.json |
| P01 | THAM KHẢO | DX-P2 | MISSING | artifact missing: design/tokens.json |
| T1 | THAM KHẢO | DX-A1 (sổ gu G-001, G-006) | MISSING | artifact missing: contract.json: sonification.bandsHz |
| T2 | THAM KHẢO | DX-A2 (sổ gu G-002) | FAIL | repeated phrases (%) = 57.575758 (need <= 5.0); longest run of repeated phrases = 6 (need <= 1) |
| T3 | THAM KHẢO | DX-R6 (sổ gu G-003) | FAIL | silences measured = 0 (need >= 1) |
| L1 | CHÍNH | DX-A1, DX-A9 (sổ gu G-006) | PASS |  |
| REG | CHẶN | CH §5, §4 khâu 3 (cổng hồi quy) | PASS | first version: nothing to compare |
