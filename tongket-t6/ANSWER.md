# Câu trả lời tổng kết Tập 6 (chủ dự án, 11/10/2026)

Chép nguyên văn từ lệnh mở phiên P1 Tập 7 (G1 lô Tập 7–8). Gói: `tongket-t6/REPORT.md` §5.

```
1 a·d·f·g: duyệt cả bốn; (d) và (f) dùng thử 3 tập rồi hiệu chuẩn lại.
2 deep: duyệt (14–17 phút, ước G1 ≥ 14:42, mid-roll 2–3, ba điều kiện không độn). Tập 7: deep nếu F-14 đạt đích trước G1 lô, không thì lab 11 phút. Tập 8: xét cùng cách ở G1 lô. EL: chủ dự án chưa kiểm — phiên tự đọc hạn mức còn lại qua API ElevenLabs (GET /v1/user/subscription, khoá qua proxy; chỉ ghi số ký tự còn/giới hạn và ngày làm mới, không ghi khoá) và nêu ở G1 lô; thiếu cho 2 tập deep thì đề xuất phương án.
3 Thumbnail API lai: KHÔNG ĐẠT (chủ dự án bác) — không dùng, không render đối chứng 2D; bộ nhận diện api-*.png không duyệt. Gói phát hành (tiêu đề, mô tả, thumbnail, tag) chủ dự án làm trên ChatGPT. Claude cung cấp đầu vào khi video hoàn tất (P4, trước G3): PACKAGING-BRIEF.md tiếng Anh dán thẳng vào ChatGPT gồm (a) quét tốc độ 7 ngày của đề tài (anchors.py trend), (b) 1–3 video neo + cụm từ chính + điểm khác biệt, (c) khuôn tiêu đề thắng + cụm từ tìm kiếm đặt đầu tiêu đề và 2 dòng đầu mô tả, (d) kiểu thumbnail thắng 90 ngày + vật thể trung tâm của chính video (đúng tên gọi trong lời), (e) claim được/bị cấm, chương + mốc giờ từ timeline, câu hỏi khán giả đã trả lời, (f) 3–4 khung đẹp nhất PNG làm tham chiếu. Sau đó chủ dự án dán tiêu đề, mô tả, ảnh thumbnail ChatGPT vào P4 → kiểm S21, claim-risk, từ ngữ vật thể khớp lời, chương khớp timeline, mức bám xu hướng/neo (rescore.py chỉ là bộ lọc thô) → trả câu sửa sẵn nếu lệch. Ghi vào packaging.md §7 + P3.md chặng P4; text.py/thumbs.py giữ làm công cụ phụ, không phải đường chính.
```

## Đã áp (nhánh `tongket-t6-answer`, phiên P1 Tập 7)
| Mục | Áp ở |
|---|---|
| 1a sửa D-011 (chạy tiếp sau `/compact` khi tệp lớn ở container) | `decisions/D-011.md` "Sửa đổi 11/10", `playbook/episode.md` §1, `prompts/P3.md` chặng P4, lessons T6-3 |
| 1d F-14 (dùng thử 3 tập) | `tongket-t6/F14-brief.md` (đầu bài phiên nhà máy `factory-f14`, chủ dự án mở song song; P1 không làm), `BACKLOG.md` F-14, lessons T6-6 |
| 1f phiếu L3 (dùng thử 3 tập) | `playbook/templates/L3.md` bỏ chữ "nháp", lessons T6-8 |
| 1g khoá Console chuẩn + trần chi `101` $35 · `lab` $45 · `deep` $60 | `playbook/episode.md` §2, §8, §11; `decisions/D-011.md`; lessons T6-9 |
| 2 `deep` | `CHARTER.md` §1, `playbook/episode.md` §8–§9 (bỏ "chờ"; Tập 7: `deep` chỉ khi F-14 đạt trước G1 lô, không thì `lab` 11 phút), `decisions/D-012.md` |
| 3 đường đóng gói: ChatGPT chính, brief (a)–(f) ở P4, P4 kiểm; API lai + đối chứng 2D + bộ nhận diện bác | `playbook/packaging.md` §7, `episode.md` §1b.6, §5, §5c, §11, `prompts/P3.md` (G2 câu 2, chặng P4 4a–4b), `templates/PACKAGING-BRIEF.md`, `templates/G1.md`, `toolkit/market/brief.py` (`--trend`, `--anchors`, `--g1-title`, `--frame`; bỏ màu trụ), `decisions/D-012.md`, lessons T6-11 |
| Hoàn lại (mục áp ở tổng kết mà bị bác) | §5 "thumbnail lai là đường chính", bộ nhận diện §7.4, đối chứng 2D, `--pillar` trong brief. `toolkit/package/{text,thumbs}.py` giữ làm công cụ phụ (câu 3). |
| CHARTER §5 dòng G2 "tiêu đề/thumbnail" | **chưa sửa** — câu trả lời chỉ duyệt sửa CHARTER §1. Nêu ở G1 lô. |
