**ĐẠT có sửa.** Không có lỗi CHẶN. Gói gửi được sau khi sửa 5 mục CHÍNH dưới đây.

Lượt 1 có 22 mục, đã kiểm cả 22: 21 mục đã sửa đúng. CHẶN-1 (thương hiệu) không phải lỗi, vì "Money Rerouted" là kênh của Crux (T6-12). Phần còn dở của các sửa ở lượt 1 nằm ở PHỤ-1 và PHỤ-5. Các số đã khớp nguồn:
- Trần từng phiên khớp `t6.jsonl` (P1 0,88 · P2 1,73 · P3 0,39 · P3b 72,95 · K 1,86).
- Sinh ra 2,84 · đọc cache 825,9 · agent 25 · giờ máy 23,44 h · EL 7.699 · 5,8 triệu · × 5,5 · 88 %.
- Chi Console: $25,5 (= 25,46) và X/Y/Z $13,49, khớp `PLAN-history.md:182,283`. Phép tính 228.104 + 246.213 cũng khớp.
- Cổng gốc 20/23 (C4 21/23) · 36/36 · 13/13 khớp G2. Điểm §4f khớp `rescore.json`.
- Độ dài 882/1020/930 s · thiếu ≈ 830 từ · 2,40/2,66.
- Gen §4: PROMPT OpenAI, footer, RULES của `text.py` và `rescore.py` đều đạt. `anchors/*.json` chỉ chứa nhãn, không có số thô của kênh khác.

**CHÍNH**
1. `REPORT.md:10,21` — trần phiên K có thể bị đếm thiếu.
   - K có `pti` 0 và `origin` human, lại có 2 lượt người (mở K + trả lời K4.1), và `first_request_input_tokens` 521.227. Đây đúng là dấu hiệu khởi động lại mà dòng 10 dùng để sửa P3c.
   - Đọc lại transcript không đưa lại `modelUsage` của tiến trình trước.
   - Sửa: đo K bằng `session_tokens.py` trên transcript cục bộ như P3c. Nếu không đo được thì ghi "K ≥ 1,86 (tiến trình cuối)", "cả tập ≥ 83,0", và ghi rõ "−3 % so Tập 5 chưa chắc" (vì K thiếu > 2,4 triệu là đổi dấu).
2. `packaging.md:113` (cùng `PACKAGING-BRIEF.md:24` "Kit (fixed)" và `thumbs.py`) — bộ nhận diện là gu (REPORT §5 câu 3) nhưng đã ghi thành LUẬT "cố định mọi tập". BƯỚC 0 của prompt lại merge nó vào `main` trước khi chủ dự án trả lời.
   - Sửa: thêm "*(chờ chủ dự án — gói tổng kết Tập 6 câu 3)*" vào tiêu đề §7.4 và vào dòng Kit của brief.
   - Ở `REPORT.md:79`, ghi (i) = "ÁP phần luật vật thể/đường lai; bộ nhận diện CHỜ".
3. `toolkit/package/thumbs.py:94` (và `packaging.md:111`) nói lớp chữ "qua claim-risk", nhưng mã không kiểm chữ: không chạy `scan`/`bad_numbers` và không xác thực `--claims`.
   - Sửa: import `scan`, `bad_numbers`, `claim_number_set` từ `package_check`, đọc `claims.json` của tập, rồi `sys.exit` khi chữ có câu khuyên/dự báo hoặc có số không có claim.
4. `toolkit/checks_split.sh:23` — `[ -n "$PYONLY" ] || node … && echo` kiểm sai.
   - Nếu `sampler.js` lỗi, `set -e` không dừng, nên `run.sh` vẫn chạy với `SKIP_PAGE=1` trên `page.json` cũ, và `|| true` nuốt mã lỗi. Kết quả có thể ra ĐẠT trên dữ liệu trang cũ.
   - Sửa: `if [ -z "${PYONLY:-}" ]; then node … --jobs "${K_JOBS:-4}" || { echo "sampler lỗi"; exit 4; }; echo "page sampler OK"; fi`.
