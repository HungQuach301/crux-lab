"""Test comment_guard (tổng kết Tập 5 mục 13; cine-lab #42, #76). Chạy: python3 toolkit/tests/test_comment_guard.py"""
import os, sys, tempfile, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import comment_guard as G  # noqa: E402


def mk(d, name, text):
    p = os.path.join(d, name)
    open(p, 'w').write(text)
    return p


class T(unittest.TestCase):
    def test_js_swallowed_assignment(self):   # cine-lab #76: lệnh đặt vị trí bị nuốt, không lỗi cú pháp
        with tempfile.TemporaryDirectory() as d:
            mk(d, 'scene.js', "const p = {position: {x: 0}};\nfoo(1);   // note p.position.x = 2;\n")
            bad, _ = G.check([d])
            self.assertTrue(any('scene.js:2' in b for b in bad), bad)

    def test_js_swallowed_call(self):
        with tempfile.TemporaryDirectory() as d:
            mk(d, 'scene.js', "let a = 1;   // giữ a; draw(a);\n")
            self.assertTrue(G.check([d])[0])

    def test_py_swallowed_append(self):      # cine-lab #76: `: nohero.append` bị nuốt
        with tempfile.TemporaryDirectory() as d:
            mk(d, 'cont.py', "nohero = []\nfor x in [1]:\n    if x:  # chú thích: nohero.append(x)\n        pass\n")
            self.assertTrue(G.check([d])[0])

    def test_js_syntax_error(self):
        with tempfile.TemporaryDirectory() as d:
            mk(d, 'scene.js', "export function f( {\n")
            bad, _ = G.check([d])
            self.assertTrue(any('node --check' in b for b in bad), bad)

    def test_clean_and_prose_comment(self):
        with tempfile.TemporaryDirectory() as d:
            mk(d, 'scene.js', "import * as T from 'three';\nexport const a = 1;   // C5b: O.card = thẻ nền (không tính chữ)\nconst u = 'http://x//y';\n")
            mk(d, 'spine.py', "x = 1  # 2 s mỗi mốc\n")
            self.assertEqual(G.check([d])[0], [])

    def test_real_case_moc_v(self):          # lỗi thật còn trong đoạn chứng minh Mốc V (E5k), đã sửa khi port sang Tập 5
        bad, _ = G.check([os.path.join(G.ROOT, 'moc-v', 'seg', 'ep005')])
        self.assertTrue(any('moc-v/seg/ep005/scene.js:98' in b for b in bad), bad)

    def test_factory_and_ep005_clean(self):
        bad, n = G.check([os.path.join(G.ROOT, 'toolkit', 'factory', 'world'), os.path.join(G.ROOT, 'episodes', 'ep005', 'world')])
        self.assertEqual(bad, [])
        self.assertGreater(n, 30)


if __name__ == '__main__':
    unittest.main()
