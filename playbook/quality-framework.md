# Khung chất lượng 3 lớp của Crux (v2, 04/10/2026)

v1 (29/09/2026) rút từ khung Cine Lab. v2 áp `decisions/D-005.md`: 3 cổng GU, 3 cổng TỰ ĐỘNG; bỏ phép che chữ/số; mọi kiểm mù do agent độc lập, mù tập chấm. Tài liệu này đứng ngay sau `CHARTER.md`. Cách chạy một tập: `playbook/episode.md`.

## 0. Định nghĩa chất lượng

> **Người xem, xem một lần ở tốc độ thường, đánh giá tập của Crux ngang với ba tham chiếu** (`playbook/references.md`): Vox về truyện, 3Blue1Brown về hình mang nghĩa, WSJ "three charts" về thể loại.

Chất lượng không định nghĩa bằng một con số đếm được. Con số chỉ canh lỗi (L1) hoặc cảnh báo (L2).

## 1. Ba lớp

| Lớp | Đo cái gì | Ai | Kết quả | Vai trò |
|---|---|---|---|---|
| **L1 Kỹ thuật** | Số liệu và claim; nguồn và điều khoản; quyền tài sản; kỹ thuật file; âm lượng; ASR không mất từ khoá | Máy (Phiên K, khoá SHA) | Đạt / trượt | Điều kiện cần. Lỗi L1 là lỗi **Chặn** |
| **L2 Nghề** | Truyện, kịch bản, hình, giọng, âm, dựng | Kiểm mù ở cổng; phần máy đo được **chỉ cảnh báo** | Điểm kèm bằng chứng | Tay nghề |
| **L3 Khán giả** | Hiểu, cảm, muốn xem tiếp; so với ba tham chiếu | Chủ dự án xem **một lần** (C6); sau phát hành: số liệu YouTube | Phiếu chấm; số liệu | **Thước đo cuối** |

Thứ tự khi xung đột (Murch, mở rộng): **cảm xúc > truyện > nhịp > đường mắt > bố cục**. Lớp dưới không được bắt hy sinh cảm xúc hay truyện, trừ lỗi L1 Chặn.

## 2. Chống Goodhart (luật cứng)

1. Không chỉ tiêu số lượng cho kỹ thuật nghệ thuật. Số lượng chỉ là cảnh báo; mỗi kỹ thuật có lý do ghi trong kịch bản hoặc shot list.
2. **Chỉ số trong ±5% quanh ngưỡng phải nêu tên** trong báo cáo cổng.
3. Không thủ thuật để qua số đo: không dấu ngắt giả; không giãn/nén giọng; **không đổi model giọng giữa tập** (G-010); không thêm phần tử chỉ để vượt ngưỡng.
4. Đo từ file đã render hoặc đã phát, không từ bản khai.
5. Không duyệt hình bằng ảnh tĩnh (G-011). Kiểm mù hình dùng dải 6 khung cắt từ clip có chuyển động, đúng thời gian.
6. Phê bình AI không thay khán giả. Điểm CRITIC là L2 tham khảo.
7. Bên dựng không sửa bộ đo đang chấm mình (CHARTER §7.1). **Bên dựng không chấm kiểm mù của mình** (lessons E1).
8. Thước đo mới phải **hiệu chuẩn trên đối chứng đã biết kết quả** trước khi thành ngưỡng (lessons E2).

## 3. Phân cấp luật máy

| Cấp | Nghĩa | Hệ quả |
|---|---|---|
| **Chặn** | Số sai, claim thiếu nguồn, quyền chưa rõ, file hỏng, âm lượng ngoài chuẩn, mất từ khoá | Không phát hành |
| **Chính** | Lỗi nghề đo được (chữ đè, tương phản, lời bị lấn) | Sửa hoặc giải thích một câu trong báo cáo |
| **Tham khảo** | Nhịp, mật độ số, wpm, độ lặp nhạc, độ dài cold open… | Chỉ báo cáo |

Gán cấp là việc của Phiên K, chủ dự án duyệt. **Checks khi dựng:** chỉ chạy luật liên quan cảnh vừa sửa. **Chạy đủ bộ hai lần:** cuối C4 và ở C5.

## 4. Sáu cổng: 3 GU, 3 TỰ ĐỘNG

