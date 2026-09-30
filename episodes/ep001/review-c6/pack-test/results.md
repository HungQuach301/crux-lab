# So cặp mù gói phát hành v2 — kết quả (THAM KHẢO; chủ dự án chọn)

48 agent mới, mỗi agent một ảnh (thư mục tên ngẫu nhiên), câu hỏi cố định trong `prompt.txt`, không thấy tên ảnh hay `key.json`. Mỗi cặp chạy cả hai thứ tự. Giải mã bằng `key.json` sau khi đủ 48 câu trả lời. Câu trả lời nguyên văn: `<id>/answer.md`.

Vai: "an American currently paying a mortgage you signed between 2022 and 2024 … scrolling YouTube search results for 'refinance'".

## 1. Gói (tiêu đề + thumbnail), 42 ảnh = 21 cặp × 2 thứ tự

| Gói | Tiêu đề | Thumbnail | Thắng |
|---|---|---|---|
| c2 | Borrowed Over 7% in 2023? The Rate Cut a Refinance Needs | W | **12/12** |
| c1 | Got a 2023 Mortgage? The 1-Point Rule May Not Fit Your Loan | W | 10/12 |
| đối chứng | How Big a Rate Cut Makes a Refinance Worth It? (T1) | thumb-3 | 8/12 |
| b2 | Refinance Break-Even: The $1,133 That Simple Division Misses | L | 6/12 |
| a1 | Why a Smaller Loan Needs a Bigger Rate Cut to Be Worth It | H | 3/12 |
| b1 | The Refinance Cost That Isn't in the Fees | L | 2/12 |
| a2 | Same Rate Cut, Opposite Results for a Small and Big Mortgage | H | 1/12 |

- Lệch vị trí: chọn ô 1 = 19, ô 2 = 23 (không đáng kể).
- 19/21 cặp thắng ở cả hai thứ tự; 2 cặp đổi theo vị trí: a1–b1, a2–b1.
- **Nhiễu gộp:** mỗi hướng dùng một thumbnail (a→H, b→L, c→W), nên thứ hạng gói không tách được phần của tiêu đề và phần của thumbnail. Lý do nguyên văn của c1/c2 nhắc cả tiêu đề ("Got a 2023 Mortgage?", "over 7% in 2023") lẫn thumbnail W ("Missed it?", "5.98%"). Chỉ cặp c1–c2 (cùng W) so tiêu đề thuần: c2 thắng 2/2.
- Đối chứng T1 + thumb-3 thắng mọi gói hướng (a) và (b) ở cả hai thứ tự; thua c1, c2 ở cả hai thứ tự.

## 2. Thumbnail riêng (cùng tiêu đề T1), 6 ảnh = 3 cặp × 2 thứ tự

| Thumbnail | Thắng |
|---|---|
| W (cửa sổ, "5.98%", "Missed it?") | **4/4** |
| L ("$5,124" / "+$1,133") | 1/4 |
| H ("−1.12 pts" / "−0.32 pts") | 1/4 |

- W thắng L và H ở cả hai thứ tự. H–L: mỗi bên thắng một lần (ô 2 cả hai lần) → hoà.
- Lệch vị trí: ô 1 = 2, ô 2 = 4.

## 3. Lý do nguyên văn (mỗi dòng: gói ô 1 vs gói ô 2 → chọn)

