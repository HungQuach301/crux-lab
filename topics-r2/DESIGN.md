# topics-r2 — thiết kế vòng 2 (ghi TRƯỚC khi sinh)

Thẩm quyền: `decisions/D-004.md`; chủ dự án mở vòng 2 ngày 2026-10-01 sau khi duyệt báo cáo vòng 1 (`topics-r1/REPORT.md`, KHÔNG ĐẠT, chạm trần). Phiên DT1. Luật ở file này viết trước khi có thẻ nào; không sửa sau khi thấy kết quả.

## Biến đổi (đúng MỘT)

**Cách chấm bước 1:** chủ dự án chọn **đúng 9/18** thẻ "muốn làm" (thay thang tuyệt đối 5 mức của vòng 1). "Được chọn" thay cho "điểm ≥ 4" trong mọi thước đo.

## Giữ nguyên

Đầu bài (`BRIEF.md`, khối BRIEF giống hệt vòng 1), khuôn thẻ và `tools/cardcheck.py` (bản sao vòng 1), tỉ lệ 12 máy / 6 đối chứng (4 + 2 mỗi trụ), bên máy (3 agent, quy trình và hồ sơ như `topics-r1/DESIGN.md` §"Bên máy"), đối chứng GPT-5.5 (medium, không công cụ, không dữ liệu, một lệnh/trụ, gọi lại tối đa 2 lần), luật kiểm hợp lệ V0–V5 (`verify/verify.py`, bản sao), câu hỏi cố định *"Would you approve this as a future episode for this channel?"*, chip lý do, nút quay lại, ghi giây, bảng AI 6 vai niêm phong trước khi chủ dự án chấm (các vai chấm theo cùng ngân sách 9/18), bước 2.

**Thẻ mới (yêu cầu của chủ dự án, không phải biến thí nghiệm):** loại mọi đề tài trùng `topics/queue.md`, 6 thẻ đối chứng vòng 1 và đề tài Tập 1. Danh sách loại trùng đưa nguyên văn cho **cả hai bên** (khối `EXCLUDE` trong `BRIEF.md`). Trùng = cùng lõi quyết định; một agent mới phán xét 18 thẻ trước khi đóng băng; thẻ đối chứng trùng → gọi lại theo luật sai khuôn; thẻ máy trùng → agent máy thay thẻ.

## Thước đo vòng 2

Gọi m = số thẻ máy được chọn (0–9); đối chứng được chọn 9 − m.
- **CHÍNH-1:** m/12 ≥ 50 % ⇔ m ≥ 6.
- **CHÍNH-2:** m/12 − (9 − m)/6 ≥ +20 điểm ⇔ **m ≥ 7** (m = 6 cho 0 điểm; m = 7 cho +25 điểm).
- **CHẶN:** hồ sơ máy hợp lệ ≥ 10/12.
- Vòng **đạt** ⇔ m ≥ 7 và CHẶN đạt. Cửa sổ ±5 %: m = 6 (CHÍNH-1 đúng ngưỡng 50 %) phải nêu tên.
- THAM KHẢO: thời gian chấm, nửa đầu/nửa sau, chip, từng trụ, độ khớp bảng AI (đồng ý chọn/không chọn với chủ dự án).

## (a) Xác suất qua do ngẫu nhiên (ghi trước)

Nếu chủ dự án chọn 9/18 hoàn toàn ngẫu nhiên, m theo phân phối siêu bội (N = 18, K = 12 máy, n = 9):

| m | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|
| P | 0,5 % | 6,1 % | 24,4 % | 38,0 % | 24,4 % | 6,1 % | 0,5 % |

**P(m ≥ 7) ≈ 31,0 % mỗi vòng**; qua hai vòng liên tiếp do ngẫu nhiên ≈ 9,6 %. Một vòng đạt riêng lẻ **không** phải bằng chứng máy hơn đối chứng; vì vậy D-004 đòi 2 vòng liên tiếp.

## (b) Cách đọc kết quả (ghi trước)

- Vòng 1 đã tính "máy không hơn đối chứng". Nếu vòng 2 cũng vậy (m ≤ 6) → đủ điều kiện dừng của D-004 §5 cho câu hỏi *"máy có đề xuất đề tài tốt hơn không"*. Cách đọc: **khâu ý tưởng không cần máy; giá trị máy nằm ở khâu kiểm dữ liệu và mới lạ** (hồ sơ hợp lệ 12/12 ở vòng 1). Đề xuất khi đó: **D-005 mô hình lai** — ý tưởng đến từ mọi nguồn (chủ dự án, đối chứng, người xem, máy), máy kiểm dữ liệu, mới lạ và rủi ro claim cho từng ý tưởng. **Không** đề xuất "dừng hẳn, chọn tay như Tập 1".
- Nếu m ≥ 7 → vòng đạt 1/2; ghi kèm xác suất ngẫu nhiên 31 %; cần vòng 3 đạt nữa mới qua.

## Chỉ báo cáo (sau khi chủ dự án chấm; không tính vào ngưỡng)

Chạy kiểm mới lạ theo quyết định của máy (cùng quy trình: ≥ 3 truy vấn web, phán `not-found` / `answered-without-data` / `answered-with-data`, chỉ ghi link) trên **6 thẻ đối chứng vòng 1 và 6 thẻ đối chứng vòng 2**; báo tỉ lệ `answered-with-data` (so với 0/12 hồ sơ máy giữ lại sau tự lọc, và tỉ lệ loại khi máy tự sinh).

## Trộn và chấm

Như vòng 1, trừ trang chấm: mỗi thẻ một màn hình, một nút bật/tắt **"Want to make it"**, bộ đếm `x / 9`; trang chỉ hiện mã khi đúng 9 thẻ được chọn. Mã: `R2-<sha6> 01:y:nv:12 02:n::8 …` (thẻ:chọn y/n:chip:giây).
