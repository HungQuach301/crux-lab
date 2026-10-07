"""Nhà máy · TRANG KIỂM CỦA TẬP cho đoạn thế giới 3D (checks-appeal A11; hợp đồng window.CHECKS của checks/CONTRACT.md §Page).

  python3 toolkit/factory/world/episode_page.py <episode.yaml> [--out <html>] [--res 1080]

Sinh MỘT file HTML tự chứa (mở bằng file://, không máy chủ) mà bộ lấy mẫu trang của checks/ (checks/page/sampler.js) chạy được:
  - mọi module ES (three của vendor, toolkit/factory/world/{core,lib3d}.js, scene.js của mỗi đoạn `world:` và thư viện tập nó nhập) nhúng nguyên
    văn; chỉ chuỗi đặc tả import được thay bằng chỗ giữ __CRUXMOD_<i>__ → lúc chạy thành blob: URL, phụ thuộc trước (episode_page.js);
  - JSON mà scene.js nạp bằng loadJSON (chuỗi '/….json' trong mã, spine.json của đoạn, các .json của inputs.json) nhúng theo đường dẫn URL;
  - phông Inter (@font-face của page.html) nhúng data: URI;
  - claims (out/claims.json của tập: claimId, display) → khoảng claim trong chữ (core.claimSpans).
Đoạn: `world:` của episode.yaml + t0/t1 trong out/factory/timeline.json (`world`, sau splice) → seek(t) theo giờ của tập.
Ghi <episode>/out/page.json = {url, ready} (url tương đối gốc tập; ready = biểu thức chờ window.READY).
Giới hạn: chỉ khung của đoạn thế giới; khung 2D (shot của nhà máy 2D) chưa có window.CHECKS (checks-appeal A8) → objects() rỗng ở đó.
"""
import base64
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
VENDOR = os.path.join(HERE, 'vendor', 'node_modules', 'three')
IMPORT_RE = re.compile(r"""(\bfrom\s*|\bimport\s*\(\s*|\bimport\s+)(['"])([^'"\n]+)\2""")
JSON_RE = re.compile(r"""['"`](/[\w./-]+\.json)['"`]""")
READY = "new Promise((r) => { const k = () => (window.READY ? r(true) : setTimeout(k, 50)); k(); })"


def resolve(spec, importer):
    """Đặc tả import → đường dẫn file (như importmap của page.html: three, three/addons/…, '/…' từ gốc repo, './…' tương đối)."""
    if spec == 'three':
        return os.path.join(VENDOR, 'build', 'three.module.js')
    if spec.startswith('three/addons/'):
        return os.path.join(VENDOR, 'examples', 'jsm', spec[len('three/addons/'):])
    if spec.startswith('/'):
        return os.path.join(ROOT, spec.lstrip('/'))
    if spec.startswith('.'):
        return os.path.normpath(os.path.join(os.path.dirname(importer), spec))
    return None


def graph(entries):
    """Đồ thị module từ các file vào → (mods [{path, src (đã thay chỗ giữ)}], order (phụ thuộc trước), index {path: i})."""
    mods, index, order, state = [], {}, [], {}

    def visit(p):
        p = os.path.abspath(p)
        if state.get(p) == 'done':
            return index[p]
        if state.get(p) == 'open':
            raise SystemExit(f'episode_page: vòng import qua {os.path.relpath(p, ROOT)}')
        if not os.path.isfile(p):
            raise SystemExit(f'episode_page: không có module {p}')
        state[p] = 'open'
        i = index[p] = len(mods)
        mods.append({'path': p, 'src': None})
        src = open(p, encoding='utf-8').read()

        def sub(m):
            q = resolve(m.group(3), p)
            if not q or not os.path.isfile(q):
                return m.group(0)
            return f'{m.group(1)}{m.group(2)}__CRUXMOD_{visit(q)}__{m.group(2)}'
        mods[i]['src'] = IMPORT_RE.sub(sub, src)
        state[p] = 'done'
        order.append(i)
        return i
    for e in entries:
        visit(e)
    return mods, order, index


def fonts_css():
    """@font-face của page.html (Inter 400/600/700) với src = data: URI."""
    html = open(os.path.join(HERE, 'page.html'), encoding='utf-8').read()
    out = []
    for m in re.finditer(r'@font-face\{[^}]*\}', html):
        rule = m.group(0)
        u = re.search(r'url\(([^)]+)\)', rule).group(1).strip('\'"')
        b = base64.b64encode(open(os.path.join(ROOT, u.lstrip('/')), 'rb').read()).decode()
        out.append(rule.replace(f'url({u})', f'url(data:font/woff2;base64,{b})'))
    return '\n'.join(out)


