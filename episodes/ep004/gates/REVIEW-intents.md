# REVIEWER — soát hai ý đồ kiểm mù TRƯỚC khi chạy (quality-framework §5.1) · 2026-10-05

## 1. `cal-hook/INTENT.md` (hiệu chuẩn so cặp móc): TRƯỢT, sửa xong thì chạy

Phần đạt: mẫu mới (Tập 1 và tax-4 không thuộc Mốc B, cũng không phải đề tài Tập 4). Thứ tự cân bằng: `key.json` có A 2X/2Y, B 2X/2Y. Độ dài lệch nhau dưới 15 % (66/62, 67/64 từ). Ngưỡng ≥ 7/8 chặt hơn ví dụ ≥ 5/6 ở `episode.md` §3, p ≈ 3,5 % tính đúng. Ý đồ đã ghi trước hệ quả khi ĐẠT và khi TRƯỢT. Ý đồ cấm chạy thêm người đọc để cứu. Không thấy thủ thuật Goodhart ở ngưỡng.

Dòng TRƯỢT:
1. **Mô tả Mốc B sai.** Đối chiếu `moc-b/cal-engagement/key.json` với `answers.jsonl`: gốc ở X trong 5/6 cặp (đúng), nhưng chỉ **5/6 người chọn X**, không phải "cả 6". Người duy nhất thấy gốc ở Y (`ac007b59`) đã chọn **Y**, tức chọn bản gốc. → Sửa thành: "6/6 chọn gốc; chỉ 1 cặp có gốc ở Y (người đó chọn Y), nên với n = 1 chưa tách được thiên lệch vị trí." Kết luận "cần cân bằng" vẫn đúng.
2. **"Cùng dữ kiện" chưa đúng ở cả hai mẫu.** A-degr thiếu 5,98 %, $459 và "She didn't take it", lại có thêm 7,79 % và "3 in 10". B-degr có thêm $12.500, 2028 và payroll tax, nhưng thiếu ~$1.400. B-degr cũng là đoạn viết tự do, không cắt từ cùng một kịch bản như F4 và §2.8 đòi. → Sửa chữ trong INTENT thành "cùng kịch bản; móc (được–mất, câu hỏi, lời hứa) dời ra sau 30 s; mở bằng bối cảnh của chính kịch bản (Op1 Mốc B, `DEGRADE-NOTES.md`)". Với B: ghi vào `samples.md` một kịch bản B liền mạch khoảng 130 từ, gồm cả câu móc lẫn câu luật. B-orig và B-degr phải là hai cách xếp câu của chính kịch bản đó.
3. **A-degr có câu làm hỏng đối chứng.** S04.1 ("Nora isn't a real person…") là câu nói về cách làm, dễ khiến người đọc mất hứng. Bản làm kém như vậy kém vì câu này, không phải vì thiếu móc, nên thành bù nhìn. → Thay S04.1 bằng S04.2 (câu thật của tập; ước khoảng 64 từ, phải đếm lại). Đổi xong thì chạy lại `deal.py` để sinh lại khoá.
4. **A-orig chưa phải "móc theo story §1".** 5 s đầu là số thị trường, được–mất tới ở khoảng 0:17, và trước 0:30 không có lời hứa (câu hỏi tới ở 0:46). → Sửa phần Câu hỏi: A kiểm "móc được–mất không có lời hứa (bản đã phát hành)", B kiểm "móc đủ story §1". Thêm vào Giới hạn: A yếu hơn các móc Tập 4.
5. **Câu tiêu đề gộp vào: hiệu chuẩn gần như không hỏng, nhưng phép so tiêu đề thì hỏng.** Người đọc mang vai A (trả góp, 30–55 tuổi) và vai B (làm theo giờ, 25–50 tuổi), không phải khán giả đích Tập 4 (50–60+ tuổi, mua nhà khoảng năm 2000). Theo §5.3, kết quả CLICK vì thế không dùng được, kể cả làm tham khảo. Thêm nữa, cặp T1 xuất hiện 6 lần thì 4 lần đứng trước, nên thứ tự chưa cân bằng. → Bỏ câu tiêu đề khỏi `deal.py`. Nếu vẫn muốn giữ, ghi trong INTENT và gói G1 rằng "vai sai, không dùng để chọn". Tiêu đề so riêng với vai đích Tập 4.