**GU** = chủ dự án quyết, phiên dừng chờ. **TỰ ĐỘNG** = ngưỡng ghi trước, tối đa 2 vòng, nhánh dự phòng đặt sẵn. Qua cổng (kể cả qua bằng dự phòng) thì mở issue thông báo và **đi tiếp, không chờ**. Chủ dự án phủ quyết được tới cổng GU kế tiếp. Truyện chốt ở C4, trước render.

| Cổng | Loại | Đầu vào | Thước đo | Ngưỡng | Vòng tối đa | Nhánh dự phòng khi trượt | Ai quyết |
|---|---|---|---|---|---|---|---|
| **C1 Ý tưởng và lời hứa** | **GU** | Hồ sơ đề tài (`topic-dossier.md`); bối cảnh có claim, mốc ngày "hiện tại"; 2 logline; 2–3 tiêu đề nháp | Kiểm mù kể lại logline (5 vai đích + 1 phổ thông, chấm độc lập); so cặp tiêu đề **một vòng** (tham khảo) | Logline đưa lên: kể đúng ≥ 4/5 vai đích | 2 (sửa logline) | Đưa logline tốt nhất kèm điểm, ghi rõ chưa đạt | Chủ dự án: logline, tiêu đề nháp, phạm vi |
| **C2 Kịch bản** | **TỰ ĐỘNG** | Kịch bản WRITER (đầu bài v2, `episode.md` §3); bảng nhịp + **phân loại nhịp**; danh sách claim | (a) Máy: claim 100%, S10 = 0, có "US only" và "history, not a forecast". (b) Kiểm mù lời: 5 vai đích + 1 phổ thông, chấm độc lập: đúng câu hỏi + đáp án; câu khuyên; đoạn mất chú ý | (a) đạt hết. (b) đúng ≥ 5/6; câu khuyên 0/6; không đoạn nào bị ≥ 4/6 cùng chỉ là mất chú ý | 2 | Đoạn mất chú ý → rút còn **1 câu lời + thẻ + mô tả** (mẫu đoạn phương pháp). Vẫn trượt → giữ bản điểm cao nhất, ghi rủi ro vào gói C3 | Phiên; issue báo |
| **C3 Thiết kế và giọng** | **GU** | **Một hướng** từ `toolkit/visual-library/` + thiết kế mới cho nhịp chưa có ký hiệu; style frame **có chuyển động** cho mọi nhịp loại 1; clip giọng ~30 s; clip phối nhạc ≤ 60 s (độ lặp T2, tham khảo) | Cổng gốc trên style frame (§5) | Mỗi nhịp loại 1: ≥ 2/3 đúng nghĩa, câu khuyên 0 | 2 mỗi nhịp, trước khi gửi gói | Vòng 2 = nhãn nghĩa (≤ ~8 từ, ≥ 40 px, ≥ 1 s/3 từ). Vẫn trượt → hạ nhịp xuống loại 2, báo trong gói | Chủ dự án: ký hợp đồng hình (gồm màu), giọng, nhạc; có quyền đòi thêm hướng |
| **C4 Animatic có chuyển động** | **TỰ ĐỘNG** | Animatic toàn tập 720p, giọng đã chọn, âm tạm | Cổng gốc trên dải nhịp loại 1 (§5); checks đủ bộ lần 1 | ≥ 80% nhịp loại 1 đạt (≥ 2/3, câu khuyên 0) | 2 | Nhãn nghĩa cho nhịp trượt. Vẫn trượt → **ngoại lệ**: render, ghi điểm hai vòng vào ledger và gói C6 | Phiên; issue báo |
| **C5 Render và L1** | **TỰ ĐỘNG** | Bản cuối 1080p; phối nhạc đã chốt sau C2 | Checks khoá K đủ bộ lần 2 | Chặn = 0; Chính có giải thích | 2 | Sửa trong danh sách §6. Lỗi Chặn không sửa được trong danh sách → **không phát hành**, đưa vào gói C6 kèm khiếu nại luật | Phiên; issue báo |
| **C6 Chấm cuối (L3)** | **GU** | Clip nổi bật ≤ 3 phút + bản đầy đủ 720p; 3 thumbnail đã qua claim-risk; tóm tắt AI (chấm độc lập) | Phiếu L3 (§8); so cặp thumbnail một vòng (tham khảo) | Chủ dự án duyệt | 1 | — | Chủ dự án: L3, phát hành, tiêu đề, thumbnail |

