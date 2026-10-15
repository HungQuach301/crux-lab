# REVIEW G1 — Tập 8 (REVIEWER headless Opus, khoá Console, 13/10; chỉ đọc)

**SOÁT G1 Tập 8, REVIEWER** (chỉ đọc; `check_script.py --cast Nina` chạy lại: ĐẠT, 9:49, M1–M6 ĐẠT)

| # | Mục | KQ | Bằng chứng |
|---|---|---|---|
| 1 | Khung, ngưỡng, ý đồ | ĐẠT* | Rubric N3 không bị sửa sau kết quả (`PRE-objects.md`, N3 v2 = 0,5·0,5). *Rubric bổ sung N4/N5 lại nằm cùng commit với kết quả (`60a3d1b`), nên không chứng minh được là ghi trước. `C2-blind.md` v1 ghi ngưỡng "≥ 4/6", trong khi ý đồ ghi "≥ 2/6". |
| 2 | Claim-risk | TRƯỢT | G1 §1 ghi "< 2,42 %", nhưng cột Hiển thị là "below about 2.4%". Short S17.1→S19.3 chỉ có ca xấu nhất ($82,385 behind), thiếu "about 3 in 4" và hai thời kỳ. Mọi số khác trong G1 và lời khớp cột Hiển thị. Không có câu khuyên hay dự báo (S03.3, S30.3). |
| 3 | Chống Goodhart | TRƯỢT | C2 v2: loại "khác" 2/6 chạm đúng ngưỡng "≥ 2/6" của `C2-intent.md`. G1 vẫn ghi "không loại khối ≥ 2/6 — ĐẠT", lý do "hai chỗ khác nhau" được diễn giải sau khi có kết quả và không được nêu tên. Các mục ±5 % đã nêu tên: concept +7,5, limits −6,4, H-B M2 28,6 s. |
| 4 | Tự quyết §6 | TRƯỢT | Đổi bố cục N1 từ một dãy sang lưới năm×tháng là việc "hướng hình", nằm ngoài §6, mà G1 không hỏi. Sửa regex `check_script.py` không có trong G1. `ledger.md` không có dòng nào cho đổi tên Maya→Nina, S01.3/S04.4, N1 hay regex. |
| 5 | Không lệch | TRƯỢT | `ledger.md` thiếu mọi lượt C1, PRE, C2 và table-read. `continuity.md`/`beats.md` vẫn ở v1 (10:29, 1.510 từ, "Claims wanted", ý thumbnail). Script còn trỏ S26.2/S27 dù không tồn tại, ghi MR2 "190 s" trong khi checker ra 149 s, và HA.3 lệch S01.3. Khuyến nghị bỏ N5, nhưng S08.4, S29.1, B02, B29, B32 vẫn dựa vào sương. |
| 6 | Chất lượng trước | TRƯỢT | G1 dòng 40 ghi "Console P1 ≈ $X" (số giữ chỗ) và "token: PLAN §5" thay cho số thực. |
| 7 | Hình–âm | ĐẠT (chưa áp) | Chưa có đoạn dựng. Lượt đạo diễn chưa dùng làm ngưỡng. |
| 8 | Kịch bản | ĐẠT | Nina xuất hiện ở S01.1 (0:00) và đi qua phương pháp ở S04.3, S08.4. M6 = 0. Câu đỉnh S17.2 có 10 từ. Câu kết S32.3 là của Nina và quay về câu hỏi S01.2. |
| 9 | `fix:` mỗi vòng | ĐẠT | `PRE-objects.md` ghi `fix: picture` ở mỗi vòng. Nhãn N4 "cash, not stocks" chỉ được đề xuất sau 2 vòng sửa bằng hình (E6). |
| 10 | Hồ sơ cầu | ĐẠT | Q1 ở S04/S13; Q2 ở S09–S28; Q3 trả lời một phần ở S04/S05.6. Logline trả lời Q1. S06 xử lý điểm yếu đối thủ, không nêu tên kênh. Có dòng "Thị trường" với 3 video vượt trội ghi "tự tính". |
| LT | Luật tạm 13/10 | ĐẠT có sửa | Đủ: vision; continuity đủ cột; clip 540p 6–7 s; 2 người đọc; hai vật trượt có trước/sau; đèn riêng N3; số neo là vật thật (đèn, chồng W2, thẻ); `c2/advice-words.json`; hotword Nina/Marcus/Priya; footage 25 s ≈ 4 %; RIGHTS có dòng M-NE-ADM1; 3 khung thử; 1 Short, không thumbnail; gói 3 câu. Còn thiếu: `vision.md` vẫn tả "đường thẳng" và sương; N3, N4 vẫn trượt sau 2 vòng. |

**Việc cần sửa (WRITER/điều phối, không đổi nội dung đã duyệt):**
1. G1 §1: đổi "< 2,42 %" thành "dưới khoảng 2,4 %" cho đúng cột Hiển thị.
2. Short: thêm đối trọng, gồm S13.2 "about 3 in 4" cùng 1990s/2009–2016, hoặc một thẻ cuối. Nếu không, đổi Short sang S24–S25.
3. G1 §2: nêu đúng là "loại khác 2/6, chạm ngưỡng ≥ 2/6", kèm trích hai chỗ người đọc mất chú ý, và để chủ dự án quyết. Không ghi "ĐẠT" thẳng.
4. G1 §3: ghi rõ rubric N4/N5 nằm cùng commit với kết quả, không chứng minh được là ghi trước.
5. Bỏ N5 thì phải sửa kéo theo S08.4, S29.1, B02, B29, B32 (lời nhắc "fog"), liệt kê theo §6.5. Nếu không sửa, G1 phải nói khuyến nghị bỏ N5 kéo theo đổi lời.
6. Đưa bố cục lưới N1 vào G1 như một việc gu, gộp vào câu 3, và cập nhật `vision.md` cùng `beats.md`.
7. Thêm vào `ledger.md`: các lượt kiểm mù C1, PRE, C2, table-read EL, kèm chi phí $; các việc tự quyết (đổi tên, S01.3/S04.4, regex checker, bố cục N1), mỗi việc một dòng lý do.
8. Thay "$X" và "PLAN §5" bằng số Console và token thực.
9. Làm mới `continuity.md` (9:49, 589 s, footage ≈ 4,2 %, bỏ N5) và `beats.md`/`script.md` (bỏ S26.2/S27, đổi "190 s" thành 149 s, bỏ "Claims wanted" và ý thumbnail).
10. Ghi chú thêm: T3 "1991–2016" là khoảng tháng bắt đầu, không phải khoảng dữ liệu. Nên ghi "start months 1991–2016" hoặc khuyến nghị T1.

**Kết luận: ĐẠT có sửa.** Mục 2, 3, 4, 5, 6 trượt nhưng sửa được bằng chữ hoặc sổ sách, không cần chạy lại kiểm mù. Gửi gói sau khi sửa xong việc 1–8.
