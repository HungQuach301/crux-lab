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

## Bổ sung (13/10, ghi TRƯỚC khi đọc; vật mới WRITER khai ở C2 v1 `story/beats.md`): cùng giao thức, cùng ngưỡng
| Vật | Đúng nghĩa (1) cần đủ | 0,5 | 0 |
|---|---|---|---|
| **N4 the glass box** (hộp kính tiền mặt của người thuê) | (a) tiền (các bó) được cất trong một hộp kính đóng kín, cạnh căn hộ = tiền để dành của người thuê; (b) hộp đầy dần: mỗi lần thêm một bó (để dành thêm theo thời gian); (c) tiền chỉ nằm đó, không được đầu tư / không sinh lời thị trường | đủ 2/3 | ≤ 1/3 |
| **N5 the fog** (sương cuối phố) | (a) cuối dãy nhà là sương/mù, con đường đi tiếp vào sương; (b) trong sương không có nhà/kết quả nào; (c) phần sau dữ liệu (tương lai, các năm gần đây) chưa biết — không có kết quả, không dự đoán | đủ 2/3 | ≤ 1/3 |


Output JSON only (no prose, no code fence): {"R1": {"score": 1|0.5|0, "advice_stated": true|false, "advice_inferred": true|false, "caution_only": true|false, "why": "<one line, quote the reader>"}, ...}

### R1 — object N5 the fog
1. It shows a 3D grid of small orange toy houses on a dark surface, seen at an angle. Beyond the houses, the grid continues as empty dotted outlines of lots. A bright, hazy glow sits in the upper right. There is no text, axis, or legend, so nothing says what the houses stand for.

2. The houses disappear over time. In frame 1 the grid is mostly full, and only the far right edge shows empty outlines. By frames 4–6 only a few columns on the left are still filled. The rest are dotted outlines where houses used to be. The glow and camera barely change. The houses vanish from the far side toward the near side, so the filled area shrinks steadily.

3. The most literal reading is that something housing-related is running out or shrinking. Possible meanings include a shrinking supply of homes, fewer homes people can afford, or a shrinking share of households who can buy. The empty outlines suggest homes that could exist but don't. I can't tell which of these it is, because the frames carry no labels, numbers, or captions.

4. A viewer might take away "housing is getting scarcer or less attainable." As a renter, I might read that as pressure to buy sooner, or as a sign that buying is out of reach. The frames don't give anything to base a decision on. They show no prices, rents, mortgage rates, or time scale. I wouldn't compare renting and buying on the strength of this animation.

5. The animation only suggests the general idea of houses disappearing and a shrinking filled grid. Everything about affordability, renting versus buying, or advice to act is my own interpretation. The muted frames contain no text or data tying the houses to rent, prices, or ownership.

### R2 — object N5 the fog
1. It shows a 3D grid of small orange houses on a dark plane, with a bright glow at the upper right. Some grid slots are empty and drawn as faint dotted outlines. There's no text, labels, or numbers.

2. The houses disappear over time. In frame 1 the grid is mostly full. By frame 6 only a few columns of houses remain at the left, and most of the grid is empty dotted outlines. The houses vanish from the far, right-hand side first. The camera angle and the glow stay roughly the same.

3. Literally, the supply of houses is shrinking, or houses are being removed or becoming unavailable. The animation doesn't say why. It could stand for housing inventory running out, homes being bought up, or affordability pushing homes out of reach. Without labels, that is only a guess.

4. A viewer might conclude that homes are getting scarce, so buying is getting harder and renting is the only option. They might also read it as "buy now before there are none left." Neither is a solid basis for a decision. The animation has no prices, rents, rates, or dates.

5. That advice is my own reading. The animation only shows houses disappearing. It doesn't mention rent, buying, costs, or timing. The rent-versus-buy question comes from my own situation. To answer it I'd need real numbers: local home prices, mortgage rates, rent, how long I'd stay, and what the down payment could earn if invested.

### R3 — object N4 the glass box
1. It shows a figure labeled "Nina · ILLUSTRATIVE" standing between an apartment building with a "RENT" sign and a clear box labeled "CASH". A small yellow dot floats beside the figure's head. I can't tell what it stands for. It might be a thought or an idea.

2. The box starts empty. Green cash bars drop in from above one at a time, and the stack grows until the box is nearly full by frame 6. In frame 3 one bar appears to be moving near the building. The building, the figure and the sign stay the same throughout.

3. Nina lives in a rented apartment and her cash keeps piling up. The "ILLUSTRATIVE" tag says this is a generic example and not real data. The most direct reading is that a renter who isn't buying keeps accumulating savings. The animation shows no rent being paid, no home price, no mortgage and no investment growth. So it doesn't actually show whether renting costs more than buying.

4. A viewer might conclude that renting lets you build up cash, so renting is fine or even better than buying. Someone could also read it the other way, as a reminder that the saved cash only matters if you actually save it. As a renter in 2026, I couldn't take any real decision from it. It has no numbers for rent, down payment, maintenance, taxes, appreciation or what the cash earns.

5. The animation itself only suggests that cash accumulates alongside renting. The advice in my answer to question 4 is my own interpretation, not something the animation states. It has no text, no figures and no comparison to buying, and the "ILLUSTRATIVE" label warns against treating it as evidence. To compare renting and buying for myself, I'd need to run my own numbers, such as monthly rent against the full cost of owning, plus what the saved cash would earn.

### R4 — object N4 the glass box
1. It shows a simple 3D scene labeled "Nina · ILLUSTRATIVE". A figure (Nina) stands between an apartment building with a "RENT" sign and a glass box labeled "CASH". A small yellow dot floats beside the figure's head.

2. In frame 1 the cash box is empty. In frames 2 to 6, green cash bricks drop in one at a time, from above the scene or from near the building, and the pile in the box grows. By frame 6 the box is nearly full. The building, the figure, and the yellow dot stay the same throughout.

3. The most natural reading is that Nina rents, and the cash she isn't spending on something else (such as a down payment or mortgage) is piling up. That cash can be saved or invested. The label "ILLUSTRATIVE" says the scene is a made-up example and not real data. The animation gives no numbers: no rent amount, no home price, no interest rate, no time scale.

4. Not much that is specific. A viewer might conclude that renting can let you build up cash, which is a pro-renting message. The scene doesn't show the other side of the comparison. It has no home purchase, no equity, no home appreciation, no mortgage interest, taxes, or maintenance, and no cash that is lost to rent. So it can't tell me whether renting costs more than buying. For that I'd have to run my own numbers, including price-to-rent ratio, mortgage rates, how long I'd stay, and what my savings would earn.

5. The animation only suggests the picture of cash accumulating next to a rented building. The "renting lets you save" reading is my interpretation, and the advice in question 4 is my own conclusion. The video is muted and has no text beyond the labels, so it makes no explicit claim or recommendation.
