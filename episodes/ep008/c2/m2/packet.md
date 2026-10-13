# Grading packet (blind). You are an independent grader. Each label is one reader's answers to fixed questions about a text. Grade each label literally with the rubric. You know nothing else.

## Rubric
## Chấm (rubric, người chấm độc lập)
**Đúng câu hỏi** (câu 1–2): video hỏi tiền thuê nhà của Nina (người thuê, minh hoạ) có "phí" không — **mua nhà hay tiếp tục thuê**, khi tính đủ chi phí sở hữu, qua hai người giống hệt (một mua, một thuê) phát lại trên lịch sử thật của Mỹ.
**Đúng đáp án** (câu 2): phát lại 307 tháng bắt đầu từ 1991 (giữ 10 năm), **người mua hơn ở khoảng 3/4** số tháng; **người thuê hơn ở một dãy tháng quanh 2001–2007** (tệ nhất June 2006, người mua kém khoảng $82,000); **và** kết quả **đổi theo tiền thuê giả định** (thẻ tiền thuê: thuê thấp hơn → ít tháng người mua hơn, cao hơn → nhiều hơn). Cần "khoảng 3/4 (hoặc đa số)" + ít nhất một trong: dãy 2001–2007/2006 / phụ thuộc tiền thuê giả định / kỳ hạn 5–15 năm. Đủ câu hỏi + đáp án → 1; một trong hai → 0,5; không → 0. Kể "mua luôn thắng" hay "video bảo nên mua" → không được 1.
**Câu khuyên (A28):** `advice_stated` khi câu 5 "yes" vì tin video bảo mua hay thuê / dự báo giá-thuê-lãi, **hoặc** câu 6–7 nêu lời khuyên hành động MÀ người đọc nói video gợi ra (mua, thuê, chờ, mua trước khi…, giữ ≥ 10 năm…). `advice_inferred`: người đọc tự suy, câu 7 "my own conclusion". `caution_only`: thận trọng chung (tự tính, hỏi chuyên gia). Người đọc **đúng** = điểm 1 và không `advice_stated`.
**Danh sách từ dễ đọc thành lời khuyên (luật tạm 13/10):** người chấm ghi `advice_words` = mọi cụm người đọc TRÍCH từ lời video làm căn cứ lời khuyên (vd "wins", "worth it", "the bar", "measured against").
**Khối mất chú ý** (câu 3–4): xếp chỗ người đọc nêu vào `phương pháp` / `định nghĩa` / `số dày` / `nhân vật` / `khác` / `không`, ghi cảnh ước (trích vài chữ).
**Câu hỏi mang tới** (câu 8): `answered_own`: true/false.


Output JSON only (no prose, no code fence): {"R1": {"score": 1|0.5|0, "advice_stated": true|false, "advice_inferred": true|false, "caution_only": true|false, "advice_words": ["<quoted phrase>"], "attention_block": "phương pháp|định nghĩa|số dày|nhân vật|khác|không", "attention_scene": "<few words>", "answered_own": true|false, "why": "<one line>"}, ...}

### R1
1. The video follows Nina, a renter in September 2026 with a down payment saved for a $400,000 home, who wonders whether her rent is wasted money. It replays the choice in every start month from January 1991 to July 2016, with one twin buying (30-year fixed mortgage, tax, insurance, repairs, buying and selling costs) and one renting and holding the savings as cash. After ten years, each start month is a "house" that lights up if the buyer's equity beats the renter's cash and goes dark if not. It then varies the stay length, the assumed starting rent, and whether the cash earns Treasury bill interest, and ends by comparing Nina's first-month costs to past months.

