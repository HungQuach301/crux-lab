# REVIEW — C2 v3, Tập 6 (sau G1 b) · 2026-10-08 · REVIEWER độc lập

Phạm vi: `git diff e7e15e1 HEAD` (script, beats, numbers, model.py); checklist quality-framework §7 mục 1–5, 8.
**Kết luận: kịch bản ĐẠT có sửa** (0 CHẶN · 3 CHÍNH · 4 PHỤ). **Cổng kiểm mù C2 vòng 3: chưa ĐẠT** (khuyên 5/6, người chấm ghi trước) — kết luận "nêu chủ dự án ở C3, không mở WRITER" đúng khung, nhưng gói C3 phải trình bày theo CHÍNH-2.

## Kiểm số và claim (mục 2)
- Tự tính từ `data/raw/CPIAUCNS.csv` (không đọc model.py), Carl 1966-01, k=0..20: 100,0 · 98,6 · 97,0 · 94,8 · 91,1 · 88,2 · 87,1 · 85,7 · 80,0 · 72,9 · 69,7 · 67,6 · 64,5 · 60,2 · 53,9 · 49,2 · 46,3 · 45,5 · 44,6 · 43,9 · **43,1** → giảm **20/20** kỷ niệm ✓ = `worst_window_years_2pct_fell_20y`; hàng thùng cuối round(4,31) = 4 ✓.
- Edna 1949-01 → 1969-01: cuối **100,2 %** → "ended full / all 10 lit" đúng luật (≥ 100 = `kept_up_last_start_20y`) ✓. Carl bắt đầu 1966-01 → bà kết thúc **3 năm** vào quãng của ông → "a few years into Carl's" ✓. Ruth: dưới 100 ở k=2 (96,8) rồi lên lại k=3 (100,3) → S24.6 ✓; Ruth cuối 90,4 → "about 9" ✓; S16.3 "most of its 10" ↔ 80,7 ✓.
- Câu thêm/sửa (S06.2, S16.3, S24.4–6, S27.4–5, S28.2, S29.2–3): có claim, không khuyên, không dự báo, không "we", Carl/Edna ILLUSTRATIVE (S24.2, S27.1, nhãn B24/B27/B29), không so tiền giữa hai khoản (mọi so sánh là khoản tăng 2 % so với đầu của chính nó). Số mới: đúng **1** (≤ 1 theo G1).
- `check_script.py`: **ĐẠT** không cờ (1.279 từ, ước 8:27; cảnh báo khuôn thí nghiệm −8,2, tham khảo). `numbers_said.py`: **0 BLOCK**; S24 mới 1 số (6,38), S27/S29 mới 0 → mọi cảnh ≤ 2 số mới ✓.

## Checklist §7
| # | Kết quả |
|---|---|
| 1 Khung | Ý đồ vòng 3 commit trước (1f2f294) ✓; ngưỡng không đổi ✓. **Lệch:** khoá nhãn r3/r23 commit cùng lúc với điểm (659c0f6) — §5.4 đòi commit trước khi chấm; r23 (chấm lại) không có trong ý đồ (CHÍNH-2). |
| 2 Claim-risk | ĐẠT (mục trên); S27.5 dễ nghe sai nhân quả (CHÍNH-1). |
| 3 Goodhart | Không thủ thuật; dư 4 từ ≈ 1,6 s trên đích 505 s đã nêu tên ✓. **Thiếu nêu tên:** Edna 100,2 % cách ngưỡng 100 % 0,2 % (PHỤ-5). |
| 4 Tự quyết §6 | S06.2, S28.2 sửa giữ nghĩa qua BLOCK (§6.5) ✓, phải liệt kê trong gói C3. Thêm nhịp = lệnh G1 ✓. |
| 5 Không lệch | numbers.md ↔ beats ↔ script ↔ ledger dòng 18–20 khớp ✓. |
| 8a–e Nhân vật | Ruth mở S01.1, qua phương pháp (S13.2–13.3), kết S32.2–32.3 câu của bà ✓; M6 = 0 ✓; vật cụ thể = hàng 10 thùng có claim ✓; đỉnh S10.2 **14 từ**, một ý ✓; kết quay về câu hỏi Ruth, không khái quát ✓. Nhịp mới giữ Ruth làm mốc so (S24.6, S29.2). |

**Chất hay độn (mục 3):** S24.4–6 mang ý mới (Carl tụt *mọi* năm, không lần nào lên lại — đối lập với Ruth); S27.4–5 ý mới (hai quãng chồng thời gian: cùng giá, khác chỗ đứng); S29.2 là phần trả của ký hiệu thùng cho cả ba (Carl "about 4" lần đầu nói bằng thùng). S16.3 yếu nhất (nói lại S16.2 bằng thùng, "most" thay vì số để giữ S16 ≤ 2 số mới) — chấp nhận. Không khối số dày nào quay lại. Kiểm mù: 0/6 nêu nhịp mới là chỗ mất chú ý.

