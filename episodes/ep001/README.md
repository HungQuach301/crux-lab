# Tập 1 — "Ở mức chênh lãi suất nào thì tái cấp vốn hoàn lại được chi phí đóng hồ sơ?"

Đề tài 7, dòng 1 (vay và nợ, quyết định về nhà). Phiên D1, nhánh `ep001`.

## Trạng thái: M1 XONG, dừng chờ chủ dự án duyệt (không làm M2)

| Bước | Trạng thái |
|---|---|
| A-M0a, M0b | xong (lượt trước): toolkit theo cấu trúc crux-lab, mẫu 10 giây |
| A-M0c lãi suất | xong: FRED `MORTGAGE30US` + đối chiếu `OBMMIC30YF` (`data/sources.json`) |
| A-M0c chi phí đóng hồ sơ | **xong**: HMDA 2018–2025 toàn quốc, đọc theo luồng, **không lưu file thô**. `data/hmda.py` (tái tạo), `data/hmda-sources.json` (URL, SHA-256 của từng luồng, byte, ngày tải, số dòng, định nghĩa trường trích nguyên văn), `data/normalized/hmda_refi_costs.csv` (trung vị và P25–P75, theo năm × mục đích × quy mô khoản vay, đô la và % số tiền vay). **Điều khoản HMDA: chưa trích được câu nào**, xem mục mở dưới đây. |
| M1-1 mô hình, claims, test | `model/refi.py`, `model/test_refi.py` (8 test đạt), `build.py` → `out/model.json`, `out/claims.json` (62 claim) |
| M1-2 kịch bản | `script/script.tpl.md` (mẫu, số chỉ lấy từ claim) → `script/script.md`, `out/script-draft.json`; 83 câu, 1.334 từ, không cảnh nào > 2 số mới, CV độ dài câu 0,37 |
| M1-3 đọc thử | 84 take Eric `eleven_v3`, **4.292 ký tự**; `review-m1/table-read-full.m4a` (10:09, khoảng lặng ≤ 0,75 s); `script/table-read-notes.md` |
| M1-4 storyboard, shot list, cue sheet, tension map | `preprod/` (storyboard 14 khung, 84 shot, cue sheet có kế hoạch âm thanh theo dữ liệu cho cột, đường, điểm, bộ đếm; tension map dự kiến), `edit/cues.json`, `preprod/timeline-plan.json` (10:39) |
| M1-5 hợp đồng tập | `contract.json`, `design/tokens.json` |
| M1-6 gói duyệt | `review-m1/`: `summary.md`, `animatic-0000-0120.mp4` (2 phút: cold open + câu móc lại, hình là storyboard), `table-read-full.m4a`, `sb-01…05.png` |

## Mục mở

1. **Điều khoản HMDA (DX-H4).** Không trang nào đọc được từ môi trường này có câu điều khoản sử dụng dữ liệu HMDA; điều khoản web của CFPB nằm ở `www.consumerfinance.gov` (proxy 403). Cần trích trước khi phát hành.
2. **FRED.** Theo quyết định của chủ dự án: video hiển thị số kèm ghi nguồn; không công bố lại file; mô tả video chỉ dẫn link tới nguồn gốc.
3. **Hợp đồng với phiên kiểm.** S01, S03–S06, V04, V09 của bộ luật khoá gắn với mô hình và nhân vật bài D (xem `contract.json`).
4. **Tốc độ đọc ở M2.** v3 đọc 180–240 wpm ở câu ngắn; cold open 180 wpm, act 2 167 wpm (`script/table-read-notes.md`).
5. **Mức tiếng dữ liệu** chốt bằng tai chủ dự án ở M2 (`preprod/cue-sheet.md`).

## Thư mục

- `data/`: dữ liệu và script tải lại (`python3 episodes/ep001/data/fetch.py`, kiểm SHA: `--verify`; HMDA: `python3 episodes/ep001/data/hmda.py --years 2025,...,2018`).
- Dựng lại M1: `python3 build.py && python3 contract_build.py && python3 preprod/plan.py && python3 preprod/storyboard.py && python3 preprod/edit.py && python3 preprod/animatic.py` (trong `episodes/ep001`; đọc thử: `EP_ROOT=$PWD EL_MAX_TAKES=1 EL_MAX_FALLBACK=0 python3 ../../toolkit/voice/d_el_voice.py`).
- `m0-sample/`: mẫu 10 giây (gốc thử riêng, cùng cấu trúc với gốc tập).
