# A32 — hiệu chuẩn cổng gốc · GHI TRƯỚC (commit trước lượt đọc đầu tiên) · K4.4, 13/10/2026

**Bản đo:** master bản giao Tập 6 `episodes/ep006/out/video.mp4` SHA-256 `f96da0ea…` (ghép từ `ep006-delivery`, trùng SHA bản giao). Dải 6 khung tắt tiếng, giữ chữ/số, 23 nhịp loại 1 (`blind_c4.IMAGE`), khoảng = cảnh của nhịp ±0,2 s (như F-14 `root_v4.py`).
**Người đọc:** headless mới mỗi lượt (`toolkit/blind/headless.sh`, sonnet, chỉ Read), vai T + câu 1–5 của `blind_c4.py`. 2 người/nhịp, người thứ 3 khi tách đôi. **Người chấm:** 2, headless, rubric MỚI (A28), gộp thận trọng, cả gói của lượt chấm lại sau khi có người thứ 3.
**Ba lượt đối chứng âm** `p1`, `p2`, `p3`: mỗi lượt một bộ người đọc mới, một gói chấm riêng. **Đối chứng dương** (trong gói của `p3`): B01, B10, B24 với 6 ô hình **đảo thứ tự** (dải số 1–6 giữ nguyên) — nghĩa của ba nhịp nằm ở chiều thời gian (thùng tắt dần, đường tụt xuống, hàng mờ dần), đảo lại là nghĩa ngược. 20 nhịp còn lại của bản dương = ảnh trùng từng điểm với `p3` nên lấy kết quả `p3`.

## Luật mới đề xuất (đo trên dữ liệu này, chưa áp; đổi cổng gốc → gói chủ dự án)
Bản ứng viên X so với bản đối chứng C (bản đã qua cổng), **đọc lại C trong cùng phiên, cùng gói chấm**:
1. Nhịp **tụt** = ĐẠT ở C (lượt đọc lại cùng phiên) và không ĐẠT ở X.
2. **TRƯỢT** khi tụt **≥ 2 nhịp**.
3. Tụt đúng **1 nhịp** → xác nhận: gói riêng, 3 người đọc mới + 2 người chấm, cả hai bản, chỉ nhịp đó; vẫn tụt (C ĐẠT ≥ 2/3, X không) → TRƯỢT.
4. **Sàn tuyệt đối:** số nhịp ĐẠT của X ≥ **F = (min số nhịp ĐẠT của p1, p2, p3) − 1**; dưới sàn → TRƯỢT. advice_stated = 0 giữ nguyên.

## Tiêu chí chấp nhận (ghi trước)
- **Âm:** với mọi cặp có thứ tự (Ci, Xj), i ≠ j trong {p1, p2, p3} (6 cặp), luật mới bước 2 + 4 cho **không TRƯỢT** (cặp tụt đúng 1 nhịp ghi "cần xác nhận", không tính TRƯỢT ở bước này; báo số cặp như vậy).
- **Dương:** (C = p3, X = p3+pos) luật mới cho **TRƯỢT**.
- Đạt cả hai → khuyến nghị luật mới. Trượt một trong hai → báo số, không khuyến nghị luật này (đề xuất khác trong gói).
- Báo kèm: phân bố số nhịp ĐẠT, nhịp lật giữa các lượt, luật CŨ (≥ 20/23 và không nhịp nào tụt) trên cùng 6 cặp và cặp dương.
**Trần chi A32:** $8 (Console). Vượt → dừng, báo số đã có.