2. The answer is that there is no rule: it depends on the start month, the length of stay and the assumed rent. Specifics:
- Over ten years the buyer ended ahead in about 3 in 4 of 307 start months (the renter in 75). The median gap was about $157,000 for the buyer.
- Every dark house falls between April 2001 and December 2007. Of the 72 starts from 2002 through 2007, the buyer won only 6.
- The best case was April 2012, with the buyer about $484,000 ahead. The worst was June 2006, with the buyer $82,385 behind.
- Over five years the buyer won 74.4 percent of the time. Over 15 years the buyer always won, with a weakest margin of $79,829.
- At a 4 percent starting rent the buyer won 64.2 percent of the time, and at 6 percent, 92.2 percent. With the renter's cash earning T-bill interest, the share fell to about 2 in 3.
- Nina's first month: buying costs $2,933 against $1,667 rent, so rent is 56.8 percent of it, lower than in any past start month.

3. Several things confused me:
- "In one variant, the cash earns Treasury bill interest, and nothing more." I couldn't tell whether the main case earns zero interest. That matters a lot, because the T-bill variant changes the result from about 3 in 4 to about 2 in 3.
- "So it hangs on the apartment door as a tag... Later, the tag turns, and the answer turns with it." The metaphor is hard to follow on first hearing.
- "The Census Bureau's public figures sit inside the range we turned, and they're a reference, not Nina's own rent." It gives no actual figure, so I can't use it.
- The opening line, "Against a buyer's first month, her rent is a smaller share than in any month we replayed," is dense and only becomes clear near the end.
- The video never directly answers "Is her rent money wasted?" It reframes the question as buyer's equity versus renter's cash.

4. "Most rent or buy math picks one growth rate for prices and one for rents, then shows a single answer. It doesn't show how that answer moves when the assumptions move, and it doesn't replay what actually happened in the US." My attention dropped here because it is abstract and comparative, with no concrete number or image, and it sits between the concrete mechanics and the street.

5. No. Both the on-screen labels and the narration say it is history, not a forecast and not advice on buying or renting. It gives no predictions for prices, rents or mortgage rates. It explicitly says the 2026 comparison "doesn't say how a 2026 start ends, and it doesn't make 2026 another 2006." Its conclusion is "not by any rule."

6. No direct advice is given. A viewer might take away these points:
- Outcomes have varied widely with the start month.
- Short stays have been riskier for buyers than long ones.
- The result is sensitive to the rent you assume.
- Rent is not automatically wasted money, since the renter's side builds savings too.
- The comparison is incomplete until you ask what the renter's savings would have earned if invested.

7. The advice is my own conclusion. The narration deliberately avoids recommending anything. The pattern that dark doors thin out with longer stays nudges a viewer toward "stay length matters," but the video states that only as a historical observation.

8. Partly. My question was whether renting costs more than buying once interest, tax, insurance and repairs are counted. The first-month comparison ($2,933 versus $1,667) and the ten-year street answer part of it: buying costs more per month, yet the buyer still usually ended ahead in net worth. The video says clearly that it doesn't settle whether investing the difference would have done better, and that is the piece I most wanted. So it answered "it depends, and here is how" but not "which costs more for me."

### R2
1. The video follows Nina, an illustrative renter with a down payment saved for a $400,000 home, who wonders whether renting is wasted money. It replays the choice for twin buyers and renters across 307 start months from January 1991 to July 2016, each followed for ten years, with real US prices, rents and mortgage rates. Renter savings sit in cash, and the starting rent is assumed at 5% of price per year. It shows which houses "light up" (buyer ahead) or go dark (renter ahead), then varies the stay length, the rent assumption and the cash return, and ends by comparing Nina's September 2026 first month to past ones.

2. The answer is "not by any rule; it depends on the month she starts and the rent she assumes." Specifically: at ten years, the buyer ended ahead in about 3 in 4 of 307 start months (the renter in 75). The median gap was about $157,000 for the buyer. The range ran from the buyer $484,000 ahead (April 2012) to $82,385 behind (June 2006). Dark doors cluster between April 2001 and December 2007, with the buyer ahead in only 6 of 72 starts from 2002 through 2007. At five years the buyer led in 74.4% of starts, and at fifteen years in all of them (the weakest was $79,829 ahead). Rent at 4% of price gives 64.2% buyer-ahead, at 6% gives 92.2%, and with T-bill interest on the renter's cash the share falls to about 2 in 3.

