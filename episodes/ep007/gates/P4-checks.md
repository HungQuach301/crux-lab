# P4 — checks đủ bộ trên master 1080p (khoá `dc4981b3`) · 2026-10-13

Bộ lấy mẫu trang chạy 2 lượt (trần 2 h, `RESUME=1`) + luật Python (`KEEP=1 PYONLY=1`) trên bản sao `/home/user/chk-p4`. Môi trường đã sửa: PyAV 19 → 14.2 (faster-whisper 1.2.1 gọi `av.open(metadata_errors=…)`), dữ liệu FRED tải lại (`fetch.py --verify`, SHA khớp). Báo cáo: `c5/checks-reports/chk-p4-report.{json,md}`, log `chk-p4py.log`. Tổng: PASS 49 · FAIL 43 · MISSING 7 · ERROR 1.

**Đạt so với P3:** F10, F11, S21 (gói P4) ĐẠT; SH01–SH05 ĐẠT (chạy lại với `out/shorts/` link tới `work/factory/SH*.mp4` — P3 MISSING).

**CHẶN đã biết (chủ dự án chấp nhận ở G2):** A14 — ASR small.en "Tesla's" thay "Tessa's" ở S09.3, S15.3, S25.2 (P3: S15.3, S25.2; S09.3 là chỗ mới cùng loại, A34).

**CHẶN MỚI — luật đọc `out/checks/page.json`, lần đầu đo ở Tập 7 (P3 chưa chạy bộ lấy mẫu trang):**
| Luật | Đo | Bản chất |
|---|---|---|
| **C07** tỉ lệ cột | 122 khung S09 (≈ 166 s): cột "runs off the frame along its value axis" | **Hình thật:** máy đẩy vào hai chồng lãi, đáy chồng (mốc 0) và chồng $477,622 ra ngoài khung (`c07-S09.png`). Sửa = đổi máy quay S09 (render lại đoạn b) |
| **S02** giả định trên thẻ phương pháp | "us-only / history-not-forecast in method card" = False | **Nhận diện:** thẻ S32 "What this leaves out" CÓ dòng "US only · History, not a forecast" — luật không nhận thẻ này là thẻ phương pháp (tiêu đề/role). Ứng viên khiếu nại |
| **S07** số trong lời chưa đăng ký | 52 (vd "15", "30" của kỳ hạn; "$320,000" ở S01.2, S04.2) | **Siêu dữ liệu:** `claims.json` thiếu `spoken` cho các số này; không đổi lời/hình |
| **S09** cơ sở tiền | 29 claim tiền thiếu `basis`; 2.384 khung thiếu nhãn cơ sở trên hình | **Siêu dữ liệu + hình:** khai `basis` (danh nghĩa) trong claim được; vế "nhãn cơ sở trên hình" cần thêm chữ lên hình (đổi hình) |
| REG | MISSING (không có báo cáo nền) | thủ tục: chạy `--first` hoặc `--baseline` |

CHÍNH mới (page): V08 (1 mẫu tương phản 1,01), V09 (nhân vật khai báo không thấy = 0), V11 (285 va chạm chữ), V12 (17 mẫu NCC < 0,97), L1 (tỉ lệ lời/dữ liệu 1–4 kHz).
