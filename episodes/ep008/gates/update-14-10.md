# Cập nhật chủ dự án 14/10 (giữa chặng M3–M5) — nguyên văn

> Cập nhật chủ dự án 14/10 (A32 = 1a, K4.4b sắp khoá): cổng gốc khi so hai bản (vd 5 nhịp "so sánh giữa cảnh") chỉ là CHẨN ĐOÁN, không tự trượt và không mở thêm vòng sửa. G2 nêu các nhịp lật kèm khung trước/sau ghép cạnh nhau; phiếu L3 của chủ dự án là thước cuối. Khi K4.4b merge main: merge vào ep008 trước khi chạy checks đủ bộ. Tiếp tục tới G2.

Áp ở Tập 8:
- Cổng gốc ở M5 (nháp so với animatic) = **chẩn đoán**: không tự trượt, không mở vòng sửa vì nó; B09 B10 B20 B24 B25 không sửa thêm.
- G2: các nhịp lật (đạt ↔ trượt giữa animatic r1/r2 và nháp) có **khung trước/sau ghép cạnh nhau**; phiếu L3 là thước cuối.
- Trước checks đủ bộ: `git fetch origin main`; nếu có K4.4b → merge vào `ep008` rồi mới chạy (`contract.json lock` theo LOCK mới).
- `gates/M5-intent.md` §2 (ngưỡng 20/24, hồi quy → đọc lại) được thay bằng cập nhật này (lệnh chủ dự án, không phải sửa bộ đo của bên dựng).
