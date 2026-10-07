# C3 · vòng 3 (vòng CUỐI, sửa người dựng) — N1 lịch, N2 cột · 2026-10-07

Nguồn trượt: `gates/C3-root.md` vòng 2. Nghĩa giữ (N1 3/3, N2 2/2), nhưng khuyên_tính vẫn 3/3 và 2/2 (`c3/root-r2/*.json`, `key.json`).
Câu khuyên còn lại: N1 "plan to stay a long time", "make extra principal payments early", "weigh how long you'll stay"; N2 "only buy if you can stay in the home", "don't try to time the market".
Tiền lệ: D-010 §6 (b) vòng #10 (E5j): đổi màu đường chậm sang trung tính + nhãn thời lượng → 6/6, 0 khuyên (`moc-v/seg/ep005/scene.js`: `slow` → `C.accent`, nhãn "slowest case ≈ 9 years").
Vòng 3 được phép: đổi hình + **một** nhãn ngắn (≤ 8 từ, ≥ 48 px, sự thật, không mệnh lệnh). Không đổi: lời, take (0 ký tự EL), độ dài đoạn (N1 449 khung, N2 446), sự kiện âm, `spans.json` (muted read), quy tắc D-010 1/2/3/7, `checks/`, `toolkit/`, `obj5.js`.

## 1. Chẩn đoán (đọc câu trả lời vòng 2)

### N1 — "ở lâu", "trả thêm gốc sớm"
| Phần tử (vòng 2) | Vì sao còn mời khuyên |
|---|---|
| Đoạn cuối đường in (kỳ 240–360) **sáng lên** (chrome, dày hơn) ở "faster"; chồng đứng ở kỳ 114 | Cuối lịch thành **đích sáng** cách xa chồng → "trả nhanh" là phần thưởng phải *ở đủ lâu* mới tới (R2/R5: "the payoff comes from holding the home for years"). |
| Tiêu đề "loan balance · on the schedule" | Không nói lịch là **cho sẵn** → đường dư nợ đọc như thứ người vay điều khiển được → "extra principal payments early" (R2, R3, R5). |

### N2 — "chỉ mua nếu ở được lâu", "đừng canh thị trường"
| Phần tử (vòng 2) | Vì sao còn mời khuyên |
|---|---|
| Cụm cột > 60 tháng **warn (vàng)** + ngoặc + dải warn | Màu báo động = rủi ro cần phòng → câu khuyên phòng thủ (ở lâu, chịu được đợt giảm). Giống đường chậm E5i trước E5j. |
| Ý nghĩa chiều cao cột chỉ nằm trong tiêu đề xa phía trên ("Months to 80% on paper · one bar …") | Người đọc gọi chiều cao là "chờ 5 năm+" chung chung → hiểu thành thời gian **phải giữ nhà** ("plan for five years or more … buy only if you could stay put"). |
| Đường chỉ số màu accent dưới cụm | Không gây khuyên trực tiếp, nhưng trùng màu với lựa chọn trung tính cho cột chậm → đổi. |

## 2. Đã đổi gì

### N1 — `n1-calendar/{scene.js,spine.py}` (spine v4, cùng mốc)
1. **Bỏ "đích" ở cuối lịch:** xoá ribbon `late` (đoạn 240–360 sáng lên ở "faster"). Cả lịch 360 kỳ in một màu trung tính (muted), một độ dày (0,055, đậm hơn vòng 2 để đọc như vật cho sẵn). Chồng vẫn đi 0 → 114 rồi đứng (vòng 2).
2. **Nhãn sự thật duy nhất (7 từ, 52 px, ink):** tiêu đề đồ thị `loan balance · on the schedule` → **`loan balance schedule · set on day one`** (lịch cố định từ ngày vay — đúng S20.2 "set the day the loan starts"). Không mệnh lệnh, không số.
3. "faster later" thêm nền mờ (cùng kiểu các nhãn khác); vẫn hiện ở "faster" cạnh đoạn dốc. Cue hình `a1.faster` đổi từ motion-roi (đoạn sáng lên, đã bỏ) sang **nhãn** (`label_cues['a1.faster'] = 'faster later'`).
4. Giữ: chip `$2,362/month · principal + interest` (REVIEWER R1 B06, muted read), người/nhà rời khung khi sang đồ thị, 5 s đầu thế giới.

