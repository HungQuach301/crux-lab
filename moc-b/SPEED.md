# Mốc B — số đo tốc độ

## Checks đủ bộ (đo 05/10/2026, 14:58–15:54 UTC, máy 4 lõi, 15 GB)
- **Bản đo:** bản sao khoá `git archive` của `moc-b`, LOCK `a20c6878…`. Video là bản giao YouTube của Tập 3 (1080p30, 572 s, SHA `1274f9f6…`), cùng thời lượng và khổ hình với bản gốc. Không có stem (`out/audio/stems` không commit), nên 13 luật MISSING. Script: `checks-time.sh` (giữ trong scratchpad; cách làm giống `episodes/ep003/design/c5/checks.sh`).

| Phần | Thời gian | Tỉ lệ |
|---|---|---|
| Bộ lấy mẫu trang (`checks/page/sampler.js`, mẫu đối tượng mỗi 3 khung, điểm ảnh mỗi 6 khung, một tiến trình) | **3.001 s (50,0 phút)** | **88 %** |
| Luật Python (`checks/py/run.py`, gồm ASR whisper small.en) | 391 s (6,5 phút) | 12 % |
| **Cộng** | **3.392 s (56,5 phút)** | |

- **Đối chiếu Tập 3:** 60–75 phút mỗi lần, có stem. Phần chênh nằm ở các luật cần stem, vốn MISSING ở lần đo này.
- **Điểm nghẽn: bộ lấy mẫu trang**, không phải ASR. Đề xuất A3 trong `checks-appeal.md` sắp lại theo số đo:
  1. song song theo cảnh (`--scenes`, 3–4 tiến trình) → ước 50 → 15–18 phút;
  2. cache kết quả trang theo băm cảnh → lần chạy thứ hai chỉ lấy mẫu cảnh đổi;
  3. một lần ASR cho hai họ luật.
  **Sau:** chưa đo — cần phiên K viết và khoá lại (bên dựng không sửa `checks/`).

## Render 1080p
- **Trước:** Tập 3 ≈ 25–30 phút mỗi lần render 1080p (ledger Tập 3). Khung truyền ra dạng RGBA thô qua base64 (`episodes/ep003/design/c3/render.js` → `APP.frame`), một tiến trình.
- **Sau (phiên nhà máy, đo 05/10/2026, máy 4 lõi, 15 GB):** cùng cảnh Tập 3 **S04 "The replay"** dựng bằng nhà máy (`toolkit/factory/render.js`), 1080p30, **2.249 khung (75,0 s)**, 16 đoạn × ≤ 5 s, mã hoá H.264 CBR 17 Mb/s giống nhau ở mọi lần; chỉ đổi khung trung gian và số worker:

| Khung trung gian | Worker | Thời gian | Khung/s | So với RGBA 1 worker |
|---|---|---|---|---|
| RGBA thô base64 (cách Tập 2–3) | 1 | 481,1 s | 4,68 | 1× |
| **JPEG q 0,95** | 1 | 68,7 s | 32,76 | **7,0×** |
| RGBA thô base64 | 4 | 170,0 s | 13,23 | 2,8× |
| **JPEG q 0,95** | 4 | **41,3 s** | **54,45** | **11,6×** |

- **Chất lượng JPEG so với RGBA (cùng khung, sau H.264):** SSIM 0,99893, PSNR trung bình 48,0 dB (thấp nhất 46,2 dB). Không thấy khác bằng mắt; chữ vẫn qua F05/F08 của checks.
- **Ước cho cả tập 572 s (17.160 khung), không cache:** RGBA 1 worker ≈ 61 phút → JPEG 4 worker ≈ 5,3 phút.
- **Chỉ đoạn đổi (cache theo băm):** dựng lại S04 khi không đổi gì: render 0 s (16/16 đoạn trúng cache), cả lệnh `build.sh` 39 s (trộn tiếng, phần 720p, Short, qc). Lần đầu (voice đã cache): 108 s.
- Lệnh: `node toolkit/factory/render.js <job> --workers 1|4 --fmt rgba|jpeg` trên job `ep003` do `build.py` viết.
