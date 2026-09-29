# C4 — Kiểm mù tắt tiếng animatic (kết quả)

29/09/2026, P2. Ý đồ và tiêu chí được ghi trước, ở `animatic/intent.md` (commit `fb61ff9`, trước khi render). Vật liệu: `animatic/strips/S01–S20.png`. Mỗi dải có 6 khung theo thời gian và đã ẩn câu chú thích, không có lời đọc. Mỗi dải được 3 agent mới đọc; mỗi agent đọc một file tên ngẫu nhiên. Đối chứng yếu gồm 3 agent đọc `review-m1b/sb-03.png`. Tổng cộng 63 agent.

## Độ lệch quy trình (ghi thật)
- Câu hỏi thực tế chạy có thêm cụm "arranged in a 3×2 grid and numbered 1–6 in time order", thay cho "in order left to right" ghi trong ý đồ, vì dải được dựng theo lưới 3×2. Ba câu hỏi còn lại giữ nguyên văn. Cả 3 người đọc đối chứng đều ghi rằng ảnh không phải lưới 3×2, vì sb-03 là trang dọc có 3 khung.
- Đối chứng sb-03 có nội dung khác (Hồi 2–3 bản cũ) và vẫn còn chữ chú thích, lại lộ nhãn nội bộ ("a2-cliff", "DX-H6"). Vì vậy không chấm đối chứng theo bảng ý đồ; chỉ so định tính ở cuối.

## Chấm (tiêu chí ghi trước)
Một câu trả lời được tính là **đọc đúng** khi nói được ý câu (1) và ít nhất 2 ý bắt buộc (nhịp chỉ có 2 ý thì phải đủ cả 2). Một nhịp **đọc đúng** khi ≥ 2/3 người đọc đọc đúng. Cổng qua khi ≥ 16/20 nhịp đọc đúng.

| Nhịp | Đọc đúng | Ghi chú của P2 |
|---|---|---|
| S01 | 3/3 | "window" chỉ rõ nghĩa ở khung cuối |
| S02 | 3/3 | |
| S03 | 3/3 | |
| S04 | 3/3 | |
| S05 | 3/3 | không có số trên trục tung; "(our test value)" nhỏ |
| S06 | 3/3 | |
| S07 | 3/3 | |
| S08 | 3/3 | |
| S09 | 3/3 | "?" trên khối dư nợ được đọc là gợi ý (đúng ý) |
| S10 | 3/3 | thanh "magnified" khó thấy khác biệt |
| **S11** | **0/3 — TRƯỢT** | Cả 3 không hiểu nhãn "division: month 38". Hai người gán tháng 38 cho vạch giảm 1 điểm (sai); người thứ ba chỉ đoán. Đường trắng không có nhãn, và đường xanh đổi hình dạng mà không có giải thích. Cả 3 hiểu "Never". |
| S12 | 3/3 | đường xanh không có nhãn |
| S13 | 3/3 | ô đỏ và tam giác cam "?" chưa có nhãn (cố ý báo trước, người đọc thấy khó hiểu) |
| S14 | 3/3 | "bill" không được định nghĩa là phí vay lại |
| S15 | 3/3 | "loan costs + still owed" khó hiểu |
| S16 | 3/3 | khung 6 không có chú giải Walt/Nora; "still owed" khó hiểu |
| S17 | 3/3 | tam giác 1.12 và chấm 0.5 không có nhãn |
| S18 | 3/3 | |
| S19 | 3/3 | 3 thanh màu ở khung 1 không có nhãn; chấm che chữ "Nora's $5,124" |
| S20 | 3/3 | từ "refinance" không xuất hiện trên hình |

**Kết quả: 19/20 nhịp đọc đúng (95%) → QUA ngưỡng C4. 57/60 câu trả lời đọc đúng.** Nhịp trượt S11 đã được thiết kế lại (`e8f6fce`): nhãn nằm ngay trên đường trắng "same 0.25 cut, savings alone", và "division" đổi thành "simple division". Kiểm lại với 3 agent mới cho kết quả **3/3 đọc đúng** (mục cuối). Sau sửa: **20/20 nhịp**.

**Hiểu nhờ hình hay chữ:** hầu hết câu trả lời nói "Both, but mostly the words and numbers". Hình mang được cấu trúc (lên/xuống, chồng tiền đuổi khối phí, cỡ nhà), còn số và nhãn mang ý. Đây là dải ảnh tĩnh, nên chưa đo được chuyển động (G-011).

**Lỗi lặp lại (đầu vào cho C5, mức Chính/Tham khảo):**
- Thuật ngữ trên màn hình không được giải thích khi tắt tiếng: HMDA, FRED, "Dollars of the day". Lời đọc có thể giải thích.
- Những dòng xám giả chữ trên tờ đề nghị (S02, S06, S07, S09, S18).
- Ký hiệu không có nhãn: S11, S13, S16, S17, S19.
- Chữ nhỏ hoặc mờ ở chân trang, tick trục, chữ bị chấm che (S19). Tất cả vẫn đọc được, không ai báo là không đọc nổi.

**Đối chứng yếu (sb-03, định tính):** cả 3 người đọc vẫn nắm được đại ý, nhưng dựa gần như hoàn toàn vào chữ chú thích. Mỗi người liệt kê 5–6 chỗ không hiểu: trục không có số, nhãn nội bộ, tên nhân vật không được giới thiệu, chữ quá nhỏ. Ứng viên thì có chữ chú thích bị ẩn và mỗi dải có ít chỗ khó hơn. Vì nội dung khác nhau, đây **không** phải phép so sánh công bằng; chỉ ghi để tham khảo.

---
## Nguyên văn 63 câu trả lời (xếp theo nhịp; CTRL = đối chứng sb-03)

===== CTRL 5a8500e5
File: 5a8500e5

Note: the image did not match the description I was given. It is not a 3x2 grid of six numbered frames. It is one tall page with three labeled chart panels stacked top to bottom ("07 a2-cliff", "08 a3-range", "09 a3-answer2"), and each has a caption. I answered based on what the image actually shows.

1. What is this scene telling you?
I think it's saying that when my mortgage rate drops, refinancing takes longer to pay for itself than the usual calculators say, because they just divide the closing cost by the monthly saving. If you count what I still owe, a small cut like 0.25 points or less "never" breaks even, and today's cut of about 0.59 points pays back within 36 months only if you count it that way. The last panel shows three example borrowers (Priya 0.2, Maya 0.5, Dan 1.12) on a scale of how big a cut each would need, and today's 0.59 is marked. Since I locked in during 2022–2024, the message seems to be to check my own break-even carefully before I refinance on a small cut.

2. Pictures, words/numbers, or both?
Both, but mostly the words and numbers. The shapes alone were suggestive: the solid line shoots up at small cuts and the green "today" line is marked. Still, I only understood the point from the axis labels ("months to break even", "rate cut (points)"), the legend ("most calculators (cost / monthly saving)" vs "counting what is still owed"), and the captions under each panel.

3. What I didn't understand / couldn't read:
- The middle bar chart (1974–2023) doesn't show numbers on the bars, so I can't tell how many months each bar stands for. I also don't know why 2018 and 2023 are blue while the others are grey.
- The subtitle "grey = fixed pre-2018 cost share (ILLUSTRATIVE); red mark: the next full point came first" is very small and I don't really get it. I can't tell what "cost share" means or what the red triangles on 1980, 1981 and 1984 mean for me.
- "Act 3: every drop since 1971 (DX-H6)": I don't know what "DX-H6" is.
- In the bottom panel, who are Priya, Maya and Dan, and what makes their numbers different? There's also a second, unlabeled "Maya" floating at the top left.
- I'm not sure what the row of 13 dots ("13 drops since 1971") at the bottom is supposed to show.
- The small grey text (the chart subtitle, the axis tick labels, the year labels under the bars and "13 drops since 1971") is hard to read at this size. The panel headings like "a2-cliff" and "a3-answer2" look like internal labels and mean nothing to me.
===== CTRL b7dc73a5
File: b7dc73a5

Note: The image is not a 3×2 grid of six numbered moments. It is a single vertical page with three labeled chart panels: "07 a2-cliff", "08 a3-range" and "09 a3-answer2". My answer is based on those three panels.

1. What is this scene telling you?
If I refinance, the usual calculator shortcut (closing cost divided by monthly saving) makes break-even look sooner than it really is when the rate cut is small. Once you count what is still owed on the loan, a cut under about 0.25 points never pays back, and today's cut of about 0.59 points takes roughly 30 months instead of about 24. For someone like me with a 2022–2024 mortgage, the last panel suggests that the cut needed to pay back within 36 months depends on the borrower (illustrative people: Priya 0.2, Maya 0.5, Dan 1.12), and today's 0.59 is enough for some of them but not all.

2. Pictures, words/numbers, or both?
Both. The curves and the number line show the shape of the idea, but I only understood it from the legend ("most calculators (cost / monthly saving)" vs "counting what is still owed"), the captions, the axis labels ("months to break even", "rate cut (points)") and the "today 0.59" marker.

3. What I did not understand / could not read
- The middle bar chart (1974–2023) has no y-axis numbers, so I can't tell how many months each bar stands for. I also don't know why 2018 and 2023 are blue, what "fixed pre-2018 cost share" means, or exactly what the red triangles ("the next full point came first") are telling me.
- "DX-H6" in "every drop since 1971 (DX-H6)" means nothing to me.
- In the last panel, "Maya" shows up twice (once alone at the top left and once as "Maya 0.5"), and I don't know who Priya, Maya and Dan are supposed to be or which one is like me. The row of 13 dots ("13 drops since 1971") isn't explained.
- Panel labels like "a2-cliff", "a3-range" and "a3-answer2" look like internal production names.
- The small text is readable but tiny: the chart subtitles, the legend and the year labels under the bars.
===== CTRL e0f84e1b
File: e0f84e1b

Note: the image I opened isn't a 3x2 grid of six numbered moments. It's three charts stacked vertically, labeled "07 a2-cliff", "08 a3-range" and "09 a3-answer2". I answered from what is actually shown.

1. What is this scene telling you?
If I'm thinking about refinancing the mortgage I took out in 2022-2024, the usual calculator (closing costs divided by monthly savings) makes the break-even look faster than it really is once you count what is still owed. Rates are down about 0.59 points "today". For a small cut the real payback takes much longer, and below about a 0.25-point cut it never pays back. Whether 0.59 is enough depends on the person: it works for "Priya" (needs 0.2) and "Maya" (needs 0.5), but not for "Dan" (needs 1.12).

2. Pictures, words/numbers, or both?
Both. The shapes carry the main idea: the solid line shoots up at small cuts and joins the dashed line at bigger cuts, and the green "today" marker sits between the people's markers. But I needed the words and numbers to know what it's about: "months to break even", "rate cut (points)", "most calculators (cost / monthly saving)", "counting what is still owed", "today 0.59", "Priya 0.2 / Maya 0.5 / Dan 1.12", and "pays back within 36 months".

3. What I didn't understand / couldn't read
- The middle bar chart (1974-2023 drops) has no y-axis numbers, so I can't tell how many months each bar means. It's also unclear what the blue 2018/2023 bars and the red triangles ("the next full point came first") mean for me.
- The tiny subtitle "grey = fixed pre-2018 cost share (ILLUSTRATIVE)" and the year labels under the bars are very small and hard to read. The axis numbers on the top chart are small too.
- Jargon or internal labels mean nothing to me: "a2-cliff", "a3-range", "a3-answer2", "DX-H6", "Act 3".
- In the bottom chart there's an extra "Maya" label in the top left, apart from "Maya 0.5". There's also a row of 13 dots ("13 drops since 1971") that isn't explained. And I'm not sure who Priya, Maya and Dan are or why their numbers differ (different loan balances? costs?). The "ILLUSTRATIVE" tag suggests they're made-up examples.
- The charts don't tell me which person I am, so I still don't know if the 0.59 cut is enough for my own loan.
===== S01 6c39a600
File: 6c39a600

1. What is this scene telling you?
Mortgage rates fell to about a full percentage point below what someone like me locked in during 2023 (5.98% in late February 2026 vs. Nora's 7.62%). Refinancing then would have cut her payment by about $459 a month. That "window" closed after late July 2026, when rates climbed back above 7% (7.03%), so the savings are gone. For me, the message is that there was a short chance to refinance and it's over for now. Next time rates drop that far, I should act quickly.

2. Did you understand it from the pictures, from the words and numbers on screen, or both?
Both. The charts and the shrinking or crossed-out stack of cash show the idea: rates went down, a savings opportunity opened, then it closed. But I needed the numbers and labels to get the details: 7.62%, 5.98%, $459 a month less, "the window," "window closed," and "Back above 7%."

3. Which part, if any, did you not understand, and which words or numbers could you not read?
I got the main story. A few things were unclear:
- The small text on the tilted loan cards under "NORA'S LOAN" (it seems to say "October 2023") is tiny and blurry. I only knew what it meant because of the caption "7.62% since October 2023."
- The first chart ends around February 2026 while its axis runs to August, so at first I wasn't sure if the chart was incomplete or still showing data as it came in.
- The stacks of money show a monthly payment, but no dollar amount is given for Nora's actual payment or loan size. I can't tell how $459 compares to my own payment, and closing costs aren't mentioned.
- "Dollars of the day" is unclear. I guess it means amounts aren't adjusted for inflation.
- In the last chart, it isn't clear whether "window closed" means the rate rose back to exactly 1 point below Nora's rate (about 6.62%) or went above 7%.
===== S01 aeaa2845
File: aeaa2845

1. What is this scene telling you?
For a while, mortgage rates dropped far enough below a 2023-era rate like "Nora's" 7.62% (down to 5.98% in late February 2026) that refinancing would have saved about $459 a month. That "window" has closed: rates climbed back above 7% (7.03% as of the week ending September 24, 2026), so the savings are gone. For me, with a 2022–2024 mortgage, the message is that the refinance chance I may have been waiting for came and went, and if my rate is like Nora's, it would no longer pay off right now.

2. Did you understand it from the pictures, the words and numbers, or both?
Both, but mostly the words and numbers. The charts, the shaded "the window" area and the stacks of cash (a smaller stack, then the $459 crossed out) gave me the idea of "it got cheaper, then it went away". The actual story came from the text: Nora's 7.62% since October 2023, 5.98% at its lowest, "$459 a month less", "window closed", "Back above 7%", 7.03%.

3. What did you not understand, and what couldn't you read?
- It isn't clear what the "window" exactly means. It seems to be the stretch when rates were at least 1 percentage point below Nora's rate, which is a common refinance rule of thumb, but the scene never says the word "refinance" or explains why 1 point matters.
- The $459 figure depends on a loan size, balance and closing costs that are never shown, so I can't tell how much I would save on my own loan. "Dollars of the day" is also unclear to me.
- It isn't obvious how panel 3 (Nora's monthly payment as a single stack) is supposed to compare with panel 4 until the green "$459 a month less" appears.
- Small text I couldn't read clearly: the small print on the "Nora's loan" card under 7.62% (it looks like "October 2023", but it's tilted and faint), and the small y-axis labels on the charts beyond "7%". Everything else was readable.
===== S01 d6b9906c
File: d6b9906c

