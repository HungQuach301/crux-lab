# Ý đồ — hiệu chuẩn bộ đo hấp dẫn (Mốc B, việc 4) · ghi TRƯỚC khi chạy, 2026-10-05

**Câu hỏi:** bộ đo đọc mù (agent mới, chấm độc lập) có **tách được** bản gốc với bản làm kém có kiểm soát của **cùng** kịch bản không? Theo `quality-framework.md` §2.8, thước đo mới phải hiệu chuẩn trên đối chứng đã biết kết quả trước khi được dùng. Lần hiệu chuẩn trước (Tập 3, C3/C4) hiệu chuẩn bộ đo câu khuyên; giới hạn của nó là đối chứng âm phải **cùng chủ đề**. Lần này cả hai bản đều cùng chủ đề và cùng dữ kiện.

## Mẫu
- **Bản gốc:** lời cuối Tập 2 và Tập 3 (`episodes/epNNN/out/script.json` → `orig-epNNN.txt`), mỗi câu kèm mốc thời gian thật.
- **Bản làm kém** (`degr-epNNN.txt`): một agent dựng (không phải người đọc) làm **đúng ba thao tác**, giữ nguyên dữ kiện, không thêm claim, độ dài ±10 %:
  1. **Bỏ móc 5 s:** 30 s đầu không còn câu được–mất, câu hỏi hay lời hứa. Mở bằng bối cảnh hoặc định nghĩa trung tính. Câu hỏi và lời hứa của tập dời xuống sau ~1:00 hoặc bỏ.
  2. **Dồn số:** gom các câu nêu số thành từng cụm liền nhau, mỗi cụm ≥ 3 số; bỏ câu thở ngay sau số quyết định.
  3. **Bỏ callback:** lần nhắc lại con số cốt lõi về sau được thay bằng câu trung tính, hoặc bỏ đi.
  Mốc thời gian của bản làm kém ước theo tốc độ đọc của tập (Tập 2: 129 wpm; Tập 3: 145 wpm).

## Người đọc (Sonnet, mỗi người là một agent mới, chỉ thấy một văn bản, không có ngữ cảnh dự án)
- **A. Đọc trọn (bộ đo bỏ xem):** mỗi tập 3 người đọc bản gốc và 3 người đọc bản làm kém. Câu hỏi cố định (tiếng Anh, vai khán giả đích: người Mỹ 30–55 tuổi có tiền tiết kiệm/khoản vay):
  - (1) điểm móc 1–5 sau 30 s đầu;
  - (2) id câu mà người đọc nhiều khả năng **bỏ xem**, hoặc NONE;
  - (3) id câu đầu tiên chú ý tụt;
  - (4) một câu lý do.
- **B. So cặp móc:** mỗi tập 3 người đọc xem 30 s đầu của hai bản (nhãn X/Y, thứ tự ngẫu nhiên), chọn bản khiến họ xem tiếp.

## Thước đo và ngưỡng (ghi trước)
- **Bỏ xem:** vị trí bỏ = % số từ của kịch bản tính tới câu bỏ xem (NONE = 100 %). Một tập **tách được** khi trung bình vị trí bỏ của bản gốc − bản làm kém **≥ 15 điểm %**.
- **Móc:** một tập **tách được** khi trung bình điểm móc của bản gốc − bản làm kém **≥ 1,0** **và** so cặp chọn bản gốc **≥ 2/3**.
- **Kết luận:**
  - Một bộ đo **ĐẠT** khi tách được ở **cả hai tập**. Hai bộ đo kết luận riêng.
  - Bộ đo móc ĐẠT → dùng tự động ở C2 (THAM KHẢO) và để chọn móc (Mốc B, việc 3).
  - Bộ đo bỏ xem ĐẠT → báo điểm rời dự kiến ở C2 (THAM KHẢO).
  - Không đạt → ghi vào `playbook/lessons.md`, không dùng.
- Hiệu số trong ±5 % quanh ngưỡng phải nêu tên.

## Không làm
- Không sửa ý đồ sau khi thấy kết quả. Không chạy thêm người đọc để cứu một bộ đo trượt.
- Không đọc nguyên văn trả lời vào gói; gói chỉ lấy bảng tổng (`RESULT.md`).
- Người dựng bản làm kém không là người đọc. Phiên điều phối chỉ gộp số.
