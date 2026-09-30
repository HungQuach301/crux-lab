# PLAN — Cổng Mốc 3 (Phiên M3)

Nhánh `claude/gracious-bell-cf9wvf` (chủ dự án giữ tên). Thiết kế: `DESIGN.md` (đã duyệt). Không chạm Tập 1 / `ep001-v2`.

## Điểm dừng an toàn
- 2026-09-30 (2): đối chứng xong (khoá có thể thu hồi), 20 hồ sơ máy, đóng băng `c84715b`, trộn + khoá key (`6bf5102`, key sao lưu ở scratchpad; dựng lại được bằng khớp văn bản với tệp đóng băng), trang chấm đã gửi, hợp lệ 19/20 (`REPORT.md`). Tiếp: nhận mã chấm → commit key.json → kiểm SHA → giải mã → hoàn tất REPORT.md.
- 2026-09-30 (1): thiết kế + luật hợp lệ khoá (`66c2a10`). Đang: (a) đối chứng `python3 m3/control/gen_control.py` (chạy lại được: bỏ trụ đã có `control/out/<trụ>.json`); (b) ba agent bên máy viết `m3/machine/<trụ>-k/` (thư mục có `thesis.json` hợp lệ = xong; nếu mất agent, mở agent mới cho phần còn thiếu, không cho xem `m3/control/`).
- Tiếp: báo chủ dự án thu hồi khoá khi đối chứng xong → đóng băng (commit, ghi SHA vào `FREEZE.md`) → `m3/verify/verify.py` (V1, V2, V4, V5) + agent V3 mỗi luận điểm → trộn, xoá nhãn, khoá key (`m3/blind/`) → trang chấm → báo cáo.
