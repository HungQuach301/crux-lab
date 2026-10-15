"""Test F-18 (Editor + Sound): J/L-cut qua biên đoạn trong world/splice.py. Không mạng, không render three.js.
Master giả 4 s / 30 fps (cảnh S01 0–1 s, S02 1–2 s, S03 2–4 s); đoạn w1 (S02, đỏ) và w2 (S03, xanh lam) mang SỐ KHUNG CỤC BỘ trong độ sáng
(đỏ = 20 + 6·i, lam = 20 + 3·i) → đọc lại được khung nào của đoạn nào đang lên hình ở mỗi khung master.

(a) không khai `cuts` → master trùng TỪNG BYTE với splice.py của main (đồ thị lọc cũ);
(b) J 0,5 s ở S03: khung 60–74 = khung cuối w1 giữ nguyên, khung 75–119 = w2 cục bộ 15–59 (ngoài vùng J: lệch 0 khung), 30–59 = w1 0–29;
(c) L 0,4 s: khung 30–47 = w1 0–17, 48–59 = w2 khung 0 giữ, 60–119 = w2 0–59 (lệch 0 khung ngoài vùng L);
(d) khai sai → dừng: J/L ở cảnh trong đoạn, offset ngoài 0,3–1,0 s, từ khoá rơi vào phần không lên hình, không có đoạn liền trước;
(e) tiếng: merge_audio không dời tiếng (stem trùng từng mẫu với bản không khai), trả `joins`; --transitions ghi điểm cắt hình audio j/l.
SFX ghi âm thật (world/audio.py `sfx_real`, toolkit/sfx/):
(f) không khai sfx_real → mọi stem + mix trùng TỪNG BYTE audio.py của main; (g) khai → tick/land/whoosh phát tệp thư viện (năng lượng mỗi sự
    kiện = tiếng tổng hợp ±1 dB), xoay vòng biến thể, hai lượt trùng byte; (h) sfx_labels.thin_events: bỏ tick trên từ thường và tick thừa
    trong 10 s, giữ whoosh/land, spine gốc không đổi; (i) manifest: mọi tệp ≤ 2 MB, SHA-256 khớp, giấy phép CC0/CC BY có trích nguyên văn;
(j) sfx_labels.plan_real: nhãn cảnh → tệp, KHÔNG tệp nào dùng lại trong 60 s (cả qua hai đoạn), hết tệp → giữ tiếng tổng hợp, tất định;
    audio.py phát đúng kế hoạch; (k) Sonniss TẮT mặc định (chủ dự án 15/10); khi bật: license không cho video thương mại → DỪNG; không cho phân phối lại → tệp không vào repo (bộ nhớ
    đệm) và --verify kiểm SHA; zip bị xoá sau khi lấy; (l) ElevenLabs tắt mặc định: từ chối, không gọi mạng; không còn mã Freesound;
(m) build.py `audio.aac_true_peak` (chủ dự án 15/10): khai → master đích trần − 0,3 dBTP, AAC của video ≤ trần; không khai → loudnorm/mux như cũ.
"""
import importlib.util, json, os, shutil, subprocess, sys, tempfile, unittest, zipfile
import numpy as np
import soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(HERE, '..', 'factory', 'world'))
sys.dont_write_bytecode = True
import splice as SP  # noqa: E402

FPS, W, H, SR = 30, 64, 48, 48000
ENC = {'crf': 4, 'preset': 'ultrafast'}
TL = {'fps': FPS, 'total': 4.0, 'scenes': [{'id': 'S01', 'start': 0.0, 'dur': 1.0}, {'id': 'S02', 'start': 1.0, 'dur': 1.0},
                                            {'id': 'S03', 'start': 2.0, 'dur': 2.0}]}


def ff(*a, inp=None):
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', *a], check=True, input=inp)


def frames(p):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True, check=True)
    return np.frombuffer(r.stdout, np.uint8).reshape(-1, H, W, 3).astype(float)


