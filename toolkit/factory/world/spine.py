"""Nhà máy · SPINE v2 — đặc tả nhịp "một thế giới, hai chế độ máy quay" (D-010), rút từ hai đoạn chứng minh Mốc V.
Một nguồn duy nhất cho mọi lớp: lời (take), hình (chế độ, tư thế máy, cửa sổ động tác), âm dữ liệu, sfx, nhạc (bản đồ căng).
Mốc giờ CHỈ từ alignment của take ("@câu[:từ][$]"), đầu từ chỉnh theo năng lượng (onset.refine). Đoạn khai báo nhịp + động tác;
thư viện tính cửa sổ, âm của động tác, cảnh render (cache) và tự kiểm quy tắc 2/3/7. Quy tắc 1 kiểm trên nhật ký trang (verify_seg.py).

  from spine import Anchors, beats_from, window, move_sounds, shots_for, check_rules
  A = Anchors(words); beats = beats_from(B, A, lines); moves = [...window(...)...]; errs = check_rules(beats, moves, pad)
"""
import re


class Anchors:
    """words: [{w, s, e, sid}] (đã cộng vị trí take). at('@S01.2:twenty') = đầu từ; '@S01.2$' = cuối câu; '@S01.2' = từ đầu câu."""
    def __init__(self, words):
        self.words = words

    def at(self, ref):
        m = re.match(r'@(S\d\d\.\d)(?::([^$]+))?(\$)?$', ref)
        if not m:
            raise SystemExit(f'mốc sai: {ref!r}')
        sid, wd, e = m.groups(); ws = [w for w in self.words if w['sid'] == sid]
        if not ws:
            raise SystemExit(f'mốc {ref!r}: không có câu {sid} trong take')
        if e: return ws[-1]['e']
        if wd:
            hit = [w['s'] for w in ws if re.sub(r'[^\w-]', '', w['w']).lower().startswith(wd.lower())]
            if not hit: raise SystemExit(f'mốc {ref!r}: không có từ {wd!r} trong {sid}')
            return hit[0]
        return next(w['s'] for w in ws if not w['w'].startswith('['))


def words_from_timeline(timeline, scenes):
    """Lời của nhà máy (out/factory/timeline.json sau bước resolve) → words cho Anchors, giờ tính từ đầu cảnh đầu tiên của đoạn.
    Trả (words, t0 của đoạn trong tập, độ dài đoạn). Đoạn thế giới của một tập dùng đúng take đã dựng, không sinh lại giọng."""
    sc = [s for s in timeline['scenes'] if s['id'] in scenes]
    if [s['id'] for s in sc] != list(scenes): raise SystemExit(f'cảnh {scenes} không liền/không có trong timeline')
    t0, t1 = sc[0]['start'], sc[-1]['start'] + sc[-1]['dur']
    ws = [{'w': w['w'], 's': round(w['s'] - t0, 3), 'e': round(w['e'] - t0, 3), 'sid': w['sid']} for w in timeline['words'] if t0 <= w['s'] < t1]
    return ws, t0, round(t1 - t0, 4)


def beats_from(B, A, lines):
    """B: [(id, sid, mode world|chart, ý, hình, {cue: '@…'}, [âm], căng 0–1, cảm xúc, chuyển)] → nhịp có t0/t1/cues (giây)."""
    out = []
    for bid, sid, mode, idea, visual, cues, sound, ten, emo, nxt in B:
        if mode not in ('world', 'chart'): raise SystemExit(f'{bid}: chế độ {mode!r} (world|chart)')
        out.append({'id': bid, 'sid': sid, 'mode': mode, 'idea': idea, 'visual': visual, 'line': lines[sid], 'sound': sound, 'music': ten,
                    'emotion': emo, 'next': nxt, 't0': A.at('@' + sid), 't1': A.at('@' + sid + '$'), 'cues': {k: A.at(v) for k, v in cues.items()}})
    return out


def cue_list(beats):
    return sorted((t, f"{b['id']}.{k}") for b in beats for k, t in b['cues'].items())


