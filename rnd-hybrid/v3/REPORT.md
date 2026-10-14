# Vòng 3 · Bước 2 với P3: báo cáo (14/10/2026)

**Gói 3 câu:** P3 đã sửa (gạch thưa hơn ~40 %, không gạch trên mặt, tay, chữ và thẻ; người to hơn ở K2; nhãn năm không che chữ chính) và qua cổng nén giả YouTube 360p ngay vòng đầu. Clip v3 dài 46,9 s, dùng P3 cho phần lịch sử và biến thể màu sạch cho "Today", cùng lời và giọng v2, đủ sửa a–d. Đọc mù 2 người × 2 lượt đều đạt ngưỡng chẩn đoán (5–6/6) và chỉ ra 6 lỗi hình cụ thể để sửa ở lượt sau.

## 1. Sửa P3
| Yêu cầu | Đã làm |
|---|---|
| Gạch giảm ~40 % | `HATCH.spacing = 1.67` trong `style/figure1930.js`. Khoảng cách nét ×1,67, tức mật độ nét ≈ 0,6 lần trước |
| Không gạch trên mặt, tay, chữ, thẻ | Bỏ gạch mặt. Tay, tai, da đầu `dark: 0`; cổ 0,15. Biển hiệu, trán BANK và tờ CLOSED `d = 0` (`style/street2d.js`). Thẻ chữ vẽ phẳng |
| Tăng tỉ lệ người so với ngân hàng ở K2 | Ngân hàng 13 × 10,7 m lùi về z −16,5. 4 hàng người ở z −14,6 … −8,6. Máy K2 (0,8; 2,1; −1,0), fov 44 |
| Nhãn năm không che chữ chính | Nhãn năm, ILLUSTRATIVE và dòng nguồn nằm trong vùng an toàn của lớp phủ. Kiểm trên K1, K2 |

Khung mới: `style/out/P3-K{1,2}-1080.jpg`. Dựng lại 2 lần trùng byte.

## 2. Cổng máy: nén giả YouTube (`gate/youtube_gate.py`)
Quy trình: x264 1080p 8 Mbps → giải mã → hạ 640×360 bicubic. Trong từng vùng ROI (lấy từ `window.ROI` của scene qua `gate/roi.js`) đo ngưỡng Otsu, rồi Michelson và chiều cao vùng.

Ngưỡng ghi trước: chữ ≥ 0,35 và ≥ 9 px; mặt ≥ 0,35 và ≥ 14 px.

| Khung | Vùng | Michelson | Cao (px @360p) | Kết quả |
|---|---|---|---|---|
| K1 | CLOSED | 0,427 | 35 | đạt |
| K1 | FACE | 0,577 | 70 | đạt |
| K2 | CLOSED | 0,389 | 27 | đạt |
| K2 | BANK | 0,559 | 21 | đạt |

- **Đạt ngay vòng 1**, nên không cần giảm gạch thêm.
- **Tự xem ảnh 360p** (`gate/out/P3-K{1,2}-360p.png`, các vùng cắt ×4):
  - CLOSED và BANK đọc được.
  - Mặt K1 đọc được mắt, mũi và miệng méo lo âu. Lông mày lẫn vào bóng vành mũ: **chưa rõ**, nên cần đẩy lông mày xuống thấp hơn.
  - Ở K2 người phần lớn quay lưng (85 %), mặt nhỏ, không đọc được biểu cảm; không phải vùng kiểm. Nhãn "December 1930" nằm ở góc, không che BANK hay CLOSED.
- Thêm 8 khung clip qua cùng đường nén: `clip3/out/360p/`, ghép ở `clip3/out/360p-sheet.jpg`.
- **Giới hạn:** Michelson đo tương phản, không đo đọc hiểu. Ngưỡng chưa hiệu chuẩn trên đối chứng, nên đây là **chẩn đoán**.

## 3. Clip v3
- **Tệp:** `clip3/out/clip-1080.mp4`.
  - Bản commit: crf 25, 23 MB, sha256 `0d618644…`.
  - Bản gốc: `work/v3clip3/clip-1080.mp4`, sha256 `06df44c0…33efa93`, không commit.