### N2 — `n2-bars/{scene.js,spine.py}` (spine v4, cùng mốc)
1. **Cột chậm màu trung tính** (`C.accent`, không còn `C.warn`) — cả cột, ngoặc trên cụm và dải mờ dọc cụm xuống trục tháng mua (theo E5j).
2. **Chỉ số giá quốc gia → muted** (không trùng màu cột chậm); đoạn đỉnh → đáy ở "slump" đậm bằng ink; nhãn "national home price index" muted.
3. **Nhãn thời lượng gắn vào cụm (nhãn mới duy nhất, 8 từ, 48 px, ink, nền mờ):** `each bar's height:` / `months to 80% on paper`, cạnh một **thước dọc** ở mép phải cụm (chân cột → đỉnh cột cao nhất, `maxB_months_to80` = 112). Chiều cao = một phép đo trên giấy theo tháng mua, không phải thời gian giữ nhà.
4. **Trục tháng mua làm chủ:** tiêu đề còn `one bar per purchase month` (52 px, trước 48 px kèm "Months to 80% on paper"); năm 48 px, dải chỉ số trong trục, ngoặc `one stretch of purchase months` giữ nguyên. Tỉ lệ `14.7% (about 1 in 7)` giữ nguyên.

## 3. Trước / sau (dải mù, cùng thời điểm `spans.json` / `strips.json`)
- N1: vòng 2 `review-c3/strips/N1-calendar.r2.png` (vòng 1 `.r1.png`) → vòng 3 `review-c3/strips/N1-calendar.png`. Khung 1–3 như vòng 2 (thế giới; chip vốn + lãi ở khung 3). Khung 4–6: tiêu đề `loan balance schedule · set on day one`; cả đường lịch một màu, không đoạn cuối sáng; `payment 43 / 92 / 114`; khung 6 `faster later` trên nền mờ, chồng đứng ở 114.
- N2: vòng 2 `review-c3/strips/N2-bars.r2.png` (vòng 1 `.r1.png`) → vòng 3 `review-c3/strips/N2-bars.png`. Khung 1–2 cụm chậm xanh trung tính (không vàng). Khung 3–6: tiêu đề `one bar per purchase month`; thước + `each bar's height: / months to 80% on paper` bên phải cụm; khung 5–6 chỉ số muted trong trục. Khung 6 rơi đúng "national" như vòng 1–2 (đoạn "slump" đậm chưa hiện).

## 4. Kiểm (bằng chứng `review-c3/evidence/`)
| Đoạn | spine 2/3/7 | verify quy tắc 1 / 2 (từ khoá) / 3 | cắt cứng | 5 s đầu W | W / C | sync lời (median, p90) | sync hình ≤ 0,2 s |
|---|---|---|---|---|---|---|---|
| N1 | OK | 0 / 0 (8) / 0 | 0 | có | 38,7 % / 61,3 % | −0,016 / 0,106 s | **4/4** (faster +0,139, nhãn) |
| N2 | OK | 0 / 0 (9) / 0 | 0 | có | 37,3 % / 62,7 % | −0,008 / 0,099 s | **5/5** (tail −0,036, together +0,014, national +0,013) |
Lời + take: `words`/`takes` trong spine.json không đổi (0 ký tự EL); ASR khớp 32/37 (N1), 38/38 (N2) như vòng 1–2. Âm của hai đoạn mới **trùng bit** với vòng 2 (md5 PCM). C14 bỏ qua ở 540p (đo ở bản 1080p).

## 5. Clip + giờ render
- `review-c3/c3-clip.mp4`: thay N1 (khung 1070–1518) và N2 (2029–2474) bằng bản vòng 3; mọi khung khác chép từ clip vòng 2 (PSNR so r2: cold open 56,9 dB, N3 53,1 dB = chỉ do mã hoá lại; N1/N2 so bản đoạn 54,9 / 54,0 dB). Âm clip chép nguyên (trùng bit). 2476 khung, 82,53 s. `strips/strips.json`: sha video mới + N1/N2 mới, mục `r3`; PNG N3 giữ của r1.
- Giờ render thật (540p, 4 lõi): N1 1 lần dựng — render 32,1 s wall cho 14,97 s phim (3,57 s/s), build 39,3 s. N2 2 lần dựng (lần 1 nhãn chiều cao tràn mép phải → rút "until" thành "to", dời 6 px) — bản cuối render 53,5 s cho 14,93 s (5,97 s/s), build 61,1 s; cả hai lần ≈ 122 s. ASR sync 2 lượt; ghép clip ≈ 10 s; dải ≈ 2 s.

## 6. Việc tiếp
Cổng gốc C3 vòng 3 cho N1, N2 (người đọc MỚI, dải mới, cùng ý đồ `gates/C3-root-intent.md`); khoá nghĩa: nghĩa ≥ vòng 2. Muted read N2 trong `spans.json` vẫn ghi "turn warn" (không sửa theo lệnh) — người chấm so nghĩa (cột > 60 tháng nổi bật, ít, liền nhau 2005–2009, dưới đoạn đỉnh → đáy của chỉ số), màu không phải nghĩa; ghi lại nếu người chấm trừ vì màu.
Khi dựng tập: màu cột chậm trung tính (accent) và chỉ số muted phải thống nhất với S11/S14 (cùng cBars); tiêu đề N1 "set on day one" khớp S20.2.
