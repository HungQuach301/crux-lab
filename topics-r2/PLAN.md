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
- (3) Bảng AI niêm phong `c042120`; trang chọn https://claude.ai/artifact/9Q2ULkS5L1DXGreNuCSGsk; issue #10. V3 xong: 9/12 khớp theo luật khoá; **debt-2, debt-3, debt-4 trượt V3 chỉ vì cách viết ngày** (hồ sơ ghi `YYYY-MM-01`, agent V3 ghi `YYYY-MM`, cùng tháng; so chuỗi chính xác theo `close()`). Không sửa luật sau khi thấy kết quả: báo cáo con số theo luật khoá (hợp lệ 9/12, CHẶN trượt) và cách đọc theo giá trị (12/12) để chủ dự án quyết.
- (4) 2026-10-04: chủ dự án chốt vòng 2 ĐẠT theo giá trị (D-004 sửa đổi 1); errata `topics-r1` debt-2 (19,26 %/20,6 %) và tax-4 (29,65 %); chuẩn hồ sơ cho r1 tax-4, tax-2 (retire-4 không chạm: Tập 3); lessons R4–R5; merge main; DỪNG. Bước 2 vòng 2 chờ mã `S2R2`. Vòng 3 chưa chạy (chờ lệnh).
- (5) 2026-10-04: bước 2 vòng 2 Có 7/7 → `topics/queue.md` dòng 13–19 (thêm cột "Vòng", đường dẫn có tiền tố vòng, giữ số thứ tự dòng 1–12). Merge main; DỪNG.