1. What is this scene telling you?
For a while, mortgage rates were low enough for someone like me to refinance. In late February 2026 they fell to 5.98%, a full point below the 7.62% loan of "Nora", an example borrower. That would have saved her about $459 a month. The window closed after the week ending July 23, 2026, and by September 24, 2026 rates were back above 7% (7.03%). So if you locked in at a high rate in 2022–2024 and didn't refinance during that stretch, the chance is gone for now.

2. Pictures, words/numbers, or both?
Both. The pictures (the line dropping into a shaded "window" and then climbing back out, and the stack of cash getting smaller and then the $459 being crossed out) gave me the general story. But I needed the words and numbers (7.62%, 5.98%, $459 a month less, "window closed", "Back above 7%", 7.03%) to know what the window was and how much money was involved.

3. What didn't you understand / couldn't read?
- It wasn't clear to me what "the window" means until frame 6. I guessed it's the stretch when rates sat at least one point below Nora's rate, which is the usual rule of thumb for refinancing. The chart never says "refinance" in so many words.
- Frame 5 crosses out "$459 a month less" before the chart explains why. I only understood it once I saw "window closed" in frame 6.
- The small date printed under "7.62%" on the loan card was hard to read. I assume it says "October 2023", which matches the label below it.
- The $459 figure is for Nora. The scene doesn't give her loan amount, so I can't tell how much I would save on my own mortgage. "Dollars of the day" was also a bit unclear to me.
- Everything else was readable: the axis labels (Aug 2025 to Aug), the 7% line, and the source (Freddie Mac weekly survey, via FRED).
===== S02 13021706
File: 13021706

1. What is this scene telling you?
A refinance offer would drop the rate from 7.62% to 7.03%, but the new loan comes with about $5,124 in fees (the median 2025 refinance bill). It then compares loan sizes (a smaller loan, "Nora" in the middle, a larger loan, and an empty outline marked "your loan?") to suggest that whether refinancing pays off depends on how big your loan is. As someone who signed a mortgage between 2022 and 2024, I read it as: that rate cut may apply to me, but I have to weigh the fees against my own loan size.

2. Did you understand it from the pictures, the words and numbers, or both?
Both, but mostly the words and numbers. The rates, the "$5,124" loan costs, and the labels (smaller loan, Nora, larger loan, your loan?) carry the message. The houses of different sizes and the empty wireframe house help show that loan sizes differ and that I should put my own loan in, but they would not mean much without the labels.

3. What did you not understand, and what could you not read?
The scene does not say what the answer is. It never shows how long it takes to earn back the $5,124 for each loan size, or at what loan size refinancing is worth it; it seems to stop just before that. In frame 6 the smallest house's windows light up and "smaller loan" turns yellow, but I am not sure what that highlight means (maybe that refinancing is a worse deal for small loans?). "HMDA" is not explained. The fine print on the offer sheet (the grey lines under "A new loan at a lower rate pays off your current loan.") is only placeholder lines, and the small tilted copy of the sheet in frames 4–6 is too small to read apart from the familiar numbers. Otherwise I could read all the main words and numbers.
===== S02 32bc8004
File: 32bc8004

1. What is this scene telling you?
A refinance offer would drop someone's rate from 7.62% to 7.03%, but the new loan comes with $5,124 in fees (the median 2025 refinance bill). Then it compares loan sizes (a smaller loan, "Nora" in the middle, a larger loan, and an empty outline labeled "your loan?") to suggest that whether that fee is worth it depends on how big your loan is. As someone who locked in around 7% sometime in 2022–2024, this feels aimed right at me: don't jump at a lower rate without checking whether the savings cover the fees.

2. Did you understand it from the pictures, the words and numbers, or both?
Both, but mostly the words and numbers. The offer sheet with its highlighted lines and the callouts ("a new loan at a lower rate 7.62% → 7.03%", "Loan costs: $5,124 the fees for the new loan") carry the main point. The row of houses, going from smaller to larger with an empty wireframe house at the end, gets across "compare this to your own loan" without much text, though the labels help.

3. What didn't I understand, and what couldn't I read?
- The scene never says how much Nora's loan is, what her monthly savings are, or how long it takes to break even. I get that loan size matters, but I don't know what the answer is for her, or where the cutoff would be for me.
- In the last frame the smallest house's windows light up and the "smaller loan" label turns yellow. I think that means the smaller loan is the one where the fees don't pay off (or pay off slowly), but nothing says so outright.
- "HMDA" in the footnote isn't explained; I'm guessing it's some government mortgage data source. I also wasn't sure what "Nora is illustrative" means at first; I take it she's a made-up example.
- I couldn't read the small grey lines under the "A new loan at a lower rate pays off your current loan" text on the offer sheet (they look like placeholder lines), or the tiny text on the shrunken offer sheet in the bottom-left of frames 4–6. Beyond "7.62%", "7.03%" and "$5,124", which I could still make out, it's too small to read.
===== S02 54c8452d
File: 54c8452d

