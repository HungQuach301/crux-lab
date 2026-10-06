"""Mốc V · mốc lời THẬT cho spine: alignment ký tự của TTS hay gộp khoảng nghỉ vào đầu từ ("Has" 1,52–2,12 nhưng tiếng bắt đầu 2,08).
Tinh chỉnh: đầu từ = khung 10 ms đầu tiên trong [s, e] có năng lượng ≥ ngưỡng (−30 dB so với RMS lời của take).
Không đổi thứ tự từ, không dời quá e − 0,02. Dùng cho mọi spine (cue = lúc người xem NGHE từ, không phải lúc TTS đặt mốc).
  refine(words, mp3, offset) → words (s đã chỉnh, thêm 's_tts')"""
import subprocess
import numpy as np

SR = 16000


def pcm(path):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32)


def refine(words, path, offset=0.0, db=-30.0):
    x = pcm(path); hop = SR // 100
    n = len(x) // hop; e = np.sqrt((x[:n * hop].reshape(n, hop) ** 2).mean(1) + 1e-12)
    ref = np.sqrt(np.mean(e[e > np.percentile(e, 60)] ** 2)); thr = ref * 10 ** (db / 20)
    out = []
    for w in words:
        s, en = w['s'] - offset, w['e'] - offset
        i0, i1 = int(s * 100), max(int(s * 100) + 1, int((en + 0.15) * 100))   # tìm tới quá cuối từ một chút (TTS có khi đặt cả từ vào khoảng lặng)
        seg = e[i0:min(i1, n)]
        hit = np.nonzero(seg >= thr)[0]
        s2 = min(s + hit[0] / 100, en - 0.02) if len(hit) else s
        out.append(dict(w, s=round(s2 + offset, 3), s_tts=w['s']))
    return out
