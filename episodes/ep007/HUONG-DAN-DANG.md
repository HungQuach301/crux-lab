# Hướng dẫn đăng — Tập 7

**ĐƯỢC ĐĂNG** — G2 duyệt 13/10/2026: phát hành bản hiện tại, không sửa hình/lời; L3: chủ dự án duyệt phát hành, không chấm số từng dòng (`gates/G2-answer.md`). Checks khoá `dc4981b3` trên master 1080p (`gates/P4-checks.md`): **Tập TRƯỢT theo luật, chủ dự án chấp nhận có ý thức** — A14 (ASR tên riêng, A34) ở G2; C07, S02, S07, S09 (luật trang, lần đầu đo) ở P4 13/10 → khiếu nại A35–A37, C07 vào tổng kết. F10, F11, S21, SH01–SH05 ĐẠT.

## Giao file (G3)
<<GIAO>>

## Đăng video chính
- **Tiêu đề:** **T2** "30-Year Mortgage Paid Off in 15 Years: What It Really Costs" (G1, 58 ký tự).
- **Mô tả và chương:** `ep007-description.md` — dán nguyên văn. 5 chương: 0:00 · 0:54 · 3:12 · 7:24 · 9:27 (khớp đầu hồi ±0,9 s). Khối "How we know this" có nguồn FRED (MORTGAGE30US, MORTGAGE15US; kiểm chéo OBMMIC30YF, OBMMIC15YF) đúng trích dẫn `data/sources.json`; cuối: "US only · history, not a forecast. Not advice …". Kiểm: `package_check.py` ĐẠT, F10/S21 ĐẠT, REVIEWER ĐẠT có sửa (đã áp, `gates/REVIEW-P4-package.md`).
- **Tag (5):** `ep007-tags.txt` — 30 year mortgage paid in 15 · 15 year vs 30 year mortgage · extra mortgage principal payment · pay off mortgage early · mortgage amortization schedule.
- **Phụ đề:** `ep007-captions.srt` (tiếng Anh, 130 cue).
- **Thumbnail (Claude dựng từ khung thế giới của phim, không chữ của cảnh; 1280×720; đọc được ở 168×94):**
  - **mặc định `ep007-thumb-1.png`** — the stack cạnh nhà Tessa + **"$120 A MONTH?"** (claim `extra_vs15_month_now`; mốc tuần dữ liệu ở dòng 1 mô tả);
  - `ep007-thumb-2.png` — the bar + **"THE BAR"** (không nêu 7,40 %);
  - `ep007-thumb-3.png` — hai cột + the stack + "$120 A MONTH?".
  - **Test & Compare:** 1, 2, 3. Cả ba có nhãn ILLUSTRATIVE và dòng "US only · history, not a forecast" (dòng này không đọc được ở cỡ điện thoại — mô tả đã có).
  - REVIEWER PHỤ (anh chọn): thumb-1 bóng nhà phủ nửa chồng tiền, ở 168×94 chồng đọc thành khối tối; thumb-3 hai ý trong một hình — đề xuất thumb-1 mặc định, thumb-2 để thử.
  - **Anh có thể thay bằng thumbnail ChatGPT sau khi đăng** (brief `out/package/PACKAGING-BRIEF.md` + 4 khung `frame-1..4.png`). Khi thay: chữ ≤ 4 từ lớn, số chỉ "$120 A MONTH?", có ILLUSTRATIVE cạnh nhân vật, không "guaranteed/beat/clear/earns", không 7,40 % ở phương án the bar. Gửi ảnh cho phiên nếu muốn kiểm.
- **Mid-roll: 2 mốc** `out/adbreaks.json`: **3:11 (191,3 s)** và **7:23 (443,44 s)** — đều ở ranh giới hồi có lặng, ≥ 120 s từ đầu/cuối, cách nhau 252 s. Tập 10:06,7 (`lab` 9–11 phút).

## Shorts (G2: duyệt SH1, SH2; SH3 bỏ)
Mỗi Short gắn link video chính (Related video). Tiêu đề đề xuất (anh sửa được; giữ: không khuyên, số có claim, ILLUSTRATIVE đã trên hình):
- `ep007-short-SH1.mp4` (35,9 s, S06–S07, móc "The price of a fallback"): *What a 30-year mortgage paid in 15 years really costs each month*
- `ep007-short-SH2.mp4` (33,3 s, S30, móc "Same plan, different week"): *Same mortgage plan, two different weeks: Leo vs Tessa*
Đo: 1080×1920, −13,8 / −13,9 LUFS, SH01–SH06 ĐẠT; SH2 cảnh báo F-2 (nhãn Leo giao nhau 3,7–8,9 s, không chặn). Trùng hình bản G2 (SSIM 1,000).

## Trước khi bấm đăng: claim có hạn dùng
- **Lãi tuần 8/10/2026** (15 năm 6,73 %, 30 năm 7,40 %; Tessa ILLUSTRATIVE; $120 a month, $21,622): lời, hình và mô tả đều ghi "the week of October 8, 2026" → là số lịch sử có ngày, **giữ nguyên** dù Freddie Mac công bố tuần mới (quyết định G1: không nói "this week").
- Không có claim "hiện tại" khác; dữ liệu FRED ghim `coed=2026-10-08` (SHA ở `data/sources.json`).

## Giữ nguyên (đã quyết ở G2 và P4)
- Cổng gốc tắt tiếng 5–7/21, S21 lớp trả thêm, S25 `must_beat` (giữ S25), B23 câu khuyên, A14 (A34) — chấp nhận ở G2 → tổng kết Tập 7 / Tập 8.
- C07 (cột S09 tràn khung), S02, S07, S09 — chấp nhận ở P4 (A35–A37; C07 → tổng kết).
- qc nhà máy 7 mục TRƯỢT cùng loại Tập 5–6 đã đăng (đối trọng master "0 khung log" ×4, freezedetect, true peak −1,9 dBTP).

## Sau khi đăng (G3)
- Ghi link video, ngày đăng vào `episodes/ep007/audience.md`.
- Báo phiên đã đăng và tải xong → phiên squash `ep007` vào `main` và ghi `TONGKET-INPUT.md`; xoá nhánh `ep007-delivery` (proxy chặn xoá → anh xoá: GitHub → Branches → Delete).
- Mốc 7 ngày: một ảnh chụp YouTube Studio cho chat chiến lược (`playbook/templates/audience.md`).
