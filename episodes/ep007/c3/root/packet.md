# Grading packet (blind). Independent grader. Each label is one reader's answers about one silent 6-frame strip; the strip id is given so you compare against its muted read. Grade literally.

## Rubric
- **Chấm:** người chấm độc lập mù tập; nghĩa 1 / 0,5 / 0 so với "muted read" chép **nguyên văn** từ `beats.md` (`spans.json`). **Cờ khuyên theo rubric MỚI** (G1 câu 2, như Tập 6 C4): `advice_stated` (chính hình/chữ trên hình nêu/ngụ ý hành động: chọn 15/30 năm, trả thêm, đầu tư, trả tháng/năm, chờ/khoá lãi) → **trượt**; `advice_inferred` / `caution_only` chỉ báo, câu trích vào bảng. Người đọc đúng = nghĩa 1 và `advice_stated` false.


Muted read (đáp án đúng) theo hình:
- N1-s01-stack: A faceless figure by her house; a thin stack of bills appears beside the house and grows by one bundle on each beat, with a monthly price over it.
- N1-s06-stack: The 30-year bar is raised to finish in 15 years and ends just above the 15-year bar; the sliver above becomes bills that drop onto the stack, month after month, until it stands at its full height.
- N1-s21-track: A month track runs from Tessa's house: 180 tiles, then 15 more tiles light in warn past the 15-year mark. Then a thin extra slab on top of the required payment makes the track end exactly at 180.
- N1-s23-track: On the month track, extra principal arrives as one big block every 12th tile instead of thin slabs; the track ends 4 tiles later.
- N1-s25-bar: A horizontal beam rises beside the house to the height of the loan rate; a single extra dollar sits on top of it; a second dollar, labelled "any other use", is held up against the beam.

Output JSON only: {"R1": {"score": 1|0.5|0, "advice_stated": true|false, "advice_inferred": true|false, "caution_only": true|false, "quote": "<reader words behind any flag, else empty>", "why": "<one line>"}, ...}

### R1 (strip N1-s06-stack)
1. **The idea.** The animation compares two ways to pay off a house, using an illustrative homeowner named Tessa. The first is a 15-year mortgage. The second is a 30-year mortgage paid at the 15-year pace, which the animation says costs $2,948 a month. The source is labeled as the Freddie Mac weekly mortgage survey. The 30-year loan has a lower required payment, and the gap is shown as an extra $120 a month. That $120 a month builds into a growing stack of gold coins worth $21,622 over 15 years.

2. **What changes.** Frame 1 shows Tessa, her house, and two plain bars labeled 15-year and 30-year. The 30-year bar is shorter. In frames 2 and 3, the bars are drawn side by side and a gold sliver is added on top of the 30-year bar. The text then labels it "+$120 a month" next to "30-year paid in 15: $2,948 a month." In frames 4 to 6, a gold coin stack appears beside the house and grows taller. The last frame labels it "the stack: $21,622 over 15 years."

3. **What it means.** The animation shows a 30-year loan with a smaller required payment, and it shows the monthly difference between the two loans as $120. If Tessa pays the 30-year loan at the 15-year pace, she gets 15-year payoff speed. If she pays only the lower required amount and sets aside the difference, that money accumulates to about $21.6k over 15 years. The frames never show what the coins are invested in or what return they earn. The footer says "US only · history, not a forecast," and each frame carries an "ILLUSTRATIVE" tag. So the numbers are an example, not a prediction.

4. **Advice a viewer might take.** The animation gives no explicit instruction. A viewer might take away that a 30-year mortgage keeps the required payment lower and leaves some flexibility. The viewer might also take away that the leftover money can build up on its own if it is saved or invested. That is a possible reading, not a recommendation the animation makes.

5. **Source of that takeaway.** It is my own reading. The picture and text only show the payment figures and the growing stack, and they carry the disclaimers "ILLUSTRATIVE" and "history, not a forecast." Nothing on screen tells the viewer to choose one loan or to invest instead of paying extra.

### R2 (strip N1-s06-stack)
1. The animation shows an illustrative homeowner, "Tessa," comparing a 15-year mortgage with a 30-year mortgage. The rates come from the Freddie Mac weekly survey. Tessa takes the 30-year loan but pays it at the 15-year loan's pace, which costs $2,948 a month. The 30-year loan's required payment is about $120 a month lower than the 15-year loan's. The animation treats that $120 as a monthly amount she could invest.

