# Lời đọc v3.2 (C4, 29/09/2026)

- Kiểu sinh: **theo cảnh** + 8 thẻ cảm xúc thưa (G-015 · chọn; `story/voice-tags.md`). Eric `cjVigY5qzO86Huf0OWal`, `eleven_v3`, mặc định, không `speed`/voice_settings, seed 1. Mỗi cảnh một lần gọi; không tái dùng take cũ.
- 20 lần gọi, 8.458 ký tự gửi, 3.384 ký tự tính phí. Không sinh lại cảnh nào.
- ASR (faster-whisper small.en): 0 từ khoá mất, trừ S18: "Waltz" và "Angeli's" là ASR viết sai tên đồng âm Walt's/Anjali's; số và câu còn lại khớp. Không sinh lại; chủ dự án nghe ở animatic.
- Sự cố: lúc 14:20 UTC proxy ngắt kết nối ở S14 (ProxyError RemoteDisconnected); container khởi động lại; chạy tiếp bằng `work/v32-voice/src/run_resume.sh`, chỉ sinh các cảnh S14–S20.
- Ghép (`work/v32-voice/src/build.py`): 0,5 s đầu, ~1,4–1,6 s giữa cảnh, 1,0 s cuối; không cắt trong cảnh. Nghỉ trong cảnh là nghỉ tự nhiên của model: 85 chỗ, trung bình 0,83 s, độ lệch chuẩn 0,27 s (bản cũ v3.1 là 0,60 ± 0,06 s). Tổng 9:51,7; −19,5 LUFS, chỉ chỉnh gain.
- Ra: `timeline.json`, `sentences.json` (105 câu), `review-c4/narration-v32.m4a`.
