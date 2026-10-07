"""Test artefact hợp đồng từ đoạn thế giới (F11: whoosh, camera.json, sonify-events.json) + Shorts từ đoạn thế giới (helpers) + gói trang kiểm.
(a) audio.sfx_layer(split=True): tiếng động tác máy quay (whoosh_*, swish, `sound` của moves) tách riêng; sfx + whoosh = lớp cũ (cùng rng).
(b) splice.merge_audio: đoạn có stem whoosh → stem whoosh của tập; tổng các stem = mix-raw; đoạn cũ không có whoosh vẫn ghép được.
(c) artefacts.map_frame: máy nhìn thẳng mặt phẳng z = 0 → tâm, zoom đúng công thức; tốc độ máy (công thức của checks) không phụ thuộc W0;
    camera_json: khung ngoài đoạn = đứng yên, thiếu khung → None; sonify_json: khung = giờ nốt vang (t_sound) của tập.
(d) shorts: seg_for; frame_logs → dạng engine 2D mỗi 6 khung mà qc.frame_rules('v') đọc được; short_audio: −14 LUFS ± 0,5, ≤ −1,5 dBTP, đúng độ dài.
(e) episode_page.graph: đặc tả import → chỗ giữ, phụ thuộc trước; vòng import → dừng; JSON nạp bằng chuỗi '/….json' được nhúng.
"""
import json, math, os, shutil, subprocess, sys, tempfile, unittest
import numpy as np
import soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'factory', 'world')); sys.path.insert(0, os.path.join(HERE, '..', 'factory'))
sys.dont_write_bytecode = True
import artefacts as ART  # noqa: E402
import audio as AU  # noqa: E402
import episode_page as EP  # noqa: E402
import shorts as WS  # noqa: E402
import splice as SP  # noqa: E402

SR = 48000


class Whoosh(unittest.TestCase):
    def test_a_split_sums_to_old_layer(self):
        spine = {'moves': [{'sound': 'land'}], 'events': [{'kind': 'whoosh_mode', 't': 0.2, 'dur': 0.6}, {'kind': 'tick', 't': 0.5, 'v': 0.5},
                                                          {'kind': 'swish', 't': 0.9, 'to': 1.3}, {'kind': 'land', 't': 1.4}, {'kind': 'chime', 't': 2.2}]}
        N = int(2.5 * SR)
        AU.rng = np.random.default_rng(5); old = AU.sfx_layer(spine, N)
        AU.rng = np.random.default_rng(5); sfx, wh = AU.sfx_layer(spine, N, split=True)
        self.assertTrue(np.allclose(sfx + wh, old, atol=1e-12))
        self.assertGreater(np.abs(wh[int(0.3 * SR):int(0.7 * SR)]).max(), 1e-3)     # whoosh_mode
        self.assertGreater(np.abs(wh[int(1.4 * SR):int(1.5 * SR)]).max(), 1e-4)     # 'land' = sound of a move → whoosh
        self.assertLess(np.abs(wh[int(2.2 * SR):int(2.3 * SR)]).max(), 1e-9); self.assertGreater(np.abs(sfx[int(2.2 * SR):int(2.3 * SR)]).max(), 1e-3)   # chime stays sfx
        self.assertGreater(np.abs(sfx[int(0.5 * SR):int(0.55 * SR)]).max(), 1e-4)
        self.assertTrue(AU.is_whoosh('whoosh_air') and AU.is_whoosh('swish') and not AU.is_whoosh('tick'))

    def test_b_splice_whoosh_stem(self):
        d = tempfile.mkdtemp()
        try:
            ep, sg = os.path.join(d, 'stems'), os.path.join(d, 'seg'); os.makedirs(ep); os.makedirs(sg)
            N, n = 3 * SR, SR
            t = np.arange(N) / SR
            sf.write(os.path.join(ep, 'voice.flac'), np.stack([0.1 * np.sin(2 * np.pi * 200 * t)] * 2, 1), SR, subtype='PCM_24')
            for k, a in (('voice', 0.1), ('music', 0.02), ('data', 0.03), ('sfx', 0.04), ('whoosh', 0.05), ('room', 0.001)):
                x = a * np.sin(2 * np.pi * (300 + 50 * len(k)) * np.arange(n) / SR)
                sf.write(os.path.join(sg, k + '.wav'), np.stack([x, x], 1), SR)
            raw = os.path.join(d, 'raw.wav')
            info = SP.merge_audio(ep, [{'id': 'w', 'stems': sg, 't0': 1.0, 't1': 2.0}], 3.0, raw, 30)
            self.assertIn('whoosh', info['stems'])
            S = {k: sf.read(os.path.join(ep, k + '.flac'), always_2d=True)[0] for k in info['stems']}
            mix = sf.read(raw, always_2d=True)[0]
            self.assertLess(np.abs(sum(S.values()) - mix).max(), 1e-4)            # stems sum to the pre-master mix
            self.assertGreater(np.abs(S['whoosh'][int(1.2 * SR):int(1.8 * SR)]).max(), 0.01)
            self.assertLess(np.abs(S['whoosh'][:SR - 10]).max(), 1e-6)
            os.remove(os.path.join(sg, 'whoosh.wav'))                              # segment built before the split: still splices, no whoosh stem
            shutil.rmtree(ep); os.makedirs(ep)
            sf.write(os.path.join(ep, 'voice.flac'), np.stack([0.1 * np.sin(2 * np.pi * 200 * t)] * 2, 1), SR, subtype='PCM_24')
            self.assertNotIn('whoosh', SP.merge_audio(ep, [{'id': 'w', 'stems': sg, 't0': 1.0, 't1': 2.0}], 3.0, raw, 30)['stems'])
        finally:
            shutil.rmtree(d, ignore_errors=True)


