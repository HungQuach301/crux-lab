# H2 · "Hình học của lãi" — ý đồ (viết TRƯỚC khi render, 01/10/2026)

Hướng H2: mọi ý là **đường và diện tích** trên một mặt phẳng lãi suất (ngang = thời gian, dọc = lãi suất).

Từ vựng hình (một nghĩa một vật, chỉ màu token):

| Nghĩa | Hình H2 | Màu / kênh thứ hai |
|---|---|---|
| Lãi cố định 9% | **thanh ray**: một đường ngang dày, không bao giờ động | `ink` · đường dày thẳng |
| Lãi thả nổi của Leah | **đường** chạy theo lịch sử, đầu đường là **hạt hình thoi** của Leah | đường `accent` · Leah = `ink` + **hình thoi** |
| Lịch sử T-bill | **dải địa hình** (đường + diện tích nhạt) cả 1954–2026 ở dưới khung | `accent` |
| Khung 10 năm | khung chữ nhật viền trượt trên dải địa hình | `ink-muted` viền |
| Mỗi tháng lãi thả nổi **dưới** 9% | diện tích giữa ray và đường, **dưới** ray | `positive` · vị trí dưới ray |
| Mỗi tháng lãi **trên** 9% | diện tích giữa ray và đường, **trên** ray; đoạn ray phía dưới sáng lên | `warn` · vị trí trên ray |
| Nợ còn lại | một **nêm** xám nhạt dưới trục thời gian: cao ở đầu, về 0 ở cuối | `ink-muted` mờ |
| Phần đệm | **bể diện tích** bên phải: một cột có vạch 0; mỗi tháng một lát diện tích dưới ray bay vào bể (lát dày khi nêm nợ cao), mỗi tháng trên ray cắt một lát ra | `positive` trên vạch 0 |
| Đắt hơn tổng cộng | phần bể **dưới** vạch 0; ô kết quả hình **vuông** | `negative` · sọc chéo nền + vị trí dưới vạch 0 · ô vuông |
| Không đắt hơn | ô vuông xám | `ink-muted` |
| Hai nửa lịch sử | **dải kết quả** ngay dưới dải địa hình: mỗi tháng bắt đầu một lát đứng đúng dưới chỗ khung bắt đầu; tách đôi ở 1981 (nửa leo / nửa xuống) | — |
| Tiền lãi phải trả | **diện tích hình chữ nhật** (KEY-6): lãi cố định = một khối; phần thả nổi trả thêm = khối đặt chồng lên | `ink-muted` / `negative` |
| Khoảng chênh khởi đầu | **ngoặc** đứng giữa ray và hạt ở vạch xuất phát | `positive` khi hạt dưới ray, `warn` khi hạt lật lên trên |

Ý chính H2: lãi thả nổi là một đường quanh vạch 9%; phần dưới vạch tích thành diện tích "đệm", phần trên vạch rút dần diện tích đó; kết quả là **dấu ± của diện tích còn lại** trong bể (trên hay dưới vạch 0). Chữ/số chỉ xác nhận cái hình đã nói.

## KEY-1 (S01.2–S01.3)
- **Ý (beats.md):** "Someone is weighing a cost that stays level against one that starts lower but wanders up and down."
- **Chuyển động mang ý khi tắt tiếng và che hết chữ/số:** thanh ray kéo ngang từ trái sang phải và đứng yên. Hạt thoi của Leah hiện ra ngay **dưới** ray ở vạch xuất phát; trước mặt hạt, đường thả nổi **chưa chọn được**: nhiều đường mảnh rẽ lên rẽ xuống, sáng lên rồi tắt, đổi nhau liên tục (tương lai không biết), trong khi ray không đổi. Khe hẹp giữa hạt và ray sáng xanh (nó đang rẻ hơn). Hạt lắc nhẹ giữa hai lựa chọn (nhìn lên ray / nhìn ra đường gợn) = đang cân nhắc.

## KEY-2 (S03.5–S03.8)
- **Ý:** "The size of the starting gap is the thing being measured, and it can be big, small, none or reversed."
- **Chuyển động:** một ngoặc đứng **bật** vào khe giữa ray và hạt ở vạch xuất phát, kèm thước có vạch đều đứng cạnh (= cái đang được đo). Ray đứng yên; hạt trượt xuống → ngoặc **dãn** (to), trượt lên → ngoặc **co** (nhỏ), chạm ray → ngoặc **khép** thành một vạch (không), vượt lên trên ray → ngoặc **lật** sang phía trên và đổi màu từ xanh sang hổ phách (ngược). Mỗi lần dừng, một lát diện tích đầu tiên (xanh dưới ray / hổ phách trên ray) mọc ra từ ngoặc để nói "khe này là thứ sẽ tích lại".

