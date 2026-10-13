# Trước/sau Tập 4–7 — khoá K4.4 (luật đổi hoặc mới)

Chạy `checks-runs/K44/ba.py` trên gốc tạm (symlink), page.json = bản lưu mới nhất của tập (Tập 7 chưa có page: S23 chỉ phần lời, F15 không có footage). Không liệt kê luật trùng kết quả. A12/A13/R01 trên stem tái dựng: `a33/`.

| Tập | Luật | main c735828 | K4.4 | chỉ số trượt (K4.4) |
|---|---|---|---|---|
| ep004 | A13 | ERROR | MISSING | artifact missing: out/voice/takes.json: take S01 without raw/final |
| ep004 | SH07 | absent | PASS | episode 4: before Episode 8 the count (D-006 2–3) is reported only |
| ep004 | F13 | absent | PASS | — |
| ep004 | F15 | absent | PASS | no declared external footage |
| ep004 | S23 | absent | PASS | — |
| ep004 | R09 | absent | FAIL | {"act turns with a hard cut": 5} |
| ep005 | SH07 | absent | PASS | episode 5: before Episode 8 the count (D-006 2–3) is reported only |
| ep005 | F13 | absent | PASS | — |
| ep005 | F15 | absent | PASS | no declared external footage |
| ep005 | S23 | absent | FAIL | {"advice-like terms not allowed": 2} |
| ep005 | R09 | absent | FAIL | {"act turns with a hard cut": 4} |
| ep006 | SH07 | absent | PASS | episode 6: before Episode 8 the count (D-006 2–3) is reported only |
| ep006 | F13 | absent | PASS | — |
| ep006 | F15 | absent | PASS | no declared external footage |
| ep006 | S23 | absent | FAIL | {"advice-like terms not allowed": 4} |
| ep006 | R09 | absent | FAIL | {"act turns with a hard cut": 6} |
| ep007 | SH07 | absent | PASS | episode 7: before Episode 8 the count (D-006 2–3) is reported only |
| ep007 | F13 | absent | PASS | — |
| ep007 | F15 | absent | PASS | no declared external footage |
| ep007 | S23 | absent | FAIL | {"advice-like terms not allowed": 8} |
| ep007 | R09 | absent | FAIL | {"act turns with a hard cut": 5, "most used view share (%)": 24.090759} |

**Tập 8 (cây thật `origin/ep008` @ 1a39f896, chỉ đọc, chưa dựng):** hợp đồng `package.thumbnails: 0`, 1 Short → SH07 PASS, SH06 PASS, P01 PASS (ghi chú không thumbnail); F11/F13/F15/S23/R09 MISSING (chưa có `out/`).
