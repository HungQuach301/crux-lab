# Hướng dẫn đăng — Tập 7

**ĐƯỢC ĐĂNG** — G2 duyệt 13/10/2026: phát hành bản hiện tại, không sửa hình/lời; L3: chủ dự án duyệt phát hành, không chấm số từng dòng (`gates/G2-answer.md`). Checks khoá `dc4981b3` trên master 1080p (`gates/P4-checks.md`): **Tập TRƯỢT theo luật, chủ dự án chấp nhận có ý thức** — A14 (ASR tên riêng, A34) ở G2; C07, S02, S07, S09 (luật trang, lần đầu đo) ở P4 13/10 → khiếu nại A35–A37, C07 vào tổng kết. F10, F11, S21, SH01–SH05 ĐẠT.

## Giao file (G3)
- **Nhánh tạm `ep007-delivery` @ `6d3cc32`, phần 90 MB** (như Tập 6; lessons T5-3).
- **Master 1080p giữ nguyên từng byte** (`deliver.py --skip-encode`, `c5/deliver.sh`): `ep007-youtube.mp4` = `out/video.mp4`, 1.313.723.079 byte, 10:06,7, −14,0 LUFS / −1,9 dBTP.
- **Đã kiểm ngược (13/10/2026):** tải lại cả 25 file từ link công khai dưới, ghép 15 phần, `sha256sum -c SHA256SUMS` → **24/24 OK**.

