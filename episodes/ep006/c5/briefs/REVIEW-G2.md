## Tập 6 · REVIEWER G2 (chỉ đọc) — repo /home/user/crux-lab, nhánh ep006
Vai: REVIEWER độc lập của kênh CRUX (`CHARTER.md`, `playbook/quality-framework.md` §7, `playbook/prompts/P3.md` việc 4). Đọc gói `episodes/ep006/gates/G2.md` và kiểm từng khẳng định bằng nguồn trong repo; không tin gói.
Nguồn: `episodes/ep006/out/checks/run-c5c/report.{md,json}` (và `run-c5`, `run-c5b` để so), `out/explanations.json`, `out/factory/qc.md`, `out/package/{description.md,thumb-*.json}`, `out/claims.json`, `contract.json`, `c4/ROOT-SUMMARY-P3c.md`, `c4/root-c5b`, `c4/root-c5b-ctl`, `c4/root-c5c` (KEY/scores), `c5/sync/*.json`, `episode.yaml shorts`, `out/timeline.json`, `out/adbreaks.json`, `gates/G1-answer.md`, `gates/C3-answer.md`, `gates/C4-answer.md`, `PLAN.md`, git log ep006.
Kiểm bắt buộc:
1. Mọi số trong G2.md khớp nguồn (checks, cổng gốc, độ dài, LUFS/dBTP, đồng bộ, Shorts, chi/giờ). Sai → ghi "cũ → mới".
2. **V11.plateOverGraphics**: đọc giá trị và ví dụ (`run-c5c/page.json.gz` → rules.V11.plateOverGraphics/plateOverExamples; python3 gzip) — có chỗ nào là chữ đè hình thật bị tấm nền che không? Nêu trong mục riêng (quality-framework §7 mục 7).
3. Ngoại lệ V11 S04: lập luận khoá nghĩa có đứng không (số đo root-c5b, đối chứng, root-c5c)?
4. Mô tả: chương khớp timeline (≥ 3, đầu 0:00, mỗi chương ≥ 10 s), mọi số là claim, không khuyên, không "we" chỉ người xem, chính tả.
5. Thumbnail json: mọi số là claim, claim-risk (ILLUSTRATIVE, "US only · history, not a forecast", không số tiền/"total", không khuyên).
6. `advice_stated` = 0 ở mọi lượt đọc cổng gốc P3c (đọc từng câu trích `advice_inferred` — có câu nào thực ra do hình nêu không?).
7. Có điều gì gói G2 bỏ sót mà chủ dự án cần biết để chấm (CHẶN ẩn, hồi quy so run-c5b, cam kết gate trước chưa giữ — vd. C3/G1 "C5 ≥ 8:00 và có mid-roll hợp lệ")?
Trả về (Markdown, ≤ 60 dòng, tiếng Việt, câu ngắn): dòng đầu "Kết luận: ĐẠT | ĐẠT có sửa | KHÔNG ĐẠT"; các mục 1–7; cuối "## Sửa (cũ → mới)" liệt kê từng sửa cho G2.md. Không sửa tệp.
