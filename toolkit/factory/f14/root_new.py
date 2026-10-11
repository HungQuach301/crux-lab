"""F-14 · bảng cổng gốc theo rubric MỚI (gates/C4-answer.md: chỉ advice_stated chặn), gộp thận trọng — như c4/ROOT-SUMMARY-P3c.md.
  python3 toolkit/factory/f14/root_new.py <thư mục lượt (episodes/ep006/c4/...)> [--json ra.json]
In mỗi nhịp: điểm (người đọc, thấp nhất qua 2 người chấm), cờ advice_stated, trạng thái (PASS/FAIL/cần người đọc thêm) — packets.beat_status."""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'blind'))
import packets  # noqa: E402
o = sys.argv[1]
key, rk = packets._load(os.path.join(o, 'KEY.json')), packets._load(os.path.join(o, 'rubric-key.json'))
scs = [packets._load(os.path.join(o, f)) for f in sorted(os.listdir(o)) if f.startswith('scores-g')]
r = packets._tally_one(key, rk, scs, 0.8, None, 'new')
for x in r['rows']:
    print(f"{x['id']}  {' · '.join(str(s) for s in x['scores']):16s} stated={x['advice']}  {x['status']}")
print(f"PASS {r['gate_pass']}/{r['gate_beats']} · chờ thêm người đọc: {r['pending']} · advice_stated: {r['advice_beats']} · verdict {r['verdict']}")
if '--json' in sys.argv:
    json.dump(r, open(sys.argv[sys.argv.index('--json') + 1], 'w'), indent=1, ensure_ascii=False)
