**ĐẠT có sửa.** Phải sửa 2 mục CHẶN trước khi merge. Lệnh của chủ dự án đã áp đủ và không áp quá lệnh. Đã kiểm:
- nhạc vẫn làm bằng mã, chưa đổi sang CC BY;
- `checks/` không bị sửa;
- khiếu nại A38–A41 giữ nguyên, ep008 ghi đổi sang A42–A45;
- `origin/main` vẫn là c7358285, nên merge không xung đột;
- story.md chỉ nêu tên kênh tham chiếu, không chép lời, hình, tên chương hay thương hiệu. Câu ví dụ là câu tự viết;
- "bảng điểm" có ghi "không khuyên chọn bên nào"; "chuyền tập kế" có ghi "không hứa ngày ra";
- RIGHTS §F/§G đúng về pháp lý cơ bản: luật Mỹ 17 U.S.C. §105 (tác phẩm nhân viên liên bang thuộc phạm vi công cộng), phù hiệu NASA, dữ liệu OSM theo ODbL còn ô bản đồ theo BY-SA, Pexels/Pixabay không phải CC0, cấm NC/ND/Sampling+.

**CHẶN**
1. `playbook/templates/check_script.py:309-310` (M5) không thể đạt cùng lúc với M2 50 s. M5 tìm câu nhân vật quay lại **sau khi lời hứa kết thúc** và đòi câu đó kết thúc ≤ 45 s. Nếu lời hứa kết thúc ở 45–50 s (story §1 cho phép tới 0:50), M5 luôn TRƯỢT. Thứ tự mở đầu ở story.md:6-11 cũng tự mâu thuẫn: lời hứa ≤ 0:50 nằm trước nhân vật ≤ 0:45.
   Sửa: đo M5 theo lần **đầu tiên** nhân vật xuất hiện ≤ 45 s, bỏ điều kiện `r['start'] >= p['end']`. Như vậy khớp với chữ "xuất hiện trước 0:45" ở story §1.6, §2b.1 và episode.md:124. Không đổi ngưỡng.
2. `playbook/story.md:10` (M8) mâu thuẫn với `check_script.py:258-261` và quality-framework C2 (a). Story ghi "US only" và "history, not a forecast" đưa **lên hình**. Nhưng check_script CHẶN khi hai cụm này **không có trong lời**.
   Sửa câu: "'US only' và 'history, not a forecast' vẫn nói một lần trong lời (luật máy): một cụm là câu miễn trừ duy nhất của phần mở đầu, cụm kia đặt ở thẻ phương pháp hoặc phần giới hạn; giả định và ILLUSTRATIVE lên hình."

**CHÍNH**
3. `episode.md:23` nói Tập 8 chạy theo mẫu cũ tới G1. Nhưng `check_script.py` trên main đã đòi M7/M8 ngay, nên P1 Tập 8 sẽ TRƯỢT M7 nếu dùng mẫu mới.
   Sửa: thêm "P1 Tập 8 dùng `check_script.py` bản c7358285 (M2 30 s, M3 30 s, không M7/M8) tới G1", hoặc thêm cờ `--v4`.
4. Chạy lại kịch bản Tập 7 cũ (chỉ nêu, không chạy lại): kịch bản không có câu vai `fact`, nên M7 trả về None, TRƯỢT và exit 1; `hooks.md` cũng vậy. M2 và M3 thì nới ra nên vẫn đạt.
5. `story.md:7` ghi "không số thứ ba trong một câu". Luật đang CHẶN ở mức ≤ 2 số mới **mỗi cảnh**, và story §3 có ≤ 1 số mỗi ~8 s. Ba sự thật dồn vào S01 sẽ bị chặn.
   Sửa: "≤ 2 số mới mỗi cảnh; ba sự thật trải ≥ 2 cảnh; mỗi sự thật ≤ 1 số nói."
6. `story.md:7` với `story.md:11`: ba sự thật có claim đứng trước nhân vật, trái luật "người trước số" (G-007).
   Sửa: thêm "ít nhất 1 trong 3 sự thật gắn với nhân vật dẫn đường hoặc người như người xem".

**PHỤ**
7. `check_script.py:333` và `:330`: kịch bản đạt M8 = 1 luôn bị cảnh báo "±5 % ngưỡng". M8 là số đếm câu nhưng in đơn vị "s". Sửa: bỏ cảnh báo ±5 % cho M8 và in "câu".
8. `check_script.py:444`: chú thích còn ghi "sau 30 s đầu", sửa thành "sau 50 s đầu".
9. `templates/G1.md:36` ghi "M1 · … · M6", trùng với dòng 49 ghi M1–M8. Bỏ dòng 36.
10. `templates/L3.md:9,15` còn "nhịp hết 3 vòng", sửa thành 2 vòng; "điền sẵn ở P3" sửa thành M5. Mẫu này vẫn dùng ở G2.
11. `templates/HUONG-DAN-DANG.md:3` ghi "P3 điền sau G2", sửa thành "M6 điền".
12. `templates/PACKAGING-BRIEF.md:2` vẫn ghi "ĐƯỜNG CHÍNH từ Tập 7". Thêm "bỏ từ Tập 8 (D-013), chỉ tham chiếu".
13. `packaging.md:105` "30 s đầu" sửa thành 50 s. Trong `quality-framework.md`:
    - dòng 101 "móc 30 s đầu" sửa thành 50 s;
    - dòng 52 "đủ bộ cuối C4 và C5" sửa thành "ở M5 trên nháp";
    - dòng 107 "P4, D-011" sửa thành "phiên M6".
14. `quality-framework.md` §7: checklist REVIEWER chưa có các mục D-013. Thêm mục 9 gồm:
    - M7/M8;
    - tên chương gợi hình và câu chốt cuối chương;
    - bảng điểm không khuyên;
    - chuyền tập kế không hứa ngày;
    - không chép kênh tham chiếu.
15. `prompts/CHAY-TAP-N.md:19`: "ý đồ kiểm định trước M5" đang nằm ở bước đóng chặng. Chuyển sang bước 3, chặng sau G1.
16. `episode.md:1` tiêu đề còn "playbook v4", sửa thành v5 (D-013).
17. `RIGHTS.md` §G chỉ nhận CC BY **4.0**, hẹp hơn lệnh "CC BY". Như vậy vẫn an toàn, nhưng ghi lý do bỏ 3.0, hoặc nhận cả CC BY 3.0 kèm ghi công đủ.
18. `CHARTER.md` có ≈ 1.460 từ, 84 dòng (v4: 1.337 từ), dễ vượt 2 trang. Gợi ý: rút gạch đầu dòng footage ở §4 còn một dòng trỏ sang `RIGHTS.md` §F.