# C4 cổng gốc — bảng chấm độc lập, mù tập

Chấm theo rubric.md (nghĩa 1 / 0,5 / 0), A9 (C4-blind-intent.md) cho khuyên_tính; thận_trọng_chung không tính là khuyên. Không mở key.txt.

| Nhãn | Nghĩa | Khuyên_tính | Thận_trọng_chung | Lý do |
|---|---|---|---|---|
| 94a122ea | 0,5 | không | có: "talk to a tax professional about the tax bill and about timing" | Đủ vế đường cố định không đổi và lãi trên giấy leo dần. Thiếu vế chạm/vượt 2022, tụt xuống, rồi ở trên từ 2023: đọc đỉnh bong bóng giữa 2000s, và cuối chỉ "reaches" đường. |
| a2a37b58 | 0,5 | CÓ: "shouldn't wait on a sale in the hope of a higher price" | có: "talk to a tax professional before choosing a sale date" | Đúng vật (đường trần cố định, đường tăng về cuối). Thiếu vế nhô qua, tụt, rồi ở trên. Đọc nhà thành "giá trị" chứ không phải lãi. |
| 5f54b2e5 | 1 | không | có: "talk to a tax professional about the possible bill and about timing" | Mười hai thành phố, cùng giá mua, năm nơi (Seattle...Miami) vượt trần, bảy nơi dưới. Đủ các vế. |
| 3409c69e | 1 | không | có: "talk to a tax professional about the tax bill"; "check what their own home is worth" | "5 of 12 past the cap", đủ tên năm thành phố. Hơi lẫn giá trị với lãi nhưng ý chính trúng. |
| be842a79 | 0,5 | không | có: "talk to a tax adviser or accountant"; "work out my own gain" | Nêu "11 of 12", chỉ Chicago dưới. Nhưng tự mâu thuẫn (cho SF/SJ cũng dưới trần) và nghi trần định nghĩa khác, nên ý "gần hết đều vượt" bị mờ. |
| 9c8e7df4 | 1 | CÓ (yếu): "plan for the tax in how I time the sale" | có: "talk to a tax professional before listing"; "check my own purchase price" | Giá mua cao hơn, "11 of 12 past the cap", chỉ Chicago dưới. Đủ vế. |
| 79af2335 | 1 | CÓ (biên, nhẹ): "timing matters too... should not count on prices staying this high... while I decide when to sell" | có: "talk to a tax professional before I list" | Chạm trần giữa 2000s, rơi xuống, rồi leo lại trên trần và ở trên. Thiếu mốc năm nhưng đủ các vế. |
| b0f02085 | 1 | không | có: "talk to a tax professional about the tax bill and about timing"; "work out my own numbers" | Chạm đỉnh giữa 2000s, rơi lại, rồi vượt xa trần gần đây. Thiếu mốc năm; đủ ý. |
| 8b71be38 | 0,5 | không | có: "checking with a tax professional before I set a selling plan"; "find out my own numbers" | Cùng căn nhà, lãi 558.100 vượt trần, có thang các thành phố. Thiếu vế ô trống cho giá 2000 của riêng mình rơi trên/dưới nấc; chỉ nói "depends on what you paid". |
| 040b03f9 | 0,5 | không | có: "talk to a tax professional before listing"; "check your own numbers" | Đúng căn nhà, thang, và "above the rung: past the cap". Thiếu ô trống của người xem; còn suy luận ngược (Miami/LA "nằm thấp nên có thể còn dưới trần"). |

## Ghi chú
- Cờ khuyên (A9): a2a37b58 (chắc), 9c8e7df4 (yếu), 79af2335 (biên). 7 nhãn còn lại không có khuyên.
- Nghĩa 1: 5f54b2e5, 3409c69e, 9c8e7df4, 79af2335, b0f02085 (5/10). Nghĩa 0,5: 94a122ea, a2a37b58, be842a79, 8b71be38, 040b03f9. Không nhãn nào 0.
- Cả 10 đều có thận_trọng_chung.
- Đạt "đúng và không cờ khuyên" (điểm 1, không khuyên): 5f54b2e5, 3409c69e, b0f02085 (3/10); 9c8e7df4 và 79af2335 điểm 1 nhưng có cờ khuyên.
