# Tiền kỳ (c) — kết quả đọc mù clip vật thể mới (ý đồ `gates/PRE-objects-intent.md`, 13/10)

| Vật | Vòng | Người đọc 1 | Người đọc 2 | advice_stated | Kết quả | Sửa |
|---|---|---|---|---|---|---|
| N1 **the street** (lưới 307 nhà: cột = năm, hàng = tháng) | 1 | 1 | 1 | 0 | **ĐẠT 2/2** | — (trước vòng đọc: hàng 307 nhà một dòng → lưới năm × tháng, vì khung đồ thị chỉ 3 px/nhà — sửa bố cục, chưa đọc mù) |
| N2 **the rent tag** (thẻ RENT 5 → 4 → 6 %, cả lưới đổi đèn) | 1 | 1 | 1 | 0 | **ĐẠT 2/2** | — |
| N3 **Nina + đèn riêng** | 1 | 0 | 0,5 | 0 | TRƯỢT | `fix: picture` — người đọc thấy cô **bước về phía ngôi nhà** = "chuyển từ thuê sang mua" (hình ngả về một lựa chọn) → vòng 2: đứng yên giữa, đèn đưa về bên đang nhìn, thẻ RENT / BUY trên hai căn |
| N3 | 2 | 0,5 | 0,5 | 0 | **TRƯỢT (2 vòng — hết hạn luật tạm)** | đọc ra (a) đèn riêng + (c) "weighing renting against buying"; trượt (b) vì rubric ghi trước có "bước về phía giữa" mà bản sửa đã bỏ có chủ ý — **không sửa rubric sau kết quả**. → G1: trước/sau cho chủ dự án |

Lượt: 8 đọc + 2 chấm headless Sonnet (khoá Console), ≈ $0,27. Nguyên văn: `preprod/read-r1/`, `preprod/read-r2/` (khoá `key.json`, `label-key.json`). Cờ `advice_inferred` 4/8, `caution_only` 5/8 (báo, không chặn — A28).
Clip (không commit, `work/objclip/`): `street.mp4` 7 s, `tag.mp4` 7 s, `nina.mp4` 6 s (vòng 2) — 960×540, có âm vật thể; dải `work/objclip/strips/*.png`.
**Ghi chú K (quy tắc 1):** thẻ RENT mang chữ số ở chế độ thế giới — K-brief mục 4.

## N4, N5 (vật WRITER khai ở C2 v1; rubric bổ sung ghi trước)
| Vật | Vòng | Người đọc | advice_stated | Kết quả | Sửa |
|---|---|---|---|---|---|
| N4 **the glass box** | 1 | 0,5 · 0,5 | 0 | TRƯỢT | `fix: picture` — đọc ra hộp đầy dần nhưng "tiền thu cho chủ nhà" → vòng 2: bó tiền bay ra từ CỬA căn hộ có thẻ RENT, Nina + đèn đứng cạnh |
| N4 | 2 | 1 · 0,5 · 0,5 (người 3 do lệch) | 0 | **TRƯỢT 1/3 (2 vòng — hết hạn)** | 3/3 đọc ra (a) tiền để dành của người thuê + (b) đầy dần; **(c) "không đầu tư" 1/3** → G1 trước/sau. Đề xuất: giữ hình vòng 2; (c) do lời S05.1 mang + nhãn nghĩa "cash, not stocks" (cách cuối, E6, sau 2 vòng hình) |
| N5 **the fog** | 1 | 0 · 0 | 0 (inferred 2/2) | TRƯỢT | `fix: picture` — "nhà bị xoá = nhà khan hiếm" → vòng 2: sương không phủ nhà; lô đất trống viền đứt chạy vào sương |
| N5 | 2 | 0 · 0 | 0 (**inferred 2/2: "buy now before there are none left"**) | **TRƯỢT (2 vòng — hết hạn)** | → G1. **Đề xuất bỏ N5**: hình sương/lô trống đọc thành khan hiếm nhà và gợi "mua sớm" (rủi ro lời khuyên); thay bằng chế độ đồ thị: lưới dừng ở cột 2016 + nhãn "data ends July 2026 · history, not a forecast" |
Lượt N4/N5: 9 đọc + 3 chấm, ≈ $0,27. Nguyên văn `preprod/read-n45-r1/`, `read-n45-r2/`, `read-n45-r2b/`.
