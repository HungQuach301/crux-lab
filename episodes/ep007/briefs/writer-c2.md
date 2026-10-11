Bạn là WRITER của Crux (kênh YouTube tài chính cá nhân Mỹ, không lộ mặt, "phòng thí nghiệm quyết định": phát lại lịch sử thật). Viết kịch bản C2 Tập 7 bằng tiếng Anh Mỹ. Không dùng agent con. Không commit. Chỉ ghi vào `episodes/ep007/story/` (script.md, beats.md, hooks.md, và sửa các dòng `# TẬP:` của check_script.py). Mỗi lệnh Bash là MỘT lệnh `python3 …` (không `cd`, không `&&`, không `;`, không pipe).

## Đọc trước (theo thứ tự)
1. `playbook/story.md` (toàn bộ — luật truyện, năm luật nhân vật §2b, khuôn `lab` §4).
2. `playbook/episode.md` §3 (đầu bài WRITER: ASR, claim-risk, móc M1–M6, hồ sơ cầu mục 11, video neo mục 12) và §9 (format `lab`: 9–11 phút, 2 mid-roll ở ranh giới hồi).
3. `episodes/ep007/numbers.md` — **mọi số đọc lên hoặc hiện trên hình phải là một claim ở đây, đúng cột Hiển thị**; luật nói ở đầu tệp.
4. `topics-r2/machine/debt-1/claim-risk.md`, `card.json`.
5. `market/topics/q13-15-vs-30-mortgage.md` (hồ sơ cầu: câu hỏi khán giả, hoàn cảnh, điểm yếu đối thủ) và `tongket-t6/anchors/q13-15-vs-30-mortgage.json` (video neo + khoảng trống).
6. `episodes/ep007/gates/C1-logline.md` (logline L1 đã chọn).
7. `taste-ledger.md` các dòng G-007…G-016; `toolkit/visual-library/README.md` (thư viện hình V*, W*; thế giới 3D tối giản D-010: low-poly, màu kênh, nhân vật không mặt, không chi tiết trang trí).
8. Mẫu định dạng (KHÔNG chép câu chữ): `episodes/ep006/story/script.md` (đầu tệp + vài chục dòng), `episodes/ep006/story/beats.md` (đầu bảng), `episodes/ep006/story/hooks.md` (một phương án).

