# Grading packet (blind). Independent grader. Each label is one reader's answers about one silent 6-frame strip; the strip id is given so you compare against its muted read. Grade literally.

## Rubric
- **Chấm:** người chấm độc lập mù tập; nghĩa 1 / 0,5 / 0 so với "muted read" của `review-c3/spans.json`; cờ khuyên theo **A9** (thận trọng chung — tự kiểm số, hỏi bên cho vay — không tính; khuyên mua/chờ/bán/chọn tính). Người đọc đúng = nghĩa 1 và khuyên_tính false.


Muted read (đáp án đúng) theo hình:
- B02-S02: The loan, as a share of the price, starts at 90 % and drifts down slowly; it only touches the 80 % line after about 8 years.
- B18-S18: Three panels side by side, aligned at purchase: one fixed schedule band and a fan of on-paper lines from fast to slow; a vertical 'your plan' marker stands between the schedule band and the fan; the 75 % line stays visible under all of them.

Output JSON only: {"R1": {"score": 1|0.5|0, "advice": true|false, "caution_only": true|false, "why": "<one line>"}, ...}

### R1 (strip B02-S02)
1. **The idea:** The animation shows how long it takes a buyer who puts about 10% down to get their loan down to 80% of the home's value. The loan starts near 90% of the price. The 80% line is a marker. I'd guess it matters because that's where mortgage insurance usually can come off, but the image doesn't say so. The first two frames are an illustrative schedule. The later frames use real data: the FHFA and Freddie Mac numbers via FRED, with one line for each purchase month from 1991 to 2016.

2. **What changes across the frames:**
   - Frames 1–2: A single line slopes down from 90% and reaches 80% at about 8 years. That is the planned pay-down.
   - Frames 3–5: Many thin gray lines are added, one for each real purchase month. They spread out widely. Many drop below the schedule line, and many rise well above 90% before falling.
   - Frame 6: Two cases are highlighted. The typical buyer reached 80% in about 2 years. The slowest case took about 9 years, and its loan share climbed well above 90% along the way.

3. **What it means:** The 8-year schedule only counts paying down the loan. In real life the ratio also moves with home prices. Rising prices got most past buyers to 80% much faster than the schedule, typically in about 2 years. Falling prices pushed some buyers' loan share up for years, and the slowest took even longer than the schedule. So the time to reach 80% varied a lot, from about 2 years to about 9.

4. **What a viewer would take from it:** The animation says outright that it isn't advice. It calls itself a measurement of past US buyers, "not a reason to buy, rent or wait," and "history, not a forecast." As someone with 10% saved, I'd take away three things:
   - Don't count on the 8-year schedule. It could be much faster or slower.
   - Don't assume the quick 2-year result will repeat, because it depended on prices rising.
   - Plan for the slow case. If I buy, I should be able to afford the payment, including any mortgage insurance, for many years, and I shouldn't need to sell soon.

### R2 (strip B18-S18)
**1. The idea.** The animation shows how long it takes a first-time buyer with a small down payment to get down to 80% loan-to-value. That is the point where mortgage insurance can usually come off. It compares three past buyers, Owen, Grace and Victor. They all follow the same rule and the same price index (FHFA and Freddie Mac data via FRED), lined up at the month they bought.

**2. What changes across the frames.**
- **Frame 1:** Three separate panels show each buyer's loan-to-value line falling toward the 80% line.
- **Frames 2–3:** The panels merge into one chart over 0 to 10 years. A faint bundle of many past buyers sits behind the three highlighted ones. A fixed "on paper" schedule is marked "a plan."
- **Frame 4:** The text gives numbers. On paper, the typical buyer reached 80% in about 23 months, and about 1 in 7 took more than 60 months. Roughly 2 years matched the typical month. It did not match the slow buyers, and it did not match the lender's fixed step-down schedule.
- **Frame 5:** A $400,000 home is shown as a stack of money, with a note that this is "a measurement, not a next step."
- **Frame 6:** Two icons appear: a house labeled "buying now + mortgage insurance" and an apartment building labeled "still renting, still saving."

**3. What it means.** How fast you reach 80% depends mostly on what home prices do after you buy, not only on your payments. Owen got there fast because prices rose. Victor got there slowly because prices were flat or fell. The typical past buyer needed about 2 years, but a meaningful minority needed 5 years or more. The animation labels all of this as illustrative, US-only and based on history, so it doesn't forecast what will happen to you.

