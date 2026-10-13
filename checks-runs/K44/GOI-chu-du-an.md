# Gói chủ dự án — Phiên K lô Tập 8 (K4.4), nới luật CHẶN cũ / đổi cổng gốc · 13/10/2026

Đã **tự khoá** (lỗi máy, mục anh đã quyết, luật mới; README mục K4.4): A33, A38 (1 Short, không thumbnail), A39 + A44 (luật footage F13 CHẶN, F15 CHÍNH), A40 (áp làm nguyên tắc), A41, A42, A45 (S23 CHÍNH); A29 (cache trang) khoá ở K4.4.1 khi đo xong trùng byte. Ba câu dưới **nới luật CHẶN cũ hoặc đổi cổng gốc** nên chờ anh. Mã nháp có sẵn ở nhánh `k44b-draft` (chưa khoá, chưa vào `main`).

## Câu 1 — A32: cổng gốc (kiểm mù tắt tiếng) có dùng được làm cổng so hai bản không?
**Đo (ghi trước ngưỡng ở `a32/PREREG.md`, $6,32):** cùng master bản giao Tập 6, ba lượt đọc lại độc lập (2 người/nhịp + người thứ 3, 2 người chấm, rubric mới) cho **20 / 16 / 19** trên 23 nhịp; **7/23 nhịp lật** giữa các lượt. Luật cũ ("≥ 20/23, không nhịp nào tụt") tự trượt **6/6** cặp đối chứng âm. Luật đề xuất (tụt ≥ 2 nhịp, sàn = đáy − 1) vẫn trượt **3/6** cặp âm và **không** bắt được đối chứng dương (đảo thứ tự khung B01/B10/B24: hai nhịp đã trượt sẵn ở đối chứng, B24 đảo vẫn được đọc đúng). → Với 2–3 người đọc, cổng gốc không phân biệt được khác biệt nhỏ hơn ≈ 4–5 nhịp; ngưỡng 80 % (C4) cũng nằm trong biên nhiễu (16–20/23 = 70–87 %).
- **(a) Khuyến nghị:** từ nay cổng gốc khi **so hai bản** chỉ là **chẩn đoán** (báo nhịp lật, không tự TRƯỢT); lô K sau hiệu chuẩn bản **5 người đọc/nhịp** (đa số ≥ 3/5) với đối chứng dương mạnh (bỏ nhãn số), ghi trước ngưỡng, ước **$15–20** Console, rồi mới khoá lại thành cổng.
- (b) Hiệu chuẩn 5 người đọc ngay ở phiên K kế, chưa đổi gì trong lúc chờ.
- (c) Giữ luật cũ (biết là tự trượt chính bản giao 6/6 lần).

## Câu 2 — A34: A14 (CHẶN) nghe tên riêng sở hữu cách
**Đo:** small.en nghe "Tesla's" thay "Tessa's" ở S09.3, S15.3, S25.2 của master Tập 7; **medium.en nghe đúng cả 3**. Nháp: chỉ khi small.en mất một **tên riêng sở hữu cách**, câu đó được medium.en nghe lại (cùng đoạn cắt, cùng cách giải mã); chỉ trượt khi cả hai cùng mất. Kết quả nháp: A14 Tập 6, Tập 7 **ĐẠT** (trước: Tập 7 TRƯỢT 3 từ). Đối chứng âm thật: thay âm "Tessa's" bằng âm từ khác (cùng giọng, cùng master) → **cả hai mô hình đều mất tên → vẫn TRƯỢT**. Thêm ≈ 1,5 GB mô hình, vài giây mỗi câu nghi vấn.
- **(a) Khuyến nghị:** áp nháp (medium.en nghe lại chỉ tên riêng sở hữu cách).
- (b) Dùng `hotwords` gợi tên cho small.en — không khuyến nghị: gợi ý làm mô hình dễ "nghe" tên dù đọc sai.
- (c) Giữ (mỗi tập đổi seed giọng, Tập 7 tốn 5.839 ký tự EL).

## Câu 3 — A35–A37: S02, S07, S09 (CHẶN) ở Tập 7
{A3537}
- **(a) Khuyến nghị:** cả ba như nháp — **S02** nhận thẻ phương pháp ở hồi `method` **hoặc** `limits` (hoặc `claims.methodActs` khai); **S07** số nằm trong tên sản phẩm khai ở `claims.termNames` (vd `\b(15|30)-year\b`) không phải claim, số lạ vẫn bị bắt; **S09** tập **chỉ có tiền danh nghĩa** không cần nhãn cơ sở trên hình (vẫn phải khai `basis` và nói cơ sở một lần trong lời, K3.2); tập có tiền thực giữ nguyên.
- (b) Chỉ S02 (sửa nhận diện, không nới); S07, S09 giữ — bên dựng khai `spoken`/`basis` và thêm nhãn trên hình.
- (c) Giữ cả ba.

Trả lời ngắn, ví dụ "1a, 2a, 3a". K viết selftest đã có sẵn, chạy trước/sau Tập 4–7 (bảng ở nhánh nháp), REVIEWER, khoá **K4.4b**, merge `main`.
