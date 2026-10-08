"""Test M6 của mẫu check_script (REVIEWER 08/10): ca gốc Tập 5 — hứa "three illustrative buyers" ở S03.4, tên chỉ ra ở S15 (≈ 4,5 phút).
Chạy: python3 toolkit/tests/test_check_script_m6.py"""
import os, shutil, subprocess, sys, tempfile, unittest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TPL = os.path.join(ROOT, 'playbook', 'templates', 'check_script.py')
EP = os.path.join(ROOT, 'episodes', 'ep005')


def run(role, cast=True):
    with tempfile.TemporaryDirectory() as d:
        os.makedirs(os.path.join(d, 'story'))
        shutil.copy(os.path.join(EP, 'numbers.md'), d)
        shutil.copy(os.path.join(EP, 'episode.yaml'), d)
        src = open(os.path.join(EP, 'story', 'script.md'), encoding='utf-8').read()
        open(os.path.join(d, 'story', 'script.md'), 'w').write(src.replace('S03.4 {promise}', f'S03.4 {{{role}}}'))
        args = [sys.executable, TPL, os.path.join(d, 'story', 'script.md')] + (['--cast', 'Grace,Owen,Victor'] if cast else [])
        return subprocess.run(args, capture_output=True, text=True, cwd=ROOT).stdout


class T(unittest.TestCase):
    def test_tagged_promise_fails_m6(self):
        out = run('promise_character')
        m = __import__('re').search(r'M6 ([\d.]+) s TRƯỢT', out)
        self.assertTrue(m and float(m.group(1)) > 250, out[:200])   # ≈ 4,5 phút: S03.4 → S15

    def test_untagged_person_promise_blocks(self):
        out = run('promise')
        self.assertIn('S03.4: lời hứa về người phải gắn vai promise_character', out)

    def test_no_cast_not_measurable(self):
        out = run('promise_character', cast=False)
        self.assertIn('M6 – s TRƯỢT', out)


if __name__ == '__main__':
    unittest.main()
