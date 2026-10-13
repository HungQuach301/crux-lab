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
1. **The idea:** The animation compares a 15-year mortgage with a 30-year mortgage that is paid off in 15 years by making extra payments. Tessa, a character with a house, is the example. The 15-year loan costs $2,828 a month. The 30-year loan has a required payment of only $2,216 a month. Paying that 30-year loan off in 15 years takes $2,948 a month, which is $120 a month more than the true 15-year loan.

2. **What changes:**
   - Frame 1 shows Tessa, the house and two blank bars.
   - Frame 2 labels the bars. The 15-year bar is taller, at $2,828. The 30-year bar is shorter, at the required $2,216.
   - Frame 3 raises the 30-year bar to $2,948. A gold sliver marks the extra $120 a month.
   - Frames 4–5 show gold pieces dropping off the bar and piling into a stack next to the house.
   - Frame 6 shows the finished stack, labeled "$21,622 extra paid over 15 years."

   The captions on every frame say "ILLUSTRATIVE," "US only · history, not a forecast," and "Freddie Mac weekly mortgage survey."

3. **What it means:** Under the rates used here, a 30-year loan prepaid on a 15-year schedule costs more than a real 15-year loan. That is probably because the 30-year loan carries a higher rate. Over 15 years the difference adds up to about $21.6k. The figures roughly fit: $120 × 180 months is $21,600.

4. **Advice a viewer might take:** The animation gives no explicit advice. A viewer could infer that if they plan to pay off in 15 years anyway, the 15-year loan is cheaper than a 30-year loan with extra payments. The animation also doesn't say whether to pay extra or invest, so it doesn't answer your question.

5. **Source of the advice:** The advice in 4 is my own inference. The pictures and text show only the payment amounts and the $21,622 gap. They don't tell the viewer what to do. The "history, not a forecast" and "illustrative" labels also suggest it is meant to inform rather than to recommend.

### R2 (strip N1-s23-track)
1. The animation shows a homeowner, labeled "Tessa · ILLUSTRATIVE", paying off a mortgage. The grid of blocks next to the house stands for the monthly payments. It compares paying once a year, a lump sum of $8,792, with paying monthly.

2. The grid starts flat and then rises into columns, so the payments look like rows of upright blocks. In frames 4 and 5 a label appears, "$8,792 once a year", and the blocks are grouped into yearly columns. In frame 6 a few gold blocks show up at the far end of the grid. The caption there reads "ends in 184 months: 4 months later than monthly." The house and Tessa stay the same, and the "ILLUSTRATIVE" tags and the "US only · history, not a forecast" footer stay on screen throughout.

3. Paying the same yearly total in one lump sum at year-end, instead of spreading it across monthly payments, lets interest accrue longer. The loan therefore ends at month 184 instead of month 180, which is 4 months later than paying monthly. The animation presents this as a small cost of delaying payment. It doesn't show how large the interest cost is.

4. The only takeaway a viewer would get is that paying monthly pays the loan off slightly sooner than paying once a year. The animation does not say whether to pay extra on a mortgage or invest the cash instead, and it gives no advice on that question. The footer also says this is history and not a forecast.

5. The payoff-timing point comes from the animation's own text and picture, namely the "4 months later than monthly" caption. The takeaway that monthly is better than yearly is my reading of that caption. Anything about paying extra versus investing is not in the animation at all.

### R3 (strip N1-s25-bar)
1. The animation compares paying extra on a mortgage with putting the same money elsewhere. A figure named Tessa, labeled "illustrative," has a house. A bill goes toward the house, and a bar is set at "7.40% a year, before taxes," which appears to be the mortgage rate from the Freddie Mac weekly survey. Paying extra toward the mortgage is shown as interest no longer charged. The caption says this is "not an investment return."

2. In frame 1, Tessa hands a bill to the house. In frame 2, the bill moves up onto a bar, and the house and Tessa shrink and move back. In frame 3, the bar is labeled as the 7.40% yearly rate before taxes, and a vertical measuring line links it to the house. In frame 4, a caption says the benefit is "interest no longer charged, not an investment return." In frame 5, a second, dashed bill appears off to the right, labeled "any other use." In frame 6, a final caption says what was not tested: how any investment compares once risk and taxes are counted.

