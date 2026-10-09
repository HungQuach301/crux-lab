"""Test cho ba script playbook v2: dải kiểm mù, đóng gói/chấm kiểm mù, giao hàng.

Chạy: python3 -m unittest discover -s toolkit/tests -v   (cần ffmpeg, ffprobe, git; không cần mạng)
"""
import json, os, subprocess, sys, tempfile, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [os.path.join(HERE, '..', 'blind'), os.path.join(HERE, '..', 'deliver')]
import strips, packets, deliver  # noqa: E402


def make_video(path, secs=4, size='1280x720', rate=30, audio=True):
    cmd = ['ffmpeg', '-v', 'error', '-y', '-f', 'lavfi', '-i', f'testsrc2=size={size}:rate={rate}:duration={secs}']
    if audio:
        cmd += ['-f', 'lavfi', '-i', f'sine=frequency=440:duration={secs}', '-c:a', 'aac', '-b:a', '128k']
    cmd += ['-c:v', 'libx264', '-preset', 'ultrafast', '-pix_fmt', 'yuv420p', path]
    subprocess.run(cmd, check=True)


def dims(path):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'stream=width,height,codec_type,codec_name,bit_rate',
                        '-of', 'json', path], capture_output=True, text=True, check=True)
    return json.loads(r.stdout)['streams']


class Strips(unittest.TestCase):
    def test_times_are_slice_centres(self):
        self.assertEqual(strips.frame_times(0, 6), [0.5, 1.5, 2.5, 3.5, 4.5, 5.5])
        self.assertRaises(ValueError, strips.frame_times, 3, 3)

    def test_strip_layout(self):
        with tempfile.TemporaryDirectory() as d:
            v = os.path.join(d, 'v.mp4'); make_video(v, audio=False)
            spans = os.path.join(d, 'spans.json'); json.dump({'KEY-1': [0.2, 3.8]}, open(spans, 'w'))
            strips.main([v, spans, os.path.join(d, 'out')])
            s = dims(os.path.join(d, 'out', 'KEY-1.png'))[0]
            self.assertEqual((s['width'], s['height']), (3 * 624 + 4 * 12, 2 * (351 + 50) + 3 * 12))
            rec = json.load(open(os.path.join(d, 'out', 'strips.json')))
            self.assertEqual(len(rec['strips']['KEY-1']['times']), 6)


