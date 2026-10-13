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

### R1 — object N3 Nina + đèn riêng
1. It shows a simple 3D scene labeled "Nina · ILLUSTRATIVE". A small figure, presumably Nina, stands between two buildings. The apartment block on the left has a sign reading "RENT". The house on the right has a sign reading "BUY". A small glowing yellow orb floats near the figure's head.

2. Very little changes. The orb moves around the figure's head. In frame 1 it sits above the head. In frame 2 it is upper left. In frame 3 it is farther left and apart from the figure. In frames 4 and 5 it is to the right. In frame 6 it is back above the head. The camera appears to shift slightly, since the buildings move a little in the frame. The figure stays in place and never moves toward either building. The orb seems to stand for a thought, or for the figure weighing a decision.

3. It looks like a visual metaphor for being undecided between renting and buying. The orb moving between the two sides suggests Nina is deliberating. The scene shows no numbers, prices, or outcome. The "ILLUSTRATIVE" label says it is a stylized depiction, not data.

4. A viewer could take away only that the rent-or-buy decision is a real dilemma and takes thought. The animation gives no guidance on which option is cheaper. It shows no costs, no timeline, and no result. Nothing in it suggests renting or buying is better.

5. The animation suggests only the idea of weighing the two options. Any advice beyond that would be my own conclusion. For the question you actually care about, you would need a rent-versus-buy calculation. It would use your local prices, mortgage rate, down payment, property taxes, maintenance, how long you'd stay, and what you'd earn by investing the difference.

### R2 — object N3 Nina + đèn riêng
1. It shows a simple 3D scene at night. A small figure labeled "Nina · ILLUSTRATIVE" stands between two buildings. The apartment block on the left has a "RENT" sign. The house with a red roof on the right has a "BUY" sign. A small glowing orb floats near the figure's head.

2. The orb moves around the figure's head. It starts above the head in frame 1. It moves up-left in frame 2, then out to the left in frame 3. In frames 4 and 5 it drifts to the right. In frame 6 it is back above the head. The figure and both buildings barely move. The camera or lighting may shift slightly. The figure never walks toward either building.

3. The orb looks like a thought bubble or a flicker of attention. The figure is weighing renting against buying. The orb moves around but doesn't settle on either side, which suggests indecision. The "ILLUSTRATIVE" tag says Nina is a made-up example and not real data. The animation gives no numbers, such as rent, mortgage, price or timeline, so it can't show which option costs less.

4. A viewer wouldn't get a concrete recommendation. The most they could take away is that this is a common dilemma, and that you should think it through before deciding. The animation doesn't say that either option is better. To answer my own question about whether renting costs more than buying, I'd need real numbers. Those would include local rent and home prices, mortgage rates, property taxes, insurance, maintenance, how long I plan to stay, and what I'd earn by investing the down payment.

5. The animation only suggests that there is a choice and that it hasn't been made. The advice to compare actual costs is my own conclusion. The video doesn't say it. I'm also guessing that the orb stands for a thought. Nothing in the frames confirms that, and there is no text or sound to back it up.
