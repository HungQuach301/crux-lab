# Đầu bài WRITER — Tập 3, Cổng C2 (P1, 2026-10-04)

Viết bằng **tiếng Anh Mỹ** (lời phim). Ghi chú cho P bằng tiếng Việt được. Đọc: `CHARTER.md` §5, `episodes/ep003/gates/C1.md`, `episodes/ep003/numbers.md`, `topics-r1/machine/retire-4/claim-risk.md`, `toolkit/visual-library/README.md`, `taste-ledger.md` (dòng G-007…G-016 và "Tập 3 · C1"). **Không đọc kịch bản tập cũ** (`episodes/ep001/`, `episodes/ep002/story/`).

## Đã chốt (C1, chủ dự án)
- Logline **A** ("người như tôi" + lời hứa đáp án). Tiêu đề nháp **A1** *"Money You Won't Touch for 20 Years: Savings Bond or T-Bills?"*. Người xem: người Mỹ có tiền để yên ~20 năm (đang ở tài khoản ngân hàng hay T-bill), cân nhắc trái phiếu tiết kiệm Series EE bảo đảm gấp đôi sau 20 năm với việc lăn T-bill 3 tháng.
- **Giả định trước 5/2005 — luật của tập:** điều khoản gấp đôi hiện nay áp cho bond phát hành **từ May 2005**; bond trước đó có điều khoản khác (**không** nói "không có bảo đảm trước 2005"). Câu giả định nằm **trong cold open, trước mọi con số lịch sử**, viết bằng **lời thường** (kiểm mù C1: 6/6 người đọc vấp câu "…as if they had existed"; giữ ý, đổi cách nói — ví dụ kiểu "the promise in its current form only started in 2005, so for the years before that we pretend it already existed"). Ghi chú hình: **nhãn cố định trên mọi cửa sổ trước 5/2005** (ví dụ "IF today's guarantee had existed") suốt tập; 17 cửa sổ có bảo đảm thật vẽ khác hẳn.
- **Mốc 17 tháng có bảo đảm thật** (`starts_with_guarantee`, 5/2005–9/2006; T-bill 1.378–1.388 lần; 0/17 vượt gấp đôi): chỉ dùng **trong phim**, **luôn kèm** "mẫu ngắn, một thời kỳ" **và** tỉ lệ toàn kỳ (52.3%) trong cùng đoạn.
- Lãi EE hiện hành: **2.40%** cố định, lời và hình ghi **"for bonds issued May to October 2026"** (`ctx_ee_rate`); lãi đặt lại mỗi 1/5 và 1/11 — đừng nói như lãi cố định mãi mãi của mọi bond.
- Dữ liệu ghim **August 2026** (T-bill 3.72%).

## Gu đã chốt (không hỏi lại) — `taste-ledger.md`
- **G-007** cold open: một người, một khoảnh khắc cụ thể, người xem thấy mình. **G-008** mọi số gắn với hoàn cảnh người xem. **G-009** truyện: bối cảnh → nhân vật → vấn đề → hành trình → đáp án; số chỉ đến khi người xem cần; câu liền mạch, có chuyển ý. **G-013** "người như tôi" + một **ngưỡng tự đối chiếu** được (gợi ý: điều kiện lịch sử để lăn T-bill vượt gấp đôi — ví dụ lãi T-bill trung bình phải ở mức nào suốt 20 năm; nếu cần số mới, ghi `needs-claims.md`).
- Nhân vật minh hoạ (nếu dùng): ILLUSTRATIVE trong lời và trên hình; tên là gu — chủ dự án duyệt ở C3.
- Giọng Eric `eleven_v3`, sinh **theo cảnh** (mỗi cảnh ≤ ~900 ký tự lời), **thẻ cảm xúc thưa** (5–8 thẻ cả tập, chỉ nhịp then chốt; không thẻ ngắt/nghỉ, không "...", không speed). Đánh dấu thẻ đầu dòng, ví dụ `[curious]`.
- G-014: chữ trên hình ít, lớn (sàn 40 px). G-016: nhạc sáng/năng động (không phải việc của kịch bản, chỉ đừng viết cảnh "buồn").

