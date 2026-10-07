# C4 · vòng 2 (người dựng) · B03 · B08 · B14 · B17 · B18 · 2026-10-07

Nguồn trượt: `gates/C4-root.md` vòng 1 (7/12). Đọc: câu trả lời `c4/root-r1/*.json`, `c4/root-r1x/*.json` (theo `key.json`), `review-c4/spans.json` (muted read; B18 đã sửa trước vòng 2, vạch đứng thay thẻ "your plan").
Luật: sửa bằng hình trước, nhãn sau cùng (≤ 8 từ, ≥ 48 px); khoá nghĩa (không thêm câu khuyên, nghĩa không thấp hơn). Không đổi lời, `checks/`, `toolkit/`.
Chỉ sửa `world/c4/*` + `world/c4kit.py`. Không commit.

## 1. Chẩn đoán và sửa từng nhịp

### B03 / S03 (đoạn A)
| Vòng 1 | Vì sao |
|---|---|
| "vạch 80 % dịch / nhân đôi" | Vạch 75 % **trượt ra từ chính vạch 80 %** (cùng chiều dài, cùng x). Ở fov 12 hai vạch cách nhau 23 px (1080p), nên đọc như một vạch dày lên. |
| khung 4 = giữa cú bay | Đồ thị S03.3 chỉ đứng yên **0,5 s** (nhãn B+2 ở "bar" 40,99 → bay đi 41,50). Khung 4 (41,719) rơi giữa cú bay, nên nhãn `Fannie Mae: wait ≥ 2 years · loan ≤ 75%` không có trong dải. |
| thiếu ba bước | Không có gì trên hình nói "request · appraisal · wait". |

Đã sửa (hình trước):
1. **Vạch 75 % thành một vạch riêng:** vẽ ra từ trái sang phải ở đúng mức 75 % (không trượt từ 80 %). Vạch đặt lệch phải, từ mép chồng vay ra ngoài (x 17,6–21,2), không trùng đoạn với vạch 80 %. Nhãn `75%` đặt dưới đầu phải vạch.
2. **Phần khoản vay còn ở trên vạch 75 %** đổi màu warn ở "seventy-five", theo vai màu "still above the bar" trong beats.md.
3. **Khung chặt hơn:** `cDef75` fov 12 → 8, x 16,8 → 17,0. Khoảng 80 %↔75 % thành 35 px (1080p). Nhãn "80% on paper" dời lên 24 px ở S03.3.
4. **Đồ thị S03.3 đứng yên lâu hơn:** cú bay `m_c7` sát "three" (late, 1,1 → 0,9 s): 41,953–42,853. Khung 4 (41,719) giờ là đồ thị đứng yên, có vạch 75 %, nhãn B+2 và nhãn luật.
5. **Nhãn (cách cuối, 6 từ, 56 px):** `loan owner's rule` → `loan owner's rule: request · appraisal · wait`. Chữ lấy từ beats.md B03 ("request · appraisal · minimum wait") và S09.3. Không có số mới, không mệnh lệnh.

### B08 / S08 (đoạn B)
| Vòng 1 | Vì sao |
|---|---|
| khuyên "not a reason to rule out buying" (2/2) | Khung 5–6 (S08.3): **căn nhà** đứng cạnh đường trả nợ đi hết 360 kỳ về 0, nên đọc thành "PMI là một chặng ngắn của việc sở hữu nhà, cứ mua". Người đọc: "payments 99 and 114 sit early … well before the house is paid off". |

Đã sửa: ở S08.3 **bỏ căn nhà**. Thay bằng **chồng giá trị nhà** (chồng tiền xám nhạt, 400k) đứng ngoài khung gạch "based on the schedule only", với tên `home value` (thay "the house"). Hình nói đúng muted read: giá trị nhà nằm ngoài biểu đồ. Nhà chỉ trở lại khi máy bay sang thế giới ở S09.1, rồi đặt lên chồng. "value" (S09.1) giờ là chồng bật lên (60 % trong 0,6 s), vùng đo sync dời lên đỉnh chồng.

