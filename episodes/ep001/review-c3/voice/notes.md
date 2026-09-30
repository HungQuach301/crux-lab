# Thử giọng mù C3 (Tập 1): ghi chú VOICE

Ba bản `voice-A.m4a`, `voice-B.m4a`, `voice-C.m4a`, cùng một đoạn lời, cùng khoảng nghỉ dựng, cùng độ to. Thứ tự A/B/C xáo ngẫu nhiên (`secrets.SystemRandom`). Giải mã ở `key.json`: **không đưa key.json cho người nghe mù**.

- **Đoạn lời:** `story/script-v3.md` (@`3802b4e`), S01 toàn bộ + S02 đến hết câu hỏi thứ nhất ("How big a rate cut makes that worth it for her?"). 7 câu, 119 từ đọc; chữ gửi TTS là bản đã chuẩn hoá của table read C2, không có claim ID.
- **Thời lượng: 47–52 s, không phải ~20 s.** Riêng S01 đã ~80 từ (~30 s); theo luật đã giao ("dài hơn ~25 s thì dùng đến hết câu hỏi thứ nhất của S02") đoạn vẫn dài gần 50 s. Muốn ~20 s thì phải bỏ bớt S01 (ví dụ chỉ S02, hoặc câu 1–3 của S01); chưa làm vì ngoài phạm vi được giao.
- **Khoảng nghỉ (dựng đặt):** đầu 0,5 s · 0,45 s giữa câu · 1,0 s ở mỗi `[beat]` (2 chỗ) · 1,4 s giữa S01 và S02 · cuối 1,0 s.
- **Luật G-010:** mỗi bản một model; không "...", không `<break>`, không giãn/nén; take cắt theo vùng có tiếng ±30 ms, không cắt trong câu. Mỗi câu 1 take; 2 câu (ở 2 bản khác nhau) sinh lại đúng 1 lần vì ASR mất từ khoá hoặc nghe thêm chữ (chi tiết trong key.json).
- **Độ to:** cả ba cùng −20,15 LUFS tích hợp, đỉnh mẫu ≤ −1,0 dBFS. Chỉ tăng/giảm gain, không nén/limit. −19 LUFS không đạt được cho một bản mà vẫn giữ đỉnh ≤ −1 dBFS (hệ số đỉnh lớn), nên cả ba hạ chung xuống −20,15 để bằng nhau.
- **Mã hoá:** AAC 192 kbps, mono, 48 kHz (PyAV; máy không có ffmpeg).
- **ASR (faster-whisper small.en):** cả ba bản đọc đủ mọi số và tên (5.98, September 2022, 2023, 7.62, $459, 7 percent, January 2025, $5,124, "rate cut"). Một bản đọc câu hỏi cuối với ngữ điệu xuống (ASR ghi dấu chấm) — nghe lại xem có mất giọng hỏi không.
- **wpm:** Tham khảo, không dùng để chọn; số từng bản ở key.json. Take, metadata (seed, chữ gửi, Character-Cost) và script dựng: `work/c3-voice/`.

## Quyền giọng (để P2 chép vào `RIGHTS.md`)

- Một trong ba bản dùng **giọng thiết kế riêng** tạo trong phiên này bằng ElevenLabs Voice Design: `POST /v1/text-to-voice/design` (model `eleven_ttv_v3`, mô tả do VOICE viết, không mô phỏng người thật) → chọn 1 trong 3 preview theo luật định trước → `POST /v1/text-to-voice` lưu vào tài khoản với tên `crux-analyst-f1`, category `generated`. voice_id và mô tả đầy đủ trong key.json / `work/c3-voice/design/`. Không có mẫu giọng người thật nào được tải lên (không phải clone).
- Hai bản kia dùng giọng thư viện premade **Eric** của ElevenLabs (như table read C2).
- Điều khoản: VOICE **chưa đọc trực tiếp** điều khoản ElevenLabs trong phiên này (chưa trích được nguyên câu). Theo hiểu biết chung: giọng tạo bằng Voice Design thuộc tài khoản tạo ra nó, dùng thương mại được với gói trả phí, và không nằm trong Voice Library trừ khi chủ tài khoản chia sẻ. **P2 cần mở ElevenLabs Terms of Service / Prohibited Use Policy, trích nguyên câu về quyền sử dụng đầu ra và giọng generated, và ghi gói tài khoản** trước khi đưa vào `RIGHTS.md`. Đổi giọng là quyết định `irreversible` (voice-spec).
- Không xoá giọng nào khỏi tài khoản.

## Ký tự ElevenLabs

1.157 ký tự bị tính (header `Character-Cost`), 2.905 ký tự đã gửi: ba bản 851 (gồm 2 lần sinh lại) + hiệu chuẩn tốc độ 306 (3 câu ngoài đoạn thử × 3 mức speed). Voice Design (1 lần thiết kế + 1 lần lưu) không trả header chi phí; chưa rõ có trừ credit không.
