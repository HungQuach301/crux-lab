# C3b — Kiểm mù KEY-7 phương án (A) · một vòng (01/10/2026)

Ý đồ: `gates/C3-K7-intent-r3.md` (commit 7f6814a). Mẫu: `design/c3/final/K7-A-strip-masked.png` (lúc chạy tên là K7-strip-masked.png, commit 5210681). Khoá: `review-c3/k17/key-r3.json`.

## Nguyên văn

**ab384b8b** (KEY-7): The section shows one loan panel at first, with a long flat line and a mostly full grid of red squares. New panels are added one at a time, and each shows a teal block that grows larger while its grid of red squares shrinks. This looks like loan interest or balance building up over time (teal) while the unpaid balance (red) drops, or it may compare repayment periods or loans. I can't be certain without the text, but the basic idea is that the debt shrinks while the accumulated amount grows.

**f58e8646** (KEY-7): The section shows a loan being repaid or refinanced in successive stages: each new panel adds a teal bar (a growing amount, perhaps accumulated interest or a new loan balance) alongside two calendar-style grids of red squares (time units, perhaps years or months). The red squares get steadily fewer from panel to panel. The likely meaning is that as time passes, the original debt's repayment period shrinks while a larger balance builds up in each later stage, as with interest capitalizing on a loan. I can't be sure, because all labels are hidden.

**3a0d8b32** (KEY-7): The section shows a loan being repaid over successive periods: the first account has a large red balance (red squares, which look like unpaid dollars or months) that shrinks. Meanwhile, new accounts (green interest-accrual blocks) appear alongside it, and their own red balances start small. My reading is that interest compounds and gets added to the loan, so the debt grows or gets pushed forward while it is being paid down, and the growing green blocks show how much interest accrues on top of the principal. I'm not fully certain, because all the text is covered.

## Chấm
| Người đọc | (i) khoảng chênh lớn hơn → ít đỏ hơn | (ii) một thùng sạch, thùng kia còn đỏ | Kết |
|---|---|---|---|
| ab384b8b | ✗ "teal grows, red shrinks", nhưng hiểu là trả nợ/tích luỹ | ✗ | sai |
| f58e8646 | ✗ đọc ô vuông đỏ là đơn vị thời gian, nhập lãi | ✗ | sai |
| 3a0d8b32 | ✗ đọc là trả nợ và lãi cộng dồn | ✗ | sai |

**0/3 → TRƯỢT.** Theo lệnh C3b: dùng **(B)**, tức bản r2 (`K7.mp4` = `K7-r2.mp4`); phương án A giữ ở `K7-A.*`. Không thêm vòng.
Nhận xét: các ô tĩnh vẫn bị đọc thành **chuỗi thời gian**, vì hiện lần lượt và khối xanh to dần từ ô này sang ô sau. Khi tắt tiếng, "khoảng chênh lúc đầu" chưa từng được đọc ra ở bất kỳ vòng nào (C3, r1, r2, A). Ý đó phải do lời mang.

## Rủi ro cho C4 (ghi rõ theo lệnh)
Ngưỡng C4 là điểm trung bình 21 lượt ≥ 0,70 (tổng ≥ 14,7). KEY-7 qua 4 vòng đạt 0–0,5 mỗi người đọc. Nếu KEY-7 được khoảng 0,5/3, sáu nhịp còn lại phải đạt trung bình ≥ 0,79 (≥ 14,2/18). Ở C3, nhịp tốt nhất đạt 2–3/3, nhưng KEY-2/KEY-4/KEY-5 chưa từng thử trên hệ cuối. Nếu C4 trượt chỉ vì KEY-7, P sẽ báo hai số: có và không có KEY-7. P không tự hạ ngưỡng.
