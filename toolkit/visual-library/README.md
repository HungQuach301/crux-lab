# Thư viện hình của kênh (v1, 04/10/2026)

Gom từ Tập 1–2 những ký hiệu **đã qua kiểm mù**. Từ Tập 3, C3 dựng **một hướng** từ thư viện này và chỉ thiết kế mới cho nhịp chưa có ký hiệu (`playbook/quality-framework.md` v2 §4). Chủ dự án có quyền yêu cầu thêm hướng ở C3.

Mã ở đây là **mã tham chiếu** chép từ tập gốc (CHARTER §3.1: đồ dùng một lần). Tập mới chép sang thư mục của tập rồi sửa; không sửa tại chỗ. Số trên hình luôn qua `CL(claimId)`.

## 1. Nền chung

| Mục | File | Nghĩa / luật | Nguồn và bằng chứng |
|---|---|---|---|
| **Bảng màu E2** | `tokens.json` | `bg #0E1116` · `surface #171B22` · `grid #2A303B` · `ink #F2F4F7` (chữ chính, người xem minh hoạ) · `ink-muted #9AA4B2` (chữ phụ, **mức cố định**) · `accent #4C8DFF` (**chỉ số thị trường**) · `warn #F2B441` (**vượt mức cố định**, huy hiệu ILLUSTRATIVE) · `costlier #C72323` (**đắt hơn tổng**; không bao giờ là màu chữ, 3,3:1) · `cushion #269783` (**đệm / khởi đầu thấp hơn**). Một vai một màu, không thêm màu. | Chủ dự án chọn ở C3 Tập 2 (E2). Mọi cặp màu dữ liệu ΔE2000 ≥ 25,6 dưới mô phỏng protan/deutan, thang xám ≥ 1,5:1 (đo bằng `cvd_report` của V09, `episodes/ep002/design/c3/cvd.md`). |
| **Phông** | `toolkit/render/fonts/` | Inter 400/600/700, số tabular. Bậc px @1080: hero 150 · number 96 · head 72 · caption 64 · label 54 · note 48 · badge 48. Sàn 40 px; đọc được ở 25% (G-014). | Hợp đồng hình Tập 1 (sàn 40 px) và Tập 2; kiểm 25% `episodes/ep002/animatic/legibility.md`. |
| **Ngữ pháp chuyển động** | — | Vẽ trái → phải = thời gian · vạch đứng yên = cố định · hạt lên xuống = lãi thả nổi · ngoặc mở rộng = khởi đầu lớn hơn · ô đỏ tắt = ít lần đắt hơn. **Không quét ngược ở cuối nhịp**; nhịp kết ở trạng thái của kết luận, giữ yên ≥ 1 s. | `episodes/ep002/design/c3/final/system.md` §4 (bài học KEY-7). |
| **Nhãn nghĩa** | — | Khi hình chưa tự mang ý: nhãn ≤ ~8 từ, ≥ 40 px, hiện ≥ 1 s cho mỗi 3 từ; hai ý thì hai dòng. Nhãn không thêm vật, không thêm số ngoài claim. | Lệnh C4c Tập 2; nâng KEY-2/5/6 từ trượt lên đạt "đúng nghĩa" ở cổng gốc vòng 2. |
| **Mã chung** | `code/d2/engine.js` | Bậc chữ, `CL()`, easing, API khung, tự kiểm (chữ↔đồ hoạ ≥ 4 px, tương phản, vùng an toàn). Cờ `MASK` là di sản (phép che chữ/số đã bỏ, D-005 Q3). | Tập 2 C3 final. |

## 2. Ký hiệu

Kiểm mù "cổng gốc" = tắt tiếng, GIỮ chữ/số, dải 6 khung, người đọc vai khán giả đích, chấm độc lập mù tập (từ C4b Tập 2). Điểm = tổng 3 người đọc (1 / 0,5 / 0). "Khuyên" = số câu trả lời tự rút lời khuyên.

