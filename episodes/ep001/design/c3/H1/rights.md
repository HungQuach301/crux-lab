# H1 — quyền tài sản

Mọi hình trong F1–F3 được **dựng bằng mã** trong `src/` (hình học, texture vẽ bằng Canvas 2D, ánh sáng). Không dùng ảnh, mô hình 3D, texture hay đồ hoạ bên thứ ba. Không có mô phỏng thiết kế tiền giấy Mỹ (cọc tiền là giấy xanh chung chung ghi "SAVED $221").

| Tài sản | Loại | Nguồn | Giấy phép (trích nguyên câu) | Phạm vi | Ghi công |
|---|---|---|---|---|---|
| three.js 0.186.1 | Thư viện JS (render) | npm `three` (https://github.com/mrdoob/three.js), file `LICENSE` của gói | MIT: "Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software…" ("Copyright © 2010-2026 three.js authors") | YT, DL (không vendor trong repo; nếu vendor phải kèm LICENSE) | Không bắt buộc trên hình |
| Inter 400/600/700 | Font | `toolkit/render/fonts/` (gói @fontsource/inter; RIGHTS.md F-INTER) | SIL OFL 1.1 (trích từ văn bản OFL-1.1 có trên máy, `/root/.rustup/.../licenses/OFL-1.1.txt`): "Permission is hereby granted, free of charge, to any person obtaining a copy of the Font Software, to use, study, copy, merge, embed, modify, redistribute, and sell modified and unmodified copies of the Font Software, subject to the following conditions: 1) Neither the Font Software nor any of its individual components, in Original or Modified Versions, may be sold by itself." | YT, DL | — |
| Chromium (Playwright build 1194) + SwiftShader | Công cụ render | `/opt/pw-browsers` | Công cụ, không nằm trong sản phẩm | — | — |
| PyAV 18.1.0 / libx264 | Công cụ mã hoá | pip `av` | Công cụ, không nằm trong sản phẩm (lưu ý: libx264 GPL — chỉ dùng để mã hoá, không phân phối binary) | — | — |
| Số liệu trên hình | Dữ liệu | `numbers.md` / `out/claims.json` (FRED MORTGAGE30US; CFPB HMDA 2025; mô hình `model/refi.py`) | Theo RIGHTS.md D-FRED-1, D-HMDA | YT: hiển thị kèm dòng nguồn (đã có trên mỗi khung) | "Freddie Mac PMMS via FRED", "CFPB HMDA 2025" |

Tham chiếu Vox/3Blue1Brown/WSJ: không xem lại, không tải, không chép thiết kế cho hướng này.
