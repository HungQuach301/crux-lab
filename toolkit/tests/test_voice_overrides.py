"""Test voice_overrides (Mốc V B+1): seed/take theo cảnh trong episode.yaml.

Chạy: python3 -m pytest toolkit/tests/test_voice_overrides.py   hoặc   python3 toolkit/tests/test_voice_overrides.py
Không mạng: `requests` bị khoá; take giả là mp3 tạo bằng ffmpeg trong thư mục tạm.

(a) không khai voice_overrides → scene_cfg trả CHÍNH đối tượng cấu hình chung → khoá SHA-256, take, file đều như trước (giống hệt).
(b) {seed: N} chỉ đổi seed của cảnh đó (khoá đổi), cảnh khác giữ nguyên.
(c) {take: <tên>} dùng đúng take đó, không gọi API; chữ của take khác chữ cảnh → dừng.
(d) spec.check() BLOCK: cảnh không có trong tập, khoá lạ, take không có trong voice-takes/.
(e) Build.do_voice() truyền cấu hình theo cảnh (override chỉ tới đúng cảnh).
Ca thật (Tập 5 S18 seed 1006, ASR "illustrative"): moc-v/b1/b1_check.py → moc-v/b1/b1-ep005.json.
"""
import hashlib, json, os, subprocess, sys, tempfile, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'factory'))
sys.dont_write_bytecode = True
sys.modules['requests'] = None   # không mạng
import voice as V   # noqa: E402
import spec as SPEC  # noqa: E402
import build as BUILD  # noqa: E402

BASE = {'provider': 'elevenlabs', 'voice': 'vX', 'model': 'm', 'seed': 1005, 'settings': {'stability': 0.5, 'speed': 0.9}}


def fake_take(d, text, seed=1005, name=None):
    """Take giả: mp3 1 s + json (khoá đúng công thức voice.py, alignment từng ký tự)."""
    settings = BASE['settings']
    key = hashlib.sha256(json.dumps([text, BASE['voice'], BASE['model'], seed, settings], sort_keys=True).encode()).hexdigest()
    name = name or key[:16]
    os.makedirs(d, exist_ok=True)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'lavfi', '-i', 'sine=f=220:d=1', os.path.join(d, name + '.mp3')], check=True)
    n = len(text)
    json.dump({'key': key, 'text': text, 'voice': BASE['voice'], 'model': BASE['model'], 'seed': seed, 'settings': settings, 'chars': n,
               'alignment': {'characters': list(text), 'character_start_times_seconds': [i / n for i in range(n)],
                             'character_end_times_seconds': [(i + 1) / n for i in range(n)]}}, open(os.path.join(d, name + '.json'), 'w'))
    return name


