"""F-17 (toolkit/factory/f17/INTENT.md): lớp ánh sáng điện ảnh opt-in (khoá `cine` của spine.json).
Chạy: python3 -m unittest toolkit.tests.test_factory_f17   (cần three trong world/vendor + playwright; phần trình duyệt ≈ 1–2 phút)
  a  cine_color: CIEDE2000 đúng bảng Sharma (2005); ΔE > 5 → CHẶN; đảo thứ tự sáng → CHẶN; cặp sát nhau (|ΔL*| < 1) không tính
  b  tài sản: manifest SHA-256 khớp tệp trong git; tệp > 2 MB không được commit (cờ commit theo cỡ)
  c  cảnh thử nhỏ: KHÔNG khai `cine` vs khai `cine` ở 540p → mp4 + nhật ký trùng byte (nháp không bật lớp); ở 1080p khác (lớp chạy)
  d  O.text({font: 'serif'}) → log.texts[].font = 'serif' và đối tượng trang kiểm (CK.on) mang font; chữ thường không có trường font
  e  comment_guard + node --check trên toolkit/factory/world/cine
"""
import hashlib, json, os, shutil, subprocess, sys, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
CINE = os.path.join(ROOT, 'toolkit', 'factory', 'world', 'cine')
sys.path[:0] = [HERE, CINE]
sys.dont_write_bytecode = True
import cine_color as CC  # noqa: E402
import comment_guard  # noqa: E402

VENDOR = os.path.join(ROOT, 'toolkit', 'factory', 'world', 'vendor', 'node_modules', 'three')
WORK = os.path.join(ROOT, 'toolkit', 'factory', 'f17', 'work')
SCENE = r"""import * as THREE from 'three';
import { Stage, Camera, CK, fonts } from '/toolkit/factory/world/core.js';
import { Studio, House } from '/toolkit/factory/world/lib3d.js';
export async function boot(res) {
  if (new URLSearchParams(location.search).get('ckon') === '1') CK.on = true;
  await fonts();   // như mọi cảnh thật (không chờ phông → khung đầu đổi theo lần chạy)
  const st = Stage(res), O = st.O, scene = new THREE.Scene(), { key } = Studio(scene, { shadowBox: 8 });
  const CAM = Camera({ k: { pos: [0, 2.2, 7], tgt: [0, 0.6, 0], fov: 35, chart: 1 } }, []);
  const bar = new THREE.Mesh(new THREE.BoxGeometry(1, 1.4, 1), new THREE.MeshStandardMaterial({ color: '#F2B441' })); bar.position.set(-1.2, 0.7, 0);
  bar.userData.checks = { role: 'bar', key: 'b' }; bar.castShadow = true; scene.add(bar);
  const h = House({ w: 1.4 }); h.position.set(1.2, 0, 0); scene.add(h);
  function frame(t) { const pose = CAM.apply(t); key.target.position.set(0, 0, 0); renderer.render(scene, CAM.cam); const log = O.begin(t, pose.chart, CAM.cam);
    O.text('Bank of United States', 160, 200, 64, { font: 'serif', kind: 'title' }); O.text('1931', 160, 300, 56, { kind: 'number' });
    st.compose(); log.camMoving = false; return log; }
  const renderer = st.renderer;
  return { canvas: st.out, frame };
}
"""


def node_env():
    return {**os.environ, 'NODE_PATH': subprocess.run(['npm', 'root', '-g'], capture_output=True, text=True).stdout.strip()}


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


class F17Color(unittest.TestCase):
    def test_a_de2000_sharma(self):
        for a, b, e in [((50, 2.6772, -79.7751), (50, 0, -82.7485), 2.0425), ((50, -1.3802, -84.2814), (50, 0, -82.7485), 1.0),
                        ((50, 2.5, 0), (73, 25, -18), 27.1492), ((60.2574, -34.0099, 36.2677), (60.4626, -34.1751, 39.4387), 1.2644),
                        ((2.0776, 0.0795, -1.135), (0.9033, -0.0636, -0.5514), 0.9082)]:
            self.assertAlmostEqual(CC.de2000(a, b), e, places=3)

    def test_a_judge(self):
        g = lambda k, b, c: {'key': k, 'n': 999, 'base': b, 'cine': c}  # noqa: E731
        ok = CC.judge({'samples': [{'t': 0, 'data': [g('#a', [200, 190, 170], [201, 190, 171]), g('#b', [60, 120, 230], [60, 121, 229])]}]})
        self.assertEqual(ok['level'], 'PASS')
        de = CC.judge({'samples': [{'t': 0, 'data': [g('#a', [200, 190, 170], [215, 170, 170])]}]})   # kem → hồng
        self.assertEqual(de['level'], 'BLOCK'); self.assertIn('ΔE2000', de['block'][0])
        # đảo thứ tự sáng với ΔE nhỏ mỗi màu (ΔL* ≈ 2 mỗi bên) — v4 cảnh c: "hi" tối hơn vàng trước lớp, sáng hơn sau
        fl = CC.judge({'samples': [{'t': 0, 'data': [g('#hi', [150, 150, 150], [156, 156, 156]), g('#y', [153, 153, 153], [148, 148, 148])]}]})
        self.assertEqual(fl['level'], 'BLOCK'); self.assertTrue(any('đảo thứ tự' in m for m in fl['block']))
        near = CC.judge({'samples': [{'t': 0, 'data': [g('#p', [150, 150, 150], [151, 151, 151]), g('#q', [151, 151, 151], [150, 150, 150])]}]})
        self.assertEqual(near['level'], 'PASS')   # |ΔL*| trước < 1: không định thứ tự

    def test_b_assets(self):
        man = json.load(open(os.path.join(CINE, 'assets', 'manifest.json')))
        tracked = set(subprocess.run(['git', 'ls-files', 'toolkit/factory/world/cine/assets'], cwd=ROOT, capture_output=True, text=True).stdout.split())
        for k, m in man.items():
            self.assertEqual(m['commit'], m['bytes'] <= 2_000_000, k)
            self.assertIn('CC0', m['licence'])
            p = os.path.join(CINE, 'assets', 'cc0' if m['commit'] else 'dl', m['file'])
            if m['commit']:
                self.assertEqual(sha(p), m['sha256'], k)
            if tracked:   # sau commit: chỉ tệp ≤ 2 MB nằm trong git
                self.assertEqual(os.path.relpath(p, ROOT) in tracked, m['commit'], k)

    def test_e_lint(self):
        bad, n = comment_guard.check([CINE])
        self.assertEqual(bad, []); self.assertGreaterEqual(n, 3)


