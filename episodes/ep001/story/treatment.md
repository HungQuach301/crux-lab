# Tập 1 — Treatment (vòng 2)

Nhân vật: **Nora** (khoản trung vị), **Walt** (khoản nhỏ), **Anjali** (khoản lớn, vẫn dưới hạn mức conforming). Cả ba là ILLUSTRATIVE: người giả định, khoản vay và phí là trung vị HMDA thật. Mọi số kèm claim ID từ `numbers.md`; ID chưa có ghi ở cuối `beats.md`.

---

Tuần kết thúc 7/1/2021, lãi cố định 30 năm trung bình chỉ 2.65% [low] [low_date], thấp nhất kể từ 1971 [y1971]. Trong gần ba năm sau đó lãi đi lên là chính, và cuối tháng 10/2023 chạm 7.79% [peak2023], cao nhất kể từ năm 2000 [peak2023_since]. Người ta vẫn cần nhà: cứ mười khoản vay mua nhà năm 2023 thì ba khoản có lãi từ 7% trở lên [purch23_ge7]. Đây là lịch sử, không phải dự báo, và chỉ nói về nước Mỹ.

Nora là một trong số đó. Tháng 10/2023 [oct2023], cô chuyển thành phố vì công việc mới và mua căn nhà đầu tiên, với khoản vay $375,000 [loan_median] ở mức 7.62% [r_old]. Giờ ngân hàng gửi cô một đề nghị vay lại, tức là một khoản vay mới để trả hết khoản cũ. Lãi đề nghị bám mức trung bình của tuần kết thúc 24/9/2026, 7.03% [r_today], thấp hơn lãi của cô 0.59 điểm phần trăm [cut_today]. Mỗi tháng cô trả ít hơn $221 [sav_median]. Nhưng đi kèm là hoá đơn phí khoản vay $5,124 [cost_median], trả bằng tiền mặt. Cả hai là trung vị thật của gần nửa triệu khoản vay lại năm 2025 [n31].

Cô nghe hai câu trả lời. Quy tắc truyền miệng bảo chờ lãi giảm đủ một điểm phần trăm [s10], nên đề nghị này chưa đạt. Phép chia thì nói khoảng 24 tháng [be_simple_median]. Hai câu không khớp, và cả hai thiếu một thứ.

Thứ bị thiếu là đồng hồ 30 năm. Nora đã trả 35 kỳ [k35]; khoản mới bắt đầu lại 30 năm [term30], những năm đầu tiền trả chủ yếu là lãi, nên nợ giảm chậm hơn. Đến tháng 24, cô còn nợ nhiều hơn $1,133 [gap24] so với nếu giữ khoản cũ. Tính cả phần đó, hoà vốn đến ở tháng 30 [be_bal_median]. Với một phần tư điểm [s025], phép chia hứa 38 tháng [be_simple_025], nhưng tính cả dư nợ thì không hoà vốn trước ngày khoản cũ lẽ ra đã trả xong [be_bal_025]. Với nửa điểm [s05], cô cần đúng 36 tháng [be_bal_05]. Vậy ngưỡng ba năm [hold36] của Nora là nửa điểm [cut36_median], chỉ bằng một nửa quy tắc.

Nhưng nửa điểm có phải ngưỡng của mọi người không? Walt cũng vay tháng 10/2023 và nhận lá thư tương tự. Khoản của anh chỉ $115,000 [loan_small], vậy mà hoá đơn vẫn $3,667 [cost_small]. Phần lớn hoá đơn trả cho xử lý hồ sơ và dịch vụ, tốn gần như nhau dù khoản vay lớn hay nhỏ. Với Walt, hoá đơn bằng khoảng 3.2% khoản vay [share_walt]. Cùng mức giảm, anh chỉ bớt $68 mỗi tháng [sav_small], nên phải đợi 75 tháng [be_bal_small]. Nếu bán nhà sau ba năm [y3], anh lỗ $1,777 [net36_small]. Ngưỡng ba năm của anh là 1.12 điểm [cut36_small], cao hơn cả quy tắc.

Anjali ở đầu kia: cùng tháng, cùng mức giảm, khoản $655,000 [loan_large], vẫn dưới hạn mức conforming. Hoá đơn của cô là $5,514 [cost_large], gần bằng của Nora, nhưng khoản vay lớn hơn nhiều nên mỗi tháng cô bớt $387 [sav_large]. Ngưỡng của cô chỉ là 0.32 điểm [cut36_large].

Vậy đáp án không phải một con số chung: khoảng một phần ba điểm với Anjali, nửa điểm với Nora, hơn một điểm với Walt. Quy tắc một điểm không vừa với ai. Giới hạn: lãi trung bình, phí trung vị, ba hộ giả định. Câu còn lại thuộc về người xem: bạn định ở căn nhà này bao lâu? Nếu Nora bán sau ba năm, cô dư $1,039 [net36_median]; nếu ở bảy năm [y7], cô dư $8,093 [net84_median].

---

## Changelog (vòng 2, theo `critic-r1.md` và quyết định điều phối)

- Sửa lỗi thời gian "Ba năm trước… 2021" và "leo lên không ngừng" (thành "đi lên là chính"); 2.65% ghi là mức của một tuần.
- Gộp bối cảnh hồi 1 thành một beat; bỏ beat "một năm lên xuống" (6.30%); 7.03% vào beat đề nghị, $221 đến trước 1:30.
- Nora có chi tiết đời thường (chuyển thành phố vì việc mới, căn nhà đầu tiên). Câu tạo lòng tin với [n31].
- Định nghĩa bằng lời thường: "refinance", "percentage point" (khác discount points), "khởi động lại đồng hồ 30 năm".
- Walt: dùng tỉ lệ riêng của anh (~3.2%, ID tạm `share_walt`), không dùng trung vị nhóm; giải thích vì sao phí gần như cố định. Anjali: "vẫn dưới hạn mức conforming", cùng tháng, cùng mức giảm.
- "Never" được thu hẹp: không hoà vốn trước ngày khoản cũ lẽ ra trả xong.
- Bỏ "six extra months" (không có claim). Bỏ đoạn 13 đợt lịch sử khỏi lời; chuyển vào thẻ phương pháp.
- Hồi 3 kể thành chuyện: câu hỏi riêng ("nửa điểm có phải ngưỡng của mọi người?"), bước ngoặt (phí không co theo khoản vay), mỗi câu tối đa một số.
- Cold open: hai bản 45–55 từ; hoá đơn $5,124 chỉ hiện trên màn hình. B dựng lại: bối cảnh là quy tắc một điểm, rồi Nora và lá thư.
- Gắn đủ claim ID; ID thiếu liệt kê cuối `beats.md`.