2. Frame 1 shows the house, the person and two bars labeled 15-year and 30-year. The bars straighten out in frame 2, and a thin gold slice appears on top of the 30-year bar. Frame 3 labels the slice "+$120 a month." Frames 4 to 6 add a stack of gold coins beside the house. It starts small, grows taller, and ends with the label "the stack: $21,622 over 15 years."

3. The $120 a month is the cost difference between the two loans. If Tessa invests it each month, it grows to about $21,622 over 15 years. The animation implies that this is the benefit of choosing the 30-year loan and investing the difference. It doesn't show the investment return assumed or any risks or costs. The footers say "ILLUSTRATIVE" and "US only · history, not a forecast," which signal that the numbers are an example and not a prediction.

4. The animation gives no explicit advice. A viewer might take away that a 30-year loan paid at the 15-year pace, with the $120 a month invested, can build a pile of money. A viewer might also read the result as a reason to invest the spare cash instead of paying extra on the mortgage. That second reading is an inference, because the animation never says it.

5. Neither the picture nor the on-screen text states any advice, so the takeaway in 4 is my own inference. The only guidance on screen is the disclaimer that this is history, not a forecast. The animation also doesn't compare the $21,622 with what paying extra on the mortgage would save in interest, so it can't settle the original question.

### R3 (strip N1-s21-track)
1. **Idea:** The animation shows an illustrative homeowner, "Tessa", and how long her mortgage takes to pay off. It compares a 30-year mortgage with a 15-year target. The grid of tiles stands for monthly payments.

2. **What changes:** In frames 1–3, a house and a figure appear, and then a grid of payment tiles grows next to the house. In frame 4, the grid is complete. A few tan tiles stick out past a gray divider line, and the caption reads "pay $2,828 on the 30-year: about 195 months." Frame 5 labels the overhang "about 15 months late." In frame 6, the tiles turn green and the caption reads "to finish in 180 months: +$733 a month."

3. **Meaning:** Paying $2,828 a month on the 30-year loan would pay it off in about 195 months, which is 15 months past the 180-month (15-year) target. To finish on the 15-year schedule, she would have to add about $733 a month. The "Freddie Mac weekly mortgage survey" header suggests the numbers come from historical rates. The "ILLUSTRATIVE" tag and "US only · history, not a forecast" mean the example is not a prediction.

4. **Advice:** The animation gives no explicit advice. A viewer might take away that extra payments of about $733 a month shorten the payoff by years. The frames don't show interest saved, investment returns or any comparison with investing, so they don't say whether paying extra is better than investing.

5. **Source:** The animation's own text supports the payoff-timing takeaway: the $2,828 figure, the 195 months, the "15 months late" label and the "+$733 a month" caption. It does not suggest choosing between paying extra and investing, so any such conclusion would be my own. I haven't drawn one.

### R4 (strip N1-s01-stack)
1. The animation shows a homeowner, labeled "Tessa" and marked illustrative, who saves money on a $320,000 mortgage. The labels credit the Freddie Mac weekly mortgage survey and a "week of Oct 8, 2026" date. The "$120 a month" figure suggests she saves that much each month, but the image doesn't say what causes the saving. Possible causes include a lower rate, a refinance, or an extra payment.

2. A figure stands beside a house, and a stack of gold money appears next to it. In frame 1 there is no money. Frame 2 shows a small flat bundle, and frame 3 shows it getting thicker. The "$120 a month" label appears in frame 4. In frames 5 and 6 the stack grows taller. Frame 6 adds the caption "$320,000 loan · week of Oct 8, 2026."

3. It means that a $120 monthly amount adds up to a growing pile of money over time. The loan size and survey date are given as context, but the image doesn't state a rate, a total, or a time span.

4. The only takeaway a viewer could draw is a loose one: small monthly amounts build up, and a $320,000 loan is the example. The image gives no instruction to pay extra on the mortgage or to invest. It doesn't compare the two options, so it offers nothing to help choose between them. The footer "US only · history, not a forecast" warns against treating it as a prediction.

5. The animation didn't suggest any advice. The takeaway in 4 is my own reading of the growing stack. The on-screen text only describes the loan, the source, and the $120 figure, and it says the content is illustrative and not a forecast.

### R5 (strip N1-s21-track)
1. **The idea:** The animation shows how paying extra on a mortgage shortens the loan. Tessa is an illustrative homeowner. Each tile in the grid appears to stand for one monthly payment. The grid shows that a 30-year loan paid at the $2,828 monthly payment runs about 195 months, and that she would need an extra $733 a month to finish in 180 months (15 years).

