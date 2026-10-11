**ĐẠT có sửa**: gói gửi được sau khi sửa 2 mục CHẶN và các mục CHÍNH dưới đây.

Các số đã khớp nguồn: P1, P2, P3, P3b và K khớp từng phiên với `t6.jsonl`. Các tổng cũng đúng: trần 83,06, sinh ra 2,84, đọc cache 825,9, agent 25, giờ máy 23,44 h, EL 7.699, khoảng $605 niêm yết, 5,8 triệu, −3 %, hằng 2,40/2,66 (−4,8 %/−3,3 %), độ dài 882/1020 s, thiếu ≈ 830 từ. Các số đo nhịp hình (freezedetect 206 s / 51 đoạn, R07 70,3 %, "3%" trễ 1,26 s) khớp G2. Repo không chứa số thô của kênh khác: `anchors/*.json` chỉ có nhãn, và `--save` chỉ ghi nhãn.

**CHẶN**
1. `playbook/packaging.md:113` (cùng logo "M." ở `toolkit/package/thumbs.py:3,60`, `PACKAGING-BRIEF.md:24`): bộ nhận diện kênh mang tên **"Money Rerouted"**. Đây là kênh đối thủ trực tiếp ở `market/CHANNELS.md:66`, và hồ sơ q01/q17 xếp nó vào nhóm "dữ liệu lịch sử thật". Kênh của mình là Crux, và `packaging.md:41` cấm dùng thương hiệu của bên khác. Sửa: đổi thành "Bộ nhận diện kênh Crux", bỏ logo "M." hoặc ghi "logo: chờ chủ dự án chọn". Ảnh `api-*.png` phải render lại trước khi đưa vào câu 3.
2. `REPORT.md:56`: ghi "cổng gốc 21/23", nhưng bản giao là **20/23 = 87 %** (`gates/G2.md:18`). 21/23 là số của C4 vòng 2–4, trước C5b. Sửa: "cổng gốc 20/23 = 87 % (C4 21/23)". Số này đang làm chứng cho "chất lượng không giảm", nên phải đúng.

**CHÍNH**
3. `REPORT.md:99` và `episode.md:196`: phép tính EL lệch. 2.120 × 5,9 × 1,1 = 13.760 và 2.450 × 5,9 × 1,1 = 15.900, tức ≈ **13.800–15.900**, không phải 13.000–15.000. Tháng 4 tập ≈ 64.000. Còn nếu 5,9 đã gồm phần sinh lại (Tập 6: 7.699 ÷ 1.288 = 5,98) thì bỏ "+10 %". Sửa một cách rồi chép đúng số đó vào §3, §5 câu 2 và §8.
4. `episode.md` §8, bảng mới (khoảng dòng 193–196): bảng ghi `101` EL ≈ 8.000, nhưng dòng 189 nói "hai trần này không đổi" và dòng 198 nói "trần 6.000 là cho `101`". Hai chỗ mâu thuẫn. Bảng cũng ghi $35/$45/$60 như luật đã áp, trong khi (g) còn CHỜ, và đây là chi tiêu. Sửa: thêm "*(chờ câu 1 g / câu 2)*" vào tiêu đề bảng, và ghi `101` EL "≤ 6.000 (trần); thực Tập 6 7.699 do duyệt C3".
5. `playbook/templates/check_script.py:373,380`: luật §9 yêu cầu `deep` có 2 mid-roll khi dưới 15:30 và 3 khi từ 15:30. Mã chỉ kiểm 2–3, nên tập 16:30 có 2 điểm vẫn ĐẠT. Mã cũng không cảnh báo khi tập `deep` thiếu ACT 4 (`TEMPLATE.get(p, share)` bỏ qua phần thiếu). Như vậy câu "`check_script.py` mẫu đã kiểm" ở `episode.md:221` và `REPORT.md:96` nói quá. Sửa:
   - thay dòng 380 bằng `need = 3 if EST >= 930 else 2` (với `deep`), rồi kiểm `len(mid) == need`;
   - thêm `if FORMAT == 'deep' and 'questions' not in span: fail.append('deep thiếu ACT 4')`.
6. `toolkit/package/thumbs.py:32` (PROMPT): mã vẫn giữ câu "Make them larger and closer to the camera". Đây chính là câu làm api-2 hỏng ở lần 1; bài học "giữ khoảng cách máy" chỉ nằm trong `--keep` của một ảnh. Sửa: thay bằng "Keep the same camera distance and framing; do not zoom in."
7. `REPORT.md:70` (và lessons T6-5): câu "ước 8:56 = thật 8:56,6" là khớp trong mẫu, vì hằng được đo trên chính tập này. Sửa: thêm "(trong mẫu; kiểm ngoài mẫu ở Tập 7 bằng `measure_pace.py`)".
8. `REPORT.md:164–169`, câu 1: bốn việc gộp chung một lời "duyệt cả bốn", không nêu đánh đổi. Sửa: thêm một vế cho mỗi việc.
   - (a): ngữ cảnh phình, dễ mất container.
   - (d): F-14 làm chậm C3 Tập 7 ≈ N ngày.
   - (f): rủi ro neo điểm.
   - (g): ≈ $140–240/tháng chi thật, so với $0 khi dùng thuê bao.
