# C3 — cổng gốc 3 hình mới · kết quả

Ý đồ: `gates/C3-root-intent.md`. Dữ liệu `c3/root/` (vòng 1). Headless có ảnh: 6 lượt 70.080 token (≈ 11,7 nghìn/lượt) + người chấm 13.886.

## Vòng 1
| Hình | Nghĩa | Khuyên_tính (A9) | Kết luận | Câu khuyên |
|---|---|---|---|---|
| N1 lịch trả góp (B06) | 2/2 | **2/2** | **TRƯỢT** | "stay in the home long enough for the principal paydown to speed up"; "extra payments made early…" |
| N3 gập đường → cột (B10) | 2/2 | 0/2 | **ĐẠT** | (thận trọng chung: chừa ngân sách) |
| N2 cột + đuôi chậm (B13) | 2/2 | **2/2** | **TRƯỢT** | "plan to stay put for many years to ride out a downturn" |

Hướng sửa (vòng 2, **bằng hình trước**, D-009 E6): xem `gates/C3-root-r2.md` khi có.

## Vòng 2 (sửa bằng hình: `world/c3/FIX-R2.md`; người đọc mới `c3/root-r2/`)
| Hình | Nghĩa | Khuyên_tính | Kết luận |
|---|---|---|---|
| N1 | 3/3 | **3/3** (sau người đọc thứ 3; chấm lại cả bộ: người chấm mới đổi người đọc 1 từ "không" sang "khuyên" — người chấm dao động, ghi nhận) | **TRƯỢT** — "plan to stay a long time", "extra principal payments early" |
| N2 | 2/2 | **2/2** | **TRƯỢT** — "only buy if you can stay in the home", "don't try to time the market" |
Token: người đọc 46.575 + 11.524, người chấm 10.623 + 11.646. Khoá nghĩa: nghĩa giữ 1/1 ở mọi lượt; vòng 2 không tốt hơn vòng 1 về khuyên (bằng nhau) → vòng 3 sửa tiếp từ bản vòng 2 (cùng hạng, bản mới hơn sửa đúng nguyên nhân hình đã chẩn đoán).

## Cold open (E5k port + sửa lỗi "slowest case" hiện sớm) — kiểm lại E1/E2
Rubric nguyên văn Mốc V (`moc-v/eval/ROOT-intent-ep005.json`), dải từ `review-c3/c3-clip.mp4` (E1 11,3–24,6 s; E2 24,8–34,6 s = mốc Mốc V + 1 s thẻ tiêu đề), `c3/coldopen/`. **E1 2/2 · E2 2/2 · khuyên 0/4 → ĐẠT.** Token 47.735 + 10.038.

## Vòng 3 — cuối (`world/c3/FIX-R3.md`; người đọc mới `c3/root-r3/`, người thứ 3 N1 `c3/root-r3x/` chấm riêng)
Trước khi chạy: mô tả đáp án N2 "turn warn" → "are set apart in their own colour" (màu đổi theo tiền lệ D-010 §6, nghĩa không đổi; ghi trong `spans.json`).
| Hình | Nghĩa | Khuyên_tính | Kết luận |
|---|---|---|---|
| N1 | 3/3 | 2/3 (1 người đọc chỉ thận trọng chung) | **TRƯỢT** (đúng 1/3 < 2/3) — tốt nhất trong 3 vòng |
| N2 | 2/2 | 2/2 | **TRƯỢT** — "plan to stay in the home for a long time" |
Token: người đọc 46.797 + 11.668, người chấm 11.133 + 6.147.

## Tổng 3 vòng (luật 3 vòng, episode.md v4 → chủ dự án chọn)
| Hình | Vòng 1 đúng | Vòng 2 | Vòng 3 | Bản tốt nhất (khoá nghĩa) |
|---|---|---|---|---|
| N1 lịch | 0/2 | 0/3 | **1/3** | vòng 3 |
| N2 cột | 0/2 | 0/2 | 0/2 | hoà → vòng 3 (màu trung tính, tiền lệ D-010) |
| N3 gập | **2/2** | — | — | vòng 1 |
Nghĩa 1/1 ở mọi lượt (19/19). Câu khuyên cùng một dạng ở cả 3 vòng: "ở lâu trong nhà / trả thêm gốc sớm" (N1), "chỉ mua nếu ở được lâu" (N2) — do **chính nội dung** (khấu hao chậm rồi nhanh; ca chậm 2005–2009) khi xem **tắt tiếng**; bản có lời (kiểm mù C2 v2, S03→S12) 0/6 và 0/6 khuyên.
