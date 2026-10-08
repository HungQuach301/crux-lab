"""Test core.js — sửa C5b (Tập 5, lượt sửa checks C5):
(a) khung ngang: chữ cảnh tràn ít khỏi vùng an toàn 90 % được đẩy vào (V03), chữ đang bay xa ngoài khung không bị kéo lại;
    lớp bắt buộc (ILLUSTRATIVE, dòng đối trọng/history) nằm trong vùng an toàn; nhãn gốc tính tiền cấp khung `basis` (S09, K3.3).
(b) lớp chẩn đoán 'graphics3d' (chỉ hình 3D) và 'graphics2d' (chỉ nét lớp phủ) — tách va chạm chữ×3D khỏi chữ×nét 2D (V11).
(c) khung dọc (Short): chữ cảnh xếp chỗ không giao nhau (chữ lớn dịch dọc, nhãn trục nhỏ giao thì bỏ); khung có dòng history luôn có ILLUSTRATIVE;
    `basis` thành một dòng dưới (tag BASIS).
"""
import json, os, re, shutil, subprocess, sys, tempfile, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True
from test_world_checks import EP, node_env, png  # noqa: E402

SCENE = r"""
import * as THREE from 'three';
import { Stage } from '/toolkit/factory/world/core.js';
export async function boot(res) {
  const st = Stage(res), { renderer, O } = st, scene = new THREE.Scene(); scene.background = new THREE.Color('#0E1116');
  scene.add(new THREE.HemisphereLight('#ffffff', '#222222', 1.2));
  const bar = new THREE.Mesh(new THREE.BoxGeometry(2, 2, 0.2), new THREE.MeshBasicMaterial({ color: '#4C8DFF' })); bar.position.set(0, 1, 0); scene.add(bar);
  const cam = new THREE.PerspectiveCamera(35, 16 / 9, 0.1, 100); cam.position.set(0, 2, 10); cam.lookAt(0, 1, 0); cam.updateMatrixWorld();
  function frame(t) {
    renderer.render(scene, cam);
    const log = O.begin(t, 1, cam);
    O.text('EDGE LEFT', 60, 500, 48);
    O.text('EDGE RIGHT', 1550, 420, 48);
    O.text('FAR OUT', -400, 600, 48);
    if (t < 1) { O.text('Big label one', 700, 760, 60); O.text('Big label two', 700, 790, 60); O.text('1991', 760, 770, 40, { kind: 'number', role: 'axis-label' }); O.text('2005', 1000, 775, 48, { kind: 'number', role: 'axis-label' }); }
    else O.text('Only words here', 700, 760, 60);
    O.ctx.save(); O.ctx.strokeStyle = '#9AA4B2'; O.ctx.lineWidth = 6; O.ctx.beginPath(); O.ctx.moveTo(1300, 300); O.ctx.lineTo(1700, 300); O.ctx.stroke(); O.ctx.restore();
    O.chrome({ illus: t < 1, cw: 'A measurement, not a next step', hist: t >= 1, basis: 'nominal' });
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
  const shot = async (name) => { await ev((n) => window.CHECKS.layer(n), name); const buf = await p.screenshot({ omitBackground: true, type: 'png' }); await ev(() => window.CHECKS.layer('all')); return buf.toString('base64'); };
  const out = { errs };
  if (vertical) {
    await ev(() => window.CHECKS.seek(0.5)); out.v0 = await ev(() => window.CHECKS.log().v);
    await ev(() => window.CHECKS.seek(1.5)); out.v1 = await ev(() => window.CHECKS.log().v);
  } else {
    await ev(() => window.CHECKS.seek(0.5)); out.a = await ev(() => window.CHECKS.objects());
    out.g3 = await shot('graphics3d'); out.g2 = await shot('graphics2d'); out.g = await shot('graphics');
    await ev(() => window.CHECKS.seek(1.5)); out.b = await ev(() => window.CHECKS.objects());
  }
  console.log(JSON.stringify(out)); await b.close();
})().catch((e) => { console.error(e); process.exit(1); });
"""

SAFE = (96, 54, 1824, 1026)


def inter(a, b):
    return min(a[2], b[2]) - max(a[0], b[0]) > 1 and min(a[3], b[3]) - max(a[1], b[1]) > 1


