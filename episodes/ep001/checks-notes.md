# Tập 1 — ghi chú cho Phiên K (không sửa `checks/`)

LOCK đang dùng: `b97bfc6bb6524e9fd108e708aa96a01c19c965b42cf9bcda9d2e9d7ce738fe74`.

## 1. T1 xung đột với sổ gu G-006 (2026-09-28)

**Luật.** T1 đòi tiếng dữ liệu nổi trong dải 1,5–8 kHz:
- ≥ 3 dB ở mọi cửa sổ đo;
- ≥ 1 dB ngay cả trong cửa sổ số được đọc `[onset − 0,5 s, end + 1,6 s]`, tức là **trong lúc có lời**.

Ngưỡng hiện là **ngưỡng tạm** (`checks/README.md`, mục "Ngưỡng tạm"), hiệu chỉnh sau Tập 1 bằng H8.

**Chủ dự án (nghe `m0-sample` trên loa điện thoại, 2026-09-28):**
- *"Lời đọc rõ nhưng VẪN BỊ tiếng dữ liệu lấn."*
- *"Không tăng +10 dB."*
- Sổ gu G-006: *"lời đọc là ưu tiên số một; tiếng dữ liệu không được lấn lời; không giải bằng cách tăng âm lượng."*

**Số đo trên mẫu (đo của bên dựng, cùng cửa sổ 0,15 s và cùng dải với T1).**

| Bản | Tiếng dữ liệu so với lời (RMS toàn dải) | Độ nổi 1,5–8 kHz | Kết quả |
|---|---|---|---|
| +10 dB (m0, bản chủ dự án đã nghe) | −6 dB | 1,4–7,9 dB khi có lời | T1 máy kiểm: 3/4 cửa sổ đạt. **Chủ dự án: lấn lời.** |
| 0 dB | −16 dB | 0,2–1,8 dB khi có lời | T1 trượt |
| Ba bảng âm mù S1–S3 | khoảng −21 dB | trung vị 0,0 dB; chỉ các cửa sổ ở chỗ lời nghỉ mới nổi (tới 6,6 dB) | T1 sẽ trượt |

Ba bảng âm dùng chung luật (`toolkit/audio/sonify_palettes.py`):
- sidechain −8 dB khi có lời;
- gần như bỏ hẳn 1–4 kHz khi có lời (tiếng dữ liệu thấp hơn lời 31–56 dB trong dải đó);
- dời nốt vào khe giữa âm tiết (−60…+120 ms);
- giữ nguyên ánh xạ cao độ.

**Kết luận.** Tiếng dữ liệu "không lấn lời" và "nổi ≥ 1 dB ở 1,5–8 kHz trong lúc có lời" khó cùng đạt. Phần lớn năng lượng 1,5–8 kHz của lời là phụ âm và formant cao, nên muốn nổi ở dải đó thì tiếng dữ liệu phải to gần bằng lời trong chính dải đó.

**Quyết định cho Tập 1 (chủ dự án):** gu thắng T1. T1 không phải luật cứng (CHARTER §5 chỉ kể lỗi số liệu, nguồn, ILLUSTRATIVE, chính sách nền tảng). Tập 1 giao theo G-005/G-006, và T1 được báo cáo nguyên số đo, **không tối ưu để qua T1**.

**Đề xuất để Phiên K cân nhắc** (không phải yêu cầu; K và chủ dự án quyết):
- đo T1 ở **khoảng lời nghỉ** (ngoài cửa sổ có lời), hoặc bằng **tỉ lệ sự kiện nghe được ở một trong hai phía của cú cắt lời**, thay vì đòi nổi giữa lúc có lời;
- trong lúc có lời, thay "độ nổi ≥ 1 dB" bằng một tiêu chí không lấn lời: tiếng dữ liệu ở 1–4 kHz ≤ lời − X dB, cộng với việc nó có mặt ở dải khác;
- hiệu chỉnh bằng điểm H8 của chủ dự án trên bảng âm được chọn (`review-m1/sonify-S1/S2/S3.mp4`).

## 2. Luật gắn với bài D (đã ghi ở `contract.json`)

- S01, S05, S06: mô hình hưu trí của bài D.
- V04, V09: nhân vật `1966`/`mirror`. Tập 1 dùng `small`/`large`/`median`.
- S03, S04: nguồn chính Damodaran + đối chiếu FRED, file `annual.csv`. Tập 1 dùng FRED `MORTGAGE30US` + Optimal Blue + HMDA.

Tập 1 cần hợp đồng riêng cho các luật này trước khi kiểm M3.

## 3. Điều khoản HMDA (DX-H4)

Chưa trích được câu điều khoản nào: trang nằm ở `www.consumerfinance.gov`, bị proxy chặn. Xem `data/hmda-sources.json`.
