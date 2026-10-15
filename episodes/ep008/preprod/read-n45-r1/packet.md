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

### R1 — object N4 the glass box
1. It shows a simple 3D scene with a gray building with nine lit windows, which looks like an apartment or house. Next to it is a clear glass box labeled "CASH". There is no text, narration, or other explanation.

2. The box starts empty in frame 1. Green cash bundles then drop into it from above, one at a time. The pile grows from a thin layer in frame 2 to several stacked layers by frame 6. The building doesn't change, and the camera angle shifts only slightly.

3. The literal meaning is that cash is accumulating next to a building. The building could stand for a home, a rental unit, or housing in general. The most natural reading is that money builds up in a pile that is separate from the housing. That could be savings kept while renting, or money you aren't putting into a house. It could also mean the opposite: cash piling up for a landlord or owner. The animation doesn't say which.

4. As a renter wondering about rent versus buying, I wouldn't take much from it. A loose takeaway might be "money you save adds up over time." Another might be "keep cash on hand alongside housing costs." Neither is a real answer to rent versus buy. The animation gives no prices, rates, time frame, or comparison between the two options.

5. That conclusion is mostly mine. The animation shows only a building and a growing cash pile, with nothing to say who the cash belongs to or why it's growing. Any advice would come from what I bring to it. If you want to decide about renting versus buying, you'd need real numbers: rent, home price, mortgage rate, down payment, taxes, maintenance, how long you'd stay, and what you could earn by investing the difference.

### R2 — object N5 the fog
1. It shows a 3D grid of identical orange-roofed houses, in neat rows on a dark ground. A large pale, glowing void sits at the right. There is no text, no numbers and no labels.

2. The houses disappear over time. In frame 1 the grid is full and dense. By frames 3 and 4, the houses nearest the glowing area are gone. By frames 5 and 6 only a few columns remain at the left edge. The pale void grows and takes over the scene, and the camera seems to shift a little.

3. Literally, the housing stock is being erased, or swallowed by the blank area. In the abstract, it reads as housing disappearing or becoming scarce. It could stand for a shortage of homes, or for homes being lost to something large and faceless. The video doesn't say which, and it gives no cause.

4. A viewer would probably take away that homes are scarce and getting scarcer. They might guess that prices or rents will keep climbing, so buying sooner would beat waiting. Someone who rents and wonders whether rent costs more than owning could take that as pressure to buy before supply runs out. That would be a shaky conclusion. The animation has no prices, rents, mortgage rates or time scale, so it can't show whether renting or buying costs more.

5. The scarcity or disappearing-homes idea comes from the animation, because the visuals show houses vanishing. The advice in question 4, buying or renting, is my own inference. Nothing in the frames recommends either choice. A real rent-versus-buy decision depends on things the video never shows. Those include local price-to-rent ratios, mortgage rates, down payment, how long you'd stay, maintenance, taxes and what else you could do with the money.

### R3 — object N5 the fog
1. It shows a grid of small orange-roofed houses laid out in rows on a dark surface. A large pale, glowing gray-blue area sits off to the right. There is no text, no labels, no numbers, and no audio.

2. The houses disappear over time, and the pale area grows to replace them. In frame 1 the grid is full. By frames 2 and 3, houses on the right and far side are gone. By frame 4, about half are gone. In frames 5 and 6, only a few columns remain at the left. The camera also seems to shift slightly as this happens.

3. My reading is that the houses are housing supply, and it is being eaten away or wiped out. That could be a shrinking stock of homes, or homes being taken off the market. The pale area could be emptiness, a void, or a flood or fog. Without captions I can't tell which, or whether the cause is investors, a shortage, or something else. It may be a metaphor for scarcity, with fewer homes available meaning higher prices and rents.

4. The animation gives a renter like me no concrete advice. If I read it as "housing is getting scarcer," I might guess that rents and home prices will stay high or keep rising. That would make me think waiting to buy won't necessarily make it cheaper. It tells me nothing about whether renting or buying costs more for me. That depends on my local price-to-rent ratio, mortgage rate, down payment, how long I'd stay, and maintenance and taxes.

5. The animation doesn't suggest any advice. It has no text, numbers or call to action, so any advice is my own conclusion. Even the "scarcity" reading is my interpretation of the visuals, not something the animation states.

### R4 — object N4 the glass box
1. A simple 3D scene with a gray building with lit yellow windows, standing next to a clear box labeled "CASH". Green bundles of money drop into the box.

2. The building doesn't change. The box starts empty in frame 1. Bundles fall in one at a time (frames 2–5) and stack up, and by frame 6 the box is mostly full in rows of three, with nothing left falling.

3. The most natural reading is that cash accumulates over time next to a fixed building. That could mean saved money piling up, or money being collected from or paid out around a property. The video has no text beyond "CASH" and no numbers, so it doesn't say which. As a renter, I'd read it as "money builds up while the housing stays the same."

4. A viewer might take away "keep saving and the pile grows," or "money steadily accumulating matters more than the building." The animation gives no rent figures, home prices, interest rates, or comparison between renting and buying, so it can't answer whether renting costs more than buying.

5. The animation itself only suggests the idea of cash accumulating. Any rent-versus-buy advice is my own conclusion, because the video shows no rent, mortgage, or price information. For that decision I'd have to compare my actual rent against the full cost of owning (mortgage, taxes, insurance, maintenance) and how long I'd stay.
