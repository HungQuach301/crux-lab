# Lượt chạy K2 trên mẫu m0 của Tập 1

| | |
|---|---|
| Bộ luật | `checks/` nhánh `checks-v2` (khoá K2, xem `checks/LOCK`) |
| Gốc | `episodes/ep001/m0-sample` của nhánh `ep001` @ `10b5438` (bản sao) |
| Hợp đồng tập | `episodes/ep001/contract.json` của cùng commit (`--contract`) |
| Baseline cho REG | báo cáo của **bên dựng** trên cùng mẫu (`m0-sample/out/checks/report.json`, LOCK `b97bfc6b…`, master `82ba6767…`). Không phải báo cáo do phiên kiểm giữ; dùng ở đây chỉ để cho thấy REG so những luật nào |
| Trang dựng | không chạy lại: trang nằm trong `toolkit/`, phiên K2 không dùng code đó. Luật khung hình đọc `out/checks/page.json` bên dựng đã sinh bằng bộ lấy mẫu khoá `b97bfc6b` |

**Kết quả: 26 PASS · 15 FAIL · 37 MISSING · 0 ERROR** (78 luật). Bên dựng (khoá `b97bfc6b`, có master): 41 · 29 · 5 · 0 (75 luật).

## Luật đổi kết quả, và vì sao

| Nhóm | Luật | Trước (bên dựng, `b97bfc6b`) → K2 | Vì sao |
|---|---|---|---|
| Master không được commit (`out/video.mp4`, 25 MB) | F01–F08, F10, A01–A06, A09, A14, A15, S11, S14, R03, R06, V05, V10, C13, T3 | PASS/FAIL → MISSING | Luật đo trên master. Định nghĩa không đổi (cùng fingerprint): không phải do K2 |
| Hợp đồng tập thiếu trường | S01, S05 (`model.kind`), S03 (`data.sources`), S04 (`data.crosscheck`), S06 (`coverage`) | S01, S03–S05: MISSING → MISSING (nay nêu tên trường, không còn đòi `annual.csv` của bài D); S06: FAIL → MISSING | Định nghĩa đổi (K2): đọc từ hợp đồng tập |
| Gốc mẫu dùng token riêng | V04, V09 | FAIL → MISSING | `m0-sample/design/tokens.json` không có token `cmedian` mà hợp đồng tập khai (token có ở `episodes/ep001/design/tokens.json`). Ở gốc tập sẽ không còn lỗi này. Trước đây hai luật trượt vì không thấy nhân vật `1966`/`mirror` của bài D |
| T1 | T1 | FAIL → MISSING | Hợp đồng tập chưa khai `sonification.bandsHz` |
| Mới | L1 | — → **FAIL** | lời/tiếng dữ liệu ở 1–4 kHz: phân vị 10 = −17,9 dB (cần ≥ 20). Khớp phán đoán của chủ dự án về m0 +10 dB: "vẫn bị tiếng dữ liệu lấn" |
| Mới | F11, S16 | — → MISSING | Hợp đồng tập chưa có `artefacts.M3`; nhân vật chưa có `words` |

Mọi luật có định nghĩa không đổi và còn đủ artefact cho **cùng kết quả** với báo cáo của bên dựng.

## REG

- So được: 66 luật (cùng fingerprint). Không so: S01, S03, S04, S05, S06, V04, V09, T1 (K2 đổi định nghĩa); F11, S16, L1 mới.
- 14 "hồi quy" (F01–F06, F08, A01, A02, A04–A06, A14, C13: PASS → MISSING) đều do thiếu master trong cây đã commit, không do luật. Với master `82ba6767…` các luật này chạy như cũ.
