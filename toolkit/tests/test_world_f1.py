"""Test F-1 (BACKLOG): chuyển chế độ bằng máy quay di chuyển thật, cờ opt-in `style: 'fly'` trên động tác `mode`.
(a) cờ tắt: with_style(None|'dissolve') trả nguyên động tác; cửa sổ, âm (move_sounds), cảnh render (shots_for) và check_rules
    KHÔNG đổi khi bật 'fly' → quy tắc 2/3 và cache cảnh giữ nguyên.
(b) check_rules: 'fly' trên động tác khác 'mode' hoặc kiểu lạ → lỗi F-1.
(c) core.js (node + three của vendor; bỏ qua nếu thiếu): động tác không cờ = nội suy cũ (lerp vị trí, log fov, chart tuyến tính theo ease);
    'fly' đi qua tư thế via ở giữa cửa sổ, chạm đúng tư thế đích, chartW đơn điệu và < 0,95 tới khi máy đã gần chính diện
    (cổng số của quy tắc 1 trong Overlay dùng chính chartW này), dolly-zoom: fov ở giữa đường rộng hơn hai đầu khi via gần vật.
Bằng chứng render (chạy tay): seg-s01-s03 dựng lại với core.js mới → 5/5 cảnh trùng MD5 với cache cũ (BACKLOG F-1).
"""
import json, os, shutil, subprocess, sys, tempfile, unittest
HERE = os.path.dirname(os.path.abspath(__file__))
WORLD = os.path.join(HERE, '..', 'factory', 'world')
sys.path.insert(0, WORLD)
sys.dont_write_bytecode = True
import spine as SV  # noqa: E402

W = [{'w': 'You', 's': 0.2, 'e': 0.4, 'sid': 'S01.1'}, {'w': 'ten', 's': 1.0, 'e': 1.2, 'sid': 'S01.1'},
     {'w': 'Then', 's': 8.0, 'e': 8.3, 'sid': 'S01.2'}, {'w': 'schedule.', 's': 9.5, 'e': 10.0, 'sid': 'S01.2'}]
B = [('a', 'S01.1', 'world', 'i', 'v', {'ten': '@S01.1:ten'}, [], 0.3, 'e', 'n'), ('b', 'S01.2', 'chart', 'i', 'v', {'s': '@S01.2:schedule'}, [], 0.5, 'e', 'n')]
LINES = {'S01.1': 'You ten.', 'S01.2': 'Then schedule.'}
MV = {'verb': 'mode', 'from': 'w', 'to': 'c', 't0': 6.0, 't1': 7.1, 'reason': 'r', 'sound': 'whoosh_mode'}


class FlagOff(unittest.TestCase):
    def test_a_unchanged_timing(self):
        self.assertIs(SV.with_style(MV), MV)
        self.assertIs(SV.with_style(MV, 'dissolve'), MV)
        fly = SV.with_style(MV, 'fly', 'via')
        self.assertEqual((fly['style'], fly['via']), ('fly', 'via'))
        self.assertEqual({k: v for k, v in fly.items() if k not in ('style', 'via')}, MV)
        g = lambda m: 0.6
        self.assertEqual(SV.move_sounds([fly], g), SV.move_sounds([MV], g))
        self.assertEqual(SV.shots_for([fly], 12.0), SV.shots_for([MV], 12.0))
        beats = SV.beats_from(B, SV.Anchors(W), LINES)
        self.assertEqual(SV.check_rules(beats, [MV], 0.25), [])
        self.assertEqual(SV.check_rules(beats, [fly], 0.25), [])

    def test_b_bad_style(self):
        beats = SV.beats_from(B, SV.Anchors(W), LINES)
        with self.assertRaises(SystemExit): SV.with_style(dict(MV, verb='pan'), 'fly')
        with self.assertRaises(SystemExit): SV.with_style(MV, 'warp')
        self.assertTrue(any('F-1' in e for e in SV.check_rules(beats, [dict(MV, verb='pan', style='fly')], 0.25)))
        self.assertTrue(any('F-1' in e for e in SV.check_rules(beats, [dict(MV, style='warp')], 0.25)))


