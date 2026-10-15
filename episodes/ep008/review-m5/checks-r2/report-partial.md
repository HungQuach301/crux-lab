# checks/ report

root: `/home/user/chk-ep008/episodes/ep008`  
lock: `a35970a866c5d9cd11b9dd7dcbf374e908259c7b16f64dc99b0de39d0b954fd8`  
master SHA-256: `4149bd41a3d6100819e209f87f7b89facc979c34d51674aca24240047232babf`  
{'PASS': 0, 'FAIL': 2, 'MISSING': 0, 'ERROR': 0}

**Tập: TRƯỢT** (chỉ luật CHẶN làm trượt tập; luật CHÍNH không đạt cần bên dựng giải thích; luật THAM KHẢO chỉ báo số đo)

| cấp | luật | đạt | không đạt | lỗi thật | pháp lý | thủ tục |
|---|---|---|---|---|---|---|
| CHẶN | 1 | 0 | A14 FAIL | A14 | — | — |
| CHÍNH | 1 | 0 | L1 FAIL | L1 | — | — |
| THAM KHẢO | 0 | 0 | — | — | — | — |

CHÍNH không đạt, chưa có giải thích trong `out/explanations.json`: L1

## Chỉ số trong ±5% quanh ngưỡng

không có

| rule | tier | § | status | loại (A40) | failing metrics |
|---|---|---|---|---|---|
| A14 | CHẶN | DX-A7 | FAIL | lỗi thật | key words missing = 3 (need <= 0) |
| L1 | CHÍNH | DX-A1, DX-A9 (sổ gu G-006) | FAIL | lỗi thật | voice/data 1–4 kHz ratio, 10th percentile (dB) = 15.103469 (need >= 20.0) |
