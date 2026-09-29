# C3 final — quyền tài sản

Mọi hình trong SF1–SF6, thẻ tiêu đề và `review-c3/contract.mp4` được **dựng bằng mã** trong `src/` (hình học three.js, texture vẽ bằng Canvas 2D, đồ thị Canvas 2D). Không dùng ảnh, mô hình 3D, texture, biểu tượng hay đồ hoạ bên thứ ba; không screenshot báo; không chép thiết kế của Vox/3Blue1Brown/WSJ (không xem lại, không tải). Tiền trong khung là giấy xanh chung chung có băng, **không** mô phỏng tiền giấy Mỹ. Lá thư "REFINANCE OFFER" là giấy dựng lại, không mang tên hay logo tổ chức nào.

| Tài sản | Loại | Nguồn | Giấy phép (trích nguyên câu) | Phạm vi | Ghi công |
|---|---|---|---|---|---|
| three.js 0.186.1 | Thư viện JS (render) | npm `three` (https://github.com/mrdoob/three.js), file `LICENSE` của gói; **không** vendor trong repo (`npm i three@0.186.1` vào thư mục tạm) | MIT: "Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software…" ("Copyright © 2010-2026 three.js authors") | YT, DL (nếu vendor phải kèm LICENSE) | Không bắt buộc trên hình |
| Inter 400/600/700 | Font | `toolkit/render/fonts/` (gói @fontsource/inter; `RIGHTS.md` F-INTER) | SIL OFL 1.1: "Permission is hereby granted, free of charge, to any person obtaining a copy of the Font Software, to use, study, copy, merge, embed, modify, redistribute, and sell modified and unmodified copies of the Font Software, subject to the following conditions: 1) Neither the Font Software nor any of its individual components, in Original or Modified Versions, may be sold by itself." | YT, DL | — |
| Chromium (Playwright build 1194) + SwiftShader | Công cụ render | `/opt/pw-browsers` | Công cụ, không nằm trong sản phẩm | — | — |
| PyAV 18.1.0 / libx264 | Công cụ mã hoá | pip `av` | Công cụ, không nằm trong sản phẩm (libx264 GPL: chỉ dùng để mã hoá, không phân phối binary) | — | — |
| Đường lãi tuần (SF1) | Dữ liệu | Freddie Mac PMMS qua FRED `MORTGAGE30US`, đọc cục bộ từ `data/normalized/mortgage30_weekly.csv` (tải bằng `data/fetch.py`, SHA-256 ở `data/sources.json`) | Theo `RIGHTS.md` D-FRED-1 và E1-A2: **không commit** giá trị tuần (`src/data.js` nằm trong `.gitignore`); trên hình ghi nguồn "Freddie Mac weekly rate survey, via FRED" | YT: hiển thị kèm dòng nguồn | "Freddie Mac … via FRED" |
| Phí vay lại (SF2–SF6) | Dữ liệu | CFPB HMDA 2025 qua `numbers.md` / `out/claims.json` | Theo `RIGHTS.md` D-HMDA (dữ liệu liên bang) | YT | "median 2025 refinance bill (HMDA)" |
| Mọi số khác | Mô hình | `model/refi.py` → `out/model.json` / `out/claims.json` | Tác phẩm của dự án | YT | nhân vật ghi "illustrative" |

Không có tài sản nào chờ quyền trong thư mục này.
