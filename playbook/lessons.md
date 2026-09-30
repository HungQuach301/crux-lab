# Bài học — mọi phiên đọc khi khởi động

Cập nhật: 29/09/2026 (P2). Thêm bài học mới ở cuối mỗi tập; tỉa khi một bài học đã thành luật hoặc hết đúng.

## A. Tập 1 bản cũ (dừng ở Cổng B, 29/09/2026; tag `ep001-v1-stopped`, lưu ở `archive/ep001-v1/`)

| # | Chuyện đã xảy ra | Bài học | Luật bây giờ |
|---|---|---|---|
| A1 | Chất lượng được định nghĩa bằng luật đếm được (wpm mỗi hồi 150–160, cold open ≤ 15 s, ≤ 2 số mới mỗi cảnh, khoảng lặng ≥ 1 s). | Model tối ưu đúng thứ được đếm, không tối ưu thứ người xem cảm. | Số nghề chỉ là **Tham khảo** hoặc cảnh báo (`quality-framework.md` §2–3). |
| A2 | Để kéo wpm vào 150–160: `pauses.js` chèn "..." giả; **104/132 câu** tự đổi từ `eleven_v3` sang `eleven_multilingual_v2` speed 0,70–0,72; thẻ `<break>`. Chủ dự án: *"voice có vấn đề, nhiều đoạn bị cố kéo dài, không ổn định."* | Thủ thuật qua được máy nhưng người nghe thấy ngay. Hai model = hai màu giọng. | G-010. Một model cả tập; không dấu ngắt giả; không giãn; chậm lại bằng khoảng nghỉ giữa câu do dựng đặt. `pauses.js` đã xoá. |
| A3 | Kịch bản M1b lắp từ con số ("vào ngay nhân vật, không bối cảnh, thông tin cụt lủn"). | Số phải đến sau khi người xem cần nó. | G-007, G-008, G-009. Kịch bản viết từ treatment đã duyệt, không từ bảng số. |
| A4 | Storyboard là ảnh tĩnh; duyệt hình bằng ảnh tĩnh. Chủ dự án: *"hình ảnh tĩnh khó hiểu ý nghĩa."* | Hình data-explainer mang nghĩa qua **chuyển động** (cái gì mọc, cái gì cắt nhau). Ảnh tĩnh không kiểm được điều đó. | G-011. Duyệt hình ở animatic có chuyển động (C4), kiểm mù tắt tiếng. |
| A5 | CRITIC (AI) chấm kịch bản 4,71/5; chủ dự án chấm "chưa có kịch bản" (với bản M1b) và dừng ở Cổng B. | Phê bình AI biết người viết muốn gì nên chấm dễ; nó không phải khán giả. | Điểm CRITIC là L2 tham khảo. Cổng qua bằng kiểm mù (agent không ngữ cảnh) + chủ dự án. |
| A6 | Sửa theo máy kiểm: đổi lời 19 câu để S10/S13/S16 qua; cold open bị ép từ 26,65 s xuống 21,94 s và đọc 176 wpm. | Sửa để qua luật làm hỏng câu và nhịp. | Luật chưa phân cấp thì coi là Tham khảo; chỉ Chặn mới buộc sửa. |
| A7 | Cổng B đưa quá nhiều thứ cùng lúc (render? cold open? giọng?) trên một clip 82 s ảnh tĩnh. | Một cổng, một loại quyết định. | 6 cổng; ≤ 3 câu hỏi; clip ≤ 2 phút có chuyển động. |
| A8 | Giữ được: dữ liệu và mô hình (máy kiểm tính lại độc lập 619/619), `numbers.md` với claim ID, ba nhân vật, treatment qua Cổng A, bảng âm S2. | Phần có kiểm độc lập bằng số thì bền. | Tài sản giữ; không làm lại. |
| A9 | fhfa.gov và youtube.com bị proxy chặn; dữ liệu FRED không được commit (repo public, E1-A2). | Ghi nguồn đọc gián tiếp là "đọc qua tìm kiếm"; tải lại bằng `fetch.py --verify`. | DX-H4 theo E1-A2. |
| A10 | "Hiện tại" trong kịch bản trôi theo ngày tải dữ liệu. | Mọi số "hiện tại" phải có **mốc ngày** ghi trong claim và nói ra trong lời hoặc trên màn hình. | C1 chốt mốc ngày. |