### B14 / S14 (đoạn C)
| Vòng 1 | Vì sao |
|---|---|
| đọc thước đo thành trả hết / hoà vốn | Ở khung phóng chỉ có "on paper" 44 px màu muted. Không có gì nói chiều cao cột = số tháng tới 80 % trên giấy. |
| so sánh với lịch 90 kỳ không rõ | Mốc 90 kỳ là một khối nhỏ 0,5 đơn vị, nhãn nằm ngang hàng với nó, không có mốc lịch của các tháng khác để so. |
| khung 4–6 sang khu nhiều nhà | `m_hood` (cZoom → wHood) ở "national". Nửa dải là nhà lên xuống. |

Đã sửa:
1. **Khung giữ ở cột cao nhất tới hết S14.** Bỏ cảnh khu nhiều nhà (wHood). "national average, not one home" thành tên trên khung đồ thị (52 px, ở "single", chữ không đổi). Cú chuyển sang ba người mua là `mode` cZoom → wBuyers (fly qua `fBuy`, whoosh_mode). Lý do: lời "why did the same rule give such different answers?" → câu trả lời là ba người mua. Đây là quy tắc D-010 §2.6: thế giới 3D khó đọc thì về chế độ đồ thị.
2. **Thước chiều cao** (ngoặc từ chân tới đỉnh cột cao nhất) + `height = months to 80% on paper` ở "months". Chữ này dùng lại đúng nhãn S10.5, không phải nhãn mới.
3. **Mốc lịch so được:** sống lịch (mốc lịch của từng tháng, như S11) hiện lại ở "schedule". Mốc 90 kỳ sáng lên, có gạch nối tới nhãn `schedule at that rate: 90 payments`. Cột cao nhất (và cụm 2005) nhô lên trên sống lịch, còn các tháng khác nằm dưới.
4. `cZoom` fov 16 → 20, hạ khung: chân cột nằm trên dải chữ cố định.

### B17 / S17 (đoạn D)
| Vòng 1 | Vì sao |
|---|---|
| chỉ số "dips and recovers" | Chỉ số vẽ tới tháng 118 (tháng 112 + 6). Cuối đường (1,015) **cao hơn** mức mua, trong khi ở tháng 112 nó là 0,967 (claim −3,3 %). Tỉ lệ 2,0 làm khoảng −3,3 % chỉ còn ≈ 10 px. |
| khuyên "buy only if I can hold a decade" | Khung 6 (S17.4): nhà + **người đứng cạnh** ngay sau đồ thị mười năm, đọc thành "giữ nhà mười năm". |

Đã sửa:
1. Chỉ số của Victor **dừng ở tháng 112**. Tỉ lệ chỉ số 2,0 → 4,0 (gốc −0,3 → −0,2), áp cho cả ba làn, nhãn số không đổi.
2. **Mức chỉ số lúc mua:** đường gạch accent ngang làn, chấm ở cuối chỉ số (tháng 112) và đoạn accent từ mức mua xuống chấm. Hiện ở "below", cùng lúc nhãn `index still 3.3% below purchase` (giữ nguyên).
3. **Bỏ người cạnh nhà Victor.** Thêm `?` trên khiên ở "lender": dữ liệu không trả lời. "not in this data" giữ nguyên ở "show".

### B18 / S18 (đoạn D)
| Vòng 1 | Vì sao |
|---|---|
| không thấy "your plan" | Vạch đứng (dày 0,07) chỉ hiện ở "two" (S18.4), nên chỉ có trong khung 4. Không có tên, người đọc gọi nó là "a marker at about 2 years". |

Đã sửa: vạch đứng ở 24 tháng **hiện từ "plan"** (S18.2, sớm hơn 14 s), nên có trong khung 2–4 của dải. Vạch dày ×2,2, cao 2,3, sáng lên ở "plan". Tên ngắn `a plan` (2 từ, 56 px, đúng chữ lời "So a plan can be measured…") đặt dưới chân vạch. Vạch đứng giữa dải lịch (phải) và đầu bó trên giấy (trái), vạch 75 % vẫn thấy. Nhãn mô tả "≈ 2 years matched…" 46 → 48 px (luật ≥ 48 px). Để giữ máy đứng yên ở "plan" (quy tắc 2), cú lùi `m_bench` kết thúc trước "plan" thay vì trước "benchmarks".

