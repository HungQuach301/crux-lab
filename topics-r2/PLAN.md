# PLAN — topics-r2 (Phiên DT1, vòng 2 Mốc 3 v2)

Thẩm quyền: `decisions/D-004.md`; lệnh vòng 2 của chủ dự án 2026-10-01. Thiết kế ghi trước: `DESIGN.md`. Nhánh `topics-r2` (từ main `e117c49`). Không chạm Tập 1.

## Quyết định kỹ thuật
1. Khối loại trùng (`EXCLUDE`) đưa nguyên văn cho cả hai bên, nối sau khối BRIEF: cách duy nhất để đối chứng không lặp đề tài vòng 1 mà vẫn cùng một đầu bài. Không phải biến thí nghiệm (yêu cầu "thẻ mới" của chủ dự án).
2. Trang chấm: nút bật/tắt "Want to make it" + "Next topic"; mã chỉ hiện khi đúng 9; chặn chọn thẻ thứ 10.
3. Bảng AI: cùng 6 vai, cùng ngân sách 9/18, agent mới.
4. Nhánh `claude/lucid-bardeen-n6olpt` trên GitHub: proxy trả 403 khi xoá (như lần trước với các nhánh khác) → chủ dự án xoá tay.

## Điểm dừng an toàn
- (1) main `e117c49` (merge topics-r1, FREEZE/key/SEAL khớp), issue #8 #9 đóng. Vòng 2: DESIGN + BRIEF + công cụ chép từ vòng 1. Tiếp: đối chứng + 3 agent máy.
