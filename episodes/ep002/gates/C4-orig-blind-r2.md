# C4 gốc · vòng 2 — Kiểm mù tắt tiếng, giữ chữ/số, sau khi thêm nhãn nghĩa (01/10/2026)

Ý đồ: `gates/C4-orig-intent.md` + `gates/C4-orig-intent-r2.md` (commit dbc55a6, trước khi sửa và chạy). Mẫu: `animatic/strips/KEY-n.png` sau sửa (d7be5d5). Khoá mẫu: `review-c4/orig-r2-blind-key.json`. Người chấm: agent độc lập mới, mù tập; gói `review-c4/orig-r2-packet.json`, khoá rubric `review-c4/orig-r2-rubric-key.json` (commit 4b070c0, trước khi chấm); điểm: `review-c4/orig-r2-scores.json`. P không chấm.

| Nhịp | Điểm (/3) | Câu khuyên | Đọc đúng? | Đối chứng Tập 1 (/1) |
|---|---|---|---|---|
| KEY-1 | 3 | 1 | ✗ (điểm đủ, có câu khuyên) | 1 |
| KEY-2 | 3 | 1 | ✗ (điểm đủ, có câu khuyên) | 1 |
| KEY-3 | 2 | 0 | ✓ | 1 |
| KEY-4 | 1.5 | 2 | ✗ | 0.5 |
| KEY-5 | 3 | 0 | ✓ | 1 |
| KEY-6 | 3 | 1 | ✗ (điểm đủ, có câu khuyên) | 1 |
| KEY-7 | 1.5 | 0 | ✗ | 1 |

**Nhịp đọc đúng: 2/7. Ngưỡng ≥ 6/7 → TRƯỢT.**

## Nguyên văn và điểm

**Tập 2 · KEY-1 · 9f8bc67f** · điểm 1 — Fixed 9% vs variable 7.5% starting lower then swinging.

The section compares two private loan options, a 9% fixed rate (a flat line that never changes) and a 7.5% variable rate (a line that starts lower, then rises and swings up and down, eventually passing above the 9% fixed line). It means a variable loan looks cheaper at first, but its rate can climb past the fixed rate later, so you take on the risk of unpredictable, possibly higher costs (the chart is labeled illustrative).

**Tập 2 · KEY-1 · 7f073ca5** · điểm 1 · CÂU KHUYÊN — Fixed 9% vs variable starting lower then swinging above.

The section compares a 9% fixed-rate loan (a flat line that never changes) with a 7.5% variable-rate loan (a line that starts below the fixed rate, then drifts up and swings erratically, eventually rising above the 9% line). It means a variable rate can look cheaper at first but is unpredictable and may end up costing more than a fixed rate, so the lower starting rate is a gamble (the charts are labeled "illustrative").

**Tập 2 · KEY-1 · 7e70570b** · điểm 1 — Fixed 9% vs variable starting lower then up and down.

The section compares two private-loan options, a 9% fixed rate (a flat line that never changes) and a 7.5% variable rate (a line that starts slightly below the fixed line, then swings up and down and ends above it). The point is that a variable rate may look cheaper at first, but over time it can rise above the fixed rate, so it carries uncertainty and risk, while the fixed rate stays predictable. The frames are marked "illustrative", so the curve is an example, not real data.

**Tập 2 · KEY-2 · e2fad8b3** · điểm 1 — Head start fixed minus variable; shrinks to zero then reverses.

The section compares two loan offers, a 9% fixed rate versus a variable rate that starts lower, and defines the "head start" as fixed minus variable, which here is about 1.5 percentage points. Over time that head start shrinks to zero and then reverses (the bar turns from teal to yellow on the other side of the line). So a variable rate that looks cheaper today can end up costing more than the fixed rate if rates rise, and the initial savings are not guaranteed. The graphic is labeled "illustrative".

