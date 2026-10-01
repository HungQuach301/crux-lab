# C3 Tập 2 · H1 "Vật thể thật" — ý đồ (viết TRƯỚC khi render, 01/10/2026)

Hướng H1: mọi ý là **đồ vật trên một mặt bàn** dựng bằng three.js, render CPU (SwiftShader). Một bộ vật cho cả bảy nhịp, mỗi vật một nghĩa (`beats.md` → Visual vocabulary):

| Vật | Nghĩa | Màu / hình |
|---|---|---|
| **Thanh ray thép** nằm ngang trên hai chân | lãi cố định 9% — không bao giờ động | `ink-muted` (kim loại xám) |
| **Đường ray dây gợn** + **hạt kim cương** trượt trên nó | lãi thả nổi của Leah | dây `accent` (vì nó chép hình T-bill), hạt `ink` hình **bát diện (kim cương)** = hình riêng của Leah |
| Đoạn thanh ray **phát sáng hổ phách** | chỗ hạt đang ở trên 9% | `warn`, chỉ dùng cho việc này |
| **Kẹp chữ U** nối thanh ray với hạt ở vạch xuất phát | khoảng chênh lúc bắt đầu (head start) | `positive` khi hạt dưới ray; lật ngược thành khung rỗng `ink-muted` khi hạt xuất phát trên ray |
| **Dãy núi** dài phía sau bàn (cạnh trên là TB3MS tháng 1954-01…2026-08) | lịch sử lãi T-bill | `accent` |
| **Khung kính 10 năm** viền `accent` | một lần chạy lại | trượt từng nấc theo tháng |
| **Hai khay** ngay dưới hai nửa dãy núi (trái: bắt đầu 1954–1980, phải: 1981 trở đi); mỗi ô = một tháng bắt đầu, cột = năm, hàng = tháng | kết quả của từng lần chạy lại | ô **xám dẹt** (`ink-muted`) = không đắt hơn; ô **đỏ khối cao** (`negative`) = đắt hơn tổng cộng (hai kênh: màu + chiều cao); ô xấu nhất: khối đỏ cao gấp đôi có vòng tối |
| **Chồng xu bạc** | tiền lãi đã trả | vật liệu kim loại xám nhạt (không vàng, để không lẫn với hổ phách); phần đắt hơn = **khối xu viền đỏ** đặt trên chồng cố định |
| **Hũ thuỷ tinh nước xanh** | phần đệm (tiết kiệm dồn lại) | `positive` |
| **Chồng giấy nợ** (thấp dần mỗi tháng) | dư nợ còn lại | giấy |

Chữ: chỉ vẽ phẳng trong không gian màn hình, **mọi chữ có tấm nền đặc token `bg`** (D2); không in chữ lên vật. Cờ `mask=1` trong mã thay mọi hộp chữ (kể cả huy hiệu ILLUSTRATIVE) bằng khối phẳng `surface #171B22` đúng hộp chữ. Vì vậy mỗi nhịp dưới đây phải đọc được **chỉ bằng vật và chuyển động**.

---

## KEY-1 · S01.2–S01.3
**Ý đồ (chép nguyên `beats.md`):** "Someone is weighing a cost that stays level against one that starts lower but wanders up and down."

**Chuyển động mang ý khi tắt tiếng và che chữ/số:**
- Bàn đêm, hai tấm thẻ đề nghị đặt cạnh nhau: thẻ trái in **một đường thẳng**, thẻ phải in **một đường gợn** (hình vẽ, không chữ). Một **mốc kim cương** (Leah) đứng giữa hai thẻ, nghiêng qua lại giữa hai bên = "đang cân nhắc".
- Từ thẻ trái mọc ra **thanh ray thép thẳng** chạy hết chiều ngang, đứng yên suốt clip. Từ thẻ phải mọc ra **đường ray dây** bắt đầu **ngay dưới** thanh ray, hạt kim cương ngồi ở đầu.
- Hạt trượt tới: phía sau hạt đường dây đã cố định (lên xuống thật, theo lần chạy lại bắt đầu 1954-01); **phía trước hạt là ba nhánh mờ rung rinh, đổi hình liên tục** = không ai biết lãi đi đâu. Thanh ray phía trước luôn rõ, thẳng.
- Khoảng giữa hạt và ray **phát sáng xanh** khi hạt ở dưới; khi hạt vượt lên, phần ray đó **sáng hổ phách**.
- Người xem che chữ phải thấy: một thứ thẳng-đứng-yên và một thứ bắt đầu thấp hơn rồi lên xuống, tương lai mờ; có người đứng giữa hai lựa chọn.

