# Mốc B — số đo tốc độ

## Checks đủ bộ (đo 05/10/2026, 14:58–15:54 UTC, máy 4 lõi, 15 GB)
- **Bản đo:** bản sao khoá `git archive` của `moc-b`, LOCK `a20c6878…`. Video là bản giao YouTube của Tập 3 (1080p30, 572 s, SHA `1274f9f6…`), cùng thời lượng và khổ hình với bản gốc. Không có stem (`out/audio/stems` không commit), nên 13 luật MISSING. Script: `checks-time.sh` (giữ trong scratchpad; cách làm giống `episodes/ep003/design/c5/checks.sh`).

| Phần | Thời gian | Tỉ lệ |
|---|---|---|
| Bộ lấy mẫu trang (`checks/page/sampler.js`, mẫu đối tượng mỗi 3 khung, điểm ảnh mỗi 6 khung, một tiến trình) | **3.001 s (50,0 phút)** | **88 %** |
| Luật Python (`checks/py/run.py`, gồm ASR whisper small.en) | 391 s (6,5 phút) | 12 % |
| **Cộng** | **3.392 s (56,5 phút)** | |

- **Đối chiếu Tập 3:** 60–75 phút mỗi lần, có stem. Phần chênh nằm ở các luật cần stem, vốn MISSING ở lần đo này.
- **Điểm nghẽn: bộ lấy mẫu trang**, không phải ASR. Đề xuất A3 trong `checks-appeal.md` sắp lại theo số đo:
  1. song song theo cảnh (`--scenes`, 3–4 tiến trình) → ước 50 → 15–18 phút;
  2. cache kết quả trang theo băm cảnh → lần chạy thứ hai chỉ lấy mẫu cảnh đổi;
  3. một lần ASR cho hai họ luật.
  **Sau:** chưa đo — cần phiên K viết và khoá lại (bên dựng không sửa `checks/`).

## Render 1080p
- **Trước:** Tập 3 ≈ 25–30 phút mỗi lần render 1080p (ledger Tập 3). Khung truyền ra dạng RGBA thô qua base64 (`episodes/ep003/design/c3/render.js` → `APP.frame`), một tiến trình.
- **Sau:** **chưa đo.** Tối ưu (khung trung gian JPEG q 0,95, render song song chỉ đoạn đổi) chuyển sang phiên nhà máy (`moc-b/PLAN-FACTORY.md` §2.1, §2.9).
