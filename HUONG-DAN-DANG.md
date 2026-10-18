# Hướng dẫn đăng — Tập 9

**CHỜ G3** — đăng sau khi chủ dự án trả lời `gates/G3.md`. Sau khi đăng: chủ dự án báo → xoá `ep009-delivery`, gộp nhánh tập vào `main` (squash).

## File (nhánh `ccr-4d8bc942-73gdnl`; master không commit — giao trên nhánh tạm)
| File | Chi tiết | SHA-256 |
|---|---|---|
| `out/video.mp4` (master 1080p) | 1920×1080, 511,3 s = 8:31, 1.107.472.954 byte, −14,0 LUFS / −2,2 dBTP (AAC) | `1a21c9e42d9fcc3fd5c4cbe78ee748b85963be91242cda5b1ac8afb3db12aa13` |
| `out/shorts/SH1.mp4` | 1080×1920, 29,8 s, móc "The pile that sank" | `5fb87bf3077b217423ab11e29c4bf470278f42321fefee92c1fc3df2636e65c0` |
| `out/captions.srt` | phụ đề tiếng Anh | `5d7deffb8859a248…` |
| `out/package/description.md` | mô tả + 6 chương + `[METHOD AND SOURCES]` + ghi công "Origami" | `ca0b881fe1c83256…` |
| `out/package/tags.txt` | 5 tag | `980eb87d87c5bd96…` |
| `out/package/thumbs/ep009-{1-aia,2-aib,3-aif}.jpg` | 3 ảnh bìa 1280×720 (packaging-r1, D-015) | `e54fd89a…` · `738812da…` · `dc944f06…` |

## Giao file — nhánh tạm `ep009-delivery` (xoá sau khi tải)
- 13 phần master `ep009-youtube.mp4.part01…part13` (90 MB, cắt byte — master giữ nguyên từng byte) + `SHA256SUMS` + `JOIN.md`.
- `ep009-short-SH1.mp4` · `ep009-captions.srt` · `ep009-description.md` · `ep009-tags.txt` · `ep009-1-aia.jpg` · `ep009-2-aib.jpg` · `ep009-3-aif.jpg` · bản này `HUONG-DAN-DANG.md`.
- **Xem trước 720p ≈ 2,5 Mbps** (cùng nội dung master, 3 phần mở riêng được, mỗi phần ≈ 2:50): `ep009-review-720p-1.mp4` · `-2.mp4` · `-3.mp4`.
- Ghép: Mac/Linux `cat ep009-youtube.mp4.part* > ep009-youtube.mp4 && shasum -a 256 ep009-youtube.mp4` → phải ra `1a21c9e4…aa13` · Windows: xem `JOIN.md`.

## Điền trên YouTube Studio
- **Tiêu đề (packaging-r1, D-015, 57 ký tự):** `Rent and Invest vs Buy: Renter Ahead in 155 of 307 Months`
- **Mô tả:** dán nguyên `ep009-description.md`. **Dòng 1** (điều kiện của con số trong tiêu đề, D-015):
  `With the renting twin's savings in the whole US stock market, the renter ended ten years ahead in 155 of 307 start months (January 1991 to July 2016); the buyer in the other 152 (49.5%). History, not a forecast. Over ten years, US stocks grew more than home prices about 9 times in 10, so why only about half?`
  Có 6 dòng chương `m:ss` (0:00 · 1:17 · 2:29 · 4:24 · 6:17 · 7:19) → YouTube tự tạo chương. Ghi công nhạc "Origami" (CC BY 4.0) nằm trong mô tả — **không xoá**.
- **Ảnh bìa → Test & Compare (thứ tự):** 1 `ep009-1-aia.jpg` (đồng xu, mặc định) · 2 `ep009-2-aib.jpg` (bập bênh nhà / khối) · 3 `ep009-3-aif.jpg` (nhà trên đế rộng). Cả ba ghi "COIN FLIP? 49.5%".
- **Tag:** rent vs buy · rent and invest the difference · buying a home · stock market history · housing market history
- **Phụ đề:** tải `ep009-captions.srt` (English).
- **Quảng cáo giữa video (mid-roll):** 2:28,9 (148,89 s) và 6:16,3 (376,3 s) — trong khoảng lặng sau câu cuối S06 và S18; tắt tự đặt.
- **Short SH1:** đăng `ep009-short-SH1.mp4`; tiêu đề đề nghị "The pile that sank"; mô tả: "With the renter's savings in US stocks, the pile dipped below where it started in 183 of 307 start months — and over ten years the buyer still ended ahead in about half. History, not a forecast. Full episode: Rent and Invest vs Buy: Renter Ahead in 155 of 307 Months."
- **Khai báo:** nội dung có minh hoạ (nhân vật ILLUSTRATIVE), không quảng cáo sản phẩm; không phải lời khuyên tài chính (trên hình + mô tả). Ảnh bìa: nền vẽ bằng OpenAI gpt-image-1 (D-015; sổ `packaging/r1/ai/ledger.jsonl` trên `packaging-r1`), chữ ghép bằng mã — nếu Studio hỏi "altered or synthetic content" thì chỉ áp cho video; ảnh bìa minh hoạ không phải người thật.
- **Content ID:** nhạc "Origami" — kiểm 0 claim ở G2 (17/10).