1. What is this scene telling you?
It's a refinance offer: you'd go from 7.62% to 7.03%, but the new loan costs $5,124 in fees (that's the median 2025 refinance bill). The houses then show that "Nora" is one example borrower somewhere between a smaller and a larger loan, and they ask where my own loan fits. I take it to mean that whether the lower rate is worth $5,124 depends on how big my loan is, which matters to me because I locked in at around 7% in 2023.

2. Pictures, words/numbers, or both?
Both, but mostly the words and numbers. The offer sheet with "Your rate now 7.62%", "New rate 7.03%", "Loan costs $5,124" and the captions ("a new loan at a lower rate", "the fees for the new loan") carry the point. The houses of different sizes and the empty outline labeled "your loan?" make it clear that the idea is to compare loan sizes and picture my own.

3. What I didn't understand / couldn't read:
- The scene never says what the answer is. It doesn't tell me whether Nora comes out ahead, how many months it takes to break even, or how much she saves per month. It just stops at "your loan?", so I don't know yet what the loan size changes.
- I'm not sure why the lights come on in the smaller house in the last frame. Maybe it's pointing out that the smaller loan is the one that matters, but I couldn't tell.
- "HMDA" in the footnote isn't explained. I'm guessing it's a government data source.
- The small grey lines on the offer sheet under "pays off your current loan" can't be read and look like placeholder text. The tiny copies of the offer sheet in frames 4–6 are too small to read, but they seem to repeat the same numbers.
===== S03 3636d9aa
File: 3636d9aa

1. What is this scene telling you?
Nora (a made-up borrower) locked in a 30-year mortgage at 7.62% in October 2023. That was just below the 7.79% peak, the highest rate since 2000, and rates dropped soon after. She wasn't unusual: about three in ten home-purchase loans made in 2023 had a rate of 7% or more. As someone paying a mortgage I signed in 2022–2024, I read it as "you probably borrowed near the top too, and a lot of people are in the same spot."

2. Did you understand it from the pictures, from the words and numbers, or both?
Both. The line chart shows rates climbing and then falling, and the row of houses with a few lit up shows "some of the buyers." But the actual message comes from the text and numbers: "Nora borrowed here 7.62% · October 2023," "peak 7.79% highest since 2000," and "Three in ten had a rate of 7% or more." Without those labels I wouldn't have known whose loan it was or how common it was.

3. What did you not understand, and which words or numbers could you not read?
- The chart only has one gridline label (7%), so I can't tell how low the rate got early in 2023 or how far it fell by December. The drop after the peak looks steep, but I can't put a number on it.
- The houses: three lit houses out of roughly ten or eleven fits "three in ten." But it isn't clear if the lit houses mean the 7%+ loans or something else, since the orange underlines show up in frame 5, before the "three in ten" caption appears.
- The small source lines ("Freddie Mac weekly survey, via FRED," "HMDA 2023") were readable, but I don't know what FRED or HMDA stand for.
- The "ILLUSTRATIVE" tag and "Nora is illustrative" tell me Nora isn't real. It's less clear whether the house picture is also only illustrative or whether it shows real proportions.
- The scene doesn't say what this means for me, for example whether refinancing makes sense now.
===== S03 6d0c48c7
File: 6d0c48c7

1. What is this scene telling you?
Mortgage rates rose through 2023, and a borrower named Nora locked in at 7.62% in October, just before rates peaked at 7.79% (the highest since 2000) and then fell. She wasn't unusual either: about three in ten 30-year home-purchase loans made in 2023 had a rate of 7% or more. As someone who signed a mortgage in that same window, I read it as "a lot of us got in near the top, so you're not alone, and refinancing may be worth a look now that rates have come down."

2. Did you understand it from the pictures, the words and numbers, or both?
Both. The rising and falling line and the row of houses with a few lit up gave me the overall idea: rates climbed, then dropped, and some buyers got stuck with high ones. But the words and numbers carried the actual point: "Nora borrowed here, 7.62% · October 2023", "peak 7.79%, highest since 2000", and "Three in ten had a rate of 7% or more." Without the text, I wouldn't have known what the lit houses meant or how high the rates were.

3. What did you not understand, and what could you not read?
- The houses don't match the "three in ten" claim very well. Only three houses are lit out of roughly 13 to 15 in the row, which looks closer to two in ten than three in ten, so I had to trust the caption over the picture.
- The line chart has only one labeled level (7%) and no other numbers on the axis, so I couldn't judge how low rates were early in the year or where they ended in December. The chart also stops at the end of 2023, so it doesn't tell me what rates are now or whether refinancing makes sense for me.
- The "ILLUSTRATIVE" tag and the "Nora is illustrative" footnote made me unsure at first whether the rate line was real data or only Nora was made up. The source line ("Freddie Mac weekly survey, via FRED") suggests the rates are real and only Nora is invented.
- "FRED" and "HMDA 2023" are acronyms I don't know; I can guess they're data sources, but they're not explained.
- Everything was readable, though the small gray source footnotes and the small green "7.62% · October 2023" text are faint and hard to read at this size.
===== S03 a07e609f
File: a07e609f

1. What is this scene telling you?
In 2023, US 30-year mortgage rates climbed above 7%. They peaked at 7.79% in late October, the highest since 2000, and then fell back. An example borrower, "Nora," locked in 7.62% that October, near the top. The scene also says she wasn't unusual: about three in ten 30-year home-purchase loans made in 2023 had a rate of 7% or more. For me, having signed my own mortgage in that window, the message is that plenty of people borrowed at rates like this, many of us near the peak, and rates came down afterward.

2. Pictures, words and numbers, or both?
Both. From the pictures alone I could see a line going up, peaking and dropping, and a row of houses with a few lit up. The numbers and labels told me what that meant: the 7% line, "7.62% · October 2023", "peak 7.79% highest since 2000", and "Three in ten had a rate of 7% or more."

3. What I didn't understand or couldn't read
- The houses: I don't know exactly what the lit houses with orange underlines stand for. There are 3 of them in a row of about 12, which I take to mean "three in ten," but the scene never says so directly.
- The source lines: "FRED" and "HMDA" are abbreviations I didn't know. The small print at the bottom was readable, though.
- The labels: the "ILLUSTRATIVE" tag and "Nora is illustrative" tell me Nora is made up, but not whether the chart line itself is exact or only approximate.
- The chart: the y-axis only has a 7% gridline, so I can't read the low point of the rate early in the year.
- The drop: the chart shows the rate falling after the peak, but the scene never says where it ended up, so I can't tell whether refinancing would make sense for me.
===== S04 43870ef4
File: 43870ef4

1. What is this scene telling you?
It introduces "Nora," a made-up example homebuyer built from typical figures, who moved into her first home with a $375,000 loan at a 7.62% rate signed in October 2023. The amounts are in dollars of the day, not adjusted for inflation. As someone who signed a mortgage in 2022–2024, I read her as a stand-in for people like me who locked in at the high-rate peak, and I expect the video to use her to show what that rate means.

2. Pictures, words and numbers, or both?
Both, but mostly the words and numbers. The pictures (a dark house whose lights come on, moving boxes by the door) tell me someone has just moved into a first home. The facts come only from the on-screen text: "Nora's first home," the loan card ($375,000, 7.62%, Signed October 2023), and the "Illustrative / built from typical figures" labels.

3. What I did not understand or could not read
I could read all the text: "Nora is illustrative: built from typical figures," "ILLUSTRATIVE," "Nora's first home," "NORA'S LOAN," "Loan $375,000," "Rate 7.62%," "Signed October 2023," and "Dollars of the day / not adjusted for inflation." The "not adjusted for inflation" line in panel 6 is small but I could still read it. What is missing: the scene does not say what kind of loan this is (a 30-year fixed?), what her monthly payment is, or what the video will go on to argue, such as refinancing or rates falling. The 7.62% also seems high to me; it matches the fall 2023 peak, but it is above the typical average rate I remember, so I am not sure whether it includes extra costs or is just a rounded "typical" figure.
===== S04 8c402509
File: 8c402509

1. The scene introduces "Nora," a made-up example buyer built from typical figures. She has moved into her first home (moving boxes, lights coming on) with a $375,000 mortgage at 7.62%, signed in October 2023. As someone who signed around then too, I read her as a stand-in for people like me who locked in a high rate.

2. Both. The pictures give me the story: a dark, empty house lights up and boxes show up at the door, so someone just moved in. The words and numbers give me the facts: that it's her first home, that Nora isn't a real person ("illustrative," "built from typical figures"), and the loan amount, rate, and signing date.

3. I could read all the text. One thing was unclear. The last note, "Dollars of the day, not adjusted for inflation," shows up at the end without saying which numbers it covers. I assume it means the $375,000, but I'm not sure. The scene also doesn't say whether 7.62% is a 30-year fixed rate, or what the monthly payment is, so I can't compare her loan directly with mine yet. The small "not adjusted for inflation" line in panel 6 is small and sits partly under the tilted box, but I could still read it.
===== S04 d6a1d9b2
File: d6a1d9b2

1. What is this scene telling you?
It introduces "Nora," a made-up but typical first-time homebuyer who has just moved into her first home. She took out a $375,000 mortgage at 7.62%, signed in October 2023, and the amounts are shown in the dollars of that time, not adjusted for inflation. As someone who also signed a mortgage between 2022 and 2024, I read her as a stand-in for people like me who locked in at a high rate. The video will probably use her to show what that loan costs or how it plays out.

2. Pictures, words/numbers, or both?
Both, but mostly the words and numbers. The pictures (a house lighting up at night with moving boxes by the door) tell me someone has just moved into a new home. The labels ("Nora's first home," "Nora is illustrative: built from typical figures") and the loan card (Loan $375,000, Rate 7.62%, Signed October 2023) carry the actual message. Without the text I would only know that someone moved into a house.

3. What I did not understand or could not read
I could read all of the text: "Nora is illustrative: built from typical figures," "ILLUSTRATIVE," "Nora's first home," "NORA'S LOAN," "Loan $375,000," "Rate 7.62%," "Signed October 2023," "Dollars of the day," and "not adjusted for inflation." Some things are left unclear. The scene doesn't say what kind of loan this is (for example, a 30-year fixed), how big the down payment was, or what the home cost. It also doesn't show a monthly payment. The "Dollars of the day / not adjusted for inflation" note is small and appears only at the very end, so a viewer could easily miss it. It also doesn't say whether I'm meant to compare her rate with my own or with today's rates.
===== S05 4e6e9cef
File: 4e6e9cef

1. What is this scene telling you?
If you're like "Nora," who locked in a 30-year mortgage at 7.62%, rates dropped at least 1 point below that for 29 weeks in 2026, as much as 1.64 points below at the low of 5.98% around February–March. That window has now closed, since rates climbed back above her line as of July 23, 2026. So a borrower like me, who signed in 2022–2024, may have missed a good chance to refinance, and nobody knows what comes next ("next?"). It's history, not a forecast.

2. Pictures, words and numbers, or both?
Both. The line chart and the shaded area under the dotted line showed me visually that rates dipped well below Nora's rate and then came back up. But I needed the labels ("1 point below Nora", "29 weeks in 2026 at least 1 point below", "1.64 points gap at the low (5.98%)", "window closed", "last week: July 23, 2026") to know the actual size of the drop, how long it lasted, and that it's over.

3. What I didn't understand / couldn't read
- I wasn't sure at first who "Nora" is. The footer says "Nora is illustrative" and panel 2 says "(our test value)", so she seems to be a made-up example borrower with a 7.62% rate, not a real person. My own rate may be different, so I'd have to compare it myself.
- The row of little blue tick marks under the x-axis is only explained by the text below it (29 weeks). I couldn't count the ticks individually.
- The chart doesn't show the exact rate for each week, only the low (5.98%) and Nora's 7.62%. The y-axis has no numbers.
- The small footer text ("Freddie Mac weekly survey, via FRED. Nora is illustrative.") and "(our test value)" were small but readable. I didn't find any words or numbers I couldn't read at all.
- It doesn't say anything about refinancing costs or whether a 1-point drop is worth refinancing, so the "so what" for me is implied, not stated.
===== S05 7aed83ad
File: 7aed83ad

1. What is this scene telling you?
Someone like me who locked in a mortgage at around 7.62% ("Nora") had a stretch of 29 weeks in 2026 when the 30-year rate was at least a full point lower, bottoming out at 5.98% (a 1.64-point gap), which I read as a good chance to refinance. But by the week of July 23, 2026 rates had climbed back and that "window closed", and nobody knows what comes next. It's history, not a forecast.

2. Did you understand it from the pictures, from the words and numbers on screen, or both?
Both, but mostly the words and numbers. The picture shows the line dipping below the dotted line and then climbing back up, and the shaded area and the tick marks show how long it stayed down. The chart has no rate numbers on its side, though, so without the labels ("Nora 7.62%", "1 point below Nora", "1.64 points", "5.98%", "29 weeks", "window closed", "last week: July 23, 2026") I wouldn't know how big the drop was or what it meant for me.

3. Which part, if any, did you not understand, and which words or numbers could you not read?
- At first I didn't know who "Nora" is. The small "(our test value)" note and the footer ("Nora is illustrative") suggest she's a made-up borrower standing in for people like me, but it's never explained. I also can't tell whether 7.62% is supposed to be a typical 2022–2024 rate or just an example.
- It never actually says "refinance". I'm guessing that "1 point below" is the refinancing rule of thumb and that "window" means a refinance window. Nothing on screen says so, and it says nothing about closing costs.
- "window closed" is a little confusing because the rate at the end is still near the line, not far above it.
- The chart doesn't show rate numbers on the side, so apart from 5.98% I can't read the actual rate on any given week.
- The small print is hard to read: "(our test value)", the source line ("Freddie Mac weekly survey, via FRED") and "next?" in the last panel. I'm not sure what "FRED" is.
- The tick marks under the chart are too small and packed together for me to count, so I had to go by the "29 weeks" label.
===== S05 df118bcb
File: df118bcb

1. What is this scene telling you?
Someone like me, "Nora," locked in a 7.62% 30-year mortgage. Rates then fell at least a full point below her rate for 29 weeks in 2026, bottoming at 5.98%, a 1.64-point gap, which was a real chance to refinance. By the last week shown (July 23, 2026) rates had climbed back and that "window closed", and nobody knows what comes next. It's history, not a forecast, and the numbers are illustrative.

2. Pictures, words/numbers, or both?
Both. The line dipping into the shaded band and then climbing back out showed me the "opened then closed" story. But I needed the words and numbers to know what it meant for me: "Nora 7.62%", "1 point below Nora", "29 weeks in 2026 at least 1 point below", "1.64 points gap at the low (5.98%)", "window closed", "last week: July 23, 2026" and "next?".

3. What I didn't understand / couldn't read
- It took me a moment to see that "Nora" is a made-up borrower. The "(our test value)" note in frame 2 and "Nora is illustrative" in the footer are tiny, so I had to squint.
- "1 point below" is a rule of thumb, but nothing explains why one point is the threshold for refinancing, and closing costs aren't mentioned.
- The source line ("Freddie Mac weekly survey, via FRED") and the "ILLUSTRATIVE" tag are small. I could read them, but it's unclear which parts are real data and which are made up. The chart line looks like real rates, while Nora's 7.62% is invented.
- The tick bars under the axis ended up being a count of the 29 weeks, but I only figured that out from the caption.
- The last date ("July 23, 2026") partly overlaps the line, and the chart has no y-axis rate labels, so apart from 7.62% and 5.98% I can't read actual rate levels off it.
- Everything else was legible.
===== S06 210e9867
File: 210e9867

1. What is this scene telling you?
A borrower like me ("Nora") who locked in around 7.62% could get a refinance offer at 7.03%, the national average for the week ending September 24, 2026. That drop is 0.59 of a point, just over half a point, and it would cut about $221 off the monthly payment. The loan costs to get it are $5,124.

2. Pictures, words/numbers, or both?
Both, but mostly the words and numbers. The rates, the $5,124 cost, the 0.59-point gap and the "$221 a month less" line carry the message. The pictures help: the bar showing the gap next to a full 1-point bar makes it clear the drop is only about half a point, and the stack of cash stands for the monthly savings. On their own, the pictures would not tell me the amounts.

3. What I didn't understand / couldn't read:
- The scene never says how long it takes to earn back the $5,124. At $221 a month that's roughly 23 months, but I had to work that out myself, and it's the part I care about most.
- It doesn't give the loan balance or term behind the $221, so I can't tell how close Nora's numbers are to mine. "Illustrative" and "Dollars of the day" suggest a made-up example in current dollars, but that wasn't fully clear.
- In frames 5 and 6 the small refinance paper on the table is too small to read. I can only guess it repeats 7.62%, 7.03% and $5,124. The small gray lines under "pays off your current loan" in frames 1 and 2 are placeholder lines, not readable text.
- "FRED" is not explained. I guess it's a data source.
- The scene doesn't say whether I should refinance.
===== S06 44b8f565
File: 44b8f565

1. What is this scene telling you?
Nora, a made-up borrower, has a mortgage at 7.62% and gets a refinance offer at 7.03%. That rate matches the Freddie Mac national average for the week ending September 24, 2026. The drop is only 0.59 of a percentage point, a little over half a point, but it would still cut her payment by $221 a month, and the new loan costs $5,124 up front. As someone who took out a mortgage between 2022 and 2024, I read this as: if my rate is near hers, refinancing now could save me real money each month, but I would have to pay those costs first.

2. Did you understand it from the pictures, from the words and numbers on screen, or both?
Both, but mostly from the words and numbers. The rates, the $5,124 in loan costs, "0.59 point" and "$221 a month less" carry the message. The pictures help. The bar chart shows how small the gap is next to a full percentage point, and the stack of cash shows the monthly saving. Without the numbers, though, the pictures would not tell me much.

3. Which part, if any, did you not understand, and which words or numbers could you not read?
- The scene never shows Nora's loan balance or how many years are left on it, so I can't tell whether $221 a month would apply to a mortgage like mine.
- It does not say how long it takes to earn back the $5,124. I had to work that out myself: about 23 months (5,124 ÷ 221). It also does not say whether the costs are paid in cash or added to the loan.
- I'm not sure what "Dollars of the day" means. I think it means the amounts are not adjusted for inflation.
- The label "ILLUSTRATIVE" and the note that the offer matches the national average leave me unsure whether a real lender would offer me this rate.
- On the small refinance sheet in frames 5 and 6, the fine print is too small and blurry to read. Only the rates and $5,124 are faintly readable. The two gray placeholder lines under the heading in frames 1 and 2 have no readable text either.
===== S06 b2d9f464
File: b2d9f464

1. What is this scene telling you?
Someone like me (the example borrower "Nora", whose mortgage is at 7.62%) gets a refinance offer at 7.03%, which the video assumes is the national average for the week ending September 24, 2026. That's 0.59 of a percentage point lower, just over half a point, and it would cut her payment by about $221 a month. But the refinance comes with $5,124 in loan costs, so I'd have to weigh those costs against the monthly savings.

2. Did you understand it from the pictures, from the words and numbers on screen, or both?
Both, but mostly from the words and numbers. The rates, the $5,124 loan costs, the "0.59 point" label and the "$221 a month less" line carry the message. The pictures help: the offer letter, the bar chart comparing the 0.59 gap with a full 1-point bar, and the stack of cash that stands for the savings.

3. Which part, if any, did you not understand, and which words or numbers could you not read?
- I'm not sure what the cash stack in frames 5–6 is meant to show, or how it relates to the $5,124 in costs. The scene doesn't say how long it takes for $221 a month to pay back $5,124 (roughly two years by my math), so I can't tell whether the refinance is worth it.
- The scene never says what loan amount or loan term the $221 figure is based on, so I can't tell how it applies to my own mortgage. "Dollars of the day" is also a little unclear to me.
- "Freddie Mac weekly survey, via FRED" is a source note; I don't know what FRED is.
- On the offer letter in frames 1–2, the grey placeholder lines under "pays off your current loan" have no readable text. In frames 5–6 the letter is small and at an angle, so its text is hard to read, although the numbers (7.62%, 7.03%, $5,124) seem to match the earlier frames.
===== S07 14561cf1
File: 14561cf1

1. What is this scene telling you?
A refinance offer that drops the rate from 7.62% to 7.03% saves about $221 a month, but the loan costs of $5,124 are paid in cash at closing. That $5,124 is exactly the median closing bill across nearly half a million 2025 refinances, on a median-size $375,000 loan. As someone who locked in at around 7% in 2022–2024, I take it as: check the "loan costs" line on your own refinance letter and see where it falls on that range before you jump at a lower rate.

2. Did I understand it from the pictures, the words and numbers, or both?
Both, but mostly from the words and numbers. The pictures (a small cash stack next to a tall block, a dot on a range bar) show the size comparison. I only got the meaning from the labels: the rates, "$221 a month," "loan costs $5,124," "paid in cash at closing," and "the median bill: half pay less, half pay more."

3. What I did not understand, and what I could not read
- The scene never says how many months it takes for $221 a month to pay back $5,124 (roughly 23 months by my own math), or whether refinancing is worth it. I had to work that out myself.
- "One scale for both" was unclear at first. I think it means the two stacks are drawn at the same scale, but that is my guess.
- "Dollars of the day" is jargon. I took it to mean the amounts are not adjusted for inflation, but I am not sure.
- The empty dotted box labeled "your letter?" in frame 6 is open-ended. I think it is asking me to place my own offer on the range, but nothing tells me how.
- The range bar in frames 4–6 has no dollar values for "the middle half of bills," so I could not tell what counts as a small or large bill.
- The small refinance letter lying on the table in frames 2 and 3 is too small to read, except for faint numbers that look like 7.62%, 7.03% and $5,124. The grey placeholder lines under "A new loan at a lower rate pays off your current loan" in frame 1 have no readable text.
===== S07 4ce65360
File: 4ce65360

1. What is this scene telling you?
A refinance offer that drops Nora's rate from 7.62% to 7.03% saves about $221 a month, but it comes with $5,124 in loan costs paid in cash at closing, which is a big upfront bill shown next to the small monthly savings. That $5,124 is exactly the typical (median) cost across nearly half a million 2025 refinances on a $375,000 loan, so as someone with a 2022–2024 mortgage at a similar rate, I should check the "loan costs" line on my own offer and see where it lands on that range.

2. Did you understand it from the pictures, from the words and numbers on screen, or both?
Both. The stacks of cash (a thin $221 stack next to a tall $5,124 block) and the dot on the range bar show the idea visually, but I needed the on-screen words and numbers (the rates, "loan costs $5,124", "paid in cash at closing", "the median bill", "$375,000") to know what the stacks and the bar actually meant.

3. What did you not understand, and what could you not read?
- The small copies of the refinance offer lying on the table in frames 2 and 3 are too small to read; I only assume they repeat frame 1.
- The two gray lines under "A new loan at a lower rate pays off your current loan" in frame 1 are blank placeholders, not readable text.
- The range bar in frames 4–6 has no dollar values at its edges, so I can't tell what "smaller bills," "larger bills," or "the middle half of bills" amount to in dollars.
- It isn't stated how long it takes for $221 a month to pay back $5,124 (I'd have to work out roughly 23 months myself), and "one scale for both" and "Dollars of the day" are a bit unclear.
- The empty dashed box labeled "your letter?" in frame 6 seems to invite me to compare my own offer, but it isn't explained.
===== S07 eedc6691
File: eedc6691

