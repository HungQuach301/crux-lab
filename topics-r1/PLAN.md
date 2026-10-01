# PLAN — topics-r1 (Phiên DT1, vòng thử 1 Mốc 3 v2)

Thẩm quyền: `decisions/D-004.md`. Thiết kế khoá: `DESIGN.md`. Không chạm Tập 1 / `ep001-v2`. Bắt đầu 2026-10-01 00:00 UTC (trần 240 phút → 04:00 UTC: commit và báo).

## Quyết định kỹ thuật (tự quyết, có lý do)
1. **Nhánh.** Phiên bị giới hạn đẩy lên `claude/lucid-bardeen-n6olpt` (tạo từ main `6ab42be`); cùng commit được đẩy song song lên `topics-r1` như lệnh. Hai nhánh luôn trùng nhau. Tiền lệ M3: chủ dự án giữ tên nhánh phiên.
2. **Số nhận diện vs số kết quả kiểm bằng máy:** số chỉ được *sinh ra* ở Viewer/Decision; Promise/Title/Thumbnail chỉ được lặp lại số đã có ở đó. Viewer/Decision bị chặn khi có từ kết quả ("saves", "break even"…) cạnh một số. Lý do: luật "cấm số kết quả" cần một phép thử cơ học áp như nhau cho hai bên; số nhận diện mô tả người xem nên phải nằm trong Viewer/Decision.
3. **Tên tài khoản phổ biến** (401(k), 403(b), 457(b), IRA, Roth IRA, HSA, 529 plan) được dùng: người xem gọi tài khoản bằng tên này ("người như tôi"); tên luật/điều khoản, cơ quan, nguồn, mã chuỗi vẫn cấm. Khác M3 (M3 cấm) vì thẻ mới cần người xem nhận ra mình.
4. **Khuôn Thumbnail:** `<vật thể> / "<chữ trên ảnh>"`, vật thể ≤ 12 từ, chữ ≤ 4 từ — để máy đếm được "≤ 4 chữ".
5. **V0** (hồ sơ đủ + cardcheck + kết luận mới lạ hợp lệ) thêm trước V1–V5 vì hồ sơ mới có sáu tệp; V1–V5 giữ nghĩa và dung sai M3.
6. **Mã chấm** tự chứa (không cần hạ tầng lưu): `R1-<sha6> NN:điểm:chip:giây …`.
7. Đối chứng xin đúng 2 thẻ/trụ trong một lệnh (như M3 xin đúng quota), giữ vai và tham số M3.

## Điểm dừng an toàn
- 2026-10-01 00:20 UTC (1): D-004 (`b7aa720`); BRIEF, DESIGN, cardcheck v2, verify.py khoá. Tiếp: 3 agent máy + đối chứng song song.
