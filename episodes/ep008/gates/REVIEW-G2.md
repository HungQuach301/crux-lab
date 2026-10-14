# REVIEWER — gói G2 Tập 8 (lượt 1, 14/10; chi $0.72)

**Kết luận: KHÔNG ĐẠT ở dạng hiện tại.** Không cần đo lại gì. Chỉ cần sửa chữ trong `G2.md`, rồi gửi chủ dự án.

**CHẶN**
- **G2:34, Số đo chặng:** chi Console còn để trống "$X / $Y / $Z". Vì vậy không kiểm được ngắt P12 (M5 ≤ $8,3) và trần $25. **Sửa:** điền số thật từ sổ chi, ghi nguồn đối chiếu (±2 %).
- **G2:17, Checks:** bỏ sót CHẶN **S03**, phần đối chiếu vẫn trượt (`M5-checks.md:12`, kết luận dòng 36). G2 chỉ ghi "ĐẠT 46", giấu TRƯỢT 37, MISSING 13, ERROR 9. **Sửa:** thêm S03 vào danh sách CHẶN và ghi đủ 4 số của lần 2.
- **G2:17, A14/L1:** G2 viết "đã sửa môi trường, chạy lại", nhưng `M5-checks.md` không có kết quả lần chạy lại. A14 là CHẶN. **Sửa:** ghi "chưa chạy lại, chưa có kết quả", hoặc dán kết quả nếu đã chạy.

**CHÍNH**
- **G2:13, chỗ muốn tua:** thước ghi trước (C5) là "trượt thì sửa ≤ 2 vòng ở nhịp/hình, không đổi lời". G2 lại viết "lý do toàn ở lời → không mở vòng hình", rồi chuyển sang đề xuất cắt lời. Câu này sai với nguồn: S07 là lỗi hình (`M5-director.md:10`, thẻ không đọc được), S04 bị chê là "static". **Sửa:** nói thẳng đây là lệch ý đồ ghi trước, chưa chạy vòng hình nào. Cắt lời là quyết định của chủ dự án, không phải phép sửa của Editor.
- **G2:21, khuyến nghị (i):** chỉ cắt S06.2 và S31 thì S04, S07, S20–S22 vẫn ≥ 2/3, nên phép thử vẫn trượt. Đề xuất cắt ở G2:13 cũng bỏ quên S20. **Sửa:** ghi rõ sau khi cắt còn mấy cảnh dự kiến ≥ 2/3, và thêm S20.
- **G2:16, sửa hình (b) cold open:** đề xuất này chỉ dựa vào B02/B03 lật ở cổng gốc, mà cổng gốc chỉ là chẩn đoán (lệnh 14/10: không mở vòng vì nó). Chỗ S01–S03 không có phép thử nào của vai sở hữu trượt (§1a). **Sửa:** chuyển (b) thành "chỉ báo / câu hỏi", không đưa vào khuyến nghị.
- **G2:18, J/L-cut:** P13 yêu cầu nêu lệch "kèm số R09". G2 không có R09 (R09 TRƯỢT ở `M5-checks.md:33`). **Sửa:** thêm R09.
- **G2:12, cái giá của "thở":** chưa nêu V11 (1.135 va chạm chữ × hình), một phần do máy thở/tiến (`M5-checks.md:28`), và chưa nêu F-2 CHẶN ở lần dựng đầu vòng 2. **Sửa:** thêm hai ý này vào câu "Cái giá".
- **Cold open theo lệnh G1:** chưa có số đo trên nháp cho 3 mốc: 3 sự thật lật kỳ vọng trước 0:35, câu hỏi của Nina trước 0:40, nghịch lý trước 0:50. **Sửa:** thêm một dòng với 3 mốc giây.
- **Phiếu L3, dòng 1–2:** mức 4 cần *mọi* số máy đạt ngưỡng, nhưng thiếu các số mẫu đòi hỏi (năm luật nhân vật, "trả lời ≥ 3/5 câu hỏi khán giả", M6). "Kiểm mù C2 6/6" không có nguồn, lại đo trên kịch bản chứ không phải nháp. **Sửa:** ghi "thiếu" kèm nguồn, đổi mức gợi ý thành 3–4.
- **Phiếu L3, dòng 4:** R07 thực ra là ERROR, nên không biết R07 có ≥ 90 % không. Mức "3–4" đúng theo bảng, nhưng phải ghi "R07 ERROR" thay cho "R07 (M5-checks)". Cũng nên ghi rằng bảng quy đổi không dùng kết quả chỗ muốn tua.
- **Phiếu L3, dòng 5:** cần ghi rõ ASR S13 trượt và −1,9 dBTP vượt ngưỡng ≤ −2,0. A07 chưa có số. Mức 3–4 thì đúng.
- **G2:48, dòng trả lời gọn:** thiếu chỗ cho câu (5)–(8), trong đó có S09, là CHẶN. Chủ dự án không trả lời đủ được trong một lần. **Sửa:** thêm (5)–(8). Câu 2, 3 và 6 cần khuyến nghị cụ thể (với câu 6: chọn S04.1 hay S05.2).

**PHỤ**
- **G2:28:** câu 5 trùng mục cắt S06 → gộp vào.
- **G2:27:** thẻ cuối Short ghi "3 in 4", trong khi câu 1 đề xuất đổi lời thành "3 out of 4" → nêu là đổi đồng bộ cả hai.
- **G2:15:** `advice_stated` 0 là theo rubric mới. Rubric cũ báo 16 nhịp (`M5-root.md:5`) → ghi kèm.
- **G2:14:** nhớ lại chưa hiệu chuẩn (§1a) → ghi "chỉ báo".
- **G2:6:** "trên: animatic xám M2" không nói bản r1 hay r2. B03 và B07 đạt ở r1 → ghi rõ phiên bản trong mỗi ảnh.
- **G2:4 / G2:19:** độ dài 10:26,1 và 626,2 s lệch nhau → thống nhất một số.
- **G2:19:** "qc đối trọng 0 khung log = loại cũ" là lời giải thích chưa có bằng chứng → dẫn khung hoặc log.

**Những phần giữ đúng lệnh:** footage chỉ có bản đồ Natural Earth (5,98 s, có nhãn nguồn). 1 Short kèm thẻ đối trọng. Không thumbnail. Ngoài 3 khung tĩnh thì chưa dựng 1080p. Màu theo hồi đạt. Cổng gốc được ghi là chẩn đoán, có ảnh trước/sau. L3 là thước cuối. Freezedetect giữ ngưỡng n = 0,003, không đổi thước sau khi thấy kết quả. Mức gợi ý dòng 3 (71 % → 3) đúng bảng quy đổi.
