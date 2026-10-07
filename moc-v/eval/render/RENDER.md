# Thời gian render đoạn thử 69,6 s (1080p30, 4 vCPU Xeon 2,8 GHz, CPU DÙNG CHUNG với việc khác → số nhiễu)

| Bản | Lần chạy | Luồng | Giây máy / giây phim | Ghi chú |
|---|---|---|---|---|
| C | v1 | 4 | 0,78 | |
| C | v1b | 3 | 1,04 | song song B |
| C | v2 | 2 | 1,02 | `C.mp4.render.json` |
| A | v1 | 4 | 1,01 | |
| A | v1b | 3 | 0,93–0,94 | |
| A | v2 | 2 | 1,08 | `A.mp4.render.json` |
| B nhà mã | v1 | 4 | 12,79 | SwiftShader WebGL |
| B nhà CC-BY | v1 | 4 | 10,45 | `B-cc.mp4.render.json` |
| B nhà mã | v2 | 4 | 8,68 | `B-code.mp4.render.json` |
Số v1/v1b lấy từ log lúc chạy (đã in trong phiên); file json chỉ giữ lần cuối mỗi bản. Trộn âm (`audio.py`): ≈ 16 s / bản.
