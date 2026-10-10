"""Tập 6 P3c: 4 số token của phiên chính từ nhật ký cục bộ (~/.claude/projects/<dự án>/<phiên>.jsonl), mỗi message id đếm một lần.
  python3 episodes/ep006/c5/session_tokens.py <phiên.jsonl>  → sinh ra · đầu vào mới (input + ghi cache) · đọc cache · trần (đầu vào mới + sinh ra) · ngữ cảnh cuối"""
import json, sys
seen, tot, last = set(), [0, 0, 0, 0], 0
for line in open(sys.argv[1]):
    try: d = json.loads(line)
    except Exception: continue
    m = d.get('message') or {}
    u, mid = m.get('usage'), m.get('id')
    if d.get('type') != 'assistant' or not u or mid in seen: continue
    seen.add(mid)
    v = [u.get('input_tokens', 0), u.get('cache_creation_input_tokens', 0), u.get('cache_read_input_tokens', 0), u.get('output_tokens', 0)]
    tot = [a + b for a, b in zip(tot, v)]; last = v[0] + v[1] + v[2]
out, new = tot[3], tot[0] + tot[1]
print(json.dumps({'lượt': len(seen), 'sinh_ra': out, 'đầu_vào_mới': new, 'đọc_cache': tot[2], 'trần': new + out, 'ngữ_cảnh_cuối': last}))
