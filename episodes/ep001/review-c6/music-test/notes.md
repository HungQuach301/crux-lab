# Thử mù nhạc nền · C6 (30/09/2026)

Ba bản thử ~38 s, cùng một đoạn: **cold open + câu hứa**, 16,7 → 55,2 s của tập (từ ngay trước S01.3 "At the February rate…" tới sau S02.8
"…need a bigger cut?"). Nghe `sample-P.m4a`, `sample-Q.m4a`, `sample-R.m4a`, chọn một bản. **Đừng mở `key.json` trước khi chọn** (khoá giải mã).

Nhãn P/Q/R xáo bằng `secrets.SystemRandom().shuffle`; thứ tự chữ cái không mang nghĩa.

## Giữ nguyên giữa ba bản
- Lời: `review-c4/narration-v32.m4a` (cố định, không đụng).
- Tiếng dữ liệu: bảng S2 "minimal", cùng luật (−16 dB dưới lời, side-chain −8 dB, bỏ 1–4 kHz khi có lời, dời vào khe âm tiết; không nâng mức).
- Mức nhạc dưới lời: bằng mức của bản mix hiện tại ở đúng đoạn này (24,0 dB lời trên nhạc, cách đo A07); không nâng nhạc.
- Duck 1–4 kHz dưới lời, nhạc nhường dải dữ liệu, khoảng lặng [beat] (nhả τ 90 ms, không nốt mới 1,3 s trước khoảng lặng), nhấn ở cú cắt.
- Chuỗi master như C5 (−14 LUFS, TP −1,5 dBTP), rồi chỉ chỉnh gain để ba bản cùng −16,0 LUFS tích hợp; vào 0,25 s, ra 0,6 s.
- Cùng bộ máy nhạc (`mix.py --music-style`), tổng hợp bằng numpy, không mẫu âm thanh; hợp âm Markov không lặp cửa sổ 4 ô nhịp trong 24 ô.
- AAC 192 kb/s, stereo, 48 kHz.

## Số đo từng bản
| Bản | Lời trên nhạc (dB, A07) | LUFS tích hợp (m4a) | True peak (dBTP) |
|---|---|---|---|
| P | 24,0 | −16,0 | −3,4 |
| Q | 24,0 | −16,0 | −3,4 |
| R | 24,0 | −16,0 | −3,4 |

Sau khi chọn: sinh lại nhạc cả tập theo bản chọn, mix lại, chạy lại luật âm thanh; không render lại hình.
