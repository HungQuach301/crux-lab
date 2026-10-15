"""Nhà máy · GHÉP ĐOẠN THẾ GIỚI vào master của tập (BACKLOG F-5; D-010).

Hình: mỗi đoạn `world:` thay đúng các khung của các cảnh nó chiếm (khung [f0, f1) theo fps của tập); cả master mã hoá lại MỘT lần
      (cùng thông số H.264 với render.js: high, preset, CBR/CRF, yuv420p, bt709, timescale 15360) → một luồng đồng nhất.
      Số khung của đoạn phải bằng đúng f1 − f0 và fps của đoạn = fps của tập, sai → dừng (SystemExit), không kéo giãn.
Tiếng: lời vẫn là track lời của tập (stem voice của đoạn KHÔNG cộng vào — chỉ dùng để đo mức); nhạc/âm dữ liệu/sfx/whoosh/room tone của đoạn
      (world/audio.py: stems/{music,data,sfx,whoosh,room}.wav; whoosh tuỳ chọn) cộng vào stem music/sonify/sfx/whoosh/room của tập tại t0 của đoạn, cùng tỉ lệ
      lời-đoạn → lời-tập (RMS lời trong khoảng). Nhạc nền của tập (nếu có) tắt trong khoảng đoạn (fade 0,5 s ngoài mép).
      mix-raw = tổng đúng các stem (48 kHz stereo, cùng gốc thời gian); loudnorm 2 lượt của build.py chạy sau trên toàn bản.
Báo cáo: out/factory/splice.json (đoạn, cảnh, t0/t1, khung, sha256 đầu vào/đầu ra).
J/L-cut qua biên đoạn (F-18, opt-in): spine.json của đoạn VÀO khai `cuts: {<cảnh đầu đoạn>: {cut: J|L|hard, offset: 0.3–1.0}}`. Tiếng KHÔNG dời
      (lời, nhạc, sfx của mỗi đoạn giữ đúng đồng hồ của nó → đồng bộ lời–hình trong cảnh nguyên vẹn); chỉ điểm cắt HÌNH dời khỏi biên tiếng T:
      J = hình cắt ở T + offset (tiếng đoạn sau vào trước; khung cuối đoạn trước giữ nguyên `offset` s, `offset` s đầu đoạn sau không lên hình),
      L = hình cắt ở T − offset (tiếng đoạn trước kéo sang; khung đầu đoạn sau giữ `offset` s, `offset` s cuối đoạn trước không lên hình).
      Từ khoá (beats[].cues) của đoạn rơi vào phần không lên hình → dừng (lệch lời–hình). Không khai = đồ thị lọc, master, stem trùng byte bản cũ.
      Bản ghi mỗi mối nối: merge_audio → splice.json audio.joins; `python3 splice.py --transitions <splice.json> <out/transitions.json>` ghi điểm cắt hình
      (t = mốc cắt hình, audio j/l) cho checks (R09, V10, R06).
"""
import hashlib
import json
import os
import subprocess

import numpy as np
import soundfile as sf

SR = 48000
LAYERS = {'music': 'music', 'data': 'sonify', 'sfx': 'sfx', 'whoosh': 'whoosh', 'room': 'room'}   # stem của đoạn → stem của tập (checks/CONTRACT.md)
OPTIONAL = {'whoosh'}   # đoạn dựng trước khi audio.py tách whoosh: không có stem này (tiếng máy quay nằm trong sfx); có ở ≥ 1 đoạn → stem whoosh của tập
BED_FADE = 0.5
JL_RANGE = (0.3, 1.0)   # s: độ lệch tiếng–hình hợp lệ của J/L (BAN-DO-LIEN-MACH: "tiếng cảnh sau vào trước 0,3–1,0 s")
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))


