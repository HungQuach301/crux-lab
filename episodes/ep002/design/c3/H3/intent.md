# H3 · Dòng thời gian lịch sử — ý đồ (viết TRƯỚC khi render, 01/10/2026)

Hướng: cả lịch sử T-bill 3 tháng (TB3MS, 1954-01 → 2026-08) là **một dải địa hình** ngang màn hình (trục x = thời gian, một đường `accent` + mặt `accent` mờ). Một **khung 10 năm** (viền `ink`) trượt dọc dải; mỗi lần dừng thả **một ô** thẳng xuống **dải 753 ô** nằm ngay dưới địa hình: mỗi năm bắt đầu là một cột 12 ô (một ô một tháng), cột nằm đúng dưới năm đó trên địa hình. Vì vậy nửa trái của dải ô (bắt đầu 1954–1980) nằm dưới **sườn đi lên**, nửa phải (1981 về sau) nằm dưới **sườn đi xuống**: đọc được bằng vị trí, không cần chữ. Một vạch dọc mảnh (`ink-muted`) rơi từ đỉnh địa hình (5/1981) xuống tách hai nửa.

Bảng nghĩa (một vật một nghĩa, một màu một nghĩa; chỉ token Tập 1):
- **ray** = lãi cố định 9%: đoạn thẳng nằm ngang `ink-muted`, không bao giờ cong.
- **hạt** = lãi thả nổi của Leah: **hình thoi** `ink` (Leah minh hoạ: màu `ink` + hình thoi). Đường hạt đi theo = hình địa hình trong khung.
- **ngoặc** = khoảng chênh lúc khởi đầu (head start): ngoặc dọc `ink` giữa ray và hạt ở vạch xuất phát; lòng ngoặc tô `positive` khi hạt dưới ray, `warn` khi hạt trên ray.
- **`warn` (hổ phách)** = lãi vượt 9%: chỉ đoạn ray nằm dưới phần đường vượt lên, và dải đếm hổ phách (một vạch mảnh mỗi tháng bắt đầu, sáng khi lần chạy đó từng vượt 9%). Không vật nào khác.
- **`negative` (đỏ)** = đắt hơn tổng cộng: chỉ ô kết quả đỏ và khối thêm trên chồng xu. Không bao giờ chung vật với `warn`.
- ô **`grid` xám** = không đắt hơn.
- **`positive`** = phần đệm: cột "hũ" bên phải khung đầy/rút; mặt xanh giữa ray và đường khi đường dưới ray.
- **chồng xu** (đĩa dẹt xếp chồng) = tiền lãi đã trả; chồng cố định `ink-muted`, phần thêm `negative`.
- Nợ còn lại = nêm `grid` mờ dưới đáy khung phóng to (cao ở trái, thấp dần).

## KEY-1 (S01.2–S01.3)
- Ý đồ (nguyên văn beats.md): "Someone is weighing a cost that stays level against one that starts lower but wanders up and down."
- Chuyển động mang ý khi tắt tiếng + che chữ/số: hạt thoi (Leah) đứng ở vạch xuất phát, **hai đường mọc sang phải từ cùng một chỗ đứng**: ray ngang (không nhúc nhích) và đường của hạt bắt đầu **thấp hơn** ray rồi lượn lên xuống. Phía trước hạt, đường tương lai là một **chùm nét mờ rung rinh** (nhiều khả năng, không biết đi đâu), luôn thay hình. Khe giữa hạt và ray sáng `positive` nhẹ và "thở". Hạt nhích qua lại giữa hai lựa chọn (cân nhắc), rồi dừng ở vạch xuất phát.

## KEY-2 (S03.5–S03.8)
- Ý đồ: "The size of the starting gap is the thing being measured, and it can be big, small, none or reversed."
- Chuyển động: ngoặc **bật vào** giữa ray và hạt ở vạch xuất phát (đánh dấu "đây là thứ được đo"), rồi ray đứng yên trong khi hạt (kéo theo cả đường của nó) trượt xuống → ngoặc **dãn rộng**; lên → **hẹp**; chạm ray → ngoặc **khép thành một vạch**; vượt lên trên ray → ngoặc **lật** và lòng đổi `positive` → `warn`. Cuối clip quay về vị trí của Leah. Một thước nhỏ bên cạnh lưu dấu từng cỡ ngoặc đã thử (to, nhỏ, không, âm).

