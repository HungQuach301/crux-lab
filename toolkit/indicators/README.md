# Thước CHỈ BÁO (tổng kết Tập 5 §3.2–3.3; cine-lab Q15, Q26–Q31) — không phải luật, không chặn tập

Chạy ở C4 (animatic) và C5 (bản cuối), báo trong gói; thước mới thành luật chỉ qua phiên K sau hiệu chuẩn (CHARTER §4, §6). Hiệu chuẩn
08/10 trên Tập 1 (đối chứng âm), Tập 4 v3k, Tập 5: `tongket-t5/indicators/CALIBRATION.md`. Thước xếp sai thứ tự → bỏ.

| Thước | Lệnh | Trạng thái (08/10) |
|---|---|---|
| Nhịp trên spine (quãng có lời không cú máy, không vật đổi trạng thái > 8 s; số trên nhãn) | `python3 toolkit/indicators/spine_pace.py <spine.json…> [--labels]` | chỉ báo, **chưa hiệu chuẩn** (đối chứng dương 2/4) |
| Đa dạng khung nhìn (máy quay, không đo độ sáng) | `python3 toolkit/indicators/viewpoints.py camera out/camera.json` · `… spine <spine.json…>` | **chỉ báo, xếp đúng** |
| Mỗi vật thể đổi trạng thái có tiếng riêng (cine-lab Q28 c) | `python3 toolkit/indicators/av_indicators.py states spine <spine.json…>` · `… states episode out/` | xem CALIBRATION (mục 14) |
| Tông màu theo hồi (cine-lab Q30) | `python3 toolkit/indicators/av_indicators.py tone <video> out/timeline.json` | xem CALIBRATION (mục 14) |
| Chấm mù khung (cine-lab Q27) | `python3 toolkit/indicators/blind.py frames prep|tally …` | **BỎ** (xếp Tập 1 cao nhất) — giữ mã để tái lập |
| Xem liền mạch mù (cine-lab Q31) | `python3 toolkit/indicators/blind.py flow prep|tally …` | **BỎ** (xếp v3k ≤ Tập 1) — giữ mã để tái lập |

Lượt headless (`blind.py … prep` sinh `run.sh`) chạy NỀN bằng công cụ nền của phiên, không `&` (`playbook/episode.md` §11b).