## KEY-5 (S04.1–S04.2; S11.4–S11.6)
- **Ý:** "The same loan is replayed over and over, starting at each moment in a long history, its rate copying the history's ups and downs."
- **Chuyển động:** đường ngắn trước hạt **giãn sang trái** thành cả dải địa hình lịch sử ở nửa dưới màn hình. Một khung 10 năm đặt lên đầu trái dải; đoạn địa hình trong khung **được nhấc lên và chép** vào mặt phẳng phía trên, dời sao cho đầu đoạn trùng hạt ở dưới ray (cùng hình dạng, cùng mép lên xuống). Khung bước sang phải từng nấc, **nhanh dần**; mỗi lần dừng, mặt phẳng phía trên vẽ lại đường mới theo đúng đoạn trong khung, và một lát nhỏ rơi **thẳng xuống** dải kết quả ngay dưới chỗ khung bắt đầu. Các khung liền nhau chồng lên nhau (vệt khung cũ còn mờ, phần chung tô đậm hơn). Lát ở đây còn **trung tính** (chưa tô kết quả).

## KEY-3 (S05.2–S05.4)
- **Ý:** "The variable rate goes above the fixed rate in most replays, yet ends up costing more overall in only a few — far more often in the earlier half of history."
- **Chuyển động:** khung quét nhanh qua lịch sử; mỗi lần dừng, đoạn ray dưới phần đường vượt 9% sáng hổ phách — lần lượt **hầu như lần nào** ray cũng có hổ phách. Dải kết quả có **hai hàng**: hàng trên (vượt 9% lúc nào đó) điền gần kín hổ phách; hàng dưới (đắt hơn tổng cộng) điền chủ yếu **xám**, chỉ một ít ô **đỏ**, và ô đỏ dồn hẳn về **nửa trái** (dưới nửa địa hình đang leo). Cuối cùng hai nửa hàng dưới tách ra thành hai bể có cột đếm: bể trái đỏ dày, bể phải gần như xám; một ô đỏ đậm (xấu nhất) đứng yên trong bể trái. Hổ phách và đỏ không bao giờ trên cùng một vật (hàng khác nhau).

## KEY-4 (S06.1–S06.5)
- **Ý:** "Starting lower builds up savings early, and that saving has to be used up before the variable loan comes out worse."
- **Chuyển động:** một mặt phẳng, nêm nợ xám cao ở đầu, về 0 ở cuối; bể đệm bên phải. Ba lần chạy cùng lúc (ba hàng, cùng thang): (1) đường **trôi xuống** — mỗi tháng lát xanh dưới ray bay vào bể, lát **dày nhất lúc đầu** (nêm nợ cao nhất), bể đầy tràn; (2) đường có **một nhấp ngắn** lên trên ray — vài lát hổ phách cắt ra khỏi bể, bể chỉ **lõm nhẹ** rồi lại đầy lên; (3) đường **leo sớm và ở cao nhiều năm** — bể đầy chút ít lúc đầu rồi lát hổ phách liên tục cắt ra, bể **cạn về 0** rồi sang phần đỏ dưới vạch 0. Mắt so ba bể ở cuối: đầy / gần đầy / âm.

## KEY-6 (S08.1–S08.7)
- **Ý:** "In the worst replay, rates climbed for years and the variable loan cost a lot more — close to half again the fixed loan's interest."
- **Chuyển động:** khung trượt và **hạ xuống** đoạn leo dốc nhất ở nửa trái dải địa hình. Mặt phẳng phía trên: đường của Leah leo **xa trên ray**, diện tích hổ phách phình to và kéo dài nhiều năm; bể đệm đầy chút ít rồi cạn, rồi chìm sâu dưới vạch 0 (đỏ). Cuối nhịp, phần đỏ của bể **gấp lại thành một khối** và bay sang đặt **chồng lên** khối diện tích lãi cố định (xám): khối đỏ cao gần nửa khối xám (43%).

## KEY-7 (S09.4–S10.3)
- **Ý:** "A bigger starting gap means fewer losing replays and a smaller worst case — the later half of history clears completely, the earlier half never does."
- **Chuyển động:** ngoặc khoảng chênh đứng trên một thanh trượt; thanh trượt kéo **dãn** ngoặc. Cùng lúc, hai bể kết quả dưới hai nửa địa hình **rút đỏ**: bể phải chuyển **hết sang xám** giữa chừng; bể trái luôn giữ một **lớp đỏ mỏng** không bao giờ hết; khối đỏ chồng trên khối lãi cố định co lại nhưng không biến mất. Rồi thanh trượt kéo ngược về phía ngoặc nhỏ, khép, lật — cả hai bể **đỏ dâng lại**, khối đỏ phình lại.

## Tiêu chí tự đánh giá (khi che chữ/số)
Một người xem mù đọc dải che nhãn mà nói được câu ý của nhịp (đúng hướng, không cần đúng chữ) = khớp. P2 chấm theo câu ý trên; hình không được dựa vào chữ.
