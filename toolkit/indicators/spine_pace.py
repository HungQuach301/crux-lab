"""Thước nhịp trên spine (tổng kết Tập 5 §3.2; checks-appeal A23) — CHỈ BÁO, chưa là ngưỡng.
Đo trước render, trên `spine.json` của các đoạn thế giới (thời gian tập = thời gian đoạn + `episode_t0`):
  - still: quãng CÓ LỜI mà không có thay đổi hình nào — không cú máy (`moves` [t0, t1]), không cắt (`shots` t0), không vật thể
    đổi trạng thái (`visual_cues` → `beats[].cues`), không hoạt ảnh khoá (`*_kf`, `draw`, `ride`: mỗi khoá là một thay đổi).
    Quãng = từ từ đầu tiên tới từ cuối cùng giữa hai thay đổi liền nhau. Báo mọi quãng > 8 s (ngưỡng cine-lab Q15; đề xuất A23).
    Nhãn (`label_cues`) KHÔNG tính là thay đổi hình (đổi chữ không phải đổi hình — chống Goodhart cine-lab #44); báo riêng số quãng
    còn tĩnh nếu tính cả nhãn (`--labels`).
  - numbers_on_screen: số khác nhau trên nhãn (label_cues có chữ số). Số neo (≤ 3/tập, §3.2.4) chưa đo được: spine chưa có cờ
    `anchor` — thêm `anchor: true` ở beat từ Tập 6.
    python3 toolkit/indicators/spine_pace.py <spine.json …> [--min 8] [--labels] [--json ra.json]
Mỗi tệp có thể là `đường:sha` (đọc bằng git show) để đo phiên bản cũ, vd animatic C4 Tập 5 @ b70a0db.
"""
import json, re, subprocess, sys


def load(spec):
    if ':' in spec and not spec.startswith('/'):
        path, rev = spec.rsplit(':', 1)
        if re.fullmatch(r'[0-9a-f]{6,40}', rev):
            return json.loads(subprocess.check_output(['git', 'show', f'{rev}:{path}'])), spec
    return json.load(open(spec)), spec


def changes(d, labels=False):
    """[(t0, t1)] mọi thay đổi hình trong đoạn (giây đoạn)."""
    ch = [(m['t0'], m['t1']) for m in d.get('moves', [])]
    ch += [(s['t0'], s['t0']) for s in d.get('shots', [])[1:]]
    beats = {b['id']: b for b in d.get('beats', [])}
    keys = list(d.get('visual_cues', [])) + (list(d.get('label_cues', {})) if labels else [])
    for vc in keys:
        b, _, k = vc.partition('.')
        t = beats.get(b, {}).get('cues', {}).get(k)
        if t is not None:
            ch.append((t, t))
    for k, v in d.items():
        if (k.endswith('_kf') or k in ('draw', 'ride')) and isinstance(v, list):
            for kf in v:
                if isinstance(kf, list) and kf:
                    ch.append((kf[0], kf[0]))
    return sorted(ch)


def still(d, labels=False, min_s=8.0):
    off = d.get('episode_t0', 0.0) or 0.0
    words = [(w['s'], w['e']) for w in d.get('words', []) if not w['w'].startswith('[')]
    ch = changes(d, labels)
    # khoảng trống giữa các thay đổi (gộp khoảng chồng)
    edges, cur = [], 0.0
    for a, b in ch:
        if a > cur:
            edges.append((cur, a))
        cur = max(cur, b)
    edges.append((cur, d.get('total', cur)))
    out = []
    for a, b in edges:
        ws = [w for w in words if w[0] >= a and w[1] <= b]
        if not ws:
            continue
        s, e = ws[0][0], ws[-1][1]
        if e - s > min_s:
            out.append({'t0': round(s + off, 2), 't1': round(e + off, 2), 'dur': round(e - s, 2)})
    return out


def numbers(d):
    return sorted({n for txt in d.get('label_cues', {}).values() for n in re.findall(r'\d[\d,.]*', txt)})


def fmt(t):
    return f'{int(t // 60)}:{t % 60:04.1f}'


def run(specs, min_s=8.0, labels=False):
    res = {'segments': [], 'still': [], 'still_with_labels': [], 'numbers_on_screen': set()}
    for sp in specs:
        d, name = load(sp)
        st = still(d, False, min_s)
        res['segments'].append({'spine': name, 'segment': d.get('segment', ''), 'episode_t0': d.get('episode_t0', 0.0),
                                'total': d.get('total'), 'still': st})
        res['still'] += st
        if labels:
            res['still_with_labels'] += still(d, True, min_s)
        res['numbers_on_screen'] |= set(numbers(d))
    res['numbers_on_screen'] = sorted(res['numbers_on_screen'])
    return res


if __name__ == '__main__':
    a = sys.argv[1:]
    min_s = float(a[a.index('--min') + 1]) if '--min' in a else 8.0
    labels = '--labels' in a
    out = a[a.index('--json') + 1] if '--json' in a else None
    specs = [x for i, x in enumerate(a) if not x.startswith('--') and (i == 0 or a[i - 1] not in ('--min', '--json'))]
    r = run(specs, min_s, labels)
    for s in r['still']:
        print(f"tĩnh có lời {fmt(s['t0'])}–{fmt(s['t1'])} = {s['dur']:.1f} s")
    print(f"quãng tĩnh > {min_s:g} s: {len(r['still'])} (dài nhất {max([s['dur'] for s in r['still']] or [0]):.1f} s)"
          + (f"; tính cả nhãn: {len(r['still_with_labels'])}" if labels else '')
          + f"; số khác nhau trên nhãn: {len(r['numbers_on_screen'])}")
    if out:
        json.dump(r, open(out, 'w'), indent=1, ensure_ascii=False)
