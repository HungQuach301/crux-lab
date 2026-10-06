"""Test thư viện thế giới 3D của nhà máy (Mốc V, D-010): spine v2, lint, luật `world` trong spec. Không mạng, không render.
Bằng chứng render/âm (chạy tay, nặng): build_seg.py dựng lại hai đoạn chứng minh → hình + tiếng trùng MD5 với clip đã duyệt (moc-v/b3).

(a) Anchors: đầu từ / cuối câu / từ đầu câu bỏ thẻ cảm xúc; mốc sai → dừng.
(b) window: nằm giữa hai từ khoá ± pad; cửa sổ < 0,6 s → dừng; late/start.
(c) check_rules: từ khoá trong cửa sổ máy quay → quy tắc 2; thiếu âm → 3; đổi chế độ trước 5 s → 7.
(d) move_sounds/shots_for: mỗi động tác một âm, 'mode' thêm tiếng chạm; cảnh cắt tại đầu động tác.
(e) words_from_timeline: lấy lời đúng các cảnh, giờ tính từ đầu đoạn.
(f) lint_comments bắt mã bị nuốt sau // và #.
(g) spec: `world` thiếu spine.py/scene.js hoặc cảnh lạ → BLOCK.
"""
import json, os, sys, tempfile, unittest
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'factory', 'world')); sys.path.insert(0, os.path.join(HERE, '..', 'factory'))
sys.dont_write_bytecode = True
import spine as SV          # noqa: E402
import lint_comments as LC  # noqa: E402

W = [{'w': '[warm]', 's': 0.0, 'e': 0.1, 'sid': 'S01.1'}, {'w': 'You', 's': 0.2, 'e': 0.4, 'sid': 'S01.1'}, {'w': 'saved', 's': 0.5, 'e': 0.9, 'sid': 'S01.1'},
     {'w': 'ten', 's': 1.0, 'e': 1.2, 'sid': 'S01.1'}, {'w': 'percent.', 's': 1.3, 'e': 1.8, 'sid': 'S01.1'},
     {'w': 'Then', 's': 6.0, 'e': 6.3, 'sid': 'S01.2'}, {'w': 'twenty.', 's': 6.5, 'e': 7.0, 'sid': 'S01.2'}]
B = [('a', 'S01.1', 'world', 'i', 'v', {'ten': '@S01.1:ten'}, [], 0.3, 'e', 'n'), ('b', 'S01.2', 'chart', 'i', 'v', {'tw': '@S01.2:twenty'}, [], 0.5, 'e', 'n')]
LINES = {'S01.1': 'You saved ten percent.', 'S01.2': 'Then twenty.'}


class World(unittest.TestCase):
    def test_a_anchors(self):
        A = SV.Anchors(W)
        self.assertEqual((A.at('@S01.1'), A.at('@S01.1:saved'), A.at('@S01.1$')), (0.2, 0.5, 1.8))
        with self.assertRaises(SystemExit): A.at('@S01.1:nope')
        with self.assertRaises(SystemExit): A.at('S01.1')

    def test_b_window(self):
        self.assertEqual(SV.window(1.0, 6.0, 1.0), [3.0, 4.0])
        self.assertEqual(SV.window(1.0, 6.0, 1.0, late=True), [4.75, 5.75])
        self.assertEqual(SV.window(1.0, 6.0, 1.0, start=2.0), [2.0, 3.0])
        with self.assertRaises(SystemExit): SV.window(1.0, 1.9, 1.0)

    def test_c_rules(self):
        beats = SV.beats_from(B, SV.Anchors(W), LINES)
        ok = {'verb': 'mode', 'from': 'w', 'to': 'c', 't0': 5.0, 't1': 5.9, 'reason': 'r', 'sound': 'whoosh_mode'}
        self.assertEqual(SV.check_rules(beats, [ok], 0.25), [])
        e = SV.check_rules(beats, [dict(ok, t0=0.8, t1=1.5)], 0.25)
        self.assertTrue(any('quy tắc 2' in x for x in e) and any('quy tắc 7' in x for x in e), e)
        self.assertTrue(any('quy tắc 3' in x for x in SV.check_rules(beats, [dict(ok, sound='')], 0.25)))
        self.assertTrue(any('quy tắc 3' in x for x in SV.check_rules(beats, [dict(ok, verb='spin')], 0.25)))

    def test_d_sounds_and_shots(self):
        mv = [{'verb': 'pan', 't0': 2.0, 't1': 3.0, 'sound': 'whoosh_push'}, {'verb': 'mode', 't0': 4.0, 't1': 5.0, 'sound': 'whoosh_mode'}]
        ev = SV.move_sounds(mv, lambda m: 0.5)
        self.assertEqual([e['kind'] for e in ev], ['whoosh_push', 'whoosh_mode', 'land'])
        self.assertEqual([(s['t0'], s['t1']) for s in SV.shots_for(mv, 8)], [(0, 2.0), (2.0, 4.0), (4.0, 8)])

    def test_e_timeline(self):
        tl = {'scenes': [{'id': 'S01', 'start': 0, 'dur': 5}, {'id': 'S02', 'start': 5, 'dur': 4}],
              'words': [{'w': 'a', 's': 1, 'e': 2, 'sid': 'S01.1'}, {'w': 'b', 's': 6, 'e': 7, 'sid': 'S02.1'}]}
        ws, t0, d = SV.words_from_timeline(tl, ['S02'])
        self.assertEqual((ws, t0, d), ([{'w': 'b', 's': 1, 'e': 2, 'sid': 'S02.1'}], 5, 4))
        with self.assertRaises(SystemExit): SV.words_from_timeline(tl, ['S02', 'S01'])

    def test_f_lint(self):
        with tempfile.TemporaryDirectory() as d:
            open(os.path.join(d, 'scene.js'), 'w').write("const a = 1;  // ok comment\nfoo(); // bar.set(1); x.glow(2);\n")
            open(os.path.join(d, 'spine.py'), 'w').write("x = 1  # fine\ny = 2  # ev.append(3)\n")
            bad = LC.lint([d])
            self.assertEqual(len(bad), 2, bad)

    def test_g_spec_world(self):
        import spec as SPEC
        with tempfile.TemporaryDirectory() as d:
            json.dump({'claims': [{'claimId': 'c1', 'display': '1', 'value': 1}]}, open(os.path.join(d, 'claims.json'), 'w'))
            json.dump({'sentences': [{'id': 'S01.1', 'scene': 'S01', 'text': 'Hello.'}]}, open(os.path.join(d, 'script.json'), 'w'))
            base = {'format': '101', 'scope': 'excerpt', 'claims': 'claims.json', 'script': 'script.json', 'counterweights': [],
                    'scenes': [{'id': 'S01', 'shots': []}], 'shorts': [{'id': 'x'}]}
            wb = lambda P: [p for p in P if p['rule'] == 'world']
            self.assertEqual(len(wb(SPEC.check({**base, 'world': [{'id': 'w1', 'dir': 'world/w1', 'scenes': ['S01']}]}, d))), 1)
            os.makedirs(os.path.join(d, 'world/w1'))
            for f in ('spine.py', 'scene.js'): open(os.path.join(d, 'world/w1', f), 'w').write('')
            self.assertEqual(wb(SPEC.check({**base, 'world': [{'id': 'w1', 'dir': 'world/w1', 'scenes': ['S01']}]}, d)), [])
            self.assertEqual(len(wb(SPEC.check({**base, 'world': [{'id': 'w1', 'dir': 'world/w1', 'scenes': ['S09']}]}, d))), 1)


if __name__ == '__main__':
    unittest.main()
