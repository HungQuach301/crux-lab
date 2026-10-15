# Grading packet (blind). You are an independent grader. Each label is one reader's answers about a short muted animation of object X (named in the label header). Grade literally with the rubric (Vietnamese). Flags: advice_stated (the animation, its text or picture states or implies buy, rent, wait, choose/avoid), advice_inferred (reader's own conclusion), caution_only.

## Rubric
 (ghi trước; "ý người xem phải đọc ra")
| Vật | Đúng nghĩa (1) cần đủ | 0,5 | 0 |
|---|---|---|---|
| **N1 the street** | (a) dãy nhà = nhiều thời điểm/tháng mua khác nhau xếp theo thời gian (1991 → 2016); (b) nhà sáng đèn = mua có kết quả tốt hơn thuê (sau 10 năm), nhà tối/cửa vàng = thuê tốt hơn; (c) phần lớn sáng, có một đoạn tối | đủ 2/3 | ≤ 1/3 hoặc chỉ tả hình ("houses light up") |
| **N2 the rent tag** | (a) thẻ trên căn hộ = mức tiền thuê giả định (đổi 5 → 4 → 6 %); (b) khi mức thuê đổi, số nhà sáng đèn đổi theo (thuê cao hơn → nhiều nhà sáng hơn); (c) kết quả mua/thuê phụ thuộc vào tiền thuê giả định | đủ 2/3 | ≤ 1/3 |
| **N3 Nina + đèn riêng** | (a) một người (nhân vật chính, minh hoạ) có đèn/ánh sáng riêng đi theo; (b) cô đứng giữa căn hộ (thuê) và ngôi nhà (mua), quay nhìn rồi bước về phía giữa; (c) cô đang cân nhắc thuê hay mua | đủ 2/3 | ≤ 1/3 |

Cờ `advice_stated` (hình/chữ nêu hay ngụ ý mua/thuê/chờ) → vật trượt ngay. `advice_inferred`, `caution_only`: báo, không chặn.
**Ngưỡng mỗi vật:** 2/2 đúng (điểm 1, không `advice_stated`) → ĐẠT; 0/2 → TRƯỢT; lệch → người thứ 3, đạt khi ≥ 2/3.
**Trượt → đổi loại hình trước G1** (luật tạm 13/10 (c); E6 sửa bằng hình trước, nhãn là cách cuối), tối đa 2 vòng mỗi vật (luật tạm: ≤ 2 vòng mỗi lỗi cả tập); vòng 2 vẫn trượt → G1 nêu bản trước/sau cho chủ dự án. Mỗi vòng ghi `fix: picture|label` + lý do.


Output JSON only (no prose, no code fence): {"R1": {"score": 1|0.5|0, "advice_stated": true|false, "advice_inferred": true|false, "caution_only": true|false, "why": "<one line, quote the reader>"}, ...}

### R1 — object N1 the street
1. It shows a grid of identical small houses. Each house stands for one starting year, from 1991 to 2016, and possibly one scenario per year. The legend in frame 6 says a lit house means the buyer ended up ahead after 10 years. A dark house with an amber door means the renter ended up ahead.

2. At first (frame 1) every house is gray and unlit. The houses then light up amber row by row (frames 2–5), and the camera moves in closer. A block of them stays dark. In frame 6 the view flattens into a top-down chart with year labels. Most of the grid is lit. The dark block sits roughly between 2001 and 2007, with a few scattered dark houses near its edges.

3. In most of the periods shown, buying beat renting over a 10-year horizon. The exception is a stretch of starting years around 2001–2007. That is probably when homes were bought near the housing-bubble peak and then lost value in the crash, so the buyers did worse than renters. The result depends on when you buy, and the animation doesn't show the prices or rates behind it.

4. A viewer would likely conclude that buying usually wins if you hold the home about 10 years. They would also see that timing matters, because buying at a market peak can leave you behind a renter. As a renter in 2026, you shouldn't treat this as a verdict on your own case. Your answer depends on local prices, mortgage rates, how long you'll stay, and what you'd do with the down payment otherwise.

5. The animation only shows the pattern: mostly lit houses and one dark cluster. It doesn't say what to do. The advice in answer 4 and my guess about the 2001–2007 crash are my own conclusions. The video may have said more, but I only have the six frames.

