# B+2 — "≤ 2 số MỚI được NÓI mỗi cảnh" (Mốc V)

**Luật:** mỗi cảnh nói tối đa 2 số *mới* (lượng có đơn vị, sau chuẩn hoá lời); số đã nói ở câu trước là lặp lại, không tính.
Số thứ ba trở đi chuyển thành **nhãn trên hình** (người biên tập chọn số nào), phạm vi tuyên bố giữ nguyên.

| Hạng mục | Kết quả | Bằng chứng |
|---|---|---|
| Bộ kiểm | `toolkit/factory/numbers_said.py` (CLI + `check_scenes`) | — |
| Gắn vào spec | `spec.py` → BLOCK `spoken_numbers`; `spoken_numbers_max` (mặc định 2) | test (e) |
| Selftest | 5/5 OK (`toolkit/tests/test_numbers_said.py`) | (a) đơn vị, (b) 3 mới → BLOCK, (c) lặp không tính, (d) S03 trước/sau, (e) spec |
| Tập 5 S03 trước | **BLOCK**: "eighty percent", "two years", "seventy-five percent" | `ep005-before.txt` |
| Tập 5 S03 sau | **ĐẠT**: 2 số mới ("eighty percent", "seventy-five percent"); "2 năm" thành nhãn | `ep005-after.txt`, `ep005-S03.diff` |
| Cả Tập 5 sau sửa | 0 BLOCK (S12 nay nói "two years" lần đầu: 2 số mới, vẫn ≤ 2) | `ep005-after.txt` |
| Tập 4 | `spec: OK` (không đổi) | — |
| Tập 3 (đã phát hành) | 3 cảnh vượt (S02, S05, S08) → **WARN** (danh sách `LEGACY`), không chặn dựng lại | — |

**Sửa S03.3 (chỉ trên bản sao `moc-v/work/ep005-b1/`, không đụng nhánh `ep005`):**
"for Fannie Mae loans, that's ~~two years~~ **a waiting period** and a 75 percent bar." + nhãn trên hình
`Fannie Mae: wait ≥ {value_removal_seasoning_years} years · loan ≤ {value_removal_ltv_early}` — vẫn trỏ cùng ba claim, phạm vi không đổi.
Áp vào nhánh `ep005` thật là việc của phiên Tập 5 (cần đọc lại giọng S03 — 1 cảnh).

**Giới hạn đã biết:** hai số nối bằng "and" trước cùng một đơn vị ("1.378 and 1.388 times", Tập 3 S05) bị gộp thành một mục;
chỉ ảnh hưởng thông báo, không làm lọt cảnh vượt ngưỡng (cảnh đó vẫn bị báo). Số đếm không đơn vị và năm lịch không tính.