```
pack a1 vs a2 pick 1 = a1 | 1 — Its title directly answers the practical question I'd have as a recent borrower, which is how big a rate drop I'd need before refinancing is worth it, while title 2 only hints at a comparison.
pack a1 vs b1 pick 2 = b1 | 2 — With a relatively high 2022–2024 rate I'm weighing a refinance, and a video promising a hidden cost beyond the closing fees speaks directly to my worry about whether it really saves me money.
pack a1 vs b2 pick 2 = b2 | 2 — With a high-rate 2022–2024 mortgage, my real question is whether refinancing pays off and when, and a video titled "Refinance Break-Even" that promises the hidden cost simple division misses speaks directly to that d
pack a1 vs c1 pick 2 = c1 | 2 — The title speaks straight to someone who took out a mortgage in 2023, and the "Missed it?" rate chart hits my worry about whether I've already missed my chance to refinance.
pack a1 vs c2 pick 2 = c2 | 2 — It speaks directly to my situation as someone who locked in a high rate in 2022-2024 and tells me what rate cut I'd need to make refinancing worth it.
pack a1 vs control pick 2 = control | 2 — As someone who locked in around 7% during 2022–2024, the "5.98% → 7.03%" thumbnail and title asking how big a rate cut makes a refinance worth it speak directly to my situation and question.
pack a2 vs a1 pick 2 = a1 | 2 — I signed at high 2022–2024 rates and want to know whether a rate cut is big enough to make refinancing worth it, and this title directly frames it as a "worth it" decision rule tied to loan size.
pack a2 vs b1 pick 2 = b1 | 2 — Having locked in a high 2022–2024 rate, I'm weighing a refinance and most want to know the hidden cost beyond closing fees before deciding whether it's actually worth it.
pack a2 vs b2 pick 2 = b2 | 2 — Since I'm searching "refinance" with a recent high-rate mortgage, a video on refinance break-even costs speaks directly to whether refinancing would actually pay off for me.
pack a2 vs c1 pick 2 = c1 | 2 — It speaks directly to someone who took out a mortgage around 2023 and questions the refinance rule of thumb, so it feels tailored to my situation.
pack a2 vs c2 pick 2 = c2 | 2 — It speaks directly to my situation (a high-rate loan taken out in 2022–2024) and says what rate cut I need before a refinance is worth it.
pack a2 vs control pick 2 = control | 2 — It speaks directly to my situation, since I locked in at roughly 6–7% in 2022–2024, and it asks the exact question I'm searching for: how big a rate cut I'd need for a refinance to be worth it.
pack b1 vs a1 pick 2 = a1 | 2 — Having locked in a high 2022–2024 rate, my main question is how much rates need to fall before refinancing pays off, and this video's rate-cut threshold framing answers that directly.
pack b1 vs a2 pick 2 = a2 | 2 — Having locked in a high 2022-2024 rate, I most want to know how much a rate cut actually saves on a loan like mine, and the small-vs-big mortgage comparison speaks directly to that.
pack b1 vs b2 pick 2 = b2 | 2 — As someone with a 2022-2024 mortgage weighing whether a refinance pays off, the explicit "break-even" framing speaks directly to my decision, while title 1 is vaguer.
pack b1 vs c1 pick 2 = c1 | 2 — It speaks directly to someone who took out a mortgage in 2023, so it feels written for my exact loan and makes me want to check whether I missed a chance to refinance.
pack b1 vs c2 pick 2 = c2 | 2 — It speaks directly to my situation of having locked in a 7%+ rate in 2022–2024 and tells me what rate drop I'd need for a refinance to pay off.
pack b1 vs control pick 2 = control | 2 — With a 2022-2024 mortgage likely at a 6-7%+ rate, the question I actually need answered is how big a rate drop makes refinancing worth it, which video 2 addresses directly.
pack b2 vs a1 pick 1 = b2 | 1 — Since I locked in a high rate in 2022–2024 and am weighing a refinance, a video that says the usual break-even math misses $1,133 of cost speaks directly to whether refinancing would actually pay off for me.
pack b2 vs a2 pick 1 = b2 | 1 — As someone with a recent high-rate mortgage weighing whether a refinance pays off, a video promising the hidden cost that the simple break-even calculation misses speaks directly to my decision.
pack b2 vs b1 pick 1 = b2 | 1 — With a 2022-2024 mortgage at a high rate, my real question is whether refinancing pays off and how fast, and a title promising the break-even math that simple division gets wrong speaks directly to that.
pack b2 vs c1 pick 2 = c1 | 2 — It speaks directly to someone who took out a mortgage around 2023, and the "Missed it?" line about rates dipping near 5.98% makes me want to know if I should refinance now.
pack b2 vs c2 pick 2 = c2 | 2 — As someone who took out a mortgage in the 2022–2024 high-rate period, a title aimed directly at people who borrowed at over 7% in 2023, asking what rate cut makes a refinance worth it, speaks to my situation more tha
pack b2 vs control pick 2 = control | 2 — My 2022–2024 rate is probably around 7% like the one in the thumbnail, and the title asks what I actually want to know: how big a rate drop I'd need before refinancing pays off.
pack c1 vs a1 pick 1 = c1 | 1 — It speaks directly to me with "Got a 2023 Mortgage?" and a "Missed it?" hook on current rates, so it feels like it's about my loan and whether I should refinance now.
pack c1 vs a2 pick 1 = c1 | 1 — Its title speaks directly to someone with a 2023-era mortgage and asks whether the refinance rule of thumb fits their own loan, which is exactly my situation.
pack c1 vs b1 pick 1 = c1 | 1 — It speaks straight to my situation as someone who took out a mortgage around 2023, and it hints that the usual "rates must drop a full point" rule might not apply to my loan, so it seems more relevant than a general 
pack c1 vs b2 pick 1 = c1 | 1 — It speaks directly to me as someone with a 2022–2024 mortgage ("Got a 2023 Mortgage?") and hints I might have missed a refinance window, which feels more personally relevant than a generic break-even math video.
pack c1 vs c2 pick 2 = c2 | 2 — It speaks directly to my situation (a 7%+ rate locked in 2023) and promises the concrete number I care about: how far rates must drop before refinancing pays off.
pack c1 vs control pick 1 = c1 | 1 — Its title speaks straight to me as someone with a 2022–2024 mortgage ("Got a 2023 Mortgage?") and says the usual refinance rule of thumb may not fit my loan, so it feels more relevant than the general rate-cut questi
pack c2 vs a1 pick 1 = c2 | 1 — It speaks directly to my situation, since I likely locked in a rate over 7% around 2023, and it promises to tell me what rate I'd need to make refinancing worth it.
pack c2 vs a2 pick 1 = c2 | 1 — It speaks directly to my situation (a mortgage taken at a high rate in 2022–2024) and promises to tell me what rate cut I'd need for a refinance to pay off.
pack c2 vs b1 pick 1 = c2 | 1 — As someone who likely locked in a 7%-ish rate in 2022-2024, a title speaking directly to my situation and the rate drop I need to refinance is the most relevant click.
pack c2 vs b2 pick 1 = c2 | 1 — The title speaks directly to my situation (borrowed at over 7% in 2023) and the "Missed it?" hook about rates dipping near 5.98% makes me worry I'm missing a chance to save, so it feels more urgent and relevant than 
pack c2 vs c1 pick 1 = c2 | 1 — It speaks directly to my situation (I likely borrowed above 7% in 2023) and promises a concrete payoff: the rate drop I'd need for a refinance to make sense, which is exactly what I'm searching for.
pack c2 vs control pick 1 = c2 | 1 — Its title speaks directly to someone who borrowed at over 7% in 2023, which matches my situation, and it promises to tell me how big a rate cut I need before refinancing.
pack control vs a1 pick 1 = control | 1 — The 5.98% → 7.03% jump matches the rates I locked in on a 2022–2024 mortgage, and the title answers exactly my question: how big a rate cut would have to happen before refinancing pays off.
pack control vs a2 pick 1 = control | 1 — Having locked in a rate near 7% during 2022–2024, I'd click the video whose thumbnail shows that 7.03% figure and asks straight out how big a rate cut it takes for refinancing to be worth it.
pack control vs b1 pick 1 = control | 1 — With a 2022–2024 mortgage likely around 6–7%, my real question is how big a rate cut I need before refinancing pays off, and that's exactly what this video promises to answer.
pack control vs b2 pick 1 = control | 1 — The 5.98% → 7.03% rates match the high rate I likely locked in during 2022–2024, and "how big a rate cut makes a refinance worth it" is exactly the question I'm asking right now.
pack control vs c1 pick 2 = c1 | 2 — Its title speaks directly to my situation as someone with a 2023-era mortgage and says the usual "1-point rule" may not apply to my loan, so it feels more relevant than the generic rate-cut question in video 1.
pack control vs c2 pick 2 = c2 | 2 — Its title speaks directly to my situation (borrowed at over 7% in 2023) and promises to tell me exactly how big a rate cut I'd need for a refinance to pay off.
thum H vs L pick 2 = L | 2 — As someone who locked in a high 2022–2024 rate, the concrete dollar figures ($5,124 closing costs vs. +$1,133 savings) speak directly to whether refinancing pays off for me, which is more gripping than abstract rate-
thum H vs W pick 2 = W | 2 — Having locked in a 6–7% rate in 2022–2024, the "5.98% — Missed it?" thumbnail speaks directly to my worry about whether I already missed my chance to refinance, which feels more personal and urgent than the abstract 
thum L vs H pick 2 = H | 2 — Having locked in a high 2022–2024 rate, I'm mainly wondering how far rates have to drop for me to refinance, and the "−1.12 pts vs −0.32 pts" thumbnail speaks to that directly.
thum L vs W pick 2 = W | 2 — My 2022–2024 mortgage rate is probably in the 6.5–7.5% range, so a thumbnail showing rates dipping to 5.98% and asking "Missed it?" hits my exact fear that I let my refinance window slip by.
thum W vs H pick 1 = W | 1 — With a 2022–2024 mortgage likely around 6.5–7.5%, the big "5.98%" rate and "Missed it?" hook make me immediately compare it to my own rate and worry I let a refinance window slip by.
thum W vs L pick 1 = W | 1 — With a 2022–2024 mortgage likely around 6.5–7.5%, the 5.98% rate dip and "Missed it?" hook speak directly to my worry about whether I've already missed my chance to refinance.
```

## 4. Giới hạn

- Agent đóng vai, không phải người xem thật; kết quả là THAM KHẢO như C1. Test & Compare của YouTube là phép đo thật.
- Vai được mô tả là đã vay 2022–2024, nên các tiêu đề gọi thẳng nhóm đó (c1, c2) được lợi từ chính câu hỏi. Người xem tìm "refinance" ngoài nhóm này có thể phản ứng khác.
- Mỗi cặp chỉ 2 lượt; chênh 1 lượt không có ý nghĩa.
