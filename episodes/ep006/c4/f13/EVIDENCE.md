# F-13 — bằng chứng không đổi tập cũ (P3b, 09/10)

Sửa: `toolkit/factory/world/build_seg.py` bước `mux` bỏ `-shortest` (một dòng; commit 9479080 trên `ep006`, vào `main` ở P4).
Lỗi Tập 6 C4: AAC + `-shortest` cắt 2–4 khung cuối đoạn (a 1537 → 1535, b 2953 → 2950, c 1778 → 1774) → `splice` dừng.

Dựng lại **Tập 5 đoạn a-s01-s03 ở 1080p** bằng mã mới (`build_seg.py`, render 621 s, verify OK; `ep005-a-1080.build.json`), rồi ghép **cùng** hình + tiếng của lần dựng đó theo cách cũ (`-shortest`):

| Tệp | Khung | SHA-256 tệp | SHA-256 luồng hình (`-map 0:v -c copy`) | Dài hình / tiếng |
|---|---|---|---|---|
| Bản cũ Tập 5 (`episodes/ep005/out/factory/splice.json`) | 1740 (= f1 timeline) | `d54e88959b5b623e…` | — | — |
| Ghép cách cũ trên lần dựng lại | 1740 | **`d54e88959b5b623e…` (trùng bản cũ)** → render tất định | `3bad5d18bfea0e86…` | 58,000 / 57,984 s |
| **Mã mới (F-13)** | **1740 = timeline** | `efd4cc92cfbb4230…` | **`3bad5d18bfea0e86…` (trùng byte)** | 58,000 / **58,000 s** |

- framemd5 từng khung: 1740/1740 trùng.
- **Chỉ đuôi tiếng khác:** luồng AAC dài thêm **16 ms** (57,984 → 58,000 s = đúng `mix.wav`); Tập 5 không rơi khung vì AAC chỉ ngắn hơn hình 16 ms (< 1 khung), Tập 6 rơi vì độ dài cảnh lệch pha khung AAC khác.
- Master tập sau `splice` vẫn lấy tiếng từ stem của tập (README nhà máy: "lời vẫn là track lời của tập"), không từ luồng AAC của đoạn → master Tập 5 không đổi.