def sha_file(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def scene_span(tl, scenes, fps):
    """Các cảnh của đoạn phải liền nhau, đúng thứ tự trong timeline → (t0, t1, f0, f1)."""
    ids = [s['id'] for s in tl['scenes']]
    if not scenes or any(s not in ids for s in scenes):
        raise SystemExit(f'splice: cảnh {scenes} không có trong timeline')
    i = ids.index(scenes[0])
    if ids[i:i + len(scenes)] != list(scenes):
        raise SystemExit(f'splice: cảnh {scenes} không liền nhau / sai thứ tự trong tập ({ids})')
    sc = tl['scenes'][i:i + len(scenes)]
    t0, t1 = sc[0]['start'], sc[-1]['start'] + sc[-1]['dur']
    return round(t0, 4), round(t1, 4), round(t0 * fps), round(t1 * fps)


def probe_video(p):
    r = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height,r_frame_rate,nb_frames',
                        '-of', 'json', p], capture_output=True, text=True, check=True)
    s = json.loads(r.stdout)['streams'][0]
    n = s.get('nb_frames')
    if not n or n == 'N/A':
        r = subprocess.run(['ffprobe', '-v', 'error', '-count_frames', '-select_streams', 'v:0', '-show_entries', 'stream=nb_read_frames',
                            '-of', 'csv=p=0', p], capture_output=True, text=True, check=True)
        n = r.stdout.strip()
    a, b = s['r_frame_rate'].split('/')
    return {'frames': int(n), 'fps': float(a) / float(b), 'w': int(s['width']), 'h': int(s['height'])}


def encode_args(enc, fps):
    """Như encoder() của render.js — cùng một bộ thông số cho master."""
    rate = (['-b:v', enc['cbr'], '-minrate', enc['cbr'], '-maxrate', enc['cbr'], '-bufsize', enc['cbr'], '-x264-params', 'nal-hrd=cbr:force-cfr=1']
            if enc.get('cbr') else ['-crf', str(enc.get('crf', 16))])
    return ['-c:v', 'libx264', '-profile:v', 'high', '-preset', enc.get('preset', 'fast'), *rate, '-pix_fmt', 'yuv420p',
            '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709', '-color_range', 'tv', '-r', str(fps),
            '-video_track_timescale', '15360']


def seg_spine(s):
    """Spine của đoạn: s['spine'] (dict hoặc đường dẫn), không có thì <mp4>.build.json → <thư mục đoạn>/spine.json; không tìm thấy → None."""
    sp = s.get('spine')
    if isinstance(sp, dict):
        return sp
    if sp is None:
        bj = s['mp4'] + '.build.json'
        if not os.path.exists(bj):
            return None
        seg = json.load(open(bj)).get('segment')
        sp = os.path.join(ROOT, seg, 'spine.json') if seg else None
    return json.load(open(sp)) if sp and os.path.exists(sp) else None


