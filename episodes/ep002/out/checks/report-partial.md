# checks/ report

root: `/home/user/crux-lab/episodes/ep002`  
lock: `2fcc9fcc9a94b73084c43ba59970d88f539cd29363334faf52b0640efc2cc801`  
master SHA-256: `fdfa3d47d6ee1069a23b30d52a4044fa2f9209e1b9a0c02852e059170e2480a4`  
{'PASS': 13, 'FAIL': 4, 'MISSING': 0, 'ERROR': 0}

**Tập: ĐẠT** (chỉ luật CHẶN làm trượt tập; luật CHÍNH không đạt cần bên dựng giải thích; luật THAM KHẢO chỉ báo số đo)

| cấp | luật | đạt | không đạt |
|---|---|---|---|
| CHẶN | 6 | 6 | — |
| CHÍNH | 2 | 2 | — |
| THAM KHẢO | 9 | 5 | A03 FAIL, A08 FAIL, T2 FAIL, T3 FAIL |

## Chỉ số trong ±5% quanh ngưỡng

- A12 (THAM KHẢO) · accents on a cut (%) = 100.0 (ngưỡng >= 100.0, đạt)
- A18 (CHÍNH) · distinct voices (provider, voiceId, model) = 1 (ngưỡng <= 1, đạt)
- S14 (THAM KHẢO) · ad breaks = 2 (ngưỡng in [2, 3], đạt)

| rule | tier | § | status | failing metrics |
|---|---|---|---|---|
| A01 | CHẶN | DX-A10 | PASS |  |
| A02 | CHẶN | DX-A10 | PASS |  |
| A03 | THAM KHẢO | DX-A10 | FAIL | LRA LU = 3.1 (need in [6.0, 10.0]) |
| A04 | CHẶN | DX-A10 | PASS |  |
| A05 | CHẶN | DX-A10 | PASS |  |
| A06 | CHẶN | DX-A10, DX-X5 | PASS |  |
| A07 | THAM KHẢO | DX-A9 | PASS |  |
| A08 | THAM KHẢO | DX-A9 | FAIL | median 1-4 kHz drop dB = 4.366425 (need >= 6.0) |
| A09 | THAM KHẢO | DX-R6 | PASS |  |
| A12 | THAM KHẢO | DX-A3 | PASS |  |
| A13 | THAM KHẢO | DX-A7 | PASS |  |
| A14 | CHẶN | DX-A7 | PASS |  |
| A18 | CHÍNH | DX-A8 (K3, cảnh báo) | PASS |  |
| S14 | THAM KHẢO | DX-S10 | PASS |  |
| T2 | THAM KHẢO | DX-A2 (sổ gu G-002) | FAIL | repeated phrases (%) = 19.71831 (need <= 5.0); longest run of repeated phrases = 3 (need <= 1) |
| T3 | THAM KHẢO | DX-R6 (sổ gu G-003) | FAIL | entries outside 150–400 ms = 2 (need <= 0) |
| L1 | CHÍNH | DX-A1, DX-A9 (sổ gu G-006) | PASS |  |
