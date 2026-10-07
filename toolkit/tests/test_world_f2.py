"""Test F-2 (BACKLOG; checks-appeal A19): mật độ sfx + nhãn đè nhau — `world/sfx_labels.py`, gắn vào verify_seg/build_seg; qc 2D soi gương.
Nhật ký/sự kiện giả, không render. Bằng chứng trên đoạn thật (chạy tay): python3 toolkit/factory/world/sfx_labels.py <spine.json> <log.json> [<audio>]

(a) hai hộp chữ giao nhau cùng khung → BLOCK (đều đọc được) / WARN (đang mờ dần); hộp kề nhau (chạm mép ≤ 1 px) không tính.
(b) đường (log.lines) cắt chữ → BLOCK; đường vẽ trước chữ có nền → không tính; đường cạnh chữ → không tính; nhật ký cũ không có lines → bỏ qua.
(c) sfx trên từ khoá: không stem → BLOCK; stem với sfx nhỏ (SNR ≥ 15 dB) → không cảnh báo; sfx to (SNR < 10 dB) → BLOCK.
(d) dày: > 6 sự kiện trong 10 s → WARN (cả số/phút), không BLOCK; 'data' và nền drone không tính; sfx đè từ thường đếm + giờ.
(e) qc 2D: hộp giao nhau → mục "nhãn giao nhau (F-2)" CẢNH BÁO, không làm trượt qc.
"""
import os, sys, tempfile, unittest
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'factory', 'world')); sys.path.insert(0, os.path.join(HERE, '..', 'factory'))
sys.dont_write_bytecode = True
import sfx_labels as F2  # noqa: E402


def tx(text, box, a=1.0, **k):
    return {'text': text, 'kind': 'name', 'px': 48, 'opacity': a, 'box': box, **k}


WORDS = [{'w': 'You', 's': 0.2, 'e': 0.4, 'sid': 'S01.1'}, {'w': 'saved', 's': 0.5, 'e': 0.9, 'sid': 'S01.1'},
         {'w': 'ten', 's': 1.0, 'e': 1.3, 'sid': 'S01.1'}, {'w': 'percent.', 's': 1.4, 'e': 1.9, 'sid': 'S01.1'},
         {'w': 'Then', 's': 30.0, 'e': 30.3, 'sid': 'S01.2'}, {'w': 'twenty.', 's': 30.5, 'e': 31.0, 'sid': 'S01.2'}]
BEATS = [{'id': 'a', 'cues': {'ten': 1.0}}, {'id': 'b', 'cues': {'tw': 30.5}}]


def spine(events, total=60.0):
    return {'total': total, 'words': WORDS, 'beats': BEATS, 'events': events}


class Labels(unittest.TestCase):
    def test_a_overlap_and_adjacent(self):
        logs = [{'t': 1.0, 'texts': [tx('80%', [100, 100, 300, 150]), tx('on paper', [250, 120, 500, 170])]},
                {'t': 1.1, 'texts': [tx('80%', [100, 100, 300, 150], 0.5), tx('on paper', [250, 120, 500, 170])]},
                {'t': 1.2, 'texts': [tx('left', [100, 100, 300, 150]), tx('right', [300.5, 100, 500, 150]), tx('below', [100, 150, 300, 200])]}]
        r = F2.label_check(logs)
        self.assertEqual(r['overlaps']['count'], 2)
        self.assertEqual([o['level'] for o in r['overlaps']['examples']], ['BLOCK', 'WARN'])
        self.assertEqual(r['overlaps']['examples'][0]['overlap_px'], (50, 30))
        self.assertTrue(r['block'] and 'on paper' in r['block'][0])
        self.assertEqual(F2.label_check(logs[2:])['overlaps']['count'], 0)   # kề nhau / chạm mép: không tính
        self.assertEqual(F2.check({'events': []}, logs)['level'], 'BLOCK')

    def test_b_line_crossing(self):
        box = [400, 300, 700, 350]
        cross = {'n': 5, 'a': 1, 'w': 3, 'seg': [[550, 100, 550, 600]]}   # dọc xuyên qua chữ
        beside = {'n': 6, 'a': 1, 'w': 3, 'seg': [[720, 100, 720, 600], [400, 360, 700, 380]]}   # cạnh phải / dưới chữ
        r = F2.label_check([{'t': 2.0, 'texts': [tx('slowest case', box, n=1)], 'lines': [cross, beside]}])
        self.assertEqual(r['line_crossings']['count'], 1)
        self.assertEqual(r['line_crossings']['examples'][0]['level'], 'BLOCK')
        under = dict(cross, n=0)   # vẽ trước chữ có nền: nền che đường
        self.assertEqual(F2.label_check([{'t': 2.0, 'texts': [tx('x', box, n=1, plate=1)], 'lines': [under]}])['line_crossings']['count'], 0)
        self.assertEqual(F2.label_check([{'t': 2.0, 'texts': [tx('x', box, n=1)], 'lines': [under]}])['line_crossings']['count'], 1)
        diag = {'n': 9, 'a': 0.4, 'w': 2, 'seg': [[300, 250, 800, 400]]}   # chéo, đang mờ dần → WARN
        r = F2.label_check([{'t': 3.0, 'texts': [tx('y', box)], 'lines': [diag]}])
        self.assertEqual((r['line_crossings']['count'], r['block'], len(r['warn'])), (1, [], 1))
        self.assertIn('skipped', F2.label_check([{'t': 0, 'texts': [tx('z', box)]}])['line_crossings'])
        self.assertFalse(F2.seg_hits_box([0, 0, 100, 0], box) or F2.seg_hits_box([401, 200, 401, 299], box))