def numbered(path, n, ch, step):
    x = np.zeros((n, H, W, 3), np.uint8)
    for i in range(n):
        x[i, :, :, ch] = 20 + step * i
    ff('-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', *SP.encode_args(ENC, FPS), path, inp=x.tobytes())


REF = {}


def who(fr):
    """(đoạn, khung cục bộ) của một khung master: khung giải mã gần nhất (trung bình RGB) trong w1, w2 và master đen."""
    m = fr.mean(axis=(0, 1))
    return min(REF.items(), key=lambda kv: np.abs(kv[1] - m).sum())[0]


def spine(cuts=None, cues=(), words=((0.05, 0.3),), total=1.0):
    return {'total': total, 'cuts': cuts or {}, 'beats': [{'id': 'b', 'cues': {f'c{i}': t for i, t in enumerate(cues)}}],
            'words': [{'w': 'x', 's': a, 'e': b} for a, b in words], 'moves': []}


class F18JL(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = tempfile.mkdtemp()
        cls.master = os.path.join(cls.d, 'master.mp4')
        ff('-f', 'lavfi', '-i', f'color=c=black:size={W}x{H}:rate={FPS}:duration=4', *SP.encode_args(ENC, FPS), cls.master)
        cls.w1, cls.w2 = os.path.join(cls.d, 'w1.mp4'), os.path.join(cls.d, 'w2.mp4')
        numbered(cls.w1, 30, 0, 6)
        numbered(cls.w2, 60, 2, 3)
        REF.clear()
        REF[('m', -1)] = frames(cls.master)[0].mean(axis=(0, 1))
        for sid, p in (('w1', cls.w1), ('w2', cls.w2)):
            for i, f in enumerate(frames(p)):
                REF[(sid, i)] = f.mean(axis=(0, 1))

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.d, ignore_errors=True)

    def segs(self, sp1=None, sp2=None):
        out = []
        for sid, mp4, sc, sp in (('w1', self.w1, ['S02'], sp1), ('w2', self.w2, ['S03'], sp2)):
            t0, t1, f0, f1 = SP.scene_span(TL, sc, FPS)
            out.append({'id': sid, 'mp4': mp4, 't0': t0, 't1': t1, 'f0': f0, 'f1': f1, 'scenes': sc, 'spine': sp})
        return out

    def test_a_no_cuts_byte_identical_to_main(self):
        src = subprocess.run(['git', '-C', ROOT, 'show', 'origin/main:toolkit/factory/world/splice.py'], capture_output=True, text=True)
        if src.returncode:
            self.skipTest('không có origin/main')
        p = os.path.join(self.d, 'splice_main.py')
        open(p, 'w').write(src.stdout)
        spec = importlib.util.spec_from_file_location('splice_main', p)
        OLD = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(OLD)
        a, b = os.path.join(self.d, 'old.mp4'), os.path.join(self.d, 'new.mp4')
        OLD.splice_video(self.master, [{k: v for k, v in s.items() if k != 'spine'} for s in self.segs()], a, FPS, ENC)
        SP.splice_video(self.master, self.segs(spine(), spine(total=2.0)), b, FPS, ENC)
        self.assertEqual(SP.sha_file(a), SP.sha_file(b))
        SP.splice_video(self.master, self.segs(spine(), spine({'S03': {'cut': 'hard'}}, total=2.0)), b, FPS, ENC)   # `hard` = như không khai
        self.assertEqual(SP.sha_file(a), SP.sha_file(b))

    def test_b_j_cut(self):
        out = os.path.join(self.d, 'j.mp4')
        segs = self.segs(spine(), spine({'S03': {'cut': 'J', 'offset': 0.5}}, cues=[0.8], total=2.0))
        r = SP.splice_video(self.master, segs, out, FPS, ENC)
        self.assertEqual(r['frames'], 120)
        got = [who(f) for f in frames(out)]
        self.assertEqual(got[:30], [('m', -1)] * 30)
        self.assertEqual(got[30:60], [('w1', i) for i in range(30)])
        self.assertEqual(got[60:75], [('w1', 29)] * 15)                          # vùng J: khung cuối đoạn trước giữ 0,5 s
        self.assertEqual(got[75:], [('w2', i) for i in range(15, 60)])             # ngoài vùng: khung master − f0 = khung đoạn (lệch 0)
        j = segs[1]['join_in']
        self.assertEqual((j['cut'], j['frames'], j['t_sound'], j['t_picture'], j['zone']), ('J', 15, 2.0, 2.5, [2.0, 2.5]))
        self.assertAlmostEqual(j['voice_lead'], 0.45, places=3)                   # lời đoạn sau vào trước điểm cắt hình 0,45 s (V10 ≥ 0,2)

    def test_c_l_cut(self):
        out = os.path.join(self.d, 'l.mp4')
        segs = self.segs(spine(words=((0.1, 0.9),)), spine({'S03': {'cut': 'L', 'offset': 0.4}}, total=2.0))
        SP.splice_video(self.master, segs, out, FPS, ENC)
        got = [who(f) for f in frames(out)]
        self.assertEqual(got[30:48], [('w1', i) for i in range(18)])
        self.assertEqual(got[48:60], [('w2', 0)] * 12)                            # vùng L: khung đầu đoạn sau giữ 0,4 s
        self.assertEqual(got[60:], [('w2', i) for i in range(60)])
        j = segs[1]['join_in']
        self.assertEqual((j['t_picture'], j['zone'], j['hidden']), (1.6, [1.6, 2.0], {'segment': 'w1', 'local': [0.6, 1.0]}))
        self.assertAlmostEqual(j['voice_lag'], 0.3, places=3)                     # lời đoạn trước còn 0,3 s sau điểm cắt hình

    def test_d_refusals(self):
        bad = [spine({'S04': {'cut': 'J', 'offset': 0.5}}, total=2.0),           # không phải cảnh đầu đoạn
               spine({'S03': {'cut': 'J', 'offset': 0.2}}, total=2.0),           # < 0,3 s
               spine({'S03': {'cut': 'J', 'offset': 1.2}}, total=2.0),           # > 1,0 s
               spine({'S03': {'cut': 'X', 'offset': 0.5}}, total=2.0),
               spine({'S03': {'cut': 'J', 'offset': 0.5}}, cues=[0.3], total=2.0)]   # từ khoá 0,3 s bị giấu dưới J 0,5 s
        for sp in bad:
            with self.assertRaises(SystemExit, msg=sp['cuts']):
                SP.splice_video(self.master, self.segs(spine(), sp), os.path.join(self.d, 'x.mp4'), FPS, ENC)
        with self.assertRaises(SystemExit):                                       # L giấu từ khoá cuối đoạn trước
            SP.splice_video(self.master, self.segs(spine(cues=[0.9]), spine({'S03': {'cut': 'L', 'offset': 0.4}}, total=2.0)),
                            os.path.join(self.d, 'x.mp4'), FPS, ENC)
        lone = [s for s in self.segs(None, spine({'S03': {'cut': 'J', 'offset': 0.5}}, total=2.0)) if s['id'] == 'w2']
        with self.assertRaises(SystemExit):                                       # không có đoạn thế giới liền trước
            SP.splice_video(self.master, lone, os.path.join(self.d, 'x.mp4'), FPS, ENC)

    def stems(self, root):
        ep = os.path.join(root, 'stems')
        os.makedirs(ep)
        t = np.arange(4 * SR) / SR
        v = 0.3 * np.sin(2 * np.pi * 220 * t)
        sf.write(os.path.join(ep, 'voice.flac'), np.stack([v, v], 1), SR, subtype='PCM_24')
        out = []
        for sid, n in (('w1', SR), ('w2', 2 * SR)):
            sg = os.path.join(root, sid)
            os.makedirs(sg)
            tt = np.arange(n) / SR
            for k, f in (('voice', 220), ('music', 330), ('sfx', 1000), ('data', 880), ('room', 50)):
                x = (0.05 * np.sin(2 * np.pi * f * tt)).astype(np.float32)
                sf.write(os.path.join(sg, k + '.wav'), np.stack([x, x], 1), SR)
            out.append(sg)
        return ep, out

    def test_e_audio_and_transitions(self):
        res = {}
        for tag, cuts in (('plain', None), ('j', {'S03': {'cut': 'J', 'offset': 0.5}})):
            d = tempfile.mkdtemp(dir=self.d)
            ep, sg = self.stems(d)
            segs = self.segs(spine(), spine(cuts, total=2.0))
            for s, p in zip(segs, sg):
                s['stems'] = p
            SP.splice_video(self.master, segs, os.path.join(d, 'v.mp4'), FPS, ENC)
            info = SP.merge_audio(ep, segs, 4.0, os.path.join(d, 'raw.wav'), FPS)
            res[tag] = (info, SP.sha_file(os.path.join(d, 'raw.wav')), {k: SP.sha_file(p) for k, p in SP.stem_files(ep).items()}, d)
        self.assertNotIn('joins', res['plain'][0])
        self.assertEqual(res['plain'][1:3], res['j'][1:3])                        # tiếng không dời: mix-raw + mọi stem trùng byte
        self.assertEqual([j['cut'] for j in res['j'][0]['joins']], ['J'])
        d = res['j'][3]
        sj, tj = os.path.join(d, 'splice.json'), os.path.join(d, 'transitions.json')
        json.dump({'audio': res['j'][0]}, open(sj, 'w'))
        json.dump({'cuts': [{'t': 2.0, 'from': 'w1', 'to': 'w2', 'type': 'cut', 'match': None, 'audio': None, 'reason': 'old'}]}, open(tj, 'w'))
        subprocess.run([sys.executable, os.path.join(ROOT, 'toolkit', 'factory', 'world', 'splice.py'), '--transitions', sj, tj], check=True,
                       capture_output=True)
        c = json.load(open(tj))['cuts']
        self.assertEqual(len(c), 1)
        self.assertEqual((c[0]['t'], c[0]['audio'], c[0]['type']), (2.5, 'j', 'cut'))