## 5. Giao thức kiểm mù

1. **Ý đồ ghi trước khi chạy** (`episodes/<tập>/gates/Cx-intent.md`, commit trước). Ý đồ gồm: mẫu, vai, câu hỏi cố định, rubric "đúng nghĩa" / "chỉ tả hình", ngưỡng, **luật dừng sớm** (mục 6). Không sửa sau khi thấy kết quả.
2. Mỗi mẫu giao cho **một agent mới**. Agent chỉ mở **một file tên hex** trong thư mục riêng; không có ngữ cảnh dự án (`toolkit/blind/packets.py deal`).
3. **Câu hỏi cố định, tiếng Anh**, vai khán giả đích của tập. Mọi kiểm mù có thêm câu suy diễn lời khuyên: *"What advice, if any, would a viewer take from this?"*
4. **Người chấm là agent độc lập, mù tập.** Agent chỉ đọc gói nhãn ngẫu nhiên gồm câu trả lời và rubric (`packets.py packet`); khoá nhãn commit trước khi chấm. Chấm 1 / 0,5 / 0 kèm cờ câu khuyên. Một người đọc **đúng** khi điểm = 1 **và** không có câu khuyên. Phiên điều phối chỉ ghi và gộp (`packets.py tally`).
5. Nguyên văn trả lời ghi vào `gates/Cx-blind.md`. Gói cổng chỉ đưa bảng tổng.
6. **Dừng sớm** (kiểm theo nhịp ở C3, C4; C1, C2 dùng đủ 6 người đọc): người đọc chạy lần lượt. 2 người đầu cùng kết quả thì dừng (2/2 đạt, 0/2 trượt). Lệch thì gọi người thứ 3; nhịp đạt khi ≥ 2/3 đúng. Có câu khuyên thì nhịp trượt ngay.
7. **Cổng gốc (thước đo hình, C3 và C4):** dải 6 khung tắt tiếng, **giữ chữ/số** (`toolkit/blind/strips.py`). Câu hỏi: "ý gì, cái gì đổi theo thời gian, nghĩa là gì" + câu lời khuyên. 3 người đọc **mới** mỗi nhịp mỗi vòng. **Không che chữ/số** (D-005 Q3).
8. **Phân loại nhịp ở C2:** phiên xếp mỗi nhịp vào **loại 1 "hình tự mang ý"** hoặc **loại 2 "hình minh hoạ lời"**. Bảng phân loại báo qua issue **trước mọi kiểm mù hình**; chủ dự án có quyền phủ quyết. Chỉ nhịp loại 1 tính vào ngưỡng hình. Nhịp loại 2 vẫn kiểm câu khuyên.
9. **Đối chứng:** khi có, kèm một mẫu biết trước kết quả (thường lấy từ thư viện hình hay tập trước). Đối chứng chỉ để biết bộ đo phân biệt được, không tính vào cổng. Tách hai trường hợp: "không phân biệt được" (đối chứng ngang ứng viên: bộ đo vô dụng) và "ứng viên thua" (bộ đo dùng được).
10. **"Muốn xem" không phải cổng.** So cặp mù chỉ là tham khảo, chạy một vòng: tiêu đề ở C1, thumbnail ở C6. Số đo thật là Test & Compare trên YouTube.

## 6. Việc phiên được tự quyết — DANH SÁCH ĐÓNG

Phiên **chỉ** tự quyết những việc sau, mỗi việc ghi một dòng lý do ở `ledger.md`:

1. Kỹ thuật dựng và render (engine, cách vẽ, độ phân giải nháp, chia cảnh render).
2. Tham số mã hoá (codec, bitrate, chia phần giao hàng).
3. Chia agent và chọn model/effort theo `episode.md` §2.
4. Thứ tự việc, chạy song song việc độc lập.
5. Sửa câu chữ **giữ nghĩa** để qua luật CHẶN (claim, S10, A14, S09…). Mọi câu người xem nghe hay thấy bị đổi được liệt kê trong gói GU kế tiếp.
6. Sửa nhãn chữ mang nghĩa **không thêm vật, không thêm gu** (theo luật nhãn §4 C3), kể cả dời vị trí để qua luật CHÍNH.
7. Chọn **phương án dự phòng đã ghi trước** trong bảng §4 hoặc trong ý đồ cổng.

