# Giọng đọc "đều đều": tìm nguyên nhân gốc (Tập 1, C4, G-015)

VOICE, 29/09/2026. Mọi số dưới đây là **số đo trên file âm thanh**, không phải ước đoán. Mã đo nằm ở `episodes/ep001/work/voice-test/src/prosody.py` và `rootcause.py`; số thô ở `work/voice-test/rootcause.json`.

**Cách đo:**

- **Cao độ (F0):** tính bằng pyworld Harvest (60–300 Hz, khung 5 ms), đổi ra semitone (st) so với 100 Hz.
- **Năng lượng:** RMS khung 10 ms, chỉ tính các khung nằm trong 35 dB dưới đỉnh của câu.
- **Cuối câu lên hay xuống:** so trung vị cao độ của 250 ms có tiếng cuối cùng với đoạn 250–750 ms ngay trước đó. Chênh hơn +1 st là "lên", dưới −1 st là "xuống", còn lại là "ngang".
- **Khuôn chung:** mỗi câu lấy đường nét cao độ 50 điểm, trừ trung bình. Chỉ số là tương quan trung bình giữa mọi cặp câu. Số càng cao, các câu càng lặp cùng một khuôn.
- **Nghỉ:** mọi khoảng lặng dài từ 120 ms trở lên, với ngưỡng lặng là p95 khung trừ 40 dB.
- **Tốc độ nói:** số từ chữ đọc chia cho thời lượng phần có tiếng của câu.

## 1. Bản chủ dự án thích (giọng B, C3) và bản cả tập v3.1, trên cùng đoạn lời

So `review-c3/voice/voice-B.m4a` (7 câu, 47 s) với 7 câu đầu của `review-c4/narration.m4a`: S01 và S02 tới hết câu hứa thứ nhất.

| Số đo (7 câu) | Giọng B (C3) | v3.1 cùng đoạn |
|---|---|---|
| Độ lệch chuẩn F0, cả đoạn | 4,04 st | 3,95 st |
| Dải F0 p5–p95, cả đoạn | 13,3 st | 12,5 st |
| Dải F0 trung bình mỗi câu | 12,3 st | 12,2 st |
| Độ lệch chuẩn F0 trung bình mỗi câu | 3,71 st | 3,84 st |
| Độ lệch chuẩn giữa cao độ trung bình các câu (biến thiên theo đoạn) | 1,18 st | 1,10 st |
| Độ lệch chuẩn cao độ đầu câu | 2,92 st | 2,08 st |
| Độ lệch chuẩn năng lượng trong câu (trung bình) | 8,28 dB | 8,12 dB |
| Tương quan khuôn giữa các câu | 0,12 | 0,18 |
| Cuối câu lên / ngang / xuống | 1 / 0 / 6 | 0 / 1 / 6 |
| Tốc độ khi nói | 175 từ/phút | 174 từ/phút |
| Khoảng lặng ≥ 120 ms: trung vị / trung bình | 0,40 / 0,48 s | 0,49 / 0,52 s |

**Câu hỏi của câu hứa là chỗ khác nhau rõ nhất:**

- Giọng B đọc câu hứa cũ, ngắn: "How big a rate cut makes that worth it for her?". Cuối câu lên +3,3 st, tốc độ 268 từ/phút. Đây là câu duy nhất lên giọng trong bản B.
- v3.1 đọc câu hứa ghép: "…for Nora — and where does a loan your size fall?". Cuối câu xuống −2,9 st. Câu hỏi thứ hai ("And why would a smaller mortgage need a bigger cut?") xuống −12,4 st.

**Cùng chữ, khác seed.** Năm câu S01 được gửi TTS giống nhau từng ký tự ở hai lượt: C3 dùng seed 11, còn v3.1 dùng lại take C2 seed 1. Dải F0 từng câu:

| Câu | Seed 11 | Seed 1 |
|---|---|---|
| 1 | 14,2 st | 13,5 st |
| 2 | 13,4 st | 11,6 st |
| 3 | 12,5 st | 10,3 st |
| 4 | 8,3 st | 11,4 st |
| 5 | 11,0 st | 13,1 st |
| Trung bình | 11,9 st | 12,0 st |