AUDIO = os.path.join(ROOT, 'toolkit', 'factory', 'world', 'audio.py')


class F18Sfx(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = tempfile.mkdtemp()
        t = np.arange(int(6 * SR)) / SR
        v = 0.25 * np.sin(2 * np.pi * 180 * t) * (np.sin(2 * np.pi * 3 * t) > 0) * (t < 5)
        cls.voice = os.path.join(cls.d, 'v.wav'); sf.write(cls.voice, v.astype(np.float32), SR)
        cls.music = os.path.join(cls.d, 'm.wav'); sf.write(cls.music, (0.05 * np.sin(2 * np.pi * 220 * t)).astype(np.float32), SR)
        ev = [{'t': 0.5, 'kind': 'tick', 'v': 0.4}, {'t': 1.4, 'kind': 'tick', 'v': 0.6}, {'t': 2.2, 'kind': 'land'},
              {'t': 2.8, 'kind': 'whoosh_mode', 'dur': 1.2}, {'t': 4.3, 'kind': 'tick', 'v': 0.5}, {'t': 4.9, 'kind': 'rise', 'dur': 0.6},
              {'t': 1.0, 'kind': 'data', 'v': 0.3}]
        cls.spine = {'total': 6.0, 'takes': [{'t': 0.0, 'wav': cls.voice}], 'events': ev, 'music_plan': {'stop': 5.5},
                     'moves': [{'id': 'm', 'sound': 'whoosh_mode'}]}

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.d, ignore_errors=True)

    def run_audio(self, script, spine, tag):
        sp, out = os.path.join(self.d, tag + '.json'), os.path.join(self.d, tag)
        json.dump(spine, open(sp, 'w'))
        subprocess.run([sys.executable, script, out, '--spine', sp, '--music', self.music], check=True, capture_output=True, cwd=ROOT)
        return out, {f: SP.sha_file(os.path.join(out, 'stems', f)) for f in sorted(os.listdir(os.path.join(out, 'stems')))} | \
            {'mix.wav': SP.sha_file(os.path.join(out, 'mix.wav'))}

    def test_f_no_real_byte_identical_to_main(self):
        src = subprocess.run(['git', '-C', ROOT, 'show', 'origin/main:toolkit/factory/world/audio.py'], capture_output=True, text=True)
        if src.returncode:
            self.skipTest('không có origin/main')
        old = os.path.join(ROOT, 'toolkit', 'factory', 'world', '.audio_main_f18test.py')   # cùng thư mục: ROOT của audio.py tính từ __file__
        try:
            open(old, 'w').write(src.stdout)
            _, a = self.run_audio(old, self.spine, 'old')
        finally:
            os.remove(old)
        _, b = self.run_audio(AUDIO, self.spine, 'new')
        self.assertEqual(a, b)

    def test_g_real(self):
        sys.path.insert(0, os.path.dirname(AUDIO))
        import audio as A
        real = A.RealSfx({})
        self.assertTrue({'tick', 'land', 'whoosh_mode'} <= set(real.map))
        for k, n in (('tick', int(0.45 * SR)), ('land', int(0.45 * SR)), ('whoosh_mode', int(1.2 * SR))):
            syn = 0.1 * np.random.default_rng(1).standard_normal(n) * np.exp(-np.arange(n) / (0.2 * SR))
            y = real.sound({'kind': k}, syn)
            self.assertLess(abs(10 * np.log10(np.sum(y ** 2) / np.sum(syn ** 2))), 1.0, k)   # cùng năng lượng (đỉnh không chạm trần +6 dB)
        sp = {**self.spine, 'sfx_real': {}}
        out, a = self.run_audio(AUDIO, sp, 'real1')
        _, b = self.run_audio(AUDIO, sp, 'real2')
        self.assertEqual(a, b)                                                   # tất định
        _, plain = self.run_audio(AUDIO, self.spine, 'synth')
        self.assertNotEqual(a['sfx.wav'], plain['sfx.wav'])
        self.assertNotEqual(a['whoosh.wav'], plain['whoosh.wav'])
        self.assertEqual(a['data.wav'], plain['data.wav'])                       # âm dữ liệu (bằng mã) không đổi
        rep = json.load(open(os.path.join(out, 'audio-report.json')))['sfx_real']
        self.assertEqual(rep['tick']['events'], 3)
        self.assertEqual(len(rep['tick']['files']), 3)                           # xoay vòng: 3 tick = 3 tệp khác nhau
        self.assertNotIn('rise', rep)                                            # rise (cao độ, A-MUSIC) vẫn bằng mã

    def test_h_thin(self):
        sys.path.insert(0, os.path.dirname(AUDIO))
        import sfx_labels as L
        sp = {'total': 20.0, 'words': [{'w': 'plain', 's': 0.4, 'e': 0.7}, {'w': 'key', 's': 3.0, 'e': 3.3}],
              'beats': [{'id': 'b', 'cues': {'k': 3.0}}],
              'events': [{'t': 0.5, 'kind': 'tick'}, {'t': 3.1, 'kind': 'tick'}, {'t': 0.55, 'kind': 'whoosh_mode', 'dur': 1},
                         {'t': 0.6, 'kind': 'land'}, {'t': 3.2, 'kind': 'land'}]
              + [{'t': 5.0 + 0.5 * i, 'kind': 'tick'} for i in range(6)] + [{'t': 6.0, 'kind': 'land'}, {'t': 8.0, 'kind': 'data'}]}
        before = json.dumps(sp, sort_keys=True)
        o = L.thin_events(sp, max10s=4)
        self.assertEqual(json.dumps(sp, sort_keys=True), before)
        kept = [(e['t'], e['kind']) for e in o['events']]
        self.assertNotIn((0.5, 'tick'), kept)                                    # tick trên từ thường
        self.assertIn((3.1, 'tick'), kept)                                       # tick trên từ khoá giữ
        self.assertIn((0.55, 'whoosh_mode'), kept)                               # whoosh trên từ thường giữ (gắn cú máy)
        self.assertIn((6.0, 'land'), kept)
        self.assertNotIn((0.6, 'land'), kept)                                    # tiếng chạm giữa từ thường bỏ (whoosh của cú máy còn)
        self.assertIn((3.2, 'land'), kept)                                       # chạm trên từ khoá giữ
        ts = sorted(e['t'] for e in o['events'] if e['kind'] != 'data')
        self.assertLessEqual(max(sum(1 for x in ts if t <= x < t + 10) for t in ts), 4)
        self.assertEqual(o['sfx_thin']['stuck'], [])

    def test_i_manifest(self):
        man = json.load(open(os.path.join(ROOT, 'toolkit', 'factory', 'world', 'sfx', 'manifest.json')))
        self.assertGreaterEqual(len(man), 1)
        for r in man.values():
            p = os.path.join(ROOT, r['file'])
            self.assertLessEqual(os.path.getsize(p), 2 * 1024 * 1024)
            self.assertEqual(SP.sha_file(p), r['sha256'])
            self.assertIn(r['license'], ('CC0 1.0', 'CC BY 4.0', 'CC BY 3.0'))
            self.assertIn('"', r['license_verbatim'])
            self.assertEqual(len(r['sha256_source']), 64)


    def test_j_plan_real(self):
        sys.path.insert(0, os.path.dirname(AUDIO))
        import sfx_labels as L
        man = json.load(open(os.path.join(ROOT, 'toolkit', 'factory', 'world', 'sfx', 'manifest.json')))
        W = [{'w': 'a', 's': 0.1, 'e': 0.3, 'sid': 'S01.1'}, {'w': 'b', 's': 30.0, 'e': 30.3, 'sid': 'S02.1'}]
        ev = [{'t': 0.5 + 2.0 * i, 'kind': 'tick', 'v': 0.5} for i in range(30)] + [{'t': 5.0 + 4 * i, 'kind': 'whoosh_mode', 'dur': 1.0} for i in range(5)]
        sp = {'segment': 'x', 'episode_t0': 100.0, 'total': 70.0, 'scenes': ['S01', 'S02'], 'words': W, 'events': ev, 'beats': []}
        used = {}
        a = L.plan_real(sp, {'S01': ['giay', 'tien-xu'], 'S02': ['dong-ho']}, man, used=used)
        b = L.plan_real(sp, {'S01': ['giay', 'tien-xu'], 'S02': ['dong-ho']}, man, used={})
        self.assertEqual(json.dumps(a, sort_keys=True), json.dumps(b, sort_keys=True))        # tất định
        plan = a['sfx_real']['plan']
        rep = L.repeat_report(plan)
        self.assertEqual(rep['reused_within'], 0)                                            # không tệp nào lặp trong 60 s
        self.assertGreater(rep['kept_synth'], 0)                                              # hết tệp → giữ tiếng tổng hợp
        tags = {r['id']: r['tags'] for r in man.values()}
        for p in plan:
            if p.get('file'):
                self.assertIn(p['label'], tags[p['file']])
                self.assertIn(p['label'], {'S01': ['giay', 'tien-xu'], 'S02': ['dong-ho']}.get(p['scene'], []) + ['chuyen-canh'])
        self.assertEqual(sum(1 for p in plan if p.get('file') == 'S-OGA-AIRWHOOSH'), 1)       # một tệp gió: dùng một lần / 60 s
        sp2 = {**sp, 'segment': 'y', 'episode_t0': 140.0}                                    # đoạn sau (giờ tập 140–210): used truyền qua
        c = L.plan_real(sp2, {'S01': ['giay']}, man, used=used)
        allp = plan + c['sfx_real']['plan']
        self.assertEqual(L.repeat_report(allp)['reused_within'], 0)
        # audio.py phát đúng kế hoạch
        spa = {**self.spine, 'segment': 'z', 'scenes': ['S01'], 'words': [{'w': 'a', 's': 0.1, 'e': 0.3, 'sid': 'S01.1'}], 'beats': []}
        pl = L.plan_real(spa, {'S01': ['tien-xu', 'giay']}, man)
        out, h = self.run_audio(AUDIO, pl, 'planned')
        rep = json.load(open(os.path.join(out, 'audio-report.json')))['sfx_real']
        self.assertEqual(sorted(f for v in rep.values() for f in v['files']), sorted(p['file'] for p in pl['sfx_real']['plan'] if p.get('file')))

    def zipfix(self, text):
        z = os.path.join(self.d, 'bundle.zip')
        with zipfile.ZipFile(z, 'w') as f:
            f.writestr('Pub/LICENSE.txt', text)
            f.writestr('Pub/Paper Flip 01.wav', open(os.path.join(ROOT, 'toolkit/factory/world/sfx/lib/S-KEN-BOOKFLIP1.flac'), 'rb').read())
        return z

    def test_k_sonniss(self):
        sys.path.insert(0, os.path.join(os.path.dirname(AUDIO), 'sfx'))
        import sfx_fetch as F
        with self.assertRaises(SystemExit):                                              # mặc định TẮT (chủ dự án 15/10)
            F.sonniss_take(os.path.join(self.d, 'none.zip'), 'GDC T', '2099', [], {})
        r = subprocess.run([sys.executable, os.path.join(ROOT, 'toolkit/factory/world/sfx/sfx_fetch.py'), '--sonniss-license', 'x.zip'],
                           capture_output=True, text=True)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn('TẮT', r.stderr)
        F.SONNISS_ENABLED = True                                                             # đường mã giữ sẵn, thử khi bật
        old = (F.SONNISS_LICENSE, F.LIB, F.CACHE)
        F.SONNISS_LICENSE = os.path.join(self.d, 'sonniss-license.json')
        F.LIB, F.CACHE = os.path.join(self.d, 'lib'), os.path.join(self.d, 'cache')
        try:
            z = self.zipfix('You may use these sounds in commercial projects. You may not redistribute or resell the sounds as is. '
                            'Use for training artificial intelligence is prohibited. No attribution required.')
            L = F.sonniss_license(z)[0]
            self.assertEqual(len(L['sha256']), 64)
            self.assertTrue(L['hint']['ai_training_prohibited'])
            self.assertFalse(L['hint']['raw_redistribution'])
            with self.assertRaises(SystemExit):                                              # chưa xác nhận 4 điểm → dừng
                F.sonniss_gate()
            json.dump({'commercial_video': False, 'attribution_required': False, 'ai_training_prohibited': True, 'raw_redistribution': False},
                      open(F.SONNISS_LICENSE, 'w'))
            with self.assertRaises(SystemExit):                                              # không cho video thương mại → DỪNG
                F.sonniss_take(z, 'GDC T', '2099', [], {})
            json.dump({'commercial_video': True, 'attribution_required': False, 'ai_training_prohibited': True, 'raw_redistribution': False,
                       'license_file': 'Pub/LICENSE.txt', 'license_sha256': '0' * 64}, open(F.SONNISS_LICENSE, 'w'))
            with self.assertRaises(SystemExit):                                              # xác nhận cho license khác → dừng, zip giữ
                F.sonniss_take(z, 'GDC T', '2099', [], {})
            self.assertTrue(os.path.exists(z))
            json.dump({'commercial_video': True, 'attribution_required': False, 'ai_training_prohibited': True, 'raw_redistribution': False,
                       'license_file': 'Pub/LICENSE.txt', 'license_sha256': L['sha256']}, open(F.SONNISS_LICENSE, 'w'))
            with self.assertRaises(SystemExit):                                              # thiếu tệp trong zip → dừng trước giải nén
                F.sonniss_take(z, 'GDC T', '2099', [{'id': 'S-X', 'source': 'sonniss', 'pack': 'GDC T', 'member': 'nope.wav'}], {})
            self.assertTrue(os.path.exists(z))
            man = {}
            picks = [{'id': 'S-SON-T1', 'source': 'sonniss', 'pack': 'GDC T', 'member': 'Pub/Paper Flip 01.wav', 'tags': ['giay']}]
            got = F.sonniss_take(z, 'GDC T', '2099', picks, man)
            self.assertFalse(os.path.exists(z))                                              # zip xoá sau khi lấy
            r = man['S-SON-T1']
            self.assertFalse(r['commit'])
            self.assertTrue(r['file'].startswith('$CRUX_SFX_CACHE'))                           # không vào repo
            self.assertFalse(os.path.exists(os.path.join(F.LIB, 'S-SON-T1.flac')))
            self.assertEqual(F.sha_path(F.resolve(r)), r['sha256'])
            self.assertEqual(F.verify(man), [])
            open(F.resolve(r), 'ab').write(b'x')
            with self.assertRaises(SystemExit):                                              # SHA-256 sai → dừng lúc dựng
                F.resolve(r)
        finally:
            F.SONNISS_LICENSE, F.LIB, F.CACHE = old
            F.SONNISS_ENABLED = False

    def test_l_elevenlabs_off_no_freesound(self):
        sys.path.insert(0, os.path.join(os.path.dirname(AUDIO), 'sfx'))
        import sfx_fetch as F
        calls = []
        old = F.get
        F.get = lambda *a, **k: calls.append(a) or b''
        try:
            with self.assertRaises(SystemExit):
                F.SOURCES['elevenlabs']({'id': 'S-EL-1', 'text': 'coin drop', 'duration_seconds': 1})
        finally:
            F.get = old
        self.assertEqual(calls, [])
        for p in [os.path.join(ROOT, 'toolkit/factory/world/sfx/sfx_fetch.py'), AUDIO]:
            src = open(p).read()
            self.assertNotIn('freesound.org', src)
            self.assertNotIn('FREESOUND', src)


