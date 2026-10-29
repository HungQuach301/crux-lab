# market/ — dữ liệu thị trường (Phiên Thị trường `market-r1`, 11/10/2026)

Kênh mạnh cùng chủ đề và video vượt trội cho tài chính cá nhân Mỹ (vay nợ · hưu trí/đầu tư · thuế), nhúng vào quy trình tập **không thêm cổng, phiên hay lượt chạm** của chủ dự án (`playbook/episode.md` §1b, §5c, §10).

| Tệp | Nội dung |
|---|---|
| `REPORT.md` | báo cáo định tính: đề tài theo cầu, khoảng trống, mẫu tiêu đề/thumbnail, dải thời lượng, câu hỏi khán giả, khuyến nghị Tập 7 + 8 |
| `CHANNELS.md` | danh sách kênh theo ba vòng tròn + mới nổi (thử việc 90 ngày) + đã loại, kèm lý do |
| `topics/<id>.md` | hồ sơ cầu mỗi đề tài (mức cầu, khoảng trống, 5 câu hỏi, 3 hoàn cảnh, điểm yếu đối thủ, dải thời lượng, video đối thủ, mẫu tiêu đề) · `labels.json` nhãn cho cột Cầu/Khoảng trống của `topics/queue.md` |
| `teardowns/` | mổ xẻ video hạt giống của chủ dự án (chỉ phân tích, không chép lời) |
| `R3-VIRAL-NEW.md` · `r3/` | R3 (29/10): video dài ≥ 1M trong 7 ngày của kênh ≤ 31 ngày tuổi, số thô ở `r3/*.json` (ngoại lệ luật dữ liệu bên dưới) |
| `CALIBRATION.md` | vòng tự hiệu chỉnh: nhãn cầu so với lượt xem 28 ngày của Crux |

**Luật dữ liệu (YouTube API Developer Policies III.E.4; repo public):** số liệu thô của kênh khác (lượt xem, người đăng ký, like, bình luận nguyên văn, tiêu đề, thumbnail, transcript) **không commit**. Chúng ở `~/market-cache/<ngày>/` ngoài git; `python3 toolkit/market/purge.py` xoá thư mục > 30 ngày, làm mới bằng cách chạy lại. Repo chỉ chứa mã (`toolkit/market/`), định danh kênh/video, nhãn (cao/vừa/thấp; ≥ 3×/≥ 5×), kết luận định tính và câu diễn giải lại. Mọi chỉ số tự tính ghi **"tự tính, không phải chỉ số YouTube"**.

**Ngoại lệ R3 (chủ dự án 29/10):** `market/r3/*.json` và các bảng số trong `R3-VIRAL-NEW.md` được commit số thô, lấy ngày 29/10/2026; **hạn làm mới (chạy lại `toolkit/market/r3/`) hoặc xoá: 28/11/2026**.

**Làm lại từ đầu** (≈ 7.700 đơn vị hạn mức, ≈ 67 search; hạn mức 10.000/ngày, ≤ 100 search):
```
python3 toolkit/market/discover.py search && python3 toolkit/market/discover.py aggregate && python3 toolkit/market/discover.py candidates
python3 toolkit/market/pull.py --from ~/market-cache/$(date +%F)/discover/candidates.json
python3 toolkit/market/discover.py classify
for s in tag outliers comments packaging thumbs gap profile; do python3 toolkit/market/analyze.py $s; done
python3 toolkit/market/report.py channels && python3 toolkit/market/report.py topics && python3 toolkit/market/report.py queue
```
AI: Haiku headless (`claude -p`, `ANTHROPIC_API_KEY="$CONSOLE_API_KEY"`) cho phân loại kênh, bình luận, khoảng trống, hồ sơ; Sonnet xem thumbnail bằng URL (không tải, không lưu); embeddings OpenAI `text-embedding-3-small` (`EMBEDDINGS_API_KEY` hoặc khoá proxy môi trường). Chi API ghi ở `~/market-cache/<ngày>/ai-ledger.jsonl`.
