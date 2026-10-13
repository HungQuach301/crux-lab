# G2 — trả lời của chủ dự án (Tập 7) · 2026-10-13 (lệnh mở P4)

Gói: `gates/G2.md` (REVIEWER `gates/REVIEW-G2.md`). Nguyên văn:

> 1 PHÁT HÀNH bản hiện tại (chủ dự án xem full-720p 13/10, duyệt). Không sửa hình/lời thêm. Chấp nhận có ý thức: cổng gốc 5–7/21 (phần lớn nhiễu người chấm — so khung C4/C5: B11, B13, B19, B29 gần trùng hình), S21 lớp trả thêm, S25 must_beat, B23 câu khuyên, A14 (ASR small.en, A34) — tất cả chuyển sang tổng kết Tập 7 / Tập 8. S25 giữ. · 2 T2 · 3 duyệt SH1, SH2 · L3: chủ dự án duyệt phát hành

| Mục | Quyết định |
|---|---|
| Phát hành | **CÓ — bản hiện tại** (chủ dự án xem `review-g2/full-720p.mp4` 13/10, duyệt) |
| Sửa thêm | **Không sửa hình/lời** (không hoàn 10 cảnh, không sửa "her" ×2, không sửa S25.4) |
| Chấp nhận có ý thức (D-009 ngoại lệ, chủ dự án ghi lý do) | cổng gốc 5–7/21 (phần lớn nhiễu người chấm — khung C4/C5 B11, B13, B19, B29 gần trùng hình); S21 lớp trả thêm; S25 `must_beat`; B23 câu khuyên; A14 (ASR small.en, khiếu nại A34) → **tổng kết Tập 7 / Tập 8** |
| S25 | **giữ** |
| Tiêu đề | **T2** — *30-Year Mortgage Paid Off in 15 Years: What It Really Costs* |
| Shorts | **duyệt SH1, SH2** (SH3 đã bỏ 13/10) |
| Phiếu L3 | **chủ dự án duyệt phát hành** — không chấm số từng dòng; ghi đúng như vậy, không tự điền số |

Hệ quả cho P4:
- Bản cuối không đổi hình/lời → master 1080p dựng lại theo `episode.yaml` đúng như bản G2 (container P3 mất `out/video.mp4`), không thay đổi gì.
- A14 còn CHẶN theo luật khoá (`dc4981b3`) — **chủ dự án chấp nhận**, A34 chờ lô K Tập 8. Bộ lấy mẫu trang (luật V/C) chạy trên bản 1080p; chỉ CHẶN MỚI (không phải A14) mới dừng hỏi.
- Gói phát hành: brief ChatGPT (`packaging.md` §7) → kiểm đầu ra → giao hàng → G3 (chủ dự án đăng).