Ghi chú, không chặn:
- Ngưỡng 2 và 3 thừa: ≥ 7/8 đã kéo theo mọi nhóm 4 người ≥ 3/4. Vì vậy câu "ngưỡng riêng cho vị trí" thực ra chỉ có tác dụng nhờ cân bằng thứ tự. Nên nói thẳng điều này trong INTENT.
- B-orig: "part of overtime pay comes off your federal income tax" chưa chính xác, vì đây là khoản trừ vào thu nhập chịu thuế. Nên sửa thành "is deductible from federal income tax". "Eight extra hours" nên thêm "a week".

## 2. `gates/C1-intent.md` + `C1-logline.md` (kiểm mù kể lại logline): TRƯỢT nhẹ, sửa nhanh

Phần đạt: số người đọc là 5 vai đích + 1 phổ thông, không dừng sớm; có người chấm độc lập; khoá nhãn commit trước; có câu hỏi về lời khuyên; ngưỡng ≥ 4/5 vai đích; tối đa 2 vòng, có nhánh dự phòng. Ý đồ bỏ đối chứng và có lý do (F4). Claim khớp `numbers.md`: $500.000, có hiệu lực từ 05/1997, khoảng thời gian 2000 → 2026 Q2 (~26 năm), 12 metro. "More than tripled in many cities" khớp với hệ số tăng > 3 ở 9/12 metro. Logline không khuyên, không dự báo, không đổi ngưỡng thành hoá đơn thuế.

Dòng TRƯỢT:
1. **Cụm từ claim-risk bị đổi.** Hồ sơ claim-risk ghi "Always say *a home that rose like the metro average*", còn L1 viết "the local average". → Sửa thành "a home that rose like its metro area's average".
2. **§4 C1 yêu cầu 2 logline, ý đồ chỉ có L1.** → Thêm L2 vào cùng lượt chạy, người đọc mới cho L2 (thêm 6 agent). Nếu không làm, ghi trong ý đồ lý do chỉ có một logline (đề tài máy chọn, tiết kiệm agent) và nêu điều này trong gói G1.
3. **Rubric (d) chưa bắt lỗi nói quá claim.** Nếu người đọc kể lại "giá mua trên X thì bạn sẽ phải đóng thuế / video tính thuế của tôi", hiện vẫn được điểm. → Thêm vào (d) điều kiện "ngưỡng của căn nhà tăng như trung bình metro". Thêm cờ báo riêng "căn nhà cụ thể / hoá đơn thuế": không tính vào ngưỡng, nhưng nêu tên trong gói và dùng để sửa logline ở vòng 2.

## Soát lại chỗ sửa (bản 2): ĐẠT
- cal-hook bản 2 đúng với các dòng TRƯỢT. A-degr = S03.1 + S03.2 + S04.2 (66 từ). B là kịch bản 8 câu: gốc là b1–b5, làm kém là b5–b8, nên trong 30 s đầu bản làm kém không còn móc. Khoá mới cân bằng 2X/2Y mỗi mẫu. Prompt đã bỏ câu tiêu đề. Còn hai lỗi nhỏ: B-orig thực tế 68 từ (INTENT ghi 66), và `deal.py` còn sót biến `pairs`/`T` không dùng. Không chặn.
- C1 bản 2: đã đổi sang "metro area's average", đã thêm điều kiện vào (d) và cờ `overclaim`, đã ghi lý do chỉ có một logline. Đạt.

## 3. `gates/C2-intent.md` + `story/check_script.py`: TRƯỢT (phần máy), phần mù đạt

Phần đạt (b): 5 T + 1 G, đủ 6 người; câu hỏi cố định có câu lời khuyên; người chấm mù. Ngưỡng ≥ 5/6, câu khuyên 0/6, không cảnh nào bị ≥ 4/6 cùng chỉ là chỗ mất chú ý: khớp §4 C2. Dự phòng V7 cũng khớp. A1 khớp `numbers.md` (11/12 vùng dưới $300.000). Bỏ đối chứng có lý do (E12, F4).

