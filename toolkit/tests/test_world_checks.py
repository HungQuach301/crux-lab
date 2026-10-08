"""Test trang kiểm của đoạn thế giới (checks-appeal A11; hợp đồng window.CHECKS của checks/CONTRACT.md §Page) + khung dọc (Shorts) của core.js.
Hai đoạn giả (three thật của vendor, Chromium của Playwright; bỏ qua nếu thiếu), gói bằng toolkit/factory/world/episode_page.py:
(a) seek(t) chọn đúng đoạn theo giờ của tập; objects(): chữ (role, hộp, khoảng claim khớp display; o.claims giới hạn claim), huy hiệu ILLUSTRATIVE (role badge),
    hình 3D khai userData.checks (role, case, hộp chiếu), nét lớp phủ (role line), O.shape (toạ độ thế giới → hộp).
(b) layer(): 'text' nền trong suốt chỉ có chữ; 'graphics' có hình 3D, không chữ, không sàn/nền; 'only' chỉ id đã chọn; 'all' như seek.
(c) freeze(t): máy quay giữ trạng thái khung t (hộp của hình 3D không đổi khi seek t khác), freeze(null) thả.
(d) bộ lấy mẫu trang KHOÁ của checks/ (checks/page/sampler.js) chạy trên gốc giả 3 s: thoát 0, page.json có các luật trang, casesTrack.
(e) khung dọc (CK.view): canvas 1080×1920; chữ cảnh ≥ 56 px, trong vùng an toàn dọc; khung có số mang ILLUSTRATIVE + HISTORY + một đối trọng.
"""
import json, os, shutil, subprocess, sys, tempfile, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
WORLD = os.path.join(ROOT, 'toolkit', 'factory', 'world')
sys.path.insert(0, WORLD)
sys.dont_write_bytecode = True
import episode_page as EP  # noqa: E402

SCENE = r"""
import * as THREE from 'three';
import { Stage } from '/toolkit/factory/world/core.js';
export async function boot(res) {
  const st = Stage(res), { renderer, O } = st, scene = new THREE.Scene(); scene.background = new THREE.Color('#0E1116');
  const floor = new THREE.Mesh(new THREE.PlaneGeometry(60, 60), new THREE.MeshStandardMaterial({ color: '#30343c' })); floor.rotation.x = -Math.PI / 2; floor.userData.role = 'bg'; scene.add(floor);
  scene.add(new THREE.HemisphereLight('#ffffff', '#222222', 1.2));
  const bar = new THREE.Mesh(new THREE.BoxGeometry(2, 2, 0.2), new THREE.MeshBasicMaterial({ color: '#4C8DFF' })); bar.position.set(0, 1, 0);
  bar.userData.checks = { role: 'bar', case: 'CASE', chart: 'c1', key: 'bar1' }; scene.add(bar);
  const cam = new THREE.PerspectiveCamera(35, 16 / 9, 0.1, 100);
  function frame(t) {
    cam.position.set(t * 2, 2, 10); cam.lookAt(t * 2, 1, 0); cam.updateMatrixWorld(); renderer.render(scene, cam);
    const log = O.begin(t, 1, cam);
    O.text('LABEL 23 months', 300, 300, 40, { kind: 'number' });
    O.text('2 of 23 months', 120, 200, 48, { claims: ['n2'] });
    O.text('ILLUSTRATIVE', 1824, 108, 54, { kind: 'chrome', color: '#1B1F26', plate: '#F2B441' });
    const [x, y] = O.toScreen(0, 2.6, 0); O.ctx.save(); O.ctx.strokeStyle = '#9AA4B2'; O.ctx.lineWidth = 4; O.ctx.beginPath(); O.ctx.moveTo(x - 100, y); O.ctx.lineTo(x + 100, y); O.ctx.stroke(); O.ctx.restore();
    O.shape({ role: 'mark', world: [[3, 0, 0], [3, 1, 0]], case: 'MARK', key: 'm1' });
    O.chrome({ hist: true });
    st.compose(); return log;
  }
  return { canvas: st.out, frame };
}
"""