1. What is this scene telling you?
A refinance offer that drops a made-up borrower, "Nora," from 7.62% to 7.03% saves her about $221 a month, but it comes with $5,124 in loan costs paid in cash at closing, and that bill is shown to be typical: it is the 2025 median for refinances, on a median-size $375,000 loan. For me, with a 2022–2024 mortgage at a similar rate, the message is to look at the last line (loan costs) on any refi offer and compare it with what most people pay. (I'm inferring the point that it takes about two years of savings to earn back the cost; the video doesn't say that.)

2. Did you understand it from the pictures, the words and numbers, or both?
Both, but mostly the words and numbers. The rates, the $5,124, "$221 a month" and "paid in cash at closing" carry the story. The pictures help: the small $221 bundle next to the big $5,124 block ("one scale for both") makes the gap clear right away, and the dot on the range line shows the cost is in the middle. On their own, without the labels, the pictures wouldn't tell me much.

3. What did you not understand, and what couldn't you read?
- "Dollars of the day" is unclear. I think it means the amounts aren't adjusted for inflation.
- "one scale for both" is a bit cryptic, though I guessed it means the two money stacks are drawn to the same scale.
- In panel 6, the empty dotted box labeled "your letter?" seems to be asking me to compare my own refi offer's costs, but it isn't spelled out.
- The chart's range line has no dollar amounts at the ends or on the "middle half" box, so I can't tell what counts as a small or large bill.
- "HMDA" is an acronym I don't know.
- "the last line" in panel 1 presumably points to the Loan costs row.
- The tiny copy of the offer letter in panels 2–3 is too small to read, and so is the gray placeholder text under "pays off your current loan" in panel 1. Otherwise everything was readable.
===== S08 575fb350
File: 575fb350

1. What is this scene telling you?
It's asking whether refinancing is worth it for "Nora," an example borrower who stays about 3 years. The "1-point" rule of thumb says no, because her rate would only drop 0.59 points. Simple division ($5,124 in fees ÷ $221 a month saved) says yes, since she'd earn the fees back in about 24 months. But the scene then points out that each shortcut leaves something out: the 1-point rule ignores the $5,124 bill, and the division is missing an extra cost (the "+ ?"). So neither quick answer can be trusted by itself. For me, with a mortgage signed in 2022–2024, the message is that I shouldn't decide on a refi just from "rates dropped a point" or a quick break-even number.

2. Did you understand it from the pictures, from the words and numbers on screen, or both?
Both. The pictures carry the structure: the timeline showing the house, a green payback bar and a flag at "she sells or moves," the dot falling short of the dashed line, the grid of squares that stands for months, the red NO against the green YES, and the crossed-out bill. But the actual meaning comes from the words and numbers: 0.59, $5,124 ÷ $221, "about 24 months," "3 years," "not counted" and "something left out." Without the text, I couldn't have followed it.

3. What did you not understand, and what couldn't you read?
- I couldn't tell what the "+ ?" next to the $221 stands for. It says "something left out," but the scene never says what that is (maybe taxes, lost interest or a longer loan term?), so the point stays unfinished.
- I wasn't sure whether 0.59 is how far the rate drops or something else. I'm assuming it's the rate cut in percentage points.
- It's also not clear what $221 is. I'm assuming it's the monthly savings.
- "Fees: 2025 median (HMDA)" uses a term I don't know (HMDA).
- The crossed-out red "the bill: $5,124" and the faded, grayed-out division in panel 5 were a bit hard to read, but I could make them out. The small gray footnote text is also small and hard to read. Everything else was readable.
===== S08 5a17ef20
File: 5a17ef20

1. What is this scene telling you?
It asks whether refinancing is worth it for an example borrower, "Nora," who plans to stay 3 years. Her rate would drop only 0.59 points, less than the "1-point" rule of thumb, so that rule says NO. Simple break-even math says YES: about $5,124 in fees divided by $221 a month in savings is about 24 months, well under 3 years. The 1-point rule ignores the actual bill ("not counted"), and the division may be missing some cost too ("+ ?", "something left out"). For me, with a 2022–2024 mortgage, the takeaway is to work out my own fees against my monthly savings and not rely on the 1-point rule alone.

2. Did you understand it from the pictures, from the words and numbers on screen, or both?
Both. The timeline, the flag, the green bar and the grid of month boxes gave me the structure. The numbers ($5,124, $221, 0.59, 24 months, 3 years) and the NO/YES labels carried the actual meaning. Without the words and numbers I couldn't have followed it.

3. Which part, if any, did you not understand, and which words or numbers could you not read?
- I could read all the text. The smallest, dimmest labels ("time after refinancing", "no cut", "Nora (illustrative). Fees: 2025 median (HMDA)") were small but still readable.
- It's not clear what "0.59" measures. I assume it's a 0.59-percentage-point rate cut, but the screen doesn't say "rate" or "%".
- "The 1-point line" is never explained. I guessed it means the rule of thumb that refinancing needs a cut of at least 1 point.
- The scene never says what the "+ ?" / "something left out" is. It could be closing costs, the loan term restarting, or lost principal, so the final answer is left hanging.
- I don't know what "HMDA" stands for.
- The fee total ($5,124) isn't broken down, so I can't compare it to my own loan.
===== S08 75cdde8c
File: 75cdde8c

1. What is this scene telling you?
It asks whether refinancing is worth it for an example borrower, "Nora." A refinance pays off if you win back its closing fees before you sell or move, and here they test a 3-year stay. The scene gives two quick answers. The old rule of thumb says refinance only if your rate drops by at least 1 point. Her drop is 0.59, so that rule says NO, and it ignores the $5,124 bill. Simple division says YES: $5,124 in fees ÷ $221 a month in savings is about 24 months, which is less than 3 years. But the "+ ?" box and "something left out" hint that the simple division is also missing a cost. For me, with a 2022–2024 mortgage at a fairly high rate, the point is that neither shortcut is enough. I have to compare the fees against my monthly savings and how long I plan to stay, and watch for hidden costs.

2. Pictures, words, or both?
Both. The timeline with the house, the flag and the green bar, the dot sitting short of the dashed line, the grid of about 24 squares, and the red NO and green YES carry the idea. But I needed the words and numbers (0.59, $5,124 ÷ $221, "about 24 months", "3 years", "not counted") to understand it.

3. What I did not understand, and what I could not read
- I don't know what the "+ ?" and "something left out" refer to. The scene never says what the missing cost is. It could be things like restarting the loan term, extra interest or taxes.
- "0.59" is not labeled clearly. I assume it means a 0.59 percentage-point rate cut, but the scene doesn't say so, and it doesn't show Nora's old or new rate.
- "Fees: 2025 median (HMDA)" is small, and I don't know what HMDA stands for.
- The struck-through "the bill: $5,124" is hard to read because of the red strike line. The small grey labels ("no cut", "time after refinancing") and the dimmed "Simple division" panel in frame 5 are faint but readable.
===== S09 21adb722
File: 21adb722

1. What is this scene telling you?
It's showing a refinance offer that would move someone like me from a 7.62% rate to 7.03%. The new loan costs $5,124 up front and saves $221 a month, so it takes about 24 months ($5,124 ÷ $221) before the savings cover the cost. After that point the refinance starts paying off. The last panels add a second comparison: how much of the balance has been paid off since refinancing on the old loan versus the new one. The new loan's bar has a question mark on it, so that answer isn't shown yet.

2. Did you understand it from the pictures, from the words and numbers on screen, or both?
Both. The pictures (a stack of cash growing next to a $5,124 block, and a timeline of month tick marks filling up) show the idea of savings catching up to a cost. But the exact message comes from the words and numbers: the two rates, "Loan costs $5,124", "+$221 a month", "$5,124 ÷ $221 a month = 24 months", and the "24" on the months timeline. As someone with a 2022–2024 mortgage at around this rate, the "Your rate now 7.62%" line is what made me pay attention.

3. Which part, if any, did you not understand, and which words or numbers could you not read?
- I don't fully understand the final "balance paid off since refinancing: old loan vs new loan" part. The new loan's bar is marked "?" and it's shorter than the old loan's, which seems to hint that refinancing slows how fast you pay down the balance (perhaps because the loan term starts over). The scene doesn't say how much, or whether that cancels out the 24-month break-even.
- The fine print on the offer paper under "A new loan at a lower rate pays off your current loan." is only gray placeholder lines. I couldn't read any text there.
- The footer "Nora (illustrative). Fees: 2025 median (HMDA). Dollars of the day." is readable, but I'm not sure what "HMDA" or "Dollars of the day" mean. I take it to mean Nora is a made-up example and the $5,124 is a typical 2025 closing cost, not a real quote for me.
- The timeline has no numbers other than "24", so I couldn't tell how many months the full scale covers.
===== S09 6842bfa2
File: 6842bfa2

1. What is this scene telling you?
If I refinance from 7.62% to 7.03%, it costs about $5,124 up front and saves me about $221 a month, so I only come out ahead after about 24 months ($5,124 ÷ $221 = 24). The last part also hints at a catch: after refinancing, the new loan's "balance paid off" is a question mark next to the old loan, so the new loan may pay down principal differently than my current one does.

2. Pictures, words/numbers, or both?
Both. The stack of cash growing toward the "loan costs" block and the month tick marks show the break-even idea. But I needed the on-screen numbers (rates, $5,124, $221 a month, 24 months) and labels to get the actual message. Without the numbers, the pictures alone would be too vague.

3. What I didn't understand / couldn't read
- The "?" on the blue "new loan" box in frames 5–6 is never explained. I can guess it means I'd have paid off less of the balance with a new loan that starts over, but the scene doesn't say so, and the two boxes are only slightly different in size.
- The small print on the offer sheet under "A new loan at a lower rate pays off your current loan" is just gray placeholder lines, so I can't read it.
- The footnote "Fees: 2025 median (HMDA). Dollars of the day." is tiny and full of jargon. I don't know what HMDA is or what "dollars of the day" means.
- I couldn't read any numbers on the months axis except "24". The rest are unlabeled tick marks.
- It's not clear whether $221 a month is a real payment drop for a loan like mine (it says "Nora (illustrative)"), or what loan balance it assumes.
===== S09 c37fe0bd
File: c37fe0bd

1. The scene shows a refinance offer: the rate drops from 7.62% to 7.03%, and the new loan costs $5,124. That saves $221 a month, so it takes 24 months ($5,124 ÷ $221) for the savings to cover the costs. After that the scene brings in a second comparison, how much of the balance you have paid off on the old loan versus the new loan, and leaves the new loan marked with a "?". My guess is that it's warning that refinancing restarts the payoff clock. As someone who took out a mortgage at around 7% in 2022–2024, I can see this is about whether refinancing is worth it for me.

2. Both. The pictures explain the idea: a stack of money grows until it matches the "loan costs" block, and a tally of months marks the time. But I needed the words and numbers (the rates, $5,124, +$221 a month, and the "$5,124 ÷ $221 a month = 24 months" line) to get the actual message.

3. I didn't fully understand the last part. The "balance paid off since refinancing" blocks for the old loan and the new loan are never explained, and the new loan just shows a "?" with no number, so I can't tell whether it means I'd pay off less principal or what the point is. I also didn't understand the footer "Fees: 2025 median (HMDA). Dollars of the day." I don't know what HMDA is or what "dollars of the day" means. Everything else was readable, except the small gray lines of fine print on the offer paper in frame 1, which I couldn't read.
===== S10 1c3b0990
File: 1c3b0990

1. What is this scene telling you?
If I refinance, my mortgage's 30-year clock starts over. Early payments on a new loan go mostly to interest, so less of each payment pays down the balance. So even though refinancing saves about $221 a month, it takes longer than the simple math suggests to earn back the $5,124 in loan costs. The break-even point is month 30, not month 24, because the new loan's balance comes down more slowly (about $1,133 is still behind at month 24). For me, with a 2022–2024 loan, the message is: before I refinance, look at how much principal I'd give up, not just the monthly savings.

2. Pictures, words/numbers, or both?
Both. The clock hand resetting to zero and the stacks of cash versus the loan-cost block got the idea across. I needed the on-screen words and numbers ("goes to interest", "the new loan pays down less each month", $221 a month, $5,124, +$1,133 still owed, "Break-even: month 30, not month 24") to get the actual point and the numbers.

3. What I didn't understand / couldn't read
- The paydown bars in panels 2–3 were hard to read. "Magnified" and the thin green bar under each payment bar were confusing. I couldn't tell how big the difference between the old and new loan really is.
- In panels 4–6, the dashed red outline on top of the "new loan" block isn't labeled with a number. I guessed it shows the balance paydown lost compared to the old loan.
- It isn't clear how the $1,133 is calculated, or whether it's lost principal paydown or something else.
- The footer "Nora (illustrative). Fees: 2025 median (HMDA). Dollars of the day." was small but readable. I didn't know what HMDA or "dollars of the day" means, or who Nora is. I assume she's a made-up example borrower. The scene doesn't give Nora's rates or loan amount, so I can't tell whether it applies to my own mortgage.
- The small month tick labels on the timeline were tiny, but 24 and 30 were readable.
===== S10 58a2a3a4
File: 58a2a3a4

1. What is this scene telling you?
If I refinance my mortgage, the 30-year clock starts over, so early payments on the new loan go mostly to interest and less goes to paying down the balance. In this example the refinance saves $221 a month but costs $5,124 in loan costs, and because the new loan pays down less principal, breaking even takes until month 30, not the month 24 you get from simply dividing the costs by the monthly savings. For me, with a 2022–2024 loan (about 2–4 years in, like "Nora's" 35 payments), the message is to look past the simple payback math before refinancing.

