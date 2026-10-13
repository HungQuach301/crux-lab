"""F-15 · đo theo INTENT.md §3 (một cách đo cho mọi bản).

  python3 toolkit/factory/f15/measure.py times <tên bg …>                       giờ máy từ /var/tmp/crux-bg/<tên>.t0/.t1 (T3)
  python3 toolkit/factory/f15/measure.py bytes <bản sao làm việc> [<commit>]       spine.json ×N + out/factory/timeline.json + captions.srt so commit (T1)
  python3 toolkit/factory/f15/measure.py ssim <mới 1080.mp4> <ref 720.mp4> <timeline.json>   SSIM All trung bình + min theo cảnh (T2)
  python3 toolkit/factory/f15/measure.py checks <báo cáo nháp.json> <báo cáo 1080.json>       đồng phán quyết, bỏ sót CHẶN/CHÍNH ngoài R_pix (T5, T6)
In JSON một dòng; ghi kèm vào toolkit/factory/f15/out/ khi có --save <tệp>.
"""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
BG = os.environ.get('CRUX_BG', '/var/tmp/crux-bg')
R_PIX = set('A04 A13 F01 F05 F06 F07 F08 F10 S20 R07 V14 V08 V11 V12 R03 R04 R06 SH01 SH02 T1 V05 V09 V10 V13 P01'.split())   # INTENT §3 (ghi trước)


def times(names):
    out = {}
    for n in names:
        t0, t1 = (int(open(os.path.join(BG, f'{n}.{k}')).read()) if os.path.exists(os.path.join(BG, f'{n}.{k}')) else None for k in ('t0', 't1'))
        rc = open(os.path.join(BG, f'{n}.rc')).read().strip() if os.path.exists(os.path.join(BG, f'{n}.rc')) else None
        out[n] = {'wall_s': t1 - t0 if t0 and t1 else None, 'h': round((t1 - t0) / 3600, 3) if t0 and t1 else None, 'rc': rc}
    return out


def bytes_(wt, commit='c7358285'):
    import hashlib, yaml
    Y = yaml.safe_load(open(os.path.join(wt, 'episodes/ep007/episode.yaml')))
    files = [f"episodes/ep007/{w['dir']}/spine.json" for w in Y['world']] + ['episodes/ep007/out/factory/timeline.json', 'episodes/ep007/out/factory/captions.srt']
    rows, same = [], 0
    for f in files:
        ref = subprocess.run(['git', 'show', f'{commit}:{f}'], cwd=ROOT, capture_output=True).stdout
        cur = open(os.path.join(wt, f), 'rb').read()
        ok = ref == cur
        same += ok
        rows.append({'file': f, 'same': ok, 'sha_ref': hashlib.sha256(ref).hexdigest()[:12], 'sha_new': hashlib.sha256(cur).hexdigest()[:12]})
    return {'files': len(files), 'identical': same, 'rows': rows}


def ssim(new, ref, tl):
    log = os.path.join(HERE, 'out', 'ssim-frames.log')
    os.makedirs(os.path.dirname(log), exist_ok=True)
    r = subprocess.run(['ffmpeg', '-v', 'info', '-i', new, '-i', ref, '-lavfi',
                        f'[0:v]scale=1280:720:flags=bicubic,format=yuv420p,setpts=PTS-STARTPTS[a];[1:v]format=yuv420p,setpts=PTS-STARTPTS[b];[a][b]ssim=stats_file={log}',
                        '-f', 'null', '-'], capture_output=True, text=True)
    m = re.search(r'All:([0-9.]+)', r.stderr)
    per = []
    for ln in open(log):
        d = dict(kv.split(':') for kv in ln.split() if ':' in kv)
        per.append((int(d['n']), float(d['All'])))
    T = json.load(open(tl))
    fps = T.get('fps', 30)
    sc = []
    for s in T['scenes']:
        v = [a for n, a in per if s['start'] * fps <= n - 1 < (s['start'] + s['dur']) * fps]
        if v:
            sc.append({'scene': s['id'], 'mean': round(sum(v) / len(v), 4), 'min': round(min(v), 4)})
    return {'all_mean': float(m[1]) if m else None, 'frames': len(per), 'worst_scenes': sorted(sc, key=lambda x: x['mean'])[:5],
            'min_scene_mean': min(x['mean'] for x in sc) if sc else None}


def checks(draft, full):
    D = {r['id']: r for r in json.load(open(draft))['results']}
    F = {r['id']: r for r in json.load(open(full))['results']}
    ids = sorted(set(D) | set(F))
    agree = [i for i in ids if D.get(i, {}).get('status') == F.get(i, {}).get('status')]
    miss, miss_pix, extra = [], [], []
    for i in ids:
        f, d = F.get(i, {}), D.get(i, {})
        if f.get('tier') in ('BLOCK', 'MAJOR') and f.get('status') == 'FAIL' and d.get('status') != 'FAIL':
            (miss_pix if i in R_PIX else miss).append({'id': i, 'tier': f.get('tier'), '1080': f.get('status'), 'draft': d.get('status')})
        if d.get('status') == 'FAIL' and f.get('status') != 'FAIL':
            extra.append({'id': i, 'tier': d.get('tier'), '1080': f.get('status'), 'draft': d.get('status')})
    errs = lambda X: sorted(i for i, r in X.items() if r['status'] == 'ERROR')
    return {'rules': len(ids), 'agree': len(agree), 'agree_pct': round(100 * len(agree) / len(ids), 1), 'missed_block_major_outside_Rpix': miss,
            'missed_in_Rpix': miss_pix, 'draft_only_fail': extra, 'errors': {'draft': errs(D), '1080': errs(F)},
            'differ': [{'id': i, 'tier': (F.get(i) or D.get(i)).get('tier'), '1080': F.get(i, {}).get('status'), 'draft': D.get(i, {}).get('status'), 'R_pix': i in R_PIX}
                       for i in ids if i not in agree]}


def main():
    cmd, a = sys.argv[1], [x for x in sys.argv[2:] if not x.startswith('--')]
    save = sys.argv[sys.argv.index('--save') + 1] if '--save' in sys.argv else None
    a = [x for x in a if x != save]
    res = {'times': lambda: times(a), 'bytes': lambda: bytes_(*a), 'ssim': lambda: ssim(*a), 'checks': lambda: checks(*a)}[cmd]()
    if save:
        json.dump(res, open(save, 'w'), indent=1, ensure_ascii=False)
    print(json.dumps(res, ensure_ascii=False))


if __name__ == '__main__':
    main()
