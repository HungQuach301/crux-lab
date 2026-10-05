# Ý đồ — hiệu chuẩn chính thức phép so cặp móc (Tập 4, P1) · ghi TRƯỚC khi chạy, 2026-10-05

**Vì sao:** `episode.md` §3, D-006 bổ sung 2: so cặp móc chỉ được dùng để chọn móc sau hiệu chuẩn chính thức ở P1 Tập 4, ý đồ và ngưỡng ghi trước, **mẫu mới** (không dùng lại dữ liệu Tập 2/3 của Mốc B), bản làm kém = bỏ móc 5 s, cùng kịch bản (lessons F3, F4).

**Phát hiện khi đọc lại Mốc B (trước khi chạy):** trong `moc-b/cal-engagement/key.json`, bản gốc nằm ở vị trí **X** trong 5/6 cặp, và cả 6 người đọc đều chọn X. Kết quả 6/6 vì thế **không tách được** khỏi thiên lệch vị trí. Lần này thứ tự được cân bằng và có ngưỡng riêng cho vị trí.

## Câu hỏi
Người đọc mù (Sonnet, agent mới mỗi mẫu, không ngữ cảnh dự án), đọc ~30 s lời đầu của hai bản cùng kịch bản, có chọn bản có móc theo `story.md` §1 (5 s đầu được–mất hoặc câu hỏi; lời hứa trước 0:30) **hơn** bản bỏ móc không, **bất kể vị trí**?

## Mẫu mới (nguyên văn ở `samples.md`)
- **A — Tập 1 (ep001), lời thật đã phát hành** (Tập 1 không có trong Mốc B). Gốc = câu S01.1–S01.5 (0:00–0:33; câu được–mất "$459 a month… She didn't take it."). Làm kém = mở bằng câu bối cảnh có thật của chính tập (S03.1, S03.2, S04.1): không câu được–mất, câu hỏi hay lời hứa; cùng dữ kiện, độ dài ±15 %.
- **B — kịch bản mới cho đề tài #2 hàng đợi (tax-4, overtime hay việc thứ hai)**, phiên điều phối viết theo `story.md` §1 từ số của hồ sơ (`topics-r1/machine/tax-4/result.json`). Không phải đề tài Tập 4. Làm kém = mở bằng luật và định nghĩa trung tính; bỏ câu hỏi, được–mất và lời hứa khỏi 30 s đầu; cùng dữ kiện, ±15 %.
- Người viết mẫu không là người đọc. Phiên điều phối chỉ chia mẫu, gộp số.

## Người đọc và câu hỏi
- Mỗi mẫu **4 người đọc**: 2 người thấy bản gốc ở vị trí X, 2 người ở vị trí Y (`deal.py`, khoá `key.json` commit trước khi đọc). Tổng **8 agent**.
- Vai theo khán giả đích của mẫu (A: chủ nhà Mỹ 30–55 tuổi đang trả góp; B: người làm công theo giờ ở Mỹ 25–50 tuổi). Câu hỏi giữ nguyên Mốc B (`reader-pair.txt`): KEEP X/Y, STRENGTH 1–3, WHY.
- **Câu thứ hai, tách riêng, THAM KHẢO:** so cặp tiêu đề nháp Tập 4 một vòng (`episode.md` §5; mỗi người một cặp, thứ tự cân bằng). Câu này đứng **sau** KEEP, không tính vào hiệu chuẩn; gộp vào đây để tiết kiệm agent (trần 60 agent cả tập).

## Ngưỡng (ghi trước)
Phép so cặp móc **ĐẠT** khi đủ cả ba:
1. Chọn bản gốc **≥ 7/8** (ngẫu nhiên p = 0,5: P(≥ 7/8) ≈ 3,5 %);
2. Mỗi mẫu **≥ 3/4**;
3. **Vị trí:** khi bản gốc ở Y, chọn gốc **≥ 3/4** (và khi ở X ≥ 3/4).
Trong ±5 % quanh ngưỡng: không áp dụng được cho số đếm nguyên; mọi kết quả đúng bằng ngưỡng (7/8, 3/4) được nêu tên trong gói.

## Hệ quả (ghi trước)
- **ĐẠT** → chọn móc Tập 4 bằng so cặp vòng tròn: 3 phương án × 3 cặp × 3 người đọc mới (9 agent), vai khán giả đích Tập 4, thứ tự trong mỗi cặp xoay (2–1 rồi 1–2), phương án thắng nhiều lượt nhất được chọn; hoà → WRITER + REVIEWER chọn trong số hoà.
- **TRƯỢT** → giữ cách WRITER + REVIEWER (REVIEWER chấm theo `story.md` §1, lý do một dòng); ghi vào `lessons.md` ở tổng kết.
- **Giới hạn đã biết:** hiệu chuẩn chỉ chứng minh phép đo phân biệt *có móc / bỏ móc*. Nó không chứng minh phân biệt được giữa ba móc đều tốt (việc thật ở Tập 4). Số giữ chân YouTube vẫn là thước đo thật.

## Không làm
Không sửa ý đồ sau khi thấy kết quả; không chạy thêm người đọc để cứu; nguyên văn trả lời ở `answers.jsonl`, gói chỉ đưa bảng `RESULT.md`.