def plan_joins(segs, fps):
    """Đọc `cuts` của spine mỗi đoạn → mối nối J/L giữa hai đoạn liền khung. Trả {id: {'trim': (a, b), 'pad': (trước, sau)}} (khung cục bộ của
    đoạn) và danh sách mối nối; khai sai → SystemExit. Không đoạn nào khai J/L → ({}, [])."""
    cut, joins = {}, []
    sp = {s['id']: seg_spine(s) for s in segs}
    for i, s in enumerate(segs):
        decl = ((sp[s['id']] or {}).get('cuts') or {})
        first = (s.get('scenes') or [None])[0]
        for sc, d in decl.items():
            kind = str((d or {}).get('cut', 'hard')).upper()
            if kind not in ('J', 'L', 'HARD'):
                raise SystemExit(f"splice {s['id']}: cuts.{sc}.cut = {d.get('cut')!r} (J|L|hard)")
            if kind == 'HARD':
                continue
            if sc != first:
                raise SystemExit(f"splice {s['id']}: J/L chỉ ở biên đoạn (cảnh đầu {first}); {sc} nằm trong đoạn — hình liền một lần render, đổi nhịp ở spine/scene.js")
            prev = segs[i - 1] if i else None
            if prev is None or prev['f1'] != s['f0']:
                raise SystemExit(f"splice {s['id']}: J/L ở {sc} cần một đoạn thế giới liền ngay trước (khung {s['f0']})")
            o = float(d.get('offset', 0))
            if not JL_RANGE[0] <= o <= JL_RANGE[1]:
                raise SystemExit(f"splice {s['id']}: cuts.{sc}.offset = {o} ngoài {JL_RANGE[0]}–{JL_RANGE[1]} s")
            n = int(round(o * fps))
            hid, hs = (s, sp[s['id']]) if kind == 'J' else (prev, sp[prev['id']])
            tot = (hid['f1'] - hid['f0']) / fps
            win = (0.0, n / fps) if kind == 'J' else (tot - n / fps, tot)   # khoảng (giây cục bộ) của đoạn không lên hình
            bad = sorted(round(t, 3) for b in (hs or {}).get('beats', []) for t in (b.get('cues') or {}).values() if win[0] <= float(t) <= win[1])
            if bad:
                raise SystemExit(f"splice {s['id']}: {kind}-cut {o} s giấu từ khoá {bad} s của {hid['id']} (khoảng {win[0]:.3f}–{win[1]:.3f} s) — lệch lời–hình; giảm offset")
            T = s['f0'] / fps
            tp = (s['f0'] + (n if kind == 'J' else -n)) / fps
            W = lambda x: [w for w in (x or {}).get('words', []) if not str(w['w']).startswith('[') and w['e'] > w['s']]
            wi, wo = W(sp[s['id']]), W(sp[prev['id']])
            joins.append({'scene': sc, 'from': prev['id'], 'to': s['id'], 'cut': kind, 'offset': round(n / fps, 4), 'frames': n,
                          't_sound': round(T, 4), 't_picture': round(tp, 4), 'zone': [round(min(T, tp), 4), round(max(T, tp), 4)],
                          'freeze': {'segment': prev['id'] if kind == 'J' else s['id'], 'frame': 'last' if kind == 'J' else 'first', 'frames': n},
                          'hidden': {'segment': hid['id'], 'local': [round(win[0], 4), round(win[1], 4)]},
                          # lời đoạn sau bắt đầu trước điểm cắt hình (J) / lời đoạn trước kết thúc sau điểm cắt hình (L), giây; V10 đòi ≥ 0,2 s
                          'voice_lead': round(tp - (T + wi[0]['s']), 3) if wi else None,
                          'voice_lag': round((prev['f0'] / fps + wo[-1]['e']) - tp, 3) if wo else None,
                          'moves_hidden': [m.get('id') for m in (hs or {}).get('moves', []) if win[0] <= float(m.get('t0', -1)) < win[1]]})
            cp = cut.setdefault(prev['id'], {'trim': [0, prev['f1'] - prev['f0']], 'pad': [0, 0]})
            cs = cut.setdefault(s['id'], {'trim': [0, s['f1'] - s['f0']], 'pad': [0, 0]})
            if kind == 'J':
                cp['pad'][1] += n; cs['trim'][0] += n
            else:
                cp['trim'][1] -= n; cs['pad'][0] += n
    return cut, joins