| # | Ký hiệu | Mang nghĩa | Mã · xem trước | Kiểm mù đã qua | Dùng thế nào |
|---|---|---|---|---|---|
| **V1** | **Lưới ô chạy lại** (dải chỉ số trên, mỗi ô một lần chạy lại xếp theo tháng bắt đầu, vạch đứt chia thời kỳ) | "cùng một khoản vay chạy lại từ mọi tháng bắt đầu trong lịch sử; mỗi ô một kết quả" | `code/h3/scenes.js` (`K5`, `cells`, `ridge`, `split`) · `previews/ep002-KEY-5.png` | Tập 2 KEY-5: che chữ C3 3/3; cổng gốc v2 **3/3, khuyên 0** | **Mạnh nhất.** Dùng cho mọi phép "phát lại lịch sử". |
| **V2** | **Thùng token / ô đỏ** trên lưới V1 (ô đổi `costlier` khi lần chạy đó đắt hơn tổng; dải `warn` = tháng vượt mức cố định) | "phần lớn lần chạy vượt mức cố định, nhưng chỉ một phần nhỏ đắt hơn tổng" | `code/h3/scenes.js` (`K3`, `tally`) · `previews/ep002-KEY-3.png` | Tập 2 KEY-3: cổng gốc v1 3/3; v2 **2/3, khuyên 0** | Dùng cho tỉ lệ "bao nhiêu lần tệ hơn". Luôn hiện hai thời kỳ cùng lúc. |
| **V3** | **Đường lãi so vạch** (vạch cố định `ink-muted` đứng yên; đường thả nổi `ink` + hạt thoi; phần vượt vạch `warn`) | "lãi thả nổi lên xuống quanh một mức cố định" / "lãi thị trường xuống dưới ngưỡng" | `code/d2/k1.js`, `engine.js` · Tập 1: `episodes/ep001/animatic/src/` S05 · `previews/ep001-S05.png` | Tập 2 KEY-1 (dùng V3): cổng gốc v1 3/3. Tập 1 S05 (vạch một điểm): đối chứng cổng gốc 1/1; C4 Tập 1 20/20 (có chữ) | Ký hiệu nền cho mọi so sánh lãi. |
| **V4** | **Một người, hai lời mời** (hình người `ink` không mặt, thoi ở ngực; hai thẻ cùng độ cao; một vạch mức cố định kéo liền qua hai thẻ; thẻ thả nổi bắt đầu dưới vạch) | "một người cân nhắc hai khoản vay: một cố định, một thả nổi bắt đầu thấp hơn" | `code/d2/k1.js` · `previews/ep002-KEY-1.png` | Tập 2 KEY-1: che chữ C3 vòng 2 2/3; cổng gốc v1 3/3; v2 3/3 nhưng **khuyên 1** | Dùng cho cold open / đặt vấn đề. Cần câu đối trọng trong lời (WRITER, `playbook/episode.md` §3). |
| **V5** | **Phóng vào trường hợp xấu nhất** (khung phóng trên lưới V1 + hai chồng so sánh; khối thêm cao đúng tỉ lệ) | "lần chạy tệ nhất bắt đầu ở tháng X, lãi leo nhiều năm, tốn thêm Y% tiền lãi" | `code/h3/scenes.js` (`K6`) · `previews/ep002-KEY-6.png` | Tập 2 KEY-6: cổng gốc v1 0,5/3; sau nhãn nghĩa v2 3/3 nhưng **khuyên 1** | Dùng kèm nhãn nghĩa + câu đối trọng. |
| **V6** | **Ngoặc khởi đầu** (ngoặc `cushion` giữa vạch cố định và điểm bắt đầu thả nổi; co lại, về 0, đổi dấu thành `warn`) | "khoảng chênh lúc bắt đầu là thứ được đo; có thể bằng 0 hoặc âm" | `code/d2/k2.js` · `previews/ep002-KEY-2.png` | Tập 2 KEY-2: trượt 4–5 vòng khi che chữ; chỉ đạt "đúng nghĩa" khi có nhãn hai dòng (v2 3/3, **khuyên 1**) | **Loại "hình minh hoạ lời"**: luôn kèm nhãn; không tính vào ngưỡng hình. |
| **V7** | **Thẻ phương pháp** (tiêu đề "How we know this" + ≤ 6 dòng giới hạn mô hình; mỗi số qua claim) | Mẫu trình bày, không phải ký hiệu mang ý | `code/method_card.example.json` · `previews/ep002-S11-method-card.png` | Không kiểm mù hình. Qua kiểm 25% (`legibility.md`); chủ dự án duyệt dạng "1 câu lời + thẻ + mô tả" (C2b Tập 2) | Mặc định cho mọi đoạn phương pháp. |
| **V8** | Tập 1: **thước ba mốc** (S18), **hai câu trả lời nhanh** (S08), **bán sau 3 năm** (S16), **lãi chạm đáy** (S01) | xem `episodes/ep001/animatic/intent.md` cột 1 | `episodes/ep001/animatic/src/` · `previews/ep001-S18.png`, `-S08`, `-S16`, `-S01` | Đối chứng cổng gốc Tập 2: mỗi cảnh **1/1** (1 người đọc); C4 Tập 1 20/20 (có chữ) | Bằng chứng mỏng (1 người đọc/cảnh). Dùng lại thì kiểm lại như ký hiệu mới. |
| **V9** | **Bóng lạm phát** (N1 Tập 4: trần cố định `ink-muted` liền, đứng yên; đường ĐỨT cùng màu = chính số tiền đó giữ sức mua theo CPI-U; chú thích "consumer prices, not house prices") | "một mức tiền ghi cứng không đổi trong khi chính nó tính theo giá hôm nay đã cao hơn nhiều" | `code/ep004/n1.js` · `previews/ep004-N1.png` | C3 Tập 4 (B08) nghĩa 2/2 cả hai vòng; khuyên chỉ dạng thận trọng chung (A9, không tính) | Trần/hạn mức/ngưỡng danh nghĩa không chỉ số hoá (thuế, bảo hiểm, giới hạn đóng góp). Trục từ 0; luôn kèm chú thích nguồn chỉ số. Nạp qua `custom_symbols`. |
| **V10** | **Thang ngưỡng** (N2 Tập 4: thước giá dọc cùng thang, mỗi bậc một vùng, thanh tăng trưởng mảnh bên trái dài ∝ mức tăng; vạch tham chiếu; chế độ `phoenix` một mốc + chấm nhân vật, `ladder` đủ bậc; bản G2 thêm `line`/`bars` = mẫu V3/thanh + nhãn nghĩa) | "mỗi nơi có một mức giá mà trên đó đã qua ngưỡng; nơi tăng nhanh thì bậc thấp" | `code/ep004/n2.js`, `code/ep004/n2-g2.js` · `previews/ep004-N2.png` | C3 Tập 4 v2: B13, B14 nghĩa ĐẠT; cổng gốc C4 v2 6/7 (B11 Miami `line` trượt: trục bị đọc thành giá trị nhà → ghi rõ "Gain" trên trục) | Ngưỡng tự đối chiếu theo vùng/nhóm (G-013). ≤ 13 bậc; nhãn bậc ≥ 40 px; chấm nhân vật luôn ILLUSTRATIVE. |

