#!/usr/bin/env bash
# Tập 6 P3c: một lượt Claude Code headless chi bằng khoá Console (BƯỚC 0 đạt: apiKeySource=ANTHROPIC_API_KEY). Không in khoá.
#   bash episodes/ep006/c5/api.sh <build|review> <đầu-bài.md> <log.jsonl> [--model claude-opus-5-5]
# build: sửa tệp trong repo (Read/Edit/Write/Grep/Glob, Bash python3/node/git diff/status); review: chỉ đọc.
# In tóm tắt: lượt, token 4 trường, chi USD (total_cost_usd) → ghi vào PLAN §5.
set -euo pipefail
mode=$1; brief=$(realpath "$2"); log=$3; shift 3; model=claude-opus-5-5
while [ $# -gt 0 ]; do case $1 in --model) model=$2; shift;; esac; shift; done
[ -n "${CONSOLE_API_KEY:-}" ] || { echo "thiếu CONSOLE_API_KEY"; exit 2; }
case $mode in
  build)  tools="Read,Edit,Write,Grep,Glob,Bash(python3 *),Bash(node *),Bash(NODE_PATH=* node *),Bash(git diff*),Bash(git status*),Bash(git log*),Bash(ls *),Bash(ffmpeg *),Bash(ffprobe *)";;
  review) tools="Read,Grep,Glob,Bash(git *),Bash(python3 *)";;
  *) echo "mode build|review"; exit 2;;
esac
cd "$(dirname "$0")/../../.."
ANTHROPIC_API_KEY="$CONSOLE_API_KEY" claude -p --model "$model" --output-format stream-json --verbose \
  --allowedTools "$tools" --permission-mode dontAsk < "$brief" > "$log" 2> "${log%.jsonl}.err" || true
python3 - "$log" <<'PY'
import json, sys
init = res = None
for l in open(sys.argv[1]):
    try: d = json.loads(l)
    except Exception: continue
    if d.get('type') == 'system' and d.get('subtype') == 'init': init = d
    if d.get('type') == 'result': res = d
print('apiKeySource:', init and init.get('apiKeySource'))
if res:
    u = res.get('usage', {})
    print(json.dumps({'turns': res.get('num_turns'), 'is_error': res.get('is_error'), 'cost_usd': res.get('total_cost_usd'),
                      'input': u.get('input_tokens'), 'cache_write': u.get('cache_creation_input_tokens'),
                      'cache_read': u.get('cache_read_input_tokens'), 'output': u.get('output_tokens')}))
    print('--- trả về ---'); print(res.get('result', '')[-3000:])
PY
