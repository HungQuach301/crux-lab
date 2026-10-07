# B+1 · voice_overrides — bằng chứng (06/10)

| Điều kiện (chủ dự án) | Kết quả | Bằng chứng |
|---|---|---|
| Công cụ dựng đọc `voice_overrides` (seed hoặc take theo cảnh) | ĐẠT — `toolkit/factory/voice.py` `scene_cfg()` + `take`; `build.py do_voice()`; `spec.py` BLOCK cảnh lạ / khoá lạ / take thiếu | diff trên nhánh `moc-v` |
| Tập 5 S18 seed 1006 dựng đúng chữ "illustrative" (ASR) | ĐẠT — S18 → take `5b3b914301ef48ab` (seed 1006); ASR small.en: "illustrative" ✓, "illustrated" ✗. Take mặc định seed 1005 (`e81f3c6c6994bce4`): ASR "illustrated" | `b1-ep005.json` (`b1_check.py`, API khoá, 20/20 cảnh lấy từ cache) |
| Selftest | ĐẠT — 5 test (`toolkit/tests/test_voice_overrides.py`); bộ test toolkit cũ vẫn đạt | `python3 toolkit/tests/test_voice_overrides.py` |
| Tập không khai báo → kết quả giống hệt trước | ĐẠT — mã cũ (`main`) và mã mới: 20/20 cảnh cùng khoá, cùng take, cùng file | `b1-identical-no-overrides.json` (`b1_identical.py`) |

Selftest bắt được một lỗi thật trước khi gộp: take chọn theo tên tự đặt bị tìm theo tên khoá băm (đã sửa).
Ca thật chạy trên bản sao CHỈ ĐỌC của nhánh `ep005` (`moc-v/work/ep005-b1`, không commit); không gọi ElevenLabs (0 ký tự).
