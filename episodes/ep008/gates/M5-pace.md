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

Kết quả vòng 1: (điền sau khi dựng — `review-m5/pace-r1*.json`).
