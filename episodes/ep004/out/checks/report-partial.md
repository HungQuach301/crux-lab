# checks/ report

root: `/home/user/crux-lab/episodes/ep004`  
lock: `250ab298de4f912d34fdd02474aaa1af843ea9115e36fd0675630fcdcd1641de`  
master SHA-256: `839a96671e8fc3ca0a3565eb07e126780d2adcc6406d84d1c2660b8243b78b06`  
{'PASS': 0, 'FAIL': 2, 'MISSING': 0, 'ERROR': 0}

**Tập: TRƯỢT** (chỉ luật CHẶN làm trượt tập; luật CHÍNH không đạt cần bên dựng giải thích; luật THAM KHẢO chỉ báo số đo)

| cấp | luật | đạt | không đạt |
|---|---|---|---|
| CHẶN | 1 | 0 | F11 FAIL |
| CHÍNH | 0 | 0 | — |
| THAM KHẢO | 1 | 0 | P01 FAIL |

## Chỉ số trong ±5% quanh ngưỡng

- P01 (THAM KHẢO) · thumb 1 token share (%) = 100.0 (ngưỡng >= 97.0, đạt)
- P01 (THAM KHẢO) · thumb 2 token share (%) = 99.986328 (ngưỡng >= 97.0, đạt)
- P01 (THAM KHẢO) · thumb 3 token share (%) = 99.99924 (ngưỡng >= 97.0, đạt)

| rule | tier | § | status | failing metrics |
|---|---|---|---|---|
| F11 | CHẶN | CH §4 khâu 3 (hợp đồng tập, K2) | FAIL | declared artefacts not delivered = 1 (need <= 0); release files not declared = 14 (need <= 0) |
| P01 | THAM KHẢO | DX-P2 | FAIL | thumb 1 min contrast at 10% = 2.241864 (need >= 3.0); thumb 2 min contrast at 10% = 2.241864 (need >= 3.0); thumb 3 min contrast at 10% = 2.230069 (need >= 3.0); thumb texts below 90 px = 18 (need <= 0) |