### R2 — object N3 Nina + đèn riêng
1. It's a dark, night-time 3D scene labeled "Nina · ILLUSTRATIVE". A small peg-like figure, presumably Nina, has a glowing yellow dot next to its head. On the left is an apartment building with lit windows. On the right is a single-family house with a red roof, a lit window and a dark door.

2. Nina starts right next to the apartment building, in frames 1–3. In frames 4–6 the figure moves right, away from the apartment and across the open ground toward the house. The apartment's shadow stays behind it. The camera seems to shift slightly. The yellow dot stays beside the figure's head throughout. The house stays at the right edge and doesn't visibly get closer.

3. The most natural reading is a move from renting to owning: Nina leaves the apartment (renting) and heads toward the house (buying). The dot could be a thought, an idea or a light, but nothing in the frames says what it stands for. The scene doesn't show any numbers, such as rent, mortgage, costs or timelines, and Nina hasn't reached the house by frame 6.

4. A viewer could take away "transitioning from renting to owning is a journey or a goal", and perhaps that it's a gradual, uncertain move through a dark, empty gap. It gives nothing concrete for your own question of whether renting costs more than buying. There are no prices, no break-even point and no comparison of monthly costs. The "ILLUSTRATIVE" label also signals that it isn't real data.

5. The animation itself doesn't suggest any advice. It only shows movement from one building toward the other. The renting-versus-buying meaning, and any advice from it, is my own interpretation of the apartment and house imagery. For your real decision you'd need actual numbers, like local rent, mortgage rates, down payment, taxes, maintenance, and how long you plan to stay.

### R3 — object N2 the rent tag
1. It shows a grid of many small orange houses, with an apartment building in the foreground. The building has a sign reading "RENT" followed by a percentage. Some houses in the grid are orange (lit or occupied) and others are dark (unlit or empty).

2. The rent percentage on the sign goes 5%, 5%, 4%, 4%, 6%, 6%. The dark patch of houses changes with it. In frames 1–2 (5%), a sizable dark band sits in the middle of the grid. At 4% (frames 3–4) the dark area looks larger and spreads toward the left edge. At 6% (frames 5–6) the houses shift back toward orange. The dark area shrinks to a small sliver by frame 6, and some houses show a brownish, in-between color mid-transition.

3. My reading is that the houses stand for homes or households. Orange means something like "buying makes sense" or "owners," and dark means "renting is the better deal" or "priced out." The sign suggests the rent-to-price relationship, or a rent growth rate, is the variable. When that number moves, more or fewer households tip from one side to the other. I can't read the exact labels at this resolution, so the color meaning is inferred, not stated.

4. As a renter, the cautious takeaway is that the rent-versus-buy answer isn't fixed. It depends on rent levels or rent growth, and it can change across a whole market even with small moves of 1–2 percentage points. Higher rent (6%) seems to push more people toward the orange "buy" side. So I'd run my own numbers on rent, price, mortgage rate, and how long I'd stay, instead of relying on a general rule.

5. That advice is mostly my own conclusion. The animation is muted and has no visible explanation, legend, or recommendation. It only shows the rent percentage changing and the houses changing color. The link between "higher rent" and "buying is better," and the idea of advice for renters, come from me.

### R4 — object N1 the street
1. It shows a grid of many small 3D houses, one for each starting year from 1991 to 2016. Each house stands for a person who bought a home in that year instead of renting. The final frame adds a legend. A lit house means the buyer ended up ahead after 10 years. A dark house with an amber door means the renter ended up ahead.

2. At first all the houses are gray and unlit. Then they light up in amber, starting from the early-1990s columns. The lighting sweeps across the grid. A block of houses in the middle stays dark, with a few scattered exceptions. The camera moves from a low angle at the edge of the grid to a top-down view. That final view is labeled with the years 1991, 2001, 2007 and 2016.

3. For most starting years, buying beat renting over a 10-year horizon. The exception is a band of starting years from roughly 2001 to 2007, where the renter came out ahead. Those 10-year periods would have included the mid-2000s housing peak and the crash that followed. In other words, the answer depended heavily on when you bought. I'm reading the dark band's exact boundaries off a small, blurry frame, so treat them as approximate.

