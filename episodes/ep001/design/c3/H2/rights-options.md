# H2 — Phương án quyền cho "bằng chứng" (để chủ dự án chọn)

DESIGNER H2, 29/09/2026. Đầu vào: G-012b ("screenshot bài báo và bằng chứng làm tăng độ tin cậy"). Luật F12 (quyền hình bên thứ ba) **chưa có** trong `checks/` → cần Phiên K3; tài liệu này chỉ là đánh giá của designer, không phải ý kiến pháp lý.

Cách đọc nguồn: "curl trực tiếp" = tải trang và trích nguyên văn hôm nay; "đọc qua tìm kiếm" = câu do WebSearch trả về vì host bị proxy chặn (theo bài học A9); "chưa trích được" = không đọc được.

## Tóm tắt

| | (1) Tài liệu liên bang public domain | (2) Thẻ trích dẫn dựng lại | (3) Screenshot bài báo |
|---|---|---|---|
| Rủi ro bản quyền | Rất thấp (với tài liệu do nhân viên liên bang làm) | Thấp–vừa (tuỳ nguồn câu trích và độ dài) | **Cao** với kênh có quảng cáo |
| Độ tin cậy cảm nhận | Cao (biểu mẫu, trang chính phủ) | Vừa–cao (có tên nguồn, ngày) | Cao nhất (nhận ra mặt báo) |
| Công việc | Dựng lại bố cục hoặc dùng bản PDF gốc | Chữ của mình, font Inter | Chụp + làm mờ + xin phép |
| Dùng trong 3 khung mẫu | F2 (Closing Disclosure, câu CFPB) | F2 (thẻ câu CFPB, chữ dựng lại); F1 (dòng nguồn FRED) | **Không** |

**Khuyến nghị:** lấy (1) làm xương sống (Closing Disclosure / Loan Estimate mẫu của CFPB, trang HMDA, thông cáo FHFA — sau khi trích được giấy phép FHFA), dùng (2) cho các câu trích ngắn có nguồn rõ, ưu tiên nguồn thuộc (1); **không** dùng (3) cho Tập 1 — nếu cần cảm giác "tin nóng", dựng thẻ tiêu đề bằng chữ của mình kèm tên nguồn và ngày (loại 2), không chụp mặt báo.

---

## (1) Tài liệu liên bang public domain

