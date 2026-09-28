# Tập 1 — "Ở mức chênh lãi suất nào thì tái cấp vốn hoàn lại được chi phí đóng hồ sơ?"

Đề tài 7, dòng 1 (vay và nợ, quyết định về nhà). Phiên D1, nhánh `ep001`.

## Trạng thái: M1b XONG (sửa theo duyệt M1), dừng chờ chủ dự án duyệt; chưa làm M2

Duyệt M1 của chủ dự án (2026-09-28): cold open TRUNG BÌNH; câu móc lại rõ lời hứa; toàn bài TRUNG BÌNH (thiên về diễn giải số liệu); chọn S2 (không lấn lời). Sổ gu: G-005 · chọn, G-007, G-008.

| Việc | Kết quả |
|---|---|
| Sổ gu | `taste-ledger.md`: lựa chọn S2, G-007, G-008 (nguyên văn, nguồn "duyệt M1 Tập 1"). Âm sắc S2 điền vào `preprod/cue-sheet.md`. |
| Phương pháp hoà vốn | `model/refi.py`: `break_even_balance` (tiết kiệm cộng dồn + chênh lệch dư nợ ≥ phí) là **đáp án chính**; `both`, `net_after`, `cut_for_break_even_balance`; mô phỏng lịch sử tính cả hai cách. 12 test (có bản cài đặt độc lập tính từng tháng). Bảng: `review-m1b/break-even-methods.md`, `out/break-even-methods.csv`. |
| Kịch bản | Viết lại theo G-007/G-008: cold open là Maya và khoảnh khắc lãi tuần này; ba nhân vật ILLUSTRATIVE (Maya, Dan, Priya: trung vị HMDA 2025 theo quy mô); luận điểm "most calculators say 24; counting what she still owes, 30". 83 câu, 1.275 từ, 73 claim, không cảnh nào > 2 số mới. |
| Giọng | Sinh lại câu đổi; vòng lặp 4 take v3 + dự phòng multilingual_v2. Mỗi hồi 151–158 wpm; mọi câu trong 120–190; 0 từ quan trọng bị thiếu. Câu có "rates" ("raids") đã thay. Vòng này tốn **10.883 ký tự**. `script/table-read-notes.md`. |
| Timeline dự kiến | 10:29; cold open 14,7 s (cắt đuôi hơi thở sau từ cuối, `tailCut` phải áp ở M2); câu móc lại 0:30,3–0:42,7. |
| Điều khoản HMDA | **Đã trích** (consumerfinance.gov): "Information created by the CFPB is in the public domain and you may reproduce, publish, or otherwise use it without the Bureau’s permission. Please consider appropriate citation to the Bureau as the source." (`data/hmda-sources.json`) |
| Gói duyệt mới | `review-m1b/`: `summary.md`, `animatic-0000-0080.mp4` (giọng + S2), `break-even-methods.md`, `table-read-full.m4a`, `sb-01…04.png` |

## Mục mở

1. **Hợp đồng với phiên kiểm.** S01, S03–S06, V04, V09 gắn với bài D (`contract.json`); T1 xung đột G-006 (`checks-notes.md`).
2. **FRED.** Video hiển thị số kèm ghi nguồn; không công bố lại file; mô tả video trỏ link nguồn gốc.
3. **M2:** áp `tailCut` của cold open vào stem giọng; tiếng dữ liệu S2 theo `preprod/cue-sheet.md`; mức cuối chờ tai chủ dự án.

## Thư mục

- `data/`: dữ liệu và script tải lại (`python3 episodes/ep001/data/fetch.py`, kiểm SHA: `--verify`; HMDA: `python3 episodes/ep001/data/hmda.py --years 2025,...,2018`).
- Dựng lại M1: `python3 build.py && python3 contract_build.py && python3 preprod/plan.py && python3 preprod/storyboard.py && python3 preprod/edit.py && python3 preprod/animatic.py` (trong `episodes/ep001`; đọc thử: `EP_ROOT=$PWD EL_MAX_TAKES=1 EL_MAX_FALLBACK=0 python3 ../../toolkit/voice/d_el_voice.py`).
- `m0-sample/`: mẫu 10 giây (gốc thử riêng, cùng cấu trúc với gốc tập).