class C5bCore(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.env = node_env()
        if cls.env is None:
            return
        cls.d = tempfile.mkdtemp()
        sd = os.path.join(cls.d, 'seg'); os.makedirs(sd)
        open(os.path.join(sd, 'scene.js'), 'w').write(SCENE)
        cls.segs = [{'id': 'seg', 'dir': sd, 't0': 0.0, 't1': 2.0}]
        open(os.path.join(cls.d, 'probe.js'), 'w').write(PROBE)

        def run(view, mode):
            html = os.path.join(cls.d, 'page' + mode, 'index.html')
            EP.build(cls.segs, [{'id': 'y', 'display': '1991'}], html, view=view)
            r = subprocess.run(['node', os.path.join(cls.d, 'probe.js'), html, mode], env=cls.env, capture_output=True, text=True, timeout=300)
            if r.returncode:
                raise AssertionError(r.stderr[-3000:])
            return json.loads(r.stdout.strip().splitlines()[-1])
        cls.H = run(None, 'h')
        cls.V = run({'orient': 'v', 's': 0.75, 'hook': 'A hook line', 'cws': [{'id': 'cw1', 'text': 'A measurement, not a next step'}], 't0': 0}, 'v')

    @classmethod
    def tearDownClass(cls):
        if getattr(cls, 'd', None):
            shutil.rmtree(cls.d, ignore_errors=True)

    def setUp(self):
        if self.env is None:
            self.skipTest('node / playwright / vendor three không có')

    def test_a_safe_area_and_basis(self):
        self.assertEqual(self.H['errs'], [])
        T = {o['text']: o for o in self.H['a'] if o['kind'] == 'text'}
        self.assertGreaterEqual(T['EDGE LEFT']['box'][0], SAFE[0])                      # 36 px tràn → đẩy vào
        self.assertLessEqual(T['EDGE RIGHT']['box'][2], SAFE[2])
        self.assertEqual(T['FAR OUT']['box'][0], -400)                                  # tràn xa (đang bay ra ngoài) → không kéo lại
        for s in ('ILLUSTRATIVE', 'A measurement, not a next step', 'All $ in dollars of the day'):
            b = T[s]['box']; self.assertTrue(SAFE[0] <= b[0] and SAFE[1] <= b[1] and b[2] <= SAFE[2] - 17 and b[3] <= SAFE[3], (s, b))   # 17 = viền huy hiệu
        self.assertTrue(re.search(r'dollars of the day', T['All $ in dollars of the day']['text']))
        self.assertFalse(inter(T['All $ in dollars of the day']['box'], T['A measurement, not a next step']['box']))
        U = {o['text']: o for o in self.H['b'] if o['kind'] == 'text'}
        self.assertLessEqual(U['US only · history, not a forecast']['box'][3], SAFE[3])

    def test_b_graphics_split(self):
        g3, g2, g = png(self.H['g3']), png(self.H['g2']), png(self.H['g'])
        bar = (slice(380, 560), slice(900, 1020)); line = (slice(296, 305), slice(1350, 1650))
        self.assertGreater(int(g3[bar][..., 3].max()), 200); self.assertEqual(int(g3[line][..., 3].max()), 0)    # 3D, không nét 2D
        self.assertEqual(int(g2[bar][..., 3].max()), 0); self.assertGreater(int(g2[line][..., 3].max()), 200)    # nét 2D, không 3D
        self.assertGreater(int(g[bar][..., 3].max()), 200); self.assertGreater(int(g[line][..., 3].max()), 200)  # 'graphics' = cả hai (không đổi)

    def test_c_vertical_layout(self):
        self.assertEqual(self.V['errs'], [])
        v0, v1 = self.V['v0'], self.V['v1']
        scene = [x for x in v0['texts'] if x['kind'] != 'chrome']
        for i in range(len(scene)):
            for j in range(i + 1, len(scene)):
                self.assertFalse(inter(scene[i]['box'], scene[j]['box']), (scene[i], scene[j]))   # không cặp chữ nào giao nhau
        self.assertTrue(any(d['s'] == '1991' for d in v0['dropped']))                   # nhãn trục nhỏ giao nhãn lớn → bỏ (không dịch khỏi trục)
        self.assertTrue(any(d['s'] == '2005' for d in v0['dropped']))                   # nhãn trục 48 px cũng bỏ, không dịch
        self.assertTrue(any(s['s'] == 'Big label two' for s in v0['shifted']))          # nhãn lớn thứ hai dịch dọc
        self.assertIn('BASIS', v0['tags'])
        self.assertTrue(any(x['s'] == 'All $ in dollars of the day' for x in v0['texts']))
        self.assertTrue(v1['hist'] and v1['illus'])                                     # khung history không có chữ số → vẫn có ILLUSTRATIVE
        self.assertTrue({'ILLUSTRATIVE', 'HISTORY'} <= set(v1['tags']))


class MidrollWaiver(unittest.TestCase):
    def test_waiver(self):
        import yaml
        sys.path.insert(0, os.path.join(HERE, '..', 'factory'))
        import spec as SP
        Y = yaml.safe_load(open(os.path.join(HERE, '..', '..', 'episodes', 'ep005', 'episode.yaml')))
        root = os.path.join(HERE, '..', '..', 'episodes', 'ep005')
        lv = lambda y: [p['level'] for p in SP.check(y, root) if p['rule'] == 'midrolls']
        self.assertEqual(lv({**Y, 'midrolls': [], 'midrolls_waiver': 'owner: no mid-roll'}), ['WARN'])
        self.assertEqual(lv({**Y, 'midrolls': [], 'midrolls_waiver': ''}), ['BLOCK'])     # không lý do → vẫn chặn


class SilenceGain(unittest.TestCase):
    def test_windows(self):
        import numpy as np
        sys.path.insert(0, os.path.join(HERE, '..', 'factory', 'world'))
        import audio
        SR = audio.SR; g = audio.silence_gain(SR * 4, [[1.0, 2.5]])
        self.assertIsNone(audio.silence_gain(10, []))
        self.assertEqual(float(g[int(1.2 * SR):int(2.4 * SR)].max()), 0.0)              # lặng trọn cửa sổ
        self.assertEqual(float(g[:int(0.9 * SR)].min()), 1.0); self.assertEqual(float(g[int(2.6 * SR):].min()), 1.0)   # ngoài cửa sổ + 50 ms: nguyên
        self.assertTrue(0 < g[int(0.975 * SR)] < 1)                                     # cos 50 ms ngay ngoài cửa sổ


if __name__ == '__main__':
    unittest.main()