Tải thẳng (link công khai): [`SHA256SUMS`](https://github.com/HungQuach301/crux-lab/raw/ep007-delivery/SHA256SUMS) · [`JOIN.md`](https://github.com/HungQuach301/crux-lab/raw/ep007-delivery/JOIN.md) (lệnh ghép Windows/Mac)

| File | SHA-256 |
|---|---|
| `ep007-youtube.mp4` (ghép từ 15 phần dưới) | `529471f0f2283f4fd5b502c7d4e650f4e2e0b96e36ed33ba8c96a19e13a8d601` |
| [`ep007-youtube.mp4.part01`](https://github.com/HungQuach301/crux-lab/raw/ep007-delivery/ep007-youtube.mp4.part01) | `ac2e833bed15769508a6fd91f03b11ce34d5b962f11ad99bdd03eed4f598a998` |
| [`ep007-youtube.mp4.part02`](https://github.com/HungQuach301/crux-lab/raw/ep007-delivery/ep007-youtube.mp4.part02) | `b8a042a48b7221b9f80a93dc1ae70bf126760bcd759910d20c71678ce9909341` |
| [`ep007-youtube.mp4.part03`](https://github.com/HungQuach301/crux-lab/raw/ep007-delivery/ep007-youtube.mp4.part03) | `5d2483ce27e29f6cb780b0f43d96c7ed95829a48cd74ac89975e51c580fba550` |
| [`ep007-youtube.mp4.part04`](https://github.com/HungQuach301/crux-lab/raw/ep007-delivery/ep007-youtube.mp4.part04) | `05253a2e9a17d5acc57dbba8bd840994e8bb7e225f05fc74f1dc2bad10975ef2` |
| [`ep007-youtube.mp4.part05`](https://github.com/HungQuach301/crux-lab/raw/ep007-delivery/ep007-youtube.mp4.part05) | `290887fc0c0abbdbbf125e68b29f6a6a59e0f77129164cf46db6c5f794e24497` |
| [`ep007-youtube.mp4.part06`](https://github.com/HungQuach301/crux-lab/raw/ep007-delivery/ep007-youtube.mp4.part06) | `6a07ba01e851988913afa1190e649111e22fa9f80bf726f13cfd2add98523a8b` |
| [`ep007-youtube.mp4.part07`](https://github.com/HungQuach301/crux-lab/raw/ep007-delivery/ep007-youtube.mp4.part07) | `ce86bf0a42332215e05fd07f8cf9f256ea3d35302cd18a0c51c44e8947227c82` |
| [`ep007-youtube.mp4.part08`](https://github.com/HungQuach301/crux-lab/raw/ep007-delivery/ep007-youtube.mp4.part08) | `35437443720c852fe5a578d272778dbd2cfc9576dff2b58758586184e2f5af01` |
| [`ep007-youtube.mp4.part09`](https://github.com/HungQuach301/crux-lab/raw/ep007-delivery/ep007-youtube.mp4.part09) | `6505e05b22c39d771fff919d72cf9d2ce76dd0e12a3b69a801d7655352c3aa90` |
| [`ep007-youtube.mp4.part10`](https://github.com/HungQuach301/crux-lab/raw/ep007-delivery/ep007-youtube.mp4.part10) | `6cdbbabe6b6664fb8f4a11b92031c88986c3d039c8a1f128ed87203b542b2397` |
| [`ep007-youtube.mp4.part11`](https://github.com/HungQuach301/crux-lab/raw/ep007-delivery/ep007-youtube.mp4.part11) | `f8e0940fbf5ead0bc134453b134bb97b3283f9c34134ed8cafe7fd34b090e937` |
| [`ep007-youtube.mp4.part12`](https://github.com/HungQuach301/crux-lab/raw/ep007-delivery/ep007-youtube.mp4.part12) | `e6c96fc2507e32e1cc024285ddc23141fc559329ba8af1f486869b24755208b5` |
| [`ep007-youtube.mp4.part13`](https://github.com/HungQuach301/crux-lab/raw/ep007-delivery/ep007-youtube.mp4.part13) | `22da7b8bc34706a8d9e677197d77b056af1e29f8d00ff62d8862cd385e9aea97` |
| [`ep007-youtube.mp4.part14`](https://github.com/HungQuach301/crux-lab/raw/ep007-delivery/ep007-youtube.mp4.part14) | `29b4d17adcfbee1e7d7f7cce2d607bc33287fcfe43ee4354074d620b6ec96651` |
| [`ep007-youtube.mp4.part15`](https://github.com/HungQuach301/crux-lab/raw/ep007-delivery/ep007-youtube.mp4.part15) | `4f6b41b8908a8e6203ed58e31af7a756390d8c9c5db79a176f658eb66a11dc4d` |
| [`ep007-short-SH1.mp4`](https://github.com/HungQuach301/crux-lab/raw/ep007-delivery/ep007-short-SH1.mp4) | `9317125bc5e2cb1301076d3ed915d9271aab126b443182117f7d62b9cb4dfbf9` |
| [`ep007-short-SH2.mp4`](https://github.com/HungQuach301/crux-lab/raw/ep007-delivery/ep007-short-SH2.mp4) | `3a198219d7998e264818e3431d11e88bd690482d042e1f257e65398c598844a6` |
| [`ep007-thumb-1.png`](https://github.com/HungQuach301/crux-lab/raw/ep007-delivery/ep007-thumb-1.png) | `35273d77ecef29376042c0be8d9ab08084c3be92719b5bbcf979fe3187728072` |
| [`ep007-thumb-2.png`](https://github.com/HungQuach301/crux-lab/raw/ep007-delivery/ep007-thumb-2.png) | `674114608eb2ab073d8a9944179876c1ef3990f384c62659c253660cc9dfbaf4` |
| [`ep007-thumb-3.png`](https://github.com/HungQuach301/crux-lab/raw/ep007-delivery/ep007-thumb-3.png) | `d5a4ca4d70e5e0167e291dac16c81c5b2d35a2d33296cd889dc53a41e7293e59` |
| [`ep007-captions.srt`](https://github.com/HungQuach301/crux-lab/raw/ep007-delivery/ep007-captions.srt) | `1057f6d0455a4a7e3d304b9494510247abfd6e332fa7ae2ca3689747b58faee5` |
| [`ep007-description.md`](https://github.com/HungQuach301/crux-lab/raw/ep007-delivery/ep007-description.md) | `d3c7db00a1f1bc0fad716c095f3695effb8bb79769621b15a88f42daa030f882` |
| [`ep007-tags.txt`](https://github.com/HungQuach301/crux-lab/raw/ep007-delivery/ep007-tags.txt) | `40fcb21de3df9f6e4c0fdfeac4c4a50be097478b79f3b97b0f9c2c24178315e2` |

Ghép master: tải 15 file `ep007-youtube.mp4.partNN` + `SHA256SUMS` vào một thư mục → Mac/Linux `cat ep007-youtube.mp4.part* > ep007-youtube.mp4 && shasum -a 256 -c SHA256SUMS` · Windows `copy /b ep007-youtube.mp4.part01 + … + ep007-youtube.mp4.part15 ep007-youtube.mp4` rồi `certutil -hashfile ep007-youtube.mp4 SHA256` (đầy đủ trong `JOIN.md`). Mã phải là `529471f0…a8d601`.

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
