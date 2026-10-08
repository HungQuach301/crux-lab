# checks/ report

root: `/home/user/crux-lab/episodes/ep005`  
lock: `d93276a491dd366c08ea0464d8de23bca80d82082a0c7be66ea2d555fd366b4a`  
master SHA-256: `None`  
{'PASS': 3, 'FAIL': 1, 'MISSING': 85, 'ERROR': 0}

**Tập: TRƯỢT** (chỉ luật CHẶN làm trượt tập; luật CHÍNH không đạt cần bên dựng giải thích; luật THAM KHẢO chỉ báo số đo)

| cấp | luật | đạt | không đạt |
|---|---|---|---|
| CHẶN | 35 | 3 | F01 MISSING, F02 MISSING, F03 MISSING, F04 MISSING, F05 MISSING, F06 MISSING, F08 MISSING, F09 MISSING, F10 MISSING, F11 FAIL, F12 MISSING, A01 MISSING, A02 MISSING, A04 MISSING, A05 MISSING, A06 MISSING, A14 MISSING, S02 MISSING, S05 MISSING, S06 MISSING, S07 MISSING, S08 MISSING, S09 MISSING, S10 MISSING, S17 MISSING, SH01 MISSING, SH02 MISSING, SH03 MISSING, SH04 MISSING, SH05 MISSING, C07 MISSING, REG MISSING |
| CHÍNH | 11 | 0 | F07 MISSING, A18 MISSING, V03 MISSING, V08 MISSING, V09 MISSING, V11 MISSING, V12 MISSING, C02 MISSING, C05 MISSING, C14 MISSING, L1 MISSING |
| THAM KHẢO | 43 | 0 | A03 MISSING, A07 MISSING, A08 MISSING, A09 MISSING, A10 MISSING, A11 MISSING, A12 MISSING, A13 MISSING, A15 MISSING, A16 MISSING, A17 MISSING, S11 MISSING, S12 MISSING, S13 MISSING, S14 MISSING, S15 MISSING, S16 MISSING, S18 MISSING, R01 MISSING, R02 MISSING, R03 MISSING, R04 MISSING, R05 MISSING, R06 MISSING, V01 MISSING, V02 MISSING, V04 MISSING, V05 MISSING, V10 MISSING, V13 MISSING, C01 MISSING, C03 MISSING, C04 MISSING, C06 MISSING, C10 MISSING, C11 MISSING, C12 MISSING, C13 MISSING, C15 MISSING, P01 MISSING, T1 MISSING, T2 MISSING, T3 MISSING |

CHÍNH không đạt, chưa có giải thích trong `out/explanations.json`: F07, A18, V03, V08, V09, V11, V12, C02, C05, C14, L1

## Chỉ số trong ±5% quanh ngưỡng

- S04 (CHẶN) · mortgage30 tolerance = 0.5 (ngưỡng <= 0.5, đạt)
- S04 (CHẶN) · hpi_mom tolerance = 0.5 (ngưỡng <= 0.5, đạt)

