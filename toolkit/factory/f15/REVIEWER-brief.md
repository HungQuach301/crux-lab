Bạn là REVIEWER (CHARTER §7: soát mọi gói trước khi gửi; không quyết, không sửa tệp). Repo ở thư mục hiện tại, nhánh `factory-f15`.
Việc (lượt 2, trước squash merge vào main — chủ dự án 14/10 đã quyết merge dù T3/T7 TRƯỢT): soát phiên nhà máy F-15 = diff `git diff origin/main..HEAD -- toolkit RIGHTS.md` (đã rebase lên 7f8a0da, LOCK b4551642; RIGHTS §F/F6 là luật footage của main) và báo cáo `toolkit/factory/f15/REPORT.md` đối chiếu
ý đồ ghi trước `toolkit/factory/f15/INTENT.md` (commit 6c42086, trước mọi lần đo). Bằng chứng số ở `toolkit/factory/f15/out/`, `checks/`, `root-*/`.

Trả lời bằng tiếng Việt, ngắn, theo mục, mỗi phát hiện ghi CHẶN / CHÍNH / PHỤ + tệp:dòng:
1. Bất biến "opt-in hoặc trùng byte khi không bật": có đường nào trong `toolkit/factory/build.py`, `world/build_seg.py`, `world/render_shots.js`,
   `world/core.js`, `world/page.html`, `world/shorts.py`, `world/episode_page.py`, `qc.py`, `spec.py` đổi sản phẩm hoặc báo cáo khi KHÔNG khai cờ mới
   (`--res`, `--spp`, `--resume`, plate)? Đặc biệt: build nguyên tử (`rel()`, `promote()`, `qc.py` đọc từ `B.work`), `spec.yaml_bool_traps` (thêm BLOCK).
2. Đúng/sai mã: `bg.sh` (setsid -f, PID, stop theo nhóm), `verify.sh --install` (pipefail, nhánh ASR), `api.sh` (cấm Task/Agent/Workflow, --max-budget-usd),
   `draft_overlay.py`, `toolkit/footage/fetch.py` (giấy phép nguyên văn bắt buộc, dòng RIGHTS), `map.py`, `world/plate.js`.
3. REPORT có nói quá bằng chứng không? (gồm §1b: T11/T13 chạy lại, T1/T14 trên mã rebase; T3 0,419 và T7 phải ghi TRƯỢT, không hạ đích) Kiểm từng dòng T1–T14 với tệp bằng chứng; đích có bị hạ sau khi đo không (so INTENT)?
4. Rủi ro an toàn/bản quyền: ba dòng RIGHTS F6 (X-F15-1..3) có đúng cột, bậc F1, trích nguyên văn, SHA, bản chụp nhãn quyền LoC; clip thử có theo F3/F4 (năm + nguồn trên hình, hoà từ 3D, dòng nguồn không đè)?
5. README nhà máy có ghi quy ước nháp (F08, F01, SH01 chỉ tin 1080p; bộ lấy mẫu trang không rẻ hơn → chờ A29)? Có tệp nào ngoài toolkit/, RIGHTS.md bị đổi (ep008, checks/ không được chạm)?
6. Kết luận một dòng: ĐẠT / ĐẠT có sửa / TRƯỢT.
Không chạy lệnh nặng (không render, không checks). Chỉ đọc tệp, `git diff`, `git log`, `python3 -c` nhỏ để đọc JSON.
