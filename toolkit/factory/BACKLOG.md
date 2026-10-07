# Hàng chờ nhà máy (backlog) — không chặn mốc đang chạy

| # | Việc | Nguồn | Trạng thái |
|---|---|---|---|
| F-1 | Chuyển chế độ bằng máy quay di chuyển thật thay cho hoà tan (vật thế giới không mờ; máy đi qua chúng) | D-010 §6 bổ sung 06/10 | chờ |
| F-2 | Kiểm tự động: mật độ hiệu ứng âm (sự kiện sfx/phút, sfx đè lời) và nhãn đè nhau (hộp chữ giao nhau / chữ bị đường cắt) trên nhật ký trang | D-010 §6 bổ sung 06/10 | chờ |
| F-3 | Nhạc Tập 5 theo bản đồ căng (biên độ nghe được; dâng ở phần phát lại, chốt ở "removed") | D-010 §6 bổ sung 06/10 | chờ |
| F-4 | Lint "chú thích nuốt mã" chạy trong build | Mốc V, lỗi thật tìm thấy 06/10 | **xong** 06/10: `world/lint_comments.py` là bước đầu của `world/build_seg.py` (build.py bước `world`) |
| F-5 | Ghép đoạn thế giới vào master của tập: hình (thay các cảnh đoạn chiếm, mã hoá lại một lần cho đồng nhất) + tiếng (sfx/âm dữ liệu/nhạc từ spine của đoạn vào stem của tập, loudnorm chung) | Mốc V bước áp vào nhà máy | **xong** 07/10: `world/splice.py` + bước `splice` của `build.py` (hình thay khung, mã hoá lại một lần) và ghép tiếng trong `mix` (music/sonify/sfx/room vào stem, lời không nhân đôi, loudnorm chung); `out/factory/splice.json`; `spec.py` chặn cảnh không liền/chồng. Test `toolkit/tests/test_world_splice.py` (5/5, master + đoạn giả). Còn kiểm trên đoạn thế giới thật đầu tiên của Tập 5 |