## 2. Lệnh thêm của điều phối: take mới S04 (seed 1007), S15 (seed 1006)
- `episode.yaml` voice_overrides: S04 → `68d5dbe4da841180` (28,19 s, cũ 25,52), S15 → `b0d912d29478ac29` (19,57 s, cũ 20,32). Cả hai đã có trong `voice-takes/`, chi 0 ký tự EL.
- `review-g1/voice-scenes.json` (ngoài phạm vi sửa) vẫn ghi take cũ. **`c4kit.py`** thêm `_override_takes()`: chọn take theo voice_overrides đúng như nhà máy (`{seed}` → take trong voice-takes/ cùng seed + cùng chữ/giọng/model/thiết lập; `{take}` → đúng file). Hàm thay `wlib.voice_scenes` cho các đoạn C4. Spine lấy mốc từ take mới (không gõ tay). `Seg` vẫn kiểm từng từ khớp timeline nhà máy (±2 ms). Cảnh không có override vẫn như trước.
- Timeline: S04 dài thêm 2,63 s, S15 ngắn đi 0,80 s → tổng 464,467 s. `bed.wav` sinh lại theo luật trong episode.yaml (`world/music/bed.py`, MR1 183,7–184,9). Nhạc nền đổi nên `music_db` của cả 4 đoạn đổi, và cả 4 đoạn phải render lại.
- **Span:** cùng định nghĩa (đầu câu đầu → cuối câu cuối + 0,5 s), tính lại trên timeline mới. Mọi nhịp từ S06 trở đi dời +2,63 s (từ S16 trở đi +1,83 s). `spans.json` ghi `span_r1` (giờ cũ) + `note_r2`, muted read không đổi. Dải của 7 nhịp không sửa giữ PNG vòng 1: hình cảnh không đổi, chỉ giờ master dời.

## 3. Trước / sau (dải tắt tiếng; vòng 1 ở `review-c4/strips/<id>.r1.png`)
- **B03** (giờ không đổi): khung 3 có nhãn luật 3 bước. Khung 4 = đồ thị đứng yên: vạch 80 % mờ (trái + chồng vay), vạch 75 % riêng lệch phải, đỉnh chồng vay warn, nhãn B+2 `Fannie Mae: wait ≥ 2 years · loan ≤ 75%` + nhãn luật. Vòng 1 khung 4 là giữa cú bay.
- **B08:** khung 5–6 có chồng `home value` ngoài khung gạch, không còn căn nhà.
- **B14:** cả 6 khung ở cột cao nhất. Khung 2–6 có thước `height = months to 80% on paper`. Khung 3–6 có sống lịch + mốc 90 kỳ có gạch nối. Khung 4–6 có `national average, not one home`. Vòng 1 khung 4–6 là khu nhà.
- **B17:** khung 3–5 có chỉ số dừng ở tháng 112, chấm dưới đường gạch "mức mua". Khung 6 là nhà + khiên + `?`, không có người.
- **B18:** vạch `a plan` có trong khung 2, 3, 4. Khung 4 thêm nhãn mô tả. Khung 5–6 không đổi (S18.5–S18.6).
- Giờ khung: `review-c4/strips/strips.json` (mục `r1` giữ giờ/sha cũ của 5 dải; mục `r2`).

