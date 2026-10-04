# C4 gốc — Ý đồ kiểm mù tắt tiếng, GIỮ chữ/số (ghi TRƯỚC khi chạy; không sửa sau)

Lệnh chủ dự án C4b (01/10/2026). Cổng theo `playbook/quality-framework.md` §4: tắt tiếng, từng nhịp, đọc ra ý gì. **Qua khi ≥ 80% nhịp đọc đúng ý đồ**, tức **≥ 6/7 nhịp**. Trượt thì dừng, đưa chủ dự án hai lựa chọn: thiết kế lại các nhịp trượt, hoặc duyệt ngoại lệ có lý do. Không áp phân loại nhịp hồi tố.

**Mẫu:** `animatic/strips/KEY-1.png` … `KEY-7.png`, bản hiện hành (commit eccaae6; 6 khung, **giữ chữ và số trên hình**, không phụ đề lời). Mỗi nhịp **3 người đọc mới** (sonnet), mỗi người một mẫu, file tên hex, thứ tự trộn. **Đối chứng tham khảo** (không tính vào cổng): 7 dải không che của Tập 1 (`episodes/ep001/animatic/strips/S01, S05, S08, S10, S19, S16, S18.png`), mỗi dải 1 người đọc, chấm theo ý đồ tắt tiếng của chính cảnh đó (`episodes/ep001/animatic/intent.md`, cột 1).
**Vai và câu hỏi cố định** (tiếng Anh): *"You are an American planning to start or continue a graduate program who expects to need private loans beyond the federal limit. … This image shows six frames, numbered 1–6 in time order, from a section of a YouTube video about personal finance, watched with the sound off. On-screen text and numbers are visible. In 1–2 sentences: what idea is this section showing — what changes over time, and what does it mean? If you cannot tell, say so."*
**Người chấm:** một agent độc lập, mới, **mù tập**. Agent chỉ đọc một gói gồm câu trả lời và rubric gán nhãn ngẫu nhiên; khoá rubric commit trước khi chấm. Chấm 1 / 0,5 / 0. **Nhịp đọc đúng** khi tổng điểm 3 người đọc **≥ 2**.

## Tiêu chí "đúng nghĩa" vs "chỉ tả hình"
Điểm 1 = nêu đúng **nghĩa** (cột 2). Điểm 0,5 = nêu đúng một trong hai phần nghĩa. Điểm 0 = **chỉ tả hình** (cột 3) hoặc nghĩa khác, dù tả hình đúng.

| Nhịp | Đúng nghĩa (cần đủ) | Chỉ tả hình (= 0) |
|---|---|---|
| KEY-1 | (i) một người cân nhắc **hai khoản vay / hai mức lãi**: một **cố định**, một **thả nổi**; **và** (ii) khoản thả nổi **bắt đầu thấp hơn** khoản cố định rồi lên xuống | "hai tài liệu, một đường phẳng, một đường răng cưa"; "một số dư dao động" |
| KEY-2 | (i) khoảng **chênh giữa lãi cố định và lãi thả nổi lúc bắt đầu** (head start) là thứ được đo; **và** (ii) khoảng đó có thể **lớn, nhỏ, bằng 0 hoặc âm** (thả nổi bắt đầu cao hơn) | "một số dư co lại rồi đổi dấu"; "trả nợ về 0 rồi dư" |
| KEY-3 | (i) lãi thả nổi **vượt mức cố định ở phần lớn** các lần chạy lại; **và** (ii) nhưng chỉ **một phần nhỏ** lần chạy **tốn hơn tổng cộng** (thêm, không bắt buộc: dồn về nửa đầu) | "ô đỏ dồn quanh đỉnh"; "phần lớn ổn, vài giai đoạn xấu" mà không nói thả nổi/cố định hay tổng tiền lãi |
| KEY-4 | (i) khi lãi thả nổi **dưới** mức cố định thì **tích một khoản đệm/tiết kiệm**; khi **trên** thì khoản đệm **bị rút**; **và** (ii) chỉ **tốn hơn** khi khoản đệm **cạn** | "hũ đầy rồi cạn, rồi khối đỏ" không gắn với lãi trên/dưới mức cố định; "lãi cộng dồn làm nợ phình" |
| KEY-5 | (i) **cùng một khoản vay** được **chạy lại** bắt đầu ở **nhiều thời điểm** dọc lịch sử dài (từ 1954); **và** (ii) mỗi kết quả xếp theo **thời điểm bắt đầu** | "cửa sổ trượt trên một biểu đồ thị trường" mà không có khoản vay/chạy lại; "lợi nhuận đầu tư theo thời điểm" |
| KEY-6 | (i) trường hợp **xấu nhất**: bắt đầu **April 1977**, lãi thả nổi **leo cao nhiều năm**; **và** (ii) khoản thả nổi tốn **thêm nhiều tiền lãi so với khoản cố định** (khoảng 43% hơn) | "hai chồng, một chồng có phần đỏ trên" = "gốc và lãi"; "nợ phình" |
| KEY-7 | (i) **head start lớn hơn → ít lần tốn hơn** (gắn với khoảng chênh lúc đầu, không với thời gian/trả nợ); **và** (ii) **hai thời kỳ khác nhau**: **từ 1981** sạch ở khoảng chênh đủ lớn, **1954–1980** không bao giờ sạch hẳn | "cột nợ đỏ được trả dần"; "trả ít thì nợ phình" |

Nguyên văn và hai bảng (chấm độc lập; P chỉ ghi) ở `gates/C4-orig-blind.md`.