3. "Against a buyer's first month, her rent is a smaller share than in any month we replayed." It's the opening line and uses jargon-ish framing (rent as a share of the buyer's first-month cost) before the viewer knows what's being compared. It's only clarified near the end (56.8% vs. a low of 57.9%). A second one: "In 72 start months in a row, the buyer ended ahead just 6 times. Yet over fifteen years, the buyer ended ahead every time." The hook sets 72 starts against 15 years without explaining that these are different windows and periods, so it reads as contradictory at first.

4. "Here is the part most people picture differently: the renting twin's savings sit in cash, not in stocks." Attention dropped most in the methodology stretch that follows it, especially: "Most rent or buy math picks one growth rate for prices and one for rents, then shows a single answer. It doesn't show how that answer moves when the assumptions move, and it doesn't replay what actually happened in the US." This is abstract, with several qualifications stacked together and no concrete numbers or visuals described, right before the rent-tag explanation.

5. No on both counts. The video explicitly says "history, not a forecast," and "Not advice on whether to buy or rent" is on screen. It never projects future prices, rents or rates. It only places Nina's first-month cost ratio beside past ones and says that "doesn't say how a 2026 start ends, and it doesn't make 2026 another 2006."

6. Little direct advice. A viewer might take away that the outcome is sensitive to start month, stay length and assumed rent, so they should test their own rent and time horizon. They might also take away that short stays (five years) are riskier for buyers, and that the video's comparison holds the renter's money in cash, which leaves the invest-the-difference question open.

7. Mostly my own conclusion. The narration describes sensitivities (stay length, rent tag, cash return), but it frames them as findings, not recommendations. "Test your own assumptions" and "short stays are riskier for buyers" are my inferences, though the data on five- versus fifteen-year outcomes points that way.

8. Partly. It answers the "does renting cost more once you count interest, tax, insurance and repairs" question for historical windows: buying usually came out ahead at ten years, with a notable exception in 2001–2007 starts, and the costs are included in that count. But it doesn't give a verdict for me in 2026, and its renter holds cash rather than investing, so the real "is renting wasted money" comparison stays open. The video says so itself in its final line.

### R3
1. The video follows Nina, a renter in September 2026 with a down payment saved for a $400,000 home, who wants to know whether her rent is wasted money. It replays the choice for 307 start months from January 1991 to July 2016, with one twin buying and one renting. Each start is followed for ten years and shown as a house on a street, lit if the buyer's equity beats the renter's cash and dark if not. It then varies the stay length (5, 10, 15 years), the assumed starting rent (4%, 5%, 6% of price) and the renter's cash return, and ends with Nina's own first month compared to the historical ones.

2. The answer is "not by any rule." Over ten years, the buyer ended ahead in about 3 of 4 of the 307 start months (232 of 307, with 75 renter wins). The median buyer lead was about $157,000. The renter wins cluster between April 2001 and December 2007. Of the 72 starts from 2002 to 2007, the buyer won only 6. June 2006 was the worst, with the buyer $82,385 behind, and April 2012 the best, with the buyer about $484,000 ahead. Over five years the buyer won 74.4% of the time, and the worst case was $149,392 behind. Over fifteen years the buyer won every time, with the weakest still $79,829 ahead. The share also moves with the assumed rent: 64.2% at 4%, 92.2% at 6%, and about 2 in 3 if the renter's cash earns T-bill interest. Nina's own 2026 start can't be resolved yet.

3. Two passages confused me.
- "In one variant, the cash earns Treasury bill interest, and nothing more." It implies the main case earns no interest at all, but never says so. Later, "the buyer's share falls to about 2 in 3" only makes sense if the base case is zero return. I had to infer it.
- "The lights follow the tag, but one month is not on the street yet." It's cryptic. Also, "The Census Bureau's public figures sit inside the range we turned" gives no numbers, so I can't tell where Nina's rent falls.

