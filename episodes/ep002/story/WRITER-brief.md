# Đầu bài WRITER — Tập 2, Cổng C2 (P-ep002, 2026-10-01)

Viết bằng **tiếng Anh Mỹ** (lời phim). Ghi chú cho P bằng tiếng Việt được.

## Đã chốt (C1, chủ dự án)
- Logline **A** ("người như tôi" + lời hứa đáp án). Tiêu đề nháp A1 *"Need Private Grad Loans? Variable vs Fixed Through History"*.
- **Câu hỏi trung tâm của tập:** *how much lower does a variable rate have to start than a fixed rate before the risk has been worth it, in history?* Cặp 7.5%/9% chỉ là **một điểm minh hoạ** trên đường độ nhạy (claim `spread*_share`, −1…3 điểm). Nếu thấy cấu trúc khác tốt hơn, viết **2 phương án** (treatment ngắn mỗi phương án) và nói vì sao.
- Nghịch lý (lãi thả nổi vượt 9% ở ~3/4 cửa sổ — `share_rate_above_fixed` — nhưng đắt hơn tổng cộng ở ~1/7 — `share_all`) nằm **trong phim** (cold open hoặc câu hứa), không phải tiêu đề.
- Cặp 7.5/9 và khoản vay $50,000/10 năm: **ILLUSTRATIVE** — nói trong lời và hiện trên hình.

## Gu đã chốt (không hỏi lại) — `taste-ledger.md`
- **G-007** cold open: một người, một khoảnh khắc cụ thể, người xem thấy mình. **G-008** mọi số gắn với hoàn cảnh người xem. **G-009** truyện: bối cảnh → nhân vật → vấn đề → hành trình → đáp án; không đưa số khi người xem chưa cần; câu liền mạch, có chuyển ý. **G-013** "người như tôi" + một ngưỡng **tự đối chiếu** với lời mời của chính mình (đường độ nhạy là ngưỡng đó).
- Giọng Eric `eleven_v3`, sinh **theo cảnh**, **thẻ cảm xúc thưa** (chỉ ở nhịp then chốt; không thẻ ngắt/nghỉ, không "...", không speed). Đánh dấu vị trí thẻ trong kịch bản, ví dụ `[curious]`, `[serious]`, `[warm]`; tổng cả tập khoảng 5–9 thẻ.
- G-014: chữ trên hình ít, lớn (sàn 40 px) — kịch bản đừng dựa vào chữ nhỏ.

## Gen được bảo vệ (luật cứng — CHARTER §5 + `topics-r1/machine/debt-2/claim-risk.md`)
- **Cách áp luật hai thời kỳ (chủ dự án, C2, 01/10/2026):** luật áp cho câu **NÊU một tỉ lệ / kết quả** — câu đó bắt buộc kèm cả hai thời kỳ (1954–1980, từ 1981) và trường hợp xấu nhất. Câu chỉ **NHẮC LẠI** cặp của Leah (đã nêu đầy đủ trước đó) thì **không nêu lại số**, chỉ gọi lại bằng lời ("Leah's pair", "her point on the line"). Không lặp một bộ số ở nhiều cảnh. Mỗi tỉ lệ **một dạng cố định** suốt tập (ví dụ "28.4%, more than 1 in 4"; "3.5%, about 1 in 30").
- "we" chỉ người phân tích; không khuyên; không dự báo; "US only"; câu **"history, not a forecast"** phải có.
- Không "your loan will…". Mỗi khi nói kết quả, **luôn có cả hai thời kỳ (1954–1980 và từ 1981) cùng trường hợp xấu nhất** (April 1977, +$11,219). Không "variable is safe", không "wins X%" đứng riêng. Kết quả chỉ đúng cho **cặp lãi đang xét** — vì thế mới có đường độ nhạy.
- Lời và chữ trên hình viết **dạng mô tả**. Không dùng take/lock/choose/pick/consider/avoid như mệnh lệnh với người xem (máy S10 bắt); "people who took the variable rate" (mô tả) thì được.
- Bối cảnh chính sách chỉ đủ để dựng người xem (`story/policy-context.md` mục "Risky phrasings"): không nói "Grad PLUS is gone for everyone"; không nói "everyone now needs private loans"; $50,000/$200,000 chỉ cho sinh viên **chuyên nghiệp**.
- Giới hạn mô hình phải nói (thẻ phương pháp hoặc lời): T-bill 3 tháng thay chỉ số thật (SOFR); không trần trong phát lại chính; trả nợ bắt đầu ngay, không ân hạn/phí; cửa sổ chồng nhau không phải phép thử độc lập.
- Bài học kiểm mù C1: người đọc vấp chữ **"head start"** (chưa định nghĩa) và câu "one in four… one in thirty" (so với gì?). Nói rõ "cost more **in total interest than the 9% fixed loan**".

