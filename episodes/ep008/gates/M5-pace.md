# M5 Tập 8 — nhịp (vai Editor) trên nháp 540p màu: số đo + vòng sửa

Thước ghi trước (`gates/M5-intent.md` §4 + C5/P7, `playbook/episode.md` §1a): **quãng có lời không đổi hình > 8 s = 0** (spine `f14`, `spine.check_f14` (b)) · **freezedetect ≥ 3 s có lời ≤ 30 s/tập** · kiểm mù "chỗ muốn tua" (đo sau). Sửa ≤ 2 vòng, ở nhịp/hình, không đổi lời. Công cụ: `prod/pace.py <video> [stem] [n]` ("có lời" = giọng > −45 dBFS, silencedetect d = 0,3 s).

## Nháp c1 (màu, trước sửa) — TRƯỢT

| Thước | animatic xám r2 | nháp màu c1 | Ngưỡng |
|---|---|---|---|
| freezedetect n = 0,003 (ghi trước) ∩ lời | 294,8 s | **281,6 s** | ≤ 30 s |
| freezedetect n = −60 dB (cách đo `qc.py` / F-14) ∩ lời | 223,8 s | **212,0 s** | ≤ 30 s |
| spine: quãng có lời > 8 s không major | — | **9** (b 1 · c 2 · d 3 · f 3) | 0 |

Phân bố 212 s (−60 dB) theo tư thế máy: **đồ thị ≈ 146 s** (cGrid 76 · cIdx 16 · cDots 13 · cStacks 12 · cRecord 10 · cDark 9 · cBright 7 …), thế giới ≈ 66 s. Gốc: máy chỉ chạy trong cửa sổ động tác hữu hạn (quy tắc 3) rồi đứng; vật dữ liệu đứng khi không có từ khoá; chưa có `life` (F-14 (a)).

## Vòng 1 (14/10, commit c034b0cc) — "đổi vì thước" (ghi đích danh theo bài học F-14 v4)

1. **Máy tiến chậm khi đứng** (`w8.js` setup, `kit.HOLD_PUSH`): giữa hai động tác, máy tiến về điểm nhìn — thế giới 0,8 %/s ≤ 8 % khoảng cách, đồ thị 0,2 %/s ≤ 1,2 % (nhãn đồ thị sát dòng chrome: lệch ≤ 6 px ở 1080p; thử 5–11 % làm "January 1991" và "rent" chạm dòng "US only" → bỏ); đứng yên ±pad quanh mọi từ khoá (quy tắc 2 giữ, R07 không bị nền trôi); vào động tác kế k về 0 theo ease → tư thế đích, nhật ký máy (`log.cam`) là máy thật. Nghĩa: đẩy chú ý vào vật đang nói; không mang giá trị dữ liệu.
2. **9 quãng > 8 s** — mỗi quãng một thay đổi major ở từ MỞ ý (không đổi lời):
   - b S05.6 "costs": đẩy lại gần hộp tiền mặt + thẻ (`wBox~`, 90 %).
   - c S09.1 "how": đẩy lại gần dãy nhà đầu phố; S09.3 "Prices": lùi thấy dãy sáng tiếp.
   - d S18.1 "pair": hai chồng (vốn người mua / tiền mặt người thuê) **mọc từ "a pair of stacks"**, đủ giá trị trước nhãn số (F-14 (d)); S19.3 "worse": `m_grid` (chỉ số → cả lưới, đổi hẳn nội dung khung) bắt đầu ở cuối câu thay vì sát câu hỏi + khai major; S21.2: nhãn neo "Five" (từ mở câu) thay "little".
   - f S30.1 "rent": **vạch mức $1,667 kéo ngang sang chồng người mua** (đọc được tỉ lệ trước nhãn 56.8 %); S30.3 "and": nhãn "lowest replayed … July 2006" mờ còn 40 % khi lời nói "không biến 2026 thành 2006"; `m_grid` (chấm → cả lưới) khai major.
   - Spine sau sửa: 0 quãng > 8 s, quy tắc 2/3/7 OK cả 6 đoạn.

**Kết quả vòng 1** (`work/animatic/draft-r1.mp4`, `review-m5/pace-r1*.json`; container khởi động lại giữa chừng → đoạn d–f dựng lại, cùng mã):

| Thước | c1 | **r1** | Ngưỡng |
|---|---|---|---|
| freezedetect n = 0,003 (ghi trước) ∩ lời | 281,6 s | **67,9 s** — TRƯỢT | ≤ 30 s |
| freezedetect −60 dB (`qc.py`/F-14) ∩ lời | 212,0 s | **6,4 s** — đạt | ≤ 30 s |
| spine: quãng có lời > 8 s không major | 9 | **0** — ĐẠT | 0 |
| quãng đứng hình có lời > 8 s (freezedetect) | 1 | 0 | — |