**4. What a viewer would take from it.** The video gives no direct advice, and it says so: "not a reason to buy, rent or wait." Here is what I'd take from it as a renter with about 10% saved:
- Don't assume mortgage insurance will vanish in 2 years. That is only the typical past case.
- Budget for the slow case, where insurance could last 5 years or more.
- Treat buying with insurance and renting while saving as two real options, and decide based on my own finances, not on this chart.

### R3 (strip B18-S18)
**1. The idea.** The animation shows how long past US buyers with small down payments took to get their loan down to 80% of the home's value. That is the point where mortgage insurance can usually be dropped. It compares the schedule on paper with what actually happened to home prices after purchase. The text says it uses FHFA and Freddie Mac data via FRED, and it labels the visuals "illustrative."

**2. What changes across the frames.**
- **Frame 1:** Three past buyers, Owen (fast), Grace and Victor (slow), each have a line showing their loan relative to home value. All three follow the same rule, and each is measured from the day of purchase. The paper schedule is a straight line sloping down. Owen and Grace's real paths track it fairly closely. Victor's path wanders up and down and takes much longer to reach the 80% line.
- **Frames 2 and 3:** The three paths are overlaid on one timeline from 0 to 10 years, with a "plan" marker near the start. Many faint lines show the spread of outcomes. Frame 3 adds that the schedule is fixed at the start.
- **Frame 4:** It adds numbers. On paper the typical time is 23 months, but about 1 in 7 buyers took more than 60 months. About 2 years matches the typical month, "not the slow ones, not the lender's step."
- **Frame 5:** A $400,000 home appears next to a stack of green bars. The bars seem to show the owner's stake in the home, with only a small teal slice at the bottom. A note says all dollars are in dollars of the day, and that this is "a measurement, not a next step."
- **Frame 6:** The scene splits in two. One side is "buying now + mortgage insurance" (a house). The other is "still renting, still saving" (an apartment building). The person stands between them.

**3. What it means.** Getting rid of mortgage insurance isn't guaranteed to take the time the paper schedule says. The typical buyer got there in about 2 years, but a meaningful minority (roughly 1 in 7) waited more than 5 years, because home prices moved against them. The repeated disclaimers ("not a reason to buy, rent or wait," "history, not a forecast," "US only") say this is a description of the past, not a prediction.

**4. What a viewer would take from it.** The video doesn't tell me to buy, rent or wait. If I'm putting down about 10%, I shouldn't assume the insurance will disappear on the lender's timeline. I should be ready for it to last anywhere from about 2 to 5+ years. Frame 6 suggests the real decision is between two paths: buy now and pay insurance for an uncertain stretch, or keep renting and saving. Either can be reasonable, and the animation doesn't pick one. The takeaway for me is to budget for the slow case and not just the typical one.

### R4 (strip B02-S02)
1. **The idea.** The animation is about how long it takes a home buyer with a small down payment to get the loan down to 80% of the home's value. That is the point where you have 20% equity. The scheduled paydown, with a loan that starts near 90% of the price, would get there in about 8 years. The animation then checks that schedule against what actually happened to real buyers.

2. **What changes.**
   - Frames 1–2 show an illustrative, tagged line. It starts at 90% and slopes down to the 80% line at about 8 years.
   - Frame 3 adds the real data. It shows one thin line per purchase month from 1991 to 2016, with each line measuring loan divided by home value on paper.
   - Frames 4–5 fill in more of those lines. They fan out widely. Some drop below 80% quickly, and many rise well above 90% before coming back down.
   - Frame 6 highlights two cases. The typical buyer got to 80% in about 2 years, much faster than the schedule, because home prices rose. The slowest case took about 9 years, and its line climbed well above 90% along the way, which probably means prices fell.

3. **What it means.** The paydown schedule is only part of the story. Home price changes matter more. The 8-year schedule is a middle benchmark. Many past buyers reached 80% much sooner, and some took longer than the schedule, with the slowest case taking about 9 years. The labels say this is a measurement of past US buyers. It is not a forecast.

4. **Advice a viewer would take.** The video says directly that this is "not a reason to buy, rent or wait." It doesn't tell anyone what to do. For me, as a renter with about 10% saved, the takeaways are:
   - Don't assume it will take exactly 8 years to reach 20% equity. It could be about 2 years or longer than 9, depending on prices.
   - Plan for the slow case. Expect to carry a loan above 80% of the home's value for a long time. That means keeping an emergency fund and not counting on quick equity.
   - Remember that the data is historical and US-only, so it doesn't guarantee the same results for me.
