"""Test ghép đoạn thế giới vào master (BACKLOG F-5, toolkit/factory/world/splice.py). Không mạng, không render three.js:
master giả (ffmpeg testsrc 4 s, 30 fps; cảnh S01 0–1 s, S02 1–2 s, S03 2–4 s) + đoạn giả (màu đỏ, khác kích thước) thay cảnh S02.

(a) hình: số khung không đổi; khung 30–59 là của đoạn (dò màu); khung ngoài khoảng giữ nguyên (so với master gốc, sai số mã hoá).
(b) thời lượng đoạn ≠ tổng cảnh (29 khung) → dừng; cảnh không liền → dừng.
(c) tiếng: mọi stem cùng độ dài 48 kHz stereo; tổng stem = mix-raw; lời không nhân đôi (stem voice = lời của tập; mix chiếu lên lời = 1);
    sfx của đoạn ở đúng t0 + t (1,5 s), mức theo tỉ lệ lời; data → stem sonify; nhạc nền tập tắt trong khoảng đoạn; stem đoạn sai độ dài → dừng.
(d) build.py do_splice: timeline đánh dấu `world`, nhật ký khung 2D trong khoảng đoạn bị bỏ;
    do_mix sau đó: stem có sfx của đoạn, master 120 khung, out/factory/splice.json có sha256 đầu vào/đầu ra.
"""
import json, os, shutil, subprocess, sys, tempfile, types, unittest
import numpy as np
import soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'factory', 'world')); sys.path.insert(0, os.path.join(HERE, '..', 'factory'))
sys.dont_write_bytecode = True
import splice as SP  # noqa: E402

FPS, W, H, SR = 30, 160, 96, 48000
ENC = {'crf': 10, 'preset': 'ultrafast'}
TL = {'fps': FPS, 'total': 4.0, 'scenes': [{'id': 'S01', 'start': 0.0, 'dur': 1.0}, {'id': 'S02', 'start': 1.0, 'dur': 1.0},
                                            {'id': 'S03', 'start': 2.0, 'dur': 2.0}]}


def ff(*a):
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', *a], check=True)


def frames(p, w=W, h=H):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True, check=True)
    return np.frombuffer(r.stdout, np.uint8).reshape(-1, h, w, 3).astype(float)


def tone(f, dur, a=0.2, t0=0.0, n=None):
    n = n or int(round(dur * SR))
    t = np.arange(n) / SR
    x = a * np.sin(2 * np.pi * f * t) * ((t >= t0) & (t < t0 + dur))
    return np.stack([x, x], 1)