2. Pictures, words/numbers, or both?
Both. The clock hand resetting to 12 and the shrinking green "pays down the loan" bar give the idea visually, but I needed the labels and numbers ($221 a month, $5,124 loan costs, $1,133 still owed, month 24 vs. month 30) to understand the actual point: that the simple break-even is too optimistic.

3. What I didn't understand / couldn't read
- Everything was readable. The small print was the hardest: the green bar note "(below: magnified)" and the footnote "Nora (illustrative). Fees: 2025 median (HMDA). Dollars of the day."
- I'm not sure who "Nora" is. I assume she's an example borrower introduced earlier in the video. I also don't know what "HMDA" stands for, or exactly what "Dollars of the day" means (probably not adjusted for inflation).
- In panel 5, it wasn't completely clear what the "+ $1,133 still owed" is. I take it to be the extra principal I'd still owe on the new loan compared with the old one, which gets added to the loan costs. The dashed outlines on the new-loan block hint at the same thing, but the picture doesn't spell it out.
- The monthly ticks on the timeline were too small to count one by one. I relied on the "24" and "30" labels.
===== S10 5b31e2a5
File: 5b31e2a5

1. What is this scene telling you?
Refinancing restarts my 30-year mortgage clock. Early payments go mostly to interest, so a new loan pays down less principal each month. The $221 a month I'd save looks like it covers the $5,124 in closing costs by month 24. But once you count the $1,133 in principal I'd still owe compared with keeping the old loan, I don't actually break even until month 30.

2. Did I understand it from the pictures, the words and numbers, or both?
Both. The clock face resetting to zero and the stack of cash growing toward the "loan costs" block made the idea feel intuitive. But I only got the real point from the text and numbers: "$221 a month," "$5,124," "+ $1,133 still owed," and "Break-even: month 30, not month 24." Without those, the pictures alone wouldn't tell me what the actual trade-off is.

3. What didn't I understand, and what couldn't I read?
- The "one payment" bars in frames 2–3 are a bit confusing. The two green bars (a thin one underneath marked "magnified") look almost the same length for the old and new loan, so the "pays down less each month" difference is hard to see.
- In frames 4–6 it wasn't obvious at first that the gap between the "old loan" and "new loan" blocks (the dashed red outline) is the same thing as the red-striped "$1,133 still owed" layer on the loan-cost block. I had to piece that together.
- The footnote "Nora (illustrative). Fees: 2025 median (HMDA). Dollars of the day." is small and hard to read. I don't know what HMDA is or what "dollars of the day" means. I also don't know who Nora is, what her rate or loan size is, or what rate drop the $221 comes from. That makes it hard to compare with my own 2022–2024 loan.
- The tiny tick labels on the month timeline (24, then 30) are small. Also, the green arc at the top of the clock with "35 payments made" is not labeled with a scale, so I couldn't tell how far through 360 payments it is.
- I could read the rest of the text.
===== S11 3704199a
File: 3704199a

1. What is this scene telling you?
For a made-up borrower named Nora, it shows what happens if refinancing gets her rate only 0.25 point lower. The savings grow too slowly ever to cover the $5,124 in loan costs. A 1-point cut would break even around month 38, but with a 0.25-point cut she "Never" breaks even, not even by the old loan's last payment. For me, with a 2022–2024 mortgage, the message is that a small rate drop isn't worth refinancing because the closing costs eat all of it.

2. Did you understand it from the pictures, from the words and numbers, or both?
Both. The picture shows the green savings line staying well below the white line and then curving back down, which tells me she never gets there. But I needed the words and numbers to know what the lines mean: "rate cut 0.25", "loan costs $5,124", "division: month 38", "Never", "not before the old loan's last payment", and "savings minus what she still owes".

3. What did I not understand, and what couldn't I read?
- "division: month 38" is an odd label. I guess it means the break-even point, but "division" isn't a word I'd use for that.
- In frames 2–4 it isn't clear which line goes with which scenario. I assume the white line is the 1-point cut, but nothing labels it on the chart.
- In frames 5–6 the green line rises and then falls back to zero. The label "savings minus what she still owes" helps, but I didn't fully follow why the line drops, or what the thin grey line near the start is.
- The x-axis ("months after refinancing") has no numbers, so I can't tell how many years the "Never" curve covers.
- Everything was readable. The only small problem was that the thin chart lines slightly cross the words "loan costs" and "savings" in frames 5–6.
===== S11 493774e1
File: 493774e1

1. What is this scene telling you?
If someone like me (the example is "Nora") refinances to cut the rate by only 0.25 point, paying $5,124 in closing costs up front, the savings never catch up with those costs. The green "savings minus what she still owes" curve rises, falls back, and never reaches the $5,124 line before the old loan would have been paid off. So a quarter-point cut on my 2022–2024 mortgage probably isn't worth refinancing.

2. Did you understand it from the pictures, from the words and numbers, or both?
Both. The big red "Never" and the green curve turning back down before it reaches the cost line gave me the main point. I needed the words for the rest: "rate cut 0.25," "loan costs $5,124," and "savings minus what she still owes."

3. What did I not understand, and what could I not read?
I could read all the text. These parts confused me:
- "division: month 38." The white line crosses the cost line at month 38, but I don't know what "division" means here. I'm guessing it's the break-even point for a bigger cut, maybe 1 point. Or it's how the break-even would look if you only counted monthly savings.
- The white line in panels 2–4 and the faint gray line in panels 5–6. What are they, and why does the green line bend into a hump instead of rising straight?
- The "1-point line" tick on the rate-cut slider. I think it marks a full 1-point cut to compare against, but it's never explained.
- The footer "Fees paid in cash. Dollars of the day." I think it means the fees weren't rolled into the loan and the amounts aren't adjusted for inflation, but that's a guess.
- "not before the old loan's last payment." It seems to mean she never breaks even during the old loan's remaining term, but it was a little hard to follow.
- The chart has no dollar or month numbers on its axes beyond "month 38," so I couldn't tell how big the savings get or how long the whole period is.
===== S11 e07535e0
File: e07535e0

1. What is this scene telling you?
If a refinance only lowers "Nora's" rate by 0.25 point, the monthly savings are too small to pay back the roughly $5,124 in loan costs. Once you account for what she still owes, she never comes out ahead, not even by the time the old loan would have been paid off. As someone with a 2022–2024 mortgage, I read it as a warning that a small rate drop isn't worth refinancing for.

2. Pictures, words/numbers, or both?
Both. The green line bending over and falling back to the axis before it ever reaches the "loan costs" line shows that the refinance never pays off. The big red "Never" and the caption "not before the old loan's last payment" confirm it. The "$5,124" and "0.25" figures give the scale.

3. What I didn't understand / couldn't read
- "division: month 38" (frames 2–4): I don't know what "division" means here. I'm guessing it's the break-even month for a full 1-point cut (the white line), but the word is confusing.
- In frames 1–4 the green line is a straight rising line. In frames 5–6 it becomes an arch that drops back down. The switch to "savings minus what she still owes" isn't explained, so I don't know why the curve suddenly changes shape.
- The "1-point line" tick on the slider isn't clearly tied to the white line.
- "Dollars of the day" is unclear. I assume it means not adjusted for inflation.
- In frames 5–6, "loan costs" is partly covered by the gray line, and the start of "savings minus what she still owes" is cut off at the left edge. Otherwise I could read all the text.
===== S12 157b988b
File: 157b988b

1. What is this scene telling you?
If rates fell by a full percentage point, refinancing would pay for itself fast. For "Nora", an example borrower, the savings line crosses the $5,124 in refinancing (loan) costs around month 18. That is well inside a 3-year stay. As someone with a 2022–2024 mortgage, I read this as: a one-point cut makes refinancing clearly worth it if I plan to stay in my home for more than about a year and a half.

2. Pictures, words/numbers, or both?
Both. The rising green line crossing the flat cost line shows the idea: savings catch up with costs. But I needed the words and numbers to know what it meant: "loan costs $5,124", "month 18", "3 years", "well inside 3 years", "months after refinancing" and the "rate cut" slider moving to the "1-point line".

3. What I did not understand / could not read
- The vertical axis has no label or scale. I assume the green line is total monthly savings added up over time, but the chart never says so. It also doesn't show how much Nora saves each month.
- "Counting what she still owes" is unclear. Does the math include the loan balance or payoff? I'm not sure how it changes the result.
- The chart doesn't give Nora's original rate, her new rate or her loan size, so I can't compare it with my own loan. The "ILLUSTRATIVE" tag tells me these are made-up numbers.
- In frames 1–2 the slider dot sits short of the 1-point line (a smaller cut?), and nothing is drawn yet. It isn't clear what those frames show.
- I could read all the text. The small grey labels ("rate cut", "months after refinancing", the footnote) are faint but readable.
===== S12 b036aa4a
File: b036aa4a

1. What is this scene telling you?
If rates were cut by a full percentage point, a borrower like "Nora" (a made-up example) who refinanced would earn back the $5,124 she paid in loan costs in about 18 months, well inside 3 years. So for someone like me, with a 2022–2024 mortgage, a one-point drop could make refinancing pay off fairly quickly.

2. Did you understand it from the pictures, from the words and numbers, or both?
Both. The pictures carry the story: the dot moves up to the "1-point line", the green line climbs and crosses the flat line, and a green bar marks the gap up to the 3-year mark. But I needed the words and numbers to know what those shapes mean: "loan costs $5,124", "month 18", "3 years", "well inside 3 years", "months after refinancing".

3. What did I not understand, and what couldn't I read?
I could read all the text. What's unclear:
- The green line isn't labeled. I'm assuming it's savings adding up over time, but the chart never says that, and it gives no monthly savings amount or rates (from what rate to what rate).
- "Counting what she still owes" is unclear to me. Does that mean the savings count the lower interest on her remaining balance and not just the smaller monthly payment?
- The small top slider ("rate cut" and the dot moving to the "1-point line") is easy to miss, and it doesn't show the actual starting rate or the new rate.
- "ILLUSTRATIVE" and "Nora (illustrative)" tell me this is a made-up example, so I can't tell whether my own break-even would look like this. The line also stops right after month 18, so I don't see what happens after that.
===== S12 e0a39ce5
File: e0a39ce5

1. What is this scene telling you?
If rates were cut by a full point, a borrower like "Nora" (a made-up example) who refinances would earn back her roughly $5,124 in refinancing costs through lower payments by about month 18. That's well inside 3 years, so for someone like me with a 2022–2024 mortgage, a refi after a full-point cut would pay for itself fairly quickly.

2. Did you understand it from the pictures, from the words and numbers on screen, or both?
Both. The picture shows the green line rising until it crosses the flat "loan costs" line, with a green bar showing the gap before the 3-year mark. I needed the words and numbers to know what those lines mean: "If the cut were a full point," "loan costs $5,124," "month 18," "3 years," "months after refinancing" and "well inside 3 years."

3. Which part, if any, did you not understand, and which words or numbers could you not read?
I could read all the text. Some things weren't clear to me:
- The green line isn't labeled. I assume it shows the total savings from the lower monthly payment, but the chart never says so.
- The "rate cut" slider at the top moves toward a "1-point line," but there's no scale. I can't tell what rate Nora started at, what rate she refinanced to, or how big her loan is.
- I'm not sure what "Counting what she still owes" means. Maybe the savings are measured on the remaining loan balance, not on the monthly payment alone.
- The vertical axis has no dollar figures, so apart from $5,124 I can't read any savings amounts off the chart.
- It's marked "ILLUSTRATIVE," so I don't know how closely my own loan would match Nora's.
===== S13 4709310c
File: 4709310c

1. What is this scene telling you?
It's about deciding whether refinancing is worth it for someone like me. For "Nora" (a made-up example), a refinance costs $5,124, and a rate cut of 0.5 point is her break-even line: at that size the monthly savings pay back the costs in exactly 3 years (month 36). The offer she actually got is a 0.59-point cut, which is above her line, so it pays back in less than 3 years and clears her bar. Before refinancing, I should work out my own break-even cut the same way (closing costs vs. monthly savings vs. how long I'll keep the loan) and not just go by the common "wait for a 1-point drop" rule.

2. Pictures, words/numbers, or both?
Both. The lines showed me the idea: the green line crosses the "loan costs" line at the 3-year mark, and the steeper white line crosses it earlier. But I needed the labels ("loan costs $5,124", "0.5 · Nora's line", "offer 0.59", "month 36", "1-point line", "paid back within 3 years") to know what the lines meant and what the numbers were.

3. What I did not understand / could not read
- Panel 6 adds a small red square with "?" and a small orange triangle with "?" near the top, next to the rate-cut scale. They have no labels, so I don't know what they stand for (maybe other scenarios or things still uncertain, like how long she'll stay in the house or what else could change).
- The "1-point line" is marked, but it's never explained. I guess it's the usual "refinance only if rates drop 1 point" rule, but the scene doesn't say so.
- "Counting what she still owes" is unclear to me. Does it mean the savings are counted on her remaining balance, or that the costs are counted as part of what she owes?
- The rate-cut scale has no numbers except 0.5 and 0.59, so I couldn't tell where 0 is or the exact spacing.
- In panels 5 and 6 the "3 years" label overlaps the white line and is a little hard to read, and in panel 6 the triangle's "?" overlaps "1-point line". Otherwise the text was readable.
===== S13 65b0a233
File: 65b0a233

1. What is this scene telling you?
Refinancing a made-up borrower, "Nora," costs $5,124, and a rate cut of half a point (0.5) pays that back in savings in exactly 3 years (month 36), so 0.5 is her break-even "line." A lender's offer of 0.59 beats that line and pays back sooner than 3 years. As someone who took out a mortgage in 2022–2024 at a high rate, I read it as: don't wait for the old "1-point" rule. Figure out your own break-even cut from your closing costs and how long you plan to stay, and a cut a bit above half a point can be worth it.

2. Did you understand it from the pictures, the words and numbers, or both?
Both, but mostly the words and numbers. The rising green line crossing the flat $5,124 cost line at the dashed "3 years" mark shows the break-even idea. I only knew what it meant from the labels: "loan costs $5,124," "month 36," "0.5 · Nora's line," "offer 0.59," and "her offer (0.59): paid back within 3 years." The titles ("Where is her line?" / "Half a point: paid back in exactly 3 years") told me what the question and the answer were.

