"""Test F-12 (BACKLOG; C3 Tập 6 08/10: nhạc hiệu kênh A + khúc đóng hợp A). Không mạng, không ElevenLabs:
tập giả hai cảnh dựng bằng take thật của Tập 5 (episodes/ep005/voice-takes, mp3 + alignment đã commit) + nhạc hiệu đã duyệt
(toolkit/factory/theme/ident-A.wav, close-A.wav); chạy đúng build.py do_mix (music.mix → music.post → loudnorm 2 lượt → master).

(a) nhạc lên sau chữ cuối (`close_lift_db: 12`, `close_lift_s: 0.5`): master −14 LUFS (±0,3), đỉnh thật ≤ −1 dBTP; lời không bị che:
    A07 (lời trên nhạc, cửa sổ 100 ms có lời) ≥ 19,9 dB sau khi nâng, stem music KHÔNG đổi ở mọi mẫu đang có lời (né 1–4 kHz giữ nguyên),
    và mức nhạc sau t_full đúng +12 dB so với bản không nâng; nâng bắt đầu sau chữ cuối (≥ mốc từ cuối của timeline và lúc lời tắt).
(b) ident (`ident: {after: S01}`): 3 s cuối đuôi S01 = WAV nhạc hiệu (tương quan ≈ 1 với file), nhạc nền về 0 trong cửa sổ; mức ident
    trong master ≈ lời −2 LU; lời lấn vào cửa sổ → dừng.
(c) mặc định tắt: không khai / `close_lift_db: 0` → master.wav, mix-raw, mọi stem và báo cáo trùng từng byte với bản không có F-12.
(d) spec.check: ident thiếu `after`/cảnh lạ/đuôi < 3 s/WAV không có, close_lift_db ngoài 0–24 → BLOCK; khai đúng → 0 lỗi audio.*.
(e) lib3d.js W10 Crates (node + three của vendor; bỏ qua nếu thiếu): litOf = clamp(n·value, 0, n), thùng i sáng clamp(L − i, 0, 1)
    (0,904 → 9 đủ + 4 %; 1,057 → 10, không quá n), userData.checks.level; Check lớn ×1,02^k.
(f) tập thế giới: post() trên stem sau splice (có sfx của đoạn) — chỉ stem music đổi, tổng stem = mix-raw.
In số đo: python3 toolkit/tests/test_factory_f12.py -v
"""
import hashlib, json, os, shutil, subprocess, sys, tempfile, types, unittest
import numpy as np
import soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FACT = os.path.join(ROOT, 'toolkit', 'factory')
sys.path.insert(0, os.path.join(FACT, 'world')); sys.path.insert(0, FACT)
sys.dont_write_bytecode = True
import build as BUILD  # noqa: E402
import music as MUSIC  # noqa: E402
import spec as SPEC  # noqa: E402
import voice as VOICE  # noqa: E402

SR, FPS = 48000, 30
TAKES = os.path.join(ROOT, 'episodes', 'ep005', 'voice-takes')
T1, T2 = 'd773a78c8f8a2f0c', 'ad1275a15657bc26'     # S05 cold open "You've saved ten percent…" · S19 "How we know this…"
THEME = os.path.join(FACT, 'theme')
CLIP_VOICE_TO_TOUCH = 8.421 - 7.14                   # clip duyệt: chữ cuối 7,14 s → điểm chạm khúc đóng 8,421 s
NUM = {}                                             # số đo để in


