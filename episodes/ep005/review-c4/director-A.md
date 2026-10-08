# Tập 5 · C4 · Lượt đạo diễn A (chẩn đoán, độc lập)

Bản xem: `review-c4/animatic-540p.mp4` (7:42.6). Cách xem: trích khung `select=not(mod(n\,15))` (0,5 s/khung, 926 khung), duyệt bảng 1 khung/giây có ghi mốc giờ, phóng to các mốc nghi lỗi ở đúng 960×540. Lời: faster-whisper `small.en`, có mốc từng từ. Ranh giới cảnh/hồi: `out/timeline.json`. Không đọc director-B.

Vì §10 không đặt tên 4 trục, tôi chấm theo 4 dòng đầu của phiếu L3 (§8), là 4 dòng mà người xem đánh giá được trên hình: cảm xúc (Vox), truyện (Vox), hình mang nghĩa khi tắt tiếng (3B1B), nhịp (WSJ).

## Điểm 4 trục (1–5)

| Trục | Điểm | Lý do một dòng |
|---|---|---|
| Cảm xúc | **2** | Ba người mua là ba khối trụ giống nhau, đứng im 11 s ở 0:44 và đến 5:23 mới có tên; không có lúc nào người xem thấy "đây là tôi". |
| Truyện | **3** | Khung truyện rõ (lựa chọn → luật → phát lại lịch sử → ba người → hai thước đo → đóng vòng ở 7:06), nhưng hồi 1 dồn luật vào một cận cảnh dài và Victor được kể bằng một câu lời rối. |
| Hình mang nghĩa | **3** | Có những ý hay: tháp nhà so với tháp nợ, núi đường cong biến thành cột, dãy nhà dưới đường chỉ số. Nhưng hình ở các mốc chính bị cắt hoặc ép nhỏ: đường lịch trả nợ ở 1:58, cột không có trục tung ở 3:36, đồ thị từng người mua ở 5:24. |
| Nhịp | **3** | Có bốn đoạn giữ khung tĩnh trên 15 s (0:44–0:55, 1:09–1:25, 1:58–2:30, 4:07–4:38), chính là những chỗ người xem muốn tua; các chuyển chế độ thì nhìn chung trơn. |

## Lời phê theo mốc (ưu tiên: cảm xúc > truyện > nhịp > đường mắt > bố cục)

1. **0:42–0:55 · cảm xúc** — Lời đọc "three illustrative buyers who got very different answers", nhưng hình là 0,8 s khung gần đen trống (0:42–0:43, đúng lúc nghe từ khoá), rồi ba nhà‑tháp giống hệt nhau đứng im 11 s. "Very different" không hiện lên hình. *Đề xuất:* cho ba người có màu hoặc dáng riêng, gắn tên Grace/Owen/Victor ngay tại đây, và để ba tháp nợ hạ xuống với ba tốc độ khác nhau, xem trước kết cục.

2. **1:58–2:30 · hình mang nghĩa / đường mắt** — Máy đẩy vào cận cảnh cực gần đường lịch trả nợ trong 32 s: đường trắng rất dày chéo khung, điểm cắt mốc 80% dồn về mép phải, các nhãn "payment 99: may request" và "payment 114 (9.5 years): ends automatically" chen ở mép, nhãn "80% of original value = $320,000" sát mép trái. Người xem không thấy toàn bộ đường cong cho đến 2:31. Khi máy đi rất gần, khối hình học trông bị phóng méo. *Đề xuất:* giữ khung toàn đường cong như ở 2:31–2:35, chỉ đẩy nhẹ vào điểm 99 và 114, đặt nhãn ở phía trong khung.

3. **3:36–4:03 · hình mang nghĩa** — Biểu đồ cột "months to 80% on paper" không có trục tung và không có thang tháng. "23 months" và cột 112 tháng không đọc được bằng mắt (vạch 60 tháng đến 4:46 mới hiện). Nhãn "median: 23 months on paper" và "height = months to 80%…" đè lên cột. *Đề xuất:* thêm 2–3 vạch tung (24 / 60 / 120 tháng) ngay khi các cột hiện ra, đưa nhãn trung vị lên trên vạch.

4. **4:07–4:38 · nhịp / truyện** — Một khung biểu đồ tĩnh 31 s với 5 dòng chữ. Số "at or under 80%: 58.6%" hiện trên hình mà lời không nhắc, nên mắt bị kéo khỏi con số được nói (15,6%). Các cột đều cao gần ngang vạch 80% nên khó đọc khác biệt. *Đề xuất:* bỏ hoặc làm mờ 58,6%; phóng to dải 75–100% cho cột 75% xanh nổi lên; cắt giữa đoạn này bằng một động tác máy theo nhịp "Two years after purchase".

5. **5:05–5:07 · lỗi (lớp chữ sót + méo hình)** — Mảnh nhãn "yr 4 mo)" của "October 2005: 112 months (9 yr 4 mo)" còn treo ở mép trái trên khi cảnh chuyển sang dãy nhà. Dãy nhà ở 5:05–5:16 trông bị xiên hoặc vặn (cửa sổ nhân đôi, khối nghiêng) trong lúc máy bay vào. *Đề xuất:* tắt hẳn lớp chữ trước khi chuyển chế độ; kiểm tra FOV và nội suy máy ở đoạn chuyển này.

6. **5:24–6:20 · bố cục / hình mang nghĩa** — Đồ thị từng người mua: dải tung từ khoảng 75% đến 92% nên các đường bị ép vào góc trái trên. Với Grace và Owen, đường "on paper" đè lên nhãn "80%" (rõ ở 5:42–5:52); hơn 60% diện tích khung bỏ trống. Câu "fastest in the replay" của Owen nằm trên một đường dài 1 cm. *Đề xuất:* co trục hoành về 0–3 năm cho Grace và Owen (hoặc tự giãn theo từng người), dời nhãn 80% sang bên phải.

