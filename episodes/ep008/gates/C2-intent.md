# C2 — Ý đồ kiểm mù lời (ghi TRƯỚC khi chạy; không sửa sau khi thấy kết quả) · 2026-10-13

Mẫu: `c2/sample.txt` = lời C2 v1 (sau khi thêm S04.3b, bộ kiểm ĐẠT), 1.411 từ, dựng máy từ `story/script.md` (bỏ mã, vai, thẻ cảm xúc, chú thích). Giao thức `episode.md` §2 + §1b.4: **6 người đọc headless Sonnet** khoá Console (`blind.py`), **5 T** (vai = người hỏi câu hỏi trọng số cao nhất của hồ sơ cầu: người thuê 2026 đủ 20 % cọc, "thuê có đắt hơn mua khi tính đủ") + **1 G**; 1 người chấm headless độc lập, nhãn ngẫu nhiên (`c2/rubric.md`). Câu hỏi: `c2/spec.json` (thêm câu 7 phụ K4.1, câu 8 §1b.4). Tập 8 không phải lượt model khác (Tập 6, 9, 12).
- **Kiểm máy trước (đã chạy):** `check_script.py` ĐẠT (claim, S10, US only, history-not-forecast, M1–M6, mật độ, khuôn ±5 nêu tên); **danh sách từ dễ đọc thành lời khuyên** (luật tạm 13/10): `c2/advice-words.json` — lời: chỉ "wasted" ở S01 (câu hỏi của Nina) và S32 (câu phủ định của cô) — đúng luật.
- **Ngưỡng (quality-framework §4 C2):** đúng ≥ 5/6; `advice_stated` 0/6; không loại khối nào bị ≥ 2/6 nêu mất chú ý (episode.md §2: theo loại khối). **Dừng:** gặp `advice_stated` đầu tiên hoặc 2 sai (chạy song song cả 6, ghi nếu dừng sớm sẽ đổi gì).
- **Trượt → vòng 2** (≤ 2 vòng; luật tạm: mỗi lỗi ≤ 2 vòng cả tập): WRITER MỚI, đầu bài ngắn (cảnh + lý do); khối mất chú ý → rút còn 1 câu + thẻ + mô tả. Vẫn trượt → giữ bản điểm cao nhất, nêu ở G1 trước/sau.
- Dự kiến 7 lượt (≈ $0,4).

**Vòng 2 (ghi trước khi chạy):** mẫu `c2/sample-r2.txt` (C2 v2: S26–S28 rút còn 2 câu/1 số nói, số Census + điểm lật lên hình; S05.6, S31 = 1 câu + thẻ V7; S32.3 viết lại; S04.4 bỏ "6 percent" nói → nhãn hình B04). Cùng spec/câu hỏi/rubric/ngưỡng, **6 người đọc mới**, người chấm mới. Đây là vòng cuối (≤ 2): trượt → giữ bản điểm cao hơn, G1 nêu trước/sau.