def window(after, before, dur, pad=0.25, late=False, start=None, eps=0.0):
    """Cửa sổ động tác giữa hai từ khoá: bắt đầu sau after+pad, kết thúc trước before−pad, dài tối đa dur.
    late: sát từ khoá sau; start: neo vào một mốc (vd đầu câu); eps: lùi mép phải thêm (Tập 5 dùng 0,01)."""
    a, b = after + pad, before - pad
    if b - a < 0.6: raise SystemExit(f'cửa sổ quá ngắn giữa {after} và {before}')
    b -= eps
    t0 = max(a, b - dur) if late else max(a, (a + b) / 2 - dur / 2)
    if start is not None: t0 = min(max(a, start), b - 0.6)
    return [round(t0, 3), round(min(b, t0 + dur), 3)]


VERBS = ('push', 'pull', 'pan', 'mode')
# F-1 (BACKLOG): kiểu chuyển chế độ, cờ opt-in trên động tác 'mode': không khai = 'dissolve' (hành vi cũ, điểm ảnh không đổi);
# 'fly' = máy quay đi thật (core.js flyPose: đường cong qua tư thế 'via', dolly-zoom tới tiêu cự dài, chartW chỉ dâng khi đã chính diện).
# Cửa sổ, âm, cảnh render KHÔNG phụ thuộc kiểu → quy tắc 2/3 giữ nguyên.
MODE_STYLES = ('dissolve', 'fly')


def with_style(move, style=None, via=None):
    """Gắn kiểu chuyển chế độ vào một động tác (không đổi t0/t1/âm). style None/'dissolve' → trả nguyên động tác (spine.json không đổi)."""
    if style in (None, 'dissolve'):
        return move
    if style not in MODE_STYLES or move['verb'] != 'mode':
        raise SystemExit(f'F-1: kiểu {style!r} chỉ cho động tác mode, một trong {MODE_STYLES}')
    return {**move, 'style': style, **({'via': via} if via else {})}


def move_sounds(moves, gain=lambda m: 1.0):
    """Quy tắc 3: mọi động tác có âm (sound của nó, dài bằng cửa sổ); chỉ đổi chế độ mới có tiếng chạm ở cuối."""
    ev = []
    for m in moves:
        ev.append({'t': m['t0'], 'kind': m['sound'], 'dur': round(m['t1'] - m['t0'], 3), 'gain': gain(m)})
        if m['verb'] == 'mode': ev.append({'t': m['t1'], 'kind': 'land', 'mode': True})
    return ev


def shots_for(moves, total):
    """Quy tắc 8: cảnh render (đơn vị cache) = ranh giới ở đầu mỗi động tác máy quay."""
    cuts = [0] + [m['t0'] for m in moves] + [total]
    return [{'id': f's{i}', 't0': round(a, 3), 't1': round(b, 3)} for i, (a, b) in enumerate(zip(cuts, cuts[1:]))]


def check_rules(beats, moves, pad, rule3=True):
    """Quy tắc 2 (máy đứng yên ± pad quanh mọi từ khoá), 3 (động tác hữu hạn, có lý do + âm), 7 (5 s đầu ở chế độ thế giới)."""
    errs, C = [], cue_list(beats)
    for m in moves:
        for t, name in C:
            if m['t0'] - pad < t < m['t1'] + pad: errs.append(f'quy tắc 2: từ khoá {name} @{t} trong cửa sổ máy quay {m["verb"]} {m["t0"]}–{m["t1"]}')
        if rule3 and (not m.get('reason') or not m.get('sound') or m['verb'] not in VERBS):
            errs.append(f'quy tắc 3: động tác {m} thiếu lý do/âm hoặc động từ ngoài {VERBS}')
        if m.get('style', 'dissolve') not in MODE_STYLES or (m.get('style') == 'fly' and m['verb'] != 'mode'):
            errs.append(f'F-1: kiểu chuyển {m.get("style")!r} không hợp lệ cho {m["verb"]} (chỉ mode, {MODE_STYLES})')
    if beats[0]['mode'] != 'world' or any(m['verb'] == 'mode' and m['t0'] < 5.0 for m in moves):
        errs.append('quy tắc 7: 5 s đầu phải ở chế độ thế giới')
    return errs
