# Cổng Mốc 3 — báo cáo (phần hợp lệ; phần thắng/thua chờ mã chấm)

Thẩm quyền: `decisions/D-002.md`. Thiết kế đã duyệt: `DESIGN.md`. Đóng băng: `FREEZE.md` (`c84715b`) trước mọi kiểm.

## Hợp lệ bằng máy: **19/20** (ngưỡng D-002: ≥ 15/20 → ĐẠT)

Cửa sổ ±5 % quanh ngưỡng là 14,25–15,75 (tức đúng 15/20); 19 nằm ngoài cửa sổ.

| id | V1 dữ liệu tải lại | SHA khớp | V2 calc.py | V3 tính lại độc lập | V4 nguồn + điều khoản | V5 điều luật | lệch V3 lớn nhất | hợp lệ |
|---|---|---|---|---|---|---|---|---|
| debt-1 | đạt | có | đạt | đạt | đạt | đạt | 0.0 % | CÓ |
| debt-2 | đạt | có | đạt | đạt | đạt | đạt | 0.0 % | CÓ |
| debt-3 | đạt | có | đạt | đạt | đạt | đạt | 0.0 % | CÓ |
| debt-4 | đạt | có | đạt | đạt | đạt | đạt | 0.0 % | CÓ |
| debt-5 | đạt | có | đạt | đạt | đạt | đạt | 0.0 % | CÓ |
| debt-6 | đạt | có | đạt | đạt | đạt | đạt | 0.0 % | CÓ |
| debt-7 | đạt | có | đạt | đạt | đạt | đạt | 0.0 % | CÓ |
| retire-1 | đạt | có | đạt | đạt | đạt | đạt | 0.014 % | CÓ |
| retire-2 | đạt | có | đạt | đạt | **trượt** | đạt | 0.064 % | **KHÔNG** |
| retire-3 | đạt | có | đạt | đạt | đạt | đạt | 0.008 % | CÓ |
| retire-4 | đạt | có | đạt | đạt | đạt | đạt | 0.212 % | CÓ |
| retire-5 | đạt | có | đạt | đạt | đạt | đạt | 0.178 % | CÓ |
| retire-6 | đạt | có | đạt | đạt | đạt | đạt | 0.379 % | CÓ |
| retire-7 | đạt | có | đạt | đạt | đạt | đạt | 0.107 % | CÓ |
| tax-1 | đạt | có | đạt | đạt | đạt | đạt | 0.0 % | CÓ |
| tax-2 | đạt | có | đạt | đạt | đạt | đạt | 0.158 % | CÓ |
| tax-3 | đạt | có | đạt | đạt | đạt | đạt | 0.16 % | CÓ |
| tax-4 | đạt | có | đạt | đạt | đạt | đạt | 0.009 % | CÓ |
| tax-5 | đạt | có | đạt | đạt | đạt | đạt | 0.16 % | CÓ |
| tax-6 | đạt | có | đạt | đạt | đạt | đạt | 0.08 % | CÓ |

- **retire-2 không hợp lệ:** `series[0].terms.quote` rỗng; câu bản quyền được ghi ở trường khác (`copyrightQuote`) nên V4 không tìm thấy câu trích. Lỗi định dạng hồ sơ, theo luật khoá là trượt; không sửa sau khi thấy kết quả.
- **Số lệch trong dung sai (0,5 %), nêu tên:** tax-2 (trần CPI 10 731 so với 10 748 tính lại, 0,16 %), tax-3 (0,16 %), tax-5 (0,16 %). Cùng một nguyên nhân: FRED thiếu CPI tháng 10/2025; bên sinh lấy "12 giá trị gần nhất có mặt" (8/2025–8/2026), người tính lại lấy 11 giá trị trong cửa sổ 9/2025–8/2026 đúng chữ định nghĩa. Kết luận của luận điểm không đổi.
- **Sự cố hạ tầng (không đổi luật):** (1) proxy ngắt kết nối khi `verify.py` gửi User-Agent tự đặt → đổi sang UA mặc định, chạy lại từ đầu; chưa có kết quả nào trước khi sửa. (2) Agent V3 của tax-3 không tải được FRED → điều phối tải hai chuỗi theo URL ghim, agent tự hoàn tất mã của mình.
- **Kiểm mới lạ (báo cáo, không tính vào hợp lệ):** 20 luận điểm máy: 2 `not-found` (debt-7, retire-7), 18 `partly-said`; không cái nào `already-said` (bên sinh đã bỏ 17 ý bị `already-said` trong lúc sinh).

## Đối chứng
GPT-5.5 (`gpt-5.5-2026-04-23`), effort medium, không công cụ, không dữ liệu; 3 lệnh gọi, 25–28 s mỗi trụ (trần 10 phút), 20/20 thẻ đạt khuôn ngay lần đầu.

## So mù
Chờ mã chấm của chủ dự án. Key khoá SHA-256 `d479f9ac40b3e576d76b6eaa4f9d5c4f91ae564b92dd704ff84d5c29672448fa`.