Chênh lệch từ câu này sang câu khác (±2–3 st) đi theo cả hai chiều, trung bình không lệch về bên nào. Seed chỉ tạo độ nhiễu, không phải nguyên nhân.

## 2. Take tái dùng từ C2 và take mới trong bản v3.1 (cả tập, 82 và 23 câu)

| Số đo (trung vị) | Tái dùng C2 | Mới | p (Mann–Whitney) |
|---|---|---|---|
| Dải F0 mỗi câu | 13,1 st | 13,4 st | 0,86 |
| Độ lệch chuẩn F0 mỗi câu | 4,04 st | 3,99 st | 0,89 |
| Độ lệch chuẩn năng lượng | 7,92 dB | 7,78 dB | 0,07 |
| Tốc độ nói | 177 từ/phút | 190 từ/phút | 0,22 |
| Cuối câu (lên/ngang/xuống) | 15% / 24% / 61% | 13% / 9% / 78% | — |

**Kết luận:** việc tái dùng take C2 **không** làm giọng phẳng hơn. Hai nhóm không khác nhau về cao độ hay năng lượng.

## 3. Bản v3.1 cả tập (105 câu, 9:43): những chỗ lặp đều

- **Ranh giữa các câu chỉ có bốn giá trị cố định.** Đo từ lúc hết tiếng câu trước đến lúc có tiếng câu sau:
  - Giữa câu trong cùng cảnh (72 chỗ): 0,60 ± 0,06 s.
  - Ở `[beat]` (13 chỗ): 1,16 ± 0,07 s.
  - Giữa cảnh (15 chỗ): 1,54 ± 0,04 s.
  - Giữa sequence (4 chỗ): 2,16 ± 0,07 s.

  Như vậy độ dài nghỉ không phụ thuộc câu trước là kết luận, câu chuyển ý hay câu phụ. Nó chỉ phụ thuộc vào nhãn dựng.
- **Mỗi câu tự bắt đầu lại từ cùng một âm vực.** Cao độ trung bình giữa các câu chỉ lệch nhau 1,12 st, trong khi dải cao độ trong một câu là 13,2 st. Đoạn văn không có cung lên xuống ở cấp đoạn. Mỗi câu là một đường cong riêng (tương quan khuôn 0,21).
- **Cuối câu phần lớn đi xuống:** 68/105 câu xuống (65%), 22 ngang, 15 lên.
- **Tốc độ không chậm lại ở câu kết luận.** Trong các câu từ 6 từ trở lên, 29% nói nhanh hơn 200 từ/phút (p90 là 231 từ/phút). Các câu giải thích ở S10 đạt 221–235 từ/phút. Model sinh từng câu riêng nên không biết câu nào là câu chốt của đoạn.

## 4. Khác biệt kỹ thuật giữa lượt C3 (giọng B) và lượt v3.1

| Yếu tố | C3 (giọng B) | v3.1 | Có giải thích "đều đều" không |
|---|---|---|---|
| Model / giọng | `eleven_v3` / Eric | `eleven_v3` / Eric | Không (giống nhau) |
| voice_settings, speed | không gửi (`null` trong metadata) | không gửi (`null`) | Không (giống nhau) |
| Endpoint, output_format | `with-timestamps`, mp3_44100_128 | như C3 | Không (giống nhau) |
| Chữ gửi TTS | S01 giống từng ký tự. Câu thư: "Now her lender offers a refinance…". Câu hứa ngắn "…worth it for her?" | S01 giống. Câu thư: "Now a letter comes from her lender: …". Câu hứa ghép có gạch ngang, hai câu hỏi | **Có một phần:** mất câu duy nhất lên giọng (+3,3 st thành −2,9 st) |
| Seed | 11 (câu 7: 12) | 1 (C2 và câu mới) | Không (mục 1: chênh ±2–3 st không theo chiều nào) |
| Cách sinh | từng câu, một lần gọi mỗi câu | từng câu, một lần gọi mỗi câu | Không phân biệt được hai lượt (**cả hai giống nhau**) |
| Nghỉ dựng | 0,45 / 1,0 / 1,4 s | 0,45 / 1,0 / 1,4 / 2,0 s | Không phân biệt được hai lượt. Nhưng chính yếu tố này tạo ra ranh cố định ở mục 3 |
| Cắt đầu/đuôi take | −45 dBFS, cửa sổ 20 ms, ±30 ms | −50 dBFS, cửa sổ 10 ms, +40/+120 ms | Không: mỗi ranh chỉ dài thêm khoảng 0,1 s, vẫn cố định |
| Độ to | −20,15 LUFS, chỉ gain | −19,5 LUFS, chỉ gain | Không (gain không đổi nhấn nhá) |
| Mã hoá | AAC 192 kbps | AAC 96 kbps | Không (không đụng cao độ hay nhịp) |
| Độ dài khi nghe | 7 câu, 47 s | 105 câu, 9:43 | **Có:** cùng một khuôn lặp 105 lần thì nghe ra đều |