def checks_speed(fr, fps):
    """Camera speed of checks/py/r_audio.camera_speed (2.5D form), re-written here: |Δ(x,y)|/(1920/zoom) + |Δ ln zoom| per s."""
    x = np.array([f['x'] for f in fr]); y = np.array([f['y'] for f in fr]); z = np.array([f['zoom'] for f in fr])
    dt = 1 / fps
    return np.hypot(np.gradient(x), np.gradient(y)) / dt / (1920 / z) + np.abs(np.gradient(np.log(z))) / dt


class Camera(unittest.TestCase):
    def test_c_mapping(self):
        c = {'p': [3.0, 2.0, 30.0], 'd': [0, 0, -1], 'fov': 12.0, 'aspect': 16 / 9}
        m = ART.map_frame(c)
        w = 2 * 30 * math.tan(math.radians(6)) * 16 / 9
        self.assertAlmostEqual(m['zoom'], ART.W0 / w, places=5)
        self.assertAlmostEqual(m['x'], 3 * 1920 / ART.W0 + 960, places=2)
        self.assertAlmostEqual(m['y'], -2 * 1920 / ART.W0 + 540, places=2)
        d = [0, -0.2, -1]; m2 = ART.map_frame({**c, 'd': d})                         # tilted down: hits the plane lower
        self.assertGreater(m2['y'], m['y'])
        # a pan: 30 frames moving 2 world units; the speed in frame widths/s does not depend on W0
        cams = [{'f': i, 'p': [2 * i / 30, 2, 30], 'd': [0, 0, -1], 'fov': 12, 'aspect': 16 / 9} for i in range(30)]
        sp = []
        for w0 in (20.0, 7.0):
            ART.W0 = w0
            cam, why = ART.camera_json(2.0, 30, [{'id': 'g', 'f0': 15, 'f1': 45, 'cams': cams}])
            sp.append(checks_speed(cam['frames'][15:45], 30)[5:25])
        ART.W0 = 20.0
        self.assertTrue(np.allclose(sp[0], sp[1], rtol=1e-3))
        self.assertAlmostEqual(float(sp[0].mean()), 2 / w, places=2)                # 2 units/s over the visible width
        self.assertEqual(cam['frames'][0], {'t': 0.0, 'x': 960.0, 'y': 540.0, 'zoom': 1.0})   # outside the world segment: still
        self.assertEqual(len(cam['frames']), 60)
        bad, why = ART.camera_json(2.0, 30, [{'id': 'g', 'f0': 15, 'f1': 45, 'cams': cams[:-1]}])
        self.assertIsNone(bad); self.assertEqual(why['missing_frames'], 1)

    def test_c2_sonify(self):
        s = ART.sonify_json(30, [{'id': 'b', 't0': 58.0, 'events': [{'t': 1.0, 't_sound': 1.1, 'v': 0.3}, {'t': 0.5, 'v': 0.9, 'over': True}]}])
        self.assertEqual([d['f'] for d in s['dot']], [round(58.5 * 30), round(59.1 * 30)])
        self.assertEqual(s['dot'][1]['id'], 'b:0'); self.assertEqual(s['dot'][0]['y'], 0.9)
        self.assertEqual((s['bar'], s['line']), ([], []))