## B. Từ Cine Lab (áp được cho Crux)

| # | Bài học | Nguồn | Áp thế nào |
|---|---|---|---|
| B1 | Máy kiểm lời khai thay vì kiểm hình → Goodhart chuyển sang bản khai. | BAI-HOC-BRIEF-D W1 | Đo từ file đã render. |
| B2 | Chỉ tiêu số lượng cho kỹ thuật nghệ thuật khuyến khích nhồi. | W2 | Không quota; mỗi kỹ thuật có lý do. |
| B3 | Luật không phân cấp → sửa lỗi dễ trước, bỏ lỗi quan trọng. | W3 | Chặn / Chính / Tham khảo (K3). |
| B4 | Máy chưa hiệu chuẩn với mắt người → "đạt 71/71" mà phim vẫn dở. | W4 | Luật không phân biệt được bản tốt và bản kém thì hạ cấp. |
| B5 | Một người chấm, không mù → thiên lệch người trong cuộc. | W5 | Kiểm mù ở mọi cổng, agent mới, một file tên ngẫu nhiên, câu hỏi cố định, ghi nguyên văn. |
| B6 | Khoá cứng mà không có người phán quyết khiếu nại. | W6 | Khiếu nại luật đưa lên gói quyết định của cổng kế tiếp. |
| B7 | Phiên kiểm và phiên dựng cùng model → điểm mù chung. | W7 | Khi có thể, kiểm chéo số liệu bằng mã độc lập hoặc nhà cung cấp khác. |
| B8 | Kiểm mù mặt Ida: 2 vòng sửa cùng một trục vẫn 9/10 "búp bê" (đối chứng 0/10). Dừng sau 2 vòng, đưa 3 phương án kèm khuyến nghị. | `reports/m2/MAT-IDA-AI.md` | Tối đa 2 vòng sửa–kiểm; sau đó đưa phương án, kể cả phương án đổi hướng kỹ thuật. |
| B9 | Kiểm mù cần **đối chứng** (mẫu chuyên nghiệp) để biết câu hỏi phân biệt được. | MAT-IDA §1 | Mỗi đợt kiểm mù có ít nhất một mẫu đối chứng khi có mẫu hợp pháp để dùng. |
| B10 | Ảnh tĩnh không đo được cảm xúc đến từ giọng và chuyển động (PA2 "khó đọc" ở ảnh tĩnh, chưa đo khi có tiếng). | MAT-IDA §2 | Duyệt hình bằng clip có chuyển động (G-011). |
| B11 | Truyện phải chốt ở animatic, trước khi tốn công dựng. | KHUNG-CHAT-LUONG §3 | C4 trước C5. |
| B12 | Mọi quyết định sáng tạo ghi AUTHORSHIP kèm đóng góp biểu đạt cụ thể của con người; mọi tài sản vào RIGHTS với nguồn, giấy phép (trích nguyên câu), phạm vi. | CLAUDE.md, AUTHORSHIP.md, RIGHTS.md | `AUTHORSHIP.md`, `RIGHTS.md` ở gốc repo. |

## B2. Bộ đo kiểm mù (Tập 1, C1–C2)

| # | Chuyện đã xảy ra | Bài học |
|---|---|---|
| M1 | Hỏi "muốn xem" từng bản riêng: người đọc vai khán giả đích nói "Yes" với mọi bản (kể cả đối chứng yếu 5/5). | Câu hỏi riêng lẻ bị trần: không phân biệt được. Dùng so cặp ép chọn. |
| M2 | So cặp: đối chứng yếu thắng 19/19 ở cả hai vị trí. P2 ghi "không đạt → C"; chủ dự án sửa: bộ đo đã phân biệt được, chỉ là ứng viên thua. | Tiêu chí "không đạt" phải tách **"không phân biệt được"** với **"ứng viên thua"**. Một bộ đo cho kết quả trái ý đồ vẫn có thể là bộ đo tốt. |
| M3 | Câu hỏi "hiểu" (tóm tắt + đáp án): kịch bản M1b bị chủ dự án chê vẫn được hiểu 3/3. | "Hiểu được" là điều kiện cần, không nói kịch bản hay. Tín hiệu phân biệt nằm ở "chỗ mất chú ý" và "chỗ khó hiểu". |
| M4 | Người đọc vai khán giả đích chọn bản nói với "người như tôi" và cho sẵn ngưỡng tự đối chiếu. | Khớp nhận xét M1 của chủ dự án (G-008) → G-013. |

