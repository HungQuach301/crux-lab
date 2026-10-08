# Grading packet (blind). Independent grader. Each label is one reader's answers about one silent 6-frame strip; the strip id is given so you compare against its muted read. Grade literally.

## Rubric
- **Chấm:** người chấm độc lập mù tập; nghĩa 1 / 0,5 / 0 so với "muted read" của `review-c3/spans.json`; cờ khuyên theo **A9** (thận trọng chung — tự kiểm số, hỏi bên cho vay — không tính; khuyên mua/chờ/bán/chọn tính). Người đọc đúng = nghĩa 1 và khuyên_tính false.


Muted read (đáp án đúng) theo hình:
- B02-S02: The loan, as a share of the price, starts at 90 % and drifts down slowly; it only touches the 80 % line after about 8 years.

Output JSON only: {"R1": {"score": 1|0.5|0, "advice": true|false, "caution_only": true|false, "why": "<one line>"}, ...}

### R1 (strip B02-S02)
1. **The idea.** The animation shows how long it takes a buyer who starts with a small down payment (a loan of about 90% of the price) to get down to an 80% loan-to-value ratio. At 80%, a buyer typically no longer needs mortgage insurance. It compares the scheduled path, which comes from paying down the loan, with what actually happened to past buyers. Those buyers' home values moved with the market.

2. **What changes across the frames.**
   - Frames 1–2 are an illustrative, labeled example. One line starts at 90% and slopes down to the 80% line at about 8 years. This is the amortization schedule alone.
   - Frame 3 swaps in real data: one line per purchase month from 1991 to 2016. The "schedule ≈ 8 years" label stays.
   - Frames 4–5 add more and more of these historical lines. They spread out into a wide fan. Some drop quickly. Many rise well above 90% before they come back down, probably because home values fell.
   - Frame 6 highlights two lines. The typical buyer reached 80% in about 2 years. The slowest case, in blue, took about 9 years.

3. **What it means.** The schedule says about 8 years, but the real time depended on what home prices did. For most past buyers, rising prices got them to 80% much faster, around 2 years. For unlucky buyers who bought before price drops, it took longer than the schedule, about 9 years. The caption says this is a measurement of past buyers, not a prediction.

4. **Advice a viewer would take.** The animation gives no direct buy, rent, or wait advice. Its captions say so: "not a reason to buy, rent or wait" and "history, not a forecast." A viewer would take away these points:
   - Don't assume the 8-year schedule is what you'll get.
   - Home price changes have a big effect on how quickly a 10%-down buyer builds equity. In the past the typical wait was short, but the worst case was long.
   - The data covers only the US, so it won't necessarily repeat.

   As a renter with about 10% saved, I'd read it this way. A 10%-down purchase has historically reached 80% quickly, but only if prices cooperate. I'd plan for the slow case, so I'd want a stable job, an emergency fund, and a plan to stay put for many years.
