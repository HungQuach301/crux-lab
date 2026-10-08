# Bằng chứng sampler K4.0 không đổi page.json cũ (REVIEWER CHÍNH-2)

Fixture `C12-split-view` của `checks/selftest/test_page.js` (`--keep`), chạy `node checks/page/sampler.js <gốc>` hai lần: sampler của `main` @ 447690e (K3.9) và của K4.0, xoá cache cảnh mỗi lần. Bỏ hai khoá trước khi so: `seconds` (thời gian chạy) và `textOnlyTrack` (track mới của K4.0). Ghi lại bằng `json.dump(..., sort_keys=True)`.

`cmp page-sampler-K39.json page-sampler-K40.json` → trùng từng byte (SHA256SUMS: hai dòng cùng băm).
