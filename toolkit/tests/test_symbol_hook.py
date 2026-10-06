"""Test móc nạp ký hiệu (custom_symbols) của nhà máy dựng, dùng MỘT KÝ HIỆU GIẢ trong thư mục tạm.

Chạy: python3 -m pytest toolkit/tests/test_symbol_hook.py   hoặc   python3 toolkit/tests/test_symbol_hook.py
Không mạng, không render video (node/npm bị thay bằng bản giả ở bước dựng job).

(a) spec không BLOCK template id lạ khi id đó khai trong custom_symbols (và vẫn BLOCK khi không khai).
(b) job do Build.render() ghi ra mang `symbols` [{id, url}] trỏ tới file ký hiệu, và page.html có dòng nạp
    job.symbols vào TEMPLATES. Việc import JS thật trong trình duyệt KHÔNG chạy ở đây (cần chromium/render).
(c) đổi mã file ký hiệu -> code_hash đổi -> băm của từng đoạn render (tên file cache) đổi; không đổi thì giữ nguyên.
(d) KHÔNG KIỂM ĐƯỢC mà không sửa toolkit: spec.check() không kiểm file ký hiệu có tồn tại hay không, nên spec KHÔNG BLOCK
    khi file thiếu (test_d_* ghi lại hành vi thực: spec im lặng, Build.load_inputs() nổ FileNotFoundError ngay sau spec,
    dừng build trước khi tốn API/render, nhưng đó không phải một BLOCK của spec). Muốn đúng "spec BLOCK" cần thêm
    kiểm os.path.exists vào spec.py — việc đó nằm ngoài phạm vi (không được sửa toolkit).
"""
import json, os, subprocess, sys, tempfile, unittest
from types import SimpleNamespace

HERE = os.path.dirname(os.path.abspath(__file__))
FACTORY = os.path.join(HERE, '..', 'factory')
sys.path.insert(0, FACTORY)
sys.dont_write_bytecode = True
import spec as SPEC   # noqa: E402
import build as BUILD  # noqa: E402

JS_V1 = "export const zz9 = (E, p, t) => { E.text('v1'); };\n"
JS_V2 = "export const zz9 = (E, p, t) => { E.text('v2'); };\n"


def make_episode(d, symbols=True, write_js=True):
    """Tập giả tối thiểu: claims/script/tokens/data + yaml khai ký hiệu ZZ9 ở file design/zz9.js."""
    os.makedirs(os.path.join(d, 'design'))
    json.dump({'claims': [{'claimId': 'c1', 'display': '$1', 'value': 1}]}, open(os.path.join(d, 'claims.json'), 'w'))
    json.dump({'sentences': [{'id': 'S01.1', 'scene': 'S01', 'text': 'Hello.'}]}, open(os.path.join(d, 'script.json'), 'w'))
    json.dump({}, open(os.path.join(d, 'tokens.json'), 'w'))
    json.dump({}, open(os.path.join(d, 'data.json'), 'w'))
    if write_js:
        open(os.path.join(d, 'design', 'zz9.js'), 'w').write(JS_V1)
    yml = {'episode': 'epfake', 'format': '101', 'scope': 'excerpt', 'claims': 'claims.json', 'script': 'script.json',
           'tokens': 'tokens.json', 'data': {'file': 'data.json'}, 'counterweights': [{'id': 'cw', 'text': 'x', 'when': 'historical'}],
           'scenes': [{'id': 'S01', 'shots': [{'id': 'S01-a', 'template': 'ZZ9', 'from': '@S01.1', 'p': {'at': '@S01.1'}}]}]}
    if symbols:
        yml['custom_symbols'] = [{'id': 'ZZ9', 'file': 'design/zz9.js'}]
    import yaml
    path = os.path.join(d, 'episode.yaml')
    yaml.safe_dump(yml, open(path, 'w'))
    return path


def load_spec(path):
    import yaml
    return yaml.safe_load(open(path))


def blocks(problems, rule=None):
    return [p for p in problems if p['level'] == 'BLOCK' and (rule is None or p['rule'] == rule)]


