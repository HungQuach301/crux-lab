# Table read C2 (giọng tạm): ghi chú VOICE

Nguồn: `story/script-v3.md`. Một model `eleven_v3`, một giọng Eric (`cjVigY5qzO86Huf0OWal`, giọng tạm), voice_settings mặc định (không gửi), không `speed`, không "..." hay `<break>`, không giãn/nén, không cắt trong câu (G-010). Khoảng nghỉ do dựng đặt: 0,45 s trong cảnh · 1,0 s ở `[beat]` · 1,4 s giữa cảnh · 2,0 s ở ranh sequence; im lặng số.

- **Tổng thời lượng:** 9:21,2 (561,2 s), gồm 0,5 s đầu và 1,0 s cuối. 109 câu, 1.423 từ đọc (dạng chữ).
- **Âm lượng:** −19,4 LUFS tích hợp, đỉnh mẫu −1,0 dBFS. Chỉ tăng/giảm gain, không nén/limit: kéo lên −16 LUFS thì đỉnh vượt 0 dBFS (hệ số đỉnh của take v3 ~14–17 dB), nên dừng ở đỉnh −1 dBFS. Để khâu mix xử lý.
- **Ký tự EL:** 3.168 ký tự bị tính (header `Character-Cost`); 7.918 ký tự đã gửi (110 lần gọi, gồm 1 lần sinh lại).

## wpm (Tham khảo, không dùng để chọn take)

| Sequence | Bắt đầu | Câu | Từ | wpm lúc nói | wpm tính cả nghỉ |
|---|---|---|---|---|---|
| 0 Cold open | 0:00,5 | 8 | 130 | 184 | 162 |
| 1 Hồi 1 | 0:50,7 | 40 | 516 | 168 | 149 |
| 2 Hồi 2 | 4:20,7 | 22 | 275 | 187 | 160 |
| 3 Hồi 3 | 6:05,8 | 23 | 301 | 180 | 158 |
| 4 Kết | 8:02,4 | 16 | 201 | 177 | 155 |
| Cả tập | | 109 | 1.423 | 177 | 152 |

"wpm lúc nói" = từ / thời lượng take đã cắt đầu-đuôi im lặng. Kịch bản ước 9:10 ở ~150 wpm; bản đọc ra dài 9:21 vì có khoảng nghỉ dựng.

## Sinh lại

- Câu 88 (S17) "Anjali sits at the other end.": take đầu ASR nghe "Angeli" (mất tên riêng, từ khoá). Sinh lại 1 lần, cùng model và thiết lập, seed 2 → ASR nghe đúng "Anjali". Đây có thể chỉ là ASR đánh vần tên lạ (câu 97 take đầu nghe đúng "Anjali"), nhưng luật là mất từ khoá thì sinh lại.
- Không câu nào mất số.

## Chỗ ASR thấy lạ (để WRITER xem chữ, không sửa bằng thủ thuật giọng)

1. Câu 3 (S01) "cut her payment": ASR nghe "cut **our** payment" (xác suất 0,87). Có thể "her" đọc nuốt; nghe lại. Nếu là thật: chữ có thể đổi "cut Nora's payment".
2. Câu 7 (S02, câu hứa) "How big a rate cut": ASR nghe "rake cut" (0,69). "rate cut" đứng liền dễ dính âm; nghe lại ở câu hứa.
3. Câu 45 (S08) "$5,124 divided by $221 is about 24 months": take có chỗ ngắt dài bên trong chuỗi số (≈1,2 s sau "yes", "divided"/"is" kéo dài); câu chậm nhất tập (107 wpm theo ASR). Ba số tiền đọc thành chữ liền nhau trong một câu; WRITER có thể tách câu hoặc bớt một số đọc ra.
4. Số tiền đọc đầy đủ khá dài ("five thousand one hundred twenty-four dollars", xuất hiện 4 lần); "one point six four points", "one point one two points" nghe hơi vụng (chữ "point" lặp). WRITER cân nhắc cách nói ("1.64 percentage points").
5. Câu 92 "$5,250 ahead": ASR ghi "a head" (đồng âm, không lỗi).
6. Tính từ tiền: "$375,000 loan" được gửi TTS là "three hundred seventy-five thousand dollar loan" (sửa từ "dollars loan" của normalize.js; tương tự $115,000, $655,000, "$3,667 bill").

## Clip C2 (`clip-c2.m4a`, 1:18,4)

- Phần 1: 0:00,0–0:49,0 bản đầy đủ (cold open S01 + S02 tới hết câu hứa "…need a bigger rate cut?").
- Nối 1,7 s im lặng.
- Phần 2: 5:36,9–6:04,6 bản đầy đủ (toàn bộ S13, đáp án của Nora: "Somewhere between…" → "Is half a point the line for everyone?").

Take từng câu: `work/c2-voice/cNNN.s1.mp3` (+ `.json` có seed, chữ gửi, header chi phí); câu 88 dùng `c087.s2.mp3`. Tổng 8,3 MB.
