# C3 — Ý đồ kiểm mù cổng gốc trên style frame N1, N2 (ghi TRƯỚC khi chạy; không sửa sau khi thấy kết quả)

Ngày 2026-10-06, phiên P2. Cổng **GU** chỉ cho 2 ký hiệu mới G1 đã mở (`gates/G1-answer.md` câu 3). Giao thức `quality-framework.md` §5.6–5.8, mẫu ý đồ Tập 3 (`episodes/ep003/gates/C3-intent.md`). Nguyên văn trả lời: `gates/C3-blind.md`. Gộp điểm: `gates/C3-tally.md`.

## Mẫu
- Style frame **có chuyển động**, dựng bằng nhà máy (`bash toolkit/build.sh episodes/ep004/episode.yaml`, scope excerpt: S08, S13, S14), 1080p 30 fps, **tắt tiếng**, **giữ chữ/số** (D-005 Q3). Mã mới chỉ là N1, N2 (`design/c3/`); phần còn lại là mẫu thư viện.
- Dải 6 khung (`toolkit/blind/strips.py`), lưới 3×2 đánh số, spans theo độ dài cảnh (không đo tay).
- Bảng phân loại nhịp: `story/beats.md` (C2 v2, báo ở G1). Không đổi; dự phòng hạ loại chỉ ghi trong gói.

| Nhịp | Ký hiệu | Loại | Đúng nghĩa (chép nguyên văn cột "muted read" của `story/beats.md`) |
|---|---|---|---|
| B08 · KEY-3 | N1 inflation shadow | 1 | "The cap stayed flat since 1997, while the same cap, kept up with consumer prices, would now be about $1,046,000." |
| B13 | N2 (thước giá, bậc Phoenix) | 1 (không then chốt) | "There is one purchase price where the gain lands exactly on the cap; the couple's price sits above it, so their line is over." |
| B14 · KEY-6 | N2 threshold ladder | 1 | "Each city has its own 2000 purchase price above which the gain passes the cap; those prices run from about $114,700 in Miami to about $373,400 in Chicago, and all but Chicago sit under the $300,000 line." |

## Người đọc
Mỗi (nhịp, lượt) một agent MỚI (sonnet), chỉ mở một PNG tên hex, không ngữ cảnh dự án. Câu hỏi cố định, giống nhau cho mọi mẫu (vai T của C1/C2):
> You are an American in your late 50s or 60s, married, who bought your home around 2000 and has started thinking about selling it to downsize. The image shows six numbered frames, in order, taken from a short silent animation in a personal-finance video. Look only at the image. Answer in plain sentences:
> 1. What idea is this animation showing?
> 2. What changes over time across the frames?
> 3. What does it mean?
> 4. What advice, if any, would a viewer take from this?

## Chấm (người chấm độc lập, mù tập)
Nhãn ngẫu nhiên; khoá nhãn ghi trước khi chấm. **1** = nêu đúng ý "đúng nghĩa" (diễn đạt khác được, đủ các vế; số làm tròn gần đúng được); **0,5** = đúng vật, thiếu một vế nghĩa; **0** = chỉ tả hình hoặc sai nghĩa. `advice: true` khi có lời khuyên hành động, kể cả có điều kiện ("sell before…", "you will owe tax", "keep records to lower the gain", "talk to a tax pro"). "No advice / just information / depends" → không tính. **Đọc ngưỡng thành số thuế phải nộp** ghi riêng (luật tập K-brief 3), tính như sai nghĩa.

## Luật đếm
- Một người đọc **đúng** = điểm 1 và không cờ khuyên.
- Dừng sớm: 2 người đầu cùng kết quả → xong; lệch → người thứ 3; nhịp đạt khi ≥ 2/3. Câu khuyên ở bất kỳ nhịp nào → nhịp trượt.
- Ngưỡng C3: **mỗi** nhịp trong bảng đạt. Nhịp đạt bằng 2/3 được nêu tên trong gói.

## Vòng và dự phòng
- Tối đa 2 vòng mỗi nhịp, trước khi gửi gói. Vòng 2 chỉ cho nhịp trượt: **nhãn nghĩa** (≤ ~8 từ, ≥ 40 px, ≥ 1 s/3 từ; không thêm vật, không thêm số ngoài claim), người đọc mới, cùng câu hỏi, cùng rubric. Trượt vì câu khuyên → vòng 2 siết nhãn đối trọng thay nhãn nghĩa.
- Vẫn trượt sau vòng 2 → hạ nhịp xuống loại 2, báo trong gói. Then chốt loại 1 hiện 6/7 = 86 %: hạ KEY-3 hoặc KEY-6 → 5/7 = 71 % (đạt 60 %); hạ cả hai → 4/7 = 57 % < 60 % → nêu ở gói, chủ dự án quyết.
- Sửa giữa hai vòng chỉ là nhãn. Đổi vật, màu, bố cục là gu → gói C3.
