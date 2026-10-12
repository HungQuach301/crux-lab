"""F-14 · đo nhịp hình trên một master của Tập 6 (bản giao = đối chứng, hoặc bản dựng lại) — cùng một cách đo cho cả hai.
  python3 toolkit/factory/f14/measure.py <video.mp4> <timeline.json> <thư mục spine> <ra.json> [--freeze <freeze.txt có sẵn>]
Đo:
  freeze  freezedetect n=−60 dB d=3 (đúng qc.py `freezes`) ∩ lời (qc.speech_spans trên timeline.words) — tổng giây + từng quãng (gắn đoạn/nhịp)
  labels  nhãn có số của spine (label_cues): mốc hiện thật trên nhật ký trang của đoạn (<seg>.log.json, nếu có) − mốc từ khoá (cue)
Không thay luật checks/: R07 lấy từ checks run (run.py --only R07) — số chính; ở đây chỉ gắn nhãn quãng đứng yên cho REPORT.
"""
import json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from qc import speech_spans  # noqa: E402


def freezes(video, cached=None):
    if cached and os.path.exists(cached):
        txt = open(cached).read()
    else:
        r = subprocess.run(['ffmpeg', '-hide_banner', '-i', video, '-vf', 'freezedetect=n=-60dB:d=3', '-map', '0:v', '-f', 'null', '-'],
                           capture_output=True, text=True)
        txt = r.stderr
        if cached:
            open(cached, 'w').write('\n'.join(re.findall(r'freeze_(?:start|end): [\d.]+', txt)))
    st = [float(x) for x in re.findall(r'freeze_start: ([\d.]+)', txt)]
    en = [float(x) for x in re.findall(r'freeze_end: ([\d.]+)', txt)]
    return [[a, en[i] if i < len(en) else 1e9] for i, a in enumerate(st)]


def where(spines, t):
    for sp in spines:
        a = sp.get('episode_t0', 0)
        if a <= t < a + sp['total']:
            b = [x for x in sp['beats'] if x['t0'] - 0.5 <= t - a]
            return sp['segment'].split('·')[1].split('=')[0].strip() if '·' in sp['segment'] else sp['segment'], (b[-1]['id'] if b else '—'), (b[-1]['sid'] if b else '—')
    return '—', '—', '—'


def main():
    video, tlp, sdir, out = sys.argv[1:5]
    cache = sys.argv[sys.argv.index('--freeze') + 1] if '--freeze' in sys.argv else None
    tl = json.load(open(tlp))
    sp = speech_spans(tl['words'])   # đúng qc.py (cả thẻ cảm xúc)
    fz = freezes(video, cache)
    spines = [json.load(open(os.path.join(sdir, d, 'spine.json'))) for d in sorted(os.listdir(sdir)) if os.path.exists(os.path.join(sdir, d, 'spine.json'))]
    hit = []
    for a, b in fz:
        ov = [[max(a, c), min(b, d)] for c, d in sp if min(b, d) - max(a, c) > 0]
        if ov:
            seg, beat, sid = where(spines, a + 0.01)
            hit.append({'t0': round(a, 2), 't1': round(min(b, tl['total']), 2), 'dur': round(min(b, tl['total']) - a, 2),
                        'speech_s': round(sum(y - x for x, y in ov), 2), 'segment': seg, 'beat': beat, 'sid': sid})
    res = {'video': video, 'freeze_spans': len(fz), 'freeze_speech_s': round(sum(h['speech_s'] for h in hit), 2), 'freeze_hits': hit}
    json.dump(res, open(out, 'w'), indent=1, ensure_ascii=False)
    print(f"freezedetect d=3 ∩ lời: {res['freeze_speech_s']} s ({len(hit)} quãng có lời / {len(fz)} quãng đứng yên)")
    for h in sorted(hit, key=lambda h: -h['speech_s'])[:12]:
        print(f"  {h['t0']:7.2f}–{h['t1']:7.2f}  lời {h['speech_s']:5.2f} s  {h['beat']} {h['sid']}")


if __name__ == '__main__':
    main()
