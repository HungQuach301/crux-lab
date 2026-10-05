# Hướng dẫn đăng — Tập 3

Theo quyết định C6 của chủ dự án (2026-10-05, issue [#34](https://github.com/HungQuach301/crux-lab/issues/34)): **phát hành nguyên trạng**.

## File
- Video: `ep003-youtube.mp4` (ghép từ 3 phần trên nhánh tạm `ep003-delivery`, lệnh trong `JOIN.md`). SHA-256 phải là `1274f9f6f5df6d03bb29923e07e4ea8858a9eb226d533cbfe0a7635dc1424070`. Bản này mã hoá từ bản gốc `103ff99e…`.
- Tiêu đề: **A1** "Money You Won't Touch for 20 Years: Savings Bond or T-Bills?"
- Mô tả và chương: `episodes/ep003/out/package/description.md`. Dán nguyên văn; các chương dạng `m:ss Tiêu đề` bắt đầu từ 0:00.
- Phụ đề: `episodes/ep003/out/captions.srt` (tiếng Anh).
- Thumbnail: **T1** (`out/package/thumb-1.png`) làm mặc định. **Test & Compare: T1, T2, T3** (`thumb-1..3.png`).
- Kết quả Test & Compare và số đo YouTube ghi vào `episodes/ep003/audience.md`.

## Trước khi bấm đăng: lãi EE (claim `ctx_ee_rate`)
- **Ngày đăng trước 1/11/2026:** giữ nguyên. Lời (S02.4), hình (BOND) và mô tả đều ghi "2.40% … for bonds issued May to October 2026".
- **Ngày đăng từ 1/11/2026 trở đi:** **cập nhật claim theo thông báo mới của TreasuryDirect trước khi đăng.** Đọc lãi cố định của EE cho bond phát hành tháng 11/2026 – tháng 4/2027 trên TreasuryDirect, rồi làm các việc sau:
  1. Ghi lãi mới, nguồn và ngày đọc vào `numbers.md` (claim `ctx_ee_rate`) và `out/claims.json`.
  2. Sửa đoạn "The bond as of October 2026…" trong `out/package/description.md`. Giữ câu về đợt May–October 2026, thêm một câu: lãi cho bond phát hành November 2026 – April 2027 là X%.
  3. Lời và hình **không phải sửa**. Chúng nói đúng về bond phát hành May–October 2026, và kết quả lịch sử không đổi.
  4. Ghi một dòng vào `ledger.md`.

## Giữ nguyên (đã quyết ở C6)
Hai lỗi CHÍNH đã giải thích trong `out/explanations.json`:
- **V11:** nhãn đối trọng ở cảnh 17 tháng chạm đầu vạch ×2.
- **C05:** số 52.3% màu warn.

## Sau khi đăng
- Ghi link video và ngày đăng vào `episodes/ep003/audience.md`.
- Theo dõi Test & Compare (T1/T2/T3).
- Đưa ý "móc mở đầu" vào tổng kết tập (lessons F1, Mốc B).
