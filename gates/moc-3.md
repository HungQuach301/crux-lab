# Cổng Mốc 3 — định nghĩa (chép nguyên văn)

Nguồn: [crux-studio](https://github.com/HungQuach301/crux-studio) (nhà máy cũ, đã đóng băng, chỉ đọc), file `docs/spec/CRUX-REFERENCE-SPEC.md`.
- HEAD crux-studio lúc chép: `c7cadd7d99a6c63e674b5c587108f8e5efda3d50` (2026-09-28 09:41 UTC).
- Commit gần nhất sửa file spec: `5c133eb5d43d47485f805f4187b54dc224f3ca2c` (2026-09-21), nên nội dung giống hệt ở hai commit.
- Chép ngày 2026-09-28, Phiên D1. Không sửa chữ nào; chỉ thêm dòng "Nguồn" in nghiêng trước mỗi khối.

Bốn phần:
1. mục "Cổng Mốc 3 — cổng quan trọng nhất" (khối `engine/docs/12-success-criteria.md`): điều kiện đầu vào, sản lượng, cách chấm mù, ngưỡng, ba kết quả;
2. bảng "Điều kiện dừng" của cùng khối;
3. mục 2 "Thư viện mô hình" của khối `engine/docs/14-quantitative-core.md`, vì điều kiện đầu vào 2 trỏ tới "kiểm theo bốn cấp" ở đó;
4. mục 7 "Definition of Done" của `WP-015` (Thesis Engine), vì nó nói số thesis đem chấm mù.

Lưu ý khi đọc: trong "Cách chấm — chấm mù", danh sách đánh số của bản gốc đi 1, 2, 3, 4, 5 rồi lại 3, 4. Giữ nguyên như bản gốc.

---

*Nguồn: spec dòng 1597–1685 (đến trước dấu `---` kết mục), khối `engine/docs/12-success-criteria.md`.*

## Cổng Mốc 3 — cổng quan trọng nhất

Không sang Mốc 4 nếu không đạt đủ năm điều.

### Điều kiện đầu vào — phải có trước khi chấm

Năm nguồn thesis chỉ hoạt động được khi kho dữ liệu đủ dày. Đầu vào tối thiểu:

1. Kho ảnh chụp có **≥30 chuỗi** từ **≥4 nhà cung cấp**, cơ chế phát hiện thay đổi hoạt động.
2. **≥8 mô hình** trong thư viện, mỗi mô hình qua được kiểm theo bốn cấp (xem
   `14-quantitative-core.md` mục 2).
3. Sensitivity Pass tìm được điểm đảo chiều thật trên **≥4 mô hình**.
4. Corpus đối thủ có **≥200 video**, kiểm mới lạ tự động chạy được.

### Điều kiện sản lượng

5. Thesis Engine sinh **20 thesis** hợp lệ theo schema, trong đó:
   - **Nguồn 2 (ngưỡng ẩn) và nguồn 3 (câu hỏi chưa ai trả lời) bắt buộc** sinh tổng cộng
     ≥15 thesis.
   - Nguồn 1, 4, 5 **được phép rỗng ở Mốc 3** và đo lại ở Mốc 7. Lý do: nguồn 1 cần nhiều
     cặp chuỗi đo cùng hiện tượng, nguồn 4 cần bình luận, nguồn 5 chỉ cho thời điểm chứ không
     cho luận điểm — bắt cả năm nguồn phải có ở Mốc 3 là đặt dự án vào thế fail vì thiếu
     nguyên liệu chứ không vì ý tưởng kém.

### Cách chấm — chấm mù

Vấn đề của việc chủ dự án chấm trực tiếp: toàn bộ dự án được thiết kế để bù cho việc chủ dự
án không sống ở thị trường Mỹ — nên bước đo này không được để một mình người đó chấm trực
tiếp. Cách chấm là so sánh mù:

1. Tạo **20 thesis đối chứng** từ một mô hình khác, giới hạn "10 phút suy nghĩ", **không cho
   xem dữ liệu của kho ảnh chụp**.
2. **Chuẩn hoá thẻ trước khi trộn.** Cả hai bên viết cùng một khuôn: một câu luận điểm, một
   câu niềm tin bị phản bác, cùng độ dài, **không bên nào hiển thị con số cụ thể**. Nếu một
   bên có số và bên kia chỉ có câu hỏi thì xoá nhãn không làm mù được gì — người chấm nhận ra
   ngay bên nào là máy.
3. **Ghép cặp theo trụ nội dung.** Mỗi cặp hai thesis cùng một trụ trong năm trụ. Không so
   một thesis về nhà ở với một thesis về hưu trí.
4. Trộn, xoá mọi nhãn nguồn gốc, đánh số ngẫu nhiên.
5. **Hoà được phép.** Người chấm có ba lựa chọn: A tốt hơn, B tốt hơn, hoặc không phân biệt
   được. Cặp hoà không tính vào mẫu số.
3. Chủ dự án chấm từng cặp, không biết cái nào của ai, theo một câu hỏi duy nhất: *cái này có
   sắc hơn thứ một người đọc tin tài chính nghĩ ra trong mười phút không?*
4. Nếu có thể, một người sống ở thị trường Mỹ chấm song song; chỗ bất đồng được ghi lại.

### Ngưỡng qua cổng

| Điều kiện | Ngưỡng |
|---|---|
| Tỷ lệ máy thắng trong so sánh mù, tính trên các cặp không hoà | ≥60% |
| Số thesis máy đạt chuẩn theo rubric | **≥15/20** |

**Đây là một phép sàng lọc, không phải một phép kiểm có ý nghĩa thống kê.** Với 20 cặp độc
lập, hai bên ngang nhau, xác suất máy thắng từ 12 cặp trở lên **chỉ do ngẫu nhiên** là khoảng
25%. Muốn có ý nghĩa thống kê cần khoảng 50 cặp trở lên, và chi phí chấm tăng theo. Ngưỡng
này là một công tắc dừng rẻ tiền; đọc nó đúng như vậy.

**Rubric "đạt chuẩn" — ba trục chấm riêng, không gộp:**

| Trục | Câu hỏi | Ai chấm được |
|---|---|---|
| Đúng | Mô hình và dữ liệu có đứng vững không: giả định đã khai, đơn vị nhất quán, nguồn có thật | Chủ dự án, kiểm được bằng tài liệu |
| Mới | Trong phạm vi corpus đã kiểm, có ai nói điều này chưa | `novelty-check` — và chỉ trong phạm vi corpus |
| Đáng quan tâm | Người Mỹ mục tiêu có hiểu và có muốn biết không | **Không chấm được bởi người không sống ở đó.** Cần ít nhất một người bản địa, hoặc đánh dấu chưa đo |

Một thesis "đạt chuẩn" phải đạt cả trục Đúng và trục Mới. Trục Đáng quan tâm nếu chưa có
người bản địa chấm thì ghi `chưa đo`, **không** suy ra từ hai trục kia.

### Ba kết quả, không phải hai

| Kết quả | Điều kiện | Làm gì |
|---|---|---|
| **Qua** | Đạt cả hai ngưỡng | Sang Mốc 4 |
| **Chưa đủ bằng chứng** | Sát ngưỡng, hoặc số cặp không hoà dưới 12, hoặc trục Đáng quan tâm chưa đo | **Không dừng dự án.** Tăng mẫu: thêm một đợt dữ liệu, thêm cặp, tìm người bản địa chấm. Một phép thử nhiễu không phải một câu trả lời |
| **Không đạt** | Rõ ràng dưới ngưỡng ở cả hai điều kiện | Dừng dự án |

### Tồn kho khác tốc độ cung

20 thesis trong một lần chạy chỉ chứng minh **tồn kho ban đầu**. Nhịp bền vững 8–12 tập/tháng
là một khẳng định khác, và cần đo riêng ở Mốc 7: số thesis mới đạt chuẩn mỗi đợt dữ liệu, sau
khi khử trùng và trừ thesis hết hạn, cộng chi phí mỗi thesis. Không được suy nhịp từ tồn kho.

Ngưỡng 15 được đặt để khớp với sàn Thesis Bank (≥15 mục khả dụng). Một ngưỡng thấp hơn sẽ tạo
ra tình huống vừa qua cổng vừa bị chặn.

**Không đạt thì dừng dự án.** Đây là điểm dừng rẻ nhất trong toàn bộ kế hoạch. Mọi thesis bị
bác ghi `rejectionReason`.

---

*Nguồn: spec dòng 1802–1816, cùng khối `engine/docs/12-success-criteria.md`.*

## Điều kiện dừng

| Mốc | Dừng khi |
|---|---|
| Mốc 2 | Spike canvas cho kết quả DỪNG ở cả runner tiêu chuẩn lẫn runner lớn hơn |
| **Mốc 3** | **Máy thắng <60% trong so sánh mù, hoặc <15/20 thesis đạt chuẩn** |
| Mốc 3 | Quá 4 trong 12 đề tài không có nguồn dữ liệu hợp lệ sau WP-009 |
| Mốc 4 | Sau 3 vòng lặp chưa có layout nào đạt 8/8 |
| Mốc 5 | Vertical slice fail lần thứ hai vì cùng nguyên nhân gốc |
| Mốc 7 | FPY stage kém nhất <30%, hoặc chi phí thật mỗi tập >45 USD ổn định — đây là tiêu chí kỹ thuật, đo được khi chưa đăng |
| Mốc 7b | Sau 30 tập **đã phát hành** và đủ cửa sổ đo: giữ chân 30 giây <45% và người đăng ký <300 |
| Vận hành | Giờ xem tích luỹ chưa đạt quỹ đạo tới ngưỡng nền tảng trong 365 ngày |
| Vận hành | Tỷ lệ duyệt gate đúng hạn <70% qua 4 tuần, và không nâng được bậc tự động hoá |
| Vận hành | Chạm `stopAndReviewUsd` |
| Bất kỳ lúc nào | Bài kiểm "xoá hội thoại, chỉ giữ repo" thất bại |

---

*Nguồn: spec dòng 1901–1933, khối `engine/docs/14-quantitative-core.md`.*

## 2 · Thư viện mô hình

**Vấn đề nó giải:** fact-checker đối chiếu claim với URL. Một **con số phái sinh** — thứ tạo
ra toàn bộ khác biệt của kênh — chưa từng được công bố nên **không có URL để đối chiếu**.
Không ai kiểm phép tính. Và bảng tính được công bố công khai kèm lời mời khán giả kiểm.

Rủi ro kép: ngách này có hậu quả thật cho người xem, và một lỗi công thức bị phát hiện công
khai gây thiệt hại lớn hơn một số trích dẫn sai — vì nó là lỗi của mình.

**Cấu trúc:** `/models/{genre}/M-{NNN}.json` theo `model.schema.json`: giả định, công thức,
khoảng giá trị hợp lệ từng tham số, `claimId` đầu vào, phiên bản.

**Kiểm bốn cấp — bắt buộc.** "Gọi lại cùng một hàm" không phải kiểm độc lập: hàm xác định thì
lượt hai chắc chắn khớp lượt một. Và để một mô hình ngôn ngữ tự tính lại bằng lời cũng không
phải kiểm: bên yếu hơn về số học đang kiểm bên mạnh hơn, nên "lệch" thường là mô hình ngôn ngữ
sai, còn "khớp" không chứng minh điều gì. Bốn cấp dưới đây xếp theo độ tin cậy giảm dần.

| Cấp | Cách kiểm | Bắt buộc khi |
|---|---|---|
| 1 | **Ca kiểm tay** — bộ đầu vào/đầu ra do người tính tay, commit kèm mô hình | Mọi mô hình, không ngoại lệ |
| 2 | **Đối chiếu công cụ công khai** — so với một máy tính công khai tương đương | Khi tồn tại công cụ như vậy |
| 3 | **Triển khai thứ hai** — viết lại mô hình bằng ngôn ngữ hoặc công cụ khác, so kết quả | Mô hình có `geoVarying: true` hoặc được dùng ở hơn 3 tập |
| 4 | **Mô hình ngôn ngữ kiểm giả định và đơn vị** — KHÔNG kiểm số học | Mọi mô hình |

Lệch quá dung sai khai trong mô hình ở bất kỳ cấp nào → chặn pipeline.

Nếu dùng cấp 4, **phải là nhà cung cấp khác** với mô hình chính (`LLM_API_KEY_VERIFIER`).
Khoá API riêng tạo độc lập về hạn mức và nhật ký; nó **không** tạo độc lập về suy luận nếu
cùng một mô hình đứng sau.

**Tái dùng:** mô hình đã kiểm được dùng qua nhiều tập mà không kiểm lại, trừ khi phiên bản
đổi. Đây là tài sản cộng dồn — và là thứ có giá trị nhất nếu bán hệ thống.


---

*Nguồn: spec dòng 3481–3490, khối `engine/ops/work-packages/WP-015-thesis-engine.md`.*

### 7. Definition of Done
Theo `definition-of-done.md`, cộng **Cổng Mốc 3** trong `12-success-criteria.md`:
chấm mù 40 thesis theo đúng năm bước trong mục "Cách chấm" của file đó — chuẩn hoá thẻ, ghép
cặp cùng trụ, cho phép hoà; **máy thắng ≥60% số cặp không hoà và ≥15/20 thesis đạt rubric ba
trục**; lý do loại từng thesis bị bác ghi vào `rejectionReason`.

Kết quả sát ngưỡng đọc là **"chưa đủ bằng chứng"**, không phải "dừng dự án" — xem bảng ba kết
quả trong `12-success-criteria.md`.

**Không đạt rõ ràng thì dừng dự án tại đây.** Sát ngưỡng thì tăng mẫu, không dừng.
