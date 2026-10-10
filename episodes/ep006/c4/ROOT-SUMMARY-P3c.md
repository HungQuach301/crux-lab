# Cổng gốc C4 Tập 6 — kết quả sau P3c (rubric MỚI, `gates/C4-answer.md`; 2 người chấm, gộp thận trọng)

| Nhịp | Vòng 0 (root-r1, dải trước sửa) | Vòng 2 (root-r2, sau sửa 1) | Vòng 3 (root-r3, sau sửa 2) | Vòng 4 (root-r4, sau sửa 3) | Kết |
|---|---|---|---|---|---|
| B01 | 0,5 · 0,5 | 0,5 · 0,5 | 0,5 · 0,5 | 0,5 · 0,5 | **TRƯỢT nghĩa — hết 3 vòng → G2 nêu trước/sau** |
| B03 | 0,5 · 0,5 | 1 · 0,5 · 1 (3 người) | — | — | ĐẠT |
| B04 | 1 · 0,5 | 0,5 · 0,5 | 0,5 · 0,5 | **1 · 1** | ĐẠT |
| B08 | 1 · 1 (khuyên cũ) | 1 · 1 | — | — | ĐẠT |
| B12 | 0,5 · 1 | 0,5 · 0,5 | 0,5 · 1 · 0,5 | **1 · 1** | ĐẠT |
| B15 | 0,5 · 0,5 | 0,5 · 0,5 | 0,5 · 0,5 | 0,5 · 0,5 | **TRƯỢT nghĩa — hết 3 vòng → G2 nêu trước/sau** |
| B32 | 0,5 · 0,5 | **1 · 1** | 1 · 0,5 · 0 (séc ngang + bước nấc) | — | ĐẠT — đoạn f trả về bản vòng 2 (khoá nghĩa) |

17 nhịp còn lại ĐẠT ở vòng 0 (B06 B07 B08 B09 B10 B13 B14 B16 B17 B19 B21 B22 B24 B25 B27 B29 B30). **Cổng: 21/23 = 91,3 % ≥ 80 % → ĐẠT; `advice_stated` = 0 ở mọi lượt đọc** (rubric cũ báo song song: mọi nhịp có cờ `advice_inferred`, người đọc tự nói "my own conclusion").
B01 (người chấm vòng 4): "check growth noted, but dimming to 9 lit crates not clearly stated" — người đọc nắm nghịch lý (séc lớn, thùng mờ), hụt chi tiết "9 thùng sáng". B15: "gets the early cluster and 'none since', but misreads as inflation story / misses warn region". Dải: `review-c4/strips/` (nay) · `review-c4/r1`, `r2`, `r3` (trước).