9. `REPORT.md:177`, câu 2: format được chốt ở G1, nhưng F-14 chỉ biết đạt hay không trước C3. Nếu F-14 trượt sau khi đã viết kịch bản 15 phút thì phải viết lại thành `lab`. Sửa: ghi rõ đánh đổi này, hoặc khuyến nghị "C2 viết `deep` chỉ khi F-14 đã đạt trước G1; chưa đạt thì G1 chọn `lab`".
10. `REPORT.md:189–198`, prompt P1 Tập 7:
    - (i) Chưa nói ai merge `tongket-t6`. Sửa: "bước 0: kiểm `git log main` có `tongket-t6`; chưa có thì dừng, báo chủ dự án".
    - (ii) Prompt cho sửa CHARTER/D-011 trên nhánh `ep007`, trái `episode.md` dòng 32 (trên nhánh tập chỉ sửa phần của tập). Sửa: "áp duyệt trên nhánh `tongket-t6-answer`, merge `main`, rồi mới tạo `ep007`".
    - (iii) Dòng F-14 trên `factory-f14` lẫn vào P1, nhưng prompt lại bảo "Dừng ở G1 lô". Sửa: "F-14 là phiên nhà máy riêng; P1 chỉ ghi prompt cho phiên đó".
    - (iv) Thiếu nhánh xử lý khi chủ dự án trả "không/sửa". Sửa: thêm câu "mục bị bác hoặc sửa → giữ nguyên trạng / áp theo câu sửa, ghi `ANSWER.md`".
    - (v) Danh sách đọc trước có 11 tệp, vượt luật đọc ≤ 8 tệp. Sửa: bớt `REPORT §2–§4` (đã có trong lessons/packaging).

**PHỤ**
11. Ba số trong `REPORT.md` lệch nhẹ so với phép tính:
    - dòng 37: 83,1 ÷ 15 = 5,54, nên là "× 5,5" chứ không phải "× 5,6";
    - dòng 45: 72,95 ÷ 83,1 = 87,8 %, nên là 88 %;
    - dòng 23: 0,706 + (25,5 − 13,49) × 0,052 ≈ 1,33, nên là "≈ 1,3".
12. `REPORT.md:26`: ghi X/Y/Z trần 0,706 triệu, còn `ledger.md:56` ghi ≈ 0,65. Sửa ledger, hoặc ghi rõ nguồn của số 0,706.
13. `REPORT.md:24`: ≈ $605 gồm $29 của tiến trình cuối P3c, trong khi dòng 19 ghi "(log thiếu)". Sửa: "≥ $605 (P3c chỉ có tiến trình cuối)".
14. `REPORT.md` §1b: chưa nêu tên các số trong ±5 % quanh ngưỡng. Thêm "±5 %: 8:56,6 sát trần 9:00 (−0,6 %); EL 7.699/7.700 duyệt".
15. `episode.md:217`: vẫn còn "≥ 1.275 từ nói ÷ 2,52". Sửa: "≥ 1.212 từ nói ÷ 2,40 (505 s)".
16. `thumbs.py`:
    - dòng 93: mã ghi `-bg.png`, nhưng repo có `api-*-bg.jpg`. Nếu `--out` không kết thúc bằng `.png` thì tệp `.json` ghi đè lên ảnh. Sửa: dùng `pathlib.Path(o.out).with_suffix(...)`.
    - dòng 84: mặc định `high` ($0,25/ảnh), trong khi REPORT tính `medium`. Sửa: đặt mặc định `medium`.
17. `text.py:84`: kiểm "> 160" nhưng thông báo và luật đều là 150. Sửa thành `> 150`.
18. `text.py:83`: chỉ so 12 ký tự đầu của cụm tìm kiếm. Sửa: so cả cụm.
19. `rescore.py:15`: `MODEL = 'claude-sonnet-4-5'` đã cũ. Đổi thành `claude-sonnet-5-5` và ghi model vào JSON đầu ra.
20. `anchors.py:62`: `top[j['i']]` không kiểm chỉ số trả về. Thêm `if not 0 <= j.get('i', -1) < len(top): continue`.
21. Mục "ÁP" (e) (`episode.md` §1, vòng 3 "hạ ý cần đọc ra") đụng ý nghĩa nội dung, gần với gu. Thêm "ghi trong gói G2/C4 để chủ dự án thấy".
22. `REPORT.md:192` và `BACKLOG.md` F-14: "bản giao f96da0ea" không phải SHA của merge (merge là `99e90d4`). Ghi rõ đây là MD5 hay SHA của tệp nào.

**Gen CHARTER §4** đạt ở mọi chỗ đã soát:
- Prompt OpenAI có low-poly, không ảnh thật, không mặt, không mũi tên.
- Thumbnail có chân trang "US only · history, not a forecast" và nhãn ILLUSTRATIVE.
- RULES trong `text.py` cấm khuyên và cấm dự báo.
- `rescore.py` loại mặt người, mũi tên dự báo và số tiền không claim.

Chỉ còn lỗi tên thương hiệu ở mục CHẶN 1.