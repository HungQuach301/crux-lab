# Sổ gu

Sổ gu ghi các phán đoán của chủ dự án mà máy chưa đo được, hoặc chưa đo đúng. Nó đứng sau hiến chương, `decisions/` và spec thể loại (CHARTER §10).

Mỗi dòng có: ngày, nguồn, ví dụ, trạng thái.

Trạng thái là một trong ba mức:
- **chưa thành luật**: chỉ có trong sổ gu và spec;
- **đã thành luật mã `<id>` @ `<SHA LOCK>`**: đã có luật khoá trong `checks/`;
- **đã bỏ**: kèm lý do.

Chỉ Phiên kiểm (K1…) được đổi trạng thái sang "đã thành luật mã", sau khi chủ dự án duyệt (CHARTER §7.1).

## Nguồn chung của 4 dòng đầu

- **Bài D** ("Same average, different fate") ở repo [crux-spike-opus55](https://github.com/HungQuach301/crux-spike-opus55), nhánh `claude/opus55-cine-phase-d-jw6me1`.
- **Chấm tay vòng 2** của chủ dự án trên master r2 (`dd6117c6…`): H1 4 · H2 2 · H3 3 · H4 3 · H5 4 · H6 4 · H7 3, trung bình 3,29, chưa đạt. Chỉ dẫn sửa ghi ở [BRIEF-D-amendments.md mục 17–19](https://github.com/HungQuach301/crux-spike-opus55/blob/76613cfa756e2604770043435f79eb00e269e2b6/BRIEF-D-amendments.md).
- **Vòng 3**: master r3 `6531f6c8…`, gói duyệt [`out/r3/review/`](https://github.com/HungQuach301/crux-spike-opus55/tree/76613cfa756e2604770043435f79eb00e269e2b6/out/r3/review) (mỗi clip có bản trước và sau), báo cáo ở [REPORT-D.md, mục "M3 vòng 3"](https://github.com/HungQuach301/crux-spike-opus55/blob/76613cfa756e2604770043435f79eb00e269e2b6/REPORT-D.md).
- **Câu chữ của 4 phán đoán** do chủ dự án tổng kết khi giao việc Phiên B0 ngày 2026-09-28, sau khi nghe vòng 2 và vòng 3. Riêng nhấn mạnh "NGHE THẤY ĐƯỢC" ở (a) là của chủ dự án.
- **Chấm tay vòng 3** của chủ dự án trên gói duyệt `out/r3/review/` (2026-09-28). Chỉ chấm lại ba câu đã sửa; các câu khác giữ điểm vòng 2:

  | Câu | Vòng 2 | Vòng 3 | Nhận xét của chủ dự án |
  |---|---|---|---|
  | H2 (câu móc lại) | 2 | **4** | "hình đã cải thiện" |
  | H5 (ghi chú khoảng lặng) | 4 | **4,5** | "đã cải thiện" |
  | H7 (nhạc, âm thanh theo dữ liệu) | 3 | **3,5** | "âm thanh khi các cột xuất hiện, các đường di chuyển trong biểu đồ biến động chưa có" |

  Trung bình sau vòng 3: **3,71** (H1 4 · H2 4 · H3 3 · H4 3 · H5 4,5 · H6 4 · H7 3,5). Vẫn chưa đạt ngưỡng ≥ 4.
- **Đo kiểm của chat chiến lược:** trên clip `h7-sonification.mp4`, dải 1,5–8 kHz của bản trước và bản sau chỉ chênh **−0,2 dB**. Nghĩa là âm thanh theo dữ liệu gần như không nghe thấy.

## Các dòng

| # | Phán đoán | Ngày | Nguồn | Ví dụ | Trạng thái |
|---|---|---|---|---|---|
| G-001 (a) | Mỗi phần tử biểu đồ khi biến động có tiếng riêng, và tiếng đó **NGHE THẤY ĐƯỢC**. | 2026-09-28 | Chấm tay vòng 2 (H7 = 3) → Am 19a. Vòng 3 thêm lớp sonification, duck −10 dB dưới lời và −16 dB quanh số. Chủ dự án nhấn "nghe thấy được" sau vòng 3. | `h7-sonification.mp4`: phim 8:00, 8:50, 10:50, trước/sau. 550 lần cột mọc, 89 điểm, 21 lần vẽ đường; 517 sự kiện gộp thành 166 cụm. | chưa thành luật. Spec: DX-A1. Bài D chỉ đo khớp khung (0 khung lệch), không đo nghe thấy được. **Vòng 3: H7 = 3,5, chưa đạt.** Chủ dự án: "âm thanh khi các cột xuất hiện, các đường di chuyển… chưa có". Đo dải 1,5–8 kHz trước/sau chênh −0,2 dB, gần như không nghe thấy. |
| G-002 (b) | Nhạc không lộ vòng lặp. | 2026-09-28 | Chấm tay vòng 2, H7 = 3 (RUBRIC H7 "nhạc không lộ vòng lặp") → Am 19b. | `h7-music.mp4`: phim 1:25 và 2:49, là hai đoạn nhạc r2 lặp nhiều nhất. Tự tương đồng r2: 7,6% cặp câu 4 ô ≥ 0,90; r3: 0%. | chưa thành luật. Spec: DX-A2. Số đo có sẵn ở `toolkit/audio/d_music_selfsim.py` nhưng chưa phải luật khoá, và chưa được chấm là đủ. |
| G-003 (c) | Vào khoảng lặng phải có chuyển tiếp, không cắt cứng. | 2026-09-28 | Chỉ dẫn vòng 2, ghi dưới mục H5 → Am 18. | `h5-silences.mp4`: phim 0:11.1, 2:39.0, 6:19.9, trước/sau. r3: nhạc nhả như đuôi reverb (τ 90 ms), sfx tắt trong 150 ms, room tone +6 dB làm sàn, trở lại trong 200 ms. | chưa thành luật. Spec: DX-R6. Luật A09 của bài D chỉ đếm khoảng lặng 0,8–1,5 s, không xét cách vào. Vòng 3: H5 = 4,5 ("đã cải thiện"). |
| G-004 (d) | Ở nhịp then chốt, hình minh hoạ đúng lời đang hứa, và người xem hiểu trong 1 giây. | 2026-09-28 | Chấm tay vòng 2, H2 = 2 (câu móc lại 0:30–0:45) → Am 17. | `h2-rehook.mp4`: phim 0:20–0:55. r2 dùng lưới 69 ô, không khớp câu "which ten years decided…". r3 dùng một dải 30 ô và một khung 10 năm trượt theo lời rồi dừng ở thập kỷ đầu. | chưa thành luật. Spec: DX-V2, DX-S4. Máy chưa đo được "khớp lời hứa". Cần phiếu chấm tay, hoặc đề xuất của K1. Vòng 3: H2 = 4 ("hình đã cải thiện"). |
| G-005 | Tiếng dữ liệu phải hợp — âm sắc mềm, có tính nhạc, cùng điệu với nhạc nền; không phải bíp/click máy móc. | 2026-09-28 | Nghe m0-sample trên loa điện thoại (chủ dự án). | `episodes/ep001/m0-sample` (master `82ba6767…`): *"Nghe thấy tiếng riêng của cột, đường, điểm, nhưng âm sắc CHƯA PHÙ HỢP."* | chưa thành luật. Liên quan DX-A1, G-001. Thử ba bảng âm mù trên cùng mẫu: `episodes/ep001/review-m1/sonify-S1/S2/S3.mp4`. |
| G-006 | Lời đọc là ưu tiên số một; tiếng dữ liệu không được lấn lời; không giải bằng cách tăng âm lượng. | 2026-09-28 | Nghe m0-sample trên loa điện thoại (chủ dự án). | `episodes/ep001/m0-sample` (tiếng dữ liệu +10 dB): *"Lời đọc rõ nhưng VẪN BỊ tiếng dữ liệu lấn."*, *"Không tăng +10 dB."* | chưa thành luật. Xung đột với ngưỡng T1 (≥ 1 dB trong cửa sổ số được đọc, ≥ 3 dB ở nơi khác); với Tập 1, gu của chủ dự án thắng T1 (T1 không phải luật cứng, CHARTER §5). Ghi cho Phiên K: `episodes/ep001/checks-notes.md`. |
| G-005 · chọn | Lựa chọn S2 (thử mù S1/S2/S3 trên loa điện thoại); S2 không lấn lời. | 2026-09-28 | Duyệt M1 Tập 1 (chủ dự án xem animatic 0:00–1:20, nghe table read đầy đủ; thử mù S1/S2/S3 trên loa điện thoại). | `episodes/ep001/review-m1/sonify-S2.mp4`. Giải mã (`review-m1/key.json`): S2 = bảng âm tối giản, tick lọc mềm 4,5–7 kHz + nhịp trầm nhẹ có cao độ (`toolkit/audio/sonify_palettes.py`, palette `minimal`). | chưa thành luật. Bảng âm của Tập 1. Hình chưa chấm (chờ M2). |
| G-007 | Cold open phải cho người xem thấy chủ đề liên quan đến chính mình — bằng một người và một khoảnh khắc cụ thể. | 2026-09-28 | Duyệt M1 Tập 1 (chủ dự án xem animatic 0:00–1:20, nghe table read đầy đủ; thử mù S1/S2/S3 trên loa điện thoại). | Cold open M1 chấm TRUNG BÌNH: *"cần mạnh hơn, giúp người xem cảm nhận chủ đề liên quan đến chính mình."* | chưa thành luật. Liên quan DX-S3, RUBRIC H1. |
| G-008 | Mọi số liệu phải gắn với hoàn cảnh của người xem (nhân vật, kịch bản, hệ quả), không diễn giải số đơn thuần. | 2026-09-28 | Duyệt M1 Tập 1 (chủ dự án xem animatic 0:00–1:20, nghe table read đầy đủ; thử mù S1/S2/S3 trên loa điện thoại). | Toàn bài M1 chấm TRUNG BÌNH: *"thiên về diễn giải số liệu; cần gắn số liệu với hoàn cảnh của người xem để câu chuyện gần với họ."* Câu móc lại 0:30–0:43: *"rõ lời hứa"*. | chưa thành luật. Liên quan DX-S5, RUBRIC H4. |
| G-009 | Kịch bản phải là một câu chuyện — bối cảnh → nhân vật → vấn đề → hành trình → đáp án; không đưa nhân vật hay số liệu khi người xem chưa hiểu bối cảnh; câu chữ liền mạch, có chuyển ý, không cụt lủn. | 2026-09-28 | Chủ dự án duyệt M1b Tập 1. | Kịch bản M1b (nhánh `ep001`, `episodes/ep001/script/script.md` @ `bbc28fb`): *"kịch bản rất tệ, chưa có kịch bản, vào ngay Maya không có bối cảnh, thông tin cụt lủn."* | chưa thành luật. Liên quan DX-S1, DX-S2, RUBRIC H1, H3. Tập 1 viết lại từ treatment (`episodes/ep001/story/`). |
| G-009 · Cổng A | Chọn cold open A (mở bằng lá thư của ngân hàng, bối cảnh "đỉnh lãi từ 2000" trước nhân vật Nora); câu chuyện (treatment, 25 nhịp) OK; chấp nhận cold open ~20 s cho Tập 1 vì G-009 cần bối cảnh trước nhân vật (miễn trừ S15 ghi trong amendments của tập). | 2026-09-29 | Chủ dự án duyệt Cổng A Tập 1 (trả lời trực tiếp trong phiên P1). | Nhánh `ep001`: `episodes/ep001/gates/gate-A.md`, `episodes/ep001/story/cold-open.md` (A, 55 từ), `story/treatment.md`. Trả lời: *"A; câu chuyện OK; chấp nhận cold open 20 giây cho Tập 1 (G-009 cần bối cảnh trước nhân vật; ghi vào amendments của tập)."* | chưa thành luật. Xung đột DX-S1 (cold open ≤ 15 s, S15): với Tập 1, G-009 thắng theo quyết định của chủ dự án; Phiên K cân nhắc lại trần 15 s. |
| G-010 | Giọng tự nhiên và ổn định, một màu giọng xuyên suốt tập; không ngập ngừng hay kéo dài giả; nhịp chậm lại bằng khoảng nghỉ giữa câu. | 2026-09-29 | Nhận xét Cổng B Tập 1 của chủ dự án, 29/09/2026. | Tập 1 bản cũ (tag `ep001-v1-stopped`, `archive/ep001-v1/`): 104/132 câu đổi sang `eleven_multilingual_v2` speed 0,70–0,72, "..." giả do `pauses.js`, thẻ `<break>`. Nhận xét: *"voice có vấn đề nhiều đoạn bị cố kéo dài không ổn định."* | chưa thành luật. Áp ngay: `pauses.js` đã xoá; `d_el_voice.py` tắt model dự phòng; `playbook/quality-framework.md` §2.3. Ứng viên luật K3: một `model_id` cho mọi câu của tập (Chặn). |
| G-011 | Hình phải tự nói được ý nghĩa kể cả khi tắt tiếng; không duyệt hình bằng ảnh tĩnh. | 2026-09-29 | Nhận xét Cổng B Tập 1 của chủ dự án, 29/09/2026. | Clip Cổng B (`archive/ep001-v1/`, storyboard tĩnh trong animatic 12:22). Nhận xét: *"Hình ảnh tĩnh khó hiểu ý nghĩa."* | chưa thành luật. Áp ngay: C3 kiểm mù ý nghĩa từng frame; C4 animatic có chuyển động, kiểm mù tắt tiếng (≥ 80% nhịp). |