3. Putting extra money into the mortgage saves interest at the mortgage rate, so 7.40% is the bar any other use of the money would have to beat. The dashed bill stands for an alternative, such as investing. The animation does not say whether the alternative would clear the bar. The footers say "US only · history, not a forecast," so the figure is not a prediction.

4. A viewer would not get a clear instruction to pay extra or to invest. The most they could take away is a way of framing the choice. They can compare a known, fixed saving of about 7.40% before taxes with whatever else they might do with the money. They should also remember that the animation did not test how an investment compares after risk and taxes.

5. The animation itself supplied that framing through its on-screen text: "the bar," "interest no longer charged, not an investment return," "any other use," and "not tested." It does not recommend either choice. The advice in point 4 is my reading of those captions, not something the animation states.

### R4 (strip N1-s01-stack)
1. The animation shows a homebuyer, "Tessa" (labeled illustrative), with a house and a $320,000 loan. It attaches a cost to something it calls "the fallback," which is $120 a month. The header cites the Freddie Mac weekly mortgage survey for the week of Oct 8, 2026. A caption says "US only · history, not a forecast."

2. The house and Tessa start large and close together, then shrink and shift left. A stack of gold bills appears beside the house. In frame 2 it is a single flat bundle near the house. In frame 3 it is a thin bar to the right. From frame 4 the text "$320,000 loan · week of Oct 8, 2026" and "price of the fallback: $120 a month" appears. The stack then grows taller through frames 5 and 6.

3. The most literal reading is that the fallback option costs Tessa about $120 more each month on a $320,000 loan. The growing stack shows that cost building up. The image never says what the fallback is. It might be a longer loan term or a different rate, but I can't tell from the frames. The "history, not a forecast" caption says the figure reflects past survey data and doesn't predict future rates.

4. The animation gives no explicit advice. It doesn't say to pay extra on the mortgage or to invest instead. A viewer could only infer that the fallback option costs money, and that the cost is $120 a month.

5. The animation did not suggest any advice. The only takeaway I drew from it is the inference about cost in point 4, and that comes from my own reading of the figures. The on-screen text states the cost but does not tell the viewer to do anything.

### R5 (strip N1-s23-track)
1. The animation shows an illustrative character, Tessa, with a house and a grid of blocks. Each block appears to be one monthly mortgage payment. It compares paying a 15-year mortgage in monthly installments with paying the same amount once a year, as a single lump sum of $8,792. The labels say "ILLUSTRATIVE," "US only · history, not a forecast," and "Freddie Mac weekly mortgage survey."

2. In frames 1–3, the grid of payment blocks grows and rearranges into columns. In frames 4–5, the blocks are grouped into yearly stacks, and a label appears: "$8,792 once a year." In frame 6, a few gold blocks appear at the end of the grid. The caption reads "ends in 184 months: 4 months later than monthly."

3. Paying once a year instead of monthly means the loan balance stays higher for more of each year. In the animation, that makes the payoff take 184 months instead of 180, which is 4 months later than the monthly schedule. Timing matters: the same total yearly payment, made later, costs a little more in time.

4. A viewer would probably take away that paying monthly is slightly better than saving up and paying once a year. The animation doesn't say anything about extra payments or about investing instead, so it doesn't answer your question.

5. The 184-month versus monthly comparison comes from the on-screen text. The "advice" in point 4 is my own inference from that comparison. The animation states no recommendation, and its "history, not a forecast" label signals that it isn't advising anything.

### R6 (strip N1-s01-stack)
1. **Idea:** The animation shows a cost attached to a fallback option on a home loan. A figure called "Tessa" (labeled illustrative) stands beside a house. The on-screen text says "Freddie Mac weekly mortgage survey," "$320,000 loan · week of Oct 8, 2026," and "price of the fallback: $120 a month." It also says "US only · history, not a forecast."

