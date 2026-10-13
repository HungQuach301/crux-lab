"""F-15 (toolkit/factory/f15/INTENT.md): test hoá kỷ luật phiên Tập 7 (TONGKET i, p; cine-lab #24, #41, #42, #66, #67, #70, #76, #94, #110).
Chạy: python3 -m unittest toolkit.tests.test_factory_f15   (hoặc python3 toolkit/tests/test_factory_f15.py)
  a  comment_guard + node --check / py_compile trên thư viện thế giới và MỌI mã cảnh của tập đang làm (ep007 trở đi)
  b  cấm `pkill -f` / `pgrep -f` / `killall` trong mã (dừng tiến trình bằng PID; tập 1–6 đã đóng băng không quét)
  c  khoá YAML boolean: `on/off/yes/no/y/n` không ngoặc → spec BLOCK; mọi episode.yaml hiện có: 0
  d  pipefail ở mọi script cổng (toolkit/**/*.sh và script tập ≥ ep007 có ống `|`)
  e  worker ≤ số nhân − 1 (guard.max_workers), CRUX_ALL_CORES=1 bỏ giới hạn
  f  bg.sh: setsid nohup, mã thoát, dừng theo PID nhóm
  g  api.sh: chặn agent con (Task, Agent, Workflow) + trần chi theo lệnh (--max-budget-usd)
  h  render_shots.js --resume: ngắt giữa cảnh rồi chạy lại → tệp cảnh trùng byte lượt không ngắt và lượt ống (không --resume)
  i  build nguyên tử: rel() trả đường đích, promote() thay bản cũ; lượt trượt không chạm bản cũ
  j  không cờ F-15: render_shots khung trùng MD5 với khi khai --spp mặc định bỏ trống (tham số trang không đổi)
"""
import glob, hashlib, json, os, re, shutil, subprocess, sys, tempfile, time, types, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path[:0] = [HERE, os.path.join(ROOT, 'toolkit', 'factory'), os.path.join(ROOT, 'toolkit', 'factory', 'world')]
sys.dont_write_bytecode = True
import comment_guard  # noqa: E402
import guard  # noqa: E402
import spec as SPEC  # noqa: E402

FROZEN = re.compile(r'^episodes/ep00[1-6]/')   # tập đã phát hành trước F-15: không sửa, không quét luật mới
VENDOR = os.path.join(ROOT, 'toolkit', 'factory', 'world', 'vendor', 'node_modules', 'three')


def tracked(*globs):
    out = subprocess.run(['git', 'ls-files', *globs], cwd=ROOT, capture_output=True, text=True).stdout.split()
    return [f for f in out if not FROZEN.match(f)]


