"""Trích sự kiện `result` từ trang `list_events` đã lưu (JSON của công cụ phiên từ xa, kinds=["result"]) sang JSONL của token_log.py.
Mỗi trang: {"ccr": {"data": [{"created_at", "result": {"uuid", "internal_anthropic_catchall": {"modelUsage", "usage", "origin", ...}}}]}}
hoặc {"data": [...]}. Một dòng ra: s, uuid, t, origin, u=[in, ghi cache, đọc cache, ra] của lượt, mu={model: [...]} tích luỹ.
    python3 toolkit/usage/from_events.py --session session_XXX trang1.json [trang2.json …] > phien.jsonl
    python3 toolkit/usage/from_events.py --session session_XXX --close trang*.json   # 4 số cho PLAN mục 5 khi đóng phiên
"""
import json, sys

def rows(paths, sid):
    out = {}
    for p in paths:
        d = json.load(open(p))
        for e in (d.get('ccr', d)).get('data', []):
            r = e.get('result') or {}
            c = r.get('internal_anthropic_catchall') or r
            mu = {k: [v.get('inputTokens', 0), v.get('cacheCreationInputTokens', 0), v.get('cacheReadInputTokens', 0), v.get('outputTokens', 0)]
                  for k, v in (c.get('modelUsage') or {}).items()}
            u = c.get('usage') or {}
            out[r.get('uuid') or e.get('id')] = {
                's': sid, 'uuid': r.get('uuid') or e.get('id'), 't': e.get('created_at'), 'origin': (c.get('origin') or {}).get('kind'),
                'u': [u.get('input_tokens', 0), u.get('cache_creation_input_tokens', 0), u.get('cache_read_input_tokens', 0), u.get('output_tokens', 0)],
                'mu': mu}
    return sorted(out.values(), key=lambda d: d['t'] or '')

if __name__ == '__main__':
    a = sys.argv[1:]
    sid = a[a.index('--session') + 1] if '--session' in a else 'session'
    close = '--close' in a
    files = [x for i, x in enumerate(a) if not x.startswith('--') and (i == 0 or a[i - 1] != '--session')]
    R = rows(files, sid)
    if not close:
        for d in R:
            print(json.dumps(d, ensure_ascii=False))
        sys.exit(0)
    # tích luỹ cả phiên = sự kiện có trần lớn nhất (modelUsage tăng đơn điệu, gồm agent con)
    best = max(R, key=lambda d: sum(v[0] + v[1] + v[3] for v in d['mu'].values()), default=None)
    if not best:
        sys.exit('không có sự kiện result')
    c = [sum(v[i] for v in best['mu'].values()) for i in range(4)]
    f = lambda n: f'{n / 1e6:.2f}'  # noqa: E731
    print(f'Token phiên {sid} (log, đến {best["t"]}): sinh ra {f(c[3])} · đầu vào mới {f(c[0] + c[1])} · đọc cache {f(c[2])} · '
          f'trần {f(c[0] + c[1] + c[3])} triệu')