class Splice(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = tempfile.mkdtemp()
        cls.master = os.path.join(cls.d, 'master.mp4')
        ff('-f', 'lavfi', '-i', f'testsrc=size={W}x{H}:rate={FPS}:duration=4', *SP.encode_args(ENC, FPS), cls.master)
        cls.seg = os.path.join(cls.d, 'seg.mp4')        # đoạn khác kích thước (80×48) → splice co giãn về khung master
        ff('-f', 'lavfi', '-i', f'color=c=red:size=80x48:rate={FPS}:duration=1', *SP.encode_args(ENC, FPS), cls.seg)
        cls.short = os.path.join(cls.d, 'short.mp4')
        ff('-f', 'lavfi', '-i', f'color=c=red:size=80x48:rate={FPS}', '-frames:v', '29', *SP.encode_args(ENC, FPS), cls.short)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.d, ignore_errors=True)

    def span(self):
        t0, t1, f0, f1 = SP.scene_span(TL, ['S02'], FPS)
        return {'id': 'w1', 'mp4': self.seg, 't0': t0, 't1': t1, 'f0': f0, 'f1': f1}

    def test_a_video(self):
        out = os.path.join(self.d, 'spliced.mp4')
        r = SP.splice_video(self.master, [self.span()], out, FPS, ENC)
        self.assertEqual(r['frames'], 120)
        a, b = frames(self.master), frames(out)
        self.assertEqual(len(b), 120)
        mid = b[30:60].mean(axis=(1, 2))
        self.assertTrue(np.all(mid[:, 0] > 200) and np.all(mid[:, 1:] < 60), mid[:3])      # đỏ = đoạn
        outside = np.r_[0:30, 60:120]
        diff = np.abs(a[outside] - b[outside]).mean(axis=(1, 2, 3))
        self.assertLess(diff.max(), 4.0)                                                    # giữ nguyên (chỉ sai số mã hoá lại)

    def test_b_timing(self):
        with self.assertRaises(SystemExit):
            SP.splice_video(self.master, [{**self.span(), 'mp4': self.short}], os.path.join(self.d, 'x.mp4'), FPS, ENC)
        with self.assertRaises(SystemExit):
            SP.scene_span(TL, ['S01', 'S03'], FPS)
        self.assertEqual(SP.scene_span(TL, ['S02', 'S03'], FPS), (1.0, 4.0, 30, 120))

    def audio_fixture(self, bed):
        d = tempfile.mkdtemp(dir=self.d)
        ep, sg = os.path.join(d, 'stems'), os.path.join(d, 'seg', 'stems')
        os.makedirs(ep); os.makedirs(sg)
        N = 4 * SR
        voice = tone(220, 4.0, 0.3)
        sf.write(os.path.join(ep, 'voice.flac'), voice, SR, subtype='PCM_24')
        if bed:
            sf.write(os.path.join(ep, 'music.flac'), tone(110, 4.0, 0.05), SR, subtype='PCM_24')
        # đoạn (1 s): stem như world/audio.py, mức × 0,5 (lời đoạn = nửa lời tập → hệ số 2)
        sf.write(os.path.join(sg, 'voice.wav'), (tone(220, 1.0, 0.3) * 0.5).astype(np.float32), SR)
        sf.write(os.path.join(sg, 'sfx.wav'), tone(1000, 0.1, 0.1, t0=0.5, n=SR).astype(np.float32), SR)
        sf.write(os.path.join(sg, 'data.wav'), tone(880, 0.2, 0.05, t0=0.2, n=SR).astype(np.float32), SR)
        sf.write(os.path.join(sg, 'music.wav'), tone(330, 1.0, 0.02).astype(np.float32), SR)
        sf.write(os.path.join(sg, 'room.wav'), np.full((SR, 2), 1e-4, np.float32), SR)
        return ep, sg, voice, N

    def test_c_audio(self):
        ep, sg, voice, N = self.audio_fixture(bed=True)
        raw = os.path.join(self.d, 'mix-raw.wav')
        info = SP.merge_audio(ep, [{**self.span(), 'stems': sg}], 4.0, raw, FPS)
        self.assertEqual(info['segments'][0]['gain_basis'], 'voice_rms')
        self.assertAlmostEqual(info['segments'][0]['gain_db'], 6.02, places=1)
        S = {k: sf.read(p, always_2d=True) for k, p in SP.stem_files(ep).items()}
        self.assertEqual(sorted(S), ['music', 'room', 'sfx', 'sonify', 'voice'])
        for k, (x, sr) in S.items():
            self.assertEqual((sr, x.shape), (SR, (N, 2)), k)
        mix, sr = sf.read(raw, always_2d=True)
        self.assertEqual((sr, mix.shape), (SR, (N, 2)))
        self.assertLess(np.abs(sum(x for x, _ in S.values()) - mix).max(), 1e-5)            # tổng stem = mix-raw
        v = S['voice'][0]
        self.assertLess(np.abs(v - voice).max(), 1e-5)                                       # lời = lời của tập
        span = slice(SR, 2 * SR)
        proj = np.dot(mix[span, 0], voice[span, 0]) / np.dot(voice[span, 0], voice[span, 0])
        self.assertAlmostEqual(proj, 1.0, places=2)                                          # không nhân đôi
        sfx = np.abs(S['sfx'][0][:, 0])
        self.assertEqual(sfx[:int(1.5 * SR) - 5].max(), 0.0)
        on = int(np.argmax(sfx > 0.01))
        self.assertLess(abs(on / SR - 1.5), 0.005)                                           # đúng t0 + 0,5 s
        self.assertAlmostEqual(sfx.max(), 0.2, places=2)                                     # × hệ số lời (2)
        self.assertGreater(np.abs(S['sonify'][0][int(1.2 * SR):int(1.4 * SR)]).max(), 0.05)
        bed = np.abs(S['music'][0][:, 0])
        self.assertLess(np.abs(S['music'][0][int(1.4 * SR):int(1.6 * SR), 0] - tone(330, 1.0, 0.04)[int(0.4 * SR):int(0.6 * SR), 0]).max(), 1e-4)  # chỉ nhạc đoạn
        self.assertGreater(bed[int(3.0 * SR):int(3.1 * SR)].max(), 0.045)                    # nhạc nền ngoài khoảng giữ nguyên
        self.assertGreater(bed[int(0.2 * SR):int(0.3 * SR)].max(), 0.045)

    def test_c2_audio_length_mismatch(self):
        ep, sg, voice, N = self.audio_fixture(bed=False)
        sf.write(os.path.join(sg, 'sfx.wav'), np.zeros((SR // 2, 2), np.float32), SR)
        with self.assertRaises(SystemExit):
            SP.merge_audio(ep, [{**self.span(), 'stems': sg}], 4.0, os.path.join(self.d, 'm.wav'), FPS)

    def test_d_build_step(self):
        import build as BUILD
        d = tempfile.mkdtemp(dir=self.d)
        work, out = os.path.join(d, 'work'), os.path.join(d, 'out')
        os.makedirs(work); os.makedirs(out)
        seg = os.path.join(work, 'w1-1080.mp4')
        os.link(self.seg, seg)
        os.makedirs(os.path.join(work, 'w1-1080.audio', 'stems'))
        json.dump([{'f': f, 'texts': []} for f in range(0, 120, 6)], open(os.path.join(work, 'frame-log.json'), 'w'))
        tl = json.loads(json.dumps(TL))
        tl['shots'] = [{'id': 'a', 'scene': 'S01'}, {'id': 'b', 'scene': 'S02'}, {'id': 'c', 'scene': 'S03'}]
        B = types.SimpleNamespace(S={'episode': 'epT', 'world': [{'id': 'w1', 'dir': 'x', 'scenes': ['S02']}]}, tl=tl, world={'w1': seg},
                                  picture=self.master, work=work, out=out, fps=FPS)
        old = BUILD.ENCODE_H
        BUILD.ENCODE_H = ENC
        try:
            r = BUILD.Build.do_splice(B)
        finally:
            BUILD.ENCODE_H = old
        self.assertEqual((r['frames'], r['frame_log_dropped']), (120, 5))
        T = json.load(open(os.path.join(out, 'timeline.json')))
        self.assertEqual([s.get('world') for s in T['scenes']], [None, 'w1', None])
        self.assertEqual([s.get('world') for s in T['shots']], [None, 'w1', None])
        self.assertEqual(T['world'], [{'id': 'w1', 'scenes': ['S02'], 't0': 1.0, 't1': 2.0, 'f0': 30, 'f1': 60}])
        self.assertTrue(all(not 30 <= x['f'] < 60 for x in json.load(open(os.path.join(work, 'frame-log.json')))))
        self.assertEqual(B.splice_rec['segments'][0]['frames'], 30)
        self.assertEqual(B.picture, os.path.join(work, 'picture-spliced.mp4'))
        # mix: lời của tập (một wav mỗi cảnh) + lớp của đoạn → stem, loudnorm, master
        ep, sg, voice, N = self.audio_fixture(bed=False)
        for f in os.listdir(sg):
            shutil.copy(os.path.join(sg, f), os.path.join(work, 'w1-1080.audio', 'stems', f))
        B.voices = {}
        for sc in TL['scenes']:
            w = os.path.join(d, sc['id'] + '.wav')
            sf.write(w, voice[int(sc['start'] * SR):int((sc['start'] + sc['dur']) * SR)], SR)
            B.voices[sc['id']] = {'wav': w}
        B.total, B.root, B.report = 4.0, d, {}
        B.loudnorm = lambda *a: BUILD.Build.loudnorm(B, *a)
        r = BUILD.Build.do_mix(B)
        rep = json.load(open(os.path.join(out, 'splice.json')))
        self.assertEqual(sorted(rep['audio']['stems_sha256']), ['music', 'room', 'sfx', 'sonify', 'voice'])
        self.assertEqual(len(rep['picture']['out_sha256']), 64)
        self.assertEqual(rep['video']['sha256'], r['sha256'])
        self.assertEqual(SP.probe_video(B.video)['frames'], 120)
        x, _ = sf.read(os.path.join(work, 'stems', 'sfx.flac'), always_2d=True)
        self.assertEqual(len(x), N)
        self.assertLess(abs(np.argmax(np.abs(x[:, 0]) > 0.01) / SR - 1.5), 0.005)


if __name__ == '__main__':
    unittest.main()