## 4. Kiểm (540p, `work/factory/world/<đoạn>-540.*`)
| Đoạn | Quy tắc 1/2/3 · cắt cứng | 5 s đầu W | W / C | F-2 | sync lời (median, p90) · ASR | sync hình ≤ 0,2 s |
|---|---|---|---|---|---|---|
| A S01–S03 | 0/0/0 · 0 | có | 52,9 / 47,1 % (r1 53,6/46,4) | WARN (1 cặp nhãn 1 mẫu ở S03.1 như r1; BLOCK 0) | +0,007 / 0,123 s · 131/141 | **17/17** (c6.rule +0,087, c6.seventy +0,004, c6.bar +0,107) |
| B S04–S09 | 0/0/0 · 0 | có | 32,3 / 67,7 % | WARN, BLOCK 0 | +0,004 / 0,133 s · 299/334 (r1 292) | 19/20 (p1.lender không đo được, như r1) |
| C S10–S14 | 0/0/0 · 0 | có | 31,5 / 68,5 % (r1 40,2/59,8: bỏ khu nhà S14) | WARN, BLOCK 0, label_overlaps 0 | 0,000 / 0,161 s · 296/327 | **26/26** (z0 +0,133, z1 +0,060, z2 +0,067) |
| D S15–S20 | 0/0/0 · 0 | có | 20,7 / 79,3 % | WARN, BLOCK 0 | 0,000 / 0,161 s · 319/360 | 22/24 (o0.climbing, v1.fell không đo được, như r1; a1.plan +0,109, v3.lender +0,143, v1.below +0,140) |

- Một lần dựng D trượt F-2 BLOCK: tỉ lệ chỉ số 5,0 đẩy trục năm xuống dải chữ cố định, và gạch dọc tháng 112 cắt nhãn "schedule: 90 payments". Đã sửa: tỉ lệ 4,0, gốc −0,2, bỏ gạch dọc. Dựng lại thì đạt.
- `lint_comments` 0. Khi sửa, một lần chú thích nuốt mã (D, dòng chỉ số) bị bắt bằng `node --check` trước khi dựng.
- Master: `bash toolkit/build.sh episodes/ep005/episode.yaml` exit 0 (splice 4 đoạn, mix, qc). Rồi `c4/build_inputs.py --out` → `out/video.mp4`. qc master: sàn chữ, tương phản, vùng an toàn, va chạm nhãn, F-2 giao nhau, nhãn ILLUSTRATIVE/history đều ĐẠT.
- C14 bỏ qua ở 540p (đo ở bản 1080p).
- Phát hành: `review-c4/animatic-540p.mp4` (master mới), 5 dải mới, `highlights.mp4` (168,4 s, cùng cách cắt review_pack). Không chạy `review_pack.py`, vì nó sẽ ghi đè `spans.json` từ beats.md và mất muted read B18 đã sửa.

## 5. Giờ render (thật, 540p, 4 lõi; máy chạy chung với một lượt render 1080p khác)
| Lượt | A | B | C | D | Tổng build.sh |
|---|---|---|---|---|---|
| dựng 1 (take cũ, bị dừng khi có lệnh take mới) | 408 s | — | — | — | — |
| dựng 2 (take mới) | 546 s | 1362 s | 972 s | 446 s (verify F-2 BLOCK) | 3709 s |
| dựng 3 (cuối) | 238 s / 58,0 s phim (12,8 s/s) | 415 s / 129,8 s (10,9) | 718 s / 132,6 s (18,8) | 464 s / 144,0 s (12,5) | 3483 s (world 2189 s, splice 67, mix 185, shorts 856) |

Dựng 3 render lại cả A và C: `music_db` của spine đổi theo lời/nhạc mới. Khoá cache gồm spine, nên cache không giữ được.
Stills dò bố cục (`render_shots.js --stills`): ≈ 4 s mỗi lần, khoảng 10 lần. ASR sync: 4 đoạn × ≈ 1–2 phút.

## 6. Việc tiếp
Cổng gốc C4 vòng 2 cho B03, B08, B14, B17, B18: người đọc MỚI, dải mới, cùng ý đồ `gates/C4-root-intent.md`, khoá nghĩa ≥ vòng 1.
- Lưu ý cho người chấm: B14 không còn cảnh nhiều nhà (S14.3 là tên trên đồ thị). B18 có tên `a plan`, không phải "your plan".
- Một lượt render 1080p khác (`scratchpad/fx`, đoạn B) đang chạy song song trên `spine.json` cũ của đoạn B. Spine đã đổi (take S04 mới) → cần dựng lại.
