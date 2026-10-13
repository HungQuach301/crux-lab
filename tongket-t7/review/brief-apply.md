Bạn là REVIEWER (playbook/quality-framework.md §7) soát PHẦN ÁP tổng kết Tập 7 (D-013) trước khi merge main. CHỈ ĐỌC, không đọc thư mục checks/. Repo ở thư mục hiện tại, nhánh tongket-t7.
Đọc: tongket-t7/ANSWER.md (câu trả lời nguyên văn của chủ dự án — đây là lệnh); decisions/D-013.md; `git diff c7358285 --stat`; diff của CHARTER.md, RIGHTS.md, playbook/{episode.md,story.md,lessons.md,quality-framework.md,packaging.md}, playbook/templates/{TAM-NHIN.md,BAN-DO-LIEN-MACH.md,PLAN-tap.md,G1.md,HUONG-DAN-DANG.md,check_script.py}, playbook/prompts/, checks-appeal.md, PLAN.md.
Soát:
1. Mỗi mục trong lệnh của chủ dự án đã áp đúng và đủ, không áp quá lệnh (vd không đổi nhạc sang CC BY; không sửa checks/; số khiếu nại A38–A41 giữ, ep008 → A42–A45).
2. Mâu thuẫn còn sót giữa các tệp sau khi áp (C3 cổng riêng, 3 vòng, 2–3 Shorts, thumbnail, ChatGPT ở G2, prompt phiên kế, M2 30 s / M3 30 s) trong CHARTER, episode.md, story.md, templates, prompts — chỉ nêu chỗ còn hiệu lực, không nêu phần đã ghi rõ là lịch sử/tham chiếu.
3. Công thức kể chuyện (story.md §1–§3, check_script M7/M8): đúng lệnh; không chép lời/hình/tên chương/thương hiệu của kênh tham chiếu; không trái gen CHARTER §4 (không khuyên, không dự báo, US only, history not a forecast, ILLUSTRATIVE) — vd "bảng điểm" không thành lời khuyên; "chuyền tập kế" không hứa ngày; M8 với "US only"/"history, not a forecast" phải có trong lời (check_script vẫn kiểm?) có mâu thuẫn không.
4. check_script.py: lỗi mã (biến, vai mới `fact`, M7 None khi < 3 fact, M8 kiểu số), ảnh hưởng tới kịch bản Tập 7 cũ (chỉ nêu, không chạy lại).
5. CHARTER < 2 trang; RIGHTS §F/§G đúng pháp lý cơ bản.
Trả về tiếng Việt: dòng đầu "ĐẠT", "ĐẠT có sửa" hoặc "TRƯỢT"; rồi CHẶN / CHÍNH / PHỤ (tệp:dòng, vấn đề, câu sửa). ≤ 40 dòng.
