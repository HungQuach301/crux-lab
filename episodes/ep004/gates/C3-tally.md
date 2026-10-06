# C3 — gộp điểm kiểm mù cổng gốc (ý đồ `gates/C3-intent.md`)

Nguyên văn trả lời: `review-c3/r1/answers.md` (khoá nhãn `review-c3/r1/key.txt`). Người chấm độc lập (sonnet, mù tập, chỉ đọc file trả lời + rubric).

## Vòng 1 (2026-10-06) — dải `review-c3/B08|B13|B14.png`
| Nhịp | Người đọc | Nghĩa | Khuyên | Đúng | Kết quả |
|---|---|---|---|---|---|
| B08 · KEY-3 (N1) | 2acce75c2b37 | 1 | có ("work out the expected gain… talking to a tax professional") | không | |
| | 8ed68e059820 | 1 | có ("talk to a tax professional before I list") | không | **TRƯỢT (0/2, vì khuyên; nghĩa 2/2)** |
| B13 (N2) | 6dc43a82b79a | 1 | có ("check the real rules and talk to a tax professional") | không | |
| | 342b27522f22 | 0 (đảo chiều: giá cao hơn → dưới trần) | có | không | **TRƯỢT (0/2; nghĩa 1/2)** |
| B14 · KEY-6 (N2) | 1cd7cb391a45 | 0,5 (đọc số là giá trị cuối, không phải ngưỡng) | có | không | |
| | 3be8dc5b473e | 0,5 (như trên) | có | không | **TRƯỢT (0/2; nghĩa 0/2)** |

Đọc số thành tiền thuế: 0/6. Dừng sớm: cả ba nhịp 0/2 → không gọi người thứ 3.
**Ghi nhận:** câu khuyên 6/6 cùng một dạng ("tính lãi của mình / hỏi chuyên gia thuế trước khi bán"), giống C1 (5/6). N1 mang đúng nghĩa 2/2 — chỉ trượt vì cờ khuyên.

## Vòng 2 (2026-10-06) — chỉ thêm nhãn (`944c790`), dải `review-c3/r2/`, 6 người đọc MỚI
Nhãn thêm: đối trọng "A measurement, not a tax bill or a next step" (cả 3 nhịp); B13 "Paid more in 2000 → bigger gain → over the cap"; B14 "Each rung: the 2000 price where the gain hits the cap" + "Every city but Chicago is under $300,000". Không thêm vật, màu, số ngoài claim. qc 12/12, 0 CHẶN; 0 ký tự EL.

| Nhịp | Người đọc | Nghĩa | Khuyên | Kết quả |
|---|---|---|---|---|
| B08 · KEY-3 (N1) | c45643792e96 · fc2ad9b0ff38 | 1 · 1 | có · có ("work out my own gain… ask a tax professional") | **nghĩa 2/2; TRƯỢT vì khuyên** |
| B13 (N2) | a87b383cd686 · 32fecb3e5b18 | 1 · 1 | có · có | **nghĩa 2/2; TRƯỢT vì khuyên** |
| B14 · KEY-6 (N2) | 60342a183008 · cef781aa5171 | 1 · 1 | có · có | **nghĩa 2/2; TRƯỢT vì khuyên** |

Đọc số thành tiền thuế: 0/6. (Một người đọc vòng 2 gõ sai đường dẫn, không thấy ảnh → thay bằng người đọc mới cef781aa5171.)

## Kết luận theo ý đồ
- **Nghĩa:** nhãn nghĩa vòng 2 sửa được cả hai nhịp N2 (B13 1/2 → 2/2; B14 0/2 → 2/2); N1 2/2 cả hai vòng. Tổng nghĩa vòng 2: **6/6**.
- **Câu khuyên: 12/12 qua hai vòng**, cùng một dạng: "tính lãi của mình / hỏi chuyên gia thuế trước khi bán". Nhãn đối trọng không làm giảm (6/6 → 6/6); nhiều người đọc trích chính nhãn đó rồi vẫn khuyên.
- Theo luật (§5.8): câu khuyên ở bất kỳ nhịp nào → nhịp trượt; hạ loại 2 không cứu được (loại 2 vẫn tính câu khuyên). **Cổng gốc C3 TRƯỢT vì câu khuyên; chủ dự án quyết** (ý đồ, mục "Vòng và dự phòng").
- Nhận định (không phải số đo): câu khuyên đến từ vai + câu hỏi 4 trên đề tài thuế, không từ hình — cùng dạng ở C1 (5/6, chỉ đọc logline, không có hình). Bộ đo hiện không tách được hai nguồn này vì không có đối chứng.