67,9 s còn lại **toàn ở quãng đứng đồ thị** (21 quãng: cDots 13,8 · cIdx 10,6 · cRecord 10,0 · cStacks 10,0 · cGrid 8,9 · cDark 6,5 …): quãng đồ thị dài 17–50 s, trần 1,2 % trải một chiều → ≈ 0,05–0,12 %/s, quá chậm cho n = 0,003 trên đồ thị thưa (nét mảnh, nền tối). Thước ghi trước giữ nguyên (không đổi sang −60 dB sau khi thấy số); cả hai số nêu ở G2.

## Vòng 2 (cuối, 14/10) — "đổi vì thước"
Đồ thị: k **thở** tam giác 0 ↔ 2,5 % ở 0,5 %/s (thử trên quãng cIdx 47–66 s: 1,2 % ở 0,3 %/s còn một quãng 4,0 s; 2,5 % ở 0,5 %/s: 0). Khung đỉnh (2,5 %) soát tay: "January 1991" còn trên dòng chrome; "rent"/"buyer's first month" sát dòng chrome như bản c1 (verify F-2 báo nếu chạm). Nghĩa: không có — đây là chuyển động để qua thước, nêu đích danh ở G2; cổng gốc (chẩn đoán) soát nghĩa.

Dựng lần 1 vòng 2: verify **F-2 CHẶN** "rent" × dòng chrome ở cStacks (đoạn a 10 mẫu, f 88 mẫu) → trần riêng cStacks 1,2 % (`HOLD_PUSH.caps`, bản r1 không chạm), dựng lại a, f: verify OK (không F-2 mới so với r1).

**Kết quả vòng 2** (`work/animatic/draft-r2.mp4` = nháp G2, `review-m5/pace-r2*.json`):

| Thước | c1 | r1 | **r2** | Ngưỡng |
|---|---|---|---|---|
| freezedetect n = 0,003 (ghi trước) ∩ lời | 281,6 s | 67,9 s | **0 s — ĐẠT** | ≤ 30 s |
| freezedetect −60 dB ∩ lời | 212,0 s | 6,4 s | **0 s** | ≤ 30 s |
| spine: quãng có lời > 8 s không major | 9 | 0 | **0 — ĐẠT** | 0 |

Hai thước máy của Editor ĐẠT sau 2 vòng (hết vòng). Cái giá cần chủ dự án nhìn ở G2: máy **không bao giờ đứng hẳn** — thế giới tiến chậm ≤ 8 %, đồ thị thở 0 ↔ 2,5 % (cStacks 1,2 %); phần "thở" là chuyển động không mang nghĩa, chỉ để qua thước (bài học F-14 v4: soát nghĩa ở cổng gốc). Kiểm mù "chỗ muốn tua" chạy trên r2 (`prod/recall.py`).

## Vòng hình "chỗ muốn tua" r3 (14/10, sau REVIEWER G2 lượt 1) — KHÔNG GIỮ
Ý đồ C5: kiểm mù "chỗ muốn tua" trượt → sửa ≤ 2 vòng ở nhịp/hình. r2: S06 3/3; S04 S07 S20 S21 S22 S31 2/3. Vòng 1: S07.3 `wFlow` cận thẻ 5 % trên cửa (fov 42 → 22, máy cao để đầu người song sinh không che thẻ) — đạo diễn: thẻ không đọc được ở 177 s. Dựng lại đoạn b (verify OK, F-2 không mới) + ghép; freezedetect ∩ lời trên r3: 0 s (`review-m5/pace-r3.json`). Kiểm mù 3 người đọc mới (`review-m5/r3/tally.md`): **S05 3/3, S06 3/3, S04 2/3, S07 2/3** → TRƯỢT, **không vượt r2** (S07 vẫn 2/3; S05 lên 3/3) → theo §6 ("vòng chỉ giữ khi vượt bản tốt nhất ngoài biên nhiễu") **hoàn về r2**; G2 gửi r2. Lý do từng người (r3): R1 1:23–3:03 "định nghĩa và lưu ý trước khi có kết quả"; R2 1:56–3:04 "danh sách mỗi người trả + giải thích thẻ tiền thuê"; R3 1:01–2:23 "mỗi người trả + đoạn tốc độ tăng". Vòng 2 không chạy (bên dựng dừng ở 1/2 vòng) — G2 nêu lệch.