3. What did you not understand, and what couldn't you read?
- Frame 6 adds a small red square with "?" and an orange triangle with "?" near the top of the rate-cut scale. I couldn't tell what they stand for. They might be other offers or warnings, or something the next scene covers.
- "Counting what she still owes" is unclear. I can't tell whether the savings count only the lower monthly payment or also the faster drop in loan balance.
- The chart never gives Nora's loan size, her old and new rates, or the dollar savings per month. I can't check the $5,124 / 36-month math or apply it to my own loan without them.
- The rate-cut scale has no numbers except the 0.5, 0.59 and "1-point line" labels, so the dots' exact positions are approximate.
- The small grey text was faint but readable. In frames 5–6, "3 years" overlaps the white line and is a little hard to read, and in frame 6 the "?" overlaps "1-point line."
===== S13 ecbe7e6f
File: ecbe7e6f

1. What is this scene telling you?
A refinance costs "Nora" (a made-up example) $5,124. If rates drop by half a point, her monthly savings add up to that $5,124 in exactly 36 months, so half a point is her break-even line, not the usual "1-point" rule of thumb. A lender's offer of a 0.59-point cut clears that line and pays back the cost in less than 3 years. For someone like me who took out a mortgage in 2022–2024, the takeaway is that I shouldn't wait for a full 1-point drop. I should work out my own break-even cut from my closing costs and how long I plan to stay.

2. Did you understand it from the pictures, the words and numbers, or both?
Both. The rising savings lines crossing the flat "loan costs $5,124" line at the dashed "3 years / month 36" marker show the payback idea. The titles and labels ("rate cut," "1-point line," "0.5 · Nora's line," "offer 0.59," "her offer (0.59): paid back within 3 years") tell me what the lines and dots mean. Without the words the lines would just be abstract.

3. What did you not understand, and what could you not read?
- Panel 6 adds a small red square with a "?" and an orange triangle with a "?" near the rate-cut scale. They have no labels, so I don't know what they stand for. Maybe other offers or other people's lines, still to come.
- The "rate cut" scale has no numbers at the ends, so I had to guess that it runs from 0 to 1 point.
- "Counting what she still owes" is unclear. I'm not sure if the savings count only lower interest or also the change in the remaining balance.
- The graph doesn't show the actual rates, loan size or monthly savings, so I can't check the $5,124 or the 36 months against my own loan.
- Everything was readable, though some small gray text ("months after refinancing," the footnote) is faint, and in panel 6 the triangle's "?" overlaps "1-point line."
===== S14 0133ec52
File: 0133ec52

1. What is this scene telling you?
Two made-up borrowers, Walt with a $115,000 loan in a small house and Nora with a $375,000 loan in a bigger house, get the same refinance offer: the rate drops from 7.62% to 7.03%. Walt's loan is far smaller, but his bill ($3,667) is only a little smaller than Nora's ($5,124), so the rate cut is worth much less to him in dollars. As someone paying a 2022–2024 mortgage at around that rate, what I take from it is that whether refinancing pays off depends a lot on how big my loan is, not just on the rate drop.

2. Did you understand it from the pictures, from the words and numbers, or both?
Both, but mostly the words and numbers. The house sizes show that Walt's loan is smaller, and the bill boxes show two costs next to each other. But the rates, the loan amounts, the bill amounts and the captions "far smaller loan" and "only a little smaller bill" are what actually give the message.

3. What did you not understand, and what could you not read?
- It wasn't clear what "bill" means. My guess is the closing costs or fees for refinancing, since it isn't a monthly payment (a $3,667 monthly payment on a $115,000 loan makes no sense). The scene never says so, and that confused me.
- The small print on the "Refinance offer" paper on the ground (frames 3–6) was too small to read. I could only roughly make out "7.62%", "7.03%" and "$3,667".
- I didn't know what "HMDA" in the footnote ("Bills: 2025 medians (HMDA)") stands for.
- The scene doesn't show how much each person would save per month, so I couldn't tell whether the refinance is worth it for either of them.
===== S14 3bf1b97c
File: 3bf1b97c

1. What is this scene telling you?
Two made-up homeowners, Walt ($115,000 loan) and Nora ($375,000 loan), get the same refinance offer (7.62% down to 7.03%), but Walt's bill is $3,667 and Nora's is $5,124. Walt's loan is about a third the size of Nora's, yet his bill is only a little smaller. So the fixed costs of refinancing hit a small loan much harder, and the same rate cut pays off far less for him. For me, with a 2022–2024 mortgage somewhere around those rates, the point is to compare the closing costs to my loan size before assuming a refinance is worth it.

2. Did you understand it from the pictures, from the words and numbers on screen, or both?
Both, but mostly the words and numbers. The house sizes (small house vs. big house, "to scale with the loan") and the similar-sized "bill" boxes show the idea visually. The rates, loan amounts, bill amounts and the captions "far smaller loan" / "only a little smaller bill" are what made the message clear.

3. Which part, if any, did you not understand, and which words or numbers could you not read?
- "Bill" is ambiguous. I am assuming it means the closing costs / fees for the refinance, because the footer says "2025 medians (HMDA)" and $3,667 on a $115,000 loan is too high to be a monthly payment. The scene never says "closing costs" and never says whether it is a one-time or a monthly amount, so I had to guess.
- The scene doesn't show how much either person would save per month or how long it takes to break even. That's the number I would need to decide about my own mortgage.
- I could not read the small printed "Refinance offer" sheet on the ground (frames 3–6). I could only just make out the heading and what look like 7.62%, 7.03% and $3,667. The row labels on it were too small to read.
- The footer text ("Walt, Nora: illustrative. Bills: 2025 medians (HMDA). House size to scale with the loan.") is small but readable. "HMDA" is an acronym that most viewers won't know.
===== S14 e1890272
File: e1890272

1. What is this scene telling you?
Two made-up borrowers with the same refinance offer, from 7.62% down to 7.03%. Walt has a small $115,000 loan and Nora has a big $375,000 loan, yet Walt's bill is $3,667 and Nora's is $5,124. So a far smaller loan comes with only a slightly smaller bill. As someone who signed a mortgage at high rates in 2022–2024, what I take from it is that refinancing costs are mostly fixed, so on a small loan the savings from a lower rate may not cover the cost.

2. Pictures, words/numbers, or both?
Both, but mostly the words and numbers. The houses drawn to match the loan size and the two bill boxes let me compare at a glance. The actual point comes from the labels, though: the loan amounts, the bill figures, the rate change, and the captions "far smaller loan" and "only a little smaller bill."

3. What I didn't understand / couldn't read
- The small "refinance offer" paper on the ground is too tiny to read. I can make out 7.62%, 7.03% and what looks like $3,667, but not its row labels.
- The scene never says what "bill" means. I'm assuming it's the closing costs or fees for the refinance, not a monthly payment, but I'm not sure. It also doesn't say what the monthly savings would be, or how long it would take to earn back the bill.
- The footer says "Bills: 2025 medians (HMDA)". I can read it, but I don't know what HMDA is.
===== S15 83ec4bbd
File: 83ec4bbd

1. What is this scene telling you?
If someone with a small loan refinances, the costs of refinancing hardly go down: Walt has a $115,000 loan and pays $3,667 in costs, about 3.2% of his loan, while Nora has a $375,000 loan and pays $5,124. Both get the same rate drop, from 7.62% to 7.03%. But Walt saves only $68 a month compared with Nora's $221, so it takes him about 75 months (over six years) to earn back those costs. For someone like me with a 2022–2024 mortgage, the message is that a smaller balance makes refinancing much less worth it.

2. Pictures, words/numbers, or both?
Both, but mostly the words and numbers. The bar charts in 1–4 show the size difference, but I needed the dollar labels and the captions ("the bill barely shrinks", "his bill = about 3.2% of his loan", "savings shrink with the loan") to follow the argument. In 5–6 the picture of a growing stack of money catching up to the "loan costs" block, with a month counter, made the idea of break-even easy to see. The "Break-even: month 75" headline confirmed it.

3. What I did not understand or could not read
- In frame 1, Walt's loan-costs bar is shown full length with no number, and it seems to match Nora's bar at first. That confused me until frame 2 showed $3,667.
- In 5–6, I'm not sure what "+ still owed" under "loan costs" means. Maybe some of the costs get added to the loan balance, but that isn't explained.
- The tick marks on the month counter are too small and packed to count. Only "75" is labeled.
- The small grey footnote ("Walt, Nora: illustrative. Same offer: 7.62% → 7.03%.") is faint, but I could read it. It's also not clear whether the 7.62% is the old rate on the loans (a 2023-style rate like mine) or something else. Loan term and closing-cost details aren't given.
- All other large text and numbers were readable.
===== S15 9f5df2f5
File: 9f5df2f5

1. What is this scene telling you?
It's about refinancing. Two made-up borrowers get the same offer to drop their rate from 7.62% to 7.03%. Walt only owes $115,000, but his refinance costs are still $3,667 (about 3.2% of his loan), almost as much as Nora's $5,124 on a $375,000 loan. So he saves only $68 a month, compared with her $221, and it takes him about 75 months (over six years) to break even. For me, with a mortgage from 2022–2024 at a rate like that, the point is: a lower rate isn't enough. With a smaller balance, the fixed closing costs can eat up the savings, so I should work out my own break-even before I refinance.

2. Pictures, words/numbers, or both?
Both, but mostly the words and numbers. The bar charts show at a glance that Walt's loan is small but his costs are nearly full length ("the bill barely shrinks"). The house scene, with the tall stack of $68 bills growing each month until it matches the $3,667 block, shows the break-even idea. Still, I needed the labels ($115,000 vs. $375,000, $3,667 vs. $5,124, $68 vs. $221, "Break-even: month 75") to get the actual message.

3. What I did not understand / could not read
- I wasn't sure at first who Nora is, because she only appears as the green "full length" reference bars. The footnote says both people are illustrative.
- "loan costs + still owed" in the house scene was a little unclear. Does the red striped roof mean costs that get rolled into the loan?
- The fine print (the footnote "Walt, Nora: illustrative. Same offer: 7.62% → 7.03%." and "Nora's bar = full length") and the small green numbers on the right ($375,000, $5,124, $221) are small and low contrast, but I could read them. The tick marks on the month axis in frames 5–6 can't be counted. Only "75" is labeled.
- In frame 1 the gold "Loan costs" bar has no number yet. It's filled in as $3,667 from frame 2 on.
===== S15 dceaf2b8
File: dceaf2b8

1. What is this scene telling you?
The scene compares two made-up borrowers. Both get the same refinance offer, from 7.62% down to 7.03%. Nora has a $375,000 loan, so her closing costs are $5,124 and she saves $221 a month. Walt has a $115,000 loan, but his closing costs are still $3,667, which is about 3.2% of his loan, and he saves only $68 a month. At that rate Walt needs about 75 months (over 6 years) to earn back his costs. For me, with a mortgage I signed in 2022–2024, the point is that a lower rate only pays off if my loan is big enough and I plan to keep it long enough to reach break-even.

2. Did you understand it from the pictures, the words and numbers, or both?
Both, but mostly the words and numbers. The bar charts show how Walt's loan is much smaller than Nora's while his costs are not much smaller. In the 3D scene, the stack of $68 payments grows until it matches the $3,667 cost block, which makes break-even easy to see. Still, I needed the dollar amounts, the rates and "Break-even: month 75" to get the actual message.

3. What did you not understand, and what could you not read?
- The 3D scene took some thought. The "loan costs + still owed" block has a red striped top, and it was not clear what "still owed" means or what the striped part stands for. It might be costs rolled into the loan, or interest on them.
- The chart says "Loan costs" but does not say whether that means closing costs, points or fees.
- The chart does not say which of the two rates is the old one and which is the new one. I guessed it is a refinance from 7.62% to 7.03%.
- The small tick marks on the month timeline are not labeled, except for "75" in the last frame.
- The small gray footnote ("Walt, Nora: illustrative. Same offer: 7.62% → 7.03%.") and the "Nora's bar = full length" subtitle are faint, but I could read them. Every word and number was readable to me.
===== S16 1825798e
File: 1825798e

1. What is this scene telling me?
It's saying refinancing only pays off if you stay in the house long enough to earn back the closing costs. Walt has a small $115,000 loan, and his refinance costs $3,667 but only saves him $68 a month. If he sells after 3 years he's still $1,777 short, so he'd need the rate to drop about 1.12 points to break even in 3 years. Nora's bigger $375,000 loan only needs about a 0.5-point cut. For me, with a 2022–2024 mortgage, the lesson is that the smaller my balance, the bigger the rate drop I need before a refi is worth it.

2. Pictures, words and numbers, or both?
Both, though mostly the words and numbers. The picture of the small pile of cash growing toward the tall "loan costs" block without reaching it, plus the tick marks counting months, gave me the basic idea. The actual message came from the labels: "$1,777 short," "+$68 a month," "1.12 points," "Smaller loan, bigger cut needed," and the Nora and Walt loan amounts.

3. What I didn't understand or couldn't read
- The last panel's bars confused me. "Bill: barely shrinks" shows $3,667 next to $5,124, and "Savings: shrink" shows $68 next to $221. I'm guessing the green bars are Nora's figures and the yellow ones are Walt's, but there's no legend, and I don't get why a bill that goes from $5,124 to $3,667 "barely shrinks."
- "Loan costs + still owed" wasn't clear to me. Does "still owed" mean the rest of the closing costs or something else? And I couldn't tell how the $3,667 was calculated.
- The scene never gives Walt's actual old rate or new rate, so I can't compare it to my own mortgage.
- "1-point line" wasn't explained until the small caption "point = one percentage point of the rate." That caption, the "no cut" label and the "months" / "3 years" labels are in small gray text and hard to read, but I could make them out. The tick marks aren't numbered, so I couldn't count the months.
- The "ILLUSTRATIVE" tag suggests these are made-up example numbers, not real rates.
===== S16 3c18eee4
File: 3c18eee4