## KEY-5 (S04.1–S04.2; nhắc lại S11.4–S11.6)
- Ý đồ: "The same loan is replayed over and over, starting at each moment in a long history, its rate copying the history's ups and downs."
- Chuyển động: đường ngắn của Leah **kéo dài sang trái thành cả dải địa hình**; khung 10 năm đặt ở mép trái; hạt chạy dọc phần địa hình trong khung (đường của hạt = hình địa hình); xong một lần chạy, khung **thả một ô thẳng xuống** dải ô dưới đúng chỗ nó bắt đầu, rồi **bước sang phải một nấc**; vài nấc đầu chậm (thấy rõ khung mới chồng lên gần hết khung cũ — viền khung cũ còn mờ lại), rồi nhanh dần cho tới khi 753 ô lấp đầy dải. Cùng một khoản vay, cùng một ray, chỉ khác chỗ bắt đầu.

## KEY-3 (S05.2–S05.4)
- Ý đồ: "The variable rate goes above the fixed rate in most replays, yet ends up costing more overall in only a few — far more often in the earlier half of history."
- Chuyển động: khung quét lại nhanh; mỗi lần ray bật `warn` thì một vạch mảnh trong **dải đếm hổ phách** (giữa địa hình và dải ô) sáng lên → dải hổ phách sáng **gần kín cả hai nửa**. Sau đó các ô kết quả lật màu từ trái sang phải: phần lớn thành **xám**, chỉ một ít thành **đỏ**, và đỏ dồn ở **nửa trái** (dưới sườn đi lên); nửa phải chỉ lấm tấm. Hai nửa được khoanh lần lượt. Hổ phách nhiều, đỏ ít, đỏ ở bên trái: đọc bằng diện tích màu và vị trí.

## KEY-4 (S06.1–S06.5)
- Ý đồ: "Starting lower builds up savings early, and that saving has to be used up before the variable loan comes out worse."
- Chuyển động: khung phóng to một lần chạy; hũ `positive` bên phải khung **đầy lên** khi hạt dưới ray, nhanh nhất ở đầu (cạnh nêm nợ cao nhất); khi ray bật `warn` hũ **rút**. Ba lần chạy liên tiếp, vị trí khung trên địa hình nhỏ phía trên cho biết ở đâu trong lịch sử: (1) một cú nhô `warn` ngắn chỉ **làm lõm** hũ một chút, hũ còn đầy → ô xám; (2) leo dốc sớm và cao lâu: hũ **cạn sạch**, rồi ô **đỏ** rơi xuống; (3) đoạn đi xuống: hũ **đầy mãi**. Hũ phải cạn trước khi ô thành đỏ.

## KEY-6 (S08.1–S08.7)
- Ý đồ: "In the worst replay, rates climbed for years and the variable loan cost a lot more — close to half again the fixed loan's interest."
- Chuyển động: trên dải ô, một ô ở nửa trái được khoanh (ô xấu nhất); khung bay tới đó, **đáp xuống đoạn leo dốc nhất** của nửa trái và phóng to; hạt leo **rất xa trên ray**, ray `warn` **hàng năm liền**; hũ đầy chút ít rồi **cạn**; cuối cùng hai chồng xu mọc cạnh nhau: chồng cố định, và chồng thả nổi = bằng chồng cố định + **một khối đỏ thêm cao gần nửa** chồng đó.

## KEY-7 (S09.4–S10.3)
- Ý đồ: "A bigger starting gap means fewer losing replays and a smaller worst case — the later half of history clears completely, the earlier half never does."
- Chuyển động: toàn cảnh địa hình + dải ô; dưới cùng một thước với con trượt là **ngoặc** (ray + hạt thu nhỏ). Con trượt **kéo ngoặc rộng ra** → các ô đỏ **tắt dần** ở cả hai nửa; tới khoảng giữa đường, **nửa phải xám hoàn toàn**; nửa trái luôn **giữ một lớp đỏ mỏng**; cột "khối thêm đỏ" (trên chồng xu cố định) **co lại nhưng không biến mất**. Rồi con trượt quét ngược qua vị trí Leah tới ngoặc âm: **cả hai nửa đỏ lại**, khối thêm cao vọt. Ô xấu nhất (khoanh) không bao giờ rời chỗ.

## Tiêu chí tự đánh giá (để P2/kiểm mù so)
Một người xem tắt tiếng, xem dải che chữ phải nói được: (1) có một mức đứng yên và một mức bắt đầu thấp hơn rồi dao động; (2) khoảng chênh lúc đầu là thứ thay đổi/được đo; (3) cùng một phép thử lặp lại dọc lịch sử, mỗi lần một ô; (4) hổ phách nhiều, đỏ ít, đỏ dồn bên trái (giai đoạn đi lên); (5) tiết kiệm tích lại đầu kỳ, phải cạn thì mới thua; (6) lần xấu nhất: lãi leo cao nhiều năm, tốn thêm gần nửa; (7) chênh càng lớn đỏ càng ít, bên phải sạch, bên trái không bao giờ sạch.