def sha_file(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def take(name, d):
    j = json.load(open(os.path.join(TAKES, name + '.json')))
    wav = os.path.join(d, name + '.wav')
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', os.path.join(TAKES, name + '.mp3'), '-ar', str(SR), '-ac', '1', wav], check=True)
    al = j['alignment']
    words = VOICE.words_of(j['text'], al['characters'], al['character_start_times_seconds'], al['character_end_times_seconds'])
    return wav, sf.info(wav).duration, words


class Episode:
    """Tập giả: S01 (take T1, đuôi 4 s = 1 s + ident 3 s) · S02 (take T2, đuôi tới hết khúc đóng). Nhạc nền: close-A dưới S01 và
    close-A đặt sao cho chữ cuối → điểm chạm như clip duyệt."""
    def __init__(self, d):
        self.d = d
        (w1, d1, wd1), (w2, d2, wd2) = take(T1, d), take(T2, d)
        s1 = round(round((d1 + 4.0) * FPS) / FPS, 4)
        last = s1 + wd2[-1]['e']
        c0 = last + CLIP_VOICE_TO_TOUCH - 8.421
        total = round(round((c0 + 10.5) * FPS) / FPS, 4)
        self.scenes = [{'id': 'S01', 'start': 0.0, 'dur': s1}, {'id': 'S02', 'start': s1, 'dur': round(total - s1, 4)}]
        self.words = [{**w, 's': w['s'], 'e': w['e']} for w in wd1] + [{**w, 's': round(w['s'] + s1, 3), 'e': round(w['e'] + s1, 3)} for w in wd2]
        self.total, self.c0, self.last = total, c0, last
        self.voices = {'S01': {'wav': w1}, 'S02': {'wav': w2}}
        close, _ = sf.read(os.path.join(THEME, 'close-A.wav'), always_2d=True)
        N = int(round(total * SR)); bed = np.zeros((N, 2))
        bed[:len(close)] += close[:N]
        i = int(round(c0 * SR)); bed[i:i + len(close)] += close[:N - i]
        self.bed = os.path.join(d, 'bed.wav'); sf.write(self.bed, bed, SR, subtype='FLOAT')
        self.picture = os.path.join(d, 'pic.mp4')
        old = BUILD.ENCODE_H; BUILD.ENCODE_H = {'crf': 30, 'preset': 'ultrafast'}
        try:
            BUILD.blank_picture(self.picture, (64, 36), FPS, total)
        finally:
            BUILD.ENCODE_H = old

    def build(self, audio, tag):
        d = os.path.join(self.d, tag); work, out = os.path.join(d, 'work'), os.path.join(d, 'out')
        os.makedirs(work); os.makedirs(out)
        tl = {'fps': FPS, 'total': self.total, 'scenes': self.scenes, 'words': self.words}
        B = types.SimpleNamespace(S={'episode': 'epT', 'audio': audio}, tl=tl, voices=self.voices, work=work, out=out, root=self.d,
                                  total=self.total, fps=FPS, report={}, picture=self.picture)
        B.loudnorm = lambda *a: BUILD.Build.loudnorm(B, *a)
        r = BUILD.Build.do_mix(B)
        stems = {f[:-5]: os.path.join(work, 'stems', f) for f in sorted(os.listdir(os.path.join(work, 'stems')))}
        return types.SimpleNamespace(r=r, info=B.report['music'], master=os.path.join(work, 'master.wav'), raw=os.path.join(work, 'mix-raw.wav'),
                                     stems=stems, video=B.video)


def rd(p):
    return sf.read(p, always_2d=True)[0]


class F12Audio(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = tempfile.mkdtemp()
        cls.E = Episode(cls.d)
        base = {'lufs': -14, 'true_peak': -1.0, 'music': 'bed.wav'}
        cls.base = base
        cls.off = cls.E.build(base, 'off')
        cls.lift = cls.E.build({**base, 'close_lift_db': 12, 'close_lift_s': 0.5}, 'lift')
        cls.ident = cls.E.build({**base, 'close_lift_db': 12, 'ident': {'after': 'S01'}}, 'ident')

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.d, ignore_errors=True)
        if NUM:
            print('\nF-12 số đo:', json.dumps(NUM, ensure_ascii=False), file=sys.stderr)

    def test_a_lift_levels(self):
        L, E = self.lift, self.E
        m = MUSIC.ebur(L.master)
        ma = MUSIC.ebur(L.video)
        NUM.update(master_lufs=m['I_lufs'], master_dbtp=m['tp_dbtp'], aac_lufs=ma['I_lufs'], aac_dbtp=ma['tp_dbtp'])
        self.assertLess(abs(m['I_lufs'] + 14.0), 0.3)
        self.assertLessEqual(m['tp_dbtp'], -1.0)
        cl = L.info['close_lift']
        self.assertGreaterEqual(cl['t0'], E.last)                         # sau chữ cuối của timeline
        self.assertGreaterEqual(cl['t0'], cl['t_voice_off'])              # và sau lúc lời thật tắt
        self.assertLessEqual(cl['t_full'] - cl['t0'], 0.5 + 1e-9)         # đủ +12 dB trong 0,5 s
        self.assertFalse(cl['music_changed_while_voice'])

    def test_a2_voice_not_masked(self):
        L, O = self.lift, self.off
        v, m, m0 = rd(L.stems['voice']), rd(L.stems['music']), rd(O.stems['music'])
        gap = MUSIC.a07_gap(v, m)
        NUM.update(a07_voice_over_music_db=round(gap, 2), a07_without_lift_db=round(MUSIC.a07_gap(v, m0), 2))
        self.assertGreaterEqual(gap, 19.9)
        act, sc = MUSIC.voice_active(v), L.info['post_peak_scale']
        self.assertLess(float(np.abs(m[act] - sc * m0[act]).max()), 1e-4)       # nhạc khi có lời = bản không nâng (né 1–4 kHz giữ nguyên)
        # cửa sổ 100 ms có lời: lời trên nhạc từng cửa sổ (trung vị / phân vị 10)
        w = int(0.1 * SR); k = len(v) // w
        pv = (v[:k * w].mean(1) ** 2).reshape(k, w).mean(1); pm = (m[:k * w].mean(1) ** 2).reshape(k, w).mean(1)
        a = 10 * np.log10(pv + 1e-20) > -45
        loc = 10 * np.log10(pv[a] + 1e-20) - 10 * np.log10(pm[a] + 1e-20)
        NUM.update(local_margin_median_db=round(float(np.median(loc)), 1), local_margin_p10_db=round(float(np.percentile(loc, 10)), 1))
        # nâng đúng +12 dB sau t_full (stem trước master bus; cùng hệ số đỉnh)
        cl = L.info['close_lift']; i = int(cl['t_full'] * SR) + 1
        lift_db = 20 * np.log10(np.sqrt(np.mean(m[i:] ** 2)) / (sc * np.sqrt(np.mean(m0[i:] ** 2))))
        NUM.update(lift_measured_db=round(float(lift_db), 2), t_last_word=cl['t_last_word'], t_full=cl['t_full'])
        self.assertLess(abs(lift_db - 12.0), 0.05)
        # tổng stem = mix-raw
        raw = rd(L.raw)
        self.assertLess(float(np.abs(sum(rd(p) for p in L.stems.values()) - raw).max()), 1e-4)

    def test_b_ident(self):
        I, E = self.ident, self.E
        a, b = MUSIC.ident_window({'scenes': E.scenes}, 'S01')
        self.assertEqual((I.info['ident']['t0'], I.info['ident']['t1']), (a, b))
        m = rd(I.stems['music'])
        x = rd(os.path.join(THEME, 'ident-A.wav'))
        i0 = int(round(a * SR)); seg = m[i0:i0 + len(x)]
        corr = float(np.sum(seg * x) / np.sqrt(np.sum(seg ** 2) * np.sum(x ** 2)))
        self.assertGreater(corr, 0.999)
        res = seg - np.sum(seg * x) / np.sum(x * x) * x                   # nhạc nền về 0 trong cửa sổ: chỉ còn ident
        NUM.update(ident_corr=round(corr, 5), ident_residual_db=round(float(20 * np.log10(np.sqrt(np.mean(res ** 2)) / np.sqrt(np.mean(seg ** 2)))), 1))
        self.assertLess(np.sqrt(np.mean(res ** 2)), 1e-3 * np.sqrt(np.mean(seg ** 2)))
        g = MUSIC.ebur_of(rd(I.master)[i0:i0 + len(x)]); v = MUSIC.ebur_of(rd(I.master)[:int(8.9 * SR)])
        NUM.update(ident_rel_voice_lu=round(g['I_lufs'] - v['I_lufs'], 1), ident_master_lufs=MUSIC.ebur(I.master)['I_lufs'],
                   ident_master_dbtp=MUSIC.ebur(I.master)['tp_dbtp'])
        self.assertLess(abs(g['I_lufs'] - v['I_lufs'] + 2.0), 1.0)
        self.assertLessEqual(MUSIC.ebur(I.master)['tp_dbtp'], -1.0)
        with self.assertRaises(SystemExit):   # cửa sổ ident 3 s mà đuôi S01 chỉ 1 s → lời lấn vào
            tl = {'total': E.total, 'scenes': [{'id': 'S01', 'start': 0.0, 'dur': E.words[len(E.words) // 3]['e'] + 1.0}], 'words': E.words}
            MUSIC.post(os.path.dirname(I.stems['voice']), os.path.join(self.d, 'x.wav'), tl, {'ident': {'after': 'S01'}}, ROOT)

    def test_c_default_off_identical(self):
        O = self.off
        for tag, audio in (('zero', {**self.base, 'close_lift_db': 0}), ('none', {**self.base, 'close_lift_db': None})):
            Z = self.E.build(audio, tag)
            self.assertEqual(Z.info, O.info)
            for k in ('master', 'raw'):
                self.assertEqual(sha_file(getattr(Z, k)), sha_file(getattr(O, k)), f'{tag} {k}')
            self.assertEqual({k: sha_file(p) for k, p in Z.stems.items()}, {k: sha_file(p) for k, p in O.stems.items()})
        d = tempfile.mkdtemp(dir=self.d)   # post() không khai → {} và không chạm file
        for k, p in O.stems.items():
            shutil.copy(p, d)
        before = {f: sha_file(os.path.join(d, f)) for f in os.listdir(d)}
        self.assertEqual(MUSIC.post(d, os.path.join(d, 'raw.wav'), {'total': self.E.total}, {'lufs': -14}, ROOT), {})
        self.assertEqual({f: sha_file(os.path.join(d, f)) for f in os.listdir(d)}, before)

    def test_f_world_stems(self):
        # tập thế giới: post() chạy sau splice.merge_audio trên mọi stem (sfx/sonify/… của đoạn) — chỉ stem music đổi, tổng = mix-raw
        d = tempfile.mkdtemp(dir=self.d)
        for p in self.off.stems.values():
            shutil.copy(p, d)
        N = int(round(self.E.total * SR))
        sf.write(os.path.join(d, 'sfx.flac'), 0.01 * np.random.default_rng(1).standard_normal((N, 2)), SR, subtype='PCM_24')
        keep = {f: sha_file(os.path.join(d, f)) for f in os.listdir(d) if f != 'music.flac'}
        tl = {'total': self.E.total, 'scenes': self.E.scenes, 'words': self.E.words}
        info = MUSIC.post(d, os.path.join(d, 'raw.wav'), tl, {'close_lift_db': 12}, ROOT)
        self.assertEqual(info['post_peak_scale'], 1.0)
        self.assertEqual({f: sha_file(os.path.join(d, f)) for f in keep}, keep)
        tot = sum(rd(os.path.join(d, f)) for f in os.listdir(d) if f.endswith('.flac'))
        self.assertLess(float(np.abs(tot - rd(os.path.join(d, 'raw.wav'))).max()), 1e-4)


class F12Spec(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()
        json.dump({'claims': [{'claimId': 'c1', 'display': '$1', 'value': 1}]}, open(os.path.join(self.d, 'claims.json'), 'w'))
        json.dump({'sentences': [{'id': 'S01.1', 'scene': 'S01', 'text': 'Hello there.'}]}, open(os.path.join(self.d, 'script.json'), 'w'))

    def tearDown(self):
        shutil.rmtree(self.d, ignore_errors=True)

    def check(self, audio, tail=4.0):
        S = {'episode': 'epfake', 'format': '101', 'scope': 'excerpt', 'claims': 'claims.json', 'script': 'script.json',
             'counterweights': [{'id': 'cw', 'text': 'x', 'when': 'historical'}], 'audio': audio,
             'scenes': [{'id': 'S01', 'tail': tail, 'shots': []}]}
        return [p for p in SPEC.check(S, self.d) if p['rule'].startswith('audio.')]

    def test_d_spec(self):
        self.assertEqual(self.check({'ident': {'after': 'S01'}, 'close_lift_db': 12, 'close_lift_s': 0.5}), [])
        self.assertEqual(self.check({'ident': {'after': 'S01', 'wav': 'toolkit/factory/theme/ident-A.wav'}}), [])
        self.assertEqual(self.check({}), [])
        for a, tail in (({'ident': {'after': 'S09'}}, 4.0), ({'ident': {}}, 4.0), ({'ident': 'S01'}, 4.0), ({'ident': {'after': 'S01'}}, 1.0),
                        ({'ident': {'after': 'S01', 'wav': 'nope.wav'}}, 4.0), ({'close_lift_db': 40}, 4.0), ({'close_lift_db': 12, 'close_lift_s': 0}, 4.0)):
            P = self.check(a, tail)
            self.assertEqual([p['level'] for p in P], ['BLOCK'], (a, tail, P))


JS = r"""
import { Crates, Check, litOf, checkScale, CRATE } from './lib3d.js';
const row = Crates({ n: 10 }), lv = (v) => { row.set({ value: v }); return row.userData.crates.map((c) => c.c.userData.checks.level); };
const card = Check({ base: 0.6 });
console.log(JSON.stringify({ lit: [0, 0.05, 0.5, 0.904, 1, 1.057, -0.2].map((v) => litOf(v)), l0904: lv(0.904), l1057: lv(1.057), l0: lv(0),
  ret: row.set({ value: 0.37 }), keys: row.userData.crates.map((c) => c.c.userData.checks.key), width: row.userData.width,
  half: (row.set({ value: 1, appear: 0 }), row.userData.crates.map((c) => c.c.visible)),
  k20: checkScale(20), cardSet: card.set({ k: 20 }), cardLevel: card.userData.checks.level, dark: CRATE.dark }));
"""


def run_js():
    node, three = shutil.which('node'), os.path.join(FACT, 'world', 'vendor', 'node_modules', 'three')
    if not node or not os.path.isdir(three):
        return None
    d = tempfile.mkdtemp()
    try:
        shutil.copy(os.path.join(FACT, 'world', 'lib3d.js'), d)
        os.makedirs(os.path.join(d, 'node_modules')); os.symlink(os.path.abspath(three), os.path.join(d, 'node_modules', 'three'))
        for name, body in (('package.json', '{"type": "module"}'), ('t.js', JS)):
            with open(os.path.join(d, name), 'w') as f:
                f.write(body)
        r = subprocess.run([node, 't.js'], cwd=d, capture_output=True, text=True, timeout=60)
        if r.returncode:
            raise AssertionError(r.stderr)
        return json.loads(r.stdout)
    finally:
        shutil.rmtree(d, ignore_errors=True)


class F12Crates(unittest.TestCase):
    def test_e_crates(self):
        J = run_js()
        if J is None:
            self.skipTest('không có node hoặc vendor/node_modules/three (npm ci trong toolkit/factory/world/vendor)')
        np.testing.assert_allclose(J['lit'], [0, 0.5, 5, 9.04, 10, 10, 0], atol=1e-9)
        np.testing.assert_allclose(J['l0904'], [1] * 9 + [0.04], atol=1e-9)
        self.assertEqual(J['l1057'], [1] * 10)                      # 105,7 % vẫn là 10, không quá n
        self.assertEqual(J['l0'], [0] * 10)
        self.assertAlmostEqual(J['ret'], 3.7)
        self.assertEqual(J['keys'][0], 'crate-row-0'); self.assertEqual(len(set(J['keys'])), 10)
        self.assertAlmostEqual(J['width'], 10 * 0.6 - 0.1)
        self.assertEqual(J['half'], [False] * 10)                    # appear 0: chưa thùng nào mọc
        self.assertAlmostEqual(J['k20'], 1.02 ** 20); self.assertAlmostEqual(J['cardSet'], 1.02 ** 20)
        self.assertEqual(J['cardLevel'], round(1.02 ** 20, 4))
        self.assertEqual(J['dark'], '#3E444D')


if __name__ == '__main__':
    unittest.main()