def splice_video(master, segs, out, fps, enc):
    """segs: [{id, mp4, f0, f1}] (khung của tập, không chồng nhau). Thay khung [f0, f1) của master bằng đoạn; mã hoá lại một lần.
    J/L (F-18): mối nối khai trong spine → mỗi seg mang 'join_in' (bản ghi mối nối), merge_audio trả lại trong 'joins'."""
    M = probe_video(master)
    if abs(M['fps'] - fps) > 1e-3:
        raise SystemExit(f"splice: master {M['fps']} fps ≠ tập {fps} fps")
    segs = sorted(segs, key=lambda s: s['f0'])
    cut, joins = plan_joins(segs, fps)
    for j in joins:
        next(s for s in segs if s['id'] == j['to'])['join_in'] = j
    ins, flt, parts, cur = ['-i', master], [], [], 0
    for k, s in enumerate(segs, 1):
        V = probe_video(s['mp4'])
        want = s['f1'] - s['f0']
        if abs(V['fps'] - fps) > 1e-3:
            raise SystemExit(f"splice {s['id']}: đoạn {V['fps']} fps ≠ tập {fps} fps")
        if V['frames'] != want:
            raise SystemExit(f"splice {s['id']}: đoạn {V['frames']} khung ≠ các cảnh {want} khung (f {s['f0']}–{s['f1']}) — đoạn phải khớp đúng các cảnh nó thay")
        if s['f0'] < cur or s['f1'] > M['frames']:
            raise SystemExit(f"splice {s['id']}: khung {s['f0']}–{s['f1']} chồng đoạn khác hoặc vượt master ({M['frames']} khung)")
        if s['f0'] > cur:
            flt.append(f"[0:v]trim=start_frame={cur}:end_frame={s['f0']},setpts=PTS-STARTPTS[p{len(parts)}]"); parts.append(None)
        ins += ['-i', s['mp4']]
        fit = '' if (V['w'], V['h']) == (M['w'], M['h']) else f",scale={M['w']}:{M['h']}:flags=lanczos"
        c = cut.get(s['id'])
        if c:   # J/L: bớt khung không lên hình, giữ khung đầu/cuối (tpad clone) — tổng khung của đoạn vẫn = want ± phần của đoạn bên cạnh
            a, b = c['trim']; pre, post = c['pad']
            pad = f",tpad=start={pre}:start_mode=clone:stop={post}:stop_mode=clone" if pre or post else ''
            flt.append(f"[{k}:v]trim=start_frame={a}:end_frame={b},setpts=PTS-STARTPTS{fit}{pad},setsar=1,format=yuv420p[p{len(parts)}]"); parts.append(None)
        else:
            flt.append(f"[{k}:v]trim=end_frame={want},setpts=PTS-STARTPTS{fit},setsar=1,format=yuv420p[p{len(parts)}]"); parts.append(None)
        s['probe'] = V
        cur = s['f1']
    if cur < M['frames']:
        flt.append(f"[0:v]trim=start_frame={cur},setpts=PTS-STARTPTS[p{len(parts)}]"); parts.append(None)
    flt.append(''.join(f'[p{i}]' for i in range(len(parts))) + f'concat=n={len(parts)}:v=1:a=0,setsar=1,format=yuv420p[v]')
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', *ins, '-filter_complex', ';'.join(flt), '-map', '[v]', *encode_args(enc, fps),
                    '-frames:v', str(M['frames']), out], check=True)
    O = probe_video(out)
    if O['frames'] != M['frames']:
        raise SystemExit(f"splice: master ghép {O['frames']} khung ≠ {M['frames']}")
    return {'frames': O['frames'], 'master_in': M}


def load(p, n):
    x, sr = sf.read(p, always_2d=True, dtype='float64')
    if sr != SR:
        raise SystemExit(f'splice: {p}: {sr} Hz (cần {SR})')
    x = x if x.shape[1] == 2 else np.repeat(x[:, :1], 2, 1)
    out = np.zeros((n, 2))
    out[:min(n, len(x))] = x[:n]
    return out, len(x)


def stem_files(d):
    return {os.path.splitext(f)[0]: os.path.join(d, f) for f in sorted(os.listdir(d)) if f.endswith(('.wav', '.flac'))}


def rms(x):
    return float(np.sqrt(np.mean(x ** 2))) if len(x) else 0.0