class SymbolHook(unittest.TestCase):
    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.d = self._td.name
        self.addCleanup(self._td.cleanup)

    def build_with_inputs(self, path):
        B = BUILD.Build(path, [])
        B.load_inputs()
        return B

    # (a)
    def test_a_declared_symbol_id_is_not_unknown_template(self):
        path = make_episode(self.d)
        P = SPEC.check(load_spec(path), self.d)
        self.assertEqual(blocks(P, 'template'), [], P)

    def test_a_undeclared_id_still_blocks(self):
        path = make_episode(self.d, symbols=False)
        P = SPEC.check(load_spec(path), self.d)
        self.assertEqual(len(blocks(P, 'template')), 1, P)
        self.assertIn('ZZ9', blocks(P, 'template')[0]['msg'])

    # (b)
    def test_b_job_carries_symbol(self):
        path = make_episode(self.d)
        B = self.build_with_inputs(path)
        self.assertEqual([s['id'] for s in B.symbols], ['ZZ9'])
        jobs = []

        def fake_run(cmd, **kw):
            if cmd[0] == 'node':
                jobs.append(json.load(open(cmd[2])))
                return SimpleNamespace(returncode=0, stdout=json.dumps({'render': {'frames': 0, 'seconds': 0}}), stderr='')
            return SimpleNamespace(returncode=0, stdout='/nowhere', stderr='')

        orig = BUILD.subprocess.run
        BUILD.subprocess.run = fake_run
        try:
            B.render('t', [{'id': 'S01-a', 'template': 'ZZ9', 't0': 0, 't1': 1, 'p': {}}], 'h', 1)
        finally:
            BUILD.subprocess.run = orig
        self.assertEqual(len(jobs), 1)
        job = jobs[0]
        self.assertEqual([s['id'] for s in job['symbols']], ['ZZ9'])
        self.assertEqual(job['shots'][0]['template'], 'ZZ9')
        # url -> đúng file mã JS của ký hiệu (url tương đối với gốc repo)
        self.assertEqual(open(BUILD.ROOT + job['symbols'][0]['url']).read(), JS_V1)
        # trang nạp job.symbols vào TEMPLATES
        page = open(os.path.join(FACTORY, 'page.html'), encoding='utf-8').read()
        self.assertIn('job.symbols', page)
        self.assertIn('TEMPLATES[c.id]', page)

    # (c)
    def segment_hashes(self, path):
        B = self.build_with_inputs(path)
        orig = BUILD.subprocess.run
        BUILD.subprocess.run = lambda cmd, **kw: SimpleNamespace(returncode=0, stdout=json.dumps({'render': {}}), stderr='')
        try:
            segs, _ = B.render('t', [{'id': 'S01-a', 'template': 'ZZ9', 't0': 0, 't1': 12, 'p': {}}], 'h', 12)
        finally:
            BUILD.subprocess.run = orig
        return B.code_hash, [s['hash'] for s in segs]

    def test_c_symbol_code_change_changes_cache_hash(self):
        path = make_episode(self.d)
        h1, s1 = self.segment_hashes(path)
        h1b, s1b = self.segment_hashes(path)
        self.assertEqual((h1, s1), (h1b, s1b))  # ổn định khi không đổi
        self.assertGreater(len(s1), 1)
        open(os.path.join(self.d, 'design', 'zz9.js'), 'w').write(JS_V2)
        h2, s2 = self.segment_hashes(path)
        self.assertNotEqual(h1, h2)
        self.assertTrue(set(s1).isdisjoint(s2))  # mọi đoạn đều đổi băm

    # (d) xem docstring đầu file: ghi lại hành vi thực, không khẳng định "spec BLOCK"
    def test_d_missing_file_not_flagged_by_spec_but_stops_load_inputs(self):
        path = make_episode(self.d, write_js=False)
        P = SPEC.check(load_spec(path), self.d)
        self.assertEqual(blocks(P), [], P)  # spec hiện không kiểm file ký hiệu
        B = BUILD.Build(path, [])
        with self.assertRaises(FileNotFoundError):
            B.load_inputs()


if __name__ == '__main__':
    unittest.main()
