# Ý đồ — hiệu chuẩn chính thức phép so cặp móc (Tập 4, P1) · ghi TRƯỚC khi chạy, 2026-10-05

**Bản 2 — sửa theo REVIEWER trước khi chạy** (`gates/REVIEW-intents.md` §1, chưa có kết quả nào).

**Vì sao:** `episode.md` §3, D-006 bổ sung 2: so cặp móc chỉ được dùng để chọn móc sau hiệu chuẩn chính thức ở P1 Tập 4, ý đồ và ngưỡng ghi trước, **mẫu mới** (không dùng lại dữ liệu Tập 2/3 của Mốc B), bản làm kém = bỏ móc 5 s, cùng kịch bản (lessons F3, F4).

**Phát hiện khi đọc lại Mốc B (trước khi chạy):** trong `moc-b/cal-engagement/key.json`, bản gốc nằm ở vị trí **X** trong 5/6 cặp; 6/6 chọn gốc, nhưng chỉ 1 cặp có gốc ở Y (người đó chọn Y). Với n = 1, kết quả 6/6 **chưa tách được** khỏi thiên lệch vị trí. Lần này thứ tự được cân bằng (2 X / 2 Y mỗi mẫu).

## Câu hỏi
Người đọc mù (Sonnet, agent mới mỗi mẫu, không ngữ cảnh dự án), đọc ~30 s lời đầu của hai bản cùng kịch bản, có chọn bản có móc **hơn** bản bỏ móc (cùng kịch bản, móc dời ra sau 30 s) không, **bất kể vị trí**? Mẫu A kiểm *móc được–mất không có lời hứa trước 0:30* (bản đã phát hành, yếu hơn story §1); mẫu B kiểm *móc đủ `story.md` §1* (câu hỏi trong 5 s đầu, lời hứa trước 0:30).

## Mẫu mới (nguyên văn ở `samples.md`)
- **A — Tập 1 (ep001), lời thật đã phát hành** (Tập 1 không có trong Mốc B). Gốc = câu S01.1–S01.5 (0:00–0:33; câu được–mất "$459 a month… She didn't take it."). Làm kém = mở bằng câu bối cảnh có thật của chính tập (S03.1, S03.2, S04.2), móc dời ra sau 30 s (Op1 Mốc B, `moc-b/cal-engagement/DEGRADE-NOTES.md`); cùng kịch bản, độ dài ±15 % (66/66 từ).
- **B — kịch bản mới cho đề tài #2 hàng đợi (tax-4, overtime hay việc thứ hai)**, phiên điều phối viết **một kịch bản liền mạch 8 câu** theo `story.md` §1 từ số của hồ sơ (`topics-r1/machine/tax-4/result.json`). Không phải đề tài Tập 4. Gốc = thứ tự b1…b8; làm kém = b5…b8 rồi b1…b4 (câu luật lên đầu, móc dời ra sau 30 s); 66/64 từ.
- Người viết mẫu không là người đọc. Phiên điều phối chỉ chia mẫu, gộp số.

## Người đọc và câu hỏi
- Mỗi mẫu **4 người đọc**: 2 người thấy bản gốc ở vị trí X, 2 người ở vị trí Y (`deal.py`, khoá `key.json` commit trước khi đọc). Tổng **8 agent**.
- Vai theo khán giả đích của mẫu (A: chủ nhà Mỹ 30–55 tuổi đang trả góp; B: người làm công theo giờ ở Mỹ 25–50 tuổi). Câu hỏi giữ nguyên Mốc B (`reader-pair.txt`): KEEP X/Y, STRENGTH 1–3, WHY.
- Không gộp câu tiêu đề (REVIEWER: vai sai). Tiêu đề Tập 4 so riêng với vai đích Tập 4.

## Ngưỡng (ghi trước)
Phép so cặp móc **ĐẠT** khi đủ cả ba:
1. Chọn bản gốc **≥ 7/8** (ngẫu nhiên p = 0,5: P(≥ 7/8) ≈ 3,5 %);
2. Mỗi mẫu **≥ 3/4**;
3. **Vị trí:** khi bản gốc ở Y, chọn gốc **≥ 3/4** (và khi ở X ≥ 3/4).

Ghi chú (REVIEWER): ngưỡng 2 và 3 bị ngưỡng 1 kéo theo (≥ 7/8 thì mọi nhóm 4 người ≥ 3/4). Bảo vệ khỏi thiên lệch vị trí thực chất đến từ **cân bằng thứ tự**; ngưỡng 3 chỉ làm rõ điều đó trong bảng kết quả.
Trong ±5 % quanh ngưỡng: không áp dụng được cho số đếm nguyên; mọi kết quả đúng bằng ngưỡng (7/8, 3/4) được nêu tên trong gói.

## Hệ quả (ghi trước)
- **ĐẠT** → chọn móc Tập 4 bằng so cặp vòng tròn: 3 phương án × 3 cặp × 3 người đọc mới (9 agent), vai khán giả đích Tập 4, thứ tự trong mỗi cặp xoay (2–1 rồi 1–2), phương án thắng nhiều lượt nhất được chọn; hoà → WRITER + REVIEWER chọn trong số hoà.
- **TRƯỢT** → giữ cách WRITER + REVIEWER (REVIEWER chấm theo `story.md` §1, lý do một dòng); ghi vào `lessons.md` ở tổng kết.
- **Giới hạn đã biết:** mẫu A là móc yếu hơn móc Tập 4 (không lời hứa trước 0:30). Hiệu chuẩn chỉ chứng minh phép đo phân biệt *có móc / bỏ móc*. Nó không chứng minh phân biệt được giữa ba móc đều tốt (việc thật ở Tập 4). Số giữ chân YouTube vẫn là thước đo thật.

## Không làm
Không sửa ý đồ sau khi thấy kết quả; không chạy thêm người đọc để cứu; nguyên văn trả lời ở `answers.jsonl`, gói chỉ đưa bảng `RESULT.md`.
