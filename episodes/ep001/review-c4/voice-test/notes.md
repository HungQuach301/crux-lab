# Thử giọng mù C4 (Tập 1, G-015): ghi chú VOICE

Ba bản `sample-X.m4a`, `sample-Y.m4a`, `sample-Z.m4a`: cùng một đoạn lời, cùng giọng, cùng model, cùng độ to. Thứ tự X/Y/Z xáo ngẫu nhiên bằng `secrets.SystemRandom` so với ba cách làm (V1/V2/V3 trong sổ gu G-015). **Người nghe mù không mở `key.json` và không mở `episodes/ep001/work/voice-test/`** (tên take ở đó lộ cách làm). Giải mã và mọi số đo từng bản nằm trong `key.json`.

## Đoạn lời

`story/script-v3.1.md` (@`4f0edb3`), 12 câu, 12 câu này ở cả ba bản giống hệt nhau từng chữ:

- **S01** cả cảnh (cold open, 5 câu: "In February 2026…" → "…since January 2025.").
- **S02** cả cảnh, **câu hứa mới**: "How big a rate cut makes that worth it for Nora — and where would your own loan fall?" / "And why would a smaller mortgage need a bigger cut?"
- **S10**, đoạn "$1,133" → "month 30" (4 câu: "By month 24, she owes $1,133 more…" → "Count it, and break-even moves from month 24 to month 30.").

Chữ gửi TTS được chuẩn hoá như bản đọc v3.1 (số đọc thành chữ).

## Giống nhau ở cả ba bản

- Eric (`cjVigY5qzO86Huf0OWal`), `eleven_v3`, không gửi voice_settings, không gửi `speed`, `output_format` mp3_44100_128. Không "...", không `<break>`, không thẻ ngắt/nghỉ/tốc độ, không giãn/nén.
- Mỗi bản sinh 1 lần, không chọn take theo tai. ASR (faster-whisper small.en) nghe đủ mọi số, tên và từ khoá ở cả ba bản, nên **không bản nào sinh lại**.
- Dựng: 0,5 s đầu, 1,0 s cuối, 1,4 s im lặng giữa hai cảnh ở cả ba bản. Cắt đầu/đuôi im lặng như v3.1 (−50 dBFS, +40/+120 ms), không cắt giữa câu.
- Độ to: chỉ gain, cả ba −19,5 LUFS tích hợp, đỉnh mẫu ≤ −1,2 dBFS. Không nén, không limit.
- Mã hoá: AAC 192 kbps, mono, 48 kHz (PyAV, máy không có ffmpeg).
- Thời lượng: 83–91 s. Bản dài nhất là 90,6 s, trong đó có 1,5 s lặng ở đầu và cuối, nên phần lời 89,1 s, nằm trong giới hạn 90 s. Vì vậy không bỏ bớt S01.

## Nghe gì

Nghe cả ba từ đầu đến cuối, theo thứ tự nào cũng được. Câu hỏi: **bản nào nghe như một người kể chuyện có nhấn nhá, không đều đều?** Nên nghe kỹ ở ba chỗ: "She didn't take it.", câu hứa, và câu "month 30". Chọn xong thì mở `key.json`. Theo G-015, cách được chọn sẽ dùng để sinh lại **cả tập theo một kiểu duy nhất**, không trộn take của kiểu khác.

## Ghi chú kỹ thuật

- `previous_text`/`next_text` (tham số ngữ cảnh của API) **không dùng được với `eleven_v3`**. Gọi thử trả về HTTP 400 `unsupported_model`: "Providing previous_text or next_text is not yet supported with the 'eleven_v3' model." (0 ký tự bị tính). Việc này không ảnh hưởng đến đoạn thử, vì mỗi cảnh ≤ 491 ký tự, dưới giới hạn 5.000 ký tự/lần. Với cả tập, cảnh dài nhất cũng dưới giới hạn, nên không phải tách cảnh.
- elevenlabs.io (tài liệu) bị proxy chặn. Danh sách thẻ cảm xúc hợp lệ được đọc gián tiếp qua kết quả tìm kiếm (blog "Audio Tags 101", trang help "How do audio tags work with Eleven v3?").
- Ký tự ElevenLabs: **1.045** ký tự bị tính (header `Character-Cost`), 2.611 ký tự đã gửi, 7 lần gọi thành công, cộng 1 lần gọi thử bị từ chối (9 ký tự, không bị tính).
- Mã và take nằm ở `episodes/ep001/work/voice-test/` (`src/gen.py`, `src/build.py`, `src/prosody.py`). Chẩn đoán nguyên nhân gốc: `../voice-rootcause.md`.