JS = r"""
import { Camera } from './core.js';
const poses = { w: { pos: [-10.4, 3, 11.8], tgt: [-10.9, 1.6, 0], fov: 35, chart: 0 }, c: { pos: [0, 2, 35.2], tgt: [0, 2, 0], fov: 12, chart: 1 },
  v: { pos: [-6.4, 2.2, 6.4], tgt: [-4, 1.2, 0], fov: 35, chart: 0 } };
const base = { verb: 'mode', from: 'w', to: 'c', t0: 1, t1: 2.1 };
const T = Array.from({ length: 34 }, (_, i) => 0.8 + i * 0.05);
const off = Camera(poses, [base]), dis = Camera(poses, [{ ...base, style: 'dissolve' }]), fly = Camera(poses, [{ ...base, style: 'fly', via: 'v' }]);
const out = { T, off: T.map((t) => off.poseAt(t)), dis: T.map((t) => dis.poseAt(t)), fly: T.map((t) => fly.poseAt(t)), mid: fly.poseAt(1.55), moving: T.map((t) => fly.moving(t)) };
console.log(JSON.stringify(out));
"""


def run_js():
    node, three = shutil.which('node'), os.path.join(WORLD, 'vendor', 'node_modules', 'three')
    if not node or not os.path.isdir(three): return None
    d = tempfile.mkdtemp()
    try:
        shutil.copy(os.path.join(WORLD, 'core.js'), d)
        os.makedirs(os.path.join(d, 'node_modules')); os.symlink(os.path.abspath(three), os.path.join(d, 'node_modules', 'three'))
        for name, body in (('package.json', '{"type": "module"}'), ('t.js', JS)):
            with open(os.path.join(d, name), 'w') as f: f.write(body)
        r = subprocess.run([node, 't.js'], cwd=d, capture_output=True, text=True, timeout=60)
        if r.returncode: raise AssertionError(r.stderr)
        return json.loads(r.stdout)
    finally:
        shutil.rmtree(d, ignore_errors=True)


def ease(t, a, b):
    x = min(1, max(0, (t - a) / (b - a))); return x * x * (3 - 2 * x)


class CoreJs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.R = run_js()

    def setUp(self):
        if self.R is None: self.skipTest('node hoặc vendor/three không có')

    def test_c_default_is_old_lerp(self):
        import math
        a, b = [-10.4, 3, 11.8], [0, 2, 35.2]
        for t, p, q in zip(self.R['T'], self.R['off'], self.R['dis']):
            self.assertEqual(p, q)                       # style 'dissolve' = không cờ
            x = ease(t, 1, 2.1)
            for i in range(3): self.assertAlmostEqual(p['pos'][i], a[i] + (b[i] - a[i]) * x, places=9)
            self.assertAlmostEqual(p['fov'], math.exp(math.log(35) + (math.log(12) - math.log(35)) * x), places=9)
            self.assertAlmostEqual(p['chart'], x, places=9)
            self.assertNotIn('fly', p)

    def test_d_fly_path_and_gate(self):
        T, F = self.R['T'], self.R['fly']
        for t, p in zip(T, F):
            if t <= 1: self.assertEqual((p['pos'], p['fov'], p['chart']), ([-10.4, 3, 11.8], 35, 0))
            if t >= 2.1: self.assertEqual((p['pos'], p['fov'], p['chart']), ([0, 2, 35.2], 12, 1))
        cw = [p['chart'] for p in F]
        self.assertEqual(cw, sorted(cw))                                   # đơn điệu
        for t, p in zip(T, F):                                             # cổng số: chỉ mở khi máy đã gần chính diện (x ≥ 0,9)
            if p['chart'] >= 0.95: self.assertGreaterEqual(ease(t, 1, 2.1), 0.9, t)
            if 1 < t < 2.1: self.assertTrue(p.get('fly'))
        m = self.R['mid']                                                  # giữa cửa sổ: đúng tư thế via, chartW = 0
        for i in range(3): self.assertAlmostEqual(m['pos'][i], [-6.4, 2.2, 6.4][i], places=6)
        self.assertEqual(m['chart'], 0)
        self.assertGreater(m['fov'], 35)                                   # dolly-zoom: sát vật → góc rộng; xa → tiêu cự dài
        self.assertEqual([t for t, mv in zip(T, self.R['moving']) if mv], [t for t in T if 1 < t < 2.1])   # quy tắc 2: cửa sổ không đổi


if __name__ == '__main__':
    unittest.main()