2. **What changes:** Frames 1–2 show only Tessa and the house, and a gold cash stack appears by the house in frame 2. In frame 3 the stack is a flat bar off to the side. Frames 4–6 add the loan amount and date at the top and the "$120 a month" label. In those frames the stack grows from a thin bar to a taller pile. The house and Tessa stay the same.

3. **Meaning:** Taking the fallback option on a $320,000 loan costs about $120 more per month, and the growing stack shows that cost building up. The animation doesn't say what the "fallback" is. It doesn't say whether it is a longer loan term, a higher rate, or something else. It also doesn't say whether the $120 is a difference between two loans or a standalone charge. The Freddie Mac label suggests the figure comes from survey rate data. The "illustrative" tags and the "history, not a forecast" caveat mean it is an example and not a prediction.

4. **Advice:** The image gives no explicit advice. A viewer might take away that the fallback option has a real monthly cost they should weigh. That is an inference from the picture. It doesn't answer your question about paying extra on the mortgage versus investing the spare cash, because nothing in the frames compares those two choices.

5. **Source:** The takeaway in 4 is my own reading. The animation shows only the $120 figure and the caveats. It doesn't tell the viewer to do anything.

### R7 (strip N1-s06-stack)
1. The animation compares a 15-year mortgage with a 30-year mortgage for an illustrative homebuyer named Tessa. It shows that you can take the cheaper 30-year loan and still pay it off in 15 years by paying extra each month. The banner says "Freddie Mac weekly mortgage survey". The footers say "US only · history, not a forecast" and the frames are labeled "ILLUSTRATIVE".

2. Frame 1 shows Tessa, a house, and two blank bars. In frame 2 the bars are labeled. The 15-year bar is $2,828 a month, and the 30-year bar is lower at a "required" $2,216 a month. Frame 3 adds a "30-year paid in 15" payment of $2,948 a month, which is $120 a month more than the 15-year payment. In frames 4 and 5, gold slabs drop from that $120 extra and pile up into a stack next to the house. In frame 6 the stack is complete and labeled "the stack: $21,622 extra paid over 15 years".

3. The 30-year loan has a lower required payment, but paying it off in 15 years costs more per month than the 15-year loan. This fits with the 30-year loan's higher interest rate. Over 15 years, that works out to about $21,622 more paid in total. The 30-year loan lets you choose to pay less in a tight month. The 15-year loan is cheaper overall but gives you no flexibility.

4. The animation gives no explicit advice. A viewer might conclude that the 15-year loan is cheaper than paying a 30-year loan down early. They might also see that the 30-year loan's lower required payment gives them room to adjust. The animation doesn't address the question of investing the spare cash instead.

5. None of that is stated on screen. The pictures and text only show the numbers, the "illustrative" label, and the "history, not a forecast" disclaimer. Any takeaway about which loan to pick is the viewer's own inference. It isn't something the animation recommends.

### R8 (strip N1-s25-bar)
1. The animation shows a way to compare paying extra on a mortgage with using the money elsewhere. A figure named Tessa, standing by a house, puts a dollar bill toward the mortgage. That payment is set against a bar labeled "7.40% a year, before taxes," which appears to be the mortgage rate from the Freddie Mac weekly survey. The idea is that any other use of the money has to beat that bar to come out ahead.

2. In frame 1, Tessa hands cash to the house. In frame 2, the bill moves up onto a flat bar. In frame 3, the bar is labeled with the 7.40% figure. In frame 4, the text says "interest no longer charged, not an investment return." In frame 5, a second, dashed bill appears off to the right, labeled "any other use." In frame 6, a caveat appears: "not tested: how any investment compares, once risk and taxes count."

3. Paying down the mortgage saves interest at the loan's rate, which here is 7.40%. That is a benchmark for comparing alternatives, not a return on an investment. The animation does not say whether any alternative beats the benchmark. It states that this comparison was not tested once risk and taxes are included.