PROBE = r"""
const { chromium } = require('playwright');
(async () => {
  const [html, mode] = process.argv.slice(2);
  const b = await chromium.launch({ args: ['--font-render-hinting=none', '--disable-lcd-text'] });
  const vertical = mode === 'v';
  const p = await b.newPage({ viewport: vertical ? { width: 1080, height: 1920 } : { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  const errs = []; p.on('pageerror', (e) => errs.push(e.message));
  await p.goto('file://' + html + (vertical ? '?res=1920' : ''));
  await p.evaluate("new Promise((r) => { const k = () => (window.READY ? r(true) : setTimeout(k, 50)); k(); })");
  const ev = (f, a) => p.evaluate(f, a);
  const px = async (name, ids) => { await ev(([n, i]) => window.CHECKS.layer(n, i), [name, ids || []]);
    const { PNG } = { PNG: null }; const buf = await p.screenshot({ omitBackground: true, type: 'png' }); await ev(() => window.CHECKS.layer('all')); return buf.toString('base64'); };
  const out = { errs };
  if (vertical) {
    await ev(() => window.CHECKS.seek(0.5)); out.v = await ev(() => window.CHECKS.log().v);
    out.size = await ev(() => { const c = [...document.querySelectorAll('canvas')].find((x) => x.style.display !== 'none'); return [c.width, c.height]; });
  } else {
    await ev(() => window.CHECKS.seek(0.5)); out.a = await ev(() => window.CHECKS.objects());
    out.text = await px('text'); out.gfx = await px('graphics');
    const id = out.a.find((o) => o.kind === 'text' && o.text.startsWith('seg')).id; out.only = await px('only', [id]);
    out.all = (await p.screenshot({ type: 'png' })).toString('base64');
    await ev(() => window.CHECKS.seek(2.5)); out.b = await ev(() => window.CHECKS.objects());
    await ev(() => window.CHECKS.seek(1.0)); out.moved = await ev(() => window.CHECKS.objects());
    await ev(() => window.CHECKS.freeze(0.5)); await ev(() => window.CHECKS.seek(1.0)); out.frozen = await ev(() => window.CHECKS.objects()); await ev(() => window.CHECKS.freeze(null));
    await ev(() => window.CHECKS.seek(1.0)); out.released = await ev(() => window.CHECKS.objects());
  }
  console.log(JSON.stringify(out)); await b.close();
})().catch((e) => { console.error(e); process.exit(1); });
"""


def node_env():
    node = shutil.which('node')
    if not node or not os.path.isdir(os.path.join(WORLD, 'vendor', 'node_modules', 'three')):
        return None
    npm = subprocess.run(['npm', 'root', '-g'], capture_output=True, text=True).stdout.strip()
    if not os.path.isdir(os.path.join(npm, 'playwright')):
        return None
    return {**os.environ, 'NODE_PATH': npm}


def png(b64):
    import base64, io
    from PIL import Image
    import numpy as np
    return np.asarray(Image.open(io.BytesIO(base64.b64decode(b64))).convert('RGBA'))


def make_segments(d):
    segs = []
    for k, (t0, t1, label) in enumerate([(0.0, 2.0, 'A'), (2.0, 4.0, 'B')]):
        sd = os.path.join(d, f'seg{label}'); os.makedirs(sd)
        open(os.path.join(sd, 'scene.js'), 'w').write(SCENE.replace('CASE', f'case-{label}').replace('LABEL', f'seg{label}'))
        segs.append({'id': f'seg{label}', 'dir': sd, 't0': t0, 't1': t1})
    return segs


class ChecksPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.env = node_env()
        if cls.env is None:
            return
        cls.d = tempfile.mkdtemp()
        cls.segs = make_segments(cls.d)
        cls.html = os.path.join(cls.d, 'page', 'index.html')
        cls.info = EP.build(cls.segs, [{'id': 'm23', 'display': '23 months'}, {'id': 'n2', 'display': '2'}], cls.html)
        open(os.path.join(cls.d, 'probe.js'), 'w').write(PROBE)
        r = subprocess.run(['node', os.path.join(cls.d, 'probe.js'), cls.html, 'h'], env=cls.env, capture_output=True, text=True, timeout=300)
        if r.returncode:
            raise AssertionError(r.stderr[-3000:])
        cls.R = json.loads(r.stdout.strip().splitlines()[-1])

    @classmethod
    def tearDownClass(cls):
        if getattr(cls, 'd', None):
            shutil.rmtree(cls.d, ignore_errors=True)

    def setUp(self):
        if self.env is None:
            self.skipTest('node / playwright / vendor three không có')

    def test_a_objects(self):
        R = self.R
        self.assertEqual(R['errs'], [])
        self.assertEqual(self.info['modules'], 5)   # three.module, three.core, core.js, 2 scene.js
        T = {o['text']: o for o in R['a'] if o['kind'] == 'text'}
        lab = T['segA 23 months']
        self.assertEqual(lab['role'], 'label'); self.assertEqual(lab['fontPx'], 40)
        self.assertEqual([c['id'] for c in lab['claims']], ['m23'])           # '2' không khớp bên trong '23'
        cb, tb = lab['claims'][0]['box'], lab['box']
        self.assertGreater(cb[0], tb[0] + 50); self.assertAlmostEqual(cb[2], tb[2], delta=1)   # khoảng claim = phần cuối của chữ
        self.assertEqual([c['id'] for c in T['2 of 23 months']['claims']], ['n2'])   # o.claims: only these claim ids
        self.assertEqual(T['ILLUSTRATIVE']['role'], 'badge'); self.assertEqual(T['ILLUSTRATIVE']['background'], '#f2b441')
        self.assertIn('US only · history, not a forecast', T)
        bar = next(o for o in R['a'] if o.get('case') == 'case-A')
        self.assertEqual((bar['kind'], bar['role'], bar['chart']), ('shape', 'bar', 'c1'))
        self.assertTrue(0 < bar['box'][0] < bar['box'][2] < 1920 and 0 < bar['box'][1] < bar['box'][3] < 1080)
        self.assertTrue(any(o['kind'] == 'shape' and o['role'] == 'line' and o['stroke'] == '#9aa4b2' for o in R['a']))
        mk = next(o for o in R['a'] if o.get('case') == 'MARK'); self.assertGreater(mk['box'][3] - mk['box'][1], 20)
        ns = [o['id'] for o in R['a']]; self.assertEqual(len(ns), len(set(ns)))
        # seek 2.5 → đoạn B (giờ của tập), đoạn B ở giờ đoạn 0.5
        self.assertTrue(any(o.get('text') == 'segB 23 months' for o in R['b']))
        self.assertTrue(any(o.get('case') == 'case-B' for o in R['b']))

    def test_b_layers(self):
        import numpy as np
        R = self.R
        txt, gfx, only, allp = png(R['text']), png(R['gfx']), png(R['only']), png(R['all'])
        lab = next(o for o in R['a'] if o.get('text') == 'segA 23 months')['box']
        bar = next(o for o in R['a'] if o.get('case') == 'case-A')['box']
        crop = lambda im, b: im[int(b[1]):int(b[3]), int(b[0]):int(b[2])]
        self.assertEqual(int(txt[5, 5, 3]), 0)                                  # nền trong suốt
        self.assertGreater(int(crop(txt, lab)[..., 3].max()), 200)              # chữ có ở lớp text
        self.assertEqual(int(crop(txt, bar)[..., 3].max()), 0)                  # không có hình 3D ở lớp text
        self.assertGreater(float((crop(gfx, bar)[..., 3] > 200).mean()), 0.9)   # hình 3D ở lớp graphics
        self.assertEqual(int(crop(gfx, lab)[..., 3].max()), 0)                  # không chữ ở lớp graphics
        self.assertEqual(int(gfx[1070, 5, 3]), 0)                               # sàn (role bg) + nền bỏ
        self.assertGreater(int(crop(only, lab)[..., 3].max()), 200)
        self.assertEqual(int(only[60:130, 1400:1830, 3].max()), 0)              # ILLUSTRATIVE không ở 'only'
        self.assertEqual(int(allp[..., 3].min()), 255)                          # 'all' đục

    def test_c_freeze(self):
        R = self.R
        box = lambda objs: next(o for o in objs if o.get('case') == 'case-A')['box']
        self.assertNotEqual(box(R['a']), box(R['moved']))                       # máy quay chạy theo t
        self.assertEqual(box(R['a']), box(R['frozen']))                         # freeze(0.5): seek(1.0) giữ máy quay của 0.5
        self.assertEqual(box(R['moved']), box(R['released']))

    def test_d_locked_sampler(self):
        """checks/page/sampler.js (khoá, không sửa) trên gốc giả 3 s: không lỗi, page.json có các luật trang."""
        import numpy as np
        root = os.path.join(self.d, 'root'); os.makedirs(os.path.join(root, 'out')); os.makedirs(os.path.join(root, 'design'))
        J = lambda p, x: json.dump(x, open(os.path.join(root, p), 'w'))
        J('out/timeline.json', {'fps': 30, 'total': 3.0, 'acts': [{'id': 'act1', 'start': 0, 'end': 3.0}],
                                'scenes': [{'id': 'S01', 'act': 'act1', 'start': 0.0, 'dur': 2.0}, {'id': 'S02', 'act': 'act1', 'start': 2.0, 'dur': 1.0}]})
        J('out/claims.json', {'claims': [{'claimId': 'm23', 'display': '23 months', 'value': 23, 'illustrative': True}]})
        J('design/tokens.json', {'colors': {'bg': '#0e1116', 'grid': '#2a303b', 'muted': '#9aa4b2'}, 'series': {}})
        J('contract.json', {'episode': 'x'})
        J('out/page.json', {'url': os.path.relpath(self.html, root), 'ready': EP.READY})
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'lavfi', '-i', 'color=c=0x0e1116:s=1920x1080:r=30:d=3', '-pix_fmt', 'yuv420p', '-c:v', 'libx264',
                        os.path.join(root, 'out', 'video.mp4')], check=True)
        r = subprocess.run(['node', os.path.join(ROOT, 'checks', 'page', 'sampler.js'), root, '--jobs', '1'], env=self.env, capture_output=True, text=True, timeout=900)
        self.assertEqual(r.returncode, 0, r.stderr[-2000:])
        P = json.load(open(os.path.join(root, 'out', 'checks', 'page.json')))
        for k in ('C07', 'S08', 'S09', 'S17', 'V11', 'V12'):
            self.assertIn(k, P['rules'])
        self.assertEqual(P['samples'], 30)
        self.assertEqual(P['rules']['S08']['framesWithout'], 0)                # badge on every frame with the illustrative claim
        self.assertIn('m23', P['claimScenes'])
        self.assertTrue(any('case-A' in c['cases'] for c in P['casesTrack']) and any('case-B' in c['cases'] for c in P['casesTrack']))
        self.assertTrue(any('history, not a forecast' in i['text'] for e in P['textTrack'] for i in e['items']))

    def test_e_vertical(self):
        html = os.path.join(self.d, 'pagev', 'index.html')
        EP.build(self.segs, [], html, view={'orient': 'v', 's': 1, 'hook': 'A hook line', 'cws': [{'id': 'cw1', 'text': 'A measurement, not a next step'}], 't0': 0})
        r = subprocess.run(['node', os.path.join(self.d, 'probe.js'), html, 'v'], env=self.env, capture_output=True, text=True, timeout=300)
        self.assertEqual(r.returncode, 0, r.stderr[-2000:])
        R = json.loads(r.stdout.strip().splitlines()[-1])
        self.assertEqual(R['errs'], []); self.assertEqual(R['size'], [1080, 1920])
        V = R['v']
        for x in V['texts']:
            self.assertGreaterEqual(x['px'], 56 - 0.01, x)
            b = x['box']; self.assertTrue(72 - 1 <= b[0] and b[2] <= 1008 + 1 and 200 - 1 <= b[1] and b[3] <= 1600 + 1, x)
        self.assertTrue(any(r['s'] == 'segA 23 months' and r['to'] == 56 for r in V['raised']))   # 40 px → 56 px
        self.assertEqual(set(V['tags']), {'ILLUSTRATIVE', 'HISTORY', 'CW:cw1'})
        self.assertTrue(V['illus'] and V['hist'])
        self.assertTrue(any(x['s'] == 'A hook line' for x in V['texts']))


if __name__ == '__main__':
    unittest.main()