## Tập
- **Format `lab`, đích ≈ 10:40 ước** (≈ 1.510–1.570 từ nói ở 2,40 từ/s; tối đa cứng 11:00 = 660 s, tối thiểu 540 s). Chủ dự án: "lab 11 phút". Không độn: mỗi phút phải mang claim mới hoặc câu hỏi khán giả được trả lời.
- **Logline L1** (C1). Quyết định: vay $320,000 tuần 2026-10-08 — khoản 15 năm 6.73% hay khoản 30 năm 7.40% trả hết trong 15 năm (giữ khoản trả tối thiểu thấp hơn làm đường lui). Đáp án: (a) **giá bằng đô la của đường lui** — $120 a month, $21,622 over 15 years ở tuần này; lịch sử 1.833 tuần từ 1991: từ $6,097 (Dec 2008) đến $29,502 (Jan 2023), trung vị $16,631; tuần này đắt hơn 81% số tuần (share_extra_ge_now); (b) **câu hỏi khán giả 1 "trả thêm hay đầu tư"**: mỗi đô la gốc trả thêm "được" đúng lãi khoản vay (lãi không còn phải trả, trước thuế) = **mốc mà mọi cách dùng tiền khác phải vượt** (bar_now 7.40%); lịch sử mốc: 2.65% (Jan 2021) đến 9.25% (Nov 1994); chỉ ≈ 1 tuần trong 5 từ 1991 có mốc cao bằng tuần này. KHÔNG nói đầu tư thắng/thua, không lợi suất thị trường nào (không có claim), không khuyên.
- **Nhân vật (ILLUSTRATIVE, nhãn ở mọi khung có người):** dẫn đường **Tessa** (gợi ý; tên KHÔNG được trùng BANNED_NAMES trong check_script.py) — dựng từ hoàn cảnh 2 của hồ sơ cầu (người mua ở đô thị đắt đỏ, khoản trả tháng lớn, tự hỏi trả 15 năm có thực tế không), vay $320,000 tuần này. Đối trọng ở hồi 3: **Leo** — khoá 30 năm tuần Jan 2021 ở 2.65% (claim leo_*): đường lui rẻ hơn ($13,231) nhưng mốc trả thêm chỉ 2.65%. Cùng một lựa chọn, ý nghĩa khác theo tuần khoá lãi.
- **Câu hỏi khán giả phải trả lời ≥ 3/5** (ghi câu nào ở cảnh nào trong beats.md): Q1 (mốc = lãi khoản vay), Q2 (trả đúng khoản 15 năm trên khoản 30 năm → hết sau ≈ 195 tháng, trễ ≈ 15 tháng; muốn đúng 15 năm cần trả thêm $733 a month), Q3 (trả thêm một lần mỗi năm $8,792 thay vì hằng tháng → 184 tháng, lãi nhiều hơn ≈ $8,166). Q5 tuỳ chọn (không thêm số mới).
- **Lịch sử theo thời kỳ** (era*_median_*): 1990s, 2000s, 2010s, 2020s — đường lui đắt nhất ở hai thập niên gần đây vì chênh lãi rộng hơn (≈ 0.7 điểm so với ≈ 0.45). Chênh 30−15 năm dao động 0.2–1.0 điểm, trung bình 0.57 — **không bao giờ nói "luôn 0.6"**.
- **Điểm yếu đối thủ (một nhịp, không nêu tên kênh):** video thường coi trả sớm là mặc định tốt và dùng một lãi giả định cố định — tập đặt khoản 15 năm THẬT cạnh khoản 30 năm trả trong 15, trên mọi tuần lãi thật.
- **Video neo** (episode.md §3.12): lời hứa trong 30 s đầu trả lời đúng câu hỏi "30-year mortgage paid in 15 vs a 15-year"; một nhịp lấp khoảng trống "không đặt khoản 15 năm thật cạnh khoản 30 năm; không có lịch sử lãi thật".
- **Hình:** thế giới 3D tối giản (D-010). Gợi ý vật thể trung tâm (một vật xuyên tập, tên gọi cố định trong lời và trên hình, ví dụ "a stack of bills" cho $21,622, hoặc "the bar" — thanh ngang cao bằng lãi — cho mốc trả thêm); ưu tiên thư viện; mỗi ký hiệu mới ghi lý do + "new symbol" trong beats.md (→ C3). Ghi rõ TÊN vật thể trung tâm ở đầu beats.md (dùng cho ý tưởng thumbnail G1: chữ + vật thể).
- **Mid-roll:** 2 điểm, ở ranh giới hồi, sau hold ≥ 1 s, ≥ 120 s từ đầu và cuối.
- **Gen bắt buộc:** "US only", "history, not a forecast", ILLUSTRATIVE, "we" chỉ người phân tích, không khuyên, không mệnh lệnh, không dự báo lãi.

## Ra
1. `story/script.md`: đầu tệp (tóm tắt, nhân vật, số cốt lõi, claim-risk áp ở đâu, câu đỉnh ≤ 15 từ `{peak}`, câu kết là câu của Tessa trả lời câu hỏi của cô ở cold open), rồi các dòng `Sxx.n {role} [emotion] narration <!-- claims: id, id; hold: s -->`, chia phần bằng tiêu đề `## COLD OPEN`, `## ACT 1`, `## ACT 2`, `## ACT 3`, `## LIMITS` như mẫu Tập 6; mid-roll đánh dấu như mẫu.
2. `story/beats.md`: bảng nhịp theo mẫu Tập 6 (loại 1/2, "muted read", V-id, new symbol, chữ trên hình trong ngoặc kép, claims), câu hỏi khán giả ở cảnh nào.
3. `story/hooks.md`: **3 phương án 30 s đầu, ba kiểu móc khác nhau** (`playbook/packaging.md` §2), mỗi phương án nối vào phần chung; ghi phương án đã dùng trong script.md.
4. `story/check_script.py`: sửa dòng `# TẬP:` (CAST, CORE, FULL_FORM, WORD_EXEMPT) rồi chạy `python3 episodes/ep007/story/check_script.py episodes/ep007/story/script.md --cast Tessa,Leo` cho tới khi **ĐẠT** (exit 0); dán đầu ra cuối vào đầu script.md. Tối đa 6 lượt sửa; vẫn trượt → để nguyên và báo.
Trả về (≤ 15 dòng): ĐẠT/TRƯỢT checker; độ dài ước; M1–M6; mid-roll; câu hỏi khán giả đã trả lời (số, cảnh); vật thể trung tâm; danh sách hình mới (→ C3: có/không); 3 móc (một dòng mỗi cái, cái đã dùng); câu đỉnh; câu kết.
