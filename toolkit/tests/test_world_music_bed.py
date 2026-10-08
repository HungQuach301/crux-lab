"""Test F-3: móc `music_plan.bed` của world/audio.py — đoạn thế giới lấy đúng lát nhạc nền của tập (bản đồ căng cả tập) thay vì tự sinh.
(a) lát đúng mẫu [offset, offset + T] (ở giữa, ngoài phần vào/ra), stereo, đúng độ dài;
(b) thiếu đuôi → đệm 0; vào/ra cos `fade` (mẫu đầu = 0);
(c) không có `bed` → music_code vẫn sinh nhạc như cũ (không đổi hành vi); file thiếu / offset âm → dừng.
"""
import os, sys, tempfile, unittest
import numpy as np
import soundfile as sf
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'factory', 'world'))
sys.dont_write_bytecode = True
import audio as WA  # noqa: E402

SR = WA.SR


class MusicBed(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = tempfile.TemporaryDirectory()
        n = 6 * SR
        t = np.arange(n) / SR
        cls.x = np.stack([0.3 * np.sin(2 * np.pi * 220 * t), 0.2 * np.sin(2 * np.pi * 330 * t)], 1)
        cls.wav = os.path.join(cls.d.name, 'bed.wav')
        sf.write(cls.wav, cls.x, SR, subtype='FLOAT')

    @classmethod
    def tearDownClass(cls):
        cls.d.cleanup()

    def test_a_slice(self):
        y, info = WA.music_code({'total': 2.0, 'music_plan': {'bed': {'wav': self.wav, 'offset': 1.5, 'fade': 0.05}}})
        self.assertEqual(y.shape, (2 * SR, 2))
        a, b = int(0.1 * SR), int(1.9 * SR)
        np.testing.assert_allclose(y[a:b], self.x[int(1.5 * SR) + a:int(1.5 * SR) + b], atol=1e-6)
        self.assertEqual(info['offset'], 1.5)
        self.assertEqual(info['stop'], 2.0)

    def test_b_pad_and_fade(self):
        y, _ = WA.music_code({'total': 2.0, 'music_plan': {'bed': {'wav': self.wav, 'offset': 5.0, 'fade': 0.05}}})
        self.assertEqual(len(y), 2 * SR)
        self.assertEqual(float(np.abs(y[int(1.1 * SR):]).max()), 0.0)          # bed hết ở 6 s → phần sau đệm 0
        self.assertEqual(float(np.abs(y[0]).max()), 0.0)                       # vào cos từ 0
        self.assertGreater(float(np.abs(y[int(0.2 * SR):int(0.5 * SR)]).max()), 0.1)

    def test_c_errors_and_default(self):
        with self.assertRaises(SystemExit):
            WA.bed_slice(1.0, {'wav': os.path.join(self.d.name, 'missing.wav'), 'offset': 0})
        with self.assertRaises(SystemExit):
            WA.bed_slice(1.0, {'wav': self.wav, 'offset': -1})
        spine = {'total': 3.0, 'tension': [[0, 0.5], [3, 0.5]], 'beats': [],
                 'music_plan': {'stop': 2.0, 'release': 2.5, 'accents': [0.5]}}
        y, info = WA.music_code(spine)                                         # không có bed → sinh như cũ
        self.assertEqual(y.shape, (3 * SR, 2))
        self.assertNotIn('bed', info)
        self.assertGreater(float(np.abs(y[:int(1.5 * SR)]).max()), 0)


if __name__ == '__main__':
    unittest.main()
