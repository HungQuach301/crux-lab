Bạn là REVIEWER (CHARTER §7: soát mọi gói trước khi gửi; không quyết, không sửa tệp). Repo ở thư mục hiện tại, nhánh `factory-f17`.
Việc: soát phiên nhà máy F-17 (lớp ánh sáng điện ảnh opt-in) = diff `git diff acdd14d6..HEAD -- toolkit RIGHTS.md .gitignore` và báo cáo
`toolkit/factory/f17/REPORT.md`, đối chiếu ý đồ ghi trước `toolkit/factory/f17/INTENT.md` (commit cdd69fe6, trước mọi lần đo). Nguyên mẫu: nhánh
`rnd-hybrid` @ ba5d27f8 (`git show origin/rnd-hybrid:rnd-hybrid/v4/REPORT.md`, `…/v4/light/cine.js`). Bằng chứng số: `toolkit/factory/f17/out/`.

Trả lời bằng tiếng Việt, ngắn, theo mục, mỗi phát hiện ghi CHẶN / CHÍNH / PHỤ + tệp:dòng:
1. Bất biến "không khai `cine` = trùng byte": có đường nào trong `world/render_shots.js`, `world/core.js` (O.text serif), `world/build_seg.py`,
   `toolkit/blind/headless.sh` đổi sản phẩm/báo cáo khi KHÔNG khai? Nháp `--res 540`, `--spp`, Short dọc, trang kiểm `CK.on` có thật sự không bật lớp?
2. Đúng/sai mã `world/cine/cine.js`: pass khoá màu (RenderPass không vẽ vật dữ liệu nhưng vẫn đổ bóng; LockPass dùng `isXRRenderTarget` để tone-map +
   sRGB trong shader — có tác dụng phụ không?), `baseScene` (khôi phục đèn/sương/vật liệu sau mỗi lần), DofPass (nới độ sâu 3×3), AO nửa độ phân giải,
   viền người (chỉ Person; phía xa đèn = 0), mái theo cỡ chiếu, tất định (không Math.random lúc vẽ).
3. Luật mới `cine/cine_check.js` + `cine/cine_color.py`: CIEDE2000 đúng? mặt nạ (co 2 px, ≥ 200 điểm), ngưỡng thứ tự sáng (|ΔL*| ≥ 1 trước, ≥ 0,5 sau)
   có mâu thuẫn INTENT ("đảo thứ tự sáng → CHẶN") không? Thước có thể bị qua nhờ chính cơ chế khoá (tự chấm) không — nêu rõ điều luật thật sự đảm bảo
   và điều nó không đảm bảo.
4. REPORT có nói quá bằng chứng không? Kiểm từng dòng T1–T13 với tệp ở `f17/out/`; đích có bị hạ hoặc thước có bị đổi sau khi đo không (so INTENT)?
   Đặc biệt T6 (viền: thước gốc vs "lõi xa đèn" chẩn đoán), T11 (giờ máy), T12 (verify), T13 (cổng gốc chỉ chẩn đoán).
5. RIGHTS §F9 (18 tệp Poly Haven CC0 ≤ 2 MB, SHA-256, trích giấy phép), `assets/fetch.py`; .gitignore; có tệp nào ngoài toolkit/, RIGHTS.md, .gitignore
   bị đổi (ep008, episodes/ep007, checks/ không được chạm)? Có in/ghi khoá API ở đâu không?
6. Kết luận một dòng: ĐẠT / ĐẠT có sửa / TRƯỢT.
Không chạy lệnh nặng (không render, không checks). Chỉ đọc tệp, `git diff`, `git log`, `git show`, `python3 -c` nhỏ để đọc JSON.