## 3. Không đưa vào thư viện (đã trượt)
- **Hũ đệm** (KEY-4 Tập 2): cổng gốc v2 1,5/3, **khuyên 2** — người đọc đọc thành "tiết kiệm/an toàn". Mã ở `episodes/ep002/design/c3/final/src/k4*.js`.
- **Hai cột thời kỳ** (KEY-7 Tập 2): 7 lần kiểm, không lần nào đạt; người đọc gán chuyển động cho "trả nợ theo thời gian". Mã `k7*.js`.
- **Vật thể thật 3D** (H1 Tập 2): che chữ C3 2/7; render 13,5–20 s máy/s phim. *(Lịch sử: D-010 thay luật "không thế giới 3D" bằng thế giới 3D tối giản — xem §5; H1 vẫn trượt vì vật chân thực, không có chế độ đồ thị.)*

## 4. Thêm ký hiệu mới
Một ký hiệu vào thư viện khi: (1) qua cổng gốc ở C3 hoặc C4 (≥ 2/3, khuyên 0) với người chấm độc lập mù tập; (2) có một câu "mang nghĩa" và luật màu/chuyển động không trùng nghĩa ký hiệu khác; (3) có mã tham chiếu và một ảnh xem trước. Phiên tổng kết của tập thêm dòng vào bảng §2, ghi tập và số đo.

## 5. Thế giới 3D tối giản (D-010, Mốc V, 06/10/2026)

Gen kênh: **low-poly, màu kênh, không chân thực ảnh, nhân vật không mặt, không chi tiết trang trí không mang nghĩa.** Một thế giới, hai chế độ máy quay:
THẾ GIỚI (phối cảnh: người, nhà, khu phố) ↔ ĐỒ THỊ (máy khoá chính diện vào chính vệt đỉnh chồng tiền). Số và nhãn so sánh chỉ ở chế độ đồ thị.

**Mã dùng chung, không chép** (khác §2): `toolkit/factory/world/lib3d.js` (vật thể có tham số), `core.js` (máy quay theo spine, lớp phủ 2D, nhật ký quy tắc 1),
`spine.py` (spine v2), `render_shots.js` (render theo cảnh có cache), `audio.py` (tiếng theo spine), `build_seg.py` (một lệnh dựng + kiểm một đoạn).
Mỗi đoạn chỉ viết `spine.py` + `scene.js` của nó. Mẫu: `moc-v/seg/ep004/`, `moc-v/seg/ep005/`. Vật thể mới mỗi tập: qua C3 bằng clip có chuyển động và âm (E4, D-010 quy tắc 4).

