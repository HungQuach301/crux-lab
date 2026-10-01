# PLAN — topics-r2 (Phiên DT1, vòng 2 Mốc 3 v2)

Thẩm quyền: `decisions/D-004.md`; lệnh vòng 2 của chủ dự án 2026-10-01. Thiết kế ghi trước: `DESIGN.md`. Nhánh `topics-r2` (từ main `e117c49`). Không chạm Tập 1.

## Quyết định kỹ thuật
1. Khối loại trùng (`EXCLUDE`) đưa nguyên văn cho cả hai bên, nối sau khối BRIEF: cách duy nhất để đối chứng không lặp đề tài vòng 1 mà vẫn cùng một đầu bài. Không phải biến thí nghiệm (yêu cầu "thẻ mới" của chủ dự án).
2. Trang chấm: nút bật/tắt "Want to make it" + "Next topic"; mã chỉ hiện khi đúng 9; chặn chọn thẻ thứ 10.
3. Bảng AI: cùng 6 vai, cùng ngân sách 9/18, agent mới.
4. Nhánh `claude/lucid-bardeen-n6olpt` trên GitHub: proxy trả 403 khi xoá (như lần trước với các nhánh khác) → chủ dự án xoá tay.

## Điểm dừng an toàn
- (1) main `e117c49` (merge topics-r1, FREEZE/key/SEAL khớp), issue #8 #9 đóng. Vòng 2: DESIGN + BRIEF + công cụ chép từ vòng 1. Tiếp: đối chứng + 3 agent máy.
- (2) Đối chứng 6/6 (`c47c00a`; khoá có thể thu hồi). Lần mở bên máy đầu tiên bị DỪNG sau vài giây và chạy lại: lệnh có lỡ thêm câu gợi ý từ bảng AI vòng 1 ("not me / too narrow → chọn nhóm người xem lớn") — đó là biến thứ hai. Đã xoá câu đó, xoá đầu ra dở dang, chạy lại. Khác biệt còn lại so với lệnh vòng 1 (không phải biến thí nghiệm): khối EXCLUDE; ví dụ hồ sơ trỏ `topics-r1/machine/` thay cho `m3/machine/`; tự kiểm gọi thẳng `verify.py`.