1. What is this scene telling you?
If "Walt", who has a small $115,000 loan, refinances and then sells after 3 years, the $68 a month he saves never catches up with the $3,667 in loan costs, so he is still $1,777 short. To break even in 3 years he would need a rate cut of about 1.12 percentage points. Someone with a larger loan, like "Nora" with $375,000, only needs about 0.5 point, because her costs barely shrink but her monthly savings are much bigger ($221 vs $68). So for me, with a mortgage signed in 2022-2024, a refinance only makes sense if my rate drops enough to cover the closing costs before I expect to sell or move, and a small loan needs a bigger drop.

2. Pictures, words/numbers, or both?
Both, but mostly the words and numbers. The house, the "costs" wall and the growing cash stack alongside the month ticks (panels 1-2) showed the idea that savings build up slowly against a fixed cost. But the actual message ($1,777 short, 1.12 points, 0.5 point, the loan sizes and the bars in panel 6) came from the text and numbers.

3. What I did not understand / could not read
- I could read everything. The smallest gray text ("point = one percentage point of the rate", "no cut", "months") was faint but readable.
- It is not fully clear what "loan costs + still owed" means. I think it is the refinance closing costs plus whatever part of them is still unpaid, but "still owed" is confusing.
- In panel 6 it is not obvious at first which bar belongs to Walt and which to Nora. I assumed yellow = Walt ($3,667 costs, $68 savings) and green = Nora ($5,124 costs, $221 savings), but there is no legend. "Bill: barely shrinks" was also a little unclear; I took "bill" to mean the closing-cost bill.
- The scene does not say what Walt's current rate or new rate is, so I can't directly compare it with my own mortgage.
===== S16 fcdd2530
File: fcdd2530

1. What is this scene telling you?
It's about whether refinancing pays off: Walt, with a small $115,000 loan, pays $3,667 in loan costs to refinance but saves only $68 a month, so if he sells after 3 years he's still $1,777 short. To break even within 3 years he would need a rate cut of 1.12 points, more than the usual "1-point" rule of thumb. Nora, with a $375,000 loan, would need only a 0.5-point cut, because the costs barely shrink for a smaller loan but the monthly savings shrink a lot. For me, with a 2022-2024 mortgage, the point is that a rate drop is only worth refinancing for if it's big enough, compared with my loan size and how long I'll stay, to earn back the closing costs.

2. Pictures, words/numbers, or both?
Both, but mostly the words and numbers. The pictures helped: the cash stack grows next to the cost block but doesn't reach the top, the marker slides past the 1-point line, and the two houses are different sizes. But I couldn't get the actual message (the $3,667 cost, $68 a month, $1,777 short, 1.12 vs 0.5 points, and the loan amounts) without reading the labels.

3. What I didn't understand / couldn't read
- "loan costs + still owed": I'm not sure what "still owed" means here or how much of the $3,667 block it is. The math also doesn't add up for me: $68 x 36 months is about $2,448, and $3,667 - $2,448 is about $1,219, not $1,777. So "still owed" must add something that isn't explained.
- Panel 6: the green bars ($5,124 and $221) aren't labeled with a name. I'm guessing they are Nora's costs and savings next to Walt's $3,667 and $68 in yellow. "Bill: barely shrinks" is confusing at first, since "bill" could mean my monthly payment instead of the refinancing costs.
- The "1-point line" is shown as a benchmark but never explained as a rule of thumb.
- It's not said what the rates are before and after, or whether my own loan size is closer to Walt's or Nora's.
- Readability: all the main text was readable. The small grey subtitle ("point = one percentage point of the rate") and the small labels were faint but readable. You can't count the individual month tick marks, but the "3 years" label covers that.
===== S17 38fb0ceb
File: 38fb0ceb

1. What is this scene telling you?
Two people who got mortgages in the same month (October 2023, at 7.62%) both get the same rate drop to 7.03% and face similar refinancing bills (about $5,100-$5,500), but the one with the bigger loan (Anjali, $655,000) saves $387 a month, earns back her bill by month 18 and is $5,250 ahead after 3 years. The takeaway is that with a big loan, a rate cut of only about a third of a point can pay for itself within 3 years, so I shouldn't assume I need the old "1-point" rule before a refinance is worth it; how much I owe matters.

2. Did I understand it from the pictures, the words/numbers, or both?
Both, but mostly the words and numbers. The houses, the "bill" boxes, the growing stack of cash and the month tick bar showed the idea of paying a cost and then earning it back. But I needed the labels (rates, loan amounts, "$387 a month", "paid back: month 18", "$5,250 ahead") to know what was actually going on.

3. What I did not understand / could not read:
- Nora's outcome is never shown. She gets a $5,124 bill but no monthly savings or payback month, so I can't tell whether the same cut is worth it for her. On the last chart her green dot sits at 0.5, which I'm guessing means she'd need about half a point, but that isn't labeled.
- The gold triangle at "1.12" isn't explained. It's past the "1-point line," but I don't know whose number it is or what it stands for.
- The line "under the conforming limit (the ceiling for standard loans)" seems to go with Nora, but it isn't clear whether Anjali's $655,000 loan is over or under that limit, or why that matters here.
- It isn't clear what the "bill" is. I assume it's refinancing closing costs, but the screen never says so. "2025 medians (HMDA)" is also jargon I don't know.
- The math didn't fully add up for me: $387 x 36 months minus $5,514 comes to more than $5,250, so I'm not sure how "$5,250 ahead" was calculated.
- Everything was readable. The small caption text and the month tick marks were tiny but legible.
===== S17 c260c0ce
File: c260c0ce

1. What is this scene telling you?
Two neighbors got the same rate cut in the same month (October 2023, 7.62% down to 7.03%), and the refinance "bill" is about the same for both. Anjali has the bigger loan ($655,000), so she saves $387 a month, earns back her $5,514 bill by month 18 and is $5,250 ahead after 3 years. The last frame says a big loan like hers only needs about a third of a point of rate cut to pay off within 3 years, while a smaller loan like Nora's needs more (0.5 or more). For me, with a mortgage signed in 2022–2024, the takeaway is that a fairly small rate drop could make refinancing worth it, especially if my loan is large.

2. Pictures, words and numbers, or both?
Mostly the words and numbers. The houses, mailboxes, cash stack and month tick bar helped me follow the story (the big house, the money piling up, the payback point on the timeline), but I only got the actual point from the labels: the rates, the loan sizes, "bill," "+$387 a month," "paid back: month 18," "$5,250 ahead after 3 years" and the last chart.

3. What I didn't understand or couldn't read
- "Bill" is never explained. I guessed it means refinance closing costs, but the video doesn't say that. The mailbox makes it look like a monthly mortgage bill, which confused me at first.
- Nora's monthly savings and payback time are never shown, so the comparison is only half there. I had to guess that the green dot at 0.5 on the last chart is hers.
- On the last chart, I don't know whose number the yellow triangle at 1.12 is, or what it stands for. The "1-point line" is also unclear. Is it a rule of thumb?
- "Conforming limit" is only partly explained, and I don't know what "HMDA" stands for.
- "2025 medians" is confusing: the bills are 2025 medians, but the refinance happens in October 2023.
- The small footnote text at the bottom and the tick labels on the month bar were hard to read at this size. Beyond those, I could read all the words and numbers.
===== S17 c9a5a9e2
File: c9a5a9e2

1. What is this scene telling you?
Two neighbors with the same October 2023 rate (7.62%) refinance to the same lower rate (7.03%) and face similar refinance bills (about $5,124 and $5,514), but Anjali's bigger $655,000 loan saves her about $387 a month, so she pays the bill back by month 18 and is $5,250 ahead after 3 years. The takeaway is that the rate cut you need to make refinancing pay off depends on the size of your loan: a big loan like Anjali's only needs about a third of a point, while a smaller loan like Nora's (or mine) needs a bigger drop. That makes me think about checking my own loan balance against the closing costs before I refinance.

2. Pictures, words/numbers, or both?
Both, but mostly the words and numbers. The houses, the "bill" boxes and the growing stack of cash with the months timeline show the idea of paying back a cost over time. The actual meaning (same rate, same cut, the loan sizes, $387 a month, paid back at month 18, $5,250 ahead) only comes from the on-screen text.

3. What I did not understand / could not read
- I could read all the text. The small footnotes ("Anjali, Nora: illustrative. Bills: 2025 medians (HMDA).") were readable but tiny.
- It is not clearly said what the "bill" is. I assume it means refinance closing costs, but the word "closing costs" never appears, and I don't know what "HMDA" is.
- Nora's outcome is never shown: we never see her monthly savings or when (or if) she pays back her $5,124 bill.
- In the last panel, only the red square is labeled (Anjali, about a third of a point). The green dot at 0.5 and the triangle at 1.12 have no labels, so I had to guess that 1.12 is Nora's needed cut and wasn't sure what the 0.5 dot stands for.
- "Conforming limit" is explained briefly, but it is unclear why it matters here, since both loans are noted as under it.
===== S18 21f47c20
File: 21f47c20

1. What is this scene telling you?
Refinancing costs about the same flat fee (here $5,124) whatever the size of your loan, so how much your rate has to drop to make it worth it depends on your balance. A small $115,000 loan needs a cut of about 1.12 points to earn the fees back in 3 years, a $375,000 loan needs about 0.5 point, and a $655,000 loan needs only about a third of a point. So the old "refinance when rates drop 1 point" rule doesn't fit any of them, and I should work out the number for my own loan. For me, with a 2022–2024 mortgage (probably taken out at around 7%, like the 7.62% on the offer), even a smaller drop could be worth it if my balance is large.

2. Did you understand it from the pictures, from the words and numbers on screen, or both?
Both. The bars shrinking as the house icons get bigger showed me the idea: bigger loan, smaller rate cut needed. But I needed the labels ("Rate cut needed, by loan size", "to pay back the fees within 3 years", "1.12 points / 0.5 point / about a third of a point", the loan amounts, and "1-point rule of thumb: fits none") to understand what was actually being measured and what the takeaway was.

3. Which part, if any, did you not understand, and which words or numbers could you not read?
I could read everything. A few points were less clear:
- The link between the offer in frame 1 (7.62% to 7.03%, a 0.59-point cut, with $5,124 in costs) and the chart isn't spelled out. I assume the $5,124 is the fee used for all three borrowers, but the chart doesn't say so.
- "HMDA" in "Fees: median 2025 refinance bill (HMDA)" is an acronym I don't know.
- The footnote "October 2023 rate" isn't explained. I guess it's the starting rate the borrowers are assumed to have, which is close to when I got my loan, but I'm not sure.
- "fees paid in cash" in the footnote: I don't fully understand why that matters, or what changes if the fees are rolled into the loan instead.
- The dashed "your loan?" house invites me to find my own number, but the scene doesn't tell me how to calculate it. The frame 1 fine print and the footnotes are also small and could be hard to read on a phone.
===== S18 44ac72f1
File: 44ac72f1

1. What is this scene telling you?
Refinancing costs roughly the same fixed fees (about $5,124, the median 2025 bill) no matter how big your loan is. So how much your rate has to drop before you earn those fees back within 3 years depends on your balance. A small $115,000 loan needs about 1.12 points, a $375,000 loan about 0.5 point, and a $655,000 loan only about a third of a point. The usual "refinance if rates drop 1 point" rule doesn't really fit any of them. As someone with a 2022–2024 mortgage, I take it to mean I should work out my own break-even using my loan size, not a rule of thumb.

2. Pictures, words/numbers, or both?
Both. The bars getting shorter as the houses get bigger showed me the idea: bigger loans need smaller rate cuts. But I needed the numbers and labels to get the actual message: the offer sheet (7.62% to 7.03%, $5,124 in costs), the point values, the loan amounts, the "1-point rule of thumb: fits none" line, and the title "Rate cut needed, by loan size / to pay back the fees within 3 years."

3. What I didn't understand / couldn't read
I could read everything. A few things weren't fully clear to me:
- "HMDA" in "Fees: median 2025 refinance bill (HMDA)." I don't know what it stands for.
- The footnote "October 2023 rate." I'm not sure whether it means the example borrowers took out their loans in October 2023, or that the math uses that month's rates.
- How the 7.62% to 7.03% offer in the first frame connects to the three borrowers. It looks like a 0.59-point cut, but the scene doesn't say whose offer it is or which bar it matches.
- The dashed "your loan?" house is a prompt to plug in my own balance, but the scene doesn't show how to calculate my number.
- The "ILLUSTRATIVE" and "not advice" labels tell me Walt, Nora and Anjali are made-up examples.
===== S18 49efd33c
File: 49efd33c

1. What is this scene telling you?
A refinance only pays off if the rate drop covers the closing costs (about $5,124 here). The bigger your loan, the smaller the cut you need to earn those fees back within 3 years: about 1.12 points on $115,000, 0.5 point on $375,000, and about a third of a point on $655,000. So the old "only refinance if you can cut the rate by 1 point" rule of thumb doesn't fit any of these borrowers. I should work out the break-even for my own loan size (the "your loan?" house). My rate from 2022–2024 is probably close to the 7.62% on the offer, so this applies to me.

2. Pictures, words/numbers, or both?
Both. The bars and house sizes show the pattern: bigger house means a bigger loan and a shorter bar, so a smaller cut is needed. But I needed the words and numbers to understand what it means: "Rate cut needed, by loan size," "to pay back the fees within 3 years," the point values, the loan amounts, and the "1-point rule of thumb: fits none" line. Without the text, the bars alone would not tell me what was being measured.

3. What didn't I understand / couldn't read?
I could read almost everything. Some things are unclear or hard to follow:
- The dashed outline house labeled "your loan?" is only a prompt. It doesn't give me a number, so I have to work out my own break-even myself.
- The footnotes are very small: "Fees: median 2025 refinance bill (HMDA)" and "Assumes: fees paid back within 3 years · median 2025 bills · October 2023 rate · fees paid in cash · illustrative borrowers · not advice." I could just about read them, but "HMDA" isn't explained. It's also unclear whether "October 2023 rate" is the 7.62% starting rate, and whether the same $5,124 fee applies to all three loan sizes.
- "About a third of a point" is vague compared with the exact figures for the other two.
- In panel 1, the gray lines under "pays off your current loan" on the offer sheet are placeholder text with nothing to read.
===== S19 21abe925
File: 21abe925

