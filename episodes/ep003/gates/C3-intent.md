# C3 — Ý đồ kiểm mù hình "cổng gốc" trên style frame (ghi TRƯỚC khi chạy, commit trước; không sửa sau khi thấy kết quả)

Ngày 2026-10-04. **Bản 2 — sửa theo REVIEWER trước khi chạy** (0 CHẶN, 7 CHÍNH, 4 THAM KHẢO; bản 1 `7ad76b3`). SHA đầu vào khoá ở mục cuối. Cổng **GU** (`quality-framework.md` v2 §4 C3): kiểm mù chỉ để biết style frame có tự mang ý không, **trước khi gửi gói**; chủ dự án quyết. Giao thức §5.6–5.8. Nguyên văn trả lời: `gates/C3-blind.md`. Gộp điểm: `gates/C3-tally.md` (`packets.py tally --threshold 1 --classes story/beats-class.json`).

## Mẫu
- **Style frame có chuyển động** cho 6 nhịp loại 1 (KEY-1, 2, 4, 5, 6, 7) + KEY-3 (loại 2, chỉ kiểm câu khuyên). Nguồn: `design/c3/src/scenes.js`, render 1280×720, 30 fps, **tắt tiếng**, **giữ chữ/số** (D-005 Q3). Ghép thành một cuộn `design/c3/work/stylereel.mp4` (không commit; SHA-256 ghi vào `review-c3/r1/strips.json`).
- Dải: `python3 toolkit/blind/strips.py design/c3/work/stylereel.mp4 review-c3/r1/spans.json review-c3/r1/strips` — 6 khung tâm 6 lát bằng nhau trong mỗi clip; lưới 3×2 đánh số. Spans lấy từ **độ dài clip** (KEY-1 10 s, KEY-2 10, KEY-3 8, KEY-4 12, KEY-5 10, KEY-6 12, KEY-7 12, CTRL 8; nối liền theo thứ tự này), không đo tay. `stripTimes` trong `scenes.js` **không** dùng để cắt dải; tự kiểm chữ (`render.js --check`) chạy đúng tại 6 thời điểm `strips.py` sẽ cắt.
- Bảng phân loại: `story/beats-class.json` SHA-256 `2299ddf5…` (issue #27). Không đổi; `tally --classes` chạy trên chính file này kể cả khi dự phòng hạ loại (hạ loại chỉ ghi trong gói, không sửa file).
- **Đối chứng `ctrl:V4`** (không tính vào cổng): ký hiệu V4 "một người, hai lời mời" của thư viện, chép nguyên văn `toolkit/visual-library/code/d2/k1.js` (`design/c3/ctrl/`), dữ liệu dựng lại từ cùng file TB3MS ghim (`ctrl/build_ctrl.py`). Kết quả đã biết (README thư viện): Tập 2 KEY-1 cổng gốc v1 **3/3**, v2 3/3 nhưng **khuyên 1**. Rubric "đúng nghĩa" = cột "Mang nghĩa" của README, dịch sát sang tiếng Anh (bản gốc tiếng Việt): *"One person is weighing two loans: one fixed, and one variable that starts lower."* Đọc kết quả: đối chứng đạt mà ứng viên trượt → "ứng viên thua" (bộ đo dùng được); đối chứng trượt → ghi "bộ đo không xác nhận được ở lượt này" trong gói. Người đọc đối chứng dùng cùng câu hỏi (vai của tập này) — lệch vai là chủ ý: câu hỏi cố định cho mọi mẫu.

## Người đọc
Mỗi (nhịp, lượt) một agent MỚI (sonnet), chỉ mở **một PNG tên hex** (`packets.py deal`), không ngữ cảnh dự án. Vai đích (cùng vai T của C1/C2) nằm **trong** chuỗi `question` của manifest (`deal` chỉ gửi chuỗi đó), nên giống hệt cho mọi mẫu.

**Câu hỏi cố định (tiếng Anh, giống nhau cho mọi mẫu; đúng chuỗi `question` của `review-c3/r1/manifest.json`):**
> You are an American in your 40s with savings you will not need for about 20 years; right now the money sits in a bank account or short-term Treasury bills. The image shows six numbered frames, in order, taken from a short silent animation in a personal-finance video. Look only at the image. Answer in plain sentences:
> 1. What idea is this animation showing?
> 2. What changes over time across the frames?
> 3. What does it mean?
> 4. What advice, if any, would a viewer take from this?

## Chấm (người chấm độc lập, mù tập)
Gói nhãn ngẫu nhiên (`packets.py packet`); khoá nhãn commit **trước** khi chấm. Mỗi câu trả lời: **1** = nêu đúng ý "đúng nghĩa" bên dưới (diễn đạt khác được, đủ các vế); **0,5** = đúng một phần (đúng vật, thiếu một vế nghĩa); **0** = chỉ tả hình hoặc sai nghĩa. `advice: true` khi câu 4 (hay bất kỳ chỗ nào) nêu **lời khuyên hành động**, kể cả có điều kiện ("buy the bond", "lock in", "avoid T-bills", "the bond is safer", "if rates fall, choose…"). "No advice / it depends on the viewer / just information" → không tính.

**"Đúng nghĩa" = chép nguyên văn cột "muted read" của `story/beats.md` (C2):**
| Nhịp | Loại | Đúng nghĩa (nguyên văn) |
|---|---|---|
| KEY-1 | 1 | "A person is choosing between two ways to park money for 20 years: a chain of short bills, or a bond that is guaranteed to reach ×2 at year 20." |
| KEY-2 | 1 | "Almost the whole history shown is a what-if (hatched, 'IF today's guarantee had existed'); only a short stretch from May 2005 is real." |
| KEY-4 | 1 | "Overall about half of the rolls beat double, but the middle era (1950–1989) nearly always beat it and the starts from 1990 almost never did; the earliest era never did." |
| KEY-5 | 1 | "The only starts where the guarantee was real are a small cluster at the very end, all short of ×2 — tagged 'small sample · one era'; overall about half still beat ×2." |
| KEY-6 | 1 | "Doubling the dollars did not always keep up with prices: often the doubled stack is smaller than the 'price shadow' of what the original money bought; worst case barely over half." |
| KEY-7 | 1 | "There is a threshold on the bill-rate scale just above the long-run average; to beat ×2 the 20-year average rate must land above it, and the marker can land on either side." |
| KEY-3 | 2 | Mục rubric ghi trước: meaning = *"Not scored for meaning (illustration beat); only the advice flag counts."* Điểm nghĩa của KEY-3 không tính vào đâu. |
| ctrl:V4 | đối chứng | *"One person is weighing two loans: one fixed, and one variable that starts lower."* (README thư viện, dịch sát) |

"Chỉ tả hình" (cho người chấm): câu trả lời kể vật thấy được (chấm, cột, vạch, chữ) mà không nói chúng nghĩa là gì so với ý trên.

## Luật đếm (ghi trước; mặc định `packets.py`)
- Một người đọc **đúng** = điểm 1 **và** không cờ khuyên.
- **Dừng sớm:** 2 người đầu cùng kết quả → xong (2/2 đạt, 0/2 trượt); lệch → người thứ 3 (`packets.py next` → `deal --slots 3 --only …`); nhịp đạt khi ≥ 2/3 đúng.
- **Có câu khuyên ở bất kỳ nhịp nào → nhịp đó trượt ngay; ở KEY-3 (loại 2) câu khuyên làm CẢ CỔNG trượt** (§5.8). KEY-3 không hạ loại được: còn câu khuyên sau vòng 2 → gói C3 báo "cổng gốc trượt vì câu khuyên ở KEY-3", chủ dự án quyết.
- Ngưỡng C3 (`--threshold 1`): **mỗi** nhịp loại 1 đạt (≥ 2/3, khuyên 0).
- ±5% quanh ngưỡng: với `--threshold 1`, nếu 6/6 nhịp đạt thì tỉ lệ = 1,0 = ngưỡng và `tally` **sẽ tự in cờ "trong ±5%"** — dự kiến trước, nêu tên trong gói. Mọi nhịp đạt bằng 2/3 (không phải 2/2) cũng được nêu tên.
- Số người đọc: theo dừng sớm §5.6 (2, thêm người thứ 3 khi lệch); câu "3 người đọc mới mỗi nhịp" ở §5.7 hiểu là **tối đa** 3, mỗi vòng người đọc mới.

## Vòng và dự phòng (ghi trước, `quality-framework.md` §4 C3)
- Tối đa **2 vòng mỗi nhịp**, trước khi gửi gói. Vòng 2 chỉ cho nhịp trượt: thêm **nhãn nghĩa** (≤ ~8 từ, ≥ 40 px, hiện ≥ 1 s cho mỗi 3 từ; không thêm vật, không thêm số ngoài claim), người đọc **mới**, cùng câu hỏi, cùng rubric. Nhịp trượt vì câu khuyên: vòng 2 thêm/siết nhãn đối trọng ("Not a pick. What history did.") thay cho nhãn nghĩa.
- Vẫn trượt sau vòng 2 → **hạ nhịp xuống loại 2**, báo trong gói C3. Hạ 1 nhịp → loại 1 còn 5/7 = 71% (đạt luật 60%). **Hạ ≥ 2 nhịp → 4/7 = 57% < 60%**: báo trong gói như việc ngoài danh sách §6, chủ dự án quyết (không tự đổi bảng).
- Sửa hình giữa hai vòng chỉ là nhãn (§6.6). Mọi đổi khác (vật, màu, bố cục) là gu → gói C3.

## Đầu vào khoá (commit trước lệnh `deal`)
Ghi ở `review-c3/r1/inputs.json`: SHA-256 của `design/c3/src/scenes.js`, `design/c3/ctrl/k1.js`, `review-c3/r1/spans.json`, `manifest.json`, `rubric.json`, `stylereel.mp4`, mỗi PNG dải; commit cùng ý đồ này trước khi chia mẫu.
