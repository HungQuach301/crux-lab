# C4 Tập 7 — kết quả (P3, 11–12/10) · ý đồ `gates/C4-intent.md` (REVIEWER áp đủ trước lượt đọc đầu)

Animatic 720p cả tập 602,70 s (10:02,7), 7 đoạn thế giới verify OK, MR1 188,58 s / MR2 441,94 s (lặng 1,40 / 1,41 s), 33/33 take cache, EL 0 thêm.

## A. Cổng gốc tắt tiếng (21 nhịp loại 1; 2 người đọc + người thứ 3 khi lệch; 2 người chấm, gộp thận trọng)
| Nhịp | r1 (`c4/root-r1`, bản sửa vòng 2) | r2 (`c4/root-r2`, vòng 3) | r3 (`c4/root-r3`, vòng 4; B01/B09/B23 đọc theo ý ĐÃ HẠ) | Giữ |
|---|---|---|---|---|
| B01 | 0,5·0,5 TRƯỢT | 0,5·0,5 TRƯỢT | 0,5·1·0,5 TRƯỢT | trượt — "stack + $120 price seen" |
| B06 | ĐẠT | 1·0,5·1 ĐẠT | — | ĐẠT |
| B09 | 0,5·0,5 TRƯỢT | 1·0,5·0,5 TRƯỢT | 0,5·0,5 TRƯỢT | trượt — "gold gap seen, not tied to Tessa's stack" |
| B21 | **1·1** (extra 0/2) | 0,5·0,5 (cận cảnh — khoá nghĩa, loại) | 0,5·0,5 (về hình r1) | trượt — cùng hình r1 + r3: 2/4 |
| B23 | 0,5·0,5 TRƯỢT | 0,5·1·0,5 TRƯỢT | 0,5·0,5 TRƯỢT | trượt — "4 months later" đọc ra, cơ chế năm không |
| B25 | ĐẠT | 1·1 ĐẠT | — | ĐẠT |
| B31 | 1·0,5·0 TRƯỢT | — | 0·0 TRƯỢT | trượt — "no empty third slot described" |
| 15 nhịp còn lại | ĐẠT (r1) | — | — | ĐẠT |
**Cổng: 16/21 = 76,2 % < 80 % → TRƯỢT** (trong ±5 % quanh ngưỡng → nêu tên). Rubric mới `advice_stated` = 0 ở mọi nhịp, mọi vòng.
**Chốt C3 câu 1 (S21 lớp trả thêm thấy bằng hình, CHÍNH): TRƯỢT** — `extra_layer_seen` 0/2 ở cả ba vòng C4 (tấm sáng · tờ đô la trên ô · cận cảnh một ô); người đọc tả "tiles turn white/green". Cộng C3 r1–r3: 6 vòng, quá trần 3 (lessons V1) → G2 nêu trước/sau.

## B/C. Có lời
| Mẫu | r1 | r2 | Chốt |
|---|---|---|---|
| WHOLE (3) | stated 0 · must_beat 1/3 | stated 0 · must_beat 2/3 | stated 0 ĐẠT; "phải vượt" TRƯỢT |
| S21 (2) | nghĩa 0,5·0,5, stated 1 (một người chấm) | nghĩa 1·1, stated 0 | ĐẠT (extra chỉ báo) |
| S23–S24 (3) | stated 0/3 | stated 0/3 | **C3 câu 2 ĐẠT** — giữ nhịp Q3 |
| S25 (2) | must_beat 2/2 | must_beat 2/2 ("guaranteed return", "has to clear") | **C3 câu 5 TRƯỢT** |
Câu trích S25/WHOLE: *"The 7.40% works as a bar that any other use of the money has to clear"*; *"paying extra principal … has a guaranteed return equal to the loan's own rate"*. Nguồn: lời đã duyệt S25.4 "the bar any other use of that dollar gets measured against", S25.5 "Whether any investment **clears** it", S31.3 "**Clearing** the bar isn't the whole story" — hình đã bỏ mọi tín hiệu "so ngang/vượt" (bóng tách, không nét đứt, "not tested") mà 2/2 vẫn đọc ra → cần sửa lời (ngoại lệ phải hỏi, G2).

## Sửa đã làm (D-009: hình trước, nhãn cuối)
Vòng bố cục 1 (d F-2 CHẶN, a/b nhãn neo sai, cắt mép) · vòng 2 (S21 tờ đô la, S24 khay, f bỏ nét đứt ngang thanh) · vòng 3 (S21 cận cảnh, S23 xấp hạ ô 12/24/36, S01 4 bó, S06 một khung, S09 khối nhấc, S25 thước + đồng lãi + "not tested") · vòng 4 (S21 về v2 theo khoá nghĩa, S31 ô thứ ba) · B01/B09/B23 hạ ý cần đọc ra (beats.md, T6-7). Đầu bài: `briefs/builder-c4-*.md`.
