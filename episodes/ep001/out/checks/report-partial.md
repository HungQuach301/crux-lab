# checks/ report

root: `/home/user/crux-lab/episodes/ep001`  
lock: `f9e24c91a464b1948f6eabb08d6da05d5867f78d2fe7ce1f818ec92009f0dcdd`  
master SHA-256: `None`  
{'PASS': 4, 'FAIL': 1, 'MISSING': 6, 'ERROR': 0}

| rule | § | status | failing metrics |
|---|---|---|---|
| F11 | CH §4 khâu 3 (hợp đồng tập, K2) | FAIL | declared artefacts not delivered = 27 (need <= 0) |
| S01 | DX-H1 | PASS |  |
| S03 | DX-H4 | PASS |  |
| S04 | DX-H5 | PASS |  |
| S05 | DX-H1, DX-H2 | PASS |  |
| S06 | DX-H6 | MISSING | artifact missing: out/checks/page.json |
| S16 | DX-S3, RUBRIC H4 (sổ gu G-008) | MISSING | artifact missing: out/script.json |
| V04 | DX-V4, DX-X3 | MISSING | artifact missing: out/checks/page.json |
| V09 | DX-V4, DX-X3 | MISSING | artifact missing: out/checks/page.json |
| T1 | DX-A1 (sổ gu G-001, G-006) | MISSING | artifact missing: out/sonify-events.json or out/checks/page.json chartEvents |
| L1 | DX-A1, DX-A9 (sổ gu G-006) | MISSING | artifact missing: out/audio/stems/sonify.wav|flac |

## Metrics within 5% of a threshold

- S03 files = 2 (threshold >= 2)
- S04 series pairs = 1 (threshold >= 1)
- S04 mortgage30 tolerance = 0.5 (threshold <= 0.5)
