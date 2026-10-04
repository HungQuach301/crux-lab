# Tập 2 · C3 final — Hệ hình D2 (H2 + H3, một bộ màu, một phông)

DESIGN LEAD, 01/10/2026. Quyết định chủ dự án C3: hướng **D2** = H2 "hình học của lãi" + H3 "dòng thời gian lịch sử", **chọn theo nhịp**; màu **E2**. Máy đọc: `tokens.json`. Mã chung: `src/engine.js` (mọi khung qua cùng hàm chữ `text()`, cùng `CL()`, cùng cờ `MASK`).

## 1. Nền theo nhịp
| Nhịp | Nền | Vì sao |
|---|---|---|
| KEY-1 (S01) | **H2** (mặt phẳng lãi) + hình người | thiết kế lại: một người cầm hai tấm lời mời, mỗi tấm một đường lãi |
| KEY-2 (S03) | **H2** | ngoặc giữa ray và hạt đọc tốt nhất ở H2 |
| KEY-5 (S04) | **H3** | địa hình + khung 10 năm bước + ô rơi xuống đúng năm |
| KEY-3 (S05) | **H3** | dải hổ phách ≫ ô đỏ; đỏ dồn nửa trái (1/1 ở C3) |
| KEY-4 (S06) | **H2** | diện tích dưới ray → bể đệm |
| KEY-6 (S08) | **H3** | phóng vào cửa sổ 4/1977 (1/1 ở C3) |
| KEY-7 (S09–S10) | **H3** + nêm (ngoặc H2 quét thành nêm) | thiết kế lại: chỉ một chiều, hẹp → rộng, kết ở trạng thái rộng |

## 2. Màu (token Tập 1 + bí danh E2; không thêm màu)
| Vai | Màu | Kênh thứ hai |
|---|---|---|
| nền / khối che chữ | `bg #0E1116` / `surface #171B22` | — |
| ô "không đắt hơn", viền thùng | `grid #2A303B` | — |
| chữ chính / phụ (D5) | `ink #F2F4F7` / `ink-muted #9AA4B2` | — |
| T-bill (địa hình) | `accent #4C8DFF` | đường mảnh + mặt 16% |
| lãi cố định 9% (ray) | `ink-muted`, dày, không bao giờ động | đường ngang |
| **Leah** | `ink` + **hình thoi** | hạt thoi đầu đường lãi; KEY-1: hình người `ink` có thoi khoét ở ngực |
| lãi vượt 9% / khởi đầu đảo | `warn #F2B441` | luôn **trên** ray |
| **đắt hơn tổng cộng** | **costlier `#C72323`** (E2, thay `negative`) | ô; thanh có **sọc chéo `bg`**; không bao giờ là màu chữ (3,3:1) |
| **đệm / tiết kiệm**, ngoặc/nêm khởi đầu | **cushion `#269783`** (E2, thay `positive`) | mảng đặc, luôn **dưới** ray |
| huy hiệu | `warn` nền, chữ `bg`: ILLUSTRATIVE | mọi khung có khoản vay của Leah |

## 3. Chữ (Inter 400/600/700, số tabular; G-014)
Bậc px @1080: hero 150 · number 96 · head 72 · caption 64 · label 54 · note 48 · badge 48. Sàn 40 px; `text()` chỉ nhận các bậc này nên chữ nhỏ nhất là 48 px (32 px ở 720p). Mỗi lúc ≤ 1 số nhấn + huy hiệu; số chỉ qua `CL(claimId)`.

## 4. Chuyển động — một nghĩa mỗi loại
vẽ trái→phải = thời gian · ray đứng yên = cố định · hạt thoi lên xuống = lãi thả nổi · ngoặc/nêm mở rộng = khởi đầu lớn hơn · ô đỏ tắt / thanh đỏ ngắn lại = ít lần đắt hơn · bập bênh hai tấm thẻ = cân nhắc. **Không quét ngược ở cuối nhịp** (bài học KEY-7): nếu có phía hẹp/âm thì đi trước, nhịp kết ở trạng thái của kết luận. Giữ yên ≥ 1 s cuối nhịp.