class F15(unittest.TestCase):
    def test_a_comment_guard_scene_code(self):
        dirs = [os.path.join(ROOT, 'toolkit', 'factory', 'world')]
        for ep in sorted(glob.glob(os.path.join(ROOT, 'episodes', 'ep*'))):
            if int(re.sub(r'\D', '', os.path.basename(ep)) or 0) >= 7 and os.path.isdir(os.path.join(ep, 'world')):
                dirs += sorted({os.path.dirname(p) for p in glob.glob(os.path.join(ep, 'world', '**', 'scene.js'), recursive=True)})
        bad, n = comment_guard.check(dirs)
        self.assertGreater(n, 10)
        self.assertEqual(bad, [], '\n'.join(bad))

    def test_b_no_pkill_f(self):
        rx = re.compile(r'\b(pkill\s+-f|pgrep\s+-f|killall)\b')
        hits = []
        for f in tracked('*.sh', '*.py', '*.js', '*.mjs'):
            for i, ln in enumerate(open(os.path.join(ROOT, f), errors='replace'), 1):
                code = ln.split('#', 1)[0] if f.endswith(('.sh', '.py')) else ln.split('//', 1)[0]
                if rx.search(code) and 'rx = re.compile' not in ln:
                    hits.append(f'{f}:{i}: {ln.strip()[:100]}')
        self.assertEqual(hits, [], 'dừng tiến trình bằng PID (cine-lab #24, #41):\n' + '\n'.join(hits))

    def test_c_yaml_bool_lock(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, 'episode.yaml')
            open(p, 'w').write('audio:\n  ident: {after: on}\n  flag: true\ncountry: NO\nquoted: "yes"\non: 1\n')
            traps = SPEC.yaml_bool_traps(p)
            self.assertEqual(sorted(t[2] for t in traps), ['NO', 'on', 'on'], traps)
            P = SPEC.check({'format': 'nope'}, d)
            self.assertTrue(any(x['rule'] == 'yaml-bool' and x['level'] == 'BLOCK' for x in P), P)
        for y in sorted(glob.glob(os.path.join(ROOT, 'episodes', '*', 'episode.yaml'))):
            self.assertEqual(SPEC.yaml_bool_traps(y), [], y)

    def test_d_pipefail_gates(self):
        miss = []
        for f in tracked('toolkit/*.sh', 'toolkit/**/*.sh', 'episodes/*.sh', 'episodes/**/*.sh'):
            src = open(os.path.join(ROOT, f)).read()
            code = '\n'.join(l.split('#', 1)[0] for l in src.splitlines())
            if re.search(r'[^|]\|[^|]', code) and not re.search(r'set -[a-z]*o pipefail|set -o pipefail', src) and 'PIPESTATUS' not in src:
                miss.append(f)
        self.assertEqual(miss, [], 'script cổng có ống mà không pipefail/PIPESTATUS (cine-lab #67)')

    def test_e_max_workers(self):
        n = os.cpu_count() or 2
        old = os.environ.pop('CRUX_ALL_CORES', None)
        try:
            self.assertEqual(guard.max_workers(64), max(1, n - 1))
            self.assertEqual(guard.max_workers(1), 1)
            os.environ['CRUX_ALL_CORES'] = '1'
            self.assertEqual(guard.max_workers(64), 64)
        finally:
            os.environ.pop('CRUX_ALL_CORES', None)
            if old is not None:
                os.environ['CRUX_ALL_CORES'] = old

    def test_f_bg_sh(self):
        with tempfile.TemporaryDirectory() as d:
            env = {**os.environ, 'CRUX_BG': d}
            bg = ['bash', os.path.join(ROOT, 'toolkit', 'bg.sh')]
            r = subprocess.run(bg + ['start', 'x', '--no-guard', '--', 'bash', '-c', 'echo hi; exit 7'], env=env, capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            r = subprocess.run(bg + ['wait', 'x', '60'], env=env, capture_output=True, text=True)
            self.assertEqual(r.returncode, 7, r.stdout)
            self.assertEqual(open(os.path.join(d, 'x.log')).read().strip(), 'hi')
            subprocess.run(bg + ['start', 'y', '--no-guard', '--', 'bash', '-c', 'sleep 300 & sleep 300'], env=env, check=True, capture_output=True)
            pid = int(open(os.path.join(d, 'y.pid')).read())
            self.assertEqual(os.getpgid(pid), pid)   # setsid: nhóm riêng → stop giết đúng cây
            subprocess.run(bg + ['stop', 'y'], env=env, check=True, capture_output=True)
            time.sleep(0.5)
            alive = subprocess.run(['ps', '-o', 'pid=', '-g', str(pid)], capture_output=True, text=True).stdout.split()
            self.assertEqual(alive, [])
            self.assertEqual(open(os.path.join(d, 'y.rc')).read().strip(), '143')

    def test_g_api_sh_static(self):
        src = open(os.path.join(ROOT, 'toolkit', 'api.sh')).read()
        self.assertIn('--disallowedTools "Task,Agent,Workflow"', src)
        self.assertIn('--max-budget-usd "$cap"', src)
        self.assertNotIn('Bash(*)', src)

    def _seg(self, d):
        seg = os.path.join(d, 'seg')
        os.makedirs(seg)
        json.dump({'total': 0.6, 'shots': [{'id': 's1', 't0': 0.0, 't1': 0.6}]}, open(os.path.join(seg, 'spine.json'), 'w'))
        open(os.path.join(seg, 'scene.js'), 'w').write(
            "export async function boot(res) {\n"
            "  const c = document.createElement('canvas'); c.width = Math.round(1920 * res / 1080); c.height = res; const g = c.getContext('2d');\n"
            "  return { canvas: c, frame(t) {\n"
            "    g.fillStyle = '#123044'; g.fillRect(0, 0, c.width, c.height); g.fillStyle = '#f2b134'; g.fillRect(20 + t * 300, 40, 80, 60);\n"
            "    g.fillStyle = '#fff'; g.font = '40px sans-serif'; g.fillText('t=' + t.toFixed(2), 30, 200);\n"
            "    return { violations: [], cam: { x: t } }; } };\n"
            "}\n")
        return seg

    def _render(self, seg, cache, extra=(), env=None):
        npm = subprocess.run(['npm', 'root', '-g'], capture_output=True, text=True).stdout.strip()
        out = os.path.join(cache, 'out.mp4')
        r = subprocess.run(['node', os.path.join(ROOT, 'toolkit', 'factory', 'world', 'render_shots.js'), os.path.relpath(seg, ROOT), '360', out,
                            '--workers', '1', '--cache', cache, *extra], cwd=ROOT, capture_output=True, text=True,
                           env={**os.environ, 'NODE_PATH': npm, **(env or {})})
        files = sorted(glob.glob(os.path.join(cache, 's1-*.mp4')))
        return r, files

    @unittest.skipUnless(os.path.isdir(VENDOR), 'three.js chưa cài (verify.sh --install)')
    def test_h_resume_byte_identical(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as d:   # trong gốc repo: máy chủ trang của render_shots chỉ phục vụ tệp dưới ROOT
            seg = self._seg(d)
            r, a = self._render(seg, os.path.join(d, 'pipe'))
            self.assertEqual(r.returncode, 0, r.stderr[-2000:])
            r, _ = self._render(seg, os.path.join(d, 'res'), ['--resume'], {'CRUX_TEST_STOP_AFTER': '9'})
            self.assertEqual(r.returncode, 9, r.stderr[-1500:])   # "bị ngắt" ở khung 9/18
            fr = glob.glob(os.path.join(d, 'res', '*.frames', '*.jpg'))
            self.assertEqual(len(fr), 9)
            r, b = self._render(seg, os.path.join(d, 'res'), ['--resume'])
            self.assertEqual(r.returncode, 0, r.stderr[-2000:])
            self.assertIn('giữ 8/18', r.stdout)   # khung cuối (có thể ghi dở) dựng lại
            ha, hb = (hashlib.sha256(open(x[0], 'rb').read()).hexdigest() for x in (a, b))
            self.assertEqual(ha, hb)
            self.assertEqual(open(a[0].replace('.mp4', '.log.json')).read(), open(b[0].replace('.mp4', '.log.json')).read())
            self.assertEqual(glob.glob(os.path.join(d, 'res', '*.frames')), [])

    def test_i_atomic_promote(self):
        import build as BUILD
        with tempfile.TemporaryDirectory() as d:
            B = BUILD.Build.__new__(BUILD.Build)
            B.atomic = True
            B.work_final, B.out_final, B.epout_final = (os.path.join(d, x) for x in ('work', 'outf', 'out'))
            B.stage = os.path.join(B.work_final, '.new-1')
            B.work, B.out, B.epout = (os.path.join(B.stage, x) for x in ('work', 'out-factory', 'ep-out'))
            for x in (B.work_final, B.out_final, B.epout_final, B.work, B.out, B.epout, os.path.join(B.work_final, 'stems')):
                os.makedirs(x, exist_ok=True)
            open(os.path.join(B.work_final, 'video.mp4'), 'w').write('old')
            open(os.path.join(B.work_final, 'stems', 'old.flac'), 'w').write('old')
            self.assertEqual(B.rel(os.path.join(B.work, 'video.mp4')), os.path.relpath(os.path.join(B.work_final, 'video.mp4'), ROOT))
            self.assertEqual(B.cdir('cache'), os.path.join(B.work_final, 'cache'))
            # lượt trượt: không promote → bản cũ còn nguyên
            open(os.path.join(B.work, 'video.mp4'), 'w').write('new')
            self.assertEqual(open(os.path.join(B.work_final, 'video.mp4')).read(), 'old')
            os.makedirs(os.path.join(B.work, 'stems'))
            open(os.path.join(B.work, 'stems', 'voice.flac'), 'w').write('new')
            open(os.path.join(B.epout, 'camera.json'), 'w').write('{}')
            B.promote()
            self.assertEqual(open(os.path.join(B.work_final, 'video.mp4')).read(), 'new')
            self.assertEqual(sorted(os.listdir(os.path.join(B.work_final, 'stems'))), ['voice.flac'])
            self.assertTrue(os.path.exists(os.path.join(B.epout_final, 'camera.json')))
            self.assertFalse(os.path.exists(B.stage))

    @unittest.skipUnless(os.path.isdir(VENDOR), 'three.js chưa cài')
    def test_j_spp_param_off_by_default(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as d:
            seg = self._seg(d)
            r, a = self._render(seg, os.path.join(d, 'a'))
            r2, b = self._render(seg, os.path.join(d, 'b'), ['--spp', '0'])
            self.assertEqual(r.returncode, 0); self.assertEqual(r2.returncode, 0)
            self.assertNotEqual(os.path.basename(a[0]), os.path.basename(b[0]))   # spp vào khoá cache
            ka = json.load(open(os.path.join(d, 'a', 'out.mp4.render.json')))['codeKey']
            r3, c = self._render(seg, os.path.join(d, 'c'))
            self.assertEqual(json.load(open(os.path.join(d, 'c', 'out.mp4.render.json')))['codeKey'], ka)
            self.assertEqual(open(a[0], 'rb').read(), open(c[0], 'rb').read())


if __name__ == '__main__':
    unittest.main()
