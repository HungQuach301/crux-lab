"""K4.0 — chạy HỒI TỐ luật mới trên Tập 3–5 (và mẫu hiệu chuẩn), CHỈ BÁO: không sửa tập đã phát hành, không ghi vào cây tập.
  python3 checks-runs/K40/retro.py <luật,…> [--out checks-runs/K40/retro-<tên>.json] [--video <ep>=<mp4>] [--root <tên>=<dir>]
Mỗi gốc tập dựng lại trong thư mục tạm: liên kết mọi tệp của episodes/<ep>/ (trừ out/checks), out/checks/page.json lấy từ lần lấy mẫu trang
đã lưu (Tập 5: run-c5c, bản cuối C5c; Tập 3, Tập 4: không có page.json đã lưu → luật trang MISSING), hợp đồng hồi tố ở checks-runs/K40/contracts/.
"""
import gzip, json, os, shutil, sys, tempfile
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'checks', 'py'))
import common  # noqa: E402
import run as runner  # noqa: E402

PAGE = {'ep005': 'episodes/ep005/out/checks/run-c5c/page.json.gz'}
EPS = ['ep003', 'ep004', 'ep005']


def build(ep, src=None, video=None):
    src = src or os.path.join(ROOT, 'episodes', ep)
    d = tempfile.mkdtemp(prefix=f'k40-{ep}-')
    for n in os.listdir(src):
        if n != 'out':
            os.symlink(os.path.join(src, n), os.path.join(d, n))
    os.makedirs(os.path.join(d, 'out', 'checks'))
    if os.path.isdir(os.path.join(src, 'out')):
        for n in os.listdir(os.path.join(src, 'out')):
            if n != 'checks':
                os.symlink(os.path.join(src, 'out', n), os.path.join(d, 'out', n))
    if ep in PAGE:
        json.dump(json.load(gzip.open(os.path.join(ROOT, PAGE[ep]))), open(os.path.join(d, 'out/checks/page.json'), 'w'))
    if video:
        if os.path.lexists(os.path.join(d, 'out/video.mp4')):
            os.unlink(os.path.join(d, 'out/video.mp4'))
        os.symlink(os.path.abspath(video), os.path.join(d, 'out/video.mp4'))
    cache = os.path.join(ROOT, 'checks-runs', 'K40', 'cache', ep)   # ASR cache kept across runs (by video SHA)
    os.makedirs(cache, exist_ok=True)
    return d, cache


def main():
    a = sys.argv[1:]
    rules = a[0].split(',')
    out = a[a.index('--out') + 1] if '--out' in a else None
    videos = dict(x.split('=', 1) for i, x in enumerate(a) if i and a[i - 1] == '--video')
    roots = dict(x.split('=', 1) for i, x in enumerate(a) if i and a[i - 1] == '--root')
    eps = [x for i, x in enumerate(a) if i and not x.startswith('--') and a[i - 1] not in ('--out', '--video', '--root')] or EPS + list(roots)
    R = {fn.rid: fn for fn in common.RULES}
    res = {}
    for ep in eps:
        d, cache = build(ep, os.path.join(ROOT, roots[ep]) if ep in roots else None, videos.get(ep))
        c = os.path.join(ROOT, 'checks-runs', 'K40', 'contracts', f'{ep}.json')
        ctx = common.Ctx(d, cache=cache, contract=c if os.path.exists(c) else None)
        res[ep] = {'contract': os.path.relpath(c, ROOT) if os.path.exists(c) else 'episodes/%s/contract.json' % ep, 'video': videos.get(ep)}
        for rid in rules:
            r = common.safe(R[rid], ctx)
            res[ep][rid] = r
            print(f"{ep} {rid} {r['status']:7} " + '; '.join(f"{m['name']}={m['value']}" for m in r['metrics']) + (f"  {r['note']}" if r.get('note') else ''), flush=True)
        shutil.rmtree(d, ignore_errors=True)
    if out:
        json.dump(res, open(out, 'w'), indent=1, ensure_ascii=False, default=str)


if __name__ == '__main__':
    main()