4. The animation gives no direct advice. A viewer could take away that extra payments earn a guaranteed saving equal to the loan rate, and that an alternative has to beat that rate after risk and taxes to be worth choosing. The animation does not tell them which to pick.

5. That takeaway is my own reading. The on-screen text only sets out the 7.40% bar and the "not tested" caveat. It does not recommend paying extra or investing. The footers "ILLUSTRATIVE" and "US only · history, not a forecast" also signal that it is not advice.

### R9 (strip N1-s21-track)
1. The animation shows how paying extra on a mortgage shortens the payoff time. An illustrative homeowner, "Tessa", has a house and a grid of blocks. Each block appears to stand for one monthly payment. The labels say "Freddie Mac weekly mortgage survey", "ILLUSTRATIVE", and "US only · history, not a forecast."

2. In frames 1–3, the house sits alone and then a grid of payment blocks grows out from it. By frame 4 the grid is a full rectangle. A few gold blocks stick out at the edge of the grid. The caption says paying $2,828 on the 30-year takes "about 195 months". In frame 5 all the blocks are white, so the grid is now a uniform 180-month block. In frame 6 the caption reads "to finish in 180 months: $2,216 required + $733 a month."

3. I read the gold blocks as the months beyond 180 that Tessa would still owe if she kept paying the 30-year payment. The caption's numbers add up: $2,216 plus $733 is about $2,949, which is more than $2,828. So adding roughly $733 a month to the required payment would pay the loan off in 15 years (180 months) instead of about 16 years and 3 months (195 months). The picture suggests the extra payments cut the length of the loan. The caption never states how much interest is saved. The extra amount and the dollar figures appear to be tied to a particular loan.

4. A viewer might take away that paying extra each month shortens the loan, and that a specific extra amount would finish it by a set date. The animation does not say whether Tessa should pay extra or invest instead. It doesn't compare mortgage rates with investment returns, and it says nothing about risk, taxes, or your $320,000 loan.

5. The animation did not state any advice. The advice in 4 is my own reading of what a viewer might conclude from the picture and captions. The on-screen text only describes the numbers and warns that the content is illustrative, US-only, and historical rather than a forecast.

### R10 (strip N1-s21-track)
1. **The idea.** The animation shows how paying extra on a mortgage shortens the loan. A character named Tessa, labeled "illustrative," has a house and a grid of tiles. Each tile appears to stand for one monthly payment. The caption says the data is "US only · history, not a forecast" and credits the Freddie Mac weekly mortgage survey.

2. **What changes.** Frame 1 shows only the house and Tessa. In frames 2 and 3 a grid of tiles grows out from the house, which looks like the payment schedule being laid out. In frame 4 the grid is full and gray, with a few gold tiles along the right edge. The label reads "pay $2,828 on the 30-year: about 195 months." In frame 5 the gold tiles are gone and the grid is all white. In frame 6 the label reads "to finish in 180 months: $2,216 required + $733 a month."

3. **What it means.** Tessa's 30-year loan has a required payment of $2,216 a month. If she pays $2,828 a month instead, the loan ends in about 195 months, which is roughly 16 years. To finish in exactly 180 months (15 years), she would add $733 a month to the required $2,216. The gold tiles in frame 4 seem to show the months that extra payments cut off. The $2,216 and $733 add up to about $2,949, a little more than the $2,828 in frame 4. I'm treating that as an approximation, not an error.

4. **Advice a viewer might take.** The animation gives no direct advice. Nothing on screen says to pay extra or to invest instead. A viewer could only conclude that extra monthly payments shorten the loan and that finishing in 15 years takes a specific, larger payment. The animation never compares this with investing, so it doesn't help with your question.

5. **Source of the takeaway.** The "extra payments shorten the loan" reading comes from the picture and on-screen text, namely the shrinking grid and the month and dollar labels. Any advice beyond that would be my own conclusion, because the animation gives none. For your question, the disclaimers "illustrative" and "history, not a forecast" mean you shouldn't treat these numbers as a prediction or as proof that paying extra beats investing.
