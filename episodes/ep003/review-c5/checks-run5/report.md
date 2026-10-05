# checks/ report

root: `/tmp/claude-0/-home-user-crux-lab/51de23e7-5129-5f5e-bb96-d4b3c7fc7c4b/scratchpad/lc9/episodes/ep003`  
lock: `a20c6878c0dc1c1e9320db4553c92144ed4a9c46cd69ad4c20c9899696483791`  
master SHA-256: `103ff99ef637984f2438d7c46f6e604735fae096c57f123cd9ba4c6d5904cf27`  
{'PASS': 50, 'FAIL': 31, 'MISSING': 1, 'ERROR': 0}

**Tập: ĐẠT** (chỉ luật CHẶN làm trượt tập; luật CHÍNH không đạt cần bên dựng giải thích; luật THAM KHẢO chỉ báo số đo)

| cấp | luật | đạt | không đạt |
|---|---|---|---|
| CHẶN | 29 | 29 | — |
| CHÍNH | 11 | 9 | V11 FAIL, C05 FAIL |
| THAM KHẢO | 42 | 12 | A03 FAIL, A09 FAIL, A10 FAIL, A11 FAIL, A12 FAIL, A13 MISSING, A15 FAIL, A16 FAIL, A17 FAIL, S11 FAIL, S12 FAIL, S14 FAIL, S15 FAIL, S16 FAIL, R01 FAIL, R02 FAIL, R03 FAIL, R04 FAIL, R05 FAIL, R06 FAIL, V01 FAIL, V02 FAIL, V05 FAIL, V10 FAIL, C10 FAIL, C12 FAIL, C13 FAIL, T1 FAIL, T2 FAIL, T3 FAIL |

## Chỉ số trong ±5% quanh ngưỡng