2. **What changes across the frames:**
   - Frames 1–3: The house and Tessa appear, then the grid of payment tiles grows until it is a full block, with a wall at one edge.
   - Frame 4: The tiles are white, with a few tan ones that stick out past the wall. The caption reads "pay $2,828 on the 30-year: about 195 months."
   - Frame 5: A label marks those extra tiles as "about 15 months late."
   - Frame 6: The tiles turn teal and all fit inside the wall. The caption reads "to finish in 180 months: +$733 a month."

3. **What it means:** Paying the regular amount takes about 15 months longer than the 180-month target. Adding $733 a month pulls the payoff date back to exactly 15 years. The labels "ILLUSTRATIVE" and "US only · history, not a forecast" tell the viewer that this is a made-up example, not a prediction. The "Freddie Mac weekly mortgage survey" header suggests the rates come from historical data.

4. **Advice a viewer might take:** The animation gives no explicit advice. A viewer could infer that extra monthly payments shorten the loan. It does not say whether to prepay or invest instead, and it does not compare the two options.

5. **Source of the takeaway:** The animation itself showed the 195-month and 180-month figures, the "+$733 a month," and the "history, not a forecast" disclaimer. It did not tell anyone to do anything. The inference that extra payments are worth making is my own conclusion, not something the picture or text says. It also says nothing about your situation, such as a $320,000 mortgage or investing the spare cash.

### R6 (strip N1-s25-bar)
1. The animation shows how to think about extra mortgage payments. A character named Tessa, labeled "ILLUSTRATIVE", puts a bill of cash toward her house. Paying down the mortgage saves interest at the mortgage rate. That rate acts as a "bar" of 7.40% a year, before taxes, and the source is labeled as the Freddie Mac weekly mortgage survey. The cash could go to "any other use" instead, such as investing, but the bar says it would have to beat 7.40% to be worth more.

2. In frame 1, the cash goes onto the house and a flat bar sits off to the side. In frame 2, the cash and bar float up above the house. In frame 3, a vertical gauge appears next to the house, and the bar is labeled "the bar: 7.40% a year, before taxes". In frame 4, the text "interest no longer charged, not an investment return" appears. In frame 5, a second cash bill extends the bar and is labeled "any other use". In frame 6, a new line is added: "not tested: whether any investment clears it". The footer reads "US only · history, not a forecast" throughout.

3. Paying extra on the mortgage earns a guaranteed saving equal to the loan's interest rate. That is 7.40% in this example, and it is not a market return. Any alternative use of the money has to clear that rate to come out ahead. The animation does not say whether any investment actually does. It explicitly leaves that untested.

4. The animation gives no direct advice. A viewer could take away a framework: compare your mortgage rate with what you expect to earn elsewhere, and keep in mind that the comparison is before taxes. It does not say whether to prepay or invest.

5. The framework comes from the animation's on-screen text and pictures, such as the bar, the labels, and the "not tested" line. The animation does not tell the viewer what to do. Any advice beyond comparing the rates would be my own conclusion, and I haven't given any.

### R7 (strip N1-s25-bar)
1. The animation shows how to compare paying down a mortgage with investing the same cash. A figure named Tessa, labeled "ILLUSTRATIVE", stands next to a house. Putting a bill toward the house is treated as earning a guaranteed return equal to the mortgage interest rate. That rate is the "bar" that any other use of the money would have to beat. The source is labeled "Freddie Mac weekly mortgage survey".

2. In frame 1, Tessa holds a bill by the house, and a flat bar sits off to the side. In frame 2, the bill and bar move up and away from the house. In frame 3, the bar is labeled "the bar: 7.40% a year, before taxes", and a vertical measuring line links the bar to the house. In frame 4, the text "interest no longer charged, not an investment return" appears. In frame 5, a second bill sits on the bar's end, labeled "any other use". In frame 6, a note is added: "not tested: whether any investment clears it".

3. Paying extra on the mortgage saves interest at the loan's rate, which is 7.40% in this example. That saving is certain and is calculated before taxes. It is not an investment return in the usual sense. Any other use of the cash would need to beat 7.40% to come out ahead. The animation does not test whether any investment can do that. The footer says the data is US only and is history, not a forecast.

4. A viewer would take away a way to frame the decision. Paying extra earns the mortgage rate with certainty, so compare an alternative against that rate. The animation does not say which choice is better. It does not tell anyone to prepay or to invest.

5. The animation did not give advice, so the framing in point 4 comes from its own on-screen text. The "bar" label, the "not an investment return" note, and the "not tested" note all say this directly. Because there is no recommendation, nothing in point 4 is my own conclusion. I also did not apply it to your $320,000 loan, because the animation uses 7.40% and your rate isn't given.

