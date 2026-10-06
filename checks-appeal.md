# Hàng chờ đề xuất đổi luật (checks-appeal)

Bên dựng, phiên tổng kết và REVIEWER **không sửa `checks/`**. Mọi đề xuất ghi vào đây (CHARTER §6). Phiên K xử lý **theo lô** ở lần chạy K của tập kế tiếp. Chỉ mở phiên K riêng khi cần **kind mới**. Chủ dự án duyệt phán quyết của K.

**Cách ghi:** mỗi mục có id, ngày, người đề xuất, luật hoặc DX liên quan, chuyện đã xảy ra (số đo), đề xuất, tiêu chí đo thay thế, ảnh hưởng theo 5 tiêu chí (tốc độ, chất lượng, công chủ dự án, chi phí, mở rộng), trạng thái (`mở` / `K nhận` / `K bác` / `chủ dự án duyệt`).

| # | Ngày · ai | Luật | Chuyện (số đo) | Đề xuất | Tiêu chí đo thay thế | 5 tiêu chí | Trạng thái |
|---|---|---|---|---|---|---|---|
| A1 | 05/10 · Phiên B (lessons F5) | mới (liên quan S02, issue #29) | Tập 3: nhãn giả định "IF today's guarantee had existed" phải có trên mọi kết quả trước 5/2005. Luật khoá chỉ canh lúc nhãn xuất hiện, nên phải canh tay suốt C3–C5. | Luật kênh "nhãn điều kiện của claim": claim có cờ `conditional` (trong `out/claims.json`) → **mọi khung** hiện số của claim đó phải có nhãn điều kiện khai trong `contract.json` | Lấy mẫu trang mỗi 0,1 s: khung có số `conditional` mà không có nhãn = 0 | chất lượng ↑ (không sót nhãn); công chủ dự án ↓; tốc độ: +1 luật trang, không đáng kể | K nhận (K3.8) — chờ chủ dự án duyệt |

> **K3.8 — CHẤP NHẬN (CHẶN).** Luật mới **S17**: claim có `conditional:"<id>"` trong `out/claims.json` → mọi khung (mẫu 0,1 s + mọi khung quanh lần hiện đầu, như S08) hiện số đó phải có chữ khớp `pattern` của `contract.json claims.conditions[{id, pattern, claims?}]`; claim liệt kê dưới điều kiện phải mang cờ. Sai nghĩa/claim → CHẶN. Tập 4: điều kiện "a home that rose like its metro area's average" (luật tập 1 của K-brief) đi qua S17; luật tập 2 (ILLUSTRATIVE trên giá $200k/$300k) đã có ở S08; luật tập 3 (không đổi ngưỡng thành thuế phải nộp) là phán đoán nghĩa → REVIEWER/kiểm mù, không thành luật máy.

| # | Ngày · ai | Luật | Chuyện (số đo) | Đề xuất | Tiêu chí đo thay thế | 5 tiêu chí | Trạng thái |
|---|---|---|---|---|---|---|---|
| A2 | 05/10 · Phiên B (story.md §1, lessons F2) | DX-S3, DX-S4; S15 | Tập 3: câu hỏi đầu ở 0:37, lời hứa ~1:04; điểm móc AI 2/5, chủ dự án "mấy phút đầu chưa đủ thu hút". Luật hiện có chỉ canh cold open ≤ 15 s. | (a) `out/script.json` gắn vai câu `hook` / `promise`. (b) Luật THAM KHẢO: câu `hook` đầu tiên bắt đầu ≤ 5 s; câu `promise` kết thúc ≤ 30 s. (c) Xét bỏ trần "cold open ≤ 15 s" của S15 khi đã có (b), vì G-009 đã miễn trừ ở Tập 1 | Đo mốc từ ASR của master (như A14), không đo từ bản khai | chất lượng ↑; tốc độ =; mở rộng ↑ (áp mọi format) | K nhận (K3.8) — chờ chủ dự án duyệt |

> **K3.8 — CHẤP NHẬN CÓ SỬA (THAM KHẢO).** Luật mới **S18**: câu `role:"hook"` / `"promise"` trong `out/script.json`; mốc đo trên ASR của master (từ đầu tiên / cuối cùng nghe được của câu đầu mỗi vai), hook ≤ 5 s, promise ≤ 30 s; câu không nghe thấy = trượt. **Bỏ trần cold open ≤ 15 s của S15** (S18 thay; G-009 đã miễn ở Tập 1). Sửa: không có câu mang vai = MISSING (không đoán vai).

| # | Ngày · ai | Luật | Chuyện (số đo) | Đề xuất | Tiêu chí đo thay thế | 5 tiêu chí | Trạng thái |
|---|---|---|---|---|---|---|---|
| A3 | 05/10 · Phiên B (lessons F6, `moc-b/SPEED.md`) | toàn bộ bộ chạy | Đo ở Mốc B, Tập 3 không có stem: **56,5 phút**; trong đó bộ lấy mẫu trang **50,0 phút (88 %)**, luật Python 6,5 phút. Tập 3 chạy 5 lần, 60–75 phút mỗi lần | (1) **Bộ lấy mẫu trang song song theo cảnh** (`sampler.js --scenes` đã có) trên 3–4 tiến trình, gộp `page.json`: ước 50 → 15–18 phút. (2) **Cache theo cảnh:** cảnh có băm (dữ liệu + mã trang + khoảng master) không đổi thì dùng lại kết quả trang lần trước. (3) Một lần ASR cho hai họ luật (`r_audio` A14 và `r_sound` mỗi họ tải whisper riêng): cache chép lời theo SHA master | Kết quả mọi luật trên Tập 3 trùng từng số với lần chạy tuần tự (so khớp `report.json`), chỉ thời gian đổi | tốc độ ↑↑ (ước 56 → ~20 phút; lần chạy lại còn ít hơn); chất lượng = (cùng định nghĩa); chi phí máy ↓; K phải viết và khoá lại | K nhận (K3.8) — chờ chủ dự án duyệt |

> **K3.8 — CHẤP NHẬN.** (1) `sampler.js --jobs N` (mặc định `run.sh`: min(4, lõi)): mỗi cảnh là một việc, khôi phục trạng thái tuần tự mang vào cảnh (hộp chữ và claim hiện ở mẫu trước, va chạm chữ đang đi ở mẫu điểm ảnh có chữ gần nhất), gộp theo thứ tự thời gian. (2) Cache theo cảnh: băm mã sampler + đầu vào tập + khung + gói video từ keyframe trước tới keyframe sau cảnh; file trang đã nạp kiểm lại SHA khi đọc. (3) Một model whisper dùng chung (`common.whisper()`); bản chép lời vẫn cache theo SHA master. **Điều kiện đạt:** Tập 3, mọi luật trùng từng số với bản tuần tự — xem `checks-runs/K38/ep003-compare.md`. Thời gian: __A3TIME__.

| # | Ngày · ai | Luật | Chuyện (số đo) | Đề xuất | Tiêu chí đo thay thế | 5 tiêu chí | Trạng thái |
|---|---|---|---|---|---|---|---|
| A4 | 05/10 · Phiên B (D-006 bổ sung) | S14 (DX-S10), F07, S15 | Định dạng mới: `lab` 9–11 phút, 2 mid-roll; `101` 8–9 phút, 1 mid-roll; mid-roll không trong 2 phút đầu/cuối. Hiện tại: S14 đòi 2–3 điểm; S15 đòi tổng ≥ 600 s (Tập 3: 572 s, FAIL tham khảo); F07 8–15 phút | S14 đọc `format` trong `contract.json`: `lab` = 2 điểm, `101` = 1 điểm; thêm: mỗi điểm ≥ 120 s từ đầu và ≥ 120 s trước cuối. S15 "total" theo `format` (lab ≥ 540 s; 101: không có sàn, vì luật "không độn"). F07 giữ trần 900 s | Như S14 hiện tại (ranh giới hồi ±1 s, khoảng lặng ≥ 1 s) + hai khoảng cách 120 s | mở rộng ↑ (hai định dạng); chất lượng ↑ (không độn); tốc độ = | K nhận (K3.8) — chờ chủ dự án duyệt |

> **K3.8 — CHẤP NHẬN.** `contract.json format` (`lab`/`101`; không có = lab, cho Tập 1–3). S14: lab 2 điểm, 101 1 điểm, mỗi điểm ≥ 120 s từ đầu và ≥ 120 s trước cuối (giữ ranh giới hồi ±1 s, khoảng lặng ≥ 1 s). S15: tổng lab ≥ 540 s, 101 không sàn ("không độn"). F07 giữ 480–900 s (CHÍNH). Cả hai vẫn THAM KHẢO (tay nghề).

| # | Ngày · ai | Luật | Chuyện (số đo) | Đề xuất | Tiêu chí đo thay thế | 5 tiêu chí | Trạng thái |
|---|---|---|---|---|---|---|---|
| A5 | 05/10 · Phiên B (D-006 Q3) | mới (Shorts) | Từ Tập 4 mỗi tập 2–3 Shorts 9:16; chưa có luật nào cho file dọc | Bộ luật Shorts: 1080×1920, ≤ 60 s; −14 LUFS ±1, ≤ −1 dBTP; chữ ≥ 56 px (thiết kế 1080×1920); không chữ trong 200 px trên / 320 px dưới (giao diện YouTube); khung có số → ILLUSTRATIVE (nếu claim minh hoạ) và "history, not a forecast" (nếu claim lịch sử); số trên hình là claim; S10 (khuyên) áp nguyên | Lấy mẫu trang như bản ngang, trên trang dựng khổ dọc | chất lượng ↑; mở rộng ↑; tốc độ: thêm ≈ 1–2 phút checks mỗi Short | K nhận (K3.8) — chờ chủ dự án duyệt |

> **K3.8 — CHẤP NHẬN CÓ SỬA.** `contract.json shorts:[{file}]` (bắt buộc khi có `format`). Luật mới: **SH01** 1080×1920 H.264 + AAC, **SH02** ≤ 180 s (giới hạn Shorts của YouTube từ 10/2024; > 60 s chỉ báo), **SH03** −14 ± 1 LUFS, **SH04** ≤ −1 dBTP, **SH05** ASR của Short qua danh sách S10 (không khuyên/dự báo) — cả năm CHẶN (kỹ thuật file, âm lượng, gen bảo vệ). Sửa: cỡ chữ ≥ 56 px, vùng giao diện 200/320 px và nhãn ILLUSTRATIVE/"history, not a forecast" trên khung **hoãn** tới khi trang dọc của nhà máy có `window.CHECKS` (A8). Chạy thật trên Short mẫu S04: **5/5 ĐẠT** (1080×1920 H.264 + AAC; 42,1 s; −13,8 LUFS; −1,5 dBTP; 0 câu khuyên/dự báo; 24 s), `checks-runs/K38/short-S04.json`.

| # | Ngày · ai | Luật | Chuyện (số đo) | Đề xuất | Tiêu chí đo thay thế | 5 tiêu chí | Trạng thái |
|---|---|---|---|---|---|---|---|
| A6 | 05/10 · Phiên B | V11, C05 | Tập 3: hai lỗi CHÍNH (nhãn chạm đầu vạch ~30 px; số 52.3 % màu warn), chủ dự án giữ ở C6 | Không đổi luật. Ghi để K biết: theo nguyên tắc tốc độ (D-006), CHÍNH không đổi nghĩa vào hàng chờ, không mở vòng sửa | — | tốc độ ↑ | ghi nhận |

> **K3.8 — GHI NHẬN.** Không đổi luật; V11, C05 giữ CHÍNH.

| # | Ngày · ai | Luật | Chuyện (số đo) | Đề xuất | Tiêu chí đo thay thế | 5 tiêu chí | Trạng thái |
|---|---|---|---|---|---|---|---|
| A7 | 05/10 · Phiên nhà máy (`toolkit/factory/qc.py`) | mới (đứng hình khi có lời) | qc nhà máy đo `freezedetect` n = −60 dB, d = 3 s giao khoảng có lời. Đối chứng cùng chủ đề: **bản phát hành Tập 3, cảnh S04: 66,8 s / 72 s bị coi là đứng** (chỉ chấm nhỏ đổi, cả khung gần như y nguyên); bản nhà máy cùng cảnh: 3,3 s (một đoạn 39,4–42,7 s giữa hai nhãn). Ở −80 dB bản phát hành vẫn 57 s, bản nhà máy 0 s | Chưa thành luật K: hiệu chuẩn trước (CHARTER §4). Đề xuất K đo "khung đứng khi có lời" bằng chênh trên **vùng có đối tượng** (hộp từ bộ lấy mẫu trang) thay vì cả khung, rồi đặt ngưỡng trên 2–3 tập đã duyệt | Khoảng có lời (ASR) ∩ đoạn ≥ 3 s không đối tượng nào đổi hộp/độ mờ | chất lượng ↑ (bắt hình chết khi đang nói); tốc độ: thêm ≈ 1 phút; cần hiệu chuẩn | K nhận (K3.8) — chờ chủ dự án duyệt |

> **K3.8 — CHẤP NHẬN CÓ SỬA: đo, chưa thành luật.** Bộ lấy mẫu ghi `motionTrack` (mốc mọi lần một đối tượng hiện trên khung đổi hộp ≥ 1 px hoặc độ mờ ≥ 0,01). Hiệu chuẩn trên Tập 3 (bản phát hành): __A7RES__. Chưa đặt ngưỡng (CHARTER §4: cần 2–3 tập đã duyệt; Tập 1–2 chạy ở K sau).

| # | Ngày · ai | Luật | Chuyện (số đo) | Đề xuất | Tiêu chí đo thay thế | 5 tiêu chí | Trạng thái |
|---|---|---|---|---|---|---|---|
| A8 | 05/10 · Phiên nhà máy | F06, F07, luật trang | Demo nhà máy là **đoạn trích** (S04, 75 s, chỉ lời, không nhạc). Chạy 16 luật không cần trang: 14 ĐẠT; **F06 TRƯỢT** (AAC 384k của ffmpeg chỉ ra 244 kb/s với tiếng chỉ có lời). 06/10: thêm nhạc nền → F06 ĐẠT 278 kb/s (sát ngưỡng 272), 17/18 ĐẠT; A16 TRƯỢT tham khảo (giống bản phát hành) | `contract.json` có `scope: excerpt` → F07, S14, S15 bỏ qua; F06 đo bitrate khai (`-b:a`) khi tiếng chỉ có lời, hoặc hạ sàn đo cho đoạn trích. Trang nhà máy (`toolkit/factory/page.html`) chưa có `window.CHECKS`: nếu K muốn chấm luật trang trên bản nhà máy thì bên dựng thêm `objects()` từ log engine | Như hiện tại cho bản đủ | tốc độ ↑ (chấm đoạn trích ngay trong vòng dựng); chất lượng = | mở |