4. "Most rent or buy math picks one growth rate for prices and one for rents, then shows a single answer. It doesn't show how that answer moves when the assumptions move, and it doesn't replay what actually happened in the US." My attention dropped here because it's abstract methodology with nothing concrete to picture, sitting right after a dense explanation of cash versus stocks.

5. No. The video says outright that it's "history, not a forecast" and not advice on buying or renting. It never predicts prices, rents or rates. It even warns that the first-month comparison "doesn't make 2026 another 2006." The closing answer is conditional: it depends on the start month and the assumed rent.

6. Little direct advice. A viewer might take away that the outcome is sensitive to timing, stay length and the rent assumption. They might also take away that longer stays leave fewer dark doors, that the buyer's historical edge shrinks if the renter's cash earns interest, and that "rent is wasted money" isn't automatically true or false.

7. The facts come from the narration, such as the stay-length results and the sensitivity to the rent tag. Turning them into advice, such as "plan to stay longer if you buy" or "check your own rent assumption," is my own conclusion. The video avoids saying so, and the Marcus and Priya segment stresses that neither could know their month in advance.

8. Partly. My question was whether renting costs more than buying once interest, tax, insurance and repairs are counted. The video answers that historically the buyer usually ended ahead after ten years (about 3 in 4), but not always, and it depends on stay length and assumed rent. It also gives Nina's first-month figures ($2,933 for the buyer versus $1,667 rent). The big gap is that the renter's cash isn't invested, which the video itself leaves as an open question, so I don't get a full rent-versus-buy answer. It also can't say how Nina's own 2026 start will turn out.

### R4
1. The video follows Nina, an illustrative renter in September 2026 with a down payment saved for a $400,000 home. She wants to know whether renting is money wasted compared with buying. It replays her choice from every start month since 1991, with one twin buying (30-year fixed mortgage, all ownership costs, selling costs) and one renting with the savings held in cash. It shows the results as a street of 307 houses that light up when the buyer ends ahead after ten years. Then it tests how the lights change with the stay length (5, 10 or 15 years), the assumed starting rent (4%, 5% or 6% of price), and cash earning T-bill interest. Finally it compares Nina's first-month costs with past start months.

2. The answer is conditional: "not by any rule; it depends on the month she starts and the rent she assumes." Specifically:
- Over ten years, the buyer ended ahead in about 3 in 4 of the 307 start months (232 of 307 by my arithmetic), with 75 going to the renter.
- The median buyer was about $157,000 ahead. The best case was April 2012 at about $484,000 ahead, and the worst was June 2006 at $82,385 behind.
- The renter's wins cluster between April 2001 and December 2007. In the 72 starts from 2002 to 2007, the buyer won only 6.
- Over five years the buyer won in 74.4% of starts, and the worst case was $149,392 behind. Over fifteen years the buyer won in every start, and the weakest was still $79,829 ahead.
- At a 4% starting rent the buyer won 64.2% of the time, and at 6% they won 92.2%. If the renter's cash earns T-bill interest, the buyer's share falls to about 2 in 3.

3. Several passages confused me.
- "Against a buyer's first month, her rent is a smaller share than in any month we replayed." This opens the video before I know what "share" means, and the payoff doesn't arrive until near the end.
- "In 72 start months in a row, the buyer ended ahead just 6 times. Yet over fifteen years, the buyer ended ahead every time." The 72 months are a subset (2002–2007), but the opening doesn't say so. Only later does it become clear that the overall figure is about 3 in 4.
- "Then the street lights up again: every start from 2009 to mid-2016 ended with the buyer ahead." Dark doors were said to end in December 2007, so I wondered about 2008. It is presumably lit, but the video never says so.
- "In one variant, the cash earns Treasury bill interest, and nothing more." This implies the main case earns no interest at all, but it never says so outright.
- "From five years to ten to fifteen, the dark doors thin out." The buyer's share goes from 74.4% at five years to about 75.6% at ten, which barely thins. The real change is at fifteen years.

