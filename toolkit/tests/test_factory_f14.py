"""F-14 (BACKLOG): cờ change/anchor + cảnh báo quãng > 8 s, quy tắc 7 chỉ 5 s đầu tập, nhãn neo vào từ ±0,2 s, life có `what`.
Không khai F-14 → hành vi cũ (spine.json của Tập 6 sinh lại trùng byte: kiểm bằng tay khi đổi spine.py, xem toolkit/factory/f14/REPORT.md)."""
import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'factory', 'world'))
import spine as SV  # noqa: E402


def sp(**kw):
    words = [{'w': f'w{i}', 's': i * 0.5, 'e': i * 0.5 + 0.4, 'sid': 'S01.1'} for i in range(40)]   # lời 0–19,9 s
    base = {'total': 20.0, 'episode_t0': 100.0, 'words': words, 'f14': 1,
            'beats': [{'id': 'b0', 'mode': 'chart', 'cues': {'a': 2.0, 'b': 9.0, 'c': 15.0}}], 'moves': []}
    base.update(kw)
    return base


class F14(unittest.TestCase):
    def test_rule7_episode_only(self):
        beats = [{'id': 'b0', 'mode': 'chart', 'cues': {}}]
        mv = [{'verb': 'mode', 't0': 1.0, 't1': 2.0, 'reason': 'r', 'sound': 's'}]
        self.assertTrue(any('quy tắc 7' in e for e in SV.check_rules(beats, mv, 0.25)))                 # cách cũ: mọi đoạn
        self.assertFalse(SV.check_rules(beats, mv, 0.25, episode_t0=455.0))                                # đoạn giữa tập: không buộc
        self.assertTrue(any('TẬP' in e for e in SV.check_rules(beats, mv, 0.25, episode_t0=0.0)))          # đoạn đầu tập: vẫn buộc

    def test_still_major_warns(self):
        s = sp()
        self.assertEqual(len(SV.still_major(s)), 1)                        # không major nào: 0–19,9 s
        s['changes'] = {'b0.a': 'major', 'b0.b': 'major', 'b0.c': 'major'}
        self.assertEqual(SV.still_major(s), [])                            # khoảng dài nhất 9→15 = 6 s
        s['changes']['b0.b'] = 'minor'
        self.assertEqual([x['dur'] for x in SV.still_major(s)], [12.9])    # từ 2,0–14,9 s
        errs, warn = SV.check_f14(s)
        self.assertFalse(errs); self.assertEqual(len(warn), 1)

    def test_mode_move_is_major_by_default(self):
        s = sp(moves=[{'id': 'm', 'verb': 'mode', 't0': 9.0, 't1': 10.0}, {'id': 'p', 'verb': 'pan', 't0': 4.0, 't1': 5.0}])
        self.assertEqual([m[2] for m in SV.major_changes(s)], ['m'])

    def test_label_anchor(self):
        s = sp(label_at={'b0.a': 2.15})
        self.assertFalse(SV.check_f14(s)[0])
        s['label_at']['b0.a'] = 3.3                                        # trễ 1,3 s (kiểu "3%" Tập 6)
        self.assertTrue(any('F-14 (c)' in e for e in SV.check_f14(s)[0]))

    def test_life_needs_meaning(self):
        s = sp(life={'row': {'keys': [[0, 1], [5, 0.9]]}})
        self.assertTrue(any('what' in e for e in SV.check_f14(s)[0]))
        s['life']['row']['what'] = 'sức mua theo năm của câu'
        self.assertFalse(SV.check_f14(s)[0])
        s['changes'] = {'b0.x': 'big'}
        self.assertEqual(len(SV.check_f14(s)[0]), 2)                        # sai mức + cue không có


if __name__ == '__main__':
    unittest.main()
