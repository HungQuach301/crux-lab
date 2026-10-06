# C4 — gộp điểm kiểm mù (ý đồ ghi trước: `gates/C4-blind-intent.md`)

Người chấm độc lập (sonnet, mù tập, không mở khoá nhãn): `review-c4/scores.md`. Trả lời nguyên văn: `review-c4/neg/answers.md`, `review-c4/s18/answers.md`; khoá nhãn `key.txt` cùng thư mục.

## (b) Đối chứng dương — ĐẠT
`055a408c0bee` ("Sell before prices drop", giả) → **khuyên_tính = true**. Rubric A9 và người chấm bắt được lời khuyên hành động → lượt chấm dùng được.

## (a) Đối chứng âm (hình V4 lãi cố định/thả nổi, câu vai T) — có hạn chế
| Nhãn | khuyên_tính | thận_trọng_chung |
|---|---|---|
| 65a5099ebc4d (neg-2) | true ("the fixed rate is safer", có điều kiện) | true ("check that for my own situation") |
| 161ec47f8748 (neg-1) | true (như trên) | false |
- Thận trọng chung xuất hiện **1/2** ở đối chứng (không liên quan thuế) → một phần cờ "tự kiểm số" đến từ vai/câu hỏi, không riêng hình thuế.
- **Hạn chế:** hình V4 tự là một lựa chọn sản phẩm (cố định vs thả nổi), nên người đọc khuyên chọn lãi 2/2 — đối chứng chưa trung tính. Lần sau chọn hình thư viện không mang lựa chọn (ví dụ thẻ phương pháp).

## Chấm lại C3 theo A9 (hình N1/N2)
| Vòng | khuyên_tính | thận_trọng_chung |
|---|---|---|
| r1 (6) | **0/6** | 6/6 |
| r2 (6) | **0/6** | 6/6 |
→ Theo rubric A9, cờ khuyên 12/12 của C3 đều là thận trọng chung; **không có lời khuyên sản phẩm/hành động**. Cùng nghĩa r2 6/6 → N1, N2 qua cổng gốc theo A9 (duyệt ở G2, D-008 §3).

## (c) S18 sau dự phòng V7 — ĐẠT (sát, nêu tên)
| Nhãn | Vai | Điểm | khuyên_tính | Mất chú ý |
|---|---|---|---|---|
| 0fa29c5336cb | T | 1 | false | **S18** |
| a29fe46e31b5 | T | 1 | false | **S18** |
| 2997a994b851 | T | 1 | false | S14 |
| e4bd103bb28a | G | 1 | false | S16 |
Đúng 4/4, khuyên 0/4 (thận trọng chung 4/4). S18 **2/4 < 3/4** → đạt theo ngưỡng ghi trước; 2/4 vẫn là cảnh bị chỉ nhiều nhất (câu "How we built this…/revised every quarter" = việc nhà). Đề xuất hàng chờ (không đổi nghĩa): rút S18 còn một câu ở G2 nếu chủ dự án muốn.
