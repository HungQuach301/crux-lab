"""F-14 · bản sao CÁCH ĐO hình của checks R07 (checks/py/r_k40.py r07_sync, khoá 4d688acd) để lặp nhanh ở bản nháp — KHÔNG thay luật:
số chính vẫn là checks run đủ bộ. Khác duy nhất: chữ nhãn đọc từ nhật ký trang của render (<seg>.log.json: chữ opacity > 0,5) thay cho textTrack
của bộ lấy mẫu trang (cùng tiêu chí opacity > 0,5, mẫu 0,1 s); hoặc từ page.json(.gz) của một checks run (--page). Không đo phần giọng (ASR).
  python3 toolkit/factory/f14/r07_local.py <master.mp4> <thư mục đoạn> <ra.json> [--page page.json(.gz)] [--logs <thư mục *.log.json theo tên đoạn>]
       [--like <r07.json của bản giao>]   # INTENT §8 đọc chặt: CHỈ cue của bản giao, mỗi cue đo đúng cách bản giao đo nó (label/motion); thiếu cue = trượt
"""
import gzip, json, os, subprocess, sys
import numpy as np


def diffs(video, w=320, h=180, fps=30):
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', video, '-vf', f'fps={fps},scale={w}:{h},format=gray', '-f', 'rawvideo', '-'], stdout=subprocess.PIPE)
    mean, prev, n = [0.0], None, w * h
    while True:
        b = p.stdout.read(n)
        if len(b) < n: break
        fr = np.frombuffer(b, np.uint8).astype(np.int16)
        if prev is not None: mean.append(float(np.abs(fr - prev).mean()))
        prev = fr
    p.wait()
    return np.array(mean)


def main():
    video, sdir, out = sys.argv[1:4]
    a = sys.argv
    page = a[a.index('--page') + 1] if '--page' in a else None
    logd = a[a.index('--logs') + 1] if '--logs' in a else None
    cache = video + '.diff.npy'
    d = np.load(cache) if os.path.exists(cache) and os.path.getmtime(cache) > os.path.getmtime(video) else diffs(video)
    np.save(cache, d)
    like = None
    if '--like' in a:
        like = {(v['segment'], v['cue']): v['how'] for v in json.load(open(a[a.index('--like') + 1]))['all']}
    tt = None
    if page:
        pj = json.load(gzip.open(page) if page.endswith('.gz') else open(page))
        tt = pj.get('textTrack')
    vis = []
    for name in sorted(os.listdir(sdir)):
        spf = os.path.join(sdir, name, 'spine.json')
        if not os.path.exists(spf): continue
        sp = json.load(open(spf)); t0 = sp.get('episode_t0', 0.0)
        cues = {f"{b['id']}.{k}": t for b in sp.get('beats', []) for k, t in b.get('cues', {}).items()}
        moves = [(m['t0'] + t0, m['t1'] + t0) for m in sp.get('moves', [])]
        labels = sp.get('label_cues') or {}
        log = None
        if logd and os.path.exists(os.path.join(logd, name + '.log.json')):
            log = sorted(json.load(open(os.path.join(logd, name + '.log.json'))), key=lambda l: l['t'])
        names = sp.get('visual_cues') or []
        if like is not None:
            names = [c for (sg, c) in like if sg == name]
        for cn in names:
            if cn not in cues:
                vis.append({'segment': name, 'cue': cn, 'offset': None, 'how': 'cue not in beats'}); continue
            t = cues[cn] + t0
            method = like.get((name, cn)) if like is not None else None
            if (cn in labels if method is None else method == 'label') and (tt or log):
                if tt:
                    first = None if cn not in labels else next((e['t'] for e in tt if e['t'] >= t - 1.0 and any(i.get('text') == labels[cn] for i in e.get('items', []))), None)
                else:
                    first = None if cn not in labels else next((l['t'] + t0 for l in log if l['t'] + t0 >= t - 1.0 and any(x['text'] == labels[cn] and x['opacity'] > 0.5 for x in l['texts'])), None)
                vis.append({'segment': name, 'cue': cn, 't': round(t, 3), 'offset': None if first is None else round(first - t, 3), 'how': 'label'}); continue
            end, st = t + 0.8, t - 0.3
            for x, y in moves:
                if t < x < end: end = x
                if st < y <= t: st = y + 1 / 30
            base = float(np.median(d[max(0, int((t - 0.7) * 30)):max(1, int((t - 0.15) * 30))]))
            i0, i1 = int(st * 30), int(end * 30)
            seg = d[i0:i1]
            if len(seg) == 0 or seg.max() - base < 0.08:
                vis.append({'segment': name, 'cue': cn, 't': round(t, 3), 'offset': None, 'how': 'motion', 'peak': round(float(seg.max() - base), 3) if len(seg) else None}); continue
            on = int(np.argmax(seg > base + 0.5 * (seg.max() - base)))
            vis.append({'segment': name, 'cue': cn, 't': round(t, 3), 'offset': round(i0 / 30 + on / 30 - t, 3), 'how': 'motion'})
    ok = [v for v in vis if v['offset'] is not None and abs(v['offset']) <= 0.2]
    res = {'cues': len(vis), 'within': len(ok), 'share': round(100 * len(ok) / max(1, len(vis)), 1),
           'miss': [v for v in vis if v['offset'] is None or abs(v['offset']) > 0.2], 'all': vis}
    json.dump(res, open(out, 'w'), indent=1, ensure_ascii=False)
    print(f"R07 (hình, bản sao cách đo): {res['within']}/{res['cues']} = {res['share']} %")
    for v in res['miss']:
        print(f"  {v['segment'][:1]} {v['cue']:16s} @{v.get('t', 0):7.2f}  {v['how']:6s} lệch {v['offset']}" + (f" (đỉnh {v.get('peak')})" if 'peak' in v else ''))


if __name__ == '__main__':
    main()