**Ví dụ dùng được cho Tập 1**
- Mẫu **Closing Disclosure** của CFPB (mục "Loan Costs", dòng "D. TOTAL LOAN COSTS (A + B + C)") — điền số của Nora. Danh mục mẫu: https://www.consumerfinance.gov/compliance/compliance-resources/mortgage-resources/tila-respa-integrated-disclosures/forms-samples/ (có mẫu trống, mẫu điền sẵn, bản chú thích `201312_cfpb_tila-respa_annotated-closing-disclosure.pdf`; đã thấy liên kết bằng curl, chưa tải PDF). Đã dựng lại ở **F2**.
- Câu định nghĩa của CFPB (curl trực tiếp, https://www.consumerfinance.gov/ask-cfpb/what-is-a-closing-disclosure-en-1983/): *"A Closing Disclosure is a five-page form that provides final details about the mortgage loan you have selected. It includes the loan terms, your projected monthly payments, and how much you will pay in fees and other costs to get your mortgage (closing costs)."* — dùng câu đầu ở **F2**.
- Trang dữ liệu **HMDA** (ffiec.cfpb.gov) — nguồn phí $5,124 / $3,667 / $5,514; có thể quay trang Data Browser hoặc định nghĩa trường `total_loan_costs` (câu đã có ở `data/hmda-sources.json`).
- **FHFA** thông cáo hạn mức conforming 2026 ($832,750) — cho câu Anjali "under the conforming limit".

**Giấy phép (trích nguyên câu)**
- CFPB (curl trực tiếp 29/09/2026, https://www.consumerfinance.gov/privacy/website-privacy-policy/, mục Legal notices › Copyright and trademark): *"Website content: Information created by the CFPB is in the public domain and you may reproduce, publish, or otherwise use it without the Bureau's permission."* và *"Please consider appropriate citation to the Bureau as the source."* (câu thứ hai trích ngày 28/09 ở `data/hmda-sources.json`).
- Cùng trang, giới hạn: *"Copyrighted materials created by entities outside of the Bureau also may appear on this website, or may be reached through a link on this website."* và *"The Bureau's logo, as well as the names Consumer Financial Protection Bureau and CFPB are registered trademarks."*
- Luật gốc 17 U.S.C. §105 (đọc qua tìm kiếm; uscode.house.gov, law.cornell.edu, govinfo.gov bị proxy chặn): *"Copyright protection under this title is not available for any work of the United States Government, but the United States Government is not precluded from receiving and holding copyrights transferred to it by assignment, bequest, or otherwise."* — https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title17-section105
- FHFA: **chưa trích được** (fhfa.gov bị proxy chặn: "EGRESS_BLOCKED"); RIGHTS.md dòng D-FHFA cũng ghi chưa trích.
- **Không phải public domain:** Freddie Mac PMMS qua FRED — *"Copyrighted: Citation required … you may use these data series with proper attribution of the source and acknowledgment that you obtained the data from FRED"* (RIGHTS.md D-FRED-1). Được hiển thị số/biểu đồ kèm "Source: Freddie Mac via FRED"; **không** chụp trang freddiemac.com hay biểu đồ FRED (cấm "Redistribute any third party's proprietary content, including any graphs…"). Bản in lãi tuần ở F1 là **biểu đồ do ta vẽ** từ dữ liệu tải về, không phải ảnh chụp.

**Rủi ro**
- Logo và tên CFPB là nhãn hiệu: không đặt logo lên hình, không làm như CFPB xác nhận video. Chỉ ghi nguồn bằng chữ.
- Trang .gov có thể chứa ảnh/tài liệu của bên thứ ba (câu "Copyrighted materials created by entities outside…") → chỉ dùng phần do CFPB tạo (biểu mẫu, văn bản).
- Biểu mẫu điền số nhân vật có thể bị hiểu là hồ sơ thật → luôn có dấu ILLUSTRATIVE và chú thích "Layout after the CFPB model form".
- FHFA: là cơ quan liên bang nên nhiều khả năng thuộc §105, nhưng chưa trích được câu giấy phép → chờ chủ dự án xác minh như đã làm với số $832,750.

**Cách hiển thị**
- Dựng lại bố cục bằng chữ Inter trên "giấy" (như F2) hoặc đặt bản PDF gốc lên bàn (cần công cụ rasterize PDF; máy chưa có pdftoppm).
- Chân tờ giấy: "Layout after the CFPB model Closing Disclosure. Loan costs: 2025 median, CFPB HMDA." Không logo.

## (2) Thẻ trích dẫn dựng lại (không chụp màn hình)

**Ví dụ dùng được cho Tập 1**
- Thẻ câu CFPB ở **F2** (nguồn thuộc loại 1 → rủi ro gần 0): chữ của câu trích, đặt trong thẻ tối màu `surface`, vạch `accent`, dòng nguồn "— CFPB, consumerfinance.gov · 'What is a Closing Disclosure?'".
- Dòng thời sự cho cold open (S01): thay vì chụp tin "lãi vượt 7%" (24/9/2026), dựng thẻ **bằng lời của mình và số của mình**: "Sept 24, 2026 · 30-year fixed average 7.03% — first time above 7% since January 2025 · Source: Freddie Mac via FRED". Đây là **dữ kiện**, không phải câu trích của báo → không có biểu đạt của bên thứ ba.
- Nếu muốn trích một câu báo chí thật: một câu ngắn (≤ 1–2 dòng), có tên báo, ngày, tiêu đề bài; chỉ khi câu đó là đối tượng được bình luận trong lời (ví dụ quy tắc "1 điểm" — hiện **không có nguồn**, `numbers.md` mục cuối).

**Giấy phép**
- Không có giấy phép; dựa vào **fair use**. 17 U.S.C. §107 (đọc qua tìm kiếm; law.cornell.edu, copyright.gov bị chặn): *"the fair use of a copyrighted work, including such use by reproduction in copies or phonorecords or by any other means specified by that section, for purposes such as criticism, comment, news reporting, teaching (including multiple copies for classroom use), scholarship, or research, is not an infringement of copyright."* Bốn yếu tố: mục đích và tính chất (kể cả thương mại), bản chất tác phẩm, lượng và phần cốt lõi được dùng, ảnh hưởng tới thị trường. — https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title17-section107
- Dữ kiện (con số, ngày) không được bảo hộ bản quyền; cách diễn đạt thì có.

**Rủi ro**
- Kênh có quảng cáo → yếu tố 1 nghiêng về thương mại; bù lại bằng tính bình luận/giải thích và trích rất ngắn.
- Trích sai chữ hoặc gán sai nguồn là rủi ro uy tín lớn hơn rủi ro bản quyền → mỗi thẻ cần một dòng trong RIGHTS.md với câu nguyên văn + URL + ngày đọc, và claim ID nếu có số.
- Dùng font/màu/bố cục gợi đến thương hiệu một tờ báo → không; thẻ luôn theo token kênh.

**Cách hiển thị**
- Thẻ trên bàn (vật thể giấy/bìa), chữ Inter 600, ngoặc kép, dòng nguồn `ink-muted` gồm tổ chức + trang + ngày đọc. Tối đa ~25 từ. Không logo, không ảnh chụp.

## (3) Screenshot bài báo

**Ví dụ:** trang tin ngày 24/9/2026 "Mortgage rates top 7%…" (báo lớn, có ảnh, logo, byline).

**Giấy phép:** không có giấy phép dùng lại; trang báo lớn thường giữ mọi quyền. Điều khoản của các báo cụ thể: **chưa trích được** (cnbc.com, apnews.com, reuters.com bị proxy chặn khi thử 29/09/2026). Chỉ còn đường fair use (§107 ở trên) hoặc xin phép / mua giấy phép.

**Rủi ro**
- Ảnh chụp màn hình sao chép cả tiêu đề, dàn trang, **ảnh báo chí** (thường của hãng ảnh — rủi ro cao nhất) và logo (nhãn hiệu).
- Kênh có quảng cáo: yếu tố thương mại; dùng mặt báo để "tăng uy tín" là trang trí, không phải bình luận chính nội dung bài → yếu tố 1 yếu.
- Content ID / khiếu nại bản quyền trên YouTube có thể làm mất doanh thu hoặc cảnh cáo kênh (chính sách YouTube: **chưa trích được**, youtube.com bị chặn).
- Tin lãi 7% đã có trong dữ liệu của ta (claim `r_today`, `first7_since`) → screenshot không thêm dữ kiện nào; lợi ích chỉ là cảm giác.

**Nếu vẫn muốn dùng:** làm mờ ảnh báo và logo, chỉ giữ tiêu đề và ngày, xin phép bằng văn bản, ghi vào RIGHTS.md; hoặc dựng **bài báo giả ghi rõ MOCKUP** chỉ để thử gu (H2 không dựng trong đợt này: ba khung mẫu chỉ dùng loại 1 và 2).

## Khuyến nghị của H2
Chọn **(1) + (2)**: tài liệu liên bang (CFPB/FFIEC/FHFA) làm "bằng chứng" chính và thẻ trích dẫn dựng lại bằng chữ của mình cho câu ngắn và dữ kiện thời sự; không dùng screenshot bài báo ở Tập 1. Việc cho Phiên K3: luật F12 = "mọi ảnh/tài liệu bên thứ ba trên hình phải có dòng RIGHTS với câu giấy phép nguyên văn; screenshot báo chí = Chặn trừ khi có giấy phép bằng văn bản".
