# Khung chất lượng 3 lớp của Crux (v1, 29/09/2026)

Nguồn: khung Cine Lab (`HungQuach301/cine-lab`, `docs/cine-lab/CINE-LAB-KHUNG-CHAT-LUONG.md`, `CINE-LAB-BAI-HOC-BRIEF-D.md`) rút gọn cho thể loại data-explainer. Chủ dự án duyệt khung 3 lớp ngày 29/09/2026. Tài liệu này đứng ngay sau `CHARTER.md`.

## 0. Định nghĩa chất lượng

> **Người xem, xem một lần ở tốc độ thường, đánh giá tập của Crux ngang với ba tham chiếu** (`playbook/references.md`): Vox về truyện, 3Blue1Brown về hình mang nghĩa, WSJ "three charts" về thể loại.

Chất lượng không được định nghĩa bằng một con số đếm được. Con số chỉ canh lỗi (L1) hoặc cảnh báo (L2).

## 1. Ba lớp

| Lớp | Đo cái gì | Ai | Kết quả | Vai trò |
|---|---|---|---|---|
| **L1 Kỹ thuật** | Số liệu và claim đúng; nguồn và điều khoản; quyền tài sản; kỹ thuật file; âm lượng; ASR không mất từ khoá | Máy (Phiên K, khoá SHA) | Đạt / trượt | Điều kiện cần. Lỗi L1 là lỗi **Chặn** |
| **L2 Nghề** | Truyện, kịch bản, hình, giọng, âm, dựng | Phiếu chấm có bằng chứng (mốc thời gian, câu, khung). Phần máy đo được **chỉ cảnh báo** | Điểm 1–5 kèm bằng chứng | Tay nghề |
| **L3 Khán giả** | Hiểu, cảm, muốn xem tiếp; so với ba tham chiếu | Chủ dự án xem **một lần**; kiểm mù AI ở mỗi cổng | Có/không, tỷ lệ | **Thước đo cuối** |

**Thứ tự ưu tiên khi xung đột** (Walter Murch, "Rule of Six", mở rộng): **cảm xúc > truyện > nhịp > đường mắt > bố cục**. Tiêu chuẩn lớp dưới không được bắt hy sinh cảm xúc hay truyện, trừ lỗi L1 Chặn.

## 2. Chống Goodhart (luật cứng)

1. **Không chỉ tiêu số lượng cho kỹ thuật nghệ thuật.** Không "≥ N khoảng lặng", không "wpm mỗi câu trong khoảng X", không "số mới mỗi cảnh ≤ N" làm đích. Số lượng chỉ là cảnh báo; mỗi kỹ thuật phải có lý do ghi trong kịch bản hoặc shot list.
2. **Chỉ số trong ±5% quanh ngưỡng phải nêu tên** trong báo cáo cổng.
3. **Không thủ thuật để qua số đo:**
   - không dấu ngắt giả ("...", thẻ `<break>`) để ép tốc độ đọc;
   - không giãn hay nén thời gian giọng;
   - **không đổi model giọng giữa tập**; một giọng, một model, một bộ tham số cho cả tập (G-010);
   - không thêm phần tử chỉ để vượt ngưỡng.
4. **Đo từ file đã render hoặc đã phát**, không từ bản khai.
5. **Không duyệt hình bằng ảnh tĩnh** (G-011). Hình được duyệt khi có chuyển động và đúng thời gian, và phải tự nói được ý khi tắt tiếng.
6. **Phê bình AI không thay khán giả.** Điểm của CRITIC là L2 tham khảo; nó không cho qua cổng. Ở bản cũ Tập 1, CRITIC chấm kịch bản 4,71 trong khi chủ dự án chấm "chưa có kịch bản".
7. Bên dựng không sửa bộ đo đang chấm mình (CHARTER §7.1).

## 3. Phân cấp luật máy (khoá K3)

| Cấp | Nghĩa | Hệ quả |
|---|---|---|
| **Chặn** | Số sai, claim thiếu nguồn, quyền tài sản chưa rõ, file hỏng, âm lượng ngoài chuẩn, mất từ khoá | Không phát hành |
| **Chính** | Lỗi nghề đo được (chữ đè, tương phản, lời bị lấn) | Phải sửa hoặc giải thích bằng một câu trong báo cáo |
| **Tham khảo** | Số đo nhịp, mật độ, wpm, độ dài cold open… | Chỉ báo cáo; không ai phải "sửa cho đạt" |

