"""Hồi quy: lớp phủ 2D của core.Stage không được giữ ẢNH CŨ khi một khung không vẽ chữ nào (Tập 5 C4 vòng 3).
Lỗi: Overlay.begin() chỉ xoá canvas lớp phủ; khi khung sau không có lệnh vẽ nào lên lớp phủ (không chữ, không lớp bắt buộc — vd. giữa cú bay),
Chromium (canvas 2D tăng tốc, compose() chép sang canvas ra) trả lại ẢNH CŨ của lớp phủ → chữ của cảnh trước "treo" qua cả cảnh sau.
Master Tập 5 vòng 2: mảnh "… 9 yr 4 mo)" ở 5:05–5:19 (đạo diễn A); vòng 3 dựng lần 1: nhãn S13 hiện trên ba người mua (cảnh s9 của đoạn C).
Sửa: begin() vẽ một điểm gần như trong suốt (1/255, 1 px) ngay sau khi xoá → lớp phủ luôn có lệnh vẽ mới.
(a) nhanh: begin() trong core.js có lệnh vẽ sau clearRect.
(b) chậm (CRUX_SLOW=1, cần node + playwright + three + episodes/ep005): dựng LẠI ĐÚNG ca lỗi bằng render_shots.js một worker — cảnh s7 (S13, nhiều chữ)
    rồi s9 (cú bay, không chữ) của đoạn C Tập 5 → khung 0,4 s của s9 phải tối (không chữ cũ). Đo khi viết: core cũ max 255 (chữ cũ, lặp lại 2/2),
    core mới không có chữ. Ca tổng hợp (một cảnh 300 khung nhiều chữ rồi một cảnh trống) KHÔNG tái hiện được lỗi, nên (b) dùng chính đoạn thật."""
import os, re, shutil, subprocess, tempfile, unittest
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
WORLD = os.path.join(ROOT, 'toolkit', 'factory', 'world')
SEG = os.path.join(ROOT, 'episodes', 'ep005', 'world', 'c4', 'c-s10-s14')


class OverlayClear(unittest.TestCase):
    def test_a_begin_draws_after_clear(self):
        src = open(os.path.join(WORLD, 'core.js'), encoding='utf-8').read()
        body = src[src.index('begin(t, cw, cam) {'):]
        body = body[:body.index('return log;')]
        after = body[body.index('ctx.clearRect('):]
        m = re.search(r"ctx\.fillStyle = 'rgba\(0,\s*0,\s*0,\s*([\d.]+)\)'; ctx\.fillRect\(0, 0, 1, 1\)", after)
        self.assertTrue(m, 'begin(): sau clearRect phải có một lệnh vẽ (chống ảnh lớp phủ cũ)')
        self.assertLessEqual(float(m[1]), 0.005, 'điểm vẽ phải gần như trong suốt (≤ 0,5 %)')

    @unittest.skipUnless(os.environ.get('CRUX_SLOW') == '1', 'chậm (~2 phút): đặt CRUX_SLOW=1')
    def test_b_real_case_no_ghost(self):
        npm = subprocess.run(['npm', 'root', '-g'], capture_output=True, text=True).stdout.strip()
        if not (shutil.which('node') and os.path.isdir(os.path.join(npm, 'playwright')) and os.path.isfile(os.path.join(SEG, 'spine.json'))):
            self.skipTest('node / playwright / đoạn C Tập 5 không có')
        d = tempfile.mkdtemp()
        try:
            r = subprocess.run(['node', os.path.join(WORLD, 'render_shots.js'), os.path.relpath(SEG, ROOT), '540', os.path.join(d, 'x.mp4'),
                                '--workers', '1', '--only', 's7,s9', '--cache', d], cwd=ROOT, env={**os.environ, 'NODE_PATH': npm},
                               capture_output=True, text=True, timeout=900)
            self.assertEqual(r.returncode, 0, r.stderr[-2000:])
            s9 = next(os.path.join(d, f) for f in os.listdir(d) if f.startswith('s9-') and f.endswith('.mp4'))
            import numpy as np
            raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', '0.4', '-i', s9, '-frames:v', '1', '-vf', 'format=gray', '-f', 'rawvideo', '-'],
                                 capture_output=True).stdout
            a = np.frombuffer(raw, np.uint8).reshape(540, 960)
            self.assertLess(int(a.max()), 120, 'khung không chữ của s9 còn chữ cũ của s7 (lớp phủ cũ)')
        finally:
            shutil.rmtree(d, ignore_errors=True)


if __name__ == '__main__':
    unittest.main()