## B3. Giọng (Tập 1, C3–C4)

| # | Chuyện đã xảy ra | Bài học |
|---|---|---|
| V1 | Giọng B nghe thử (7 câu mới sinh) được chọn; bản đọc cả tập (105 câu, sinh từng câu riêng, 82 câu tái dùng từ C2, nghỉ cố định 0,45 s) bị chê "đều đều, mất nhấn nhá". | Chọn giọng trên một mẫu nhỏ chưa đủ; cách **sinh** (từng câu hay cả cảnh) và cách **ghép** là một phần của giọng. Thử mù phải dùng đúng quy trình sẽ dùng cho cả tập. Kết quả thử mù: chủ dự án thích hai bản sinh theo cảnh (V2, V3) hơn bản từng câu (V1), chọn V3 — theo cảnh + thẻ cảm xúc thưa (G-015 · chọn). Cách chuẩn từ nay. |
| V2 | Chủ dự án chọn trong gói mù rồi mô tả lựa chọn theo tên kiểu ("theo cảnh, không thẻ") — mô tả không khớp nhãn đã giải mã. | Khi câu trả lời về bản mù kèm mô tả, đối chiếu với giải mã trước khi làm; mâu thuẫn thì hỏi lại, không tự chọn. |

## B4. Quyền tài sản

| # | Chuyện | Bài học |
|---|---|---|
| R1 | Phiên K3.1 ghi điểm mù: tài sản bên thứ ba có thể lọt qua máy kiểm nếu nhúng dạng `data:` hoặc ghép hậu kỳ ngoài đường khai báo. | Quy ước ở `quality-framework.md` §8; rà lại ở C5. |

## B5. Vận hành tác vụ dài (Tập 1, C4)

| # | Chuyện đã xảy ra | Bài học | Luật bây giờ |
|---|---|---|---|
| O1 | Sinh giọng v3.2: proxy ngắt kết nối ở cảnh 14/20 (ProxyError RemoteDisconnected), `gen.py` dừng; vòng chờ bên ngoài đợi dòng "calls" không bao giờ tới nên treo; container khởi động lại làm mất mọi tác vụ nền. | Tác vụ dài phải **chạy tiếp được** (bỏ qua phần đã xong, không tốn lại ký tự), **thử lại khi lỗi mạng** (nghỉ 2/4/8/16 s), **commit từng phần**. Mọi vòng chờ phải **có trần thời gian** và **thoát khi tiến trình con chết**, không chờ một dòng log. | Mẫu: `episodes/ep001/work/v32-voice/src/run_resume.sh`; chờ bằng `until xong \|\| ! pgrep … \|\| hết_giờ`. Điểm dừng an toàn trong PLAN.md cập nhật trước mỗi bước dài. |
| O2 | Hai lần vòng chờ treo vì `pgrep -f "<chuỗi>"` khớp nhầm: (1) vòng chờ của luồng P chứa chuỗi "node render.js"; (2) shell nền của P2 chứa "audio/src/mix.py" trong dòng lệnh. Script chờ mãi dù tiến trình thật đã xong. | Mẫu `pgrep -f` phải **neo đầu dòng lệnh** của tiến trình thật (`pgrep -f "^python3 .*mix.py"`, `"^node render.js"`) hoặc chờ theo PID / file kết quả; không bao giờ `pkill -f` một chuỗi có trong chính lệnh đang chạy. | Áp ngay trong `mix_after_render.sh`, `c6_final.sh`. |

## D. Mục tiêu cải tiến cho Tập 2

