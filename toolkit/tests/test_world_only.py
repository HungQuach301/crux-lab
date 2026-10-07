"""Test tập CHỈ có đoạn thế giới (Tập 5 C4: mọi cảnh trong `world:`, không shot 2D) — build.py trước đây dừng ở render (concat 0 đoạn).
(a) frame_size: 1080 → 1920×1080, 720 → 1280×720 (như cũ), 540 → 960×540; dọc cùng tỉ lệ.
(b) blank_picture: đúng round(total·fps) khung, đúng kích thước, 30 fps — splice.py nhận làm master (khung đoạn thay đúng chỗ).
(c) Build.do_render không shot 2D: có world → master đen + nhật ký khung rỗng; không có world → dừng.
"""
import json, os, subprocess, sys, tempfile, types, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'factory', 'world')); sys.path.insert(0, os.path.join(HERE, '..', 'factory'))
sys.dont_write_bytecode = True
import build as B  # noqa: E402
import splice as SP  # noqa: E402


class WorldOnly(unittest.TestCase):
    def test_a_size(self):
        self.assertEqual(B.frame_size('h', 1080), [1920, 1080])
        self.assertEqual(B.frame_size('h', 720), [1280, 720])
        self.assertEqual(B.frame_size('h', 540), [960, 540])
        self.assertEqual(B.frame_size('v', 540), [540, 960])

    def test_b_blank_spliceable(self):
        with tempfile.TemporaryDirectory() as d:
            m = os.path.join(d, 'm.mp4')
            n = B.blank_picture(m, [160, 96], 30, 2.0)
            P = SP.probe_video(m)
            self.assertEqual((n, P['frames'], P['w'], P['h'], round(P['fps'])), (60, 60, 160, 96, 30))
            seg = os.path.join(d, 's.mp4')
            subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'lavfi', '-i', 'color=c=red:s=160x96:r=30', '-frames:v', '30', '-pix_fmt', 'yuv420p', seg], check=True)
            r = SP.splice_video(m, [{'id': 'w', 'mp4': seg, 'f0': 15, 'f1': 45}], os.path.join(d, 'o.mp4'), 30, {'crf': 10, 'preset': 'ultrafast'})
            self.assertEqual(r['frames'], 60)

    def test_c_do_render(self):
        with tempfile.TemporaryDirectory() as d:
            fake = types.SimpleNamespace(tl={'shots': []}, S={'world': [{'id': 'w'}], 'res': 540}, work=d, fps=30, total=1.5)
            r = B.Build.do_render(fake)
            self.assertTrue(r['blank']); self.assertEqual(r['frames'], 45)
            P = SP.probe_video(fake.picture)
            self.assertEqual((P['frames'], P['w'], P['h']), (45, 960, 540))
            self.assertEqual(json.load(open(os.path.join(d, 'frame-log.json'))), [])
            fake2 = types.SimpleNamespace(tl={'shots': []}, S={}, work=d, fps=30, total=1.0)
            with self.assertRaises(SystemExit):
                B.Build.do_render(fake2)


if __name__ == '__main__':
    unittest.main()