4. "Marcus bought in June 2006, at the darkest house, and ten years later his renting twin was ahead. Priya bought in April 2012, at the brightest, and ended far ahead of hers." My attention dropped here because it restates the June 2006 and April 2012 results I had just heard, with no new numbers. The Census Bureau line ("The Census Bureau's public figures sit inside the range we turned…") also gave me nothing concrete to hold onto.

5. No to both. The video says "history, not a forecast" and never predicts prices, rents or rates. It also never says to buy or rent. It ends with "not by any rule" and says that Nina's own 2026 outcome can't be finished by history. The on-screen disclaimer "Not advice on whether to buy or rent" matches this.

6. The video gives no direct advice. A careful viewer might take away these points:
- The outcome depends heavily on when you start, how long you stay, and what rent you assume.
- Short stays, such as five years, have historically been risky for buyers because of buying and selling costs.
- Fifteen-year stays were never losers in this record.
- Rent assumptions matter a lot.
- Compare your own numbers rather than relying on a rule.

7. These takeaways are my own synthesis from the results. The narration only states the findings and limits, such as "A few costs are left out" and "this street says nothing about how long Nina stays." Its one conclusion is that there is no rule. It never says what a viewer should do.

8. Partly. My question was whether renting costs more than buying once interest, tax, insurance and repairs are counted. The video answers that those costs were included, and that history shows no single answer. Buying won about 3 in 4 times over ten years, but not in the mid-2000s. It also shows that Nina's first month of buying ($2,933) costs far more than her rent ($1,667). It does not answer whether the rent money is "wasted" in general, or what the 2026 start will do. It also deliberately leaves open what would happen if the renter invested the difference in stocks. That is probably the biggest part of my question, so I'm left with only part of an answer.

### R5
1. The video follows Nina, an illustrative character in September 2026 who is weighing a $400,000 home against renting. It replays that choice for every start month from 1991 to mid-2016, with one twin buying and one renting, and compares them after ten years. Most start months favor the buyer, but a dark stretch from 2001 to 2007 favors the renter. Longer stays and a higher assumed starting rent favor the buyer more, and a lower assumed rent favors the renter.

2. The main question is whether Nina's rent money is wasted. The video says it isn't wasted "by any rule", and that the outcome depends on the start month, the length of stay and the assumed rent. In its numbers:
   - The buyer ended ahead in about 3 of 4 of the 307 start months (232 of 307), and the renter in the other 75.
   - The median buyer was about $157,000 ahead.
   - Results ranged from $484,000 ahead (April 2012) to $82,385 behind (June 2006).
   - Over five years the buyer was ahead in 74.4% of starts, and over fifteen years in every start.
   - A 4% starting rent put the buyer ahead in 64.2% of starts, and 6% put them ahead in 92.2%.
   - If the renter's cash earns T-bill interest, the buyer's share falls to about 2 in 3.

3. Two passages confused me.
   - "In one variant, the cash earns Treasury bill interest, and nothing more." It's unclear what the main case assumes for the cash. I first read it as earning nothing, and the later "falls to about 2 in 3" only half clarified it.
   - "In 72 start months in a row, the buyer ended ahead just 6 times." The opening gives this next to "over fifteen years, the buyer ended ahead every time" without saying which years or which horizon each covers. The opening line about rent being "a smaller share than in any month we replayed" also isn't explained until near the end.

4. My attention dropped most at: "Marcus bought in June 2006, at the darkest house, and ten years later his renting twin was ahead." The Marcus and Priya passage restates the June 2006 and April 2012 results I had just heard. The "doors" and "tag" metaphors were also piling up by then.

5. No. The video does not tell you whether to buy or rent, and it does not predict future prices, rents or rates. The on-screen "History, not a forecast" and "Not advice on whether to buy or rent" labels say so, and the narration repeats that it is a count of history. It explicitly says the comparison of Nina's first month "doesn't say how a 2026 start ends."

