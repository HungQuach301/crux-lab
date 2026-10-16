# REVIEWER gói G2 Tập 9 (16/10) — chi $0.88

**Kết luận: ĐẠT có sửa.** Không có mục CHẶN. Có 6 mục CHÍNH, cần sửa trong gói trước khi gửi chủ dự án.

**CHÍNH**
1. **G2 §1 dòng "Cổng gốc":** số không khớp. Animatic 18/27, cộng 3 nhịp lật lên (B12, B16, B25), trừ 1 nhịp lật xuống (B27) thì ra 20/27, không phải 19/27 như gói ghi. Sửa: đối chiếu lại bảng nháp rồi sửa tổng, hoặc kể đủ các nhịp lật; sửa luôn phiếu L3 dòng 3.
2. **Câu 6b:** đề xuất "US only; the rest of the limits are on the card." làm mất hai giới hạn đang được nói ở S24.1 là "no taxes on gains or on the home" và "renters who never skip a month". Cả hai đều có tên trong mục rủi ro claim của script, tức là gen được bảo vệ. Câu đề xuất còn dùng chữ "the rest" khi chỉ nói một giới hạn. Sửa: giữ hai vế đó, chỉ rút "history, not a forecast" vì S03.4 đã nói.
3. **Câu 6c:** "The replay assumes she never stopped; real people sometimes do." đổi nghĩa. Giả định áp cho mọi người thuê ("every renting twin"), câu mới thu về một cô ("she"). Câu này cũng bỏ mất vế "a renter who sells in a crash is not on this street". Sửa: "The replay assumes every renting twin kept investing; one who sells in a crash is not on this street."
4. **Chỗ muốn tua (§1 dòng 4 và dòng 16):** lệch ý đồ nhưng gói chưa gọi tên.
   - Dòng 4 nói nhớ lại đo trên nháp 540p r2, dòng 16 lại nói r2 đo trên 1080p. Hai dòng mâu thuẫn nhau.
   - M5-intent §3 định đo trên bản (a) và quy định "trượt → sửa nhịp/hình, không đổi lời". Đo r2 trên bản khác là đổi bộ đo giữa hai vòng; câu 6 đề xuất đổi lời là ra ngoài ý đồ.
   - Sửa: ghi rõ cả hai lệch và bản đo của từng vòng; câu 6 ghi "ngoài ý đồ M5 §3, đổi kịch bản đã duyệt (§1b' ngoại lệ phải hỏi)".
5. **V12 (§1 dòng "Lệch lệnh chặng"):** ý đồ §1 yêu cầu ghi V12 riêng cho từng đoạn có lớp (a1, b1, d1, f2). Cả gói lẫn M5-checks đều chưa có. Câu "phần lớn ở đoạn không lớp" hiện chỉ dựa vào 2 ví dụ. Sửa: đưa số mẫu V12 theo từng đoạn từ `report.json` vào gói; nếu không có số thì bỏ câu khẳng định đó.
6. **Thiếu kết quả ý đồ §4 và P9/P11:** gói chưa nêu
   - lặng trước 3 số neo (0,7–0,9 s) và vật đổi trong ±1 s;
   - A/V lệch ngoài vùng J/L;
   - "số trên hình = lời";
   - màu bảng điểm;
   - SFX: lặp trong 60 s, mật độ, `sfx_fetch --verify`;
   - câu nguồn S24 có khớp nguyên văn câu chủ dự án 15/10 không.
   Sửa: thêm một dòng ghi số đo cho từng mục, hoặc ghi "chưa đo".

**PHỤ**
7. **`cine` (§1 dòng "Lệch lệnh chặng"):** chưa nêu số gốc. Sửa: "lệnh 5 cảnh đinh (H1 H2 H3 H4 H6, 136,3 s = 26,0 %) → còn 3 cảnh đinh (H1 H2 H6, 87,5 s = 16,7 %); H3 và H4 tắt sau 2 vòng ΔE". Các số 22,7 + 32,4 + 32,4 = 87,5 s và 16,7 % đều khớp nguồn.
8. **Câu 1:** ý đồ C1 định tải bản (b) 1080p, gói lại khuyên tải bản 720p. Sửa: khuyên tải 1080p, hoặc ghi rõ bản 720p có cùng tiếng. Câu khuyến nghị ở §1 dòng 20 cũng cần thêm "sau khi có ô Content ID".
9. **Câu 3:** gói gọi S04.2 là "câu tiền đầu tiên", nhưng $92,000 đã xuất hiện ở S02.1 và S03.6. Sửa cách gọi; vị trí S04.2 giữ được nếu luật S09 chấp nhận.
10. **Câu 5 và 6a chồng nhau:** cùng sửa S18.4, chọn 6a thì câu 5 không còn tác dụng. Câu 6 rút ≈ 12–15 s, làm F07 xa mức 9:00 hơn. Sửa: ghi hai điểm này ngay trong câu 4 và câu 6.
11. **Câu 9 (Short SH1):** khoảng 264,1–298,5 s chứa S14.4–S14.5, nên nếu duyệt câu 6c thì mốc giây và lời của Short đổi theo. Sửa: thêm một vế "mốc giây đổi nếu chọn 6c".
12. **M5-checks dòng S23:** còn ghi phương án "allowTerms". Ý đồ §1 cấm thêm allowTerms sau khi thấy kết quả. Gói đã không dùng phương án này, nhưng nên xoá khỏi M5-checks.

**Những phần đã đúng**
- **Số khớp nguồn:**
  - checks 45/45/14/1, V03 206, V11 1.667, V12 543, C07 434, S07 14+6;
  - tua S03 3/3, S14, S18, S24 2/3, S25 1/3;
  - cổng gốc M2 18/27 (r1 11/27);
  - Console $6,51 + $0,75 + $0,37 = $7,63;
  - 8:44 = 523,9 s.
- **Luật vòng sửa và bộ đo:** quy tắc ≤ 2 vòng có nêu ở câu 8; điểm chính thức vẫn theo lượt chấm đầu (A32); không thêm allowTerms nào.
- **Các đề xuất đổi lời câu 2, 3, 5:** giữ nguyên nghĩa và claim, không có lời khuyên.
