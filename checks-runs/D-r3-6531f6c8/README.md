# Lượt chạy K1 trên bài D, master vòng 3

Lượt này chạy bộ luật đã khoá trên master cuối của bài D.

| | |
|---|---|
| Bộ luật | `checks/` @ LOCK `62b5206df11327e50f3cca6a5d902dc988efb0bd8d27b5322dcbdf77cc4fac96` |
| Master | `crux-spike-opus55`, nhánh `media/opus55-cine-phase-d-m3`, ghép theo `m3/README.md`. SHA-256 `6531f6c8e1d11473251156875ad5631ecc2b6768517eab47d4ab8756735e3b62`, khớp `video.sha256` |
| Stem | `m3/stems/` (voice, music, sfx, whoosh, room). Khớp `stems.sha256`; `room` được ghép từ 2 phần |
| Artefact hợp đồng | nhánh `claude/opus55-cine-phase-d-jw6me1` @ `76613cf`, `out/m3/root` |
| Trang dựng | `render-d/prod/page.html` của cùng commit. 7060 mẫu đối tượng, 3372 mẫu điểm ảnh, 7015 s |
| Baseline cho REG | `baseline-audit-r2.json`: báo cáo độc lập của Phiên K trên master r2 `dd6117c6…`. Nguồn: `audit/checks-report-audit.json`, nhánh `audit/d-final`, LOCK cũ `0478df73…` |
| Lệnh | `python3 checks/py/run.py <root> --baseline baseline-audit-r2.json`. Bộ lấy mẫu trang chạy trước bằng `checks/page/sampler.js` của cùng khoá |

**Kết quả: 59 PASS · 16 FAIL · 0 MISSING · 0 ERROR** (75 luật). Chi tiết ở `report.md` và `report.json`.

## Tệp

- `report.json`, `report.md`: kết quả 75 luật.
- `page-summary.json`: phần tóm tắt của bộ lấy mẫu trang (các luật khung hình, số sự kiện biểu đồ).
- `page.json.gz`: bản đầy đủ của bộ lấy mẫu trang.
- `asr-6531f6c8e1d11473-bb994d7f.json`: bản ASR theo câu mà các luật đã dùng.
- `selftest-py.json` (154/154) và `selftest-page.json` (55/55): kết quả test tự chứng minh.
- `v12-118.4s-video-vs-clean.png`: ảnh bằng chứng cho V12 ở 118,4 s. Bên trái là khung master, nhãn "0%" nhoè và nhân đôi khi máy lia. Bên phải là bản dựng sạch của trang.

## Ghi chú

- **Có stem M3.** Lần này các luật stem đều chạy được (A07, A08, A10, A11, A12, R01). Trong audit r2, các luật này là MISSING vì thiếu stem.
- **REG trượt** vì V04: r2 PASS, r3 FAIL. Màu chính của nhân vật 1966 chỉ chiếm 94,0% số quan sát, ngưỡng là ≥ 95%.
  - Chính báo cáo của Phiên D trên r3 (LOCK cũ) cũng cho V04 FAIL.
  - 19 luật K1 đã đổi cách đo được coi là không so được.
- **Khoá mới `b97bfc6b…` (2026-09-28).** Khoá này chỉ khác `62b5206d…` ở `checks/README.md`: thêm mục "Ngưỡng tạm". Mã luật và ngưỡng không đổi, nên kết quả lượt chạy này vẫn đúng với khoá mới.

## K2 (2026-09-28): chưa chạy lại được

- Khoá K2 đọc mô hình, nhân vật, nguồn, trường hợp phải hiện và dải tiếng dữ liệu từ hợp đồng tập. Bài D không có hợp đồng; phiên K2 ghi lại hợp đồng từ các hằng số K1 đã gắn cứng: `contract.json` ở thư mục này (chạy: `run.py <root> --contract checks-runs/D-r3-6531f6c8/contract.json --baseline checks-runs/D-r3-6531f6c8/report.json`).
- **Chưa chạy lại được trên master r3**: master, stem và artefact nằm ở repo `crux-spike-opus55`; phiên K2 không được cấp quyền đọc repo đó. Vì vậy điểm hiệu chỉnh "bài D vòng 3 → T1 phải trượt" chưa được đo bằng âm thanh. Về cấu trúc T1 K2 vẫn trượt trên r3 (tiếng dữ liệu trộn trong `sfx`, không có stem `sonify`), và L1 là MISSING.
- Dự kiến khi chạy lại: các luật có định nghĩa không đổi giữ kết quả của `report.json` (REG so theo fingerprint); S01, S03–S06, V04, V09 đọc hợp đồng nên phải cho cùng kết quả như K1 nếu hợp đồng ghi đúng hằng số cũ (ngoại lệ đã biết: S04 nay lấy dung sai 0,5 pp từ hợp đồng thay vì từ `data/sources.json` của D; V04 nay đòi màu và hình **đúng** `#ffc857`/solid và `#5a9ceb`/dashed, và vẫn trượt vì màu chính của 1966 chỉ 94,0%).
