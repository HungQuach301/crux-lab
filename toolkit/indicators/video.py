"""Đọc khung video bằng ffmpeg cho các thước chỉ báo (toolkit/indicators). Không ghi gì vào repo."""
import json, subprocess
import numpy as np


def probe(path):
    out = subprocess.check_output(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'format=duration',
                                   '-of', 'json', path])
    return float(json.loads(out)['format']['duration'])


def frames(path, fps=2.0, w=96, h=54, gray=False):
    """→ (t[], mảng [n, h, w] hoặc [n, h, w, 3] uint8). Khung lấy đều theo fps từ 0."""
    pix = 'gray' if gray else 'rgb24'
    raw = subprocess.check_output(['ffmpeg', '-v', 'error', '-i', path, '-vf', f'fps={fps},scale={w}:{h}:flags=area',
                                   '-f', 'rawvideo', '-pix_fmt', pix, '-'])
    c = 1 if gray else 3
    a = np.frombuffer(raw, np.uint8)
    n = a.size // (w * h * c)
    a = a[:n * w * h * c].reshape((n, h, w) if gray else (n, h, w, 3))
    return np.arange(n) / fps, a


def lab(rgb):
    """sRGB uint8 [..., 3] → CIELAB (D65) float."""
    c = rgb.astype(np.float64) / 255.0
    c = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    M = np.array([[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722], [0.0193, 0.1192, 0.9505]])
    xyz = c @ M.T / np.array([0.95047, 1.0, 1.08883])
    f = np.where(xyz > (6 / 29) ** 3, np.cbrt(xyz), xyz / (3 * (6 / 29) ** 2) + 4 / 29)
    L = 116 * f[..., 1] - 16
    return np.stack([L, 500 * (f[..., 0] - f[..., 1]), 200 * (f[..., 1] - f[..., 2])], -1)


def grab(path, t, out, w=640):
    subprocess.check_call(['ffmpeg', '-v', 'error', '-y', '-ss', f'{t:.3f}', '-i', path, '-frames:v', '1',
                           '-vf', f'scale={w}:-2', '-q:v', '4', out])
