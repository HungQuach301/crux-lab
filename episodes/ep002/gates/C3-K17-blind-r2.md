# C3 điều kiện (a) — Kiểm mù KEY-1/KEY-7 · vòng 2 (01/10/2026)

Ý đồ: `gates/C3-K17-intent.md` (không đổi). Mẫu + khoá commit trước khi chạy (6d39481, `review-c3/k17/key-r2.json`). 6 người đọc mới, câu hỏi cố định.

## Nguyên văn

**42278f80** (KEY-1): The section compares two documents or accounts (left and right, held up by a figure) against a flat baseline line. On the right, a value starts below the baseline, grows slowly in the green area, then climbs and swings up and down with volatility, ending near or below the baseline again. It seems to show how a balance or investment changes over time: it starts negative (such as a loan balance or debt) and the later ups and downs show that the outcome is uncertain and not a steady rise. I am only moderately sure of this reading, because all the text is covered.

**2b299916** (KEY-1): Two documents are held up side by side, and a baseline line is drawn across both. In the right-hand one a value starts below the line, climbs steadily above it, then swings up and down. It looks like a balance or investment value (maybe a loan against a benchmark) that sits under the break-even line at first, then grows and turns volatile. The takeaway is that early shortfall can reverse into gains, but the path is unpredictable.

**45fab8d0** (KEY-1): Two documents (likely a loan or contract comparison) are held up against a baseline line, and a value on the right one starts just below the line (a shortfall or balance shown in green) and then climbs over time, crosses above the line, and ends up swinging up and down sharply. This seems to show something like a balance or investment/debt value that starts negative, grows past break-even, and then fluctuates with market-like volatility, meaning the outcome is uncertain and not a smooth steady path.

**634f63de** (KEY-7): Over time, a horizontal bar grows from a thin gray/white sliver into a large green block (something accumulating, like a growing balance or payoff/borrowing total), while two hatched red bars (apparently debts or costs) shrink: the left one gradually and the right one down to nothing, leaving an empty outlined box. It suggests that as the green amount builds up, the red debts get paid down or wiped out, with one fully eliminated first and the other nearly gone.

**f753fb88** (KEY-7): Over time, a horizontal bar (a timeline or loan-period bar) grows longer and fills with teal while the two red-hatched bars (debt balances, probably loan principal or interest owed) shrink toward zero, with the second one emptying entirely and ending highlighted as a clean white outline. This looks like paying off debt over time: as payments accumulate across the repayment period, the balances fall and the loans are cleared, which for a graduate student with private loans on top of federal ones suggests a repayment plan, perhaps paying the smaller or higher-interest loan off first.

**dc873a3b** (KEY-7): Over time, a long bar (likely a loan or repayment term) fills in with green while the two red hatched stacks (likely debt balances, probably a federal loan and a private loan) shrink toward zero. The second stack empties first and is outlined at the end, so this probably shows debt being paid down over the repayment period. The video may be showing that paying off the higher-cost private loan first, or paying steadily, clears the debt.

## Chấm
| Người đọc | Nhịp | (i) | (ii) | Kết |
|---|---|---|---|---|
| 42278f80 | KEY-1 | ✓ một người cầm, hai tài liệu so sánh | ✓ một vạch phẳng; bên phải bắt đầu dưới vạch rồi lên xuống | **đúng** |
| 45fab8d0 | KEY-1 | ✓ hai tài liệu cầm lên, "loan or contract comparison" | ✓ bắt đầu ngay dưới vạch, vượt lên, lên xuống | **đúng** |
| 2b299916 | KEY-1 | nửa: hai tài liệu, nhưng đọc là "giá trị so với mốc", không phải hai lựa chọn | ✓ | nửa |
| 634f63de | KEY-7 | nửa: "khối xanh lớn dần → nợ đỏ giảm" (đúng quan hệ), nhưng nghĩa là trả nợ | nửa: một cột về 0, cột kia "gần hết" | nửa |
| f753fb88 | KEY-7 | ✗ thanh tiến độ thời gian, trả nợ | nửa: cột thứ hai về 0 | sai |
| dc873a3b | KEY-7 | ✗ trả nợ theo thời gian | ✗ "trả khoản lãi cao trước" | sai |

**KEY-1: 2/3 đúng → ĐẠT.** **KEY-7: 0/3 đúng (1 nửa) → TRƯỢT vòng 2** → theo lệnh C3: đưa phương án lên chủ dự án (`gates/C3b.md`).
Chẩn đoán KEY-7: người đọc nay thấy đúng quan hệ hình (xanh lớn → đỏ giảm; cột phải về 0 trước), nhưng **thanh xanh dài dần trông như thanh tiến độ/khoản đã trả**, nên cả nhịp đọc thành "trả nợ theo thời gian". Ba vòng (C3, r1, r2) đều cho thấy: thứ gì lớn dần theo khung hình sẽ được hiểu là thời gian.
