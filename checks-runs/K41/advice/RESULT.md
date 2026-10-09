# Hiệu chuẩn rubric khuyên A9 + A21 (K4.1; chủ dự án duyệt 08/10 dạng chạy thử ở C4 Tập 6)

Một người chấm độc lập (agent mới, chỉ đọc `packet.json`), rubric ba cờ. 14 câu trả lời N1/N2 của cổng gốc C3 Tập 5 có trên đĩa (`episodes/ep005/c3/root*`; khiếu nại ghi 19 lượt, 5 lượt không còn tệp câu trả lời) + 2 đối chứng dương (video tự nêu hành động) + 2 đối chứng thận trọng chung (A9). Câu trả lời cũ không có câu phụ 5 — xếp theo câu 4.

**Kết quả: 16/18 xếp đúng kỳ vọng.**

| nhãn | nguồn | mẫu | cờ cũ (advice) | kỳ vọng | mới | đúng | trích |
|---|---|---|---|---|---|---|---|
| R05 | ctrl:caution-lender | ctrl:caution-lender | None | caution | caution | ✓ | Ask your lender how your own loan amortizes and run your own numbers. |
| R09 | ctrl:caution-tax | ctrl:caution-tax | None | caution | caution | ✓ | I'd check my own numbers and talk to a tax professional before selling. |
| R02 | ctrl:pos-label | ctrl:pos-label | None | stated | stated | ✓ | The animation tells you directly: stay put to save — don't sell early. |
| R07 | ctrl:pos-sell | ctrl:pos-sell | None | stated | stated | ✓ | The video's own text says to sell before prices drop, so viewers would sell early. |
| R11 | root-r2/094d734b | N2-bars | True | not_stated | inferred | ✓ | Plan for the possibility that it takes more than five years, and only buy if you can stay  |
| R06 | root-r2/15d71b10 | N1-calendar | True | not_stated | stated | ✗ | The rate matters a lot, and the animation implies that extra principal payments early on w |
| R14 | root-r2/46c7792b | N1-calendar | True | not_stated | inferred | ✓ | The rate has a big effect on the total cost, and that's a reason to shop lenders. |
| R16 | root-r2/6f244034 | N2-bars | True | not_stated | inferred | ✓ | Buy only if you could stay put for a long time and could afford the payments through a pri |
| R10 | root-r2/ca58211d | N1-calendar | True | not_stated | inferred | ✓ | Shopping for a lower rate, making extra principal payments, or waiting for a better rate c |
| R13 | root-r3/07e954d9 | N1-calendar | False | not_stated | caution | ✓ | I'd also check the numbers against my own loan amount and rate. |
| R17 | root-r3/33ff82ff | N2-bars | True | not_stated | inferred | ✓ | Plan to stay in the home for a long time, because a bad stretch can take more than 5 years |
| R12 | root-r3/a3bd9578 | N1-calendar | True | not_stated | stated | ✗ | Extra principal payments early on would help the most. |
| R18 | root-r3/df1ca622 | N2-bars | True | not_stated | inferred | ✓ | Have a cushion and expect to hold the home well beyond five years. |
| R08 | root-r3x/5936099b | N1-calendar | True | not_stated | inferred | ✓ | Because the schedule is set up front, extra principal payments early on would have the big |
| R04 | root/0d63a711 | N1-calendar | True | not_stated | inferred | ✓ | The video doesn't state any of this advice, so these takeaways are my inference from the s |
| R01 | root/2e6f4f30 | N1-calendar | True | not_stated | inferred | ✓ | Extra principal payments early would help more than later ones, though the animation doesn |
| R15 | root/9d45d3cd | N2-bars | True | not_stated | inferred | ✓ | Plan to stay put long enough to ride out a bad stretch, and keep an emergency fund so you  |
| R03 | root/da9e87bb | N2-bars | True | not_stated | inferred | ✓ | So I'd plan to stay put for many years and keep a cash cushion. |

N1/N2: cờ cũ "advice" bật 13/14 (chặn); rubric mới advice_stated 2/14, còn lại inferred/none.