Việc gán cấp là việc của Phiên K (K3), chủ dự án duyệt. Cho đến khi có K3, P2 đọc báo cáo K2 theo bảng trên và ghi rõ luật nào đang được coi là Tham khảo.

## 4. Sáu cổng

Trượt cổng thì quay lại cổng trước. **Truyện chốt ở C4 (animatic có chuyển động)**, trước khi render.

| Cổng | Đầu ra | Kiểm mù AI | Qua khi | Chủ dự án quyết |
|---|---|---|---|---|
| **C1 Ý tưởng** | Bối cảnh cập nhật (mọi số có claim, mốc ngày "hiện tại"); 2 logline; câu hỏi của tập | 5 agent đọc logline → kể lại, có muốn xem không | ≥ 4/5 kể đúng; ≥ 3/5 muốn xem | Chọn logline |
| **C2 Kịch bản** | Beat sheet, kịch bản, table read giọng tạm (một model, đọc tự nhiên) | 5 agent đọc bản chép lời → tóm tắt, nêu đáp án, chỉ chỗ khó hiểu | ≥ 4/5 đúng | OK / sửa |
| **C3 Thiết kế và giọng** | 3 hướng hình × 3 style frame (cùng 3 nhịp); sau đó 5–8 style frame cuối = hợp đồng hình ảnh. Thử giọng mù G1/G2/G3 (~20 s) | Mỗi frame: người xem mù đọc ý nghĩa | Ý đọc ra khớp ý đồ ghi trước | Chọn hướng; ký hợp đồng hình; chọn giọng |
| **C4 Animatic có chuyển động** | Toàn tập, chuyển động thô 480p/720p, giọng đã chọn, âm tạm | Tắt tiếng, từng nhịp: đọc ra ý gì | ≥ 80% nhịp đọc đúng ý đồ; nhịp trượt thiết kế lại | OK / sửa. Trượt → về C2/C3, **không render** |
| **C5 Render và L1** | Bản cuối; checks khoá K3 | — | Không lỗi Chặn; lỗi Chính có giải thích | (không hỏi, trừ khi có lỗi Chặn không sửa được) |
| **C6 Chấm cuối (L3)** | Clip nổi bật ≤ 3 phút + link bản đầy đủ; phiếu chấm so ba tham chiếu | AI tóm tắt toàn tập | Chủ dự án duyệt | Có / Không |

## 5. Giao thức kiểm mù