- **Tờ khung:** `clip3/out/to-khung.jpg`, 19 ô đánh số.
- **Số liệu:** 46,87 s · 19 cảnh · cảnh trung vị 2,17 s (1,07–4,70) · `clip3/out/build-1080.json`.
- **Lời và giọng:** dùng lại nguyên bản v2 (ElevenLabs Eric, eleven_v3, `work/v2/voice.json`, atempo 1,06). Không gọi TTS mới. ASR giữ như v2 vì cùng âm thanh. Claim theo `v2/CLAIMS.md`.

| Sửa | Kết quả |
|---|---|
| a) cận ≥ 1/3 số cảnh | 7/19 cảnh cận (A2, C, E, F, J, L1, N). Thêm H: Walt ở tiền cảnh, đám đông ở hàng cột |
| b) cảnh cột ~17,5 s không trống | Cảnh H có Walt ở tiền cảnh và đám đông chờ giữa các cột |
| c) cảnh đêm đọc được | Độ sáng trung bình các cảnh E/F/G/H/J: v2 **72,9** → v3 **113,6** (`clip/luma.py`). Đêm dùng tông nhân và quầng đèn, không bóp đen |
| d) thẻ "BEFORE 1934" | Thẻ "THE WHOLE LOAN / due at the end", có nhãn BEFORE 1934 |
| Ảnh LoC toàn khung ≤ 6 s | 4,27 s (9,1 %), 19,77–24,03 s. Phủ cùng LUT sepia và vân in ngang, hoà vào 0,7 s, hoà ra 0,8 s về cảnh P3 cùng chỗ |
| Chuyển cảnh chủ ý sang "Today" | Lau ngang "mực → màu" 0,9 s, có mép giấy, ở đầu cảnh P |

**Tất định:** dựng lại cảnh J vào cache riêng cho kết quả trùng byte (sha `5cb2b19b…`).

## 4. Đọc mù và đề xuất hiến chương
- `BLIND.md`: A (sonnet) đạt 6 và 5; B (opus) đạt 5 và 5. Cả 4 lượt có Q5 = 2. Q8 trung bình 3,25.
- Lỗi cả hai người cùng thấy:
  - thẻ 1–5 / "3–5 YEARS" (ô 4);
  - tường trống ở N (ô 17);
  - cặp "Today" không rõ là ai (ô 19);
  - K1 năm 1934 vẫn CLOSED;
  - ảnh tư liệu đổi chất liệu;
  - ô 80 % bị cắt (ô 15).
- `CHARTER-PROPOSAL.md` được viết lại cho P3: Đ1–Đ7, mỗi mục có ưu, nhược, tác động, rủi ro. Đ7 đề xuất áp thử cho chương lịch sử Tập 9 "How the 30-year mortgage was invented".

## 5. Giờ máy và chi
| Hạng mục | Giờ máy | Chi |
|---|---|---|
| Khung P3 K1+K2 (1080p, gồm khởi động) | ≈ 13 s | 0 |
| Cổng 360p (2 khung) | vài giây | 0 |
| Clip v3 1080p (4 worker) | 712,6 s → **15,2 s máy / s phim** (v2: 54) | 0 (dùng lại giọng v2) |
| Đọc mù 4 lượt (headless, khoá Console, 0 agent con) | — | **0,549 $** |
| **Tổng bước này** | | **0,549 $** (trần 3 $) |

Khoá không in, không ghi ra tệp; đã grep `blind/raw/`.

## 6. Giới hạn trung thực
- Lỗi đọc mù chưa sửa trong clip này. Đây là việc của lượt sau, theo bảng ở `BLIND.md`.
- Người đọc mù là **mô hình đọc khung tĩnh**, không phải người xem video.
- Ảnh LoC (nhãn: đám đông người gửi tiền sau khi ngân hàng đổ) có biển chữ, nên một lượt đọc mù hiểu là biểu tình.
- Năm catalog LoC (1931) lệch năm sự kiện (12/1930). Lời viết "still crowded outside" để khớp.
- Chưa kiểm trên điện thoại thật; cổng 360p chỉ là giả lập.
- Không sửa toolkit/factory, `checks/`, ep008. Không dùng mô hình người tải về, không dùng ảnh hay video AI, không làm thumbnail.
