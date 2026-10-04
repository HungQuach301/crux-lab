#!/usr/bin/env python3
"""Cắt dải kiểm mù: 6 khung theo thời gian của một đoạn video, ghép lưới 3×2 đánh số 1–6.

Thay cho cách làm tay ở Tập 1–2 (`episodes/ep002/animatic/src/render.js --strips`): cùng bố cục
(6 khung 624×351, khe 12 px, dải số 50 px dưới mỗi khung, nền #06080B), cùng cách chọn khung
(tâm của 6 lát bằng nhau trong [t0, t1]), nhưng đọc thẳng từ một file video bất kỳ.

Dùng:
  python3 toolkit/blind/strips.py VIDEO SPANS.json OUTDIR
SPANS.json: {"KEY-1": [t0, t1], "KEY-2": [t0, t1], ...} (giây, theo video).
Ra: OUTDIR/<tên>.png cho mỗi đoạn + OUTDIR/strips.json (thời điểm từng khung, SHA-256 video và từng PNG).
Mẫu kiểm mù cổng gốc (C3, C4) là video TẮT TIẾNG, GIỮ chữ/số — script không che gì.
"""
import argparse, hashlib, json, os, subprocess, sys

TW, TH, GAP, LAB = 624, 351, 12, 50
BG, FG = '0x06080B', '0xF2F4F7'
HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = [os.path.join(HERE, '..', 'render', 'fonts', 'inter-latin-700-normal.woff2'),
         '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf']


def frame_times(t0, t1, n=6):
    if not t1 > t0:
        raise ValueError(f'khoảng thời gian rỗng: [{t0}, {t1}]')
    return [round(t0 + (i + 0.5) * (t1 - t0) / n, 3) for i in range(n)]


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def _font():
    for f in FONTS:
        if os.path.exists(f):
            # ffmpeg drawtext cần freetype đọc được font; thử nhanh, hỏng thì sang font kế
            r = subprocess.run(['ffmpeg', '-v', 'error', '-f', 'lavfi', '-i', 'color=c=black:s=64x64:d=0.04',
                                '-vf', f"drawtext=fontfile='{f}':text=1:fontsize=20:fontcolor=white",
                                '-frames:v', '1', '-f', 'null', '-'], capture_output=True)
            if r.returncode == 0:
                return f
    return None


def make_strip(video, t0, t1, out_png, font=None):
    times = frame_times(t0, t1)
    cmd = ['ffmpeg', '-v', 'error', '-y']
    for t in times:
        cmd += ['-ss', f'{t:.3f}', '-i', video]
    chains, labels = [], []
    for i in range(6):
        c = (f'[{i}:v]scale={TW}:{TH}:flags=lanczos,setsar=1,'
             f'pad={TW + GAP}:{TH + LAB + GAP}:{GAP}:{GAP}:color={BG}')
        if font:
            c += (f",drawtext=fontfile='{font}':text={i + 1}:fontsize=34:fontcolor={FG}"
                  f':x={GAP}+({TW}-text_w)/2:y={GAP + TH}+({LAB}-text_h)/2')
        chains.append(c + f'[f{i}]')
        labels.append(f'[f{i}]')
    W, H = TW + GAP, TH + LAB + GAP
    layout = '|'.join(f'{(i % 3) * W}_{(i // 3) * H}' for i in range(6))
    fc = ';'.join(chains) + ';' + ''.join(labels) + f'xstack=inputs=6:layout={layout}:fill={BG},' \
         f'pad=iw+{GAP}:ih+{GAP}:0:0:color={BG}[out]'
    cmd += ['-filter_complex', fc, '-map', '[out]', '-frames:v', '1', out_png]
    subprocess.run(cmd, check=True)
    return times


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('video')
    ap.add_argument('spans', help='JSON {tên: [t0, t1]}')
    ap.add_argument('outdir')
    a = ap.parse_args(argv)
    spans = json.load(open(a.spans, encoding='utf-8'))
    os.makedirs(a.outdir, exist_ok=True)
    font = _font()
    if not font:
        print('cảnh báo: không có font cho drawtext, dải không đánh số', file=sys.stderr)
    rec = {'video': os.path.basename(a.video), 'video_sha256': sha256(a.video), 'font': font and os.path.basename(font),
           'layout': f'3x2, {TW}x{TH}, gap {GAP}, label {LAB}', 'strips': {}}
    for name, (t0, t1) in spans.items():
        out = os.path.join(a.outdir, f'{name}.png')
        times = make_strip(a.video, float(t0), float(t1), out, font)
        rec['strips'][name] = {'span': [t0, t1], 'times': times, 'sha256': sha256(out)}
        print(name, times)
    json.dump(rec, open(os.path.join(a.outdir, 'strips.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)


if __name__ == '__main__':
    main()