**Tập 2 · KEY-2 · 52ae651f** · điểm 1 · CÂU KHUYÊN — Head start = fixed minus variable; shrinks to zero, then negative.

The section compares a 9% fixed-rate loan offer with a variable-rate offer: the variable rate starts below the fixed line, giving a "head start" of about 1.5 points (fixed minus variable), but over time the variable rate rises, the gap shrinks to nothing, and then it goes above the fixed rate (shown in orange). This means a variable loan's initial savings are only temporary and can turn into a higher cost than the fixed rate, so you shouldn't choose a private loan on the teaser rate alone.

**Tập 2 · KEY-2 · 019d850f** · điểm 1 — Head start fixed minus variable ~1.5; shrinks to zero then flips.

This section compares two loan offers, a 9% fixed rate versus a variable rate. The "head start" is the fixed rate minus the variable rate: the variable loan starts about 1.5 points cheaper than the 9% fixed. In the last frames that gap shrinks to zero and then flips (the bar turns amber), so the variable rate rises above the fixed rate and the early advantage disappears, meaning a variable loan can end up costing more than the fixed one over time. The figures are labeled "illustrative."

**Tập 2 · KEY-3 · 9e42483e** · điểm 0.5 — Above-fixed share stated; misses that few cost more in total.

This section shows a historical, illustrative look at interest rates from 1954 to today, testing many past loan start dates (one square per start month) to see whether a variable-rate loan would have ended up costing more than a fixed rate. At first every start date is grey, then the ones where the variable rate went above the fixed rate turn red (76.2% in frame 1 for one rate and 28.4% falling to 3.5% as the fixed rate or comparison is adjusted in frames 4-6). The takeaway is that whether variable beats fixed depends heavily on when you borrow and on the fixed rate you compare against, since red outcomes cluster around the high-rate 1970s-80s era and shrink to a small share as the comparison changes.

**Tập 2 · KEY-3 · 02eeb857** · điểm 1 — Variable often goes above fixed; only small share worse overall.

This section uses an illustrative interest-rate history (1954 to today, peaking around 1981) where each small square is a historical starting period for a loan: it opens with "76.2% went above the fixed rate" (a variable rate rising above a fixed one at some point), then recolors the squares red for the periods that turn out bad, and the red share shrinks from 28.4% to 3.5%, clustered around the 1970s-80s rate spike. The takeaway is that a variable rate often drifts above a fixed rate at some point, but the cases where it actually leaves the borrower worse off overall are much rarer and come mostly from extreme rate spikes. I'm unsure of the exact condition behind the 28.4% and 3.5% figures, since the sound is off.

**Tập 2 · KEY-3 · 44ce56f8** · điểm 0.5 — Few cost more overall correct; misreads 76.2% as variable beating fixed.

This section shows an illustrative history of interest rates from 1954 to today, where each square is a period in which a loan was taken out. It starts at 76.2% of the periods going above the fixed rate and shrinks to 3.5% as the red squares fade, so the large red clusters around 1981 are the rare, extreme-rate periods where a variable-rate loan would have cost more than a fixed one. In other words, variable rates beat or matched the fixed rate in most historical periods, though a few periods of high rates were costly.

**Tập 2 · KEY-4 · a0eab513** · điểm 0.5 — Bucket fills below, drains above; cost-only-when-empty condition missing.

This section compares a fixed 9% loan rate (flat line) with a variable rate that moves over time: the variable rate starts slightly below 9% (teal, saving money, filling a "bucket" of savings), but then rises far above 9% in a big spike (orange/gold, with the bucket draining and a red "not to scale" overflow of extra cost), and the last frame shows the fixed-rate line as the stable alternative. It means a variable-rate private loan can look cheaper at first but can end up costing much more if rates climb, whereas a fixed rate gives predictable cost; the illustration is hypothetical ("ILLUSTRATIVE").

**Tập 2 · KEY-4 · f1fa4607** · điểm 0.5 · CÂU KHUYÊN — Tank fills below/drains above; 'costs more only when empty' not stated.

