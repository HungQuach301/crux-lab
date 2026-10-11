# C4 — cổng gốc tắt tiếng (A) — P3b 09/10

Ý đồ `gates/C4-intent.md` A + D. Dữ liệu `c4/root-r1/` (46 lượt, KEY/packet/rubric-key commit trước khi chấm, 2 người chấm, `classes.json` SHA-256 trong bảng). Dải `review-c4/strips/` từ animatic 720p @ 0af1076.

| Bộ | Mẫu | Loại | Điểm theo thứ tự đọc | Đúng | Câu khuyên | Kết quả |
|---|---|---|---|---|---|---|
| ep006 | B01 | image | 0.5 · 0.5 | 0/2 | 1 | FAIL |
| ep006 | B03 | image | 0.5 · 0.5 | 0/2 | 0 | FAIL |
| ep006 | B04 | image | 1 · 0.5 | 0/2 | 2 | FAIL |
| ep006 | B06 | image | 1 · 1 | 1/2 | 1 | FAIL |
| ep006 | B07 | image | 1 · 1 | 1/2 | 1 | FAIL |
| ep006 | B08 | image | 1 · 1 | 0/2 | 2 | FAIL |
| ep006 | B09 | image | 1 · 1 | 1/2 | 1 | FAIL |
| ep006 | B10 | image | 1 · 1 | 1/2 | 1 | FAIL |
| ep006 | B12 | image | 0.5 · 1 | 0/2 | 1 | FAIL |
| ep006 | B13 | image | 1 · 1 | 2/2 | 0 | PASS |
| ep006 | B14 | image | 1 · 1 | 0/2 | 2 | FAIL |
| ep006 | B15 | image | 0.5 · 0.5 | 0/2 | 0 | FAIL |
| ep006 | B16 | image | 1 · 1 | 2/2 | 0 | PASS |
| ep006 | B17 | image | 1 · 1 | 2/2 | 0 | PASS |
| ep006 | B19 | image | 1 · 1 | 1/2 | 1 | FAIL |
| ep006 | B21 | image | 1 · 1 | 0/2 | 2 | FAIL |
| ep006 | B22 | image | 1 · 1 | 0/2 | 2 | FAIL |
| ep006 | B24 | image | 1 · 1 | 1/2 | 1 | FAIL |
| ep006 | B25 | image | 1 · 1 | 0/2 | 2 | FAIL |
| ep006 | B27 | image | 1 · 1 | 1/2 | 1 | FAIL |
| ep006 | B29 | image | 1 · 1 | 1/2 | 1 | FAIL |
| ep006 | B30 | image | 1 · 1 | 0/2 | 2 | FAIL |
| ep006 | B32 | image | 0.5 · 0.5 | 0/2 | 0 | FAIL |

**Cổng (ep006, nhịp loại image): 3/23 = 13%; ngưỡng 80%; câu khuyên ở B01, B04, B06, B07, B08, B09, B10, B12, B14, B19, B21, B22, B24, B25, B27, B29, B30 → FAIL.**
Rubric khuyên: cổng theo `old` · cũ FAIL · mới PENDING · **hai rubric lệch → giữ rubric cũ** · 2 người chấm.
Bảng phân loại `classes.json` SHA-256 `0d91af0b353f…`, loại 1 = 77%.

## Đọc kết quả
- **Rubric cũ (cổng):** 3/23 = 13 % → **TRƯỢT**; cờ khuyên ở 17 nhịp. Gần như toàn bộ là `advice_inferred` (người đọc tự suy, câu 5 "own" 45/46): *"inflation is worth weighing when choosing between a level payout and a rising payout"*, *"an inflation-adjusted payout deserves a look"*. Vai T của ý đồ ("looking at an income annuity quote that offers two payout options") mời đúng loại suy luận này ở mọi nhịp.
- **Rubric mới (`advice_stated`):** 1 nhịp — **B08** (một người chấm bật S cho *"A viewer would likely take away that inflation protection matters over a long retirement"*, người đọc ghi "own"; người chấm kia ghi I). Còn lại 0.
- **Nghĩa riêng (bỏ cờ khuyên):** 2/2 đúng ở 17 nhịp (B06, B07, B08, B09, B10, B13, B14, B16, B17, B19, B21, B22, B24, B25, B27, B29, B30); chia ở B04, B12 (cần người thứ 3); 0/2 ở **B01, B03, B15, B32** (0,5 · 0,5 — nghĩa một phần) → sửa bằng hình.
- Ngoại lệ S29 (C3): B29 nghĩa 1 · 1, cờ khuyên I/C → theo ngoại lệ, chỉ xét nghĩa: ĐẠT nghĩa.
- **Lệch hai rubric → giữ rubric cũ (K4.1 câu 3) → cổng C4 TRƯỢT theo luật ghi trước.** Rubric cũ trên nội dung này không phân biệt hình tốt/xấu (17/23 nhịp, cả nhịp loại 1 đã duyệt C3 S07/S24/S27 khuyên 0/2 ở C3 với cùng vai) — xem `checks-appeal.md`.
