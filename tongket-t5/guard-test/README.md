# Thử an toàn chạy nền (áp tổng kết Tập 5 mục 12) — 08/10/2026
Đoạn nhỏ: `moc-v/seg/ep004` (Tập 4 v3k, 69,6 s), 540p, ra thư mục nháp (không ghi vào repo). Lệnh chạy bằng công cụ nền của phiên.
| Lượt | Lệnh | Kết quả |
|---|---|---|
| build 1 | `build_seg.py moc-v/seg/ep004 --res 540 --out <nháp>/v3k-540.mp4` (nền) | ĐẠT, 291,3 s; tệp dựng trong `.staging-v3k-540-<pid>/`, đưa sang chỗ thật khi cả 6 bước đạt, thư mục tạm xoá (`build1.log`, `build1.build.json`) |
| build 2 | cùng lệnh, khi build 1 đang render (`render_shots.js` pid 9906) | **TỪ CHỐI, thoát 3** — liệt kê 3 tiến trình của build 1; không ghi gì (`build2.log`) |
| `build.sh` | `bash toolkit/build.sh <yaml giả>` cùng lúc | **TỪ CHỐI, thoát 3** trước khi gọi build.py |
| `guard.py` tay | `python3 toolkit/factory/guard.py` cùng lúc / sau khi xong | thoát 3 (3 tiến trình) / thoát 0 "rảnh" |
| build 3 (trượt) | `build_seg.py moc-v/seg/ep005 --out <nháp>/v3k-540.mp4` — đoạn có lỗi chú thích nuốt mã (mục 13) | trượt ở `lint`, thoát 1; `v3k-540.mp4` **giữ nguyên** (md5 tệp 852bf805193b trước = sau); báo cáo `build3.build.failed.json`, thư mục tạm giữ để xem |
Sự cố trong lúc thử (đã hoàn tác): lần thử đầu build 1 trượt ngay (thiếu `three` trong `world/vendor`, đã `npm ci`, không commit) nên `build.sh episodes/ep005/episode.yaml` chạy thật vì máy đã rảnh — ghi đè `episodes/ep005/out/factory/timeline.json` rồi dừng ở bước world; đã `git checkout` tệp đó và xoá `episodes/ep005/work/factory/` (không theo dõi). Từ đó thử `build.sh` chỉ bằng yaml giả.