| # | Vật thể (`lib3d.js`) | Tham số chính | Mang nghĩa | Xem trước | Bằng chứng |
|---|---|---|---|---|---|
| **W1** | `House` | `w, wall, roof, lit` | căn nhà của nhân vật; ở chế độ đồ thị **đứng trên mặt đất cạnh chồng**, không phải dữ liệu | `previews/world-ep004-house-stack.png` | Tập 4 đoạn (a) v3l: cổng gốc K1 3/3 · K2 3/3 · 0 khuyên (`moc-v/eval/v3-blind22-raw`); L3 4·4·4·4·4·4 chấm trên v3k (nhà ở đồ thị khi đó chưa đứng cạnh chồng) |
| **W2** | `Stack` | `unitUsd, bundleUsd` (mệnh giá bó **cố định**), `.set({usd, fromUsd, warnAboveUsd, tintBelowUsd})` | số tiền = chiều cao (số bó × độ dày bó); đỉnh chồng vẽ ra đường dữ liệu | như trên · `previews/world-ep004-chart.png` | như W1; Tập 5 đoạn (b) E2 3/3 · 0 khuyên (`moc-v/eval/e5-blind10-raw`) |
| **W3** | `Beam` | `length, color` | mức cố định (trần, ngưỡng) — đứng yên, `ink-muted` | `previews/world-ep004-chart.png` | Tập 4 K1/K2 như W1 |
| **W4** | `Person` | `h, color` | nhân vật minh hoạ không mặt (luôn ILLUSTRATIVE) | `previews/world-ep004-house-stack.png` | Tập 4 K1 như W1 |
| **W5** | `Ribbon` | `maxPts, width, color, z` | vệt đỉnh chồng theo thời gian = đường của đồ thị | `previews/world-ep004-chart.png` | Tập 4 K2 như W1 |
| **W6** | `Fan` | `maxSeg` | bó đường phát lại (mỗi tháng mua một đường) | — | Tập 5 E1 3/3 · 0 khuyên (`e5-blind10-raw`) |
| **W7** | `Shield` | `size, color` | bảo hiểm khoản vay gắn trên mái | `previews/world-ep005-shield.png` | Tập 5 E2 3/3 · 0 khuyên |
| **W8** | `Neighborhood` | `n, seed, spanX, z, size` | "nhiều giao dịch" → một chỉ số | `previews/world-ep004-hood.png` | trong clip L3 đã duyệt; **chưa** nằm trong khoảng cổng gốc → dùng lại thì kiểm |
| **W9** | `Apartment` | `w, floors, color` | lối "thuê tiếp" | `previews/world-ep005-fork.png` | như W8 |
| **W10** | `Crates` (+ `Check`: séc lớn lên; `litOf`, `checkScale`) — chuyển từ `episodes/ep006/world/obj6.js` (F-12) | `n=10, size, gap`; `.set({value, appear, pulse})`; `Check({w, base})`, `.set({k, appear})` ×1,02^k | hàng 10 thùng = những gì khoản trả **đầu tiên** mua được; thùng i sáng `clamp(n·value − i, 0, 1)` (mờ liên tục, trần n); séc lớn lên cạnh hàng để thấy "séc tăng mà thùng vẫn tối". Không chữ trên thùng; số chỉ ở đồ thị | `previews/world-ep006-crates.png` | Tập 6 C3 cổng gốc tắt tiếng vòng 2: S07/S24/S27 nghĩa 2/2 · khuyên 0/2 mỗi đoạn; **chủ dự án duyệt 08/10** (nhánh ep006 `gates/C3-answer.md`). S29 (ba hàng cạnh nhau) trượt khuyên 1/2 sau 3 vòng → kiểm lại ở C4. Hàng thùng không séc: khuyên 8/8 ("khoản đều") — không dùng một mình |
| — | `Studio`, `Burst`, `setOpacity`, `PALETTE` | — | ánh sáng/sàn, loé khi chạm, mờ dần, màu vật liệu (màu dữ liệu vẫn là E2) | — | hạ tầng |

Bằng chứng tái lập: dựng lại hai đoạn bằng `build_seg.py` cho hình và tiếng **trùng MD5** (giải mã) với clip v3l/E5h (bản sửa sau L3; L3 chấm trên v3k/E5g) (`moc-v/b3/factory-proof.md`).
