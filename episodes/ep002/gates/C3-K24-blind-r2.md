# C3c — Kiểm mù vòng sửa KEY-2/KEY-4 (01/10/2026)

Ý đồ: `gates/C3-K245-intent.md` (không đổi). Mẫu + khoá commit trước khi chạy (4879423, `review-c3/k245-key-r2.json`). 6 người đọc mới.

## Nguyên văn

**02ebff4d** (KEY-2): The section shows a balance being weighed against a baseline: a green bar (a positive amount) sits above the baseline in frame 1, shrinks and shifts as it is paid down or drawn on in frames 2-3, and goes to zero in frame 4. In frames 5-6 an amber bar of similar size appears on the other side of the baseline, so a positive balance turns into a debt or deficit of comparable size. For a grad student, the likely point is that money borrowed or spent over time, with interest accruing, shows up as a growing negative balance you owe, such as private loan debt past the federal limit.

**00c414ad** (KEY-2): A teal bar hanging below a baseline (on the right-hand document) shrinks over frames 1-3 until it is gone in frame 4, then an amber bar appears above the baseline in frames 5-6. It seems to show a balance moving from one side of zero to the other, for example a debt or deficit being paid off and then turning into a surplus or savings, or a loan shrinking and then flipping. The covered text means I can't be sure of the exact meaning.

**2f6772ec** (KEY-2): A balance bar drawn on a scale (a line) starts as a large amount above the line (green, frame 1), shrinks to a thin sliver (2), shrinks further toward zero (3, 4), then flips to an amount below the line (orange, 5, 6). My guess is that this shows a positive balance being paid down and then, in the next stage, turning into a growing debt, such as loan interest piling up. I'm not certain of the exact context.

**2a805e95** (KEY-4): It shows a balance (a loan or account) that starts as a small negative dip and then grows into a large orange (gold) area over time, while the green tank that was full at first drains to empty and a red hatched block (debt or shortfall) grows. In other words, a sum of money you have (the green tank, e.g. borrowed funds) gets used up while the cost or debt keeps accumulating and growing, peaking and then tapering, leaving you with a large unpaid balance. This is most likely interest compounding on a loan.

**1f020418** (KEY-4): It shows a loan being taken out and then repaid over time: a bucket of borrowed money (teal) is drained while a timeline goes from a small negative (debt/spending in school) to a large gold hump of earnings, and when the bucket empties a red hatched pile of what's left remains. That is, the debt keeps growing (interest) and gets spent, and the later income has to pay it back, with a red leftover showing the cost or unpaid remainder that persists long after the loan money is gone.

**f58ef773** (KEY-4): This section shows a loan balance over time: borrowing in school pushes the balance below zero (green, a tank that fills with loan principal) and then, once you start earning, the income line rises into positive territory (gold) while the tank drains and empties. The red hatched block that grows when the tank is empty seems to show that if the repayment drains the tank slowly, a large amount of interest builds up (or is paid) on top of the principal, so your earnings over many years end up funding both the debt and the interest.

## Chấm (cùng cách chấm vòng 1)
| Nhịp | Người đọc | Điểm | Lý do |
|---|---|---|---|
| KEY-2 | 02ebff4d | 0,5 | thấy khoảng cách lớn → nhỏ → 0 → đảo phía; đọc là **một số dư** đổi dấu, không phải hai mức khởi đầu |
| KEY-2 | 00c414ad | 0,5 | như trên (có nhắc "right-hand document") |
| KEY-2 | 2f6772ec | 0,5 | như trên |
| KEY-4 | f58ef773 | 1 | đủ ba phần: ở dưới → hũ đầy; ở trên → hũ cạn dần; hũ cạn → khối đỏ lớn lên (nghĩa gán là vay/thu nhập) |
| KEY-4 | 2a805e95 | 0,5 | hũ cạn khi ở trên, cạn → đỏ; không thấy hũ đầy lên khi ở dưới |
| KEY-4 | 1f020418 | 0,5 | như trên |

**KEY-2: 0/3 đúng (3 nửa) → TRƯỢT sau vòng sửa. KEY-4: 1/3 đúng (2 nửa; 2/3 điểm) → TRƯỢT sau vòng sửa.** Theo lệnh C3c → hỏi chủ dự án (`gates/C3d.md`).
Ghi chú: KEY-4 tiến bộ rõ (vòng 1: 0 điểm; vòng sửa: 2/3 điểm). Phần hụt là "hũ đầy lên khi ở dưới": khung 1 của dải đã thấy hũ nửa đầy. KEY-2 cả hai vòng đều cho 3/3 "nửa": người đọc thấy đúng khoảng chênh lớn → nhỏ → 0 → đảo chiều, nhưng không thấy đó là **hai** lời mời.