class F18AacPeak(unittest.TestCase):
    def mix(self, audio):
        import types
        sys.path.insert(0, os.path.join(ROOT, 'toolkit', 'factory'))
        import build as BUILD
        d = tempfile.mkdtemp()
        try:
            pic = os.path.join(d, 'pic.mp4')
            ff('-f', 'lavfi', '-i', f'color=c=black:size={W}x{H}:rate={FPS}:duration=4', *SP.encode_args(ENC, FPS), pic)
            t = np.arange(4 * SR) / SR   # tiếng nhiều đỉnh nhọn: AAC vượt đỉnh thật của master
            x = 0.3 * np.sign(np.sin(2 * np.pi * 220 * t)) * (np.sin(2 * np.pi * 2 * t) > 0) + 0.2 * np.sin(2 * np.pi * 3000 * t)
            v = os.path.join(d, 'S01.wav'); sf.write(v, x.astype(np.float32), SR)
            work = os.path.join(d, 'work'); os.makedirs(work)
            B = types.SimpleNamespace(S={'episode': 'epT', 'audio': audio}, tl={'scenes': [{'id': 'S01', 'start': 0.0, 'dur': 4.0}]},
                                      voices={'S01': {'wav': v}}, work=work, picture=pic, total=4.0, root=d, out=d, report={}, fps=FPS)
            B.loudnorm = lambda *a: BUILD.Build.loudnorm(B, *a)
            info = BUILD.Build.do_mix(B)
            return BUILD.true_peak(B.video), BUILD.true_peak(B.master_wav), B.report['music'], info
        finally:
            shutil.rmtree(d, ignore_errors=True)

    def test_m_aac_ceiling(self):
        aac0, m0, rep0, _ = self.mix({'lufs': -14, 'true_peak': -2.0})
        self.assertNotIn('aac_true_peak', rep0)                                   # không khai: như cũ
        self.assertLessEqual(m0, -1.95)
        aac, m, rep, _ = self.mix({'lufs': -14, 'true_peak': -2.0, 'aac_true_peak': -2.0})
        self.assertLessEqual(aac, -2.0)                                           # AAC bản giao ≤ trần
        self.assertLessEqual(m, -2.25)                                            # master đích −2,3
        self.assertEqual(rep['aac_true_peak']['ceiling'], -2.0)
        self.assertEqual(rep['aac_true_peak']['tries'][0]['master_tp_target'], -2.3)


if __name__ == '__main__':
    unittest.main()
