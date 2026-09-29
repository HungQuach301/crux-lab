# H2 — Sổ quyền tài sản của ba khung mẫu

Mọi thứ trên hình của F1–F3 được **vẽ bằng mã** (HTML/CSS/SVG trong `src/`, chụp bằng Chromium headless). Không có ảnh, hình vẽ, biểu tượng hay âm thanh của bên thứ ba. Không có screenshot bài báo, không có "bài báo giả".

| Tài sản | Dùng ở | Nguồn | Giấy phép (trích nguyên câu + link) | Phạm vi |
|---|---|---|---|---|
| Font Inter 400/600/700 | F1–F3 | `toolkit/render/fonts/` (@fontsource/inter) | SIL Open Font License 1.1 — **chưa trích nguyên văn** (như RIGHTS.md F-INTER; trích trước C5) | YT, DL |
| Dữ liệu lãi tuần 30 năm (đường lãi F1) | F1 | Freddie Mac PMMS qua FRED, `MORTGAGE30US`; đọc lúc render từ `data/normalized/mortgage30_weekly.csv` (tải lại bằng `fetch.py --verify`), **không lưu trong thư mục này** | FRED: "Copyrighted: Citation required … you may use these data series with proper attribution of the source and acknowledgment that you obtained the data from FRED" — https://fred.stlouisfed.org/legal/ (RIGHTS.md D-FRED-1) | YT: hiển thị biểu đồ + "Source: Freddie Mac via FRED" (in ở chân tờ). DL: video có biểu đồ do ta vẽ; không có file dữ liệu. |
| Phí đóng hồ sơ ($5,124, $3,667, $5,514) | F2, F3 | CFPB HMDA 2025 (`out/claims.json`) | "Information created by the CFPB is in the public domain and you may reproduce, publish, or otherwise use it without the Bureau's permission." — https://www.consumerfinance.gov/privacy/website-privacy-policy/ (RIGHTS.md D-HMDA) | YT, DL |
| Bố cục "Closing Disclosure · Loan Costs" (dựng lại, không phải ảnh của biểu mẫu) | F2 | Theo mẫu công khai của CFPB: https://www.consumerfinance.gov/compliance/compliance-resources/mortgage-resources/tila-respa-integrated-disclosures/forms-samples/ | Như dòng trên (CFPB public domain; 17 U.S.C. §105, đọc qua tìm kiếm — xem `rights-options.md`) | YT, DL. Không logo CFPB. Chú thích trên tờ: "Layout after the CFPB model Closing Disclosure… illustrative." |
| Câu trích "A Closing Disclosure is a five-page form that provides final details about the mortgage loan you have selected." | F2 (thẻ trích dẫn dựng lại) | https://www.consumerfinance.gov/ask-cfpb/what-is-a-closing-disclosure-en-1983/ (curl trực tiếp 29/09/2026) | Như dòng CFPB ở trên | YT, DL, ghi nguồn "CFPB, consumerfinance.gov" |
| Số nhân vật (Nora, Walt, Anjali) | F1–F3 | `out/claims.json` | Do dự án tính | YT, DL; dấu ILLUSTRATIVE |
| Màu | F1–F3 | `genre-spec/channel/visual-tokens.json` | Của dự án | YT, DL |
