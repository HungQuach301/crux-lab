# topic/ — tài sản làn topic chuyển từ crux-studio (chuẩn bị cổng Mốc 3)

Chuyển ngày 2026-09-28, Phiên D1. Chỉ mang **code và dữ liệu** mà bốn điều kiện đầu vào của cổng cần (`gates/moc-3.md`). Kiểm kê và đánh giá: `gates/moc-3-inventory.md`, `gates/moc-3-readiness.md`.

## Chạy

```
node --test topic/test/*.test.ts             # 242 test, không cài gì (Node ≥ 22.18, TypeScript chạy bằng type stripping)
node topic/scripts/sensitivity-all.ts        # Sensitivity Pass trên cả 8 mô hình (--write: ghi data/sensitivity/)
```

Kết quả lúc chuyển: **242/242 PASS** trong crux-lab. Cùng 10 file test chạy trong bản clone crux-studio @ `c7cadd7` cũng cho 242/242. Không cần `pnpm`, workspace hay `node_modules`.

## Nguồn

| Ở đây | Từ crux-studio | Commit |
|---|---|---|
| `src/{snapshot,change-detect,model-runner,model-verify,models,sensitivity,corpus,novelty,demand,embeddings}.ts` | `workshops/topic/src/` | `main` @ `c7cadd7d99a6c63e674b5c587108f8e5efda3d50` |
| `test/*.test.ts` (10 file) | `workshops/topic/test/` | như trên |
| `contracts/*.v0.schema.json` | `workshops/topic/contracts/` | như trên |
| `contracts/model.schema.json` | `kernel/contracts/model.schema.json` | như trên |
| `lib/validate.ts`, `lib/hash.ts` | `kernel/src/validate.ts`, `kernel/src/hash.ts` (nguyên văn) | như trên |
| `lib/kernel.ts` | **viết mới**: gom `validate`, `stableHash`, `modelSchema`, thay cho gói `@crux/kernel` | — |
| `data/models/M-00{1..8}.json`, `data/models/cases/`, `data/models/README.md` | `workshops/topic/data/models/` | như trên. T-006 vào `main` qua PR #125 (squash `bcc034b`, head PR `019d876`) |
| `data/models/tier4/M-00{1..8}.tier4.json`, `data/models/tier4/run-log.jsonl` | nhánh **chưa merge** `claude/tier4-evidence` (`workshops/topic/data/models/tier4/`, `logs/T-006b.36253708269.jsonl`) | `413637d34d418450934e0e94b5bc1df2a59890ee` (2026-09-26, github-actions): bằng chứng sóng 2 của T-006b, cấp kiểm 4 bằng `openai/gpt-5` |
| `data/corpus/` | `workshops/topic/data/corpus/` | `main` @ `c7cadd7`. T-008 vào `main` qua PR #91 (squash `702a2d5`, head PR `d433aea`) |
| `data/embeddings/` | `workshops/topic/data/embeddings/` (T-014, PR #253; T-015, PR #315) | `main` @ `c7cadd7` |
| `packs/quota-budget.md` | `packs/channels/us-personal-finance/quota-budget.md` (`corpus.test.ts` đọc file này) | `main` @ `c7cadd7` |
| `packs/thesis-bank.md` | `packs/channels/us-personal-finance/thesis-bank.md` | `main` @ `c7cadd7` (commit gốc của file `b8c2014`) |
| `contracts/thesis.reference.schema.json` | khối `engine/contracts/thesis.schema.json` trong `docs/spec/CRUX-REFERENCE-SPEC.md` (dòng 5355–5393): **gợi ý** của spec, chưa từng thành contract ở crux-studio | spec @ `5c133eb` |
| `scripts/sensitivity-all.ts` | **viết mới** cho kiểm kê (đo điều kiện đầu vào 3) | — |
| `data/sensitivity/sensitivity-all-2026-09-28.json` | kết quả của script trên | — |

## Sửa khi chuyển

- `src/*.ts`: `from '@crux/kernel'` → `from '../lib/kernel.ts'`. Đây là chỗ sửa duy nhất trong code. Các chú thích "Bất biến I3 … `@crux/kernel`" giữ nguyên văn và nay trỏ tới `lib/kernel.ts`.
- `test/corpus.test.ts`: đường dẫn `quota-budget.md` → `../packs/quota-budget.md`.
- `packs/*.md`: thêm một dòng ghi nguồn ở đầu.

## Không mang sang (hạ tầng cũ)

- `workshops/topic/src/index.ts`, `run.ts`, `test/stub.test.ts`, `fixtures/`: vỏ "xưởng" của kernel (envelope, cassette, artifact store, CLI chạy xưởng).
- Phần còn lại của `kernel/`: envelope, workshop runner, packs, revenue, CLI.
- `ops/` (scripts, workflows, invariants, lanes, logs, golden), `.github/`, hàng đợi merge, luật nhận việc, `CLAUDE.md`.
- `ops/scripts/model-assumption-check.ts` và workflow của nó (runner cấp kiểm 4 chạy trong GitHub Actions); ở đây chỉ mang **bằng chứng** nó sinh ra.
- `ops/scripts/novelty-embeddings-trial.ts` (gọi API trả tiền, ghi log vào `ops/logs/`). Phần thuần của nó (`embeddings.ts`: provider, `measureSeparation`, `cheapestAdequateModel`, `resolveEmbeddingsAuth`) đã có ở `src/`.

## Dữ liệu lớn

Không file nào vượt 95 MB; lớn nhất là corpus mẫu 38 video (vài chục KB). Chưa có dữ liệu nào phải tải lại bằng script.

## Cần biết

- **Corpus là dữ liệu dựng tay**, không phải dữ liệu thu từ nền tảng (`provenance: "hand-built"`, 38 video, kênh `ch-01`…). Các test novelty/demand chạy trên dữ liệu giả này.
- **Kho ảnh chụp chưa có ảnh chụp thật nào.** `snapshot.ts` có ba adapter (`fred`, `bls`, `census`), nhưng `transport` mặc định ném `LiveFetchNotWiredError`, và ba chuỗi trong test chỉ là ví dụ.
- **`verification.status` của cả 8 mô hình là `pending`.** Cấp 4 đã chạy thật (bằng chứng ở `data/models/tier4/`) nhưng chưa được ghi vào `verification.tiers` của từng file mô hình. Chi tiết: `gates/moc-3-inventory.md`.
