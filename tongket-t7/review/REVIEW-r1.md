**ĐẠT có sửa** — gói gửi được sau khi sửa 1 mục CHẶN và 7 mục CHÍNH dưới đây. Tất cả đều là sửa câu chữ hoặc số; khung đề xuất không phải đổi. Phần đã khớp nguồn: các phép cộng token (0,58 · 2,22 · 371,05), Console ($115,6; 2,6×), EL (15.932; 1,9×; 37 %; 0,44), lượt chạm (5 theo thiết kế, 4 ngoài cổng, 1 ngoài tập), F-14 ($12,8; 1,41 triệu; ≈ 10 h) và quy đổi P4 (0,91 / 41,90 / 0,09 / 1,00). Phiên chỉ sửa `PLAN.md`, `archive/` và `checks-appeal.md`, không chạm `playbook/`, `CHARTER.md`, `RIGHTS.md` hay `checks/`.

**CHẶN**
1. `tongket-t7/REPORT.md:69`, `:231` (và `:138`): "cổng gốc 16 → 5–7/21" được trình như hồi quy thật, trong khi `gates/G2-answer.md:5` chủ dự án đã ghi "phần lớn nhiễu người chấm" (B11, B13, B19, B29 gần trùng hình). Ngoài ra 16/21 (76 %) tự nó đã TRƯỢT, chỉ cách ngưỡng 17/21 (80 %) chưa tới 5 %, nên theo CHARTER §4 và quality-framework §7 dòng 3 phải nêu tên. Sửa thành: "cổng gốc 16/21 (TRƯỢT, trong ±5 % quanh ngưỡng 17/21) → 5–7/21; chủ dự án đánh giá phần lớn là nhiễu (A32); hồi quy thật chưa tách được". Câu 1 ở mục 8 dựa lý do vào $ và giờ máy, không dựa vào số cổng gốc.

**CHÍNH**
1. `REPORT.md:20`, `:239`: mức cảnh báo `lab` 15 triệu tính cả "log phiên + headless thuê bao" (`episode.md:196`), nhưng số 2,80 bỏ phần headless. Sửa: "trần phiên ≥ 2,80 + headless ≥ 1,31 (P1 0,81 + P2 ≈ 0,5; P3 chưa cộng) → ≥ 4,1 triệu, vẫn dưới 15".
2. `REPORT.md:44`: hai nguồn lệch nhau. Phần chi tiết cộng ra 2,9 + 2,9 + 0,3 = 6,1 h, không phải 5,8; `ledger.md:51` ghi dựng lại 1080p "≈ 1,9 h máy", còn TONGKET-INPUT h ghi 2,9. Sửa: chọn một nguồn, ghi cả số kia, cộng lại cho đúng.
3. `REPORT.md:75`, `:136`: câu "REVIEWER trung gian chưa lần nào đổi quyết định cổng" (chất lượng ≈) bị ledger phản bác. REVIEWER C4 ý đồ bắt 2 CHẶN và 4 CHÍNH, đã áp (`ledger.md:41`); REVIEWER C3 bắt 5 CHÍNH (`:32`). Sửa: liệt kê những gì các lượt đó bắt được, và nói lỗi nào L1 hoặc Giám sát liền mạch bắt thay được, lỗi nào không. Nếu không chứng minh được, giữ REVIEWER C4 ý đồ.
4. `REPORT.md:197` so với `:237`: đích mới "trần phiên ≤ 3 triệu/tập" là hạ mức cảnh báo chủ dự án đã duyệt ngày 11/10 (15 triệu), nhưng câu 3 không nhắc. Sửa: thêm "hạ mức cảnh báo trần 15 → 3 triệu" vào câu 3, hoặc bỏ đích này.
5. `REPORT.md:235`, `:239`: câu 2 và câu 3 thiếu dòng "Đánh đổi:" riêng như câu 1. Câu 2: "giữ nhạc bằng mã thì chất nhạc không tăng ở Tập 8; footage tốn +0,5–1 h/tập kiểm quyền". Câu 3: "thêm cột ghi sổ cho mỗi mốc; đích Tập 9 chưa có tập nào kiểm chứng".
6. `REPORT.md:142`: danh sách "Chưa áp" thiếu hai chỗ CHARTER trái với quyết định 1 Short / 0 thumbnail: CHARTER §1 ("kèm 2–3 Shorts mỗi tập") và CHARTER §5 dòng G2 (thumbnail, ChatGPT). Sửa: thêm hai chỗ này và nhắc trong câu 1.
7. `REPORT.md:113`: M5 có thêm "nháp 720p để xem" (và `:125` thêm "3 khung 1080p"). Đây là một lượt dựng ngoài trình tự "nháp 540p → 1080p một lần" và chưa tính vào giờ máy M5 ở `:192`. Sửa: cho G2 xem trên 540p, hoặc ghi giờ máy của lượt 720p vào M5.
8. `de-xuat/RIGHTS-sF.md:6`: xếp LoC/NARA vào bậc 1 "phạm vi công cộng" là nói quá. Phần lớn tư liệu LoC/NARA không phải tác phẩm theo §105, và nhãn "No known restrictions" chỉ là đánh giá của thư viện, không phải bảo đảm. Sửa: chỉ tác phẩm của nhân viên liên bang (§105) ở bậc 1; tệp LoC/NARA ghi "No known restrictions" phải lưu bản chụp nhãn và ghi rõ "đánh giá của tổ chức, không bảo đảm".