## 5. Kết luận

- **Tiếng thu ra của từng câu không kém đi.** Trên cùng đoạn lời, giọng B và v3.1 trùng nhau trong độ nhiễu: độ lệch chuẩn F0 4,04 so với 3,95 st, năng lượng 8,28 so với 8,12 dB, tốc độ 175 so với 174 từ/phút.
- **Những yếu tố đã loại trừ, kèm số đo:**
  - Tái dùng take C2: p = 0,86 về dải F0, p = 0,89 về độ lệch chuẩn F0.
  - Seed: chênh không theo chiều nào.
  - voice_settings, speed, model, output_format, endpoint: giống hệt nhau ở hai lượt.
  - Chuẩn hoá độ to và bitrate: chỉ đổi gain và mã hoá, không đổi nhịp.
  - Cách cắt take: mỗi ranh dài thêm khoảng 0,1 s, vẫn cố định.
- **Những yếu tố giải thích được "đều đều":**
  - (a) **Cách sinh và cách ghép**, tức là từng câu riêng lẻ cộng với nghỉ cố định. Yếu tố này có ở cả hai lượt, nhưng chỉ lộ ra khi nghe dài:
    - 72 ranh câu trong cảnh đều là 0,60 ± 0,06 s.
    - Các câu không có cung ở cấp đoạn: độ lệch chuẩn cao độ trung bình giữa câu chỉ 1,1 st.
    - 65% câu xuống giọng ở cuối.
    - Không chậm lại ở câu chốt: 29% câu nói nhanh hơn 200 từ/phút.

    Giọng B được chọn trên 7 câu, 47 s, quá ngắn để nghe ra khuôn lặp. Điều này khớp bài học V1 ở `playbook/lessons.md` B3.
  - (b) **Chữ của câu hứa đổi.** Câu hỏi ngắn lên giọng (+3,3 st) được thay bằng câu hỏi ghép đi xuống (−2,9 st và −12,4 st). Đó là chỗ nhấn duy nhất mà bản B có trong đoạn này. Đây là tác động phụ của việc sửa chữ, không phải lỗi của giọng.
- **Giả thuyết của chủ dự án:**
  - "Sinh từng câu" và "nghỉ cố định 0,45 s": **đúng về cơ chế**. Hai yếu tố này tạo ra độ đều đo được ở trên. Tuy vậy giọng B cũng được làm đúng cách đó. Nên "mất nhấn nhá so với lần đầu" chủ yếu đến từ độ dài khi nghe cộng với việc đổi câu hứa, không phải do lượt v3.1 làm khác.
  - "82 câu tái dùng": **bị loại trừ** theo số đo.
- **Chưa đo được, cần thử mù:** sinh theo cảnh có thực sự bỏ được khuôn lặp hay không. Việc này là thử mù V1/V2/V3 trong `review-c4/voice-test/`. Số đo prosody của ba bản (nghỉ trong cảnh, tốc độ từng câu, cuối câu) đã ghi trong `voice-test/key.json`. **Chỉ mở key.json sau khi đã nghe và chọn**, để số đo không dẫn tai.
- **Cách sửa:** không vá. Không đổi nghỉ ngẫu nhiên, không chỉnh tốc độ từng câu. Chọn một cách sinh qua thử mù, rồi sinh lại cả tập theo đúng một kiểu đó (G-015).
