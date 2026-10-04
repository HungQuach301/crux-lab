# C3 — Ý đồ kiểm mù hình "cổng gốc" trên style frame (ghi TRƯỚC khi chạy, commit trước; không sửa sau khi thấy kết quả)

Ngày 2026-10-04. Bản 1. Cổng **GU** (`quality-framework.md` v2 §4 C3): kiểm mù chỉ để biết style frame có tự mang ý không, **trước khi gửi gói**; chủ dự án quyết. Giao thức §5.6–5.8. Nguyên văn trả lời: `gates/C3-blind.md`. Gộp điểm: `gates/C3-tally.md` (`packets.py tally --threshold 1 --classes story/beats-class.json`).

## Mẫu
- **Style frame có chuyển động** cho 6 nhịp loại 1 (KEY-1, 2, 4, 5, 6, 7) + KEY-3 (loại 2, chỉ kiểm câu khuyên). Nguồn: `design/c3/src/scenes.js`, render 1280×720, 30 fps, **tắt tiếng**, **giữ chữ/số** (D-005 Q3). Ghép thành một cuộn `design/c3/work/stylereel.mp4` (không commit; SHA-256 ghi vào `review-c3/r1/strips.json`).
- Dải: `toolkit/blind/strips.py stylereel.mp4 spans.json` — 6 khung tâm 6 lát bằng nhau trong mỗi clip; lưới 3×2 đánh số. Không chọn khung tay.
- Bảng phân loại: `story/beats-class.json` SHA-256 `2299ddf5…` (issue #27). Không đổi.
- **Không có đối chứng** ở vòng này: dải đối chứng đã biết kết quả nằm trong thư mục tập cũ (phiên không được đọc; `episode.md` §1), ảnh xem trước của thư viện là ảnh tĩnh (G-011 cấm duyệt hình bằng ảnh tĩnh). Bộ đo "cổng gốc" đã hiệu chuẩn ở Tập 2 (C4b). Ghi rủi ro này trong gói.

## Người đọc
Mỗi (nhịp, lượt) một agent MỚI (sonnet), chỉ mở **một PNG tên hex** (`packets.py deal`), không ngữ cảnh dự án. Vai đích (cùng vai T của C1/C2): *"You are an American in your 40s with savings you will not need for about 20 years; right now the money sits in a bank account or short-term Treasury bills."*

**Câu hỏi cố định (tiếng Anh, giống nhau cho mọi mẫu):**
> The image shows six numbered frames, in order, taken from a short silent animation in a personal-finance video. Look only at the image. Answer in plain sentences:
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
| KEY-3 | 2 | (không chấm nghĩa — cột muted read để trống ở C2; chỉ cờ câu khuyên) |

"Chỉ tả hình" (cho người chấm): câu trả lời kể vật thấy được (chấm, cột, vạch, chữ) mà không nói chúng nghĩa là gì so với ý trên.

## Luật đếm (ghi trước; mặc định `packets.py`)
- Một người đọc **đúng** = điểm 1 **và** không cờ khuyên.
- **Dừng sớm:** 2 người đầu cùng kết quả → xong (2/2 đạt, 0/2 trượt); lệch → người thứ 3 (`packets.py next` → `deal --slots 3 --only …`); nhịp đạt khi ≥ 2/3 đúng.
- **Có câu khuyên ở bất kỳ nhịp nào (kể cả KEY-3) → nhịp đó trượt ngay.**
- Ngưỡng C3 (`--threshold 1`): **mỗi** nhịp loại 1 đạt (≥ 2/3, khuyên 0).
- ±5% quanh ngưỡng: không áp dụng được với 2–3 người đọc; mọi nhịp đạt bằng 2/3 (không phải 2/2) được nêu tên trong gói.

## Vòng và dự phòng (ghi trước, `quality-framework.md` §4 C3)
- Tối đa **2 vòng mỗi nhịp**, trước khi gửi gói. Vòng 2 chỉ cho nhịp trượt: thêm **nhãn nghĩa** (≤ ~8 từ, ≥ 40 px, hiện ≥ 1 s cho mỗi 3 từ; không thêm vật, không thêm số ngoài claim), người đọc **mới**, cùng câu hỏi, cùng rubric. Nhịp trượt vì câu khuyên: vòng 2 thêm/siết nhãn đối trọng ("Not a pick. What history did.") thay cho nhãn nghĩa.
- Vẫn trượt sau vòng 2 → **hạ nhịp xuống loại 2**, báo trong gói C3 (kèm kiểm lại luật 60% nhịp then chốt loại 1).
- Sửa hình giữa hai vòng chỉ là nhãn (§6.6). Mọi đổi khác (vật, màu, bố cục) là gu → gói C3.