1. **Ý đồ ghi trước khi chạy** vào `episodes/<tập>/gates/Cx-intent.md` và commit. Không sửa ý đồ sau khi thấy kết quả.
2. Mỗi mẫu giao cho **một agent con mới**, chỉ mở **một file tên ngẫu nhiên** (8 ký tự hex) trong một thư mục tạm không có gì khác; không ngữ cảnh dự án, không tên nhân vật hay tên kênh nếu không nằm sẵn trong mẫu.
3. **Câu hỏi cố định**, viết sẵn cho từng cổng, giống nhau cho mọi agent.
4. Ghi **nguyên văn** câu trả lời vào `episodes/<tập>/gates/Cx-blind.md`, kèm bảng chấm so với ý đồ. Người chấm "khớp/không khớp" là P2, theo tiêu chí viết trong file ý đồ.
5. Khi có thể, kèm **đối chứng** (mẫu biết trước là tốt hoặc kém) để biết câu hỏi phân biệt được.
6. Tối đa 2 vòng sửa–kiểm cho một mẫu; vẫn trượt thì đưa lên chủ dự án kèm phương án, không lặp tiếp.
7. **Vai người đọc (từ C2, chủ dự án duyệt 29/09/2026):** khán giả đích — *"an American currently paying a mortgage signed in 2022–2024"*; câu hỏi và trả lời bằng **tiếng Anh**; P2 tóm tắt tiếng Việt cho chủ dự án, nguyên văn giữ tiếng Anh. Mỗi lượt thêm **1 người đọc phổ thông** (không vai) làm đối chứng.
8. **Bộ đo phải phân biệt được:** mỗi lượt có một **đối chứng yếu** (bản cũ đã bị chủ dự án bác). Nếu đối chứng yếu đạt ngang ứng viên ở chỉ số đang chấm thì **báo chủ dự án, không tự sửa tiếp**. Bộ đo mới được hiệu chuẩn một lần trên logline C1 Tập 1 trước khi dùng.
9. **"Muốn xem" đo bằng so cặp mù (chủ dự án chọn A, 29/09/2026):** mỗi người đọc vai khán giả đích thấy một file gồm hai bản (ứng viên và đối chứng yếu) và phải chọn một bản muốn bấm xem, kèm lý do nguyên văn. Mỗi cặp chạy **cả hai thứ tự** với người đọc khác nhau (một nửa ứng viên trước, một nửa đối chứng trước). Qua khi ứng viên thắng ≥ 80% (≥ 4/5). "Kể lại" và "chỗ khó hiểu" vẫn hỏi riêng, vai khán giả đích — đây là tín hiệu giá trị nhất. Nếu hiệu chuẩn so cặp không đạt: bỏ "muốn xem" khỏi kiểm AI, chủ dự án chấm (phương án C). "Muốn xem" của máy chỉ là bằng chứng phụ; phán quyết cuối là L3 của chủ dự án.
10. **Hiện hành (29/09/2026, chủ dự án sửa sau hiệu chuẩn lần 2):** so cặp trên logline C1 **đã phân biệt được** (đối chứng yếu thắng 19/19, không thiên lệch vị trí) — chỉ là **ứng viên thua**. Vì vậy: (a) kiểm mù AI ở các cổng **không dùng "muốn xem" làm cổng**; cổng chỉ đo **hiểu** (kể lại, đáp án, chỗ khó hiểu) với vai khán giả đích và đối chứng yếu; (b) **so cặp mù giữ làm bằng chứng THAM KHẢO** cho câu hứa, tiêu đề, thumbnail (ghi lý do nguyên văn); (c) "muốn xem" cuối cùng do chủ dự án chấm (L3).
11. **Đọc kết quả hiệu chuẩn:** tiêu chí "không đạt" phải tách hai trường hợp — **"không phân biệt được"** (đối chứng ngang ứng viên: bộ đo vô dụng) và **"ứng viên thua"** (bộ đo phân biệt được, ứng viên kém hơn: bộ đo có ích, ứng viên cần sửa).

## 6. Gói quyết định (mỗi cổng)

- Đọc dưới 1 phút; **≤ 3 câu hỏi**, mỗi câu có phương án và khuyến nghị.
- Clip ≤ 2 phút xem được trên điện thoại (C6: ≤ 3 phút).
- 1 dòng **kiểm độc lập số liệu**; 1 dòng **kiểm mù**.
- Hiện ngay trong phiên; đồng thời mở issue `[Cổng Cx] Tập N — cần quyết định` chỉ để thông báo.
- Câu trả lời ghi vào `taste-ledger.md` và `AUTHORSHIP.md` (main) và `episodes/<tập>/ledger.md`.
- **Gu không bao giờ tự quyết**: cấu trúc truyện, giọng và model giọng, hướng hình, âm sắc, nhạc. Việc kỹ thuật thực thi: điều phối tự quyết và ghi lý do.

## 7. Phiếu chấm L3 (C6)

Chủ dự án xem một lần, rồi chấm 1–5 mỗi dòng, ngang với tham chiếu (3 = "đúng nghề nhưng không đáng nhớ"; 5 = "ngang tham chiếu"):

| # | Câu hỏi | Tham chiếu |
|---|---|---|
| 1 | Tôi có thấy mình trong câu chuyện không? (cảm xúc) | Vox |
| 2 | Có một câu chuyện với bối cảnh, người, vấn đề, hành trình, đáp án? | Vox |
| 3 | Tắt tiếng, hình vẫn nói được ý? | 3Blue1Brown |
| 4 | Nhịp: có chỗ nào tôi muốn tua? | WSJ |
| 5 | Giọng tự nhiên, ổn định, một màu? | — |
| 6 | Tôi có muốn xem tập tiếp theo? | — |
