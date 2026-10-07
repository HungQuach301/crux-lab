"""Test luật B+2 (Mốc V): ≤ 2 số MỚI được NÓI mỗi cảnh (toolkit/factory/numbers_said.py, BLOCK 'spoken_numbers' trong spec.py).

Chạy: python3 toolkit/tests/test_numbers_said.py   (cần node cho toolkit/voice/normalize.js; không mạng)
(a) số có đơn vị được bắt sau chuẩn hoá lời; số đếm không đơn vị ("three illustrative buyers") không tính.
(b) cảnh có 3 số mới -> BLOCK, thông báo nêu đủ 3 số và câu chứa nó; 2 số mới -> không BLOCK.
(c) số đã nói ở cảnh trước là "lặp lại", không tính vào ngưỡng.
(d) Tập 5 S03 thật (bản trước B+2) -> BLOCK; bản sửa (bỏ "two years" khỏi lời, đưa lên nhãn) -> qua.
(e) spec.check() đưa BLOCK 'spoken_numbers' vào danh sách vấn đề.
"""
import os, sys, unittest
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'factory'))
sys.dont_write_bytecode = True
import numbers_said as NS  # noqa: E402
import voice as VOICE      # noqa: E402

S03_BEFORE = ["On paper means the loan is 80 percent of the home's value by a national price index.",
              "That's not the same as getting the insurance removed.",
              "Removal on today's value, when you ask, is the loan owner's rule; for Fannie Mae loans, that's two years and a 75 percent bar.",
              "You'll also meet three illustrative buyers who got very different answers."]
S03_AFTER = S03_BEFORE[:2] + ["Removal on today's value, when you ask, is the loan owner's rule; for Fannie Mae loans, that's a waiting period and a 75 percent bar.", S03_BEFORE[3]]


def run(texts, scenes=None, limit=2):
    sents = [{'id': f'{(scenes or ["S03"] * len(texts))[i]}.{i + 1}', 'scene': (scenes or ['S03'] * len(texts))[i]} for i in range(len(texts))]
    return NS.check_scenes(sents, VOICE.to_spoken(texts), limit)


class NumbersSaid(unittest.TestCase):
    def test_a_units_only(self):
        rep, _ = run([S03_BEFORE[3], 'It took 23 months.'])
        self.assertEqual([n['text'] for n in rep['S03']['new']], ['twenty-three months'])

    def test_b_three_new_blocks_two_passes(self):
        _, P = run(['It fell 10 percent, then 20 percent, over 8 years.'])
        self.assertEqual(len(P), 1)
        self.assertEqual(P[0]['rule'], 'spoken_numbers')
        for t in ('ten percent', 'twenty percent', 'eight years', 'S03.1'):
            self.assertIn(t, P[0]['msg'])
        self.assertEqual(run(['It fell 10 percent, then 20 percent.'])[1], [])

    def test_c_repeats_do_not_count(self):
        rep, P = run(['It was 10 percent and 20 percent.', 'Again 10 percent, 20 percent, and 30 percent.'], ['S01', 'S02'])
        self.assertEqual(P, [])
        self.assertEqual(len(rep['S02']['repeat']), 2)

    def test_d_episode5_s03_before_after(self):
        _, P = run(S03_BEFORE)
        self.assertEqual(len(P), 1)
        self.assertIn('two years', P[0]['msg'])
        rep, P = run(S03_AFTER)
        self.assertEqual(P, [])
        self.assertEqual([n['text'] for n in rep['S03']['new']], ['eighty percent', 'seventy-five percent'])

    def test_e_spec_check_blocks(self):
        import json, tempfile, yaml
        import spec as SPEC
        with tempfile.TemporaryDirectory() as d:
            json.dump({'claims': [{'claimId': 'c1', 'display': '1', 'value': 1}]}, open(os.path.join(d, 'claims.json'), 'w'))
            json.dump({'sentences': [{'id': 'S01.1', 'scene': 'S01', 'text': 'It fell 10 percent, then 20 percent, over 8 years.'}]},
                      open(os.path.join(d, 'script.json'), 'w'))
            spec = {'format': '101', 'scope': 'excerpt', 'claims': 'claims.json', 'script': 'script.json', 'counterweights': [],
                    'scenes': [{'id': 'S01', 'shots': []}], 'shorts': [{'id': 'x'}]}
            P = SPEC.check(spec, d)
            self.assertEqual([p['rule'] for p in P if p['level'] == 'BLOCK'], ['spoken_numbers'])


if __name__ == '__main__':
    unittest.main()
