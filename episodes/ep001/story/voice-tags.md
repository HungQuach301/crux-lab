# Tập 1 — Thẻ cảm xúc cho lời đọc (v3.2)

WRITER C4, 29/09/2026. Theo quyết định của chủ dự án sau thử giọng mù C4: chọn bản Y (sinh theo cảnh, eleven_v3, giọng Eric; thẻ cảm xúc thưa, chỉ ở nhịp then chốt, không thẻ ngắt/nghỉ). Thẻ nằm trong `script-v3.2.md`, đầu dòng lời mà nó tô màu. Thẻ gửi cho eleven_v3, không đọc thành tiếng, không hiện trên màn hình.

**Đây là đề xuất.** Chủ dự án xem vị trí khi nghe animatic C4 và có thể bỏ hoặc thêm thẻ. 4 thẻ đánh dấu **Y** là 4 thẻ đã nghe trong bản thử Y (`review-c4/voice-test/key.json`), giữ đúng vị trí; 4 thẻ còn lại là thẻ mới, chưa nghe thử.

Tổng: 8 thẻ / 20 cảnh; 7 cảnh có thẻ (S10 có 2), 13 cảnh không có.

| Cảnh | Thẻ | Câu (đầu câu) | Lý do: nhịp phải cảm thấy thế nào | Nguồn |
|---|---|---|---|---|
| S01 | `[softly]` | "She didn't take it." | Nhẹ, gần như tiếc; cơ hội đã trôi qua, để lặng xuống trước khi lãi quay lên. | **Y** |
| S02 | `[curious]` | "How big a rate cut makes that worth it for Nora…" | Câu hứa phải lên giọng hỏi thật, kéo người xem vào câu hỏi của chính họ. | **Y** |
| S10 | `[thoughtful]` | "If she sold the house then, …" | Chậm lại để suy: khe dư nợ $1,133 là chi phí thật, người xem cần theo kịp lý lẽ. | **Y** |
| S10 | `[serious]` | "Count it, and break-even moves from month 24…" | Kết luận chắc, nặng: tháng 24 thành tháng 30 là điểm xoay của hồi 2. | **Y** |
| S13 | `[warmly]` | "So for Nora, the answer is half a point…" | Đáp án cho Nora: nhẹ nhõm, ấm, như trả lời một người quen; không reo. | mới |
| S16 | `[serious]` | "So that is why a smaller mortgage needs a bigger rate cut." | Điểm lật của tập (vế thứ hai câu hứa): nói rõ, dứt khoát, không kịch hoá. | mới |
| S18 | `[matter-of-fact]` | "It depends on the size of the loan." | Mở thước ba mốc bằng giọng thẳng, như đọc một sự thật; ba mốc theo sau giữ cùng giọng. | mới |
| S20 | `[softly]` | "How long do you picture yourself in your home?" | Câu hỏi ở lại với người xem; nhẹ, riêng tư, vọng lại S01 (mở và đóng cùng `[softly]`). | mới |

Không dùng: thẻ ngắt/nghỉ (`[pause]`, `<break>`), "...", từ chỉnh tốc độ, thẻ âm thanh, `[laughs]`, `[whispers]`, la hét. Khoảng nghỉ vẫn do `[beat]` và dựng quyết định như v3.1.

**Lưu ý cho VOICE:** `work/v31-voice/src/parse.py` bỏ mọi `[chữ_số_gạch_dưới]` như claim ID, nên sẽ lặng lẽ xoá 7 thẻ và để lọt `[matter-of-fact]` (có gạch nối) vào chữ đọc. Khi sinh từ v3.2 cần tách thẻ cảm xúc trước (danh sách ở bảng trên), bỏ claim ID, rồi gắn lại thẻ vào đầu câu đã chuẩn hoá.
