"""Tập 6 · tiện ích chung cho các đoạn thế giới 3D (spine v2, D-010). Chỉ dùng take ĐÃ CÓ trong voice-takes/ (0 ký tự ElevenLabs).
  scene_take(sc)        → take của cảnh theo review-g1/voice-scenes.json (take commit của tập), kiểm chữ take == chữ kịch bản hiện tại
  scene_words(sc)       → từ (đã nói, có sid = câu kịch bản), đầu từ chỉnh theo năng lượng (onset.refine), giờ tính trong take
  episode_offsets()     → vị trí mỗi cảnh trong tập như nhà máy (take + đuôi 1,0 s; ident 3 s sau S03 như table_read.py)
  clip_voice(sids, lead)→ lời cho một đoạn ngắn (C3): cắt từ take theo câu (wav trong work/, không commit), từ đã dời giờ
Không gọi API: thiếu take → dừng (SystemExit)."""
import json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.dirname(HERE)
ROOT = os.path.abspath(os.path.join(EP, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'toolkit', 'factory', 'world'))
sys.path.insert(0, os.path.join(ROOT, 'toolkit', 'factory'))
sys.dont_write_bytecode = True
from onset import refine  # noqa: E402
TAKES = os.path.join(EP, 'voice-takes')
LINE = re.compile(r'^(S\d\d)\.(\d+)\s+(?:\{(\w+)\}\s+)?(.+?)\s*<!--')
TAIL, IDENT_AFTER, IDENT = 1.0, 'S03', 3.0


def script_rows():
    out = []
    for ln in open(os.path.join(EP, 'story', 'script.md'), encoding='utf-8'):
        m = LINE.match(ln)
        if m: out.append({'id': f'{m.group(1)}.{m.group(2)}', 'scene': m.group(1), 'text': m.group(4).strip()})
    return out


def voice_scenes():
    return json.load(open(os.path.join(EP, 'review-g1', 'voice-scenes.json')))


def scene_take(sc):
    vs = voice_scenes()
    if sc not in vs: raise SystemExit(f'không có take cho {sc} trong voice-scenes.json — dừng (không sinh giọng)')
    h = vs[sc]['take'].replace('.mp3', '')
    mp3, js = os.path.join(TAKES, h + '.mp3'), os.path.join(TAKES, h + '.json')
    if not (os.path.exists(mp3) and os.path.exists(js)): raise SystemExit(f'take {h} của {sc} không có trong voice-takes/ — dừng')
    return h, mp3, json.load(open(js)), vs[sc]['duration']


_SPOKEN = {}


def spoken(rows):
    import voice as V                       # toolkit/factory/voice.py: chỉ dùng to_spoken (node, không mạng)
    key = tuple(r['text'] for r in rows)
    if key not in _SPOKEN: _SPOKEN[key] = V.to_spoken(list(key))
    return _SPOKEN[key]


def scene_words(sc, do_refine=True):
    h, mp3, meta, dur = scene_take(sc)
    rows = [r for r in script_rows() if r['scene'] == sc]
    sp = spoken(rows); text = ' '.join(sp)
    al = meta['alignment']
    if ''.join(al['characters']) != text or meta['text'] != text:
        raise SystemExit(f'{sc}: chữ take {h} khác chữ kịch bản hiện tại — dừng (cần đọc lại giọng)')
    st, en = al['character_start_times_seconds'], al['character_end_times_seconds']
    bounds, pos = [], 0
    for r, s in zip(rows, sp): bounds.append((r['id'], pos, pos + len(s))); pos += len(s) + 1
    words = []
    for m in re.finditer(r'\S+', text):
        sid = next(b[0] for b in bounds if b[1] <= m.start() < b[2])
        words.append({'w': m.group(0), 's': round(st[m.start()], 3), 'e': round(en[m.end() - 1], 3), 'sid': sid})
    if do_refine:
        words = refine(words, mp3)
    return {'hash': h, 'mp3': os.path.relpath(mp3, ROOT), 'duration': dur, 'words': words, 'lines': {r['id']: r['text'] for r in rows}}


def episode_offsets():
    """Vị trí đầu mỗi cảnh trong tập (giây) theo luật nhà máy: take + đuôi 1,0 s; ident 3 s sau S03 (table_read.py)."""
    vs, t, out = voice_scenes(), 0.0, {}
    for sc in sorted(vs):
        out[sc] = round(t, 3); t += vs[sc]['duration'] + TAIL + (IDENT if sc == IDENT_AFTER else 0)
    out['_end'] = round(t, 3)
    return out


def clip_voice(runs, lead=0.6, tail=0.25, pre=0.15, gap_same=0.6):
    """Lời cho một đoạn C3. runs = [[sid, sid…], …]: mỗi run là các câu LIỀN NHAU của một cảnh. Mỗi run: cắt take từ (đầu câu đầu − pre)
    tới (cuối câu cuối + tail) thành wav 48 kHz trong episodes/ep006/work/world-voice/ (không commit); run nối nhau cách 1,0 s
    (khác cảnh, như nhà máy) hoặc gap_same (cùng cảnh, bỏ câu giữa). Trả (words, takes, lines, end) — takes theo audio.py ({'wav', 't'})."""
    out_dir = os.path.join(EP, 'work', 'world-voice'); os.makedirs(out_dir, exist_ok=True)
    t, words, takes, lines, prev = lead, [], [], {}, None
    for ss in runs:
        sc = ss[0][:3]
        if prev is not None: t += TAIL if sc != prev else gap_same
        W = scene_words(sc)
        ws = [w for w in W['words'] if w['sid'] in ss]
        if not ws or ws[0]['sid'] != ss[0] or ws[-1]['sid'] != ss[-1]: raise SystemExit(f'câu {ss} không có trong take {sc}')
        a = max(0.0, float(min(w['s'] for w in ws)) - pre); b = float(max(w['e'] for w in ws)) + tail
        wav = os.path.join(out_dir, f"{W['hash']}-{a:.3f}-{b:.3f}.wav")
        if not os.path.exists(wav):
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{a:.3f}', '-to', f'{b:.3f}', '-i', os.path.join(ROOT, W['mp3']), '-ar', '48000', '-ac', '1',
                            '-af', 'afade=t=in:d=0.02,afade=t=out:st={:.3f}:d=0.03'.format(b - a - 0.03), wav], check=True)
        words += [{'w': w['w'], 's': round(float(w['s']) - a + t, 3), 'e': round(float(w['e']) - a + t, 3), 'sid': w['sid'],
                   's_tts': round(float(w['s_tts']) - a + t, 3)} for w in ws]
        takes.append({'wav': os.path.relpath(wav, ROOT), 'mp3': W['mp3'], 'take': W['hash'], 'from': round(a, 3), 'to': round(b, 3), 't': round(t, 3)})
        lines.update({s: W['lines'][s] for s in ss})
        t += b - a; prev = sc
    return words, takes, lines, round(t, 3)


def music_plan_flat(total, accents):
    """Đoạn C3 ngắn: nhạc không tắt giữa đoạn (stop = cuối), điểm nhấn felt ở các mốc dữ liệu."""
    return {'stop': total, 'tau': 0.25, 'release': total + 1.0, 'accents': accents[:4]}