**PHỤ**
1. `REPORT.md:19–20`: dòng P4 chỉ có "≥" ở cột trần; nếu chỉ đọc tiến trình cuối thì mọi cột đều phải "≥". Cộng cột trần ra 2,79 (cột sinh ra + đầu vào ra 2,80): ghi chú làm tròn.
2. `REPORT.md:45`: "≥ 36" dựa trên P3 "≈ 30" và P2 "chưa ghi", nên dấu "≥" không đứng được. Sửa thành "≈ 36 (P2 chưa ghi)".
3. `REPORT.md:194`: cận dưới các mốc Console cộng ra 23, không phải 25. Sửa thành "$23–39" hoặc chỉnh lại từng mốc.
4. `REPORT.md:97`: phép thử của Line producer đo chi của các vai khác, không đo đầu ra của chính vai này (sổ chi). Thêm phép thử riêng, ví dụ sổ chi khớp `total_cost_usd` và log ±2 %, hoặc ghi rõ đây là luật ngắt, không phải phép thử vai.
5. `REPORT.md:104`: đạo diễn máy đã là chẩn đoán sẵn (CHARTER §4 L2, `episode.md:37`). Sửa thành "đã là chẩn đoán; điều mới là lời phê chỉ thành việc sửa khi phép thử của vai sở hữu cũng trượt".
6. `REPORT.md:94`: phép thử của Previz dựa vào biên nhiễu A32, mà A32 vẫn đang `mở`. Thêm A32 vào rủi ro ở `:125`.
7. `REPORT.md:150–157`: bảng mục 4 thiếu tác động token/$ cho từng dòng (chỉ có tổng ở `:159`). Thêm cột này.
8. `PLAN.md` mới đã bỏ dòng "bộ lấy mẫu trang chạy ở C4/C5 trước G2" (`archive/PLAN-kenh-history.md:17`). P1 Tập 8 đang chạy theo mẫu cũ, và nếu chủ dự án chọn 1c thì bài học này mất. Giữ lại một dòng trong mục "Tiếp".
9. `de-xuat/RIGHTS-sF.md:3`: "bậc thấp nhất" dễ hiểu ngược; sửa thành "bậc có số nhỏ nhất". `de-xuat/CHARTER-s4.md:8`: con số riêng của Tập 8 (≤ 15 %) nên để ở RIGHTS §F, không đưa vào CHARTER.
10. `checks-appeal.md:81–84`: 8 cột, trạng thái `mở`, không trùng số với A1–A37, không đòi sửa `checks/` trực tiếp, đều đúng. Còn ba điểm nhỏ:
    - A39 dựa vào RIGHTS §F chưa được duyệt: ghi thêm "phụ thuộc câu 2".
    - A40 đưa thước nhịp F-14 vào, mà đó không phải luật CHẶN: bỏ câu đó.
    - A38 ghi "không cần duyệt lại", trong khi đầu tệp quy định chủ dự án duyệt phán quyết của K: sửa thành "duyệt phán quyết K như thường lệ".
11. `REPORT.md:243`: `tongket-t7/review/REVIEW-r1.md` chưa có (thư mục mới có `brief-r1.md`). Ghi tệp này trước khi gửi gói.

Giấy phép, phần còn lại đúng: §105 và phù hiệu NASA; OSM dữ liệu ODbL còn tile CC BY-SA; Pexels/Pixabay không phải CC0; danh sách cấm NC, ND, BY-SA cho hình; Freesound CC0/CC BY; BBC RemArc phi thương mại.