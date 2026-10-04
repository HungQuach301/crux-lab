# C3 — Kiểm mô phỏng mù màu (P-ep002, đo bằng `checks/py/r_visual.py` cvd_report: Machado 2009 severity 1, ΔE2000; xám = tương phản WCAG)

Ngưỡng (lessons D3 / luật V09): mọi cặp vai phải phân biệt ΔE2000 ≥ 20 dưới protan **và** deutan; xám ≥ 1,5:1. Thêm: vật dữ liệu so với nền `bg` ≥ 3:1.
Vai: `warn` = "lãi vượt 9%", costlier = "đắt hơn tổng cộng", cushion = "đệm/tiết kiệm", `accent` = T-bill.

| Bộ màu | warn/cushion | warn/costlier | cushion/costlier | accent/cushion | accent/costlier | Đạt? |
|---|---|---|---|---|---|---|
| **Token Tập 1** (positive `#3FBF7F`, negative `#E5484D`) | 11.8 · xám 1.27 | 18.1 | 11.5 | 44.9 | 45.4 | **không** (3 cặp) |
| **Đề xuất E2** (cushion `#269783`, costlier `#C72323`; warn, accent giữ) | ≥ 25.6 | ≥ 25.6 | ≥ 25.6 | ≥ 25.6 | ≥ 25.6 | **đạt** mọi cặp; xám ≥ 1,5; nền: costlier 3.3:1, cushion 5.3:1 |
| Magenta (thử) | 31.1 | 54.6 | 32.4 | 35.3 | **7.9** | không |

E2 là **bí danh của tập** (không đổi token kênh): vẫn đỏ = thua, xanh = tiết kiệm, chỉ đậm hơn và ngả mòng két. Đổi màu nhận diện là gu → chủ dự án quyết ở gói C3. Hình dạng/vị trí vẫn là kênh thứ hai (D3).
