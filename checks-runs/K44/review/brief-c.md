Bạn là REVIEWER độc lập của Crux (Opus). Soát lô K4.4.1 (A29 cache trang theo đoạn, chủ dự án 14/10 chọn (a)) TRƯỚC khi khoá và merge `main`. Chỉ đọc. Không agent con. Mỗi lệnh Bash là MỘT lệnh. Không in biến môi trường. Không chạy bộ lấy mẫu trên tập thật (nặng).
Đọc: `checks-runs/K44/a29/ANSWER.md` · `checks-runs/K44/a29/RESULT.md`, `result.json`, `ep007-rules-4runs.json`, `runs.jsonl`, `code.sha`, `compare.py` · `git diff origin/main -- checks/` (sampler.js, selftest/test_a29.js, selftest/run.sh, README mục K4.4.1) · `checks-appeal.md` (A29, hàng chờ K4.4).
Soát:
(1) Khoá cache đủ đầu vào không: mã (sampler/objrules/pixels), bước mẫu, timeline/claims/tokens/page.json, contract `claims.conditions`, gói video từ khung khoá, lát `camera.json` (cửa sổ ±3 khung có đủ cho tốc độ máy ở mẫu đầu/cuối cảnh không), đoạn trang (Merkle module + JSON thư mục spine; trang không phải một-file → kiểm cả tệp), trạng thái mang vào `warmState`. Có đầu vào nào luật đọc mà khoá thiếu (vd `contract.json` ngoài `conditions`, `characters`, `design/tokens.json`, phông) để cache trả kết quả cũ sai?
(2) `warmState` có tái tạo đúng trạng thái `sampleJob` cũ dùng (so với mã `main` trước A29: khối `if (warm && …)` cũ) — cùng phép tính, cùng thứ tự?
(3) `try … finally` không đổi số đo; `close()` đóng ống + SIGKILL.
(4) Tiêu chí (a) được đo đúng: Tập 6 trùng byte (bỏ 2 trường đo lượt + chuẩn hoá UUID blob — có che lệch thật không?), Tập 7 ấm = cache trống từng byte, 33 luật trùng mọi chỉ số trên 4 lượt. Mã khoá khác mã đo ở chỗ nào (chỉ chặn ffprobe + try/finally)?
(5) Selftest `test_a29.js` (7 ca) có kiểm đúng "đổi một đoạn → chỉ đoạn đó đổi khoá"; README K4.4.1 khớp mã.
Trả về: **ĐẠT / ĐẠT có sửa / TRƯỢT**; CHẶN / CHÍNH / PHỤ (tệp:dòng, vấn đề, sửa nguyên văn). ≤ 30 dòng.
