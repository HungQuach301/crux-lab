# S09 trên hình: chữ cơ sở "dollars of the day" cạnh số $ (luồng P, C5) — chờ chủ dự án duyệt

Trước (`524ac85`) / sau (`dc4894d`), cùng thời điểm trong cảnh, 1080p: S01 t=22 s ($459), S07 t=5 s (chồng phí), S15 t=14 s (thanh Walt/Nora), S18 t=40 s (thước ba mốc; mẩu "amounts in dollars of the day" hiện cùng cỡ khoản vay, phần còn lại của dòng giả định hiện như cũ).
Lý do: luật S09 (CHẶN) đòi chữ cơ sở trong 300 px quanh mọi số $ đang hiện; trước sửa 70 chuỗi $ ở 19 cảnh không đạt, sau sửa 0 (kiểm đối tượng mỗi 0,2 s). Mọi ghi chú dùng một hàm (`basisNote`, cỡ note 40 px) nên đổi hay bỏ chỉ cần sửa một chỗ rồi render lại các cảnh đó.
Có ở 19 cảnh: S01 S02 S04 S06 S07 S08 S09 S10 S11 S12 S13 S14 S15 S16 S17 S18 S19 S20 (ghi chú riêng, hậu tố nhãn, hoặc thêm vào dòng nguồn); S03 và S05 không có số $.