**Việc ngoài danh sách → đưa vào gói cổng GU kế tiếp.** Trong lúc chờ, giữ nguyên bản đã duyệt. Nếu việc đó chặn tiến độ, làm việc khác. Nếu không còn việc khác, dừng và mở issue.

**Không bao giờ tự quyết** (luôn là gu hoặc irreversible):
- giọng và model giọng;
- hướng hình, bảng màu;
- nhạc và cách phối;
- cấu trúc truyện, cold open, logline, tiêu đề, thumbnail;
- phát hành.

Cùng các việc ở CHARTER §7.5.

## 7. Gói gửi chủ dự án

- **Gói cổng GU:** ≤ 3 câu hỏi, mỗi câu có phương án và **khuyến nghị**. Có clip xem được trên điện thoại (≤ 2 phút; C6 ≤ 3 phút). Có 1 dòng kiểm số độc lập, 1 dòng kiểm mù và **kết quả soát của REVIEWER**. Gói hiện ngay trong phiên; đồng thời mở issue `[Cổng Cx] Tập N — cần quyết định`.
- **Issue cổng TỰ ĐỘNG:** `[Cổng Cx · tự động] Tập N — qua/ngoại lệ`, **≤ 5 dòng**: kết quả, ngưỡng, số vòng, có dùng dự phòng không (cái nào), link file. Không hỏi, không chờ.
- Câu trả lời của chủ dự án ghi vào `taste-ledger.md`, `AUTHORSHIP.md` (main) và `episodes/<tập>/ledger.md`.

**Vai REVIEWER** (agent độc lập, đọc repo; Opus, effort Medium). REVIEWER soát mọi gói GU và mọi issue TỰ ĐỘNG trước khi gửi, theo checklist cố định:
1. Gói khớp khung chất lượng: đúng loại cổng, đúng ngưỡng ghi trước, không sửa ý đồ sau kết quả.
2. Claim-risk: mọi số, mọi câu và chữ trên hình trong gói có claim; câu NÊU số đủ hai thời kỳ + xấu nhất; không có câu khuyên, không có dự báo.
3. Chống Goodhart: không thủ thuật; chỉ số trong ±5% quanh ngưỡng được nêu tên.
4. Việc tự quyết nằm trong danh sách §6; việc ngoài danh sách có trong gói.
5. Không lệch giữa các phiên: tên kind/params theo phiên K; khoá SHA khớp; PLAN, ledger và gói nói cùng một chuyện.

Kết quả soát (đạt / các dòng trượt) in kèm gói. REVIEWER thay cho việc chủ dự án chuyển gói sang chat chiến lược.

## 8. Phiếu chấm L3 (C6)

Chủ dự án xem một lần, rồi chấm 1–5 mỗi dòng ngang tham chiếu (3 = "đúng nghề nhưng không đáng nhớ"; 5 = "ngang tham chiếu"):

| # | Câu hỏi | Tham chiếu |
|---|---|---|
| 1 | Tôi có thấy mình trong câu chuyện không? (cảm xúc) | Vox |
| 2 | Có một câu chuyện với bối cảnh, người, vấn đề, hành trình, đáp án? | Vox |
| 3 | Tắt tiếng, hình vẫn nói được ý? | 3Blue1Brown |
| 4 | Nhịp: có chỗ nào tôi muốn tua? | WSJ |
| 5 | Giọng tự nhiên, ổn định, một màu? | — |
| 6 | Tôi có muốn xem tập tiếp theo? | — |

## 9. Quy ước quyền tài sản (K3.1, chủ dự án duyệt 29/09/2026)

1. Không nhúng tài sản bên thứ ba dạng `data:` (base64 trong HTML/CSS/JS, SVG, JSON). Mọi ảnh, font, âm, video bên thứ ba là file riêng có đường dẫn.
2. Không đưa tài sản bên thứ ba vào bằng video hay ghép hậu kỳ mà không khai trong `RIGHTS.md` (nguồn, giấy phép trích nguyên câu, phạm vi).
3. Tài sản tự sinh bằng mã ghi một dòng chung trong `RIGHTS.md`.
4. Rà lại ở C5 (cấp Chặn): tìm `data:` trong mã dựng; đối chiếu mọi đầu vào ghép hậu kỳ với `RIGHTS.md`.