## Gen được bảo vệ và claim-risk (luật cứng)
- "we" chỉ người phân tích; **không khuyên** (không mệnh lệnh: buy/lock/hold/avoid/consider/choose/keep… với người xem; máy S10 bắt); **không dự báo** lãi hay lạm phát; có **"US only"** và câu **"history, not a forecast"** nguyên dạng.
- **Câu đối trọng:** mỗi kết luận có một câu chặn suy diễn "X tốt hơn / an toàn hơn" (ví dụ: "That is not a reason to pick either one; it is what history did with these two rules"). Kiểm mù C1: người đọc tự rút "coi bảo đảm như phòng hộ" — kịch bản không được dẫn tới đó.
- **Không đặt 3.72% cạnh 3.53% mà không chú giải** (khác cách tính: lãi chiết khấu trung bình tháng vs lãi kép năm; một con số hôm nay không trả lời câu hỏi 20 năm).
- **Claim-risk áp cho câu NÊU số:** câu nêu tỉ lệ toàn kỳ (52.3%) phải kèm thời kỳ (1950–1989: 93.1%; từ 1990: 5.0%) và nhắc giả định (nhãn hình đủ nếu lời đã nói ở cold open). Câu **nhắc lại** gọi bằng lời, không nêu lại số. **Mỗi tỉ lệ một dạng cố định cả tập** (ví dụ "52.3 percent, about half"). Không lặp một bộ số ở nhiều cảnh.
- "Double" không chống lạm phát: 58.7% giữ sức mua; tệ nhất bắt đầu January 1966 còn 58.0%. Không nói "doubling protects you".
- Không gọi tên môi giới, không khuyên mua.

## Luật lời cho ASR và nhịp (`playbook/episode.md` §3)
1. Không dải năm có gạch nối ("1950-1989" → "from 1950 to 1989"). Không "minus", không số âm đọc lên. Không ký hiệu (%, ±, →) trong lời: viết **"percent"**. Số tiền đọc rõ.
2. Mật độ số đọc liền nhau chỉ là Tham khảo; đoạn ≥ 3 số liền nhau thì đưa bớt lên hình.
3. **Đoạn phương pháp = 1 câu lời + thẻ phương pháp + mô tả** (thư viện V7). Giới hạn mô hình lên thẻ: lãi T-bill trung bình tháng (chiết khấu) chia 12, lãi kép tháng; bỏ qua thuế (T-bill đánh thuế liên bang hằng năm, EE hoãn thuế; cả hai miễn thuế bang); giữ đủ 20 năm; bỏ hạn mức mua; cửa sổ chồng nhau ≈ 4 giai đoạn độc lập; 6 cửa sổ sát gấp đôi.
4. Lời không gọi tên thiết bị hình (không "grid", "bin", "token"…): nhắm mắt nghe vẫn hiểu.

## Hình
- **Ký hiệu mới bắt buộc** cho ý "gấp đôi / sức mua" (việc treo C3): không lặp nguyên hình Tập 2 (lưới ô V1, thùng đỏ V2, đường lãi so vạch V3, dãy núi TB3MS). Ghi chú hình gợi ý ý tưởng; thiết kế cuối ở C3.
- Gợi ý khác lấy từ thư viện trước (V7 thẻ phương pháp; V1/V3 chỉ khi có biến thể rõ ràng khác Tập 2).

## Đầu ra (trong `episodes/ep003/story/`)
1. `treatment.md` (~500–700 từ). Nếu có cấu trúc thứ hai đáng cân nhắc: `treatment-alt.md` (chủ dự án duyệt cấu trúc + cold open ở C3).
2. `beats.md`: bảng nhịp `id | thời điểm ước | việc của nhịp | cảm xúc | claim | loại nhịp | ý người xem phải đọc ra khi tắt tiếng (chỉ loại 1) | gợi ý hình`. **Loại 1** "hình tự mang ý" / **loại 2** "hình minh hoạ lời". Đánh dấu 6–8 **nhịp then chốt** `KEY-n`; loại 1 phải ≥ 60% số nhịp then chốt (không hạ nhịp khó xuống loại 2 để dễ qua).
3. `script.md`: theo cảnh `S01…`, mỗi câu một dòng `S01.1 | lời | claim IDs | ghi chú hình`; số ký tự lời mỗi cảnh. ~1,300–1,500 từ (~9–10 phút), có đuôi end screen 15–20 s. Cold open mặc định theo G-007.
4. `needs-claims.md`: số muốn dùng mà chưa có claim (P tính + kiểm độc lập, hoặc bỏ).
5. Tin nhắn cuối ≤ 15 dòng: cấu trúc, số từ, nhịp then chốt + loại, vị trí thẻ cảm xúc, chỗ chưa chắc.
