# Grading packet (blind). Independent grader. Each label is one reader's answers about one silent 6-frame strip; the strip id is given so you compare against its muted read. Grade literally.

## Rubric
- **Chấm:** người chấm độc lập mù tập; nghĩa 1 / 0,5 / 0 so với "muted read" của `review-c3/spans.json`; cờ khuyên theo **A9** (thận trọng chung — tự kiểm số, hỏi bên cho vay — không tính; khuyên mua/chờ/bán/chọn tính). Người đọc đúng = nghĩa 1 và khuyên_tính false.


Muted read (đáp án đúng) theo hình:
- B02-S02: The loan, as a share of the price, starts at 90 % and drifts down slowly; it only touches the 80 % line after about 8 years.
- B18-S18: Three panels side by side, aligned at purchase: one fixed schedule band and a fan of on-paper lines from fast to slow; a vertical 'your plan' marker stands between the schedule band and the fan; the 75 % line stays visible under all of them.

Output JSON only: {"R1": {"score": 1|0.5|0, "advice": true|false, "caution_only": true|false, "why": "<one line>"}, ...}

### R1 (strip B18-S18)
1. **The idea.** The animation shows how long it takes a first-time buyer with a small down payment to get rid of mortgage insurance. The 80% and 75% lines look like loan-to-value targets. The animation uses past US buyers, with home-price data from FHFA and Freddie Mac via FRED. Each buyer is lined up at their purchase date and run under the same rule and the same price index. The paydown "on paper" is a fixed schedule set at the start. The real path depends on what home prices did afterward.

2. **What changes over time.**
   - Frame 1 draws a few lines falling toward the 80% and 75% levels over 10 years, along with a rising and falling green price line.
   - Frame 2 adds a "a plan" marker and names three example buyers: Owen, Grace and Victor. It also shows a faint web of many other past buyers' paths.
   - Frame 3 labels the schedule as "fixed at the start."
   - Frame 4 adds the typical result: about 23 months, with roughly 1 in 7 buyers taking over 60 months. It notes that 2 years matched the typical month, "not the slow ones, not the lender's step."
   - Frame 5 switches to a $400,000 home shown as a green stack, with a small house beside it.
   - Frame 6 shows two options, "buy now + mortgage insurance" and "keep renting, keep saving," with a person standing between a house and an apartment building.

3. **What it means.**
   - The insurance usually ends sooner than the schedule alone suggests, because price changes and paydown both count. The typical case is about two years.
   - The range is wide. A meaningful minority wait five years or more, depending on the market they bought into.
   - The caption "not a reason to buy, rent or wait" and the "illustrative / history, not a forecast" tags say this is a measurement of past outcomes, not a prediction or a recommendation.

4. **What a viewer would take from it.**
   - It gives no push toward buying or renting. The closing frame lays out both paths as legitimate.
   - It does give a way to think about the cost. If you buy with about 10% down, plan for mortgage insurance and don't assume it will vanish on a fixed date. It may be gone in about two years, and it could take five or more.
   - For someone like me, renting with roughly 10% saved, the practical step is to run my own numbers for both paths. That means the insurance cost, how long I'd stay, and what I'd gain by renting and saving longer.
   - Because this is US history and not a forecast, I wouldn't treat the 23-month figure as a promise.

### R2 (strip B02-S02)
1. **The idea:** The animation shows how long it takes a buyer who puts down about 10% to get their loan down to 80% of the home's value. The image marks 80% as the target line but doesn't say why it matters. On the fixed payment schedule alone, that takes about 8 years. It then compares the schedule with what actually happened to US buyers from 1991 to 2016.

2. **What changes:** In frames 1 and 2, a single illustrative line slides from 90% down to 80%, reaching it at about 8 years. In frames 3 to 5, a line is added for every purchase month from 1991 to 2016, until they form a mountain-shaped bundle. In frame 6, two real cases are highlighted. The typical buyer got to 80% in about 2 years. The slowest buyer, in blue, rose well above 90% before falling and took about 9 years.

3. **What it means:** Your loan as a share of the home's value depends on more than your payments. It also depends on what the home's price does. For most past buyers, rising prices got them to 80% much faster than the schedule predicted. For the unlucky ones, falling prices pushed the ratio up and made it take longer than the schedule. The captions say this is a measurement of the past. It is US-only history, not a forecast.

4. **Advice a viewer would take:** The animation gives no buy, rent or wait advice, and it says so directly: "not a reason to buy, rent or wait." What I'd take from it as a renter with about 10% saved:
   - Don't count on a fast timeline. The typical 2 years came from price growth that may not repeat.
   - Plan for the slow case. Make sure you could afford the home and stay in it for 8 to 9 years.
   - Treat the schedule's roughly 8 years as the baseline you can count on.