class Packets(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()
        for n in ('KEY-1', 'KEY-2', 'KEY-3', 'S05'):
            open(os.path.join(self.d, n + '.png'), 'wb').write(n.encode())
        self.man = os.path.join(self.d, 'manifest.json')
        json.dump({'question': 'What idea is this section showing?', 'candidate_set': 'ep003', 'samples': [
            {'id': 'KEY-1', 'set': 'ep003', 'kind': 'image', 'file': 'KEY-1.png'},
            {'id': 'KEY-2', 'set': 'ep003', 'kind': 'image', 'file': 'KEY-2.png'},
            {'id': 'KEY-3', 'set': 'ep003', 'kind': 'illustration', 'file': 'KEY-3.png'},
            {'id': 'S05', 'set': 'ep001', 'kind': 'image', 'file': 'S05.png'}]}, open(self.man, 'w'))
        self.rub = os.path.join(self.d, 'rubric.json')
        json.dump({'rules': 'r', 'items': {k: {'meaning': 'm ' + k, 'description_only': 'd ' + k}
                                           for k in ('KEY-1', 'KEY-2', 'KEY-3', 'ctrl:S05')}}, open(self.rub, 'w'))
        self.key = os.path.join(self.d, 'review', 'key.json')
        self.out = os.path.join(self.d, 'blind')

    def test_deal_isolation_and_key(self):
        hs = packets.deal(self.man, self.out, self.key, [1, 2])
        self.assertEqual(len(hs), 8)
        key = json.load(open(self.key))
        for h in hs:
            files = os.listdir(os.path.join(self.out, h))
            self.assertEqual(files, [h + '.png'])  # một file, tên hex, không gì khác
            self.assertRegex(h, r'^[0-9a-f]{8}$')
        self.assertFalse(os.path.commonpath([self.key, self.out]) == self.out)  # khoá nằm ngoài thư mục người đọc
        self.assertEqual({(v['id'], v['slot']) for v in key['items'].values()},
                         {(i, s) for i in ('KEY-1', 'KEY-2', 'KEY-3', 'S05') for s in (1, 2)})
        with self.assertRaises(SystemExit):  # không chia hai lần cùng người đọc
            packets.deal(self.man, self.out, self.key, [1])

    def _score(self, plan):
        """plan: {(set,id,slot): (score, advice)} → chạy packet + tally."""
        key = json.load(open(self.key))
        ans = {h: f'answer {v["id"]} {v["slot"]}' for h, v in key['items'].items()}
        a = os.path.join(self.d, 'answers.json'); json.dump(ans, open(a, 'w'))
        pk, rk = os.path.join(self.d, 'packet.json'), os.path.join(self.d, 'rubric-key.json')
        packets.packet(self.key, a, self.rub, pk, rk)
        P, R = json.load(open(pk)), json.load(open(rk))
        for lab, it in P['items'].items():  # gói người chấm không lộ tập, mẫu, bộ
            self.assertEqual(set(it), {'answer', 'meaning', 'description_only'})
        scores = {}
        for lab, h in R.items():
            v = key['items'][h]
            s, adv = plan[(v['set'], v['id'], v['slot'])]
            scores[lab] = {'score': s, 'advice': adv, 'why': ''}
        sp = os.path.join(self.d, 'scores.json'); json.dump(scores, open(sp, 'w'))
        return packets.tally(self.key, rk, sp, threshold=0.8), rk, sp

    def test_early_stop_advice_and_gate(self):
        packets.deal(self.man, self.out, self.key, [1, 2])
        plan = {('ep003', 'KEY-1', 1): (1, False), ('ep003', 'KEY-1', 2): (1, False),   # 2 đầu cùng đúng → PASS
                ('ep003', 'KEY-2', 1): (1, False), ('ep003', 'KEY-2', 2): (0.5, False),  # lệch → cần người 3
                ('ep003', 'KEY-3', 1): (1, True), ('ep003', 'KEY-3', 2): (1, False),     # câu khuyên → FAIL
                ('ep001', 'S05', 1): (0, False), ('ep001', 'S05', 2): (0, False)}
        res, rk, sp = self._score(plan)
        st = {r['id']: r['status'] for r in res['rows']}
        self.assertEqual(st, {'KEY-1': 'PASS', 'KEY-2': 'NEED_3RD', 'KEY-3': 'FAIL', 'S05': 'FAIL'})
        self.assertEqual(res['verdict'], 'PENDING')
        self.assertEqual(res['gate_beats'], 2)  # KEY-3 là "illustration", đối chứng không tính
        # người đọc thứ 3 chỉ cho KEY-2
        packets.deal(self.man, self.out, self.key, [3], only=['ep003/KEY-2'])
        plan[('ep003', 'KEY-2', 3)] = (1, False)
        res, _, _ = self._score(plan)
        self.assertEqual({r['id']: r['status'] for r in res['rows']}['KEY-2'], 'PASS')
        # 2/2 nhịp loại 1 đạt, nhưng KEY-3 (loại 2) có câu khuyên → cổng trượt
        self.assertEqual((res['gate_pass'], res['gate_beats'], res['verdict']), (2, 2, 'FAIL'))
        self.assertEqual(res['advice_beats'], ['KEY-3'])
        self.assertIn('câu khuyên ở KEY-3', packets.markdown(res))
        plan[('ep003', 'KEY-3', 1)] = (1, False)
        res, rk, sp = self._score(plan)
        self.assertEqual(res['verdict'], 'PASS')

    def test_advice_stated_vs_inferred(self):
        """K4.1 (A9 + A21): advice_stated chặn nhịp; advice_inferred chỉ đếm; bản chấm cũ `advice` đọc là stated."""
        packets.deal(self.man, self.out, self.key, [1, 2])
        key = json.load(open(self.key))
        ans = {h: f'answer {v["id"]} {v["slot"]}' for h, v in key['items'].items()}
        a = os.path.join(self.d, 'answers.json'); json.dump(ans, open(a, 'w'))
        pk, rk = os.path.join(self.d, 'packet.json'), os.path.join(self.d, 'rubric-key.json')
        packets.packet(self.key, a, self.rub, pk, rk)
        self.assertIn('advice_stated', json.load(open(pk))['return'])
        R = json.load(open(rk))
        sc = {}
        for lab, h in R.items():
            v = key['items'][h]
            if v['id'] == 'KEY-1':      # người đọc tự suy (video không nói) → không chặn
                sc[lab] = {'score': 1, 'advice_stated': False, 'advice_inferred': True, 'quote': "the video doesn't state this", 'why': ''}
            elif v['id'] == 'KEY-2':    # video nêu hành động → chặn
                sc[lab] = {'score': 1, 'advice_stated': v['slot'] == 1, 'advice_inferred': False, 'quote': 'the label says Stay put to save', 'why': ''}
            elif v['id'] == 'KEY-3':    # bản chấm cũ: advice = stated
                sc[lab] = {'score': 1, 'advice': v['slot'] == 1, 'why': ''}
            else:
                sc[lab] = {'score': 0, 'advice_stated': False, 'caution_only': True, 'why': ''}
        sp = os.path.join(self.d, 'scores.json'); json.dump(sc, open(sp, 'w'))
        # chủ dự án 08/10 (gói K4.1 câu 3): chạy thử — luôn tính cả hai rubric; cổng mặc định rubric cũ; lệch → giữ rubric cũ
        res = packets.tally(self.key, rk, sp, threshold=0.8)
        rows = {r['id']: r for r in res['rows']}
        self.assertEqual((res['advice_rubric'], rows['KEY-1']['status']), ('old', 'FAIL'))          # cũ: tự suy cũng chặn
        self.assertEqual(sorted(res['advice_beats_old']), ['KEY-1', 'KEY-2', 'KEY-3'])
        self.assertEqual(sorted(res['advice_beats_new']), ['KEY-2', 'KEY-3'])                       # mới: chỉ video nói
        self.assertTrue(res['rubric_disagree'])
        res2 = packets.tally(self.key, rk, sp, threshold=0.8, advice_rubric='new')
        self.assertEqual(res2['advice_rubric'], 'old')                                              # lệch → giữ rubric cũ
        new = packets._tally_one(json.load(open(self.key)), json.load(open(rk)), [json.load(open(sp))], 0.8, None, 'new')
        nrows = {r['id']: r for r in new['rows']}
        self.assertEqual((nrows['KEY-1']['status'], nrows['KEY-1']['advice'], nrows['KEY-1']['advice_inferred']), ('PASS', 0, 2))
        # hai người chấm: gộp thận trọng (một người bật cờ là tính)
        sp2 = os.path.join(self.d, 'scores2.json')
        json.dump({lab: dict(v, advice_stated=False, advice_inferred=False, quote='') if 'advice_stated' in v else v for lab, v in sc.items()}, open(sp2, 'w'))
        res3 = packets.tally(self.key, rk, [sp, sp2], threshold=0.8)
        self.assertEqual((res3['graders'], sorted(res3['advice_beats_new'])), (2, ['KEY-2', 'KEY-3']))
        self.assertIn('hai rubric lệch', packets.markdown(res) if res['verdict'] != 'PENDING' else 'hai rubric lệch')

    def test_classes_guard(self):
        packets.deal(self.man, self.out, self.key, [1, 2])
        plan = {(s, i, k): (1, False) for s, i in (('ep003', 'KEY-1'), ('ep003', 'KEY-2'), ('ep003', 'KEY-3'),
                                                    ('ep001', 'S05')) for k in (1, 2)}
        res, rk, sp = self._score(plan)
        cls = os.path.join(self.d, 'classes.json')
        json.dump({'KEY-1': 'image', 'KEY-2': 'image', 'KEY-3': 'illustration'}, open(cls, 'w'))
        ok = packets.tally(self.key, rk, sp, classesfile=cls)
        self.assertEqual(ok['classes']['image_share'], 0.667)
        json.dump({'KEY-1': 'image', 'KEY-2': 'illustration', 'KEY-3': 'illustration'}, open(cls, 'w'))
        with self.assertRaises(SystemExit):  # manifest lệch bảng đã báo
            packets.tally(self.key, rk, sp, classesfile=cls)
        json.dump({'KEY-1': 'image', 'KEY-2': 'image', 'KEY-3': 'illustration', 'KEY-4': 'illustration',
                   'KEY-5': 'illustration'}, open(cls, 'w'))
        with self.assertRaises(SystemExit):  # loại 1 = 40% < 60%
            packets.tally(self.key, rk, sp, classesfile=cls)

    def test_beat_status_table(self):
        B = packets.beat_status
        self.assertEqual(B([(1, False), (1, False)])[0], 'PASS')
        self.assertEqual(B([(0, False), (0.5, False)])[0], 'FAIL')
        self.assertEqual(B([(1, False), (0, False), (1, False)])[0], 'PASS')
        self.assertEqual(B([(1, False), (0, False), (0.5, False)])[0], 'FAIL')
        self.assertEqual(B([(1, False), (1, False), (1, True)])[0], 'FAIL')
        self.assertEqual(B([(1, True)])[0], 'FAIL')


class Deliver(unittest.TestCase):
    def test_bitrate_table(self):
        self.assertEqual(deliver.youtube_bitrate(1080, 30), 8)
        self.assertEqual(deliver.youtube_bitrate(1080, 29.97), 8)
        self.assertEqual(deliver.youtube_bitrate(1080, 60), 12)
        self.assertEqual(deliver.youtube_bitrate(720, 30), 5)
        self.assertEqual(deliver.youtube_bitrate(2160, 24), 35)

    def test_encode_split_join_and_branch(self):
        with tempfile.TemporaryDirectory() as d:
            v = os.path.join(d, 'video.mp4'); make_video(v, secs=3, size='1920x1080')
            repo, remote = os.path.join(d, 'repo'), os.path.join(d, 'remote.git')
            subprocess.run(['git', 'init', '-q', '--bare', remote], check=True)
            subprocess.run(['git', 'init', '-q', repo], check=True)
            g = lambda *a: subprocess.run(['git', '-C', repo, '-c', 'user.name=t', '-c', 'user.email=t@t', *a],
                                          check=True, capture_output=True, text=True)
            open(os.path.join(repo, 'a.txt'), 'w').write('x')
            g('add', 'a.txt'); g('commit', '-qm', 'init'); g('remote', 'add', 'origin', remote)
            head = g('rev-parse', '--abbrev-ref', 'HEAD').stdout.strip()
            out = os.path.join(d, 'deliv')
            env = dict(os.environ, GIT_AUTHOR_NAME='t', GIT_AUTHOR_EMAIL='t@t', GIT_COMMITTER_NAME='t',
                       GIT_COMMITTER_EMAIL='t@t')
            os.environ.update(env)
            deliver.main([v, '--out', out, '--name', 'ep999', '--preset', 'ultrafast', '--part-bytes', '200000',
                          '--branch', 'ep999-delivery', '--repo', repo, '--push'])
            rec = json.load(open(os.path.join(out, 'delivery.json')))
            self.assertEqual(rec['video_mbps'], 8)
            st = {s['codec_type']: s for s in dims(os.path.join(out, 'ep999-youtube.mp4'))}
            self.assertEqual(st['audio']['codec_name'], 'aac')
            self.assertGreater(len(rec['parts']), 1)
            # ghép lại như lệnh Mac/Linux trong JOIN.md và so SHA
            joined = os.path.join(d, 'joined.mp4')
            with open(joined, 'wb') as f:
                for p in rec['parts']:
                    f.write(open(os.path.join(out, p), 'rb').read())
            self.assertEqual(deliver.sha256(joined), rec['sha256'])
            self.assertTrue(all(os.path.getsize(os.path.join(out, p)) <= 200000 for p in rec['parts']))
            doc = open(os.path.join(out, 'JOIN.md')).read()
            self.assertIn('copy /b', doc); self.assertIn('shasum -a 256', doc)
            # nhánh mồ côi trên remote chỉ chứa phần + SHA256SUMS + JOIN.md; nhánh đang làm không đổi
            ls = subprocess.run(['git', '--git-dir', remote, 'ls-tree', '--name-only', 'ep999-delivery'],
                                capture_output=True, text=True, check=True).stdout.split()
            self.assertEqual(sorted(ls), sorted(rec['parts'] + ['SHA256SUMS', 'JOIN.md']))
            self.assertEqual(g('rev-parse', '--abbrev-ref', 'HEAD').stdout.strip(), head)
            self.assertEqual(g('status', '--porcelain').stdout.strip(), '')
            # nhánh đã có trên origin → dừng trước khi mã hoá
            g('branch', '-D', 'ep999-delivery')
            with self.assertRaises(SystemExit):
                deliver.branch_free(repo, 'ep999-delivery', remote=True)


if __name__ == '__main__':
    unittest.main()
