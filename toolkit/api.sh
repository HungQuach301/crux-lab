#!/usr/bin/env bash
# Mọi tập (dời từ episodes/ep006/c5/api.sh; lessons T6-9): một lượt Claude Code headless chi bằng khoá Console (BƯỚC 0 đạt: apiKeySource=ANTHROPIC_API_KEY). Không in khoá.
#   bash toolkit/api.sh <build|review> <đầu-bài.md> <log.jsonl> [--model claude-opus-5-5] [--cap-usd 5]
# build: sửa tệp trong repo (Read/Edit/Write/Grep/Glob, Bash python3/node/git diff/status); review: chỉ đọc.
# In tóm tắt: lượt, token 4 trường, chi USD (total_cost_usd) → ghi vào PLAN §5.
# F-15 (TONGKET Tập 7 g: hai lượt dựng C5 $12 + $14 dùng agent con bên trong headless):
#   - CHẶN agent con: --disallowedTools Task,Agent,Workflow (không có trong danh sách cho phép VÀ bị cấm tường minh; log có tool_use Task/Agent → thoát 5);
#   - TRẦN CHI THEO LỆNH: --cap-usd (mặc định $CRUX_API_CAP_USD hoặc 5) → `claude --max-budget-usd`; lượt dừng khi chạm trần, in "TRẦN".
set -euo pipefail
mode=$1; brief=$(realpath "$2"); log=$3; shift 3; model=claude-opus-5-5; cap="${CRUX_API_CAP_USD:-5}"
while [ $# -gt 0 ]; do case $1 in --model) model=$2; shift;; --cap-usd) cap=$2; shift;; esac; shift; done
[ -n "${CONSOLE_API_KEY:-}" ] || { echo "thiếu CONSOLE_API_KEY"; exit 2; }
case $mode in
  build)  tools="Read,Edit,Write,Grep,Glob,Bash(python3 *),Bash(node *),Bash(NODE_PATH=* node *),Bash(git diff*),Bash(git status*),Bash(git log*),Bash(ls *),Bash(ffmpeg *),Bash(ffprobe *)";;
  review) tools="Read,Grep,Glob,Bash(git *),Bash(python3 *)";;
  *) echo "mode build|review"; exit 2;;
esac
[ -z "${EXTRA_TOOLS:-}" ] || tools="$tools,$EXTRA_TOOLS"   # P3c C5b: vd. Bash(KEEP=1 PYONLY=1 bash episodes/ep006/c5/checks_split.sh *)
cd "$(dirname "$0")/.."
ANTHROPIC_API_KEY="$CONSOLE_API_KEY" claude -p --model "$model" --output-format stream-json --verbose \
  --allowedTools "$tools" --disallowedTools "Task,Agent,Workflow" --max-budget-usd "$cap" --permission-mode dontAsk < "$brief" > "$log" 2> "${log%.jsonl}.err" || true
python3 - "$log" "$cap" <<'PY'
import json, sys
init = res = None; sub = []
for l in open(sys.argv[1]):
    try: d = json.loads(l)
    except Exception: continue
    if d.get('type') == 'system' and d.get('subtype') == 'init': init = d
    if d.get('type') == 'result': res = d
    if d.get('type') == 'assistant':
        sub += [c.get('name') for c in (d.get('message') or {}).get('content') or [] if c.get('type') == 'tool_use' and c.get('name') in ('Task', 'Agent', 'Workflow')]
print('apiKeySource:', init and init.get('apiKeySource'), '· công cụ:', ','.join(t for t in (init or {}).get('tools', []) if t in ('Task', 'Agent', 'Workflow')) or 'không Task/Agent/Workflow')
if res:
    u = res.get('usage', {})
    print(json.dumps({'turns': res.get('num_turns'), 'is_error': res.get('is_error'), 'cost_usd': res.get('total_cost_usd'),
                      'input': u.get('input_tokens'), 'cache_write': u.get('cache_creation_input_tokens'),
                      'cache_read': u.get('cache_read_input_tokens'), 'output': u.get('output_tokens')}))
    if res.get('subtype') == 'error_max_budget_usd' or (res.get('total_cost_usd') or 0) >= float(sys.argv[2]):
        print(f'TRẦN: lượt dừng ở trần chi ${sys.argv[2]} (subtype {res.get("subtype")})')
    print('--- trả về ---'); print(res.get('result', '')[-3000:])
if sub:
    print(f'CHẶN agent con: {len(sub)} lần gọi {sorted(set(sub))} (bị từ chối)'); sys.exit(5)
PY
