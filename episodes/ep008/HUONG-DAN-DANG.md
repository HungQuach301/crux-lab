# Hướng dẫn đăng — Tập 8

**ĐƯỢC ĐĂNG** — G3 15/10: đăng bản hiện tại (master `98833a2a…`), L1 18,5 dB chấp nhận là ngoại lệ của chủ dự án (`gates/G3-answer.md`). Sau khi đăng: chủ dự án báo → xoá `ep008-delivery`, gộp `ep008` vào `main` (squash).

## File (nhánh `ep008`; master không commit — giao theo câu trả lời G3)
| File | Chi tiết | SHA-256 |
|---|---|---|
| `out/video.mp4` (master 1080p, không commit) | 1920×1080, 606,0 s = 10:06, 1.312.607.135 byte, −14,0 LUFS / −2,2 dBTP | `98833a2a1f3fd8c882841aa0f86bdae3beb187dd042733feef6a51aefe89fb0e` |
| `out/shorts/SH1.mp4` | 1080×1920, 45,8 s, móc "The darkest house", thẻ cuối đối trọng | `d3771fccd80d3aed2fe67a89c15da89bdae876a21cd1d9999468b7a50d874863` |
| `out/captions.srt` | phụ đề tiếng Anh (bỏ thẻ cảm xúc) | `1cad7d4f83d39b5c0abef27cf638aec18406c64ce7afc58fcc53bd8fc98b4742` |
| `out/package/description.md` | mô tả + chương + `[METHOD AND SOURCES]` | `2d8d83e47d94e8431dc31d94bf2a0777bf4e65cc67daaa3758705349538aac81` |
| `out/package/tags.txt` | 5 tag | `7d8815d34525345ad467261577b5059c45e750b648870a969e99cdd889149070` |

## Giao file — nhánh tạm `ep008-delivery` @ `8c1ece7` (chủ dự án cho phép 15/10; xoá sau khi tải)
- 15 phần master `ep008-youtube.mp4.part01…part15` (90 MB, cắt byte — master giữ nguyên từng byte) + [`SHA256SUMS`](https://github.com/HungQuach301/crux-lab/raw/ep008-delivery/SHA256SUMS) + [`JOIN.md`](https://github.com/HungQuach301/crux-lab/raw/ep008-delivery/JOIN.md).
- [`ep008-short-SH1.mp4`](https://github.com/HungQuach301/crux-lab/raw/ep008-delivery/ep008-short-SH1.mp4) · [`ep008-captions.srt`](https://github.com/HungQuach301/crux-lab/raw/ep008-delivery/ep008-captions.srt) · [`ep008-description.md`](https://github.com/HungQuach301/crux-lab/raw/ep008-delivery/ep008-description.md) · [`ep008-tags.txt`](https://github.com/HungQuach301/crux-lab/raw/ep008-delivery/ep008-tags.txt).
- **Xem trước 720p ≈ 2,5 Mbps** (cùng nội dung master, 3 phần mở riêng được, mỗi phần ≈ 3:25): [`ep008-review-720p-1.mp4`](https://github.com/HungQuach301/crux-lab/raw/ep008-delivery/ep008-review-720p-1.mp4) · [`-2.mp4`](https://github.com/HungQuach301/crux-lab/raw/ep008-delivery/ep008-review-720p-2.mp4) · [`-3.mp4`](https://github.com/HungQuach301/crux-lab/raw/ep008-delivery/ep008-review-720p-3.mp4).
- **Đã kiểm (15/10):** 22/22 file khớp `SHA256SUMS`; ghép 15 phần → SHA-256 `98833a2a…` = `out/video.mp4`.
- Ghép: Mac/Linux `cat ep008-youtube.mp4.part* > ep008-youtube.mp4 && shasum -a 256 -c SHA256SUMS` · Windows `copy /b ep008-youtube.mp4.part01+…+ep008-youtube.mp4.part15 ep008-youtube.mp4` (xem `JOIN.md`).

## Điền trên YouTube Studio
- **Tiêu đề (G1 T1):** Rent vs Buy: Every Month Since 1991, Replayed
- **Mô tả:** dán nguyên `out/package/description.md` (có 6 dòng chương `m:ss` → YouTube tự tạo chương).
- **Tag:** rent vs buy · buying a home · renting a home · housing market history · mortgage rates
- **Phụ đề:** tải `out/captions.srt` (English).
- **Quảng cáo giữa video (mid-roll):** 2:54,7 (174,73 s) và 7:19,1 (439,07 s) — trong khoảng lặng sau câu cuối của S07 và S22; tắt tự đặt.
- **Thumbnail:** không giao (chủ dự án 13/10). Nếu muốn chọn khung thay vì để YouTube tự chọn — 3 khung 1080p đề nghị (`gates/G3-assets/`):
  1. 4:20,5 (`frame-260.5.png`) — lưới phố, dãy tối "2002 to 2007: 6 of 72";
  2. 5:56,5 (`frame-356.5.png`) — nhà tối nhất June 2006, hai chồng $115,374 / $197,760;
  3. 9:52,0 (`frame-592.0.png`) — Nina, "Is her rent money wasted?".
- **Short SH1:** đăng `out/shorts/SH1.mp4`; tiêu đề đề nghị "The darkest house"; mô tả: "Ten years after June 2006, the buyer was $82,385 behind the renter on the same street — the darkest of 307 start months. History, not a forecast. Full episode: Rent vs Buy: Every Month Since 1991, Replayed."
- **Khai báo:** nội dung có minh hoạ (nhân vật ILLUSTRATIVE), không quảng cáo sản phẩm; không phải lời khuyên tài chính (trên hình + mô tả).