4. A viewer like me would probably take away three things:
   - Buying usually wins over a decade, so renting isn't automatically the cheaper choice.
   - Timing matters. Buying near a market peak can leave you worse off than a renter after 10 years.
   - Buying makes more sense if you expect to stay about 10 years or longer.

   It isn't personal advice. The animation doesn't account for my local prices, my mortgage rate in 2026, my down payment or my job stability.

5. The animation itself suggests the first three points. It shows the buyer-versus-renter outcome by year and the dark gap around 2001–2007. The advice in point 4 is my own conclusion. The frames contain no explicit recommendation, and I can't see what assumptions it used, such as rates, rent growth, costs or location. I also can't tell from these frames whether it covers the whole US or one city. Those details would change how well it applies to my situation.

### R5 — object N2 the rent tag
1. It shows a grid of many small orange houses, with a gray apartment building in the foreground. The building has a sign reading "RENT" and a percentage. Some houses in the grid are dark or dim, and the rest are lit orange.

2. The rent percentage on the sign changes from 5% (frames 1–2) to 4% (frames 3–4) to 6% (frames 5–6). The dark patch of houses changes with it. At 5% the dark band is large. At 4% it is large and spreads toward the left edge. At 6% most of the dark houses turn orange again, and only a small dark area is left. Frames 3 and 5 show brownish houses, which are in the middle of switching color.

3. This is my reading, and the frames have no labels or captions. The orange houses probably stand for homes that are worth buying compared with renting, or for households that buy. The dark ones are homes where renting is the better deal, or where households keep renting. The sign likely shows the rent level or the rent-to-price ratio. When rent is higher (6%), more houses look worth buying. When rent is lower (4%), fewer do, and renting wins in more places. So the point seems to be that whether buying beats renting depends on how rent compares with home prices.

4. A viewer might take away that there is no single answer to rent versus buy. It depends on the local rent-to-price ratio. Where rent is high relative to prices, buying looks better. Where rent is low, renting looks better. A renter like me might run the numbers for their own market and not rely on a general rule. They would check rent against the purchase price, mortgage rates, taxes and upkeep.

5. The animation did not state that advice. It only showed the rent number changing and the houses changing color. The advice and my reading of what the colors mean are my own conclusions. There was no legend, and the video was muted.

### R6 — object N3 Nina + đèn riêng
1. It shows a simple 3D night scene labeled "Nina · ILLUSTRATIVE". A small peg-shaped figure, presumably Nina, stands between two buildings. On the left is a multi-window apartment block. On the right is a small house with a red roof and a door. A small glowing yellow dot floats next to the figure's head. The frames contain no words, numbers or prices.

2. Nina starts right next to the apartment building, in frame 1. She then moves steadily to the right across the ground, away from the apartment and toward the house. By frames 5 and 6 she is closer to the house, roughly midway or a bit past it. The glowing dot moves with her. The camera also seems to shift slightly. The apartment's shadow and the warm light pool on the ground stay in the scene. Nothing else changes: the buildings' windows stay lit and no numbers appear.

3. The most likely reading is a metaphor for a renter moving from renting (the apartment) toward owning (the house). The label "ILLUSTRATIVE" says it's a concept picture and not real data. The dot could stand for an idea, a goal or a hope, but nothing in the frames says so. The animation never shows whether the move is good or bad, or what it costs. Frame 6 doesn't show her arriving at the house, so even the story is unfinished.

4. A viewer could take away the idea that renters tend to move toward homeownership, or that Nina is aiming for it. That is a mood, not advice. The video has no numbers on rent, mortgage payments, down payments, price trends or the time Nina would stay in the home, and those are what decide whether renting or buying costs more. As a renter wondering about this, I'd learn nothing about my own situation from it. To decide, I'd need to compare my actual rent with the full monthly cost of owning (mortgage, taxes, insurance, maintenance) and think about how long I'd stay.

5. The animation only suggests the movement from apartment to house, and even that is a loose reading. The idea that buying is better, or that I should buy, is my own conclusion. The video gives no cost comparison and no explicit message. The "ILLUSTRATIVE" label also tells me not to treat it as evidence.