class Shorts(unittest.TestCase):
    def test_d_helpers(self):
        segs = [{'id': 'a', 't0': 0.0, 't1': 58.0}, {'id': 'b', 't0': 58.0, 't1': 185.2}]
        self.assertEqual(WS.seg_for(segs, 60, 70)['id'], 'b')
        self.assertIsNone(WS.seg_for(segs, 50, 60))                                  # crosses two segments → 2D path
        V = {'texts': [{'s': '23 months', 'kind': 'number', 'px': 60, 'box': [100, 500, 400, 560], 'opacity': 1, 'contrast': 15}], 'raised': [], 'fitted': [],
             'shifted': [], 'collisions': [], 'recoloured': [], 'tags': ['ILLUSTRATIVE', 'HISTORY', 'CW:x'], 'claims': ['number'], 'hist': True, 'illus': True}
        world = [{'t': 10 + k / 10, 'v': V} for k in range(30)]                     # every 3 frames, segment seconds 10.0…12.9
        logs = WS.frame_logs(world, 10.0, 30, [{'f': 90, 't': 3.0, 'texts': [], 'raised': [], 'collisions': [], 'recoloured': [], 'tags': [], 'claims': [], 'hist': False, 'illus': False}])
        self.assertEqual([L['t'] for L in logs[:-1]], [round(k * 0.2, 3) for k in range(15)])
        import qc as QC
        q = QC.Q(); QC.frame_rules(q, logs, 'v', 'SHx', [{'id': 'x', 'text': 'cw'}])
        R = {i['item']: i['result'] for i in q.items}
        self.assertEqual(R['SHx sàn chữ'], 'ĐẠT'); self.assertEqual(R['SHx vùng an toàn'], 'ĐẠT'); self.assertEqual(R['SHx nhãn ILLUSTRATIVE / history'], 'ĐẠT')

    def test_d2_audio(self):
        d = tempfile.mkdtemp()
        try:
            t = np.arange(20 * SR) / SR
            x = 0.05 * np.sin(2 * np.pi * 220 * t) * (1 + 0.5 * np.sin(2 * np.pi * 0.7 * t))
            m = os.path.join(d, 'master.wav'); sf.write(m, np.stack([x, x], 1), SR)
            out = os.path.join(d, 's.wav')
            WS.short_audio(m, 4.0, 10.0, 1.5, out)
            y, sr = sf.read(out, always_2d=True)
            self.assertEqual(sr, SR); self.assertAlmostEqual(len(y) / SR, 11.5, delta=0.01)
            r = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-i', out, '-af', 'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True)
            tail = r.stderr[r.stderr.rindex('Summary:'):]
            I = float(tail.split('I:')[1].split('LUFS')[0]); P = float(tail.split('Peak:')[1].split('dBFS')[0])
            self.assertAlmostEqual(I, -14.0, delta=0.5); self.assertLessEqual(P, -1.0)
            self.assertLess(np.abs(y[int(10.2 * SR):]).max(), 1e-4)                  # silence under the end card
        finally:
            shutil.rmtree(d, ignore_errors=True)


class Bundle(unittest.TestCase):
    def test_e_graph(self):
        d = tempfile.mkdtemp()
        try:
            W = lambda n, s: open(os.path.join(d, n), 'w').write(s)
            W('a.js', "import { b } from './b.js';\nimport * as C from \"./c.js\";\nexport const a = b + C.c; // import('./nope.js') stays\n")
            W('b.js', "import { c } from './c.js';\nexport const b = c + 1; const u = '/toolkit/factory/world/page.html';\n")
            W('c.js', "export const c = 1;\n")
            mods, order, idx = EP.graph([os.path.join(d, 'a.js')])
            names = [os.path.basename(m['path']) for m in mods]
            self.assertEqual([names[i] for i in order], ['c.js', 'b.js', 'a.js'])
            a = mods[idx[os.path.join(d, 'a.js')]]['src']
            self.assertIn(f"from './__CRUXMOD_{idx[os.path.join(d, 'b.js')]}__'".replace("'./", "'"), a)
            self.assertIn(f'from "__CRUXMOD_{idx[os.path.join(d, "c.js")]}__"', a)
            self.assertIn("import('./nope.js')", a)                                   # unresolved specifier left as is
            W('c.js', "import { a } from './a.js';\nexport const c = 1;\n")
            with self.assertRaises(SystemExit):
                EP.graph([os.path.join(d, 'a.js')])
            W('s.js', "const p = loadJSON('/episodes/ep005/world/claims.json');\n")
            mods, _, _ = EP.graph([os.path.join(d, 's.js')])
            self.assertIn('/episodes/ep005/world/claims.json', EP.collect_json(mods, []))
        finally:
            shutil.rmtree(d, ignore_errors=True)


if __name__ == '__main__':
    unittest.main()
