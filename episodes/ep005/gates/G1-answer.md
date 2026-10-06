# G1 — trả lời của chủ dự án (Tập 5) · 2026-10-06

Nguyên văn: *"G1: 1 #17 L2 · 2 OK · 3 T1 · 75 %: (a) — nguyên văn Fannie Mae Servicing Guide B-8.1-04 (chat chiến lược đọc trực tiếp https://servicing-guide.fanniemae.com/svc/b-8.1-04/termination-conventional-mortgage-insurance) … Claim nói rõ đây là quy định của Fannie Mae (khoản vay Fannie Mae), không phải mọi khoản vay. Nhánh: đổi sang ep005 … NGUYÊN TẮC MỚI (chủ dự án): chất lượng là ưu tiên tuyệt đối — nội dung, hình, âm không bao giờ được hy sinh vì tốc độ/chi phí. TẠM DỪNG trước khi dựng hình: chủ dự án mở Mốc V … Được làm tiếp phần không phụ thuộc hình: dữ liệu, lời theo cảnh (take vào voice-takes/). Kịch bản sẽ được chuyển sang đặc tả nhịp mới của Mốc V. Ghi PLAN rồi DỪNG chờ Mốc V merge."*

| Câu | Quyết định |
|---|---|
| 1 | Đề tài **#17 debt-2**, logline **L2** |
| 2 | Kịch bản + cold open **H-A** OK |
| 3 | Tiêu đề nháp **T1** "10% Down and Mortgage Insurance: How Long Did It Last?"; không C3 |
| 75 % | **(a)**: nguyên văn B-8.1-04 do chủ dự án cung cấp → `data/sources.json` (provisions), claim `value_removal_ltv_early`, `value_removal_seasoning_years` ghi rõ **quy định của Fannie Mae, chỉ khoản vay Fannie Mae** |
| Nhánh | `ep005` (đẩy toàn bộ từ `ccr-a4da2518-3guqrl` @ `906f8be`; từ nay commit lên `ep005`) |
| Nguyên tắc | **Chất lượng là ưu tiên tuyệt đối** — nội dung, hình, âm không hy sinh vì tốc độ/chi phí (`decisions/D-009.md`) |
| Tiến độ | **TẠM DỪNG trước dựng hình** cho tới khi **Mốc V** merge; được làm dữ liệu + lời theo cảnh; kịch bản sẽ chuyển sang đặc tả nhịp Mốc V |

## Áp dụng
- Sources/claim: xong (check_script ĐẠT, statements 17/17).
- **Hỏi lại (đổi câu đã duyệt):** lời S03.3 ("lender policy … a 75 percent bar") và S12.3 ("the 75 percent bar that lenders often use early on") nói rộng hơn nguồn (một nhà đầu tư, không phải mọi bên cho vay). Đề xuất trong `PLAN.md` §3; S03 (đã sinh ở bản đọc thử) và S12 **chưa sinh lại** cho tới khi chủ dự án chọn.