This section compares a 9% fixed-rate loan (the flat line) with a variable rate that moves over time. Early on the variable rate dips below 9% and the "savings tank" fills. In one illustrative path it then spikes well above 9% (orange), which wipes out the savings and drains the tank, with a red "not to scale" block marking a loss that is far larger than the savings. In another path it stays below 9% for a long stretch and saves a lot (frame 6). The idea is that a variable rate offers limited, uncertain upside but open-ended downside risk, so a fixed rate trades some possible savings for certainty. The frames are labeled "illustrative," so they are not real rate data.

**Tập 2 · KEY-4 · f32da2ab** · điểm 0.5 · CÂU KHUYÊN — Savings tank fills below, drains above; empty-tank condition not stated.

The section tracks a variable interest rate against a 9% fixed-rate line over time: while the variable rate stays below 9%, the savings (green) pile up in a "tank", but a later rate spike above 9% (orange) drains the tank and, drawn "not to scale", can cost far more than all the earlier savings (red overflow). It means a variable-rate private loan may look cheaper for a while, but the occasional big spike can wipe out those gains, so the fixed rate buys protection from that risk (the graphic is only illustrative).

**Tập 2 · KEY-5 · 4618c4c3** · điểm 1 — Loan replayed for each start month since 1954, outcomes stacked by start.

The section replays a hypothetical loan ("Leah's loan") over every 10-year window since January 1954: a sliding box moves along a rate-style time-series chart (which peaks around 1981 and is high again recently), and for each start month it traces how the loan would have played out over its 10 years, building up a stack of outcomes for every start month. It means that the result of a variable-rate loan depends heavily on when you happen to borrow, so one scenario isn't representative and you need to look at the whole range of historical start dates (the chart is labeled illustrative).

**Tập 2 · KEY-5 · 0f315c5c** · điểm 1 — Same loan replayed from every month since 1954; one outcome per start.

The section replays a hypothetical borrower's (Leah's) loan over a sliding 10-year window, starting from every month since January 1954, against a long-run line that appears to be an interest-rate history. The window moves across the history and each 10-year stretch is stacked up as one outcome, showing that how the loan fares (rates above or below a reference line, with a few periods highlighted) depends heavily on when you happen to borrow, so private-loan costs can vary a lot by timing. The graphic is marked "illustrative," and I can't read exact numbers or the precise measure from the image.

**Tập 2 · KEY-5 · acf0baea** · điểm 1 — Same loan replayed every start month since 1954, outcomes stacked.

