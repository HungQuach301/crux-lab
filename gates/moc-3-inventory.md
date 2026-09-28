# Cổng Mốc 3 — kiểm kê phạm vi hẹp (bốn điều kiện đầu vào)

Phiên D1, 2026-09-28. Nguồn: crux-studio `main` @ `c7cadd7d99a6c63e674b5c587108f8e5efda3d50` và nhánh `claude/tier4-evidence` @ `413637d`. Đọc bằng git ẩn danh, không sửa gì ở crux-studio. Định nghĩa cổng: [`moc-3.md`](moc-3.md).

**Chỉ kiểm bốn điều kiện đầu vào.** Không chạy Thesis Engine, không tạo luận điểm.

## Cách đọc trạng thái PR

Phiên này **không có quyền API GitHub cho crux-studio**. Yêu cầu gắn repo có thông tin xác thực đã bị từ chối, và phiên không thử đường vòng. Trạng thái PR vì vậy suy từ git:
- ref `refs/pull/N/head`;
- commit squash-merge "(#N)" trên `main`.

Phiên **không xem được** PR nào đang mở, comment review, hay CI của PR.

| Mục backlog | PR | Trạng thái suy từ git |
|---|---|---|
| T-003 kho ảnh chụp | #114 | đã merge |
| T-004 phát hiện thay đổi | (commit của lượt `crux-worker-2`) | trên `main`; backlog ghi `status: review`, còn treo workflow và kiểm hạn |
| T-005 thư viện + kiểm bốn cấp | — | trên `main`, backlog `done` |
| T-006 tám mô hình | **#125** (head `019d876`) | đã squash-merge (`bcc034b`); backlog ghi `review` |
| T-006b cấp kiểm 4 | #264 (sóng 1, cơ chế) | đã merge. **Sóng 2 (chạy thật) nằm ở nhánh `claude/tier4-evidence` @ `413637d`, chưa merge** |
| T-007 Sensitivity Pass | (lượt `crux-worker-3`) | trên `main`, backlog `done` |
| T-008 corpus, kiểm mới lạ | **#91** (head `d433aea`) | đã squash-merge (`702a2d5`); backlog ghi `review` |
| T-014 embeddings | #253 | đã merge, backlog `review` |
| T-015 embeddings qua proxy | #315 | đã merge, backlog `review` |
| T-011 corpus bằng API nền tảng | — | `parked` (thiếu khoá API nền tảng) |

Tóm lại: "T-006/T-008 đang review" là trạng thái **mục backlog**, không phải PR mở. Code của cả hai đã ở `main`. Phần chưa merge duy nhất tìm thấy là **bằng chứng cấp 4** của T-006b.

---

## a) Kho ảnh chụp dữ liệu (T-003, T-004)

**Ngưỡng:** ≥ 30 chuỗi từ ≥ 4 nhà cung cấp, cơ chế phát hiện thay đổi hoạt động.

**Kết luận: THIẾU.** Có công cụ, không có dữ liệu: **0 chuỗi, 0 nhà cung cấp** có ảnh chụp thật.

| | Có gì |
|---|---|
| Code | `topic/src/snapshot.ts`: contract `snapshot.v0`, ba adapter chuẩn hoá `normalizeFred`, `normalizeBls`, `normalizeCensus` → `{period, value}`, `contentHash` không tính `fetchedAt`, `requireSecret` ném `MissingSecretError` trước khi chạm mạng. `transport` mặc định ném `LiveFetchNotWiredError`, tức **chưa có đường gọi API thật**. |
| Phát hiện thay đổi | `topic/src/change-detect.ts`: `diffSnapshots` (revised/added/removed), `impactedClaims` + `buildChangeIssue` (trỏ tới tập, `claimId`, số cũ/số mới), ba loại thay đổi (new-period / revision / definition-change), khử trùng. Chạy được như **hàm thuần**. Workflow định kỳ (`detect-changes.yml`) và việc mở issue thật **chưa có**. Kiểm hạn chuỗi `annual-reset` **chưa làm**. |
| Dữ liệu | Không có thư mục `data/snapshots/` ở crux-studio. Ba chuỗi trong test (`UNRATE`, `LNS14000000`, `B25077_001E`) chỉ là fixture. |
| Test | `snapshot.test.ts` (24), `change-detect.test.ts` (15): đạt |
| Đã chuyển | `topic/src/snapshot.ts`, `change-detect.ts`, `contracts/snapshot.v0`, `contracts/claim-source.v0`, hai file test |

