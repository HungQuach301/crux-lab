# A29 (cache trang theo đoạn) — đo trùng byte, K4.4.1 · 14/10/2026

**Mã đo:** A29 (`3a00e910`, cherry-pick `ddb3e387`) trên bộ lấy mẫu K4.4 + sửa rò ffmpeg (K4.4b), đóng băng ở `/home/user/k441` (`code.sha`). Mã sẽ khoá (`K441-A29.patch` áp trên `main` sau K4.4b) khác mã đo ở: chặn lỗi ffprobe (kích thước, gói), `try … finally` đóng bộ đọc (không đổi số đo), khoá đoạn theo mọi đoạn cảnh chạm tới (REVIEWER K4.4.1 C1; Tập 6, 7 ranh giới cảnh trùng ranh giới đoạn nên cùng tập hợp đoạn) và phiên bản trình duyệt trong khoá — chỉ đổi khoá, không đổi số đo. Trang: `episode_page.py` dựng lại từ `main`; video = master bản giao (Tập 6 `f96da0ea…`, Tập 7 `529471f0…`). `--jobs 4`. So sánh: `compare.py` — bỏ `seconds`, `sceneCacheHits`; chuẩn hoá URL `blob:null/<uuid>` (ngẫu nhiên mỗi lần nạp trang).

| Tập | Lượt | Giờ máy | Cảnh từ cache | So với --no-cache |
|---|---|---|---|---|
| 6 | --no-cache | 6.615 s | — | — |
| 6 | có cache, cache trống | 6.459 s | 0/31 | **trùng byte** |
| 6 | ấm | **65 s** | 31/31 | **trùng byte** |
| 7 | --no-cache | 11.322 s | — | — |
| 7 | --no-cache lần 2 | 11.449 s | — | **khác** (C12 1 số đo, 6/19.538 chartEvents ở S11/S26, motionTrack) |
| 7 | có cache, cache trống | 11.204 s | 0/34 | khác lần 1 như trên; khác lần 2 chỉ motionTrack |
| 7 | ấm | **116 s** | 34/34 | **trùng byte với lượt có cache** |

**Kết luận đo:** Tập 6 đạt tiêu chí trùng byte. Tập 7 **không** đạt theo nghĩa đen, nhưng hai lượt **không cache** cũng khác nhau đúng ở các trường đó → bộ lấy mẫu không tái lập được trên trang Tập 7 (có sẵn trước A29; lượt "cache trống" không lấy gì từ cache mà vẫn lệch). Cache tái tạo đúng lượt đã điền nó (ấm = cache trống, từng byte). Trên **33 luật đọc page.json**, bốn lượt Tập 7 cho **cùng trạng thái và cùng mọi chỉ số** (`ep007-rules-4runs.json`). `seek(t)` thử trong một trình duyệt mới với 6 lịch sử seek/freeze khác nhau cho cùng đối tượng ở S11 (`seek.js` ngoài repo) → nguồn lệch chưa xác định (nghi: gán cảnh cho trình duyệt theo thời gian khi chạy song song).
**Trạng thái:** chủ dự án 14/10 chọn (a) → **khoá K4.4.1** (`ANSWER.md`). Trước đó: chưa khoá vì điều kiện "trùng byte" không đạt theo nghĩa đen trên Tập 7. Đề xuất (lô K sau): (a) chấp nhận tiêu chí "cache = lượt đã điền nó + mọi luật trùng" và khoá; hoặc (b) tìm và sửa nguồn không tái lập của bộ lấy mẫu trên Tập 7 rồi đo lại byte.
Phát hiện kèm: rò ffmpeg của bộ lấy mẫu (66 tiến trình ≈ 10 GB → OOM giết trình duyệt → lượt treo, 2 lần) — đã sửa ở K4.4b.
