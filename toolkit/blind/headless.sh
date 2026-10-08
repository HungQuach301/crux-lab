#!/usr/bin/env bash
# Một lượt đọc mù bằng Claude Code headless (Phiên T4, đo ở tongket-t4/REPORT.md §2a): không agent con, không ngữ cảnh dự án.
# Lời chỉ nằm trong file đầu bài (vai + câu hỏi cố định + lời dán nguyên văn). Có ảnh/dải khung → --read: chỉ bật công cụ Read.
#   bash toolkit/blind/headless.sh <đầu-bài.txt> <ra.json> [--read] [--model sonnet]
# ra.json: {"answer", "tokens": {model: {input, cache_write, cache_read, output, in, out}}, "turns"}. Bốn trường riêng (tổng kết Tập 5 §3.6):
#   trần = input + cache_write + output (đầu vào mới + sinh ra); cache_read báo riêng. `in` = input + cache_write + cache_read (cận trên, giữ
#   cho tệp cũ Tập 4–5), `out` = output. Token đo: ≈ 7 nghìn/lượt chữ, ≈ 11 nghìn/lượt ảnh (agent con: 32–49 nghìn).
set -euo pipefail
prompt=$1; out=$2; shift 2
tools=""; model=sonnet
while [ $# -gt 0 ]; do case $1 in --read) tools=Read;; --model) model=$2; shift;; esac; shift; done
args=(-p --model "$model" --output-format json --no-session-persistence --tools "$tools")
[ -n "$tools" ] && args+=(--allowedTools "$tools")
raw=$(mktemp)
# chạy từ thư mục trống để không nạp CLAUDE.md hay skill của repo
(cd "$(mktemp -d)" && claude "${args[@]}" < "$(realpath "$prompt")") > "$raw"
python3 - "$raw" "$out" <<'PY'
import json, sys
d = json.load(open(sys.argv[1]))
tok = {k: {'input': v['inputTokens'], 'cache_write': v['cacheCreationInputTokens'], 'cache_read': v['cacheReadInputTokens'],
           'output': v['outputTokens'],
           'in': v['inputTokens'] + v['cacheReadInputTokens'] + v['cacheCreationInputTokens'], 'out': v['outputTokens']}
       for k, v in d.get('modelUsage', {}).items()}
json.dump({'answer': d.get('result', ''), 'tokens': tok, 'turns': d.get('num_turns')}, open(sys.argv[2], 'w'), indent=1, ensure_ascii=False)
print(sys.argv[2], {k: {'trần': v['input'] + v['cache_write'] + v['output'], 'đọc cache': v['cache_read']} for k, v in tok.items()})
PY
rm -f "$raw"