**Phụ thuộc hạ tầng cũ và cách tách:**
- `@crux/kernel` (`validate`, `stableHash`) → thay bằng `topic/lib/kernel.ts`.
- Workflow `.github/` và cơ chế mở issue → không mang; ở crux-lab sẽ là một lệnh chạy tay (không tạo CI theo đầu bài).
- Khoá API `FRED_API_KEY`, `BLS_API_KEY`, `CENSUS_API_KEY` → chưa có ở crux-lab.

**Đo mạng của môi trường này (2026-09-28):**
- `fred.stlouisfed.org/graph/fredgraph.csv` tải được **không cần khoá**. Tập 1 đã dùng đường này cho `MORTGAGE30US` và `OBMMIC30YF` (nhánh `ep001`, `episodes/ep001/data/`).
- `api.stlouisfed.org`, `api.bls.gov`, `www.bls.gov`, `api.census.gov`, `www.irs.gov`, `www.ssa.gov`, `www.treasurydirect.gov` bị proxy chặn.
- `ffiec.cfpb.gov` chỉ vào được API tổng hợp.

Với mạng hiện tại, **chỉ một nhà cung cấp (FRED) lấy được**, nên ngưỡng ≥ 4 nhà cung cấp không đạt được nếu chủ dự án chưa mở thêm domain.

## b) Thư viện mô hình (T-005, T-006)

**Ngưỡng:** ≥ 8 mô hình, **mỗi mô hình qua kiểm bốn cấp** (spec 14 mục 2).

**Kết luận: THIẾU.** Có 8 mô hình. Cấp 1 đạt cả 8. Cấp 4 đã chạy thật nhưng **chỉ 2/8 sạch**, và kết quả chưa ghi vào file mô hình. `verification.status` của cả 8 là `pending`.

Bốn cấp và trạng thái từng mô hình (cấp 2 và 3 "không bắt buộc" theo `required: false` trong file mô hình; cấp 4 lấy từ nhánh `claude/tier4-evidence`, `openai/gpt-5`, 2026-09-26):

