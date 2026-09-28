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