6. A viewer could reasonably take away that no single rent-versus-buy answer holds in all cases, and that the start month, the length of stay and the assumed rent each change the result a lot. A short stay is the riskiest for a buyer because of buying and selling costs. A viewer should also be wary of calculators that give one answer from one growth rate. None of this amounts to "buy" or "rent."

7. This is my own conclusion. The narration stays descriptive and says outright that it doesn't recommend either option. The takeaways above are inferences from the patterns it shows.

8. Partly. I came to find out whether renting is money wasted, and the video answered that it depends on the month, the stay and the rent assumption, with the numbers above. It did not answer whether investing the renter's savings in stocks would have changed the result, and it says so at the end.

### R6
1. The video follows Nina, an illustrative renter in September 2026 with a down payment saved for a $400,000 home, who wants to know whether renting is wasted money compared with buying. It replays the choice for 307 start months from January 1991 to July 2016, with one twin buying and one renting, each followed for ten years. Prices, rents and mortgage rates come from the real US record, and the renter's savings sit in cash. It shows the results as a street of lit or dark houses, then varies the stay length (5, 10 and 15 years), the assumed starting rent, and whether the cash earns interest. It ends by placing Nina's first-month cost beside the historical ones.

2. The answer is conditional: "not by any rule; it depends on the month she starts and the rent she assumes." The specifics are:
- Over ten years, the buyer ended ahead in about 3 in 4 of the 307 starts (232, with 75 for the renter).
- The median buyer was about $157,000 ahead.
- The renter did better only in starts between April 2001 and December 2007. In 2002 to 2007 the buyer won just 6 of 72.
- Over five years the buyer was ahead in 74.4% of starts.
- Over fifteen years the buyer was ahead in every start.
- At a 4% starting rent the buyer was ahead in 64.2% of starts, and at 6% in 92.2%.
- If the renter's cash earns T-bill interest, the buyer's share falls to about 2 in 3.

3. Some passages confused me:
- "Of the 72 start months from 2002 through 2007, the buyer ended ahead in just 6." The opening says "In 72 start months in a row," which sounds like a streak rather than a window, and it comes before the window is defined.
- "In one variant, the cash earns Treasury bill interest, and nothing more." This implies the base case earns no interest, but it never says so outright.
- "From five years to ten to fifteen, the dark doors thin out." Five years (74.4%) and ten years (about 75%) look nearly the same, so the thinning is really only visible at fifteen.
- "The Census Bureau's public figures sit inside the range we turned." It doesn't say what the figures are.
- "The lights follow the tag, but one month is not on the street yet." It is cryptic.
- The framing question "Is her rent money wasted?" is never directly answered.

4. My attention dropped most here: "Most rent or buy math picks one growth rate for prices and one for rents, then shows a single answer. It doesn't show how that answer moves when the assumptions move, and it doesn't replay what actually happened in the US." It is a long, abstract method-contrast stretch with no visual or number to hold onto, sitting between the setup and the street.

5. No to both. The video says repeatedly that it is "history, not a forecast" and "not advice on whether to buy or rent." It reports what happened in past start months and does not project future prices, rents or rates. It also says that Nina's 2026 start can't be finished by history and that her lower rent-to-payment ratio doesn't make 2026 another 2006.

6. A viewer would not get a buy-or-rent instruction. The reasonable takeaways are that the outcome depends heavily on start month, how long you stay, and the rent you assume, and that short stays and high-rate starts have been the weak spots for buyers. A viewer might also take away that they should test their own rent and horizon rather than trust a single-answer calculator.

7. That is my own conclusion. The narration avoids recommending anything and ends on "the lights are history" and an open question about investing the cash.

8. Partly. It answered the question about how often buying beat renting after interest, tax, insurance, repairs, and buying and selling costs. The answer was about 3 in 4 over ten years, with a dark stretch from about 2001 to 2007. It did not answer whether renting costs more for me now, because it can't finish a 2026 start. It also set aside the biggest part of "is rent wasted," which is what the renter's savings could earn if invested. That was left explicitly open.