1. **Hình tự mang ý nghĩa** (chủ dự án, C4 Tập 1): kiểm mù tắt tiếng Tập 1 đạt 20/20 nhưng người đọc hiểu *"mostly from the words and numbers"*; hình mới mang cấu trúc. Tập 2 đặt mục tiêu: nhịp then chốt phải đọc được khi che chữ/số (đo bằng dải che nhãn, có đối chứng).

2. **Tấm nền cho nhãn trên vật liệu 3D** (V08, C6 Tập 1: 349 mẫu chữ < 4,5:1, tệ nhất 2,37:1 — nhãn muted trên gỗ/tường sáng). Mọi chữ đặt trên vật liệu 3D (không phải nền `bg` phẳng) có tấm nền token `bg` (như chữ thumbnail), đo tương phản trên chữ + tấm nền ngay khi dựng cảnh.
3. **Chọn màu nhân vật qua mô phỏng protan/deutan ở C3** (V09: ba màu nhân vật ΔE2000 11,5–18,2 < 20 dưới mô phỏng đỏ-lục, Nora/Walt thang xám 1,27 < 1,5). Ở C3, mọi cặp màu nhân vật phải đạt ΔE2000 ≥ 20 dưới protan và deutan và tương phản thang xám ≥ 1,5:1 trước khi ký hệ hình; hình dạng (tròn/tam giác/vuông) vẫn giữ làm kênh thứ hai.
4. **Bộ dựng tự tránh va chạm nhãn, đệm ≥ 4 px** (V11: 715 va chạm, 714 là nhãn chạm nét đường/trục/dấu 1–2 px). Bộ đặt nhãn của engine giữ khoảng đệm ≥ 4 px với mọi nét đồ hoạ và chữ khác, kể cả khi đường đang vẽ; chạy V11 theo từng cảnh ngay khi dựng, không đợi C5.
5. **Chữ phụ cạnh số nhấn dùng muted** (C05: 1 344 khung, số nhấn in mực trên giấy tối hơn nhãn trắng cạnh nó trong thang xám). Chữ phụ đứng cạnh một số nhấn mạnh dùng màu `muted`, không dùng `text`; số in trên vật liệu sáng (giấy) có tấm nền tối để vẫn là chữ sáng nhất khung.

Nguồn 2–5: bốn luật CHÍNH không đạt ở C6 Tập 1 (K3.3), chủ dự án chấp nhận lời giải thích cho Tập 1 và yêu cầu đưa cách sửa vào playbook (30/09/2026). Lời giải thích: `episodes/ep001/out/explanations.json` (nhánh `ep001-v2`).

## M3. Cổng Mốc 3 (so mù luận điểm máy / đối chứng, 30/09/2026 — `decisions/D-003.md`)

| # | Chuyện đã xảy ra | Bài học |
|---|---|---|
| T1 | Chủ dự án cảm nhận các cặp gần ngang nhau, "nhiều lựa chọn là buộc phải chọn"; chỉ 1/20 cặp chấm hoà, A được chọn 15/19 (máy ở A 6–3, ở B 1–9). | Trang chấm phải **nói rõ "Không phân biệt được" là câu trả lời hợp lệ** (đặt ngang hàng, không phải nút phụ); cân nhắc **thang 5 mức** (A hơn rõ / A hơn chút / ngang / B hơn chút / B hơn rõ). Luôn báo cáo lệch vị trí (tỉ lệ chọn A, kết quả tách theo vị trí). |
| T2 | Thẻ đối chứng thắng nhờ là **một quyết định cụ thể** người xem nhận ra ngay (trả góp hai tuần, vay xe kỳ hạn dài); thẻ máy thường là kết luận thống kê trừu tượng dù có dữ liệu. | Khớp bài học gói phát hành "người như tôi" (G-013): luận điểm phải được **diễn đạt thành quyết định của người xem**; dữ liệu là để bảo vệ luận điểm, không thay cho móc. Đây là điều kiện chạy lại Cổng Mốc 3 (D-003). |

## C. Vận hành

- Chủ dự án không đọc tài liệu dài; chỉ trả lời gói quyết định (≤ 3 câu, < 1 phút đọc).
- Gu (truyện, giọng, hình, âm sắc, nhạc) không bao giờ tự quyết.
- ElevenLabs: tính ký tự mỗi bước vào ledger tập.