| Mô hình | Tiêu đề | Cấp 1: ca tay | Cấp 2 | Cấp 3 | Cấp 4 (chạy thật) | Trong file mô hình |
|---|---|---|---|---|---|---|
| M-001 | Tỷ lệ chi phí quỹ ăn mòn danh mục | ✅ 3 ca | — | — | ❌ 3 giả định chưa khai | cấp 4 `pass: false` |
| M-002 | Điểm hoà vốn mortgage discount points | ✅ 2 ca (CFPB Ask #136) | — | — | ❌ 6 giả định chưa khai | như trên |
| M-003 | APY theo Regulation DD | ✅ 8 ca | — | — | ❌ 3 giả định | như trên |
| M-004 | Giảm trợ cấp an sinh nhận sớm | ✅ 2 ca | — | — | ❌ 3 giả định | như trên |
| M-005 | RMD từ IRA truyền thống | ✅ 3 ca | — | — | ❌ 2 giả định + **2 lỗi đơn vị** (`applicableDenominator` khai "year" nhưng dùng như hệ số không thứ nguyên) | như trên |
| M-006 | Lãi suất tổng hợp trái phiếu Series I | ✅ 1 ca | — | — | ✅ sạch | như trên |
| M-007 | Phần trợ cấp an sinh chịu thuế | ✅ 1 ca | — | — | ❌ 5 giả định | như trên |
| M-008 | Khấu trừ IRA bị giảm theo thu nhập | ✅ 2 ca | — | — | ✅ sạch | như trên |

- Tổng 22 ca cấp 1, mỗi ca trích nguồn nhà nước Mỹ (SEC, CFPB, 12 CFR 1030, 20 CFR 404.410, IRS Pub 590-A/B, 915, TreasuryDirect).
- Log lượt chạy cấp 4: *"cấp kiểm 4 qua openai/gpt-5: 2/8 khớp, 0 đầu ra không dùng được, tổng costUsd 0.4131"*.
- `KF-012` ghi hai mâu thuẫn trong chính nguồn: TreasuryDirect 4,03% so với 4,26%, và IRS 590-A $6.830 so với $6.825. Cả hai đã nằm trong `assumptions`.

**T-006 (PR #125): phần xong, phần thiếu.**
- Xong: 8 mô hình theo contract, 22 ca cấp 1 có trích dẫn, registry công thức, 74 test ở `models.test.ts`.
- Thiếu 1: sửa 6 mô hình theo các giả định chưa khai và lỗi đơn vị mà cấp 4 nêu, rồi chạy lại cấp 4.
- Thiếu 2: ghi `verification.tiers[llm-assumption-check]` vào 8 file mô hình, kèm `evidenceRef`.
- Thiếu 3: tám issue `irreversible` để chủ dự án đặt `verified`. Theo D-C02, máy **không được** tự đặt `verified`; `computeVerification` bị khoá ở tầng kiểu.

**Hai điểm cần chủ dự án đọc:**
- Cấp 2 (đối chiếu công cụ công khai) và cấp 3 (triển khai thứ hai) đều ghi `required: false` ở cả 8 mô hình. Spec nói cấp 3 bắt buộc khi `geoVarying: true` **hoặc** mô hình dùng ở > 3 tập. Chưa mô hình nào dính điều kiện đó, nên "qua kiểm bốn cấp" hiện nghĩa là **cấp 1 + cấp 4**.
- **Không mô hình nào trong 8 là mô hình tái cấp vốn của Tập 1.** M-002 (discount points) gần nhất về công thức: trả góp đều, hoà vốn = chi phí / tiết kiệm tháng.

| | |
|---|---|
| Test | `models.test.ts` (74 test), `model-runner.test.ts`, `model-verify.test.ts`: đạt |
| Đã chuyển | `topic/src/{model-runner,model-verify,models}.ts`, `contracts/model.schema.json`, `data/models/` (8 mô hình, `cases/`, **`tier4/` lấy từ nhánh chưa merge `413637d`**) |
| Phụ thuộc cũ | `@crux/kernel.modelSchema` → `lib/kernel.ts`. Runner cấp 4 `ops/scripts/model-assumption-check.ts` chạy trong GitHub Actions với secret `OPENAI_API_KEY` → **không mang**. Muốn chạy lại cấp 4 ở crux-lab thì viết một script nhỏ gọi qua proxy (môi trường này có `api.openai.com` gắn sẵn khoá) hoặc dùng một nhà cung cấp khác Claude, theo đúng yêu cầu "nhà cung cấp khác". |

## c) Sensitivity Pass (T-007)

**Ngưỡng:** tìm được điểm đảo chiều **thật** trên ≥ 4 mô hình.

**Kết luận: THIẾU.**
- Có flip: **3/8** (M-002, M-007, M-008).
- Flip "thật" theo nghĩa ngưỡng ẩn, phái sinh: **0/8**.

Phiên này **đo** (`node topic/scripts/sensitivity-all.ts`, kết quả ở `topic/data/sensitivity/sensitivity-all-2026-09-28.json`): quét mọi tham số trên toàn `validRange`, 1.000 bước, với một output kết luận cho mỗi mô hình.

| Mô hình | Output kết luận | Điểm đảo chiều | Đánh giá |
|---|---|---|---|
| M-002 | `monthlySavingsUsd` | `rateWithPointsPct` = 5 (= lãi nền); `baseRatePct` = 4,875 (= lãi có điểm) | **đồng nhất thức**: tiết kiệm > 0 khi lãi mới < lãi cũ. Không phải ngưỡng ẩn. Flip có giá trị (hoà vốn so với thời gian giữ) cần một output mô hình chưa có. |
| M-007 | `taxableBenefitsUsd` | `baseAmountUsd` = 32.000; `adjustmentsUsd` = 100.000 | tái hiện **ngưỡng luật đã công bố** ($32.000). Điểm 100.000 là điểm lưới đầu tiên chạm 0 (bước 100.000 trên khoảng 10⁸); điểm cắt thật nằm trong (0; 100.000]. |
| M-008 | `iraDeductionUsd` | `modifiedAgiUsd` = 200.000 | tái hiện **đỉnh vùng giảm trừ đã công bố** |
| M-001, M-003–M-006 | — | không có | mô hình tính một đại lượng, không có biến quyết định đổi dấu |

- Code `runSensitivityPass` chạy đúng, xác định, có test (14).
- Chỗ thiếu nằm ở **thư viện**: 6/8 mô hình là "máy tính" của một quy định, không phải mô hình **quyết định giữa hai lựa chọn**, nên không có gì để đảo chiều.
- Không tham số nào mang `geoVarying: true`, nên chưa có phép quét toàn bang nào. Đây lại chính là cơ chế bù trừ số 1 của `persona.md`.
- Việc T-007 để lại chưa làm: CLI `run-sensitivity.ts` và một kết quả quét commit làm tham chiếu (WP-013 mục 3, 7). `topic/scripts/sensitivity-all.ts` lấp một phần.

| | |
|---|---|
| Test | `sensitivity.test.ts` (14): đạt |
| Đã chuyển | `topic/src/sensitivity.ts`, `contracts/sensitivity.v0`, test, **`scripts/sensitivity-all.ts` (mới)** và kết quả |
| Phụ thuộc cũ | chỉ `@crux/kernel.validate` → `lib/kernel.ts` |

## d) Corpus đối thủ (T-008, novelty check, embeddings T-015)

**Ngưỡng:** ≥ 200 video, kiểm mới lạ tự động chạy được.

**Kết luận: THIẾU.**
- Corpus: **38 video, dựng tay** (`provenance: "hand-built"`), không phải dữ liệu thu từ nền tảng. Tính theo dữ liệu thật: **0/200**.
- Kiểm mới lạ **chạy được tự động** (so từ vựng).
- Nhánh so ngữ nghĩa có đường gọi nhưng **chưa chọn được model**.

| | Có gì |
|---|---|
| Corpus | `topic/data/corpus/us-personal-finance-2026-09-01.json`: 38 video, `contentLevel: metadata-only` (API không cho tải phụ đề của người khác), `quota.spent.searchCalls = 10` (khai). `quotaGate` dừng ở mốc dự trữ 20%. `corpusProblems` đỏ khi số gọi lệch số trang. Hạn mức `search.list` mới "theo tài liệu" (G19, cần người đọc Cloud Console). |
| Xây corpus thật | **T-011 `parked`**: thiếu khoá API nền tảng (chọn nhà cung cấp và ký điều khoản là `irreversible`). Ở môi trường này `googleapis.com/youtube/v3` trả 403 và `youtube.com` bị chặn. |
| Kiểm mới lạ | `topic/src/novelty.ts` `checkNovelty`: thuần, không gọi mạng, trả `reasons`. Các `verdict` gồm `novel-in-corpus`, `crowded-in-corpus`, `contested-in-corpus`, `insufficient-corpus`; **không có `novel` trần**. `limitation` bắt buộc ≥ 40 ký tự. Mặc định so **từ vựng**, nên chệch về `novel-in-corpus` khi đề tài diễn đạt khác chữ. |
| Embeddings (T-014, T-015) | `topic/src/embeddings.ts`: provider trung tính, `resolveEmbeddingsAuth` (secret / proxy / stop), `measureSeparation`, `cheapestAdequateModel`. Lần chạy thật 2026-09-27: 3 model, 1.998 token, **$0,000166**. **Không model nào tách được tập thăm dò 16 cặp** (margin −0,012 / 0,038 / −0,026, đều < 0,05), nên `null`, chưa chọn model. |
| Đại lượng nhu cầu | `topic/src/demand.ts`: ba đại lượng thay thế, bắt buộc có `asOf`, `region`, `language`, `knownBias`. |
| Test | `corpus.test.ts` (18), `novelty.test.ts` (18), `demand.test.ts` (11), `embeddings.test.ts` (31): đạt |
| Đã chuyển | `topic/src/{corpus,novelty,demand,embeddings}.ts`, 5 contract, `data/corpus/`, `data/embeddings/`, `packs/quota-budget.md`, 4 file test |

**T-008 (PR #91): phần xong, phần thiếu.**
- Xong: ba contract, ba module, corpus mẫu, bảng quota, 38 test ban đầu.
- Thiếu 1: hạn mức đo thật (G19, cần người).
- Thiếu 2: corpus thật (T-011, cần khoá API nền tảng).

**Phụ thuộc cũ và cách tách:**
- `@crux/kernel` → `lib/kernel.ts`.
- `ops/scripts/novelty-embeddings-trial.ts` (ghi log vào `ops/logs/`, gọi API trả tiền) → không mang; phần thuần đã ở `src/embeddings.ts`.
- `NODE_USE_ENV_PROXY=1` cần khi gọi `api.openai.com` qua proxy từ Node (đo ở T-015).

---

## Thesis Bank và schema thesis: dùng được gì cho Thesis Engine

| Tài sản | Trạng thái | Dùng được |
|---|---|---|
| `packs/channels/us-personal-finance/thesis-bank.md` → `topic/packs/thesis-bank.md` | văn bản định nghĩa, không có mục nào | Bốn điều kiện "đạt chuẩn" (có `contradicts`, kiểm được bằng số qua ma trận ngưỡng ba tầng, mới lạ kiểm tự động, `origin.source` thuộc năm nguồn); sàn ≥ 15 mục khả dụng; `rejectionReason` bắt buộc. Dùng thẳng làm tiêu chí. |
| Thư mục `thesis-bank/` | **chưa có** (việc của T-009) | — |
| `thesis.schema.json` | **chưa từng thành contract** ở crux-studio. `kernel/contracts/` không có; spec ghi "chưa có, là mục `kernel/K-002`". Chỉ tồn tại như khối gợi ý trong spec (dòng 5354–5393) → chép thành `topic/contracts/thesis.reference.schema.json` | Dùng làm điểm khởi đầu: 13 trường bắt buộc, `origin.source` enum 5 nguồn (`data-conflict`, `hidden-threshold`, `unanswered-question`, `comment-cluster`, `release-calendar`), `expectedThresholds`, `flipPreview`, `rpmTier`, `status`. |
| Contract `topic.payload.v0` (kernel) | lỏng, về đề tài/claims của xưởng | Không dùng cho thesis. |

Hai chỗ lệch cần sửa trước khi viết engine:
1. **`noveltyVerdict`.** Schema thesis dùng enum `novel | incremental | duplicate`, còn `checkNovelty` (contract `novelty-check.v0`) trả `novel-in-corpus | crowded-in-corpus | contested-in-corpus | insufficient-corpus` và cố ý không có `novel`. Phải chọn một bộ, hoặc viết bảng ánh xạ có ghi giới hạn.
2. **Chấm mù cần tách phần hiển thị.** Theo "chuẩn hoá thẻ" của cổng, thẻ đem chấm mù không được hiện con số. Schema có `expectedThresholds` và `flipPreview`, thường chứa số, nên phải có một **dạng thẻ chấm mù** riêng (một câu luận điểm + một câu niềm tin bị phản bác, cùng độ dài).