## KEY-2 · S03.5–S03.8
**Ý đồ:** "The size of the starting gap is the thing being measured, and it can be big, small, none or reversed."

**Chuyển động:**
- Cận vạch xuất phát (một cột mốc dọc). Thanh ray ở trên, hạt ở dưới một khoảng. **Kẹp chữ U xanh "bập" vào** giữa hai vật (nảy nhẹ) — vật được chỉ ra để đo.
- Hạt tụt xuống xa: kẹp **giãn dài**. Hạt lên gần ray: kẹp **co ngắn**. Hạt chạm ray: kẹp **dẹt thành một vạch**. Hạt vọt lên trên ray: kẹp **lật ngược** (hai càng chĩa xuống), thành khung rỗng xám, và đoạn ray tại vạch xuất phát **sáng hổ phách**.
- Mỗi vị trí dừng ~0,8 s để mắt so được độ dài kẹp; một **thước khắc** dọc cạnh kẹp giữ nguyên để thấy độ dài thay đổi.
- Che chữ: "cái kẹp là thứ đang được đo; nó có thể dài, ngắn, bằng 0, ngược".

## KEY-5 · S04.1–S04.2 (method recap S11.4–S11.6)
**Ý đồ:** "The same loan is replayed over and over, starting at each moment in a long history, its rate copying the history's ups and downs."

**Chuyển động:**
- Toàn cảnh bàn: dãy núi lịch sử dài phía sau, hai khay trống phía trước, ngay dưới hai nửa dãy núi.
- Khung kính 10 năm hạ xuống mép trái dãy núi. **Đoạn sống núi trong khung được nhấc lên thành một sợi dây** (cùng hình gợn) và đặt ra trước khung làm đường ray; hạt kim cương chạy hết sợi dây (một lần chạy lại).
- Một ô **trắng giấy (chưa có kết quả)** rơi thẳng từ khung xuống khay ngay bên dưới.
- Khung **bước sang phải từng nấc một tháng**, mỗi nấc để lại **bóng viền mờ** của khung trước → thấy hai khung liền nhau chồng gần hết lên nhau. Nhịp bước **nhanh dần**; mỗi nấc thả một ô xuống đúng cột năm bên dưới; hai khay đầy dần từ trái sang phải.
- Che chữ: "cùng một thứ được chạy lại, khung trượt dọc lịch sử, mỗi lần chép đúng hình núi ở chỗ đó, mỗi lần ra một kết quả rơi xuống ngay dưới chỗ nó bắt đầu".

## KEY-3 · S05.2–S05.4
**Ý đồ:** "The variable rate goes above the fixed rate in most replays, yet ends up costing more overall in only a few — far more often in the earlier half of history."

**Chuyển động:**
- Cùng toàn cảnh, thêm **thanh ray dài** nằm dọc chân dãy núi (mỗi đoạn ứng với một tháng bắt đầu).
- Khung quét nhanh từ trái sang phải. Ở mỗi tháng bắt đầu: nếu lần chạy lại đó có lúc vượt 9% thì **đoạn ray tại đó sáng hổ phách** (dữ liệu thật, 574/753 đoạn); đồng thời một ô rơi xuống khay: **đỏ, cao** nếu đắt hơn tổng cộng (107/753), **xám, dẹt** nếu không.
- Kết thúc: thanh ray **gần như vàng hổ phách suốt chiều dài**, còn khay chỉ lốm đốm đỏ; **khay trái rõ ràng đỏ hơn** khay phải. Hổ phách (trên ray) và đỏ (trên ô khay) không bao giờ cùng một vật.
- Ô xấu nhất (tháng 4/1977) là khối đỏ cao gấp đôi, vòng tối, nhấp nháy một lần ở khay trái.
- Che chữ: "hổ phách nhiều, đỏ ít; đỏ dồn ở nửa trái (dưới nửa núi đang leo)".

