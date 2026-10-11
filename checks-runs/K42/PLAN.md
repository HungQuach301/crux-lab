# PLAN Phiên K lô Tập 7 (K4.2) — đóng 11/10/2026 (≤ 1 trang, D-011)

**Nhánh:** `checks-k42` (từ `origin/main` @ `38fda7d`) · **Phiên:** `session_01DyXYSVjKZym6fUpRYA21ze` · **Khoá:** LOCK `d9a694e5…`

## 1. Trạng thái
Phần **chỉ thêm** đã xong và đã tự merge `main` theo D-008 §2, **trước C4 Tập 7**:
- Kind `term-pair-weekly-replay`: Tập 7 S01 59 mục, 0 lệch; 57/57 claim; 8/8 bất biến; 12/12 đối chứng nhiễu.
- SH06, luật mới cho A30.
- 99/99 luật cũ giữ nguyên fingerprint và cấp. Chạy lại Tập 6 cho kết quả trùng.
- Selftest Python 356/356, trang 67/67.

REVIEWER headless: **ĐẠT có sửa**, đã sửa hết; chi $2,17.

Gói chủ dự án `checks-runs/K42/GOI-chu-du-an.md` có 2 câu (A28, A31) và **chờ trả lời**.

## 2. Việc tiếp (≤ 3) và việc treo
1. Phiên K kế: chép câu trả lời gói vào `checks-runs/K42/GOI-answer.md`, viết A28 và/hoặc A31 theo câu trả lời. Sau đó chạy selftest, báo cáo trước/sau Tập 4–7 và REVIEWER, rồi merge `main`. Việc này **phải xong trước C5** nếu Tập 7 hoặc Tập 8 là `deep`.
2. Bên dựng Tập 7, khi viết `contract.json` ở C4: chép nguyên khối `model` từ `checks-runs/K42/contract-ep007-draft.json`, khai `shorts[].hook`, rồi chạy SH06 trên spec trước khi dựng Short.
- Treo: **A29**, cache trang theo cảnh. Cần làm trong container dựng có trang + `out/video.mp4`, tiêu chí là so byte với `--no-cache` (lý do ghi ở `checks-appeal.md` lô K4.2). **SH05** báo ERROR ở container này: `faster-whisper`/`av` lệch phiên bản, lỗi giống nhau trước và sau K4.2. Cần kiểm môi trường ở container chạy checks C5.

## 3. Quyết định đã có
- 11/10 (lệnh mở phiên): chỉ thêm thì tự merge; sửa luật cũ thì gửi gói ≤ 3 câu; merge `main` trước C4 Tập 7; việc nặng chạy headless; 0 agent con.

## 5. Token
Luồng chính đọc từ log phiên: đầu vào 288 · ghi cache 362.786 · đọc cache 25.209.876 · sinh ra 106.490. Trần (đầu vào mới + sinh ra) ≈ 0,47 triệu, tính đến lúc viết PLAN. Headless: REVIEWER $2,17 (`checks-runs/K42/review/reviewer.out`).

## 6. Phiên sau đọc (≤ 8 tệp)
1. `CHARTER.md` 2. `decisions/D-008.md` 3. `checks/README.md` (mục K4.2, K4.1) 4. `checks-appeal.md` (A28, A31, lô K4.2) 5. `checks-runs/K42/GOI-chu-du-an.md` 6. `checks-runs/K42/GOI-answer.md` 7. `checks/py/r_file.py` (F07), `checks/py/r_content.py` (S14, S15) 8. `toolkit/blind/packets.py` (tally)

## 7. Prompt phiên kế (D-011) — chủ dự án dán nguyên khối vào phiên mới
```
Phiên K4.2b (gói K4.2). Nhánh checks-k42 (từ origin/main mới nhất; merge main vào nếu lệch). Mở bằng `bash toolkit/verify.sh checks-k42`; đọc mục 6 của checks-runs/K42/PLAN.md.
Việc đầu tiên: chép câu trả lời dưới đây vào checks-runs/K42/GOI-answer.md, commit, push.
Rồi viết A28 (toolkit/blind/packets.py + toolkit/tests/test_toolkit_v2.py) và/hoặc A31 (F07 theo format, F13 trần nếu chọn, S14/S15 deep) đúng phương án đã chọn. Selftest đủ, báo cáo trước/sau Tập 4–7, REVIEWER headless (khoá Console, 0 agent con), khoá LOCK, merge main, báo SHA. Đóng theo D-011, DỪNG.
Câu trả lời gói K4.2:
<<DÁN CÂU TRẢ LỜI GÓI K4.2 Ở ĐÂY>>
```
