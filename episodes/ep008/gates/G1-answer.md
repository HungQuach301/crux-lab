# G1 Tập 8 — trả lời của chủ dự án · 2026-10-13

Nguồn: lệnh mở chặng sau G1 (chủ dự án dán vào phiên mới; gói `gates/G1.md`, issue [HungQuach301/crux-lab#55](https://github.com/HungQuach301/crux-lab/issues/55)). Nguyên văn:

> 1 Duyệt #20 + logline (Census HVS 4,83 % Q4 2025 / 5,59 % Q1 2026 đã được chat chiến lược xác minh trên 2 PDF gốc ngày 13/10 — ghi RIGHTS D-CENSUS-HVS là đã xác minh; điều khoản census.gov: tác phẩm chính phủ Liên bang 17 U.S.C. §105).
> 2 Duyệt kịch bản v2, nhưng viết lại riêng cold open S01–S03 theo story.md mới (tham chiếu Fortune of Nations): 3 sự thật lật kỳ vọng trước 0:35, câu hỏi của Nina trước 0:40, hứa đáp án bằng một nghịch lý trước 0:50; câu miễn trừ trong lời ≤ 1 vế ("history, not a forecast"), "US only" và "not advice" lên hình; thêm tên chương gợi hình + câu chốt cuối chương + kết bằng bảng điểm 3–4 mục, quay lại "the street" và chuyền sang tập kế. Kiểm mù lời đúng một lượt (6 người đọc, rubric cũ); advice_stated phải = 0; M1–M6 đo lại trên bản đọc thật. Móc H-A giữ ý.
> 3 Tiêu đề T1. N1 the street (lưới cột = năm, hàng = tháng) và N2 the rent tag: duyệt, vào thư viện. N3 Nina: v2. N4: v2 + nhãn "cash, not stocks". N5: bỏ, và đổi lời S08.4 → "…sits past the end of the street, where no house stands yet, because…", S29.1 → "past the end of the street?", beats B02/B29/B32 bỏ N5. Footage Tập 8: chỉ bản đồ Natural Earth (đã tải); bỏ ảnh LoC/HUD (mạng chặn, thử ở Tập 9). Không C3 riêng. 1 Short: S17.1 → S19.3 "The darkest house" + thẻ cuối đối trọng như REVIEWER đề xuất. Không thumbnail.

Kèm trong lệnh (luật chặng, nguyên ý):
- Mô hình xưởng 6 mốc (tổng kết Tập 7, chủ dự án duyệt 13/10) áp từ ranh giới sau G1. Chặng này: **M2 hoàn tất** (sửa cold open theo câu 2; animatic 540p xám cả tập; cổng gốc tắt tiếng trên animatic, gộp thận trọng, ≤ 2 vòng mỗi lỗi — không mở cổng C3 riêng) → **M3** nháp 540p (giọng một lần, đọc `GET /v1/user/subscription` trước) → **M4** hậu kỳ (J/L-cut, màu theo hồi) → **M5** kiểm định đủ bộ trên nháp kể cả bộ lấy mẫu trang (khi K44 đã merge thì theo LOCK mới) → **G2** (phiếu L3 trên nháp + 3 khung tĩnh 1080p). **1080p chỉ dựng sau G2.**
- Khi `origin/main` có squash tongket-t7: merge `main` vào `ep008` trước M3 và theo playbook mới (CHAY-TAP-N); trước đó theo luật tạm 13/10.
- Đổi số khiếu nại Tập 8 A38–A41 → **A42–A45** (tongket-t7 giữ A38–A41).
- **Trần chi CỨNG chặng này: Console $25** (chạm thì dừng hỏi); headless khoá Console, **0 agent con kể cả bên trong headless**; dừng tiến trình bằng PID; push ≤ 2 h một lần; không mở phiên mới khi container còn tệp lớn.

| Câu | Quyết định |
|---|---|
| 1 · đề tài | **#20 + logline duyệt.** Census HVS 4,83 % (Q4 2025) · 5,59 % (Q1 2026) **đã xác minh** trên 2 PDF gốc (chat chiến lược, 13/10) → `RIGHTS.md` D-CENSUS-HVS = đã xác minh; tác phẩm chính phủ Liên bang (17 U.S.C. §105) |
| 2 · kịch bản | **v2 duyệt**, trừ cold open S01–S03: **viết lại** theo `story.md` mới (tham chiếu Fortune of Nations) — 3 sự thật lật kỳ vọng < 0:35 · câu hỏi của Nina < 0:40 · hứa đáp án bằng một nghịch lý < 0:50 · miễn trừ trong lời ≤ 1 vế ("history, not a forecast"); "US only", "not advice" **lên hình** |
| 2 · cấu trúc | Thêm **tên chương gợi hình** + **câu chốt cuối chương**; **kết bằng bảng điểm 3–4 mục**, quay lại "the street", **chuyền sang tập kế** |
| 2 · kiểm | Kiểm mù lời **đúng một lượt** (6 người đọc, rubric cũ); **advice_stated = 0**; M1–M6 đo lại trên bản đọc thật; móc H-A giữ ý |
| 3 · tiêu đề | **T1** "Rent vs Buy: Every Month Since 1991, Replayed" |
| 3 · hình | N1 the street (lưới cột = năm, hàng = tháng) + N2 the rent tag: **duyệt, vào thư viện**. N3 Nina **v2**. N4 **v2 + nhãn "cash, not stocks"**. N5 **bỏ** |
| 3 · lời đổi | S08.4 → "…sits past the end of the street, where no house stands yet, because…"; S29.1 → "past the end of the street?"; beats B02/B29/B32 bỏ N5 |
| 3 · footage | **Chỉ bản đồ Natural Earth** (đã tải); bỏ ảnh LoC/HUD và trang Census (mạng chặn; thử ở Tập 9) |
| 3 · cổng | **Không C3 riêng** |
| 3 · Short | **1 Short**: S17.1 → S19.3 "The darkest house" + thẻ cuối đối trọng (REVIEWER) |
| 3 · thumbnail | **Không** |