class VoiceOverrides(unittest.TestCase):
    def setUp(self):
        self._td = tempfile.TemporaryDirectory(); self.d = self._td.name; self.addCleanup(self._td.cleanup)
        self.sents = [{'id': 'S01.1', 'scene': 'S01', 'text': 'Hello there.'}]
        self.text = V.to_spoken(['Hello there.'])[0]

    def test_a_no_override_is_identical(self):
        self.assertIs(V.scene_cfg(BASE, None, 'S01'), BASE)
        self.assertIs(V.scene_cfg(BASE, {}, 'S01'), BASE)
        self.assertIs(V.scene_cfg(BASE, {'S02': {'seed': 7}}, 'S01'), BASE)
        name = fake_take(os.path.join(self.d, 'vt'), self.text)
        v = V.voice_scene(V.scene_cfg(BASE, None, 'S01'), self.sents, os.path.join(self.d, 'vt'), os.path.join(self.d, 'w'))
        self.assertTrue(v['cached']); self.assertEqual(os.path.basename(v['mp3']), name + '.mp3')

    def test_b_seed_only_for_that_scene(self):
        c = V.scene_cfg(BASE, {'S01': {'seed': 1006}}, 'S01')
        self.assertEqual(c['seed'], 1006); self.assertEqual({k: v for k, v in c.items() if k != 'seed'}, {k: v for k, v in BASE.items() if k != 'seed'})
        self.assertEqual(BASE['seed'], 1005)   # cấu hình chung không bị sửa
        n1006 = fake_take(os.path.join(self.d, 'vt'), self.text, seed=1006)
        v = V.voice_scene(c, self.sents, os.path.join(self.d, 'vt'), os.path.join(self.d, 'w'))
        self.assertEqual(os.path.basename(v['mp3']), n1006 + '.mp3'); self.assertEqual(v['take']['seed'], 1006)

    def test_c_take_override(self):
        name = fake_take(os.path.join(self.d, 'vt'), self.text, seed=1999, name='aaaabbbbccccdddd')
        v = V.voice_scene(V.scene_cfg(BASE, {'S01': {'take': name}}, 'S01'), self.sents, os.path.join(self.d, 'vt'), os.path.join(self.d, 'w'))
        self.assertTrue(v['cached'])
        other = [{'id': 'S01.1', 'scene': 'S01', 'text': 'Different words.'}]
        with self.assertRaises(SystemExit):
            V.voice_scene(V.scene_cfg(BASE, {'S01': {'take': name}}, 'S01'), other, os.path.join(self.d, 'vt'), os.path.join(self.d, 'w'))
        with self.assertRaises(SystemExit):
            V.scene_cfg(BASE, {'S01': {'pitch': 3}}, 'S01')

    def _spec(self, ov):
        json.dump({'claims': [{'claimId': 'c1', 'display': '$1', 'value': 1}]}, open(os.path.join(self.d, 'claims.json'), 'w'))
        json.dump({'sentences': self.sents}, open(os.path.join(self.d, 'script.json'), 'w'))
        os.makedirs(os.path.join(self.d, 'voice-takes'), exist_ok=True)
        fake_take(os.path.join(self.d, 'voice-takes'), self.text, name='1111222233334444')
        return {'episode': 'epfake', 'format': '101', 'scope': 'excerpt', 'claims': 'claims.json', 'script': 'script.json',
                'counterweights': [{'id': 'cw', 'text': 'x', 'when': 'historical'}], 'voice': BASE, 'voice_overrides': ov,
                'scenes': [{'id': 'S01', 'shots': []}]}

    def test_d_spec_blocks(self):
        rule = lambda P: [p for p in P if p['level'] == 'BLOCK' and p['rule'] == 'voice_overrides']
        self.assertEqual(rule(SPEC.check(self._spec({'S01': {'seed': 1006}}), self.d)), [])
        self.assertEqual(rule(SPEC.check(self._spec({'S01': {'take': '1111222233334444'}}), self.d)), [])
        self.assertEqual(len(rule(SPEC.check(self._spec({'S09': {'seed': 1}}), self.d))), 1)
        self.assertEqual(len(rule(SPEC.check(self._spec({'S01': {'pitch': 1}}), self.d))), 1)
        self.assertEqual(len(rule(SPEC.check(self._spec({'S01': {'take': 'nope'}}), self.d))), 1)

    def test_e_build_passes_scene_cfg(self):
        seen = {}
        B = BUILD.Build.__new__(BUILD.Build)
        B.S = {'voice': BASE, 'voice_overrides': {'S02': {'seed': 1006}}, 'scenes': [{'id': 'S01'}, {'id': 'S02'}]}
        B.script = {'S01.1': {'id': 'S01.1', 'scene': 'S01', 'text': 'a'}, 'S02.1': {'id': 'S02.1', 'scene': 'S02', 'text': 'b'}}
        B.root, B.work = self.d, self.d
        orig = BUILD.VOICE.voice_scene
        BUILD.VOICE.voice_scene = lambda cfg, sents, *a: seen.setdefault(sents[0]['scene'], cfg) and {'cached': True, 'chars': 0}
        try:
            B.do_voice()
        finally:
            BUILD.VOICE.voice_scene = orig
        self.assertIs(seen['S01'], BASE); self.assertEqual(seen['S02']['seed'], 1006)


if __name__ == '__main__':
    unittest.main(verbosity=2)