| rule | tier | § | status | failing metrics |
|---|---|---|---|---|
| F01 | CHẶN | DX-F1, DX-F2 | MISSING | artifact missing: out/video.mp4 |
| F02 | CHẶN | DX-F1 | MISSING | artifact missing: out/video.mp4 |
| F03 | CHẶN | DX-F3 | MISSING | artifact missing: out/video.mp4 |
| F04 | CHẶN | DX-F2 | MISSING | artifact missing: out/video.mp4 |
| F05 | CHẶN | DX-F2 | MISSING | artifact missing: out/video.mp4 |
| F06 | CHẶN | DX-F4 | MISSING | artifact missing: out/video.mp4 |
| F07 | CHÍNH | DX-S1 (CH §1 length) | MISSING | artifact missing: out/video.mp4 |
| F08 | CHẶN | DX-V5 | MISSING | artifact missing: out/video.mp4 |
| F09 | CHẶN | DX-F5 | MISSING | artifact missing: out/captions.srt |
| F10 | CHẶN | DX-F6 | MISSING | artifact missing: out/package/description.md |
| F11 | CHẶN | CH §4 khâu 3 (hợp đồng tập, K2) | FAIL | declared artefacts not delivered = 30 (need <= 0) |
| F12 | CHẶN | DX-A3 (sổ giấy phép), CH §5 (K3: quyền tài sản; K3.1: tài sản hình) | MISSING | artifact missing: out/rights.json |
| A01 | CHẶN | DX-A10 | MISSING | artifact missing: out/video.mp4 |
| A02 | CHẶN | DX-A10 | MISSING | artifact missing: out/video.mp4 |
| A03 | THAM KHẢO | DX-A10 | MISSING | artifact missing: out/video.mp4 |
| A04 | CHẶN | DX-A10 | MISSING | artifact missing: out/video.mp4 |
| A05 | CHẶN | DX-A10 | MISSING | artifact missing: out/video.mp4 |
| A06 | CHẶN | DX-A10, DX-X5 | MISSING | artifact missing: out/video.mp4 |
| A07 | THAM KHẢO | DX-A9 | MISSING | artifact missing: out/audio/stems/voice.wav|flac |
| A08 | THAM KHẢO | DX-A9 | MISSING | artifact missing: out/audio/stems/music.wav|flac |
| A09 | THAM KHẢO | DX-R6 | MISSING | artifact missing: out/video.mp4 |
| A10 | THAM KHẢO | DX-A5 | MISSING | artifact missing: out/camera.json |
| A11 | THAM KHẢO | DX-A5 | MISSING | artifact missing: out/sfx-events.json |
| A12 | THAM KHẢO | DX-A3 | MISSING | artifact missing: out/tempo-map.json |
| A13 | THAM KHẢO | DX-A7 | MISSING | artifact missing: out/voice/takes.json |
| A14 | CHẶN | DX-A7 | MISSING | artifact missing: out/script.json |
| A15 | THAM KHẢO | DX-A7 | MISSING | artifact missing: out/script.json |
| A16 | THAM KHẢO | DX-A7 (K3, cảnh báo) | MISSING | artifact missing: out/script.json |
| A17 | THAM KHẢO | DX-A7, DX-R6 (K3, cảnh báo) | MISSING | artifact missing: out/script.json |
| A18 | CHÍNH | DX-A8 (K3, cảnh báo) | MISSING | artifact missing: out/voice/takes.json |
| S01 | CHẶN | DX-H1 | PASS |  |
| S02 | CHẶN | DX-H1 | MISSING | artifact missing: out/timeline.json |
| S03 | CHẶN | DX-H4 | PASS |  |
| S04 | CHẶN | DX-H5 | PASS |  |
| S05 | CHẶN | DX-H1, DX-H2 | MISSING | artifact missing: out/claims.json |
| S06 | CHẶN | DX-H6 | MISSING | artifact missing: out/checks/page.json |
| S07 | CHẶN | DX-H1, DX-H2 | MISSING | artifact missing: out/claims.json |
| S08 | CHẶN | DX-H2 | MISSING | artifact missing: out/checks/page.json |
| S09 | CHẶN | DX-H3 | MISSING | artifact missing: out/claims.json |
| S10 | CHẶN | DX-I1, DX-I2 | MISSING | artifact missing: out/script.json |
| S11 | THAM KHẢO | DX-S6 | MISSING | artifact missing: out/claims.json |
| S12 | THAM KHẢO | DX-S7 | MISSING | artifact missing: out/checks/page.json |
| S13 | THAM KHẢO | DX-S8 (sổ gu G-009) | MISSING | artifact missing: out/script.json |
| S14 | THAM KHẢO | DX-S10 | MISSING | artifact missing: out/adbreaks.json |
| S15 | THAM KHẢO | DX-S1 | MISSING | artifact missing: out/timeline.json |
| S16 | THAM KHẢO | DX-S3, RUBRIC H4 (sổ gu G-008) | MISSING | artifact missing: out/claims.json |
| S17 | CHẶN | DX-H2 (claim), checks-appeal A1 | MISSING | artifact missing: out/claims.json |
| S18 | THAM KHẢO | DX-S3, DX-S4 (story.md §1), checks-appeal A2 | MISSING | artifact missing: out/script.json |
| SH01 | CHẶN | D-006 Q3, checks-appeal A5 | MISSING | artifact missing: contract.json: shorts = [{file}] |
| SH02 | CHẶN | D-006 Q3, checks-appeal A5 | MISSING | artifact missing: contract.json: shorts = [{file}] |
| SH03 | CHẶN | DX-A10, checks-appeal A5 | MISSING | artifact missing: contract.json: shorts = [{file}] |
| SH04 | CHẶN | DX-A10, checks-appeal A5 | MISSING | artifact missing: contract.json: shorts = [{file}] |
| SH05 | CHẶN | DX-I1, DX-I2 (CHARTER §4 protected genes), checks-appeal A5 | MISSING | artifact missing: contract.json: shorts = [{file}] |
| R01 | THAM KHẢO | DX-R1 | MISSING | artifact missing: out/tension-map.json |
| R02 | THAM KHẢO | DX-R2 | MISSING | artifact missing: out/timeline.json |
| R03 | THAM KHẢO | DX-R3 | MISSING | artifact missing: out/claims.json |
| R04 | THAM KHẢO | DX-R4 | MISSING | artifact missing: out/transitions.json |
| R05 | THAM KHẢO | DX-R5 | MISSING | artifact missing: out/timeline.json |
| R06 | THAM KHẢO | DX-V10 (picture check of cuts) | MISSING | artifact missing: out/transitions.json |
| V01 | THAM KHẢO | DX-V12 | MISSING | artifact missing: preprod/shotlist.json |
| V02 | THAM KHẢO | DX-V1 | MISSING | artifact missing: out/checks/page.json |
| V03 | CHÍNH | DX-V3 | MISSING | artifact missing: out/checks/page.json |
| V04 | THAM KHẢO | DX-V4, DX-X3 | MISSING | artifact missing: contract.json: characters.owen.color |
| V05 | THAM KHẢO | DX-V8 | MISSING | artifact missing: out/camera.json |
| V08 | CHÍNH | DX-V6 | MISSING | artifact missing: out/checks/page.json |
| V09 | CHÍNH | DX-V4, DX-X3 | MISSING | artifact missing: contract.json: characters.owen.color |
| V10 | THAM KHẢO | DX-V10 | MISSING | artifact missing: out/transitions.json |
| V11 | CHÍNH | DX-V11 (C rule text-line-collision, upgraded to pixels) | MISSING | artifact missing: out/checks/page.json |
| V12 | CHÍNH | DX-V9 (replaces the camera-move exemption) | MISSING | artifact missing: out/checks/page.json |
| V13 | THAM KHẢO | DX-V9, DX-V8 (replaces the camera-move exemption) | MISSING | artifact missing: out/timeline.json |
| C01 | THAM KHẢO | DX-V11 (C rule scene-leak) | MISSING | artifact missing: out/checks/page.json |
| C02 | CHÍNH | DX-V11 (C rule bg-over-data) | MISSING | artifact missing: out/checks/page.json |
| C03 | THAM KHẢO | DX-V11 (C rule unlabelled-curve) | MISSING | artifact missing: out/checks/page.json |
| C04 | THAM KHẢO | DX-V11 (C rule axis-anchors) | MISSING | artifact missing: out/checks/page.json |
| C05 | CHÍNH | DX-V11, DX-X4 (C rule grey-emphasis) | MISSING | artifact missing: out/checks/page.json |
| C06 | THAM KHẢO | DX-V11 (C rule number-colour) | MISSING | artifact missing: out/checks/page.json |
| C07 | CHẶN | DX-V11 (C rule bar-proportion) | MISSING | artifact missing: out/checks/page.json |
| C10 | THAM KHẢO | DX-V1 (C rule level1) | MISSING | artifact missing: out/checks/page.json |
| C11 | THAM KHẢO | DX-V11 (C rule layout-repeat) | MISSING | artifact missing: out/timeline.json |
| C12 | THAM KHẢO | DX-V11 (C rule split-view) | MISSING | artifact missing: out/checks/page.json |
| C13 | THAM KHẢO | DX-V11 (number–voice sync ±250 ms) | MISSING | artifact missing: out/checks/page.json |
| C14 | CHÍNH | DX-V11, DX-X4 (legible at 25%) | MISSING | artifact missing: out/checks/page.json |
| C15 | THAM KHẢO | DX-V5 (C rule tokens only) | MISSING | artifact missing: out/checks/page.json |
| P01 | THAM KHẢO | DX-P2 | MISSING | artifact missing: design/tokens.json |
| T1 | THAM KHẢO | DX-A1 (sổ gu G-001, G-006) | MISSING | artifact missing: contract.json: sonification.bandsHz |
| T2 | THAM KHẢO | DX-A2 (sổ gu G-002) | MISSING | artifact missing: out/tempo-map.json |
| T3 | THAM KHẢO | DX-R6 (sổ gu G-003) | MISSING | artifact missing: out/video.mp4 |
| L1 | CHÍNH | DX-A1, DX-A9 (sổ gu G-006) | MISSING | artifact missing: out/audio/stems/sonify.wav|flac |
| REG | CHẶN | CH §5, §4 khâu 3 (cổng hồi quy) | MISSING | no baseline report (--baseline <previous report.json>) and not declared --first |
