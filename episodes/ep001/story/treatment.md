# Tập 1 — Treatment

Nhân vật: **Nora** (khoản trung vị), **Walt** (khoản nhỏ), **Anjali** (khoản lớn conforming). Cả ba là ILLUSTRATIVE: người giả định, khoản vay và phí là trung vị HMDA thật. Mọi số kèm claim ID từ `numbers.md`.

---

Ba năm trước, người Mỹ mua nhà trong một thế giới lãi suất rất khác. Tháng 1/2021, lãi vay 30 năm trung bình chỉ 2.65% [low] [low_date], mức thấp nhất từ 1971. Rồi lãi leo lên không ngừng, và cuối tháng 10/2023 chạm 7.79% [peak2023], cao nhất kể từ năm 2000 [peak2023_since]. Trong số khoản vay mua nhà năm 2023, cứ mười khoản thì ba khoản có lãi từ 7% trở lên [purch23_ge7]. Nếu người xem là một trong số họ, câu chuyện này là của họ. Đây là lịch sử, không phải dự báo, và chỉ nói về nước Mỹ.

Nora là một người như thế. Cô vay $375,000 [loan_median] vào tháng 10/2023 [oct2023], đúng mức trung bình tháng đó là 7.62% [r_old]. Suốt một năm qua cô nhìn lãi đi xuống rồi đi lên: 6.30% một năm trước [r_year_ago], rồi lại 7.03% trong tuần kết thúc 24/9/2026 [r_today]. Giờ ngân hàng gửi cô một đề nghị vay lại. Lãi thấp hơn 0.59 điểm [cut_today], mỗi tháng trả ít hơn $221 [sav_median]. Nhưng đi kèm là hoá đơn phí khoản vay $5,124 [cost_median], trả ngay. Câu hỏi của cô: lãi phải giảm bao nhiêu thì khoản phí này mới quay về túi mình?

Cô nghe hai câu trả lời. Câu thứ nhất là một quy tắc truyền miệng: đợi lãi giảm đủ một điểm [s10]. Theo quy tắc ấy, 0.59 điểm là chưa đủ. Câu thứ hai là phép chia ai cũng làm được: $5,124 chia $221, khoảng 24 tháng [be_simple_median] là hoà vốn. Hai câu trả lời không khớp nhau, và cả hai đều thiếu một thứ.

Bước ngoặt nằm ở dư nợ. Nora đã trả gần ba năm [k35]; khoản mới bắt đầu lại 30 năm nên gốc giảm chậm hơn khoản cũ. Đến tháng 24, dư nợ khoản mới cao hơn khoản cũ $1,133 [gap24], đúng phần mà phép chia bỏ quên. Tính cả phần đó, Nora hoà vốn ở tháng 30 [be_bal_median], không phải tháng 24. Nếu lãi chỉ giảm một phần tư điểm, phép chia hứa 38 tháng [be_simple_025], nhưng tính cả dư nợ thì không bao giờ hoà vốn [be_bal_025]. Với nửa điểm, cô cần đúng 36 tháng [be_bal_05]. Vậy với Nora, nếu muốn phí quay về trong ba năm, mức giảm cần là nửa điểm [cut36_median], chỉ bằng một nửa quy tắc một điểm.

Rồi câu chuyện đổi người. Walt vay $115,000 [loan_small], nhưng phí của anh vẫn $3,667 [cost_small], tức 3.4% khoản vay [share_small]. Cùng mức giảm như Nora, anh chỉ bớt $68 mỗi tháng [sav_small] và phải chờ 75 tháng [be_bal_small]. Nếu bán nhà sau ba năm, anh lỗ $1,777 [net36_small]. Để hoà vốn trong ba năm, anh cần lãi giảm 1.12 điểm [cut36_small], nhiều hơn cả quy tắc. Anjali thì ngược lại: khoản $655,000 [loan_large], phí $5,514 [cost_large], mỗi tháng bớt $387 [sav_large], hoà vốn ở tháng 18 [be_bal_large]; cô chỉ cần 0.32 điểm [cut36_large].

Lịch sử cũng vậy: từ 1971 có 13 đợt lãi giảm ít nhất một điểm [n_eps], và trong 3 đợt [n_further] lãi còn giảm thêm một điểm trước khi kịp hoà vốn.

Đáp án cuối cùng không phải một con số chung. Mức giảm cần thiết là 0.32, 0.5 hay 1.12 điểm tuỳ khoản vay, và quy tắc một điểm không vừa với ai. Giới hạn: lãi trung bình, phí trung vị, ba hộ giả định. Câu hỏi còn lại thuộc về người xem: bạn định ở lại căn nhà này bao lâu? Với Nora, bán sau ba năm thì lời $1,039 [net36_median]; ở bảy năm thì lời $8,093 [net84_median].