def collect_json(mods, seg_dirs):
    want = set()
    for m in mods:
        want |= {j for j in JSON_RE.findall(m['src']) if os.path.isfile(os.path.join(ROOT, j.lstrip('/')))}
    for d in seg_dirs:
        rel = '/' + os.path.relpath(d, ROOT)
        want.add(rel + '/spine.json')
        inp = os.path.join(d, 'inputs.json')
        if os.path.exists(inp):
            want |= {'/' + x.lstrip('/') for x in json.load(open(inp)) if x.endswith('.json')}
    return {j: open(os.path.join(ROOT, j.lstrip('/')), encoding='utf-8').read() for j in sorted(want) if os.path.isfile(os.path.join(ROOT, j.lstrip('/')))}


def build(segs, claims, out_html, fps=30, view=None):
    """segs: [{id, dir (thư mục đoạn), t0, t1}] (giây của tập); claims: [{id, display}]. Ghi out_html, trả thông tin."""
    core = os.path.join(HERE, 'core.js')
    entries = [core] + [os.path.join(s['dir'], 'scene.js') for s in segs]
    mods, order, index = graph(entries)
    data = {'mods': [{'src': m['src']} for m in mods], 'order': order, 'core': index[os.path.abspath(core)], 'fps': fps,
            'segs': [{'id': s['id'], 'mod': index[os.path.abspath(os.path.join(s['dir'], 'scene.js'))], 't0': s['t0'], 't1': s['t1']} for s in segs],
            'json': collect_json(mods, [s['dir'] for s in segs]), 'claims': claims, 'view': view}
    blob = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
    runtime = open(os.path.join(HERE, 'episode_page.js'), encoding='utf-8').read()
    html = ('<!doctype html>\n<html><head><meta charset="utf-8"><title>Crux · trang kiểm của tập (window.CHECKS)</title>\n<style>\n' + fonts_css() +
            '\nhtml,body{margin:0;background:transparent;overflow:hidden} canvas{position:absolute;left:0;top:0}\n</style>\n'
            f'<script>window.__CRUX = {blob};</script>\n</head><body>\n<script type="module">\n{runtime}\n</script>\n</body></html>\n')
    os.makedirs(os.path.dirname(out_html), exist_ok=True)
    open(out_html, 'w', encoding='utf-8').write(html)
    return {'modules': len(mods), 'json': sorted(data['json']), 'segments': [s['id'] for s in segs], 'bytes': len(html.encode())}


def episode_segments(ep_root, Y, timeline):
    """`world:` của episode.yaml + t0/t1 của timeline (out/factory/timeline.json, mục `world` sau splice, hoặc cảnh)."""
    W = {w['id']: w for w in timeline.get('world') or []}
    sc = {s['id']: s for s in timeline['scenes']}
    out = []
    for w in Y.get('world') or []:
        t0, t1 = (W[w['id']]['t0'], W[w['id']]['t1']) if w['id'] in W else (sc[w['scenes'][0]]['start'], sc[w['scenes'][-1]]['start'] + sc[w['scenes'][-1]]['dur'])
        out.append({'id': w['id'], 'dir': os.path.join(ep_root, w['dir']), 't0': round(t0, 4), 't1': round(t1, 4)})
    return out


def write_episode(ep_root, Y, timeline, claims_file, out_html, fps=30):
    """Trang kiểm + <tập>/out/page.json. claims_file: out/claims.json (hoặc `claims:` của episode.yaml)."""
    cl = json.load(open(claims_file))['claims'] if claims_file and os.path.exists(claims_file) else []
    info = build(episode_segments(ep_root, Y, timeline), [{'id': c['claimId'], 'display': c.get('display')} for c in cl], out_html, fps)
    pj = {'url': os.path.relpath(out_html, ep_root), 'ready': READY, '_about': 'toolkit/factory/world/episode_page.py: trang một-file, window.CHECKS trên mọi đoạn world:'}
    os.makedirs(os.path.join(ep_root, 'out'), exist_ok=True)
    json.dump(pj, open(os.path.join(ep_root, 'out', 'page.json'), 'w'), indent=1, ensure_ascii=False)
    return {**info, 'page': pj['url']}


def main():
    import yaml
    yml = os.path.abspath(sys.argv[1])
    ep = os.path.dirname(yml)
    Y = yaml.safe_load(open(yml))
    tl = json.load(open(os.path.join(ep, 'out', 'factory', 'timeline.json')))
    out = os.path.abspath(sys.argv[sys.argv.index('--out') + 1]) if '--out' in sys.argv else os.path.join(ep, 'work', 'factory', 'page', 'index.html')
    cf = os.path.join(ep, 'out', 'claims.json')
    if not os.path.exists(cf):
        cf = os.path.join(ep, Y['claims'])
    print(json.dumps(write_episode(ep, Y, tl, cf, out, Y.get('fps', 30)), ensure_ascii=False)[:600])


if __name__ == '__main__':
    main()