## Phát hiện
| # | Cấp | Chỗ | Lỗi | Sửa đề xuất (nguyên văn) |
|---|---|---|---|---|
| 1 | CHÍNH | `script.md` S27.5; B27 | "The same few years of prices that ended her stretch with all 10 crates lit began his" nghe như chính những năm giá đó giữ đủ thùng cho Edna. Thực tế 1966→1969 kéo bà từ **105,7 % xuống 100,2 %**: bà còn đủ thùng nhờ phần đệm từ trước, không nhờ mấy năm này. Câu đúng về thời gian nhưng dễ hiểu sai nhân quả. Nhãn B27 "same years of prices: her last, his first" đã đúng. | S27.5 → *"The same few years of prices came at the end of her stretch, with all 10 crates still lit, and at the start of his."* (claims giữ nguyên; 0 số mới). Liệt kê trong gói C3. |
| 2 | CHÍNH | `C2-blind.md` Vòng 3; gói C3 | (a) Khoá nhãn `c2/r3/label-key.json`, `c2/r23/label-key.json` commit cùng commit với điểm (659c0f6), trái §5.4. (b) r23 là lần chấm thêm **không ghi trong ý đồ**, chạy sau khi thấy 5/6: chỉ được dùng làm chẩn đoán; số chính thức là **5/6 khuyên**. Gọi "nhiễu chấm" là chẩn đoán, không phải căn cứ. (c) Dự phòng C2 (§4) là "giữ bản điểm cao nhất": về câu khuyên, v2 (0/6 ở vòng 2) hơn v3 (5/6), nhưng v2 trái lệnh độ dài G1. Gói phải nêu rõ mâu thuẫn này. | Gói C3, câu hỏi cho chủ dự án: *"C2 vòng 3 chưa ĐẠT: câu khuyên 5/6 theo người chấm ghi trước (lần chấm thêm, không ghi trước: 1/6; v2 cũng 1/6). Kiểu khuyên 'hỏi công ty bảo hiểm khoản tăng khởi đầu nhỏ hơn bao nhiêu' đã có ở v2. Phương án: (i) giữ v3, ghi rủi ro; (ii) sửa S04.2 (CHÍNH-3) rồi kiểm mù lại hồi 1; (iii) chờ phiên K quyết rubric 'hỏi báo giá' (A9/A21). Khuyến nghị: (ii) + (iii)."* Ghi vào ledger: khoá nhãn r3/r23 commit cùng lúc với điểm (lỗi quy trình). |
| 3 | CHÍNH | `script.md` S04.2 | 4/5 câu khuyên dẫn đúng câu này: "depends on the insurer" + "this video doesn't model it" ⇒ "ask the insurer". Sửa giữ nghĩa được nhưng không thuộc §6.5 (không phải luật CHẶN) → chỉ đưa vào gói C3 làm phương án, không tự sửa. | S04.2 → *"How much smaller the rising check starts varies from one annuity to another, and this video doesn't model it."* Rủi ro: mất ý "giá do công ty định"; người xem vẫn có thể tự suy ra "đi hỏi báo giá" (S04.3, S31.3 vẫn nói về khoảng trống tiền); phải kiểm mù lại; c65d3523 ("inflation-linked option") lại bám S30.1–30.5, câu sửa này không chạm tới. |
| 4 | PHỤ | `beats.md` B24 | Hàng thùng làm tròn nguyên cho kết quả 10, 10, 10, 9… (k=1,2 vẫn 10) → nếu dựng bằng thùng nguyên, hình mâu thuẫn S24.5 "every one". | Thêm vào mô tả B24: *"each crate dims by the exact buying power at every tick (fractional brightness); whole-crate rounding only for the year-20 label."* |
| 5 | PHỤ | gói C3; B27 | Edna cuối 100,2 % (cách ngưỡng 0,2 %) chưa được nêu tên theo §7.3. Đường của bà lên tới 105,7 % (1966): hàng thùng không được hiện 11. | Gói C3: *"±5 %: Edna 100,2 % ở năm 20 (ngưỡng 100 %)."* B27: *"crate row capped at 10 lit; no crate above 10."* |
| 6 | PHỤ | `script.md` S16.3 | "lit" lần đầu được nói ở đây, chỉ dựa vào hình B07 (S07.2 không nói "lit"). | Tuỳ chọn: S07.2 giữ nguyên; S16.3 → *"In crates, the typical rising check still bought most of its first 10."* Hoặc giữ "lit" nếu hình B07 hiện rõ thùng sáng. |
| 7 | PHỤ | `C2-intent.md` Vòng 3 | Ý đồ ghi "dừng sớm: câu khuyên đầu tiên", nhưng chạy đủ 6 người đọc. Không đổi kết quả. | Ghi một dòng vào C2-blind: *"chạy song song 6 người đọc; luật dừng sớm không áp được (ghi lệch)."* |
