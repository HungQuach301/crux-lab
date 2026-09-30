# Lời đọc cả tập v3.1 (C4): ghi chú VOICE

Nguồn: `story/script-v3.1.md` (câu hứa ghép ở S02). Giọng chốt ở C3 (sổ gu "G-010 · chọn"): Eric (`cjVigY5qzO86Huf0OWal`), **`eleven_v3`**, voice_settings mặc định (không gửi), không `speed`, không "..." hay `<break>`, không giãn/nén, không cắt trong câu. Mỗi câu 1 take; sinh lại tối đa 1 lần (seed 2) chỉ khi ASR thấy mất từ khoá, sai số hoặc sai tên.

Nghỉ do dựng (mặc định để C4 chỉnh theo hình): 0,45 s giữa câu · 1,0 s ở `[beat]` · 1,4 s giữa cảnh · 2,0 s ở ranh sequence; 0,5 s đầu, 1,0 s cuối; im lặng số.

- **Tổng thời lượng:** 9:43,0 (583,0 s). 105 câu, 1.503 từ đọc (dạng chữ). (C2: 9:21,2, 109 câu.)
- **Câu:** 23 mới · 82 tái dùng take C2 (chữ gửi TTS trùng từng ký tự với C2; take C2 cũng là Eric eleven_v3 mặc định) · 1 lần sinh lại (câu 91, không thay take).
- **Âm lượng:** −19,5 LUFS tích hợp (trước gain −18,9), đỉnh mẫu −1,2 dBFS. Chỉ gain, không nén/limit.
- **Ký tự EL:** **1.013** ký tự bị tính (header `Character-Cost`); 2.530 ký tự đã gửi, 24 lần gọi (23 câu mới + 1 lần sinh lại). Tái dùng 82 câu tránh gửi lại 5.840 ký tự (≈ 2.338 ký tự bị tính theo giá C2).
- **Bản ghép:** `review-c4/narration.m4a` (AAC ~96 kbps, mono, 48 kHz). Lời thuần: `review-c4/transcript.txt`. Mốc từng câu và nghỉ: `timeline.json`. Chi tiết từng câu: `sentences.json`. Take: `work/v31-voice/vNNN.s1.mp3` (mới), `vNNN.c2-cMMM.sK.mp3` (bản sao take C2), mỗi take có `.json` (chữ gửi, seed, chi phí). Mã: `work/v31-voice/src/` (parse, gen, build).

## Tái dùng

Câu mới (23): 6–8 (S02, gồm câu hứa), 9–10 (S03), 11–12 (S04), 19–20 (S05), 24 (S06), 27 (S07), 45–46, 50–51 (S10), 56–57 (S11), 90–95 (S18). Mọi câu còn lại tái dùng take C2 cuối (câu 82 "Anjali sits at the other end." dùng `c087.s2`, take đã sinh lại ở C2). Danh sách đầy đủ: trường `source`, `c2_n`, `c2_take` trong `sentences.json`.

## wpm (Tham khảo, không dùng để chọn take)

| Sequence | Bắt đầu | Câu (mới/tái dùng) | Từ | wpm lúc nói | wpm tính cả nghỉ |
|---|---|---|---|---|---|
| 0 Cold open | 0:00,5 | 8 (3/5) | 143 | 176 | 158 |
| 1 Hồi 1 | 0:56,9 | 32 (8/24) | 457 | 168 | 150 |
| 2 Hồi 2 | 4:01,9 | 24 (6/18) | 334 | 190 | 165 |
| 3 Hồi 3 | 6:05,3 | 23 (0/23) | 301 | 180 | 158 |
| 4 Kết | 8:01,9 | 18 (6/12) | 268 | 180 | 161 |
| Cả tập | | 105 (23/82) | 1.503 | 178 | 155 |

"wpm lúc nói" = từ / thời lượng take đã cắt (đoạn có tiếng +40 ms / +120 ms). "Cả nghỉ" = từ đầu câu đầu đến cuối câu cuối của sequence.

## Sinh lại

- Câu 91 (S18) "On a loan of $115,000, like Walt's, it takes more than a full point.": seed 1 ASR nghe "like **Waltz**" (mất tên). Sinh lại 1 lần seed 2 → vẫn "Waltz". Giữ seed 1 (không bớt lỗi). Nhiều khả năng ASR viết "Walt's" thành "Waltz" (đồng âm); các câu "Walt" khác đều nghe đúng. Cần nghe lại.
- Không câu nào sai số.

## Chỗ ASR thấy lạ (để nghe lại / WRITER xem chữ; không sửa bằng thủ thuật giọng)

1. Câu 7 (S02, câu hứa) "where does **a loan your size** fall?": ASR nghe "where does **alone** your size fall". "a loan" dính âm thành "alone"; nghe lại ở câu hứa.
2. Câu 10 (S03) "She was far from **alone**": ASR nghe "far from **a loan**" (đồng âm ngược lại). Trong tập về khoản vay, người nghe có thể nghe nhầm như ASR; WRITER cân nhắc chữ khác (vd. "Many others had done the same").
3. Câu 12 (S04) "She had moved": ASR nghe "She'd moved" (TTS có thể tự rút gọn; không đổi nghĩa).
4. Nhanh (Tham khảo): câu 94 "Put your own loan on that scale, and you can see which of them you are closest to." 3,6 s ≈ 298 wpm; câu 90 "It depends on the size of the loan." 1,8 s ≈ 265 wpm; câu 50–51 (S10, giải thích khe dư nợ) 221–233 wpm. Không sinh lại (luật chỉ cho sinh lại vì mất từ khoá); nếu nghe thấy vội, C4 nới nghỉ quanh câu, không giãn.
5. Từ C2 còn giữ vì tái dùng: câu 3 "cut **her** payment" ASR nghe "our"; câu 37 "$5,124 divided by $221…" có ngắt 1,2 s sau "yes" (104 wpm); câu 86 "$5,250 ahead" → "a head" (đồng âm).
6. Nghỉ trong câu ≤ 0,8 s ở mọi câu mới (dấu hai chấm, gạch ngang, dấu phẩy); không có "..." hay kéo dài giả.