class Sfx(unittest.TestCase):
    def test_c_keyword_mask(self):
        S = spine([{'t': 1.0, 'kind': 'land', 'mode': True}])
        r = F2.sfx_check(S)
        self.assertEqual([h['keyword'] for h in r['keyword_hits']], ['a.ten'])
        self.assertTrue(r['block'] and 'a.ten' in r['block'][0], r)    # không stem → không chứng minh được không che
        self.assertEqual(F2.check(S, [])['level'], 'BLOCK')
        # sfx vang (whoosh 0,5–1,1 s) chạm từ khoá dù bắt đầu trước nó
        self.assertEqual(len(F2.sfx_check(spine([{'t': 0.5, 'kind': 'whoosh_soft', 'dur': 0.6}]))['keyword_hits']), 1)
        from scipy.io import wavfile
        sr, n = 8000, 8000 * 3
        voice = np.zeros(n, np.float32); voice[int(1.0 * sr):int(1.3 * sr)] = 0.3 * np.sin(np.arange(int(0.3 * sr)) * 0.3)
        for gain, level in ((0.003, 'OK'), (0.2, 'BLOCK')):
            sfx = np.zeros(n, np.float32); sfx[int(1.0 * sr):int(1.3 * sr)] = gain * np.sin(np.arange(int(0.3 * sr)) * 0.5)
            with tempfile.TemporaryDirectory() as d:
                os.makedirs(os.path.join(d, 'stems'))
                wavfile.write(os.path.join(d, 'stems', 'voice.wav'), sr, np.stack([voice, voice], 1))
                wavfile.write(os.path.join(d, 'stems', 'sfx.wav'), sr, np.stack([sfx, sfx], 1))
                r = F2.sfx_check(S, d)
            self.assertTrue(r['stems'])
            self.assertEqual(r['keyword_hits'][0]['level'], level, r['keyword_hits'])
            self.assertEqual(bool(r['block']), level == 'BLOCK')

    def test_d_dense_window(self):
        ev = [{'t': 10.0 + 1.2 * i, 'kind': 'tick', 'v': 0.5} for i in range(8)]   # 8 sự kiện trong 8,4 s, ngoài lời
        ev += [{'t': 0.25, 'kind': 'whoosh_air', 'dur': 0.2}, {'t': 12.0, 'kind': 'data', 'v': 0.4}, {'t': 5.0, 'kind': 'drone_on', 'until': 20.0}]
        r = F2.sfx_check(spine(ev, total=20.0))
        self.assertEqual(r['events'], 9)                        # data + drone không tính
        self.assertEqual(r['max_window']['count'], 8)
        self.assertEqual(r['per_min'], 27.0)
        self.assertEqual(r['on_speech']['count'], 1)            # whoosh_air bắt đầu trong 'You' (từ thường), tắt trước từ khoá
        self.assertEqual(r['on_speech']['times'][0]['word'], 'You')
        self.assertEqual(r['block'], [])
        self.assertTrue(any('8 sự kiện trong 10 s' in w for w in r['warn']), r['warn'])
        self.assertEqual(F2.check(spine(ev, total=20.0), [])['level'], 'WARN')
        r = F2.sfx_check(spine(ev, total=10.0))
        self.assertTrue(any('/phút' in w for w in r['warn']), r['warn'])
        sparse = F2.sfx_check(spine([{'t': 10.0, 'kind': 'tick', 'v': 0.5}, {'t': 20.0, 'kind': 'chime'}]))
        self.assertEqual((sparse['warn'], sparse['block']), ([], []))


class Qc2D(unittest.TestCase):
    def test_e_qc_mirror(self):
        import qc
        L = {'t': 1.0, 'raised': [], 'recoloured': [], 'collisions': [], 'hist': False, 'illus': False, 'claims': [], 'tags': [],
             'texts': [{'s': 'A', 'px': 48, 'z': 1, 'contrast': 7, 'box': [200, 200, 400, 260]}, {'s': 'B', 'px': 48, 'z': 1, 'contrast': 7, 'box': [380, 240, 600, 300]}]}
        q = qc.Q(); qc.frame_rules(q, [L], 'h', 'master')
        it = next(i for i in q.items if 'F-2' in i['item'])
        self.assertEqual((it['result'], it['value']), ('CẢNH BÁO', 1))
        L['texts'][1]['box'] = [400, 240, 600, 300]
        q = qc.Q(); qc.frame_rules(q, [L], 'h', 'master')
        self.assertEqual(next(i for i in q.items if 'F-2' in i['item'])['result'], 'ĐẠT')


if __name__ == '__main__':
    unittest.main()
