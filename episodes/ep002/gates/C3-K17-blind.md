# C3 điều kiện (a) — Kiểm mù KEY-1/KEY-7 thiết kế lại · vòng 1 (01/10/2026)

Ý đồ ghi trước: `gates/C3-K17-intent.md` (commit 39d01ef). Mẫu: `design/c3/final/K1-strip-masked.png`, `K7-strip-masked.png` (commit 39b5b8b). Khoá: `review-c3/k17/key-r1.json`. 6 người đọc mới (sonnet), mỗi người một mẫu, câu hỏi cố định.

## Nguyên văn

**634711ca** (KEY-1): A person holds up two cards: one shows a flat, constant line (a fixed value, like a fixed rate or balance), while the other shows a line that fluctuates and trends upward over time, then dips and bounces (a variable or market-linked value). The idea is a comparison of a steady, unchanging figure against a volatile, changing one, meaning the variable option can end up differently from the fixed one and carries uncertainty (for loans, likely fixed versus variable interest rates).

**b48179ad** (KEY-1): A person holds up two documents or accounts side by side: the left one stays flat (a fixed amount, like a loan balance or a fixed rate) while the right one is a jagged line that rises and falls over time (like a variable or market-linked rate or investment value). The idea appears to be comparing a steady, predictable option with a fluctuating one, so the variable option can drift well above its starting point and carries more risk and uncertainty than the fixed one.

**ea6815ba** (KEY-1): The section shows a person holding up two documents: the left one stays a flat, unchanging line (something fixed, like a set loan balance or fixed terms), while the right one starts empty and then fills in with a jagged line chart that rises over time and then swings and dips (something variable, like a rate or balance that fluctuates). It seems to contrast a fixed option with a variable, unpredictable one, which could mean fixed versus variable rates on private loans, or a stable amount versus one that grows and swings. I can't be certain which, since all the text is hidden.

**f180fc55** (KEY-7): Over time, the red blocks (a grid of many individual items, apparently loan balances or debts, set against a spiking blue line that looks like interest rates) are gradually paid off and cleared, while the red bars shrink and the green area below the line grows. This looks like a balance being paid down over time, with a cost (yellow) turning into a net gain (green). It seems to compare two scenarios, the left half and the right half, with different timing of payoff. I'm only moderately sure of this reading.

**7b90d02b** (KEY-7): The section shows a timeline (a rising-then-falling blue curve, likely interest rates or a balance) over which a grid of red cells (debt or loan balance/payments) gradually empties out: red blocks and bars shrink step by step until almost nothing is left, while a yellow-then-green chart below goes from a small positive (yellow) to a growing teal area beyond the baseline. It reads as repayment over time: the debt is paid down to zero and the remaining area turns into net gains or savings, showing that steady paydown of loans eventually frees up money or builds wealth (the exact meaning is partly uncertain because all text is hidden).

**d916e6f8** (KEY-7): Over time, a grid of red blocks (many debt units or loan balances, laid out along a rising-then-falling timeline line chart) gradually empties out, and the red bars underneath shrink one after another, while an area below the baseline flips from a small yellow sliver (money owed or spent) into a growing teal area (net gain or surplus). It looks like a repayment or payoff timeline: debt is paid down over the years until it is cleared, and the teal area shows that money is then left over, though I cannot be sure what the covered labels said.

## Chấm (theo đúng bảng ý đồ; chấm chặt)
| Người đọc | Nhịp | (i) | (ii) | Kết |
|---|---|---|---|---|
| 634711ca | KEY-1 | ✓ một người, hai thẻ | nửa: phẳng vs lên xuống ✓; **"bắt đầu thấp hơn" ✗** | sai |
| b48179ad | KEY-1 | ✓ | nửa: phẳng vs lên xuống ✓; "bắt đầu thấp hơn" ✗ | sai |
| ea6815ba | KEY-1 | ✓ | nửa: phẳng vs lên xuống ✓; "bắt đầu thấp hơn" ✗ | sai |
| f180fc55 | KEY-7 | chiều: đỏ giảm ✓, nhưng đọc là **theo thời gian trả nợ**, không phải theo khoảng chênh ✗ | hai nửa khác nhau ✓ (yếu) | sai |
| 7b90d02b | KEY-7 | đỏ giảm ✓ / nguyên nhân = thời gian ✗ | ✗ | sai |
| d916e6f8 | KEY-7 | đỏ giảm ✓ / nguyên nhân = thời gian ✗ | ✗ | sai |

**KEY-1: 0/3 · KEY-7: 0/3 → vòng 1 TRƯỢT cả hai.**
Tiến bộ so với C3: KEY-1 "một người, hai lựa chọn" 3/3 (trước yếu); KEY-7 không còn ai đọc ngược chiều "đỏ tăng" (trước 2/3).

## Chẩn đoán → vòng 2
- KEY-1: hai thẻ tách rời, mức của lãi cố định và điểm bắt đầu của lãi thả nổi không nằm trên **cùng một thước** → không ai thấy "bắt đầu thấp hơn". Sửa: một vạch mức cố định kéo **liền qua cả hai thẻ** (cùng độ cao, thẻ không lệch nhau), đường thả nổi bắt đầu rõ **dưới** vạch đó với khe hở tô màu, rồi mới lên xuống vượt vạch.
- KEY-7: thứ duy nhất thay đổi giữa các khung là "đỏ biến mất" → người đọc gán cho thời gian (trả nợ dần). Cái núm điều khiển (khoảng chênh lúc đầu) không hiện thành vật. Sửa: một **núm/khe hở nhìn thấy được** (hai vạch: cố định và điểm bắt đầu thả nổi, khe hở nới rộng dần) đặt **đầu khung, to**, và kết quả hiện thành **hai cột lớn cạnh nhau** (nửa 1954–1980 / nửa từ 1981) co lại cùng nhịp với khe hở; cột phải về 0 trước, cột trái còn đỏ ở khung cuối. Bỏ lưới 753 ô và nêm vàng/xanh ở nhịp này (gây đọc "trả nợ, tiền dư").