The section replays the same loan (Leah's) over a sliding 10-year window, starting from every month since January 1954, against a line chart that appears to be an interest rate or cost history. The window moves along the timeline and, in the last frame, the outcomes of all those start months are stacked up in a grid. The point is that how a loan turns out depends heavily on when it starts, so you should look at the whole range of historical start dates and not just one scenario (the graphics are labeled "illustrative").

**Tập 2 · KEY-6 · a240959b** · điểm 1 — Worst case April 1977, variable pays ~43% more than fixed.

This section replays a worst-case historical stretch starting April 1977, where a rate line (peaking around 19.3%) rises and falls over time. It compares a variable-rate loan with a fixed-rate loan: the variable-rate borrower ends up paying about 43% more than the fixed-rate one (the stacks grow from about $26,005 to a taller red-topped stack), meaning a variable rate can cost far more in a bad rate environment than locking in a fixed rate. The figures are labeled "illustrative."

**Tập 2 · KEY-6 · 6f0afd6f** · điểm 1 — Worst case April 1977; variable pays ~43% more than fixed.

This section replays the worst historical case (starting April 1977, when rates spiked to a peak of 19.3%) to compare a variable-rate loan with a fixed-rate one. As the rate line rises and falls over time, the variable-rate borrower ends up paying far more in total, about 43% more than the fixed-rate borrower (a stack of roughly $26,005 versus a taller stack with an extra red layer). The point is that variable-rate loans carry the risk of rate spikes that can substantially raise the total cost of borrowing.

**Tập 2 · KEY-6 · a9d8fb15** · điểm 1 · CÂU KHUYÊN — Worst case April 1977, rates climb; variable ~43% more interest.

This section replays a worst-case historical scenario starting April 1977, when interest rates climbed to a peak of 19.3%, and compares a variable-rate loan to a fixed-rate one. Over time the rate line rises and falls, and the variable-rate borrower ends up paying about 43% more in interest than the fixed-rate borrower (about $26,005 at the fixed rate, with red extra blocks on top for the variable loan). The point is that a variable rate can cost far more if rates spike, so a fixed rate is protection against that risk. The "illustrative" tag means the numbers are a simplified example, not a forecast.

**Tập 2 · KEY-7 · aba3fe66** · điểm 0 — Reads frames as rate flip over time, not head start; era meaning wrong.

This section compares how often loans "cost more" (variable rate versus a 9% fixed rate) for borrowers who start in 1954-1980 versus 1981 on, using an illustrative rate band that shifts over time. In the early frames the variable rate sits below the 9% fixed rate and only a small share of starts cost more (8.8%, then 4.5%, then 10.5%). When the band flips above the fixed rate (frame 5), the share jumps to 72.9% of starts, and the earlier starters are hit hardest. In other words, whether a variable rate beats a fixed rate depends heavily on rate-environment timing, and a variable rate can go from cheaper to costlier for most borrowers.

**Tập 2 · KEY-7 · 7bb4fb19** · điểm 0.5 — Bigger head start pays off; era difference (1981 clean) not stated.

This section compares a 9% fixed rate with a variable rate (an "illustrative" gap of about 1.5 points) and asks, as the variable rate's head start over the fixed rate grows, what share of historical loan starts ended up costing more, split into 1954-1980 and 1981-on. The percentages move as the head start changes (a few percent, up to 72.9% of all starts in the last frame where the bar flips to a different color), which suggests that a variable rate that looks cheaper only pays off if its head start is big enough to cover the rate rises that happened in some eras. I can only partly tell what "cost more" refers to, so this reading is tentative.

**Tập 2 · KEY-7 · 7ba9068d** · điểm 1 — Bigger head start fewer cost more; 1981-on none, 1954-80 never clean.

It compares a 9% fixed rate with a variable rate that starts about 1.5 points lower (a "head start"), and shows the share of loan starts where the variable rate ends up costing more, for 1954-1980 versus 1981 on. A bigger head start leaves almost no starts costing more (8.8%, then 4.5%, then 10.5% for 1954-1980, and none for 1981 on), but when the variable rate rises above the fixed rate (frame 5), most starts cost more (72.9% overall), so the variable rate's cheaper start is no guarantee because the rate can rise later.

**Đối chứng Tập 1 · KEY-1 · 78d59119** · điểm 1 — Fell to 5.98% then above 7%; $459/month saving missed.

Mortgage rates fell to about 1 point below Nora's 7.62% locked-in rate (down to 5.98% by Feb 2026), which would have cut her payment by $459 a month, but that "window" to refinance closed after July 2026 as rates climbed back above 7% (7.03% by late September). The point is that a favorable rate opportunity can be temporary, and waiting or missing it makes the savings vanish.

**Đối chứng Tập 1 · KEY-2 · 61f74f03** · điểm 1 — 1-point line, 29 weeks, 1.64 max, closed July, history not forecast.

The section charts the weekly US 30-year mortgage rate against a borrower's (Nora's) 7.62% rate, showing that for 29 weeks in 2026 market rates sat at least 1 point below hers, reaching a maximum gap of 1.64 points at the low (5.98%). By late July 2026 rates had climbed back up and that refinancing "window" had closed, so the point is that a good opportunity to refinance to a lower rate existed but was missed or has passed, and it is only history, not a forecast of what comes next.