## Số liệu — CHỈ dùng số có claim
`episodes/ep002/numbers.md` (bảng claim ID; sinh tự động). Mỗi câu có số phải ghi claim ID. Không làm tròn khác cột "Hiển thị"/"Lời gợi ý". Không có claim thì không dùng — ghi vào `story/needs-claims.md` cho P.
Sự thật lạ đã có claim: `share_rate_above_fixed` 76.2% vs `share_all` 14.2%; `share_early` 28.4% vs `share_late` 3.5%; `worst_*` (April 1977, +$11,219, lãi tới 19.3%, = 43% tiền lãi của khoản cố định); `best_*` (August 1981, −$15,295); khoản trả `fixed_payment` $633.38 vs `max_payment` $863.36, `share_payment_above_fixed` 58.4%; đường độ nhạy `spread*_share` (chênh 0 → 57.9%; 0.25 → 51.0%; 1.25 → 24.7%; 1.5 → 14.2%; 3 → 4.5%); bối cảnh `ctx_*` (Grad PLUS dừng với người vay mới từ July 1, 2026; $20,500/năm, $100,000 tổng; lãi liên bang 8.07% cố định 2026–27); chỉ số T-bill 3.72% (August 2026).

## Không chép Tập 1
Không đọc `episodes/ep001/story/` hay kịch bản Tập 1. Tập 1 chỉ là mẫu quy trình.

## Đầu ra (trong `episodes/ep002/story/`)
1. `treatment.md` (~500–700 từ): bối cảnh, người xem (ILLUSTRATIVE, đặt tên nếu cần — tên là gu, chủ dự án duyệt ở C2), vấn đề, hành trình, đáp án; nơi đặt nghịch lý; vai của đường độ nhạy; phần kết tự đối chiếu. Nếu có phương án cấu trúc thứ hai: `treatment-alt.md`.
2. `beats.md`: bảng nhịp (id, thời điểm ước, việc của nhịp, cảm xúc, claim). **Đánh dấu 5–7 NHỊP THEN CHỐT** `KEY-1…`: nhịp phải **tự mang ý khi tắt tiếng và che hết chữ/số** — mỗi nhịp ghi một câu "ý người xem phải đọc ra" và gợi ý hình (vật thể/chuyển động mang ý; không phải biểu đồ có nhãn). Đây là đầu vào C3/C4 (mục tiêu ≥ 70% đọc đúng khi che chữ/số).
3. `script.md`: theo cảnh `S01…`, mỗi câu một dòng `S01.1 | lời | claim IDs | ghi chú hình`. Đánh dấu thẻ cảm xúc tại chỗ. Độ dài ~1,400–1,650 từ (~9:30–11:00 ở ~150 wpm). Có **đuôi end screen 15–20 s** (lời ngắn hoặc không lời). Có câu "history, not a forecast" và "US only" (hoặc tương đương mô tả rõ dữ liệu Mỹ).
4. `needs-claims.md`: số bạn muốn dùng mà chưa có claim (P sẽ tính + kiểm độc lập, hoặc bỏ).
5. Tin nhắn cuối: tóm tắt ≤ 15 dòng (cấu trúc, số từ, các nhịp then chốt, vị trí thẻ cảm xúc, chỗ bạn chưa chắc).