@unittest.skipUnless(os.path.isdir(VENDOR), 'cần three (npm ci trong world/vendor)')
class F17Render(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = {}
        for k, cine in (('plain', None), ('cine', {'look': 'dusk'})):
            d = os.path.join(WORK, 'test-' + k); shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
            for r in (540, 1080): shutil.rmtree(os.path.join(WORK, f'cache-{k}-{r}'), ignore_errors=True)
            open(os.path.join(d, 'scene.js'), 'w').write(SCENE)
            sp = {'total': 0.2, 'shots': [{'id': 's0', 't0': 0, 't1': 0.2}], 'moves': [], 'beats': []}
            if cine: sp['cine'] = cine
            json.dump(sp, open(os.path.join(d, 'spine.json'), 'w'))
            cls.d[k] = d

    def render(self, k, res):
        out = os.path.join(WORK, f'out-{k}-{res}.mp4')
        r = subprocess.run(['node', 'toolkit/factory/world/render_shots.js', os.path.relpath(self.d[k], ROOT), str(res), out, '--workers', '1',
                            '--cache', os.path.join(WORK, f'cache-{k}-{res}')], cwd=ROOT, env=node_env(), capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr[-2000:])
        return out

    def test_c_draft_off_1080_on(self):
        a, b = self.render('plain', 540), self.render('cine', 540)
        self.assertEqual(sha(a), sha(b)); self.assertEqual(sha(a[:-4] + '.log.json'), sha(b[:-4] + '.log.json'))
        self.assertNotIn('cine', json.load(open(b + '.render.json')))
        c, d = self.render('plain', 1080), self.render('cine', 1080)
        self.assertNotEqual(sha(c), sha(d)); self.assertTrue(json.load(open(d + '.render.json')).get('cine'))
        self.assertEqual(json.load(open(c[:-4] + '.log.json')), json.load(open(d[:-4] + '.log.json')))   # lớp chữ/nhật ký không đổi

    def test_d_serif_logged(self):
        out = self.render('plain', 540)
        log = json.load(open(out[:-4] + '.log.json'))[0]
        f = {x['text']: x.get('font') for x in log['texts']}
        self.assertEqual(f['Bank of United States'], 'serif'); self.assertIsNone(f['1931'])
        # trang kiểm (CK.on): đối tượng chữ mang font
        js = r"""const { chromium } = require('playwright'); const fs = require('fs'), path = require('path'); const ROOT = process.argv[2], seg = process.argv[3];
(async () => { const b = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
  const ctx = await b.newContext({ viewport: { width: 960, height: 540 } });
  await ctx.route('http://mocv.local/**', (r) => { const p = path.join(ROOT, decodeURIComponent(new URL(r.request().url()).pathname));
    if (!fs.existsSync(p)) return r.fulfill({ status: 404, body: '' }); r.fulfill({ status: 200, body: fs.readFileSync(p), contentType: p.endsWith('.js') ? 'text/javascript' : p.endsWith('.html') ? 'text/html' : 'application/octet-stream' }); });
  const pg = await ctx.newPage(); await pg.goto(`http://mocv.local/toolkit/factory/world/page.html?seg=${seg}&res=540&ckon=1`);
  await pg.waitForFunction('window.READY === true'); const o = await pg.evaluate(() => APP.frame(0).objects.filter((x) => x.kind === 'text').map((x) => [x.text, x.font || null]));
  console.log(JSON.stringify(o)); await b.close(); })();"""
        p = os.path.join(WORK, 'ckon.js'); open(p, 'w').write(js)
        r = subprocess.run(['node', p, ROOT, os.path.relpath(self.d['plain'], ROOT)], cwd=ROOT, env=node_env(), capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr[-1500:])
        objs = dict(json.loads(r.stdout.strip().splitlines()[-1]))
        self.assertEqual(objs['Bank of United States'], 'serif'); self.assertIsNone(objs['1931'])


if __name__ == '__main__':
    unittest.main()