5. `REPORT.md:207` (prompt P1) — "Việc nặng headless khoá Console (toolkit/api.sh), 0 agent con" là bắt buộc vô điều kiện, trong khi 1g (chi tiêu) còn CHỜ.
   - Sửa: "nếu 1g duyệt: …; nếu bác: headless thuê bao (`toolkit/blind/headless.sh`), agent con theo `episode.md` §1".

**PHỤ**
1. `REPORT.md:24,34` và `episode.md:191`: với Console 1,33, tổng là 77,82 + 2,67 + 0,14 + 1,04 + 1,33 = **83,0**, không phải 83,1. Mức −3 % và 88 % giữ nguyên.
2. `REPORT.md:24`: tổng giá niêm yết là $604,6, nên "≥ $605" sai về chữ. Sửa thành "≈ $605 (P3c chỉ có tiến trình cuối)".
3. `REPORT.md:35`: ghi "6 điều phối" nhưng chỉ liệt kê 5 (P4 chạy trong P3c). Sửa thành "5 phiên điều phối (P4 trong P3c)".
4. `check_script.py:386–388`: luật khoảng cách ≥ 180 s giữa mid-roll đang áp cho cả `lab` (2 điểm), trong khi `episode.md:211` không có luật này, và thông báo lại ghi "deep". Sửa: thêm `if FORMAT == 'deep'`, hoặc thêm "cách nhau ≥ 3:00" vào dòng `lab`.
5. `REPORT.md:99`: kết quả thử `deep` có từ trước khi sửa ở lượt 1. Chạy lại và ghi cả lỗi "deep thiếu ACT 4".
6. `episode.md:258`: câu "`KEEP=1` … chỉ cảnh đổi lấy mẫu lại" chưa đúng. Khoá cache hiện gồm cả tệp trang (`sampler.js:6`), nên đổi trang thì lấy mẫu lại cả tập. Thêm "(đầy đủ khi A29 qua K)".
7. `REPORT.md:153` và `:197` mâu thuẫn với `lessons.md:197` T6-12: lessons nói "Chủ dự án xác nhận", còn câu 3 lại hỏi xác nhận. Chủ dự án đã nêu ngày 11/10, nên bỏ câu hỏi ở §5 và mẫu trả lời, giữ trích dẫn.
8. `thumbs/api-*.json`: ảnh được sinh bằng PROMPT cũ (còn "Make them larger and closer…"), còn `rescore.json` không có trường `model` (chạy bằng mã cũ). Ghi một dòng ở §4c/§4f: "ảnh/điểm sinh trước khi sửa mã; chạy lại ở P3 Tập 7".
9. `text.json`, tiêu đề Claude 3 "kept up 17 of 715" thiếu đơn vị, và 17 trường hợp đều bắt đầu 1947–49. REVIEWER G2 cần xem; gợi ý "17 of 715 stretches".
10. `PACKAGING-BRIEF.md:24`: "money stacks" mâu thuẫn với PROMPT cấm "money bill" và với luật vật thể của chính video. Bỏ cụm này.
11. `thumbs.py:67`: nhãn ILLUSTRATIVE chỉ hiện khi có cờ `--character`. Nếu quên cờ thì khung có nhân vật sẽ thiếu nhãn. Sửa: mặc định bật, thêm `--no-character`.
12. `brief.py`: đề tài không tìm thấy thì âm thầm dùng màu thuế `#4C8DFF`. Sửa: in cảnh báo.
13. Prompt `REPORT.md:205–206`:
    - "mục bác → giữ nguyên trạng" không áp được cho mục đã ÁP (T6-12, bộ nhận diện). Thêm "mục đã áp mà bị bác → hoàn lại".
    - Ghi rõ "chạy `verify.sh ep007` sau khi tạo ep007".
14. `REPORT.md:171,176`: (d) chưa có dòng "Được", (g) chưa có dòng "Mất". Thêm cho (d) "Được: tập dài không thêm quãng tĩnh", cho (g) "Mất: $140–240/tháng so với $0".
15. `market/REPORT.md` §4 (dải 15–16 phút so với 12–13) tính khi "Money Rerouted" còn bị xếp là kênh trực tiếp. Thêm vào việc treo T6-12: "tính lại §4 sau khi loại `OWN_CHANNELS`".