7. **5:53 · lỗi pop** — Khung trống chỉ còn một vạch ngang đúng lúc nghe "Victor bought…"; sau đó 5:54–6:00 là đồ thị Victor rỗng thêm khoảng 6 s. *Đề xuất:* để đường của Victor bắt đầu vẽ ngay từ "Victor", bỏ khung trống.

8. **6:09–6:16 · truyện (lời)** — ASR nghe được: "He got there by paying the loan down and his own schedule. At his lower rate of 6.07%, reached 80% of the original price first at payment 90." Câu lời rối, và "lower rate" không nói thấp hơn cái gì (6,86% của ví dụ?). Đây là đỉnh cảm xúc của Victor mà lời bị vấp. *Đề xuất:* viết lại thành hai câu ngắn, nêu rõ phép so sánh. Số liệu đã kiểm: 6,07% ⇒ lịch đến 80% ở kỳ 90 là đúng.

9. **1:06–1:25 · hình mang nghĩa / nhịp** — "It protects the lender…": hình người cho vay chỉ xuất hiện khoảng 1 s (1:08) rồi bị cắt khỏi khung khi máy đẩy vào người vay. Sau đó là 16 s gần như tĩnh, người vay cầm tấm ván. Ở 1:21–1:23 có một khối tối mờ nổi lên trên cuốn lịch, đọc như vật lỗi chứ không phải "lật trang". Hiện tượng này lặp lại ở 3:30–3:32. *Đề xuất:* giữ người cho vay trong khung khi nói "protects"; cho mặt sau trang lịch sáng màu, hoặc làm rõ chuyển động lật.

10. **0:22–0:23 · chồng nhãn / máy** — Nhãn "slowest case ≈ 9 years" màu xanh nằm trong lưới đường, bị đường xám cắt chữ. Ở 0:23, khung bị lia sang trái trong lúc nhãn đang mờ dần, nên "typical ≈ 2 years" bị cắt mép. *Đề xuất:* đặt nhãn trên đỉnh núi, có nền mờ; giữ máy đứng yên cho đến khi nhãn tắt.

11. **2:36–2:43 · hình mang nghĩa** — "Lenders and the investors who own loans can also drop the insurance": hình là một ngôi nhà đơn độc 6 s, không có người cho vay hay nhà đầu tư. Ở 2:43, khi máy bay, một vật thể xuất hiện ở mép phải (pop). *Đề xuất:* đưa nhân vật người cho vay (đã có ở 1:08) vào cảnh này.

12. **4:46–4:54 · bố cục** — Nhãn "more than 60 months: 14.7% (about 1 in 7)", nhãn "60 months" và "each bar's height…" chồng lên vạch 60 và lên khối cột xanh. *Đề xuất:* gom về một nhãn duy nhất phía trên khung xanh.

13. **6:38–6:56 · đường mắt** — Lưới đường của mọi tháng mua phủ lên ba đường Grace/Owen/Victor; nhãn "80%" và "Grace" bị đường đè, khung chú thích "≈ 2 years matched…" chồng lên dữ liệu. Đây là khung tổng kết quan trọng nhất nhưng ba nhân vật lại khó thấy nhất. *Đề xuất:* làm lưới mờ hẳn đi (khoảng 15%), tô màu ba đường theo màu nhân vật, đưa chú thích ra vùng trống phía dưới.

14. **7:13–7:22 · lỗi đọc** — Thẻ "How we know this" có nền trong suốt: các ô vuông của toà chung cư 3D nằm phía sau lộ qua chữ (cạnh "index change", "rent,"), trông như ký tự lỗi. Chữ trên thẻ cũng rất nhỏ ở 540p. *Đề xuất:* dùng nền đục cho thẻ, hoặc ẩn khối 3D phía sau; kiểm tra lại cỡ chữ theo C14 trên bản 1080p.

15. **7:34–7:42 · bố cục (kết)** — Khung kết đặt toà chung cư bị cắt ở mép phải, người và nhà lệch tâm; không có nhịp dừng hay thẻ kết, video hết sau lời 2,3 s. Chi tiết tốt: thẻ PMI vàng vẫn còn trên mái nhà, khớp với "on paper is not removed". *Đề xuất:* lùi máy để cả bộ ba vào khung giống 7:07, giữ 1–2 s cho nhạc kết.

## Kiểm số và âm (không thấy lỗi)

- Các số trên hình khớp lời và khớp phép tính lại: $2.362/tháng với $360k ở 6,86%; 80% = $320.000 ở kỳ 99; 78% = $312.000 ở kỳ 114 (9,5 năm); lịch đến 80% của Grace 71 / Owen 86 / Victor 90 tháng ở các lãi suất 4,16 / 5,71 / 6,07%; 112 tháng = 9 năm 4 tháng; 14,7% ≈ 1/7.
- Âm: không có khoảng lặng nào bị đặt sai chỗ. Chỉ có một khoảng lặng khoảng 1 s ở 3:03.5–3:04.5, ngay trước hồi 2 (3:05.2); khoảng này có vẻ cố ý để lấy hơi. Từ 7:17.5 đến 7:22.9 không có lời nhưng nhạc vẫn chạy.
- Chữ "Source:" trông như bị cắt ở mép trên khi xem qua bảng thu nhỏ; xem ở đúng độ phân giải thì không bị cắt, nên không tính là lỗi.
