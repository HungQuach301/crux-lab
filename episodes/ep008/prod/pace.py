"""Tập 8 · M5 nhịp (vai Editor, gates/M5-intent.md §4 + C5/P7): đứng hình có lời trên nháp.
  python3 prod/pace.py <video> [stem_voice]     # → review-m5/pace.json + in bảng
Đo: ffmpeg freezedetect n=0.003 d=3 trên hình; "có lời" = giọng > −45 dBFS (silencedetect trên stem voice).
Ngưỡng: tổng giây đứng hình chồng lời ≤ 30 s/tập; quãng đứng hình chồng lời > 8 s = 0."""
import json, re, subprocess, sys
from pathlib import Path
EP = Path(__file__).resolve().parents[1]


def ff(args):
    return subprocess.run(['ffmpeg', '-hide_banner', '-nostats', *args, '-f', 'null', '-'], capture_output=True, text=True).stderr


def spans(log, a, b):
    s = [float(x) for x in re.findall(a + r':\s*([\d.]+)', log)]
    e = [float(x) for x in re.findall(b + r':\s*([\d.]+)', log)]
    return s, e


def main(video, voice):
    fl = ff(['-i', video, '-vf', 'freezedetect=n=0.003:d=3', '-an'])
    fs, fe = spans(fl, 'freeze_start', 'freeze_end')
    h, m, x = re.search(r'Duration: (\d+):(\d+):([\d.]+)', fl).groups(); dur = 3600 * int(h) + 60 * int(m) + float(x)
    fe += [dur] * (len(fs) - len(fe))
    sl = ff(['-i', voice, '-af', 'silencedetect=noise=-45dB:d=0.3'])
    ss, se = spans(sl, 'silence_start', 'silence_end')
    se += [dur] * (len(ss) - len(se))
    sil = list(zip(ss, se))

    def speech(a, b):  # giây có lời trong [a, b]
        q = b - a
        for x, y in sil:
            q -= max(0.0, min(b, y) - max(a, x))
        return max(0.0, q)
    tl = json.load(open(EP / 'out/factory/timeline.json'))
    def scene(t): return next((s['id'] for s in tl['scenes'] if s['start'] <= t < s['start'] + s['dur']), '?')
    rows = [dict(t0=round(a, 2), t1=round(b, 2), dur=round(b - a, 2), speech=round(speech(a, b), 2), scene=scene(a)) for a, b in zip(fs, fe)]
    tot = round(sum(r['speech'] for r in rows), 2)
    over8 = [r for r in rows if r['speech'] > 8]
    res = dict(video=video, freezes=rows, speech_frozen_total=tot, over8=over8,
               pass_total=tot <= 30, pass_over8=not over8)
    out = EP / 'review-m5'; out.mkdir(exist_ok=True)
    (out / 'pace.json').write_text(json.dumps(res, indent=1, ensure_ascii=False))
    for r in rows:
        print(f"{r['scene']} {r['t0']:7.2f}–{r['t1']:7.2f} đứng {r['dur']:5.2f}s có lời {r['speech']:5.2f}s")
    print(f'tổng đứng hình có lời {tot}s (≤30: {res["pass_total"]}); >8 s: {len(over8)}')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else str(EP / 'work/factory/stems/voice.flac'))