- A18 (CHÍNH) · distinct voices (provider, voiceId, model) = 1 (ngưỡng <= 1, đạt)
- S04 (CHẶN) · series pairs = 1 (ngưỡng >= 1, đạt)
- S06 (CHẶN) · coverage statements = 1 (ngưỡng >= 1, đạt)
- S06 (CHẶN) · case values shown in act2 = 873 (ngưỡng >= 873, đạt)
- S15 (THAM KHẢO) · total s = 572.0 (ngưỡng >= 600.0, không đạt)
- V09 (CHÍNH) · declared characters seen on screen = 1 (ngưỡng >= 1, đạt)
- P01 (THAM KHẢO) · thumb 1 token share (%) = 100.0 (ngưỡng >= 97.0, đạt)
- P01 (THAM KHẢO) · thumb 2 token share (%) = 100.0 (ngưỡng >= 97.0, đạt)
- P01 (THAM KHẢO) · thumb 3 token share (%) = 99.196403 (ngưỡng >= 97.0, đạt)

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
| A03 | THAM KHẢO | DX-A10 | FAIL | LRA LU = 3.5 (need in [6.0, 10.0]) |
| A04 | CHẶN | DX-A10 | PASS |  |
| A05 | CHẶN | DX-A10 | PASS |  |
| A06 | CHẶN | DX-A10, DX-X5 | PASS |  |
| A07 | THAM KHẢO | DX-A9 | PASS |  |
| A08 | THAM KHẢO | DX-A9 | PASS |  |
| A09 | THAM KHẢO | DX-R6 | FAIL | silences 0.8-1.5 s = 0 (need >= 3) |
| A10 | THAM KHẢO | DX-A5 | FAIL | camera moves = 0 (need >= 5) |
| A11 | THAM KHẢO | DX-A5 | FAIL | events measured = 0 (need >= 8); Pearson pan~x = None (need >= 0.7) |
| A12 | THAM KHẢO | DX-A3 | FAIL | accents on a cut (%) = 0.0 (need >= 100.0) |
| A13 | THAM KHẢO | DX-A7 | MISSING | artifact missing: S01.0e27330e.seed1.mp3 |
| A14 | CHẶN | DX-A7 | PASS |  |
| A15 | THAM KHẢO | DX-A7 | FAIL | wpm act cold-open = 168.302945 (need in [150.0, 160.0]); wpm act act1 = 172.302464 (need in [150.0, 160.0]); wpm act act2 = 170.685036 (need in [150.0, 160.0]); wpm act act3 = 173.620458 (need in [150.0, 160.0]); wpm act method = 180.327869 (need in [150.0, 160.0]); wpm act outro = 176.740627 (need in [150.0, 160.0]); sentences > 175 wpm = 32 (need <= 0) |
| A16 | THAM KHẢO | DX-A7 (K3, cảnh báo) | FAIL | fake break marks = 11 (need <= 0); sentences with a fake break = 11 (need <= 0) |
| A17 | THAM KHẢO | DX-A7, DX-R6 (K3, cảnh báo) | FAIL | abnormal sentences share = 0.132353 (need <= 0.1) |
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
| S11 | THAM KHẢO | DX-S6 | FAIL | core claims = 0 (need >= 1) |
| S12 | THAM KHẢO | DX-S7 | FAIL | max new numbers in a scene = 12 (need <= 2) |
| S13 | THAM KHẢO | DX-S8 (sổ gu G-009) | PASS |  |
| S14 | THAM KHẢO | DX-S10 | FAIL | ad breaks = 0 (need in [2, 3]) |
| S15 | THAM KHẢO | DX-S1 | FAIL | act order = ['cold-open', 'act1', 'act2', 'act3', 'method', 'outro'] (need == ['cold-open', 'ident', 'act1', 'act2', 'act3', 'method', 'outro']); cold open s = 64.457 (need <= 15.0); ident s = None (need <= 3.0); total s = 572.0 (need >= 600.0) |
| S16 | THAM KHẢO | DX-S3, RUBRIC H4 (sổ gu G-008) | FAIL | share tied to a character or scenario = 0.0 (need >= 0.75) |
| R01 | THAM KHẢO | DX-R1 | FAIL | acts with climax peak = 0 (need >= 3) |
| R02 | THAM KHẢO | DX-R2 | FAIL | longest stretch without a break s = 140.131 (need <= 60.0) |
| R03 | THAM KHẢO | DX-R3 | FAIL | decisive claims = 0 (need >= 1); shortest pause s = None (need >= 1.0) |
| R04 | THAM KHẢO | DX-R4 | FAIL | cuts on beat/action (%) = 8.333333 (need >= 70.0) |
| R05 | THAM KHẢO | DX-R5 | FAIL | shots > 12 s = 8 (need <= 0); shot length CV = 0.375891 (need >= 0.4); act-2 scenes before climax = 0 (need >= 6) |
| R06 | THAM KHẢO | DX-V10 (picture check of cuts) | FAIL | cuts visible in picture (%) = 50.0 (need >= 90.0) |
| V01 | THAM KHẢO | DX-V12 | FAIL | storyboard present = False (need == True); colour script present = False (need == True) |
| V02 | THAM KHẢO | DX-V1 | FAIL | level-1 placed (%) = 0.0 (need >= 90.0) |
| V03 | CHÍNH | DX-V3 | PASS |  |
| V04 | THAM KHẢO | DX-V4, DX-X3 | PASS |  |
| V05 | THAM KHẢO | DX-V8 | FAIL | camera moves = 0 (need >= 5); worst ease ratio = None (need <= 0.4); anticipation in moves ≥1 s (%) = None (need >= 30.0); overshoot in moves ≥1 s (%) = None (need >= 30.0); peak |a| fw/s² = None (need <= 8.0); camera~picture Spearman = nan (need >= 0.3) |
| V08 | CHÍNH | DX-V6 | PASS |  |
| V09 | CHÍNH | DX-V4, DX-X3 | PASS |  |
| V10 | THAM KHẢO | DX-V10 | FAIL | verified match cuts = 1 (need >= 5); verified J/L cuts = 0 (need >= 4) |
| V11 | CHÍNH | DX-V11 (C rule text-line-collision, upgraded to pixels) | FAIL | text collisions = 131 (need <= 0) |
| V12 | CHÍNH | DX-V9 (replaces the camera-move exemption) | PASS |  |
| V13 | THAM KHẢO | DX-V9, DX-V8 (replaces the camera-move exemption) | PASS |  |
| C01 | THAM KHẢO | DX-V11 (C rule scene-leak) | PASS |  |
| C02 | CHÍNH | DX-V11 (C rule bg-over-data) | PASS |  |
| C03 | THAM KHẢO | DX-V11 (C rule unlabelled-curve) | PASS |  |
| C04 | THAM KHẢO | DX-V11 (C rule axis-anchors) | PASS |  |
| C05 | CHÍNH | DX-V11, DX-X4 (C rule grey-emphasis) | FAIL | frames flagged = 80 (need <= 0) |
| C06 | THAM KHẢO | DX-V11 (C rule number-colour) | PASS |  |
| C07 | CHẶN | DX-V11 (C rule bar-proportion) | PASS |  |
| C10 | THAM KHẢO | DX-V1 (C rule level1) | FAIL | scenes failing = 10 (need <= 0) |
| C11 | THAM KHẢO | DX-V11 (C rule layout-repeat) | PASS |  |
| C12 | THAM KHẢO | DX-V11 (C rule split-view) | FAIL | split-view runs = 5 (need <= 0) |
| C13 | THAM KHẢO | DX-V11 (number–voice sync ±250 ms) | FAIL | worst |offset| ms = 54690 (need <= 250.0); pairs > 250 ms = 35 (need <= 0) |
| C14 | CHÍNH | DX-V11, DX-X4 (legible at 25%) | PASS |  |
| C15 | THAM KHẢO | DX-V5 (C rule tokens only) | PASS |  |
| P01 | THAM KHẢO | DX-P2 | PASS |  |
| T1 | THAM KHẢO | DX-A1 (sổ gu G-001, G-006) | FAIL | share of slots heard in a pause = 0.0 (need >= 0.6); declared bands share of data-stem energy = 0.0 (need >= 0.5) |
| T2 | THAM KHẢO | DX-A2 (sổ gu G-002) | FAIL | repeated phrases (%) = 59.090909 (need <= 5.0); longest run of repeated phrases = 5 (need <= 1) |
| T3 | THAM KHẢO | DX-R6 (sổ gu G-003) | FAIL | silences measured = 0 (need >= 1) |
| L1 | CHÍNH | DX-A1, DX-A9 (sổ gu G-006) | PASS |  |
| REG | CHẶN | CH §5, §4 khâu 3 (cổng hồi quy) | PASS |  |
