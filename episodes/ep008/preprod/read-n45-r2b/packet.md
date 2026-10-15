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
1. It shows a figure labeled "Nina" standing between an apartment building with a "RENT" sign and a clear box labeled "CASH". Each frame carries an "ILLUSTRATIVE" tag. It's a simple 3D scene with no words explaining it.

2. In frame 1 the cash box is empty. After that, green bills drop in from above, apparently coming from the building's direction (frame 3 shows one at the building). The stack in the box grows from a thin layer in frame 2 to a nearly full, multi-layer pile by frame 6. The building, the figure and the small yellow dot beside the figure don't change.

3. The most natural reading is that Nina rents and keeps accumulating cash. Her money piles up over time instead of going into a purchase. Since the building says "RENT", the bills may be leftover money after rent, or money she would have spent on a mortgage or down payment. The animation doesn't say which. The "ILLUSTRATIVE" label means the numbers aren't real data.

4. A viewer might conclude that renting lets you save cash, which keeps you flexible and liquid. As a renter wondering about rent versus buying, I'd take it as "renting can leave you with savings." That only holds if you actually save the difference. It says nothing about home equity, appreciation, rent increases, or investment returns.

5. The animation only suggests the idea of saving while renting. It has no text, numbers or comparison scenario, such as a Nina who buys a home. The advice in 4 is my own conclusion. The animation doesn't show that renting is cheaper than buying, and it doesn't tell anyone what to do.