1. What is this scene telling you?
Refinancing a mortgage in 2025 cost real money in closing costs. The middle half of bills fell between about $3,443 and $8,270, and one example borrower, "Nora," paid $5,124. Whether a refi makes sense for someone like me, with a 2022–2024 loan, depends on my own rate, bill and balance. Rolling the fees into the loan or switching to a shorter term changes the math.

2. Did you understand it from the pictures, the words and numbers, or both?
Mostly from the words and numbers. The range bar with the dot for Nora helped me see where her bill sat within the range. The pictures alone didn't tell me much, though. The three faint colored bars in frame 1 had no labels, and the dotted house icon only makes sense because of the questions next to it.

3. What did I not understand, and what couldn't I read?
- Frame 1: the three colored bars (tan, green, red) have no labels or numbers. I guess they stand for the "three illustrative borrowers," but I can't tell what they measure. They vanish in the next frame.
- The subtitle mentions "national average rates," but no rate is ever shown. That's the number I care about most for deciding whether to refinance from my 2022–2024 rate.
- "different math" in frame 6 is vague. It doesn't say whether fees added to the loan or a shorter term makes a refi better or worse.
- I'm not sure what "HMDA" means. It's apparently a data source for total loan costs.
- "Nora's $5,124" is small, orange-on-blue text, and the yellow dot sits on top of it, so it was a bit hard to read. Everything else was readable.
===== S19 2dc043c7
File: 2dc043c7

1. What is this scene telling you?
In 2025, the typical total cost of a refinance ran about $3,443 to $8,270 (half of all bills fall in that range), and one example borrower, "Nora," paid $5,124. But whether refinancing makes sense for me depends on my own rate, bill and balance, and things like rolling the fees into the loan or switching to a shorter term change the math.

2. Did you understand it from the pictures, from the words and numbers on screen, or both?
Both, but mostly from the words and numbers. The range bar with the dot made the "typical range" and where Nora sits easy to see. The dashed house next to "your rate? your bill? your balance?" told me to think about my own mortgage. Without the dollar amounts and labels, the pictures alone would not have told me much.

3. Which part, if any, did you not understand, and which words or numbers could you not read?
- Frame 1 shows three colored blocks (brown, green, dark red) with no labels. I couldn't tell what they stood for. I'm guessing they're the "three illustrative borrowers," but nothing on screen says so.
- The scene never says what my rate would need to be for a refinance to pay off, or how "different math" plays out. With a 2022–2024 rate, I want to know if refinancing is worth it, and the scene just raises questions without answering them.
- I don't know who "Nora" is. She seems to be one of the made-up borrowers, but she isn't introduced here.
- "HMDA 2025 (total loan costs)" in the footer is small and uses an acronym I don't know (I assume it's a government mortgage data source).
- The small text is hard to read: the gray subtitle ("national average rates · median bills · three illustrative borrowers"), the footer, and "Nora's $5,124," where the orange dot partly covers the label. The big numbers ($3,443, $8,270) were easy to read.
===== S19 7af017a8
File: 7af017a8

1. What is this scene telling you?
In 2025, the typical bill for refinancing a mortgage ran from about $3,443 to $8,270 for the middle half of borrowers. One example borrower, "Nora," paid $5,124. The scene then asks me to think about my own rate, bill and balance, and says that if I roll the fees into the loan or pick a shorter term, the math changes. As someone who took out a mortgage in 2022–2024, I read it as: "Before you refinance, remember that it costs a few thousand dollars, and how you pay those costs changes whether it's worth it."

2. Did you understand it from the pictures, from the words and numbers, or both?
Both, but mostly the words and numbers. The range bar with the dollar amounts and the "half of all bills fall in here" label did most of the work. The house icon and the pill-shaped tags helped show that the scene was turning to my own situation, but I needed the text to know what they meant.

3. What did you not understand, and what could you not read?
- Frame 1 lost me. It shows three colored blocks (brown/gold, green, dark red) with no labels or numbers, and they disappear in frame 2. I guess they stand for the "three illustrative borrowers," but nothing on screen says so.
- "Nora" is never explained. I don't know who she is, what her loan looks like, or why her $5,124 matters, apart from falling inside the middle range.
- "Different math" is vague. It doesn't say whether rolling in the fees or taking a shorter term makes refinancing better or worse, or by how much.
- The heading says "national average rates," but no rate appears in these six frames.
- "HMDA 2025 (total loan costs)" in the footer is jargon to me. I don't know what HMDA is.
- Text I struggled to read: "Nora's $5,124" is small, orange, and partly covered by the dot on the bar. The blue "half of all bills fall in here" label and the grey subtitle and footer are small and low-contrast, but I could make them out.
===== S20 53ea2c5f
File: 53ea2c5f

1. What is this scene telling you?
Whether refinancing after a rate cut pays off depends on how long you stay in the home. In this example the homeowner comes out only +$1,039 ahead if she sells after 3 years, but +$8,093 ahead if she stays 7 years, because the rate cut decides how fast the fees come back and your stay decides whether you are still there to collect. As someone with a 2022–2024 mortgage, the question it leaves me with ("your home?") is how long I really plan to stay before I refinance.

2. Did you understand it from the pictures, from the words and numbers on screen, or both?
Both. The pictures (the stack of cash beside the house growing, and the timeline dot moving from 3 years to 7 years) show that staying longer earns more. The words and numbers ("+$1,039 ahead if she sells after 3 years", "+$8,093 ahead if she stays 7 years", "rate cut: how fast the fees come back") tell me that the subject is a refinance or rate cut and how big the amounts are. I would not know the topic was refinancing from the pictures alone.

3. Which part, if any, did you not understand, and which words or numbers could you not read?
I could read all the text. What was unclear: the scene never shows the loan size, the old and new interest rates, or the closing costs behind the $1,039 and $8,093 figures, so I cannot compare them to my own loan (the "ILLUSTRATIVE" label suggests they are only an example). The word "refinance" never appears; I had to guess it from "rate cut" and "fees". The outlined house labeled "your home?" in frame 6 seems to be asking me to plug in my own situation, but that was a little vague. The small tick marks on the timeline have no labels.
===== S20 88227f24
File: 88227f24

1. What is this scene telling you?
It's about refinancing after a rate cut. Whether a refi pays off depends mostly on how long you stay in the house, and only you know that. In this example the homeowner comes out only $1,039 ahead if she sells after 3 years, but $8,093 ahead if she stays 7. For someone like me with a 2022–2024 mortgage, the point is that before refinancing I should ask myself whether I'll actually still be in this house long enough for the savings to cover the fees.

2. Did you understand it from the pictures, from the words and numbers on screen, or both?
Both. The pictures carry the idea: the stack of cash grows as the dot moves along the "years in the home" timeline, and a ghost outline of a house with "your home?" appears at the end. But the words and numbers tell me what it actually means: the title "The number only you know: how long you stay," the dollar amounts, and the two lines "rate cut: how fast the fees come back" and "your stay: whether you are still there." Without the text, I would only have seen money piling up next to a house.

3. Which part, if any, did you not understand, and which words or numbers could you not read?
I could read all the text and numbers. What I couldn't tell:
- The screen never says what rate she refinanced from and to, what the closing costs were, or what the loan amount was. So I can't compare $1,039 and $8,093 to my own situation. The "ILLUSTRATIVE" label confirms these are just example numbers.
- It doesn't show the break-even point, meaning the year when she stops losing money. It also doesn't show what happens if she sells before 3 years, when she might actually lose money.
- The wireframe house with "your home?" in the last frame is a bit vague. I took it to mean "your own home / how long will you stay?", but it could also suggest moving to a different home.
- "Rate cut" doesn't say who cut rates or how much. It isn't clear whether this means a Fed cut or just lower mortgage rates in general.
===== S20 e148957a
File: e148957a

1. What is this scene telling you?
Whether a refinance to a lower rate pays off comes down to how long you stay in the home. In this made-up example the homeowner ends up only about $1,039 ahead if she sells after 3 years, because the closing costs take a while to earn back, but about $8,093 ahead if she stays 7 years. As someone who took out a mortgage in 2022–2024 at a high rate, I take it to mean I should only refinance if I expect to still be living here long enough to get the fees back.

2. Did you understand it from the pictures, from the words and numbers on screen, or both?
Both, but mostly from the words and numbers. The pictures help: the timeline slider, the stack of cash that starts small and gets tall, and the dotted outline of a house marked "your home?". But the stack alone doesn't tell me what the money is or where it comes from. The dollar amounts, "if she sells after 3 years" / "if she stays 7 years", and the captions "rate cut: how fast the fees come back" and "your stay: whether you are still there" are what explain it.

3. Which part, if any, did you not understand, and which words or numbers could you not read?
I could read all the words and numbers. What isn't clear:
- The scene never says it's about refinancing. I assumed that from "rate cut" and "fees", but it could also mean something like buying points.
- It doesn't give the rate cut, the loan amount or the fees behind $1,039 and $8,093, so I can't compare them with my own loan. The "ILLUSTRATIVE" tag tells me they're example numbers anyway.
- The timeline has no break-even point, so I can't tell when she starts coming out ahead. I also don't know if "ahead" already has the fees taken out.
- The dotted house labelled "your home?" in the last frame is vague. I think it's asking me to think about my own home and how long I'll stay, but it could also mean moving to a different house.

---
## Kiểm lại S11 sau sửa (`e8f6fce`): 3 agent mới, file ngẫu nhiên, cùng câu hỏi. Kết quả 3/3 đọc đúng (0.25 điểm; phép chia: tháng 38; tính dư nợ: không bao giờ). Chỗ còn khó: đường xanh ở khung 3–4 chưa có nhãn; lý do đường cong đi xuống; đường xám mảnh không có nhãn.

===== S11-v2 02355f75
File: 02355f75

(Viewer: an American paying a mortgage signed in 2022–2024.)

1. What is this scene telling you?
If someone like me refinances for only a 0.25-point rate cut, the usual "divide the closing costs by monthly savings" math says I'd break even around month 38. But once you account for what I still owe on the new loan, the benefit never gets past the $5,124 in loan costs before the old loan would have been paid off. So a tiny rate cut isn't worth refinancing.

2. Did I understand it from the pictures, the words and numbers, or both?
Both, but mostly from the words and numbers. The picture of the straight white line crossing the cost line at month 38, and then the green curve rising and falling back without ever reaching it, shows the idea. I needed the labels ("loan costs $5,124", "simple division: month 38", "Never", "savings minus what she still owes") to know what the lines meant.

3. What did I not understand, and what couldn't I read?
- I wasn't sure what the green line in frames 3–4 was before it turned into the curve in frame 5, or why it bends back down. I'm guessing it's because the new loan restarts the payoff clock, but the scene doesn't say that.
- The "1-point line" mark on the rate-cut slider isn't explained. I assume it's a comparison to a full 1-point cut, but it's never shown.
- The thin gray diagonal line in frames 5–6 isn't labeled.
- "Dollars of the day" in the footnote was unclear to me (I think it means not adjusted for inflation).
- It never says Nora's loan size, her old or new rate, or what month "Never" is measured up to, so I can't compare it to my own mortgage.
- The small gray text (the footnote, "months after refinancing", "rate cut") is small but I could read it. There were no numbers I couldn't read.
===== S11-v2 19080052
File: 19080052

1. What is this scene telling you?
If "Nora" refinances for a rate only 0.25 point lower and pays $5,124 in closing costs, the usual shortcut (costs divided by monthly savings) says she breaks even around month 38. But once you count what she still owes on the new loan, her savings never catch up with the costs before the old loan would have been paid off. So for someone like me, a 2022–2024 borrower hoping for a small rate drop, a quarter-point refi likely never pays for itself.

2. Did you understand it from the pictures, from the words and numbers on screen, or both?
Both. The words and numbers ("loan costs $5,124", "simple division: month 38", "Never", "not before the old loan's last payment") give the message. The pictures back it up: the white line crosses the cost line, the green line stays lower, and then the green curve rises and falls without ever reaching the cost line.

3. Which part, if any, did you not understand, and which words or numbers could you not read?
I could read all the text. What was unclear:
- The "1-point line" mark on the rate-cut slider is never explained. I guess it is a comparison to a full 1-point cut, but it never gets used.
- In panels 2–4 I'm not sure what the green line is, or why it runs lower than the "savings alone" line. It has no label until panels 5–6.
- "Savings minus what she still owes" is fuzzy to me. I'm not sure if it means the loan balance, or why the curve rises and then drops back to zero.
- The faint gray diagonal line in panels 5–6 has no label.
- The x-axis has no month numbers except the 38, so I can't tell when the old loan's last payment is. "Dollars of the day" is also a little jargon-y. I take it to mean the numbers aren't adjusted for inflation.
===== S11-v2 a6f0557c
File: a6f0557c

1. What is this scene telling you?
If Nora refinanced for only a 0.25-point rate cut, the simple math (closing costs of $5,124 divided by the monthly savings) says she breaks even in month 38. But once you account for what she still owes on the loan, her savings never actually cover the costs, "not before the old loan's last payment." For me, with a 2022-2024 mortgage, the point is that a small rate drop probably isn't worth refinancing for.

2. Pictures, words/numbers, or both?
Both. The words and numbers set it up: "If her rate were cut only 0.25 point," "loan costs $5,124," "simple division: month 38," and the big red "Never." The lines show the story: the white "savings alone" line crosses the cost line, but the green line rises much more slowly, then curves back down and ends below it without ever reaching it. Without the "Never" label I wouldn't have been sure what the arch meant.

3. What I didn't understand / couldn't read
- "Savings minus what she still owes": I don't fully get why the amount she still owes is subtracted from her savings, or why that makes the green line turn down and head toward zero. It's the key idea, and I had to take it on faith.
- In frames 3-4 the green line appears without a label until frame 5, so at first I didn't know it was a different measure.
- The "1-point line" mark on the rate-cut slider isn't explained. I guess it's a comparison to a full 1-point cut shown earlier in the video.
- "Fees paid in cash. Dollars of the day." is small and I'm not sure what "dollars of the day" means (no inflation adjustment?).
- There are no numbers on the time axis, so I can't tell when the green line peaks or ends, or how long the loan is.
- Everything was readable, though the small grey footnote and axis labels were faint. In frames 5-6 the thin grey line runs through "loan costs" and "not before," but I could still read them.
