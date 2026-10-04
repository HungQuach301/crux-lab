# C6 — So cặp mù gói phát hành: ý đồ (ghi TRƯỚC khi chạy; không sửa sau khi thấy kết quả)

Ngày 01/10/2026, PACKAGING C6, nhánh `ep002`. **THAM KHẢO**: chủ dự án chọn theo gu (`playbook/packaging.md` §1.8, §6.4). Phép đo thật là Test & Compare sau khi đăng.
Áp bài học Tập 1 (`packaging.md` §6): (2) vai người đọc **hỗn hợp**, chia đều, báo theo vai và tổng; (3) **tách** tiêu đề khỏi thumbnail bằng hai vòng riêng.

## Vật liệu
- Ảnh = 2 thẻ kết quả tìm kiếm YouTube chồng nhau, nhãn 1 (trên) và 2 (dưới). Mỗi thẻ: thumbnail 640×360 + thời lượng 9:45 (`out/video.mp4` 585,6 s) + tiêu đề + tên kênh "Crux". Mỗi cặp có cả hai thứ tự. Tên ảnh hex ngẫu nhiên; khoá `key.json` chỉ mở sau khi đủ câu trả lời. Dựng: `preprod/thumbs_c6/pack_test.js`.
- **Vòng T — tiêu đề** (thumbnail CỐ ĐỊNH, trung tính: nền KEY-3 không chữ + huy hiệu, `preprod/thumbs_c6/work/thumb-neutral.png`):
  - **A1** "Need Private Grad Loans? Variable vs Fixed Through History" (tiêu đề nháp chủ dự án chọn ở C1)
  - **A2** "No Grad PLUS? How Much Lower a Variable Rate Had to Start" (cùng hướng "người như tôi" + lời hứa đáp án)
  - **WT** (đối chứng yếu) "Indexed Rate Paths vs Level Rates: A Backtest" (thuật ngữ, không gọi người xem, không hứa đáp án)
  - 3 cặp × 2 thứ tự = **6 ảnh**.
- **Vòng M — thumbnail** (tiêu đề CỐ ĐỊNH: A1 trên cả hai thẻ):
  - **thumb-1** hai lời mời ("9%" · "7.5%"), **thumb-2** lịch sử ("14.2% cost more"), **thumb-3** giai đoạn tệ nhất ("April 1977" · "43% more"); cả ba có huy hiệu ILLUSTRATIVE.
  - **WM** (đối chứng yếu): một khung phim KEY-2 nguyên trạng, chữ nhãn 36 px, không chữ thumbnail (`preprod/thumbs_c6/work/thumb-control.png`).
  - 6 cặp × 2 thứ tự = **12 ảnh**.

## Người đọc
Agent **mới** cho mỗi lượt đọc, `claude -p --model sonnet` (khác model bên dựng), chỉ công cụ `Read`, chạy trong một thư mục tạm chỉ chứa **một** ảnh tên hex (không thấy tên gói, khoá, hay ảnh khác). Mỗi ảnh được **4 vai** đọc (mỗi vai một agent) → vòng T 24 lượt, vòng M 48 lượt, tổng 72.

Vai (nguyên văn, tiếng Anh), chia đều tuyệt đối (mỗi vai thấy mọi ảnh đúng một lần):
- **G — grad student:** "You are an American starting a graduate program next year; federal loans will not cover the full cost, so you expect to need private student loans."
- **P — parent / co-signer:** "You are an American parent who may co-sign your child's private loan for graduate school."
- **R — refinancing:** "You are an American who already has student loans and is looking at refinancing them with a private lender."
- **C — curious:** "You are an American who watches personal-finance videos out of curiosity and has no student loans right now."

Câu hỏi cố định (dán nguyên văn sau câu vai):
> You are scrolling YouTube search results for "private student loans". Open the image file in this folder with the Read tool: it shows two search results, labelled 1 (top) and 2 (bottom). Which one of these two videos would you click? Reply in exactly two lines: `ANSWER: 1` or `ANSWER: 2`, then `WHY: <one sentence>`.

## Cách tính (máy, không tự chấm)
- Mỗi lượt: ô được chọn (1/2) → giải mã bằng `key.json` → mục thắng. Lý do giữ nguyên văn.
- Báo cho mỗi vòng: số thắng / số lần xuất hiện của mỗi mục, **theo từng vai và tổng**; lệch vị trí (tỉ lệ chọn ô 1); mỗi cặp: thắng ở cả hai thứ tự hay đổi theo vị trí.
- Không có ngưỡng "đạt". Chênh ≤ 2 lượt trong một vai không có ý nghĩa.

## Dự đoán ghi trước (để biết bộ đo có phân biệt không)
- **Đối chứng yếu WT, WM** thua phần lớn lượt (≤ 25% tổng mỗi cái). Nếu một đối chứng yếu đạt ≥ 50% tổng, báo "bộ đo không phân biệt được" cho vòng đó, không diễn giải thứ hạng.
- Không dự đoán thứ hạng giữa A1/A2 hay giữa ba thumbnail.
- Có thể có lệch vai: vai G và P được A2 "No Grad PLUS?" gọi đúng hơn; vai R (refinance) và C có thể ít thấy mình trong cả hai. Ghi lại, không sửa vai sau khi thấy kết quả.

## Giới hạn biết trước
- Agent đóng vai, không phải người xem thật. Ảnh thẻ to hơn thẻ trên điện thoại.
- Vòng M dùng tiêu đề A1 cố định; thumbnail thắng với A1 chưa chắc thắng với A2 (chưa chạy lưới đầy đủ tiêu đề × thumbnail, §3 L3 (iii) — chỉ làm nếu chủ dự án cần).
- Thumbnail trung tính của vòng T có huy hiệu ILLUSTRATIVE trên cả hai thẻ (giống nhau nên không lệch cặp).