Đã thử bộ kiểm trên một kịch bản giả. Dòng TRƯỢT:
1. **"Claim 100 %" chưa được kiểm.** Bộ kiểm chỉ xem claim ID có trong `numbers.md`, không so số nói ra với giá trị claim. Câu thử "the line is $999,999" gắn `threshold_joint_los_angeles` vẫn qua. → Thêm bước CHẶN: số chữ số trong lời phải khớp giá trị claim của câu (sau khi làm tròn theo một dạng cố định cho mỗi tỉ lệ, E5). Số đọc bằng chữ thì phải có ghi chú quy đổi.
2. **Móc 5 s gần như không chặn được gì.** `first5` coi bất kỳ claim nào là "được–mất", và chỉ xét lúc câu bắt đầu, nên câu đầu luôn ở t = 0. Câu thử "In 2000, home prices were lower." (mở bằng lịch sử, trái §1.1) vẫn qua. → Bắt WRITER đánh dấu `[stake]` hoặc `[question]` ở cột ghi chú câu móc; bộ kiểm đòi dấu đó ở câu bắt đầu trước 5 s. Ghi rõ đây là điều kiện cần, REVIEWER vẫn chấm được–mất theo §1.
3. **Thiếu `hooks.md` thì bỏ qua lặng lẽ** mà vẫn có thể ĐẠT. Ý đồ đòi kiểm cả 3 phương án. → CHẶN khi thiếu file hoặc khi số phương án khác 3.
4. **Câu ngưỡng thiếu "like/average" mới chỉ là CẢNH BÁO**, trong khi claim-risk ghi "Always say". Đây là lỗi sai claim, mà theo D-006 thì phải mở vòng sửa. Câu thử "…$999,999, for anyone" chỉ bị cảnh báo. → Nâng lên CHẶN. Mở rộng cho các câu nêu `gain_at_*`, `cross_/stay_quarter_*` và `metros_threshold_*`. Thêm vào ý đồ (a) cho khớp.
5. **"Câu có số phải có claim" báo sai.** NUMWORD bắt cả "one", "half", "quarter", "double", nên câu "each one of them" bị CHẶN. Báo sai kiểu này đẩy WRITER gắn claim cho có để qua cửa (Goodhart). → Bỏ "one" và "quarter" khỏi NUMWORD trừ khi đi kèm danh từ đơn vị (one in, one-third…), hoặc cho phép cột claim ghi `—text` kèm lý do.
6. **Story §1.3 chỉ được kiểm một nửa.** Bộ kiểm chỉ chặn ràng buộc nằm giữa câu hỏi và lời hứa. Nó không kiểm ràng buộc đặt trước móc, cũng không kiểm "US only / history" phải ở sau lời hứa và trước số lịch sử đầu tiên. → Thêm cả hai: cái đầu là CHẶN, cái sau là CẢNH BÁO.

Ghi chú, không chặn:
- Story §3 tính "> 2 số mới" theo **cảnh**, bộ kiểm lại tính theo câu. Nên gộp theo tiền tố Sxx.
- Bộ kiểm chưa xét viết tắt có gạch nối (§3.1, F7: "W-2", "T-bill"). Nên thêm một CẢNH BÁO.
- Các con số $200k/$300k phải gắn nhãn "ILLUSTRATIVE" trên hình. Nên thêm một CẢNH BÁO khi `gain_at_*` không có chữ "illustrat" trong ghi chú.
- Thời lượng mới là ước 140 từ/phút. Mốc 5 s và 0:30 cần đo lại trên giọng thật ở C3/C4 (§2.4).
- A2 chặt hơn §4, vốn chỉ đòi câu hỏi + đáp án. Ghi rõ là cố ý chặt hơn, hoặc hạ A2 thành cờ tham khảo. Trong A1, bỏ cụm "thấp hơn người ta nghĩ" (chủ quan) khỏi điều kiện đủ.
