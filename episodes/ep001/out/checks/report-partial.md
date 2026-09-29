# checks/ report

root: `/home/user/crux-lab/episodes/ep001`  
lock: `f9e24c91a464b1948f6eabb08d6da05d5867f78d2fe7ce1f818ec92009f0dcdd`  
master SHA-256: `None`  
{'PASS': 9, 'FAIL': 2, 'MISSING': 12, 'ERROR': 0}

| rule | § | status | failing metrics |
|---|---|---|---|
| F11 | CH §4 khâu 3 (hợp đồng tập, K2) | FAIL | declared artefacts not delivered = 23 (need <= 0) |
| A13 | DX-A7 | PASS |  |
| A15 | DX-A7 | MISSING | artifact missing: out/video.mp4 |
| S01 | DX-H1 | PASS |  |
| S03 | DX-H4 | PASS |  |
| S04 | DX-H5 | PASS |  |
| S05 | DX-H1, DX-H2 | PASS |  |
| S06 | DX-H6 | MISSING | artifact missing: out/checks/page.json |
| S07 | DX-H1, DX-H2 | MISSING | artifact missing: out/checks/page.json |
| S08 | DX-H2 | MISSING | artifact missing: out/checks/page.json |
| S09 | DX-H3 | MISSING | artifact missing: out/checks/page.json |
| S10 | DX-I1, DX-I2 | PASS |  |
| S11 | DX-S6 | MISSING | artifact missing: out/checks/page.json |
| S12 | DX-S7 | MISSING | artifact missing: out/checks/page.json |
| S13 | DX-S8 (sổ gu G-009) | PASS |  |
| S14 | DX-S10 | MISSING | artifact missing: out/video.mp4 |
| S15 | DX-S1 | FAIL | cold open s = 21.94 (need <= 15.0) |
| S16 | DX-S3, RUBRIC H4 (sổ gu G-008) | PASS |  |
| R02 | DX-R2 | PASS |  |
| V04 | DX-V4, DX-X3 | MISSING | artifact missing: out/checks/page.json |
| V09 | DX-V4, DX-X3 | MISSING | artifact missing: out/checks/page.json |
| T1 | DX-A1 (sổ gu G-001, G-006) | MISSING | artifact missing: out/sonify-events.json or out/checks/page.json chartEvents |
| L1 | DX-A1, DX-A9 (sổ gu G-006) | MISSING | artifact missing: out/audio/stems/sonify.wav|flac |

## Metrics within 5% of a threshold

- S03 files = 2 (threshold >= 2)
- S04 series pairs = 1 (threshold >= 1)
- S04 mortgage30 tolerance = 0.5 (threshold <= 0.5)
- S15 ident s = 3.0 (threshold <= 3.0)
