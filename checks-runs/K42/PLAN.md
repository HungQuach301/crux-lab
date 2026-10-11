# PLAN Phiên K lô Tập 7 (K4.2 + K4.2b) — đóng 11/10/2026 (≤ 1 trang, D-011)

**Nhánh:** `checks-k42` (từ `origin/main` @ `38fda7d`) · **Phiên:** `session_01DyXYSVjKZym6fUpRYA21ze` · **Khoá:** LOCK K4.2 `d9a694e5…` → K4.2b `dc4981b3…`

## 1. Trạng thái
Phần **chỉ thêm** đã xong và đã tự merge `main` theo D-008 §2, **trước C4 Tập 7**:
- Kind `term-pair-weekly-replay`: Tập 7 S01 59 mục, 0 lệch; 57/57 claim; 8/8 bất biến; 12/12 đối chứng nhiễu.
- SH06, luật mới cho A30.
- 99/99 luật cũ giữ nguyên fingerprint và cấp. Chạy lại Tập 6 cho kết quả trùng.
- Selftest Python 356/356, trang 67/67.

REVIEWER headless: **ĐẠT có sửa**, đã sửa hết; chi $2,17.

**K4.2b (gói 1a, 2b, `GOI-answer.md`) đã viết và merge `main`:** F07 theo format (101 480–540 · lab 540–660 · deep 840–1020 s, CHÍNH), S14 deep 2–3 mid-roll cách ≥ 180 s, S15 sàn deep 840 s; `packets.py tally` mặc định rubric mới. Trước/sau Tập 4–7: chỉ Tập 4 F07 PASS → FAIL; A28 8 lượt Tập 6, không FAIL → PASS. REVIEWER ĐẠT có sửa (đã sửa), $1,05.

## 2. Việc tiếp (≤ 3) và việc treo
1. Bên dựng Tập 7, khi viết `contract.json` ở C4: chép nguyên khối `model` từ `checks-runs/K42/contract-ep007-draft.json`, khai `shorts[].hook`, rồi chạy SH06 trên spec trước khi dựng Short.
2. Nhà máy: `toolkit/factory/spec.py` FORMATS chưa có `deep` (REVIEWER K4.2b PHỤ 8, ngoài `checks/`) → thêm ở nhánh `factory-*` trước khi dựng tập `deep` đầu tiên.
- Treo: **A29**, cache trang theo cảnh. Cần làm trong container dựng có trang + `out/video.mp4`, tiêu chí là so byte với `--no-cache` (lý do ghi ở `checks-appeal.md` lô K4.2). **SH05** báo ERROR ở container này: `faster-whisper`/`av` lệch phiên bản, lỗi giống nhau trước và sau K4.2. Cần kiểm môi trường ở container chạy checks C5.

## 3. Quyết định đã có
- 11/10 (lệnh mở phiên): chỉ thêm thì tự merge; sửa luật cũ thì gửi gói ≤ 3 câu; merge `main` trước C4 Tập 7; việc nặng chạy headless; 0 agent con.

## 5. Token
Luồng chính đọc từ log phiên (K4.2 + K4.2b): đầu vào 478 · ghi cache 500.629 · đọc cache 48.231.047 · sinh ra 154.503. Trần (đầu vào mới + sinh ra) ≈ 0.66 triệu. Headless: REVIEWER K4.2 $2.17 + K4.2b $1.05.

## 6. Phiên sau đọc (≤ 8 tệp)
1. `CHARTER.md` 2. `decisions/D-008.md` 3. `checks/README.md` (mục K4.2, K4.1) 4. `checks-appeal.md` (A28, A31, lô K4.2) 5. `checks-runs/K42/GOI-chu-du-an.md` 6. `checks-runs/K42/GOI-answer.md` 7. `checks/page/sampler.js` (A29) 8. `playbook/lessons.md` (T6-4)

## 7. Prompt phiên kế
Không có phiên K kế đang chờ: gói K4.2 đã trả lời và đã áp. Lô K sau mở theo `checks-appeal.md` (A29 trong container dựng) hoặc khi tập cần kind mới (K-brief).
