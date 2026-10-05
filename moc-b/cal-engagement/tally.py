"""Gộp điểm hiệu chuẩn theo INTENT.md (không đổi ngưỡng)."""
import json, os
R = os.path.dirname(os.path.abspath(__file__))
key = {k['file']: k for k in json.load(open(f'{R}/key.json'))}
ans = [json.loads(l) for l in open(f'{R}/answers.jsonl')]
def pos(ep, ver, sid):
    L = [l.split(' ', 2) for l in open(f'{R}/{ver}-{ep}.txt') if l.strip()]
    tot = sum(len(x[2].split()) for x in L); acc = 0
    if sid in (None, 'NONE'): return 100.0
    for x in L:
        acc += len(x[2].split())
        if x[0] == sid: return 100 * acc / tot
    raise SystemExit(f'unknown id {sid} in {ver}-{ep}')
res = {}; lines = ['# Kết quả hiệu chuẩn bộ đo hấp dẫn (ngưỡng theo INTENT.md)', '', '| Tập | Bản | Móc (từng người) | TB móc | Vị trí bỏ xem % (từng người) | TB bỏ xem % |', '|---|---|---|---|---|---|']
for ep in ['ep002', 'ep003']:
    r = res[ep] = {}
    for ver in ['orig', 'degr']:
        a = [x for x in ans if key[x['file']]['kind'] == 'full' and key[x['file']]['ep'] == ep and key[x['file']]['ver'] == ver]
        hooks = [x['HOOK'] for x in a]; stops = [round(pos(ep, ver, x['STOP']), 1) for x in a]
        r[ver] = (sum(hooks) / len(hooks), sum(stops) / len(stops))
        lines.append(f'| {ep} | {ver} | {hooks} | {r[ver][0]:.2f} | {stops} | {r[ver][1]:.1f} |')
    pr = [x for x in ans if key[x['file']]['kind'] == 'pair' and key[x['file']]['ep'] == ep]
    r['pair'] = sum(1 for x in pr if key[x['file']][x['KEEP']] == 'orig'); r['npair'] = len(pr)
lines += ['', '| Tập | Δ móc (gốc − kém) | so cặp chọn gốc | móc tách được? | Δ bỏ xem (điểm %) | bỏ xem tách được? |', '|---|---|---|---|---|---|']
ok_h = ok_s = True
for ep, r in res.items():
    dh = r['orig'][0] - r['degr'][0]; ds = r['orig'][1] - r['degr'][1]
    h = dh >= 1.0 and r['pair'] >= 2; s = ds >= 15; ok_h &= h; ok_s &= s
    lines.append(f"| {ep} | {dh:+.2f} | {r['pair']}/{r['npair']} | {'CÓ' if h else 'KHÔNG'} | {ds:+.1f} | {'CÓ' if s else 'KHÔNG'} |")
lines += ['', f"**Bộ đo móc (điểm 1–5 tuyệt đối + so cặp): {'ĐẠT' if ok_h else 'KHÔNG ĐẠT'}** · **Bộ đo bỏ xem: {'ĐẠT' if ok_s else 'KHÔNG ĐẠT'}**"]
open(f'{R}/RESULT.md', 'w').write('\n'.join(lines) + '\n'); print('\n'.join(lines))