**Đối chứng Tập 1 · KEY-3 · d4065374** · điểm 1 — 3-year test, opposite verdicts 0.59 vs 24 months, both incomplete.

The section asks whether paying refinancing fees is worth it: it lays out a timeline (refinance until she sells or moves, tested at a 3-year stay) and then compares two quick tests. The 1-point rate-cut rule says NO (her cut is only 0.59 points, short of the 1-point line), while simple division of the fees by the monthly savings ($5,124 ÷ $221, about 24 months) says YES, so the two rules give opposite verdicts. The last frames flag that each shortcut leaves something out (the $5,124 bill is "not counted" in the 1-point rule, and the division has "something left out"), meaning neither quick answer is the full story.

**Đối chứng Tập 1 · KEY-4 · f671fca7** · điểm 0.5 — Clock restart and month 30 stated; $1,133 extra owed missing.

The section shows that refinancing a mortgage restarts the 30-year clock: after 35 payments on the old loan, each payment pays down more principal, but a new loan goes back to paying mostly interest, so it pays down less each month. The upfront loan costs ($5,124) are only recovered through the monthly savings (+$221 a month) at about month 30, not month 24. Refinancing therefore pays off only if you stay in the loan past that break-even point.

**Đối chứng Tập 1 · KEY-5 · 4628f817** · điểm 1 — Wide cost range $3,443-$8,270; viewer's own number will differ.

The section builds up a picture of what a refinance costs: it starts with the 2025 median bills ($3,443 to $8,270, with the example borrower Nora at $5,124, near the low end of the middle half of all bills). Then it layers on the factors that make your own number differ (your rate, bill and balance, fees added to the loan, a shorter term). The point is that these are illustrative national medians, and your own cost will come from different math, so you shouldn't treat the averages as your outcome.

**Đối chứng Tập 1 · KEY-6 · d212d1ef** · điểm 1 — $1,777 short, needs 1.12 points, small loans need bigger cut.

This section shows an illustrative borrower, Walt, whose small $68/month savings from a lower rate build up slowly over 3 years but still leave him $1,777 short of covering his $3,667 in loan costs plus the amount still owed. To pay that back within 3 years he would need a rate cut of 1.12 points, more than the 1-point line. The smaller the loan (Walt's $115,000 versus Nora's $375,000, who needs only 0.5 point), the bigger the rate cut needed, because the savings shrink while the costs barely shrink.

**Đối chứng Tập 1 · KEY-7 · 068f61e2** · điểm 1 — Three thresholds by loan size, 1-point fits none, your loan prompt.

The section shows that refinancing only pays off if the rate drops by enough to recover the closing fees within 3 years, and that the required rate cut shrinks as the loan gets bigger: about 1.12 points for a $115,000 loan, 0.5 point for $375,000 and about a third of a point for $655,000. It ends by asking where your own loan falls, noting that a "1-point rule of thumb" fits none of these examples (the offer shown cuts 7.62% to 7.03%, about 0.6 point, with $5,124 in costs).

## Kết luận (theo lệnh C4c, không hỏi lại)
Vòng 2 là vòng cuối. **Trượt**: 2/7 khi tính luật câu khuyên; 5/7 (71%) nếu chỉ tính điểm nghĩa. → Chuyển **(b) ngoại lệ có lý do**: render, đi tiếp C5. Đã ghi `ledger.md` và `taste-ledger.md` cả điểm che chữ lẫn điểm cổng gốc.
Lý do ngoại lệ: nghĩa do lời mang; bản đọc thử C2 đã qua kiểm mù nghe, trừ đoạn phương pháp nay đã thành thẻ. Nhãn nghĩa nâng điểm nghĩa từ 3/7 lên 5/7. Phần còn lại là người xem tự suy ra lời khuyên ("fixed is safer/protection"; 5/21 câu), đưa vào gói C6 và lessons như rủi ro claim-risk của hình.