## KEY-4 · S06.1–S06.5
**Ý đồ:** "Starting lower builds up savings early, and that saving has to be used up before the variable loan comes out worse."

**Chuyển động:**
- Ba làn song song trên bàn, cùng một thang: mỗi làn có thanh ray 9%, đường dây + hạt, **chồng giấy nợ** ở đầu làn (thấp dần theo tháng) và **hũ xanh** ở cuối làn. Ba lần chạy lại thật: làn trên **lãi trôi xuống** (bắt đầu 1981-08), làn giữa **một cú nhảy ngắn** qua 9% (1956-05), làn dưới **leo sớm và ở cao nhiều năm** (1976-06).
- Mỗi tháng hạt ở dưới ray: một **dòng nước xanh** chảy từ khe hạt–ray vào hũ, dòng **to nhất ở đầu khi chồng nợ cao nhất**.
- Khi hạt vượt ray: ray sáng hổ phách, **hũ rút** (nước chảy ra đáy hũ).
- Kết quả cùng lúc: làn trên hũ **đầy dần mãi**; làn giữa hũ **chỉ lõm nhẹ** rồi đầy tiếp; làn dưới hũ **cạn khô** rồi ray vẫn hổ phách.
- Che chữ: "dưới ray thì hũ đầy; trên ray thì hũ rút; phải rút cạn hũ trước khi thua".

## KEY-6 · S08.1–S08.7
**Ý đồ:** "In the worst replay, rates climbed for years and the variable loan cost a lot more — close to half again the fixed loan's interest."

**Chuyển động:**
- Khung kính 10 năm đáp xuống **sườn leo dốc nhất của nửa trái** dãy núi (bắt đầu 4/1977). Đoạn núi nhấc lên thành đường dây phía trước.
- Hạt leo **rất xa trên ray**; ray hổ phách **suốt nhiều năm**; hũ xanh đầy chút ít rồi **cạn**.
- Bên phải: hai chồng xu bạc mọc theo tháng (lãi cố định / lãi thả nổi). Khi hũ cạn, chồng thả nổi vượt lên; cuối cùng nó bằng chồng cố định **cộng một khối xu viền đỏ cao gần nửa chồng cố định** (43%).
- Che chữ: "lãi leo nhiều năm, hũ cạn, chồng tiền lãi của khoản thả nổi cao hơn gần một nửa".

## KEY-7 · S09.4–S10.3
**Ý đồ:** "A bigger starting gap means fewer losing replays and a smaller worst case — the later half of history clears completely, the earlier half never does."

**Chuyển động:**
- Phía trước: kẹp xanh giữa ray và hạt; dưới nó một **thanh trượt có núm**; núm dịch là kẹp giãn/co. Phía sau: dãy núi với hai khay ô (dữ liệu thật cho từng khoảng chênh −1…3 bước 0,25). Bên phải: chồng xu cố định + khối viền đỏ = lần chạy xấu nhất ở khoảng chênh đó.
- Núm trượt về phía **kẹp to hơn**: ô đỏ **hạ xuống thành xám** ở cả hai khay; **khay phải xám hoàn toàn** giữa chừng (từ 2 điểm); **khay trái luôn giữ một lớp đỏ mỏng**; khối viền đỏ **thu nhỏ nhưng không biến mất**.
- Núm trượt ngược về **kẹp nhỏ rồi lật ngược**: cả hai khay **đỏ lại**, khối viền đỏ **cao lên**.
- Che chữ: "kẹp càng to, đỏ càng ít; bên phải sạch, bên trái không bao giờ sạch; trường hợp xấu nhất nhỏ lại nhưng còn đó".

---
Tiêu chí tự chấm (dùng khi P kiểm mù): một nhịp **mạnh** nếu người đọc dải che chữ nói ra được động từ chính của ý (đứng yên/lên xuống; đo khoảng chênh; chạy lại dọc lịch sử; nhiều vượt–ít thua–trái nhiều hơn; đầy rồi rút cạn; leo nhiều năm–đắt hơn gần nửa; chênh lớn hơn thì ít đỏ, trái không sạch).
