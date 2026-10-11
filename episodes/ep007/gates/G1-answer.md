# G1 lô Tập 7–8 — trả lời của chủ dự án · 2026-10-11

Nguồn: lệnh mở phiên P2 Tập 7 (chủ dự án dán vào phiên mới theo prompt PLAN §7; gói `gates/G1.md`). Nguyên văn:

> 1 Tập 7 = #13 L1 (cụm "has to clear" đổi như lời v3). Tập 8 = #20 với điều kiện P1 Tập 8 tìm được tỉ lệ tiền thuê/giá nhà có nguồn công khai (hoặc kể như độ nhạy: câu trả lời lật theo tỉ lệ thuê/giá); không được → #6.
> 2 (a): kiểm mù vòng 3 C2 v3 trước C3. Cổng khuyên Tập 7 dùng rubric MỚI như Tập 6 (advice_stated = 0; inferred/caution chỉ báo, REVIEWER đọc câu trích); vẫn có advice_stated → bỏ nhịp Q3 (S23–S24) và bù ≥ 3/5 câu hỏi (vd Q4 PMI). Trước khi sinh giọng: đổi mọi "this week"/"this week's rates" thành mốc ngày cụ thể của dữ liệu (vd "the week of October 8, 2026"), để video không cũ và số $120 có mốc thời gian; claim/numbers.md ghi tuần dữ liệu. Format: Tập 7 `lab` (giữ ~9:53, không độn). Tập 8 `deep` NẾU F-14 đạt đích trước C2 Tập 8, không thì `lab`.
> 3 Tiêu đề T2 "30-Year Mortgage Paid Off in 15 Years: What It Really Costs". Ý tưởng thumbnail cho ChatGPT ở P4: vật thể "the stack" + "$120 A MONTH?" (ghi mốc tuần dữ liệu trong mô tả); phương án 2 "the bar" không nêu 7,4 %. C3 N1 Month track: duyệt. CHARTER §5 dòng G2: không phản đối, sửa theo D-012 câu 3. ElevenLabs: chủ dự án sẽ bật quyền user_read cho khoá; P2 đọc lại GET /v1/user/subscription, báo ký tự còn/giới hạn trước khi sinh giọng cả tập; thiếu thì dừng hỏi.

Kèm trong lệnh: chặng này kiểm mù vòng 3 C2 v3 → C3 hình mới (N1 Month track, the stack, the bar; clip có chuyển động và âm; cổng gốc) → dừng ở C3 (sửa D-011: tệp lớn còn ở container thì chạy tiếp sau `/compact`). Lô K Tập 7 chạy ở **phiên K riêng** (chủ dự án mở song song), merge `main` trước C4. Việc nặng: headless khoá Console, 0 agent con trừ khi cần công cụ phiên.

| Câu | Quyết định |
|---|---|
| 1 · Tập 7 | **#13, logline L1**; cụm "has to clear" đổi như lời v3 ("gets measured against, before taxes") ở mọi chữ phát hành |
| 1 · Tập 8 | **#20 có điều kiện**: P1 Tập 8 tìm được tỉ lệ tiền thuê/giá nhà có nguồn công khai, **hoặc** kể tập như độ nhạy (câu trả lời lật theo tỉ lệ thuê/giá); không được → **#6** |
| 2 · kiểm | **(a)**: kiểm mù vòng 3 C2 v3 **trước C3** |
| 2 · rubric | Cổng khuyên Tập 7 dùng **rubric MỚI** (như Tập 6): qua khi `advice_stated` = 0; `advice_inferred`/`caution_only` chỉ báo, REVIEWER đọc câu trích |
| 2 · dự phòng | Vẫn có `advice_stated` → **bỏ nhịp Q3 (S23–S24)** và **bù để đạt ≥ 3/5 câu hỏi** khán giả (vd Q4 PMI) |
| 2 · mốc ngày | **Trước khi sinh giọng:** mọi "this week"/"this week's rates" → mốc ngày cụ thể của dữ liệu (vd "the week of October 8, 2026"); claim + `numbers.md` ghi tuần dữ liệu |
| 2 · format | Tập 7 **`lab`** (giữ ~9:53, không độn). Tập 8 **`deep` nếu F-14 đạt đích trước C2 Tập 8**, không thì `lab` |
| 3 · tiêu đề | **T2** "30-Year Mortgage Paid Off in 15 Years: What It Really Costs" |
| 3 · thumbnail | Ý tưởng cho ChatGPT ở P4: vật thể **"the stack"** + **"$120 A MONTH?"** (mô tả ghi mốc tuần dữ liệu); phương án 2 **"the bar"**, không nêu 7,4 % |
| 3 · C3 | **N1 Month track duyệt** (đưa vào C3) |
| CHARTER §5 | Không phản đối → **sửa dòng G2 theo D-012 câu 3** (gói phát hành làm ở P4 trên ChatGPT) |
| ElevenLabs | Chủ dự án bật `user_read` cho khoá; **P2 đọc lại `GET /v1/user/subscription`, báo ký tự còn/giới hạn trước khi sinh giọng cả tập; thiếu thì dừng hỏi** |