### R8 (strip N1-s23-track)
I only opened the one image, and I can't be sure about the last frame.

1. **Idea:** The animation shows a mortgage as a grid of monthly payment tiles for a character called Tessa, who stands next to a house. The grid looks like 15 columns by 12 rows, which would be 180 months. The header says "Freddie Mac weekly mortgage survey". Every frame is tagged "ILLUSTRATIVE" and "US only · history, not a forecast". From frame 4 on, a label reads "$8,792 once a year", so it appears to be showing a payment of that size made once a year.

2. **What changes:** In frames 1–3, the camera swings from a low side angle to a top-down view of the grid. All the tiles are teal, which looks like payments still owed. In frame 4, the tiles on the left turn gray, as if they've been paid off. The teal tiles are on the right, and a teal strip sits along the top row. In frame 5, almost every tile is gray, and only the top-row strip is still teal. In frame 6, four tan tiles appear beyond the grid. The caption reads "ends in 184 months: 4 months later".

3. **Meaning:** My best reading is that the grid shows how a repeated annual $8,792 amount changes the length of the loan. Frame 6 says the end date is 184 months, which is 4 months after the 180-month grid. That is odd, because extra payments would normally shorten a loan, not lengthen it. The text doesn't say what the $8,792 is or what the 4 months are compared against. It could be a delay or a different scenario, and I can't tell which from the image alone.

4. **Advice:** None. The frames never say to pay extra on the mortgage or to invest instead. They also don't compare the mortgage rate with investment returns, and the disclaimers say it isn't a forecast.

5. **Source:** None. I gave no advice, so there is nothing to attribute to the animation or to my own conclusion.

### R9 (strip N1-s23-track)
1. **The idea:** The animation seems to show a mortgage as a grid of monthly payment tiles, with a character named Tessa standing next to a house. The labels say "Freddie Mac weekly mortgage survey", "ILLUSTRATIVE" and "US only · history, not a forecast". Later frames add "$8,792 once a year", which looks like a lump sum applied each year. The last frame says "ends in 184 months: 4 months later".

2. **What changes over time:** In frames 1–3 the camera moves from a side view to a top-down view of the grid. The house and Tessa shrink and move to the side. In frame 4 the left part of the grid turns from teal to white, while the right part stays teal. In frame 5 almost all tiles are white. Only a top row of teal tiles remains, sitting under the "$8,792 once a year" label. In frame 6 a few tan tiles appear outside the grid at the bottom right, next to the "184 months" label.

3. **What it means:** My reading is that the white tiles are payments already made and the teal ones are payments still to come. The top row of teal tiles would be the yearly $8,792 amounts. The grid probably represents a 180-month (15-year) schedule. The last frame says the loan ends at 184 months, which is 4 months past that grid. I can't tell from the image alone what the 184 months is being compared against, or why it runs longer. The image doesn't show the full scenario or the numbers behind it.

4. **Advice a viewer would take:** None. The frames don't say whether to pay extra or to invest. I'm not drawing a recommendation from them, and the "history, not a forecast" label points away from one.

5. **Source of the suggestion:** none

### R10 (strip N1-s01-stack)
1. **The idea.** The animation shows a homeowner, labeled "Tessa" and marked illustrative, with a $320,000 mortgage. It appears to show that a change in mortgage rates, taken from the Freddie Mac weekly mortgage survey, shifts her monthly payment by about $120. The final frame says "$320,000 loan · week of Oct 8, 2026".

2. **What changes.** The figure and house stay the same. A gold stack of cash first appears beside the house and then grows taller from frame to frame. The "$120 a month" label appears in frame 4 and stays through frame 6. A loan and date caption is added only in frame 6.

3. **What it means.** The growing stack stands for money. The most natural reading is that $120 a month is the size of the payment difference, or the savings, tied to the rate on a $320,000 loan. The frames don't say whether rates went up or down, what the two rates were, or whether the $120 is a cost or a saving. Those details are ambiguous. The footer says "US only · history, not a forecast", so the animation presents this as past data and not a prediction.

4. **Advice.** The animation gives no advice about paying extra on the mortgage versus investing. A viewer would only learn that rate changes can move a payment by roughly $120 a month on a loan this size, and that this is historical. Nothing in the frames compares extra payments with investing.

5. **Source.** The animation did not suggest any advice, so the only takeaway is the descriptive one in point 4. The "history, not a forecast" disclaimer actually cautions against drawing forward-looking conclusions.
