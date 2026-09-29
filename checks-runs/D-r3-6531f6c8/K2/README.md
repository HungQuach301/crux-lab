# K2 — bài D vòng 3 dưới khoá K2

| | |
|---|---|
| Bộ luật | `checks/` @ LOCK `f9e24c91a464b1948f6eabb08d6da05d5867f78d2fe7ce1f818ec92009f0dcdd` |
| Master | `crux-spike-opus55`, nhánh `media/opus55-cine-phase-d-m3` (ghép 16 phần, kiểm `parts.sha256`): SHA-256 `6531f6c8…` khớp |
| Stem | `m3/stems/` (voice, music, sfx, whoosh, room), SHA-256 khớp `stems.sha256` |
| Artefact | nhánh `claude/opus55-cine-phase-d-jw6me1` @ `76613cf`, `out/m3/root` |
| Hợp đồng | `../contract.json` (phiên kiểm ghi lại từ các hằng số K1) |
| Trang | `page.json` của lượt K1 (`../page.json.gz`, cùng mã lấy mẫu với K2 trừ phần cặp nhân vật). Dữ liệu V04 của K1 (`sideSigns [-1]`, 884 mẫu) chuyển sang dạng cặp `{"1966|mirror": {samples 884, signs {-1: 884}}}`: cùng số đo. Bộ lấy mẫu K2 chạy lại trên trang bài D mất khoảng 2 giờ; đã dừng giữa chừng |
| Baseline REG | `../report.json` (K1 trên cùng master) |

**Kết quả: 59 PASS · 18 FAIL · 1 MISSING · 0 ERROR** (78 luật). K1: 59 · 16 · 0 · 0 (75 luật).

## Điểm hiệu chỉnh bắt buộc

**T1 TRƯỢT**: 39/355 lượt nghe thấy ở khe nghỉ (0,11; cần ≥ 0,60), trong dải 1,5–8 kHz của hợp đồng D. Mở dải ra 40 Hz–16 kHz (lợi nhất cho D): 0,16, vẫn trượt. Thêm: không có stem `sonify` (tiếng dữ liệu trộn trong `sfx`), và dải khai chỉ chứa 8% năng lượng `sfx`.

## Đổi kết quả so với K1, và vì sao

| Luật | K1 → K2 | Vì sao |
|---|---|---|
| S13 | PASS → **FAIL** | định nghĩa lại theo G-009: 2 chuỗi câu vụn ("Same money in. / Same money out. / Same average."; "So, what decided it? / Not the average. / The first 10 years."). Luật cũ (CV mọi câu 0,49) cho đạt |
| F11 (mới) | — → FAIL | hợp đồng M3 gồm stem `sonify`, bài D không giao |
| S16 (mới) | — → FAIL | 2/6 câu nói số quyết định (năm 1991) không gọi tên nhân vật trong cảnh ("One ran out of money in 1991."). Tham khảo: bài D làm trước G-008 |
| L1 (mới) | — → MISSING | không có stem `sonify` |
| S01, S03, S05, S06, V09 | PASS → PASS | nay đọc hợp đồng; S01 kiểm thêm 3 trường quy ước chữ (`realBasis`, `rebalance`, `withdrawalTiming`) trùng hợp đồng |
| S04, V04, T1 | FAIL → FAIL | S04: 3 năm thiếu ở một nguồn (như K1); V04: màu chính của 1966 chỉ 94,0% (như K1); T1: định nghĩa mới, vẫn trượt |

REG: **PASS**. So được 65 luật (cùng fingerprint), 0 hồi quy; không so: S01, S03–S06, S13, V04, V09, T1 (đổi định nghĩa).
