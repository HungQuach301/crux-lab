# C3 — trả lời của chủ dự án (Tập 6) · 2026-10-08

Nguồn: lệnh mở phiên P3 (chủ dự án dán vào phiên mới theo prompt PLAN §7; gói `gates/C3.md`, issue [#49](https://github.com/HungQuach301/crux-lab/issues/49)). Nguyên văn:

> 1 Duyệt N1 hàng 10 thùng + séc lớn lên cho S07/S24/S27, ghi visual-library §5. S29 chọn (a): giữ v2, ghi ngoại lệ sổ gu; chốt C4: kiểm mù bản có lời S29 phải 0 câu khuyên sản phẩm (chọn khoản gắn CPI/COLA), không đạt thì quay lại hỏi tôi. Hàng chờ của đạo diễn (S24, S27 mốc năm, S29 nhấn "month") và đồng bộ S24/S27/S29 sửa ở C4.
> 2 Nhạc hiệu A + khúc đóng hợp A. Bước nhà máy +12 dB sau chữ cuối làm trên factory-*, kiểm −14 LUFS / ≤ −1 dBTP và lời không bị lấn.
> 3 (a) Giữ v3; "hỏi công ty bảo hiểm / hỏi báo giá" = thận trọng chung, không tính. Chốt C4: kiểm mù bản có lời cả tập, câu khuyên sản phẩm phải 0; chạy song song rubric cũ và rubric ba cờ (K4.1 câu 3), 2 người chấm. Duyệt ElevenLabs ≈ 7.700 ký tự cho Tập 6. Merge squash ep006 → main ở P4 (265 MB WAV).

Kèm trong lệnh: **không mở C4 khi `main` chưa có khoá K gồm kind Tập 6** (KINDS trong `checks/py/r_model.py`; phiên K đang làm, khoá K4.0.2). Có khoá → merge `main` vào `ep006`, chạy S01/S05, viết `contract.json` rồi mới C4. Chưa có → làm việc không phụ thuộc K (áp C3, giọng cả tập, đo độ dài thật ≥ 8:10, nhà máy F-12 trên `factory-*`, merge `main` khi xong), rồi kiểm lại `main`; vẫn chưa có thì đóng phiên và báo. **K4.1 (V11, F11, rubric khuyên) phải có trên `main` trước C5**; chưa có thì dừng trước C5 và báo.

| Câu | Quyết định |
|---|---|
| 1 | **Duyệt N1** hàng 10 thùng + séc lớn lên ×1,02/kỷ niệm cho **S07/S24/S27** (bản v2) → `toolkit/visual-library/README.md` §5 |
| 1 · S29 | **(a)** giữ **v2**, ghi ngoại lệ sổ gu (câu khuyên khi tắt tiếng đến từ nội dung — ca xấu nhất) |
| 1 · chốt C4 | Kiểm mù **bản có lời** của S29: câu khuyên sản phẩm (chọn khoản gắn CPI/COLA) = **0**; không đạt → hỏi lại chủ dự án |
| 1 · hàng chờ C4 | Lượt đạo diễn (S24 10–19 s đứng; S27 mốc năm trên thanh thời gian; S29 nhấn "month") + đồng bộ ±0,2 s S24/S27/S29 |
| 2 | **Nhạc hiệu A** ("câu hỏi rồi lời giải") + **khúc đóng hợp A** |
| 2 · nhà máy | Bước **+12 dB trong 0,5 s sau chữ cuối** trên nhánh `factory-*`; kiểm **−14 LUFS / ≤ −1 dBTP** và lời không bị lấn |
| 3 | **(a)** giữ kịch bản **v3**; "hỏi công ty bảo hiểm / hỏi báo giá" = **thận trọng chung, không tính** |
| 3 · chốt C4 | Kiểm mù bản có lời **cả tập**: câu khuyên sản phẩm = **0**; chấm **song song rubric cũ (A9) và rubric ba cờ** (K4.1 câu 3), **2 người chấm** |
| 3 · EL | **Duyệt ElevenLabs ≈ 7.700 ký tự** cho Tập 6 |
| 3 · repo | P4 merge **squash** `ep006` → `main` (≈ 265 MB WAV ở df9c2d4 không vào lịch sử `main`); không force-push |
| K | Không C4 khi chưa có kind Tập 6 trên `main`; không C5 khi chưa có K4.1 |