def merge_audio(stems_dir, segs, total, raw_out, fps):
    """stems_dir: stem của tập (voice bắt buộc, music nếu có nhạc nền) — ghi đè tại chỗ. segs: [{id, stems (thư mục), t0, t1}].
    Trả thông tin mỗi đoạn; raw_out = tổng các stem (bản mix trước master bus)."""
    N = int(round(total * SR))
    S = {k: load(p, N)[0] for k, p in stem_files(stems_dir).items()}
    if 'voice' not in S:
        raise SystemExit(f'splice: thiếu stem voice trong {stems_dir}')
    bed = 'music' in S
    info = []
    if bed:   # nhạc nền của tập tắt trong khoảng đoạn (đoạn mang nhạc riêng theo bản đồ căng)
        g = np.ones(N); t = np.arange(N) / SR
        for s in segs:
            g = np.minimum(g, np.clip(np.maximum((s['t0'] - t) / BED_FADE, (t - s['t1']) / BED_FADE), 0, 1))
        S['music'] *= g[:, None]
    for s in segs:
        i0, i1 = int(round(s['t0'] * SR)), int(round(s['t1'] * SR))
        n = i1 - i0
        F = stem_files(s['stems'])
        miss = [k for k in ['voice', *LAYERS] if k not in F and k not in OPTIONAL]
        if miss:
            raise SystemExit(f"splice {s['id']}: thiếu stem {miss} trong {s['stems']}")
        L = {}
        for k in ['voice', *LAYERS]:
            if k not in F:
                continue
            L[k], ln = load(F[k], n)
            if abs(ln - n) > SR / fps:
                raise SystemExit(f"splice {s['id']}: stem {k} dài {ln / SR:.3f} s ≠ các cảnh {n / SR:.3f} s")
        rv, re_ = rms(L['voice']), rms(S['voice'][i0:i1])
        basis = 'voice_rms' if rv > 1e-6 and re_ > 1e-6 else 'unity'   # đoạn không lời: giữ mức đoạn
        k = re_ / rv if basis == 'voice_rms' else 1.0
        added = {}
        for src, dst in LAYERS.items():
            if src not in L:
                continue
            S.setdefault(dst, np.zeros((N, 2)))
            S[dst][i0:i1] += L[src] * k
            added[dst] = round(20 * np.log10(rms(L[src] * k) + 1e-12), 1)
        info.append({'id': s['id'], 'gain_db': round(20 * np.log10(k), 2), 'gain_basis': basis,
                     'layers_rms_dbfs': added, 'bed_off': bed})
    mix = sum(S.values())
    pk = float(np.abs(mix).max())
    sc = 0.98 / pk if pk > 0.98 else 1.0   # cùng một hệ số cho mọi stem → tổng các stem vẫn = mix-raw
    for f in os.listdir(stems_dir):
        os.remove(os.path.join(stems_dir, f))
    for name, x in S.items():
        sf.write(os.path.join(stems_dir, name + '.flac'), x * sc, SR, subtype='PCM_24')
    sf.write(raw_out, mix * sc, SR, subtype='PCM_24')
    out = {'segments': info, 'stems': sorted(S), 'peak_scale': round(sc, 4)}
    joins = [s['join_in'] for s in segs if s.get('join_in')]
    if joins:   # F-18: tiếng không dời ở J/L — chỉ ghi mối nối (splice_video đặt 'join_in') để splice.json mang nó
        out['joins'] = joins
    return out


def transitions(splice_json, trans_json):
    """F-18: ghi điểm cắt HÌNH của mỗi mối nối J/L (splice.json audio.joins) vào out/transitions.json (checks/CONTRACT.md): thay mục cùng
    from/to (biên đoạn), không có thì thêm. t = mốc cắt hình; audio = j|l; reason ghi độ lệch."""
    rec = json.load(open(splice_json))
    joins = (rec.get('audio') or {}).get('joins') or []
    tr = json.load(open(trans_json)) if os.path.exists(trans_json) else {'cuts': []}
    for j in joins:
        c = {'t': j['t_picture'], 'from': j['from'], 'to': j['to'], 'type': 'cut', 'match': None, 'audio': j['cut'].lower(),
             'reason': f"{j['cut']}-cut {j['offset']} s at the segment boundary ({j['scene']}): sound of the "
                       f"{'next' if j['cut'] == 'J' else 'previous'} segment carries across the picture cut; sound not moved (F-18)"}
        k = next((i for i, x in enumerate(tr['cuts']) if x.get('from') == j['from'] and x.get('to') == j['to']), None)
        if k is None:
            tr['cuts'].append(c)
        else:
            tr['cuts'][k] = c
    tr['cuts'].sort(key=lambda x: x['t'])
    json.dump(tr, open(trans_json, 'w'), indent=1, ensure_ascii=False)
    return len(joins)


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 4 and sys.argv[1] == '--transitions':
        print(f'transitions: {transitions(sys.argv[2], sys.argv[3])} mối nối J/L → {sys.argv[3]}')
    else:
        raise SystemExit('python3 splice.py --transitions <out/factory/splice.json> <out/transitions.json>')
