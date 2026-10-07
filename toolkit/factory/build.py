"""Crux factory build (Mốc B): one command from episode.yaml to master, parts, Shorts and the qc table.

  bash toolkit/build.sh episodes/epNNN/episode.yaml [--workers 4] [--fmt jpeg|rgba] [--no-cache] [--checks]

Steps (each timed → out/factory/build-report.json):
  spec    toolkit/factory/spec.py (BLOCK/ASK stop the build before any API call)
  voice   one ElevenLabs with-timestamps request per scene, SHA-256 cache (voice.py)
  resolve "@sentence[:word][$][+s]" → seconds; a visual never starts before its word; timeline.json + captions.srt
  world   (episode.yaml `world:`) each 3D world segment built + checked by world/build_seg.py; spine total must equal its scenes
  render  segments = shot × ≤ 5 s chunks; hash = segment spec + resolved anchors + code hash + data/claims/tokens; only misses render
  splice  (F-5, world/splice.py) world segment frames replace the frames of its scenes; picture re-encoded once; timeline marks `world`
  mix     voice (+ optional music with ducking) (+ world segment music/sonify/sfx/room into the stems), loudnorm two-pass −14 LUFS /
          ≤ −1 dBTP, AAC → master (concat copy of segments, or the spliced picture)
  parts   3 parts 720p ≤ 90 MB cut at the shot boundaries nearest 1/3 and 2/3
  artefacts (world:) out/camera.json + out/sonify-events.json (world/artefacts.py) and the checks page: out/page.json → one-file
          window.CHECKS page of every world segment (world/episode_page.py; checks-appeal A11)
  shorts  shots in range re-rendered 1080×1920 (always 1080, whatever `res`), narration cut from the master and loudnormed to −14 LUFS /
          −1.5 dBTP, hook line, end card 1.5 s; a Short whose span lies inside one `world:` segment is re-rendered from that segment's scene
          at 1080×1920 (world/shorts.py: vertical window of the same camera, text ≥ 56 px in the vertical safe area, ILLUSTRATIVE + history on
          every frame with a number, counterweights in turn)
  qc      toolkit/factory/qc.py (builder rules; checks/ stays the judge)
Work files (video, cache) go to <episode>/work/factory/ (not committed); reports to <episode>/out/factory/.
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time

import yaml

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
sys.path.insert(1, os.path.join(HERE, 'world'))
import spec as SPEC  # noqa: E402
import voice as VOICE  # noqa: E402

ENCODE_H = {'cbr': '17M', 'preset': 'fast'}   # master picture (render.js encoder; world/splice.py re-encodes with the same)
CHUNK = 150  # frames per segment (5 s at 30 fps): enough pieces for 4 workers on a 70 s scene
CODE = ['lib/engine.js', 'lib/templates.js', 'page.html', 'render.js']


def sh(cmd, **kw):
    return subprocess.run(cmd, check=True, **kw)


def sha(b):
    return hashlib.sha256(b if isinstance(b, bytes) else json.dumps(b, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def probe_dur(p):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p],
                                capture_output=True, text=True, check=True).stdout)


def norm(w):
    return re.sub(r"[^a-z0-9'-]", '', w.lower()).strip("'-")


class Resolver:
    """Anchors of one scene → scene-local seconds, from the word alignment of its voice."""

    def __init__(self, v, script):
        self.v, self.words, self.sent = v, v['words'], {s['id']: s for s in v['sentences']}
        self.script = script

    def word_time(self, a):
        m = SPEC.ANCHOR.match(a)
        sid = m['sid']
        if m['end']:
            t = self.sent[sid]['end']
        elif m['word']:
            want = [norm(x) for x in VOICE.to_spoken([m['word']])[0].split()]
            ws = [w for w in self.words if w['sid'] == sid]
            toks = [norm(w['w']) for w in ws]
            hit = next((i for i in range(len(toks) - len(want) + 1) if toks[i:i + len(want)] == want), None)
            if hit is None:
                raise SystemExit(f'anchor {a}: words {want} not found in {sid} ("{self.sent[sid]["spoken"]}")')
            t = ws[hit]['s']
        else:
            t = self.sent[sid]['start']
        return t + float(m['off'] or 0)


def resolve_params(p, R, t0, anchors, shot_id, key=''):
    """Replace every anchor string in p by seconds since the shot start (≥ 0, so a visual is never earlier than its word)."""
    if isinstance(p, str) and p.startswith('@'):
        wt = R.word_time(p)
        rel = max(0.0, wt - t0)
        anchors.append({'shot': shot_id, 'param': key, 'anchor': p, 'word_t': round(wt, 3), 'visual_t': round(t0 + rel, 3)})
        return round(rel, 4)
    if isinstance(p, list):
        return [resolve_params(x, R, t0, anchors, shot_id, f'{key}[{i}]') for i, x in enumerate(p)]
    if isinstance(p, dict):
        return {k: resolve_params(x, R, t0, anchors, shot_id, f'{key}.{k}' if key else k) for k, x in p.items()}
    return p


def frame_size(orient, res):
    """Khung render theo `res` của episode.yaml (1080 → 1920×1080; 720 → 1280×720; 540 → 960×540 bản xem trước của đoạn thế giới)."""
    size = [1920, 1080] if orient == 'h' else [1080, 1920]
    return size if res == 1080 else [round(x * res / 1080) for x in size]


def blank_picture(out, size, fps, total):
    """Tập chỉ có đoạn thế giới: hình nền đen đúng round(total·fps) khung, cùng thông số mã hoá master (splice thay mọi khung)."""
    import splice as SPLICE   # world/splice.py: encode_args = thông số H.264 của render.js
    n = round(total * fps)
    sh(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'lavfi', '-i', f'color=c=black:s={size[0]}x{size[1]}:r={fps}', '-frames:v', str(n),
        *SPLICE.encode_args(ENCODE_H, fps), out])
    return n


def srt_time(t):
    ms = int(round(t * 1000))
    return f'{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}'


def wrap(text, width=42):
    lines, cur = [], ''
    for w in text.split():
        if cur and len(cur) + 1 + len(w) > width:
            lines.append(cur); cur = w
        else:
            cur = f'{cur} {w}'.strip()
    return lines + [cur] if cur else lines


def caption_cues(sents, words):
    """Captions from the written text (DX-F5): cues of ≤ 2 lines × 42 chars and 1–7 s, split at word boundaries (commas first);
    each written chunk is timed by the spoken words it becomes (toSpoken of the chunk, consumed in order)."""
    cues = []
    for s in sents:
        ws = [w for w in words if w['sid'] == s['id']]
        toks, chunks, cur = s['text'].split(), [], []
        for tkn in toks:
            if cur and (len(wrap(' '.join(cur + [tkn]))) > 2):
                chunks.append(cur); cur = []
            cur.append(tkn)
            if len(' '.join(cur)) >= 44 and re.search(r'[,;:]$', tkn):
                chunks.append(cur); cur = []
        if cur:
            chunks.append(cur)
        spoken = VOICE.to_spoken([' '.join(c) for c in chunks])
        k = 0
        for c, sp in zip(chunks, spoken):
            n = len(sp.split()); seg = ws[k:k + n] or ws[-1:]; k += n
            cues.append({'s': seg[0]['s'], 'e': seg[-1]['e'], 'lines': wrap(' '.join(c))})
    for i, c in enumerate(cues):  # 1–7 s, no overlap: stretch short cues into the gap, split nothing further (long ones are rare at 2×42)
        nxt = cues[i + 1]['s'] if i + 1 < len(cues) else c['e'] + 2
        if c['e'] - c['s'] < 1.0:
            c['e'] = min(c['s'] + 1.0, nxt - 0.001)
        c['e'] = min(c['e'], c['s'] + 7.0, nxt - 0.001) if i + 1 < len(cues) else min(c['e'], c['s'] + 7.0)
    return cues


class Build:
    def __init__(self, yml, argv):
        self.yml = os.path.abspath(yml)
        self.root = os.path.dirname(self.yml)
        self.S = yaml.safe_load(open(self.yml))
        self.argv = argv
        self.workers = int(argv[argv.index('--workers') + 1]) if '--workers' in argv else 4
        self.fmt = argv[argv.index('--fmt') + 1] if '--fmt' in argv else 'jpeg'
        self.nocache = '--no-cache' in argv
        self.work = os.path.join(self.root, 'work', 'factory')
        self.out = os.path.join(self.root, 'out', 'factory')
        for d in (self.work, self.out, os.path.join(self.work, 'cache'), os.path.join(self.work, 'jobs')):
            os.makedirs(d, exist_ok=True)
        self.fps = self.S.get('fps', 30)
        self.report = {'episode': self.S['episode'], 'yaml': os.path.relpath(self.yml, ROOT), 'steps': {}, 'started': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}

    def step(self, name, fn):
        t = time.time()
        r = fn()
        self.report['steps'][name] = {'seconds': round(time.time() - t, 2), **(r or {})}
        print(f'[{name}] {self.report["steps"][name]["seconds"]} s', flush=True)
        return r

    # ---- spec
    def do_spec(self):
        P = SPEC.check(self.S, self.root)
        self.report['spec'] = P
        for p in P:
            print(f"  spec {p['level']} {p['rule']}: {p['msg']}")
        if any(p['level'] in ('BLOCK', 'ASK') for p in P):
            json.dump(self.report, open(os.path.join(self.out, 'build-report.json'), 'w'), indent=1, ensure_ascii=False)
            raise SystemExit('spec: blocked (see above); ASK items go to the owner')
        return {'problems': len(P)}

    # ---- inputs shared by every job
    def load_inputs(self):
        S = self.S
        cl = json.load(open(os.path.join(self.root, S['claims'])))['claims']
        self.claims = {c['claimId']: {'display': c['display'], 'value': c['value'], 'historical': bool(c.get('historical')),
                                      'illustrative': bool(c.get('illustrative'))} for c in cl}
        self.tokens = json.load(open(os.path.join(self.root, S['tokens'])))
        d = S['data']
        txt = open(os.path.join(self.root, d['file'])).read()
        self.data = json.loads(txt[txt.index('=') + 1:].strip().rstrip(';')) if d['file'].endswith('.js') else json.loads(txt)
        self.script = {s['id']: s for s in json.load(open(os.path.join(self.root, S['script'])))['sentences']}
        # custom_symbols: [{id, file}] (file relative to the episode) → imported by page.html into TEMPLATES[id]; code is part of the cache hash
        self.symbols = [{'id': c['id'], 'url': '/' + os.path.relpath(os.path.join(self.root, c['file']), ROOT)} for c in S.get('custom_symbols') or []]
        self.code_hash = sha(b''.join(open(os.path.join(HERE, f), 'rb').read() for f in CODE)
                             + b''.join(open(ROOT + c['url'], 'rb').read() for c in self.symbols))
        self.counterweights = [{k: c[k] for k in ('id', 'text', 'claims', 'when', 'attach') if k in c} for c in S.get('counterweights') or []]
        self.inputs_hash = sha({'claims': self.claims, 'tokens': self.tokens, 'data': sha(txt.encode()), 'cw': self.counterweights})

    # ---- voice
    def do_voice(self):
        self.voices, chars, hits = {}, 0, 0
        for sc in self.S['scenes']:
            sents = [s for s in self.script.values() if s['scene'] == sc['id']]
            cfg = VOICE.scene_cfg(self.S['voice'], self.S.get('voice_overrides'), sc['id'])   # B+1: seed/take per scene
            v = VOICE.voice_scene(cfg, sents, os.path.join(self.root, 'voice-takes'), os.path.join(self.work, 'voice'))
            self.voices[sc['id']] = v
            hits += v['cached']
            chars += 0 if v['cached'] else v['chars']
        return {'scenes': len(self.voices), 'cache_hits': hits, 'el_chars_spent': chars}

    # ---- resolve
    def do_resolve(self):
        fps, t, shots, anchors, sents, words, scenes = self.fps, 0.0, [], [], [], [], []
        for sc in self.S['scenes']:
            v = self.voices[sc['id']]
            R = Resolver(v, self.script)
            dur = round(round((v['duration'] + sc.get('tail', 1.0)) * fps) / fps, 4)
            starts = [0.0] + [R.word_time(s['from']) for s in sc['shots'][1:]]
            starts = [round(round(x * fps) / fps, 4) for x in starts]  # shot starts on a frame: anchors resolve against it
            for i, s in enumerate(sc['shots']):
                t0, t1 = starts[i], starts[i + 1] if i + 1 < len(starts) else dur
                p = resolve_params(s.get('p', {}), R, t0, anchors, s['id'])
                shots.append({'id': s['id'], 'scene': sc['id'], 'template': s['template'], 't0': round(t + t0, 4), 't1': round(t + t1, 4), 'p': p})
            for a in anchors:
                if 'scene' not in a:
                    a.update(scene=sc['id'], word_t=round(a['word_t'] + t, 3), visual_t=round(a['visual_t'] + t, 3))
            for s in v['sentences']:
                sents.append({'id': s['id'], 'scene': sc['id'], 'text': self.script[s['id']]['text'], 'spoken': s['spoken'],
                              'start': round(s['start'] + t, 3), 'end': round(s['end'] + t, 3)})
            words += [{**w, 's': round(w['s'] + t, 3), 'e': round(w['e'] + t, 3)} for w in v['words']]
            scenes.append({'id': sc['id'], 'start': round(t, 4), 'dur': dur})
            t += dur
        self.total = round(t, 4)
        self.tl = {'fps': fps, 'total': self.total, 'scenes': scenes, 'shots': shots, 'sentences': sents, 'words': words, 'anchors': anchors}
        json.dump(self.tl, open(os.path.join(self.out, 'timeline.json'), 'w'), indent=1, ensure_ascii=False)
        cues = caption_cues(sents, words)
        with open(os.path.join(self.out, 'captions.srt'), 'w') as f:
            for i, c in enumerate(cues, 1):
                f.write(f"{i}\n{srt_time(c['s'])} --> {srt_time(c['e'])}\n" + '\n'.join(c['lines']) + '\n\n')
        return {'total': self.total, 'shots': len(shots), 'anchors': len(anchors)}

    # ---- render (shared by master and Shorts)
    def render(self, name, shots, orient, total, hook=None, encode=None, res=None):
        """shots: [{id, template, t0, t1, p}] in job-local seconds. Returns the ordered segment files (cache paths)."""
        fps, res = self.fps, res or self.S.get('res', 1080)
        size = frame_size(orient, res)
        encode = encode or (ENCODE_H if orient == 'h' else {'crf': 14, 'preset': 'fast'})
        base = {'orient': orient, 'res': res, 'fps': fps, 'fmt': self.fmt, 'quality': 0.95, 'encode': encode, 'hook': hook,
                'code': self.code_hash, 'inputs': self.inputs_hash}
        segs, todo = [], []
        for s in shots:
            f0, f1 = round(s['t0'] * fps), min(round(s['t1'] * fps), round(total * fps))
            local = {**s, 't0': s['t0'] - f0 / fps, 't1': s['t1'] - f0 / fps}  # shot-local: the segment hash ignores where the shot sits
            for a in range(0, f1 - f0, CHUNK):
                b = min(a + CHUNK, f1 - f0)
                h = sha({**base, 'shot': local, 'range': [a, b]})[:20]
                out = os.path.join(self.work, 'cache', f'{h}.mp4')
                seg = {'id': f"{s['id']}#{a // CHUNK}", 'shot': s['id'], 'f0': a, 'f1': b, 'out': out, 'hash': h, 'local': local}
                segs.append(seg)
                if self.nocache or not os.path.exists(out + '.log.json'):
                    todo.append(seg)
        if todo:
            shots_local = {}
            for g in todo:
                shots_local[g['shot']] = g['local']
            job = {'name': name, **base, 'size': size, 'tokens': self.tokens, 'claims': self.claims, 'data': self.data,
                   'floor': {'h': 40, 'v': 56}, 'counterweights': self.counterweights, 'symbols': self.symbols, 'shots': list(shots_local.values()),
                   'segments': [{k: g[k] for k in ('id', 'shot', 'f0', 'f1', 'out')} for g in todo]}
            jp = os.path.join(self.work, 'jobs', f'{name}.json')
            json.dump(job, open(jp, 'w'))
            env = {**os.environ, 'NODE_PATH': subprocess.run(['npm', 'root', '-g'], capture_output=True, text=True).stdout.strip()}
            r = subprocess.run(['node', os.path.join(HERE, 'render.js'), jp, '--workers', str(self.workers), '--fmt', self.fmt],
                               env=env, capture_output=True, text=True)
            if r.returncode:
                print(r.stdout[-2000:], r.stderr[-4000:])
                raise SystemExit('render failed')
            stat = json.loads(r.stdout.strip().splitlines()[-1])['render']
        else:
            stat = {'frames': 0, 'seconds': 0}
        return segs, {'segments': len(segs), 'rendered': len(todo), 'cache_hits': len(segs) - len(todo), **stat}

    # ---- world (D-010, Mốc V): mỗi đoạn thế giới 3D dựng + kiểm bằng world/build_seg.py; spine của đoạn đọc lời từ timeline.json
    def do_world(self):
        res, out = {}, {}
        for w in self.S.get('world') or []:
            seg = os.path.join(self.root, w['dir'])
            env = {**os.environ, 'CRUX_TIMELINE': os.path.join(self.out, 'timeline.json'), 'CRUX_WORLD_SCENES': ','.join(w['scenes'])}
            mp4 = os.path.join(self.work, 'world', f"{w['id']}-{self.S.get('res', 1080)}.mp4")
            r = subprocess.run([sys.executable, os.path.join(HERE, 'world', 'build_seg.py'), seg, '--res', str(self.S.get('res', 1080)), '--out', mp4,
                                '--workers', str(self.workers)], env=env, capture_output=True, text=True)
            print(r.stdout[-1500:])
            if r.returncode:
                print(r.stderr[-3000:])
                raise SystemExit(f"world {w['id']}: build_seg failed (see above)")
            sp = json.load(open(os.path.join(seg, 'spine.json')))
            dur = sum(s['dur'] for s in self.tl['scenes'] if s['id'] in w['scenes'])
            if abs(sp['total'] - dur) > 1 / self.fps:
                raise SystemExit(f"world {w['id']}: spine total {sp['total']} s ≠ scenes {w['scenes']} {dur:.3f} s (đoạn phải khớp đúng các cảnh nó thay)")
            res[w['id']] = json.load(open(mp4 + '.build.json'))['steps']
            out[w['id']] = mp4
        self.world = out
        return {'segments': res}

    def concat(self, segs, out):
        lst = out + '.txt'
        with open(lst, 'w') as f:
            for g in segs:
                f.write(f"file '{g['out']}'\n")
        sh(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', out])
        os.remove(lst)

    def do_render(self):
        shots = [{k: s[k] for k in ('id', 'template', 't0', 't1', 'p')} for s in self.tl['shots']]
        if not shots:   # D-010: mọi cảnh là đoạn thế giới (world:) → không có shot 2D; nền đen đúng số khung, splice thay toàn bộ
            if not self.S.get('world'):
                raise SystemExit('render: no 2D shot and no world segment')
            self.picture = os.path.join(self.work, 'picture.mp4')
            n = blank_picture(self.picture, frame_size('h', self.S.get('res', 1080)), self.fps, self.total)
            json.dump([], open(os.path.join(self.work, 'frame-log.json'), 'w'))
            return {'segments': 0, 'rendered': 0, 'cache_hits': 0, 'frames': n, 'blank': True}
        segs, st = self.render(self.S['episode'], shots, 'h', self.total)
        self.picture = os.path.join(self.work, 'picture.mp4')
        self.concat(segs, self.picture)
        logs = []
        for g in segs:
            L = json.load(open(g['out'] + '.log.json'))
            t0 = next(s['t0'] for s in self.tl['shots'] if s['id'] == g['shot'])
            f0 = round(t0 * self.fps)
            logs += [{**x, 'f': x['f'] + f0, 't': round((x['f'] + f0) / self.fps, 3), 'shot': g['shot']} for x in L['logs']]
        json.dump(logs, open(os.path.join(self.work, 'frame-log.json'), 'w'))
        return st

    # ---- splice (F-5): world segments into the master picture; audio layers are merged in do_mix
    def do_splice(self):
        import splice as SPLICE   # world/splice.py
        segs, rec = [], {'episode': self.S['episode'], 'fps': self.fps, 'segments': []}
        for w in self.S['world']:
            t0, t1, f0, f1 = SPLICE.scene_span(self.tl, w['scenes'], self.fps)
            mp4 = self.world[w['id']]
            segs.append({'id': w['id'], 'mp4': mp4, 'f0': f0, 'f1': f1, 't0': t0, 't1': t1, 'scenes': list(w['scenes']),
                         'stems': os.path.join(mp4[:-4] + '.audio', 'stems')})
        pic = os.path.join(self.work, 'picture-spliced.mp4')
        r = SPLICE.splice_video(self.picture, segs, pic, self.fps, ENCODE_H)
        rec['picture'] = {'in': os.path.relpath(self.picture, ROOT), 'in_sha256': SPLICE.sha_file(self.picture),
                          'out': os.path.relpath(pic, ROOT), 'out_sha256': SPLICE.sha_file(pic), 'frames': r['frames'], 'encode': ENCODE_H}
        self.picture = pic
        cov = {}
        for g in segs:
            rec['segments'].append({'id': g['id'], 'scenes': g['scenes'], 't0': g['t0'], 't1': g['t1'], 'f0': g['f0'], 'f1': g['f1'],
                                    'frames': g['f1'] - g['f0'], 'video': os.path.relpath(g['mp4'], ROOT), 'video_sha256': SPLICE.sha_file(g['mp4']),
                                    'stems': {k: SPLICE.sha_file(p) for k, p in SPLICE.stem_files(g['stems']).items()}})
            cov.update({sc: g['id'] for sc in g['scenes']})
        for sc in self.tl['scenes']:
            if sc['id'] in cov:
                sc['world'] = cov[sc['id']]
        for s in self.tl['shots']:   # 2D shots of covered scenes are rendered (cache) but not in the master
            if s['scene'] in cov:
                s['world'] = cov[s['scene']]
        self.tl['world'] = [{k: g[k] for k in ('id', 'scenes', 't0', 't1', 'f0', 'f1')} for g in segs]
        json.dump(self.tl, open(os.path.join(self.out, 'timeline.json'), 'w'), indent=1, ensure_ascii=False)
        fl = os.path.join(self.work, 'frame-log.json')   # qc frame rules: only 2D frames that are still in the master
        logs = json.load(open(fl))
        keep = [x for x in logs if not any(g['f0'] <= x['f'] < g['f1'] for g in segs)]
        json.dump(keep, open(fl, 'w'))
        rec['frame_log_dropped'] = len(logs) - len(keep)
        self.splice_segs, self.splice_rec = segs, rec
        return {'segments': [g['id'] for g in segs], 'frames': r['frames'], 'frame_log_dropped': rec['frame_log_dropped']}

    # ---- mix + master
    def loudnorm(self, src, dst, lufs, tp):
        flt = f'loudnorm=I={lufs}:TP={tp}:LRA=11'
        r = subprocess.run(['ffmpeg', '-hide_banner', '-i', src, '-af', flt + ':print_format=json', '-f', 'null', '-'], capture_output=True, text=True)
        m = json.loads(r.stderr[r.stderr.rindex('{'):r.stderr.rindex('}') + 1])
        flt2 = (f"{flt}:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}"
                f":offset={m['target_offset']}:linear=true")
        sh(['ffmpeg', '-y', '-loglevel', 'error', '-i', src, '-af', flt2 + ',aresample=48000', '-ac', '2', '-c:a', 'pcm_s16le', dst])

    def do_mix(self):
        A = self.S.get('audio') or {}
        lufs, tp = A.get('lufs', -14), A.get('true_peak', -1.0)
        ins, flt = [], []
        for i, sc in enumerate(self.tl['scenes']):
            ins += ['-i', self.voices[sc['id']]['wav']]
            flt.append(f"[{i}:a]adelay={int(sc['start'] * 1000)}:all=1[v{i}]")
        n = len(self.tl['scenes'])
        flt.append(''.join(f'[v{i}]' for i in range(n)) + f'amix=inputs={n}:normalize=0,apad=whole_dur={self.total}[voice]')
        voice_raw = os.path.join(self.work, 'voice-raw.wav')
        sh(['ffmpeg', '-y', '-loglevel', 'error', *ins, '-filter_complex', ';'.join(flt), '-map', '[voice]', '-t', str(self.total),
            '-ar', '48000', '-ac', '2', '-c:a', 'pcm_s24le', voice_raw])
        raw, stems, info = os.path.join(self.work, 'mix-raw.wav'), os.path.join(self.work, 'stems'), {}
        os.makedirs(stems, exist_ok=True)
        for f in os.listdir(stems):
            os.remove(os.path.join(stems, f))
        if A.get('music'):  # bed under the voice at the Tập 1–3 level (music.py: 20 dB under voice, 1–4 kHz ducked 13 dB)
            bed = os.path.join(self.root, A['music'])
            if not os.path.exists(bed) and A.get('music_cmd'):
                sh(A['music_cmd'].format(total=self.total, out=bed), shell=True, cwd=ROOT)
            import music as MUSIC
            info = MUSIC.mix(voice_raw, bed, self.total, raw, stems)
        else:
            shutil.copy(voice_raw, raw)
            sh(['ffmpeg', '-y', '-loglevel', 'error', '-i', raw, os.path.join(stems, 'voice.flac')])
        if getattr(self, 'splice_segs', None):   # F-5: world segment layers into the stems; mix-raw = sum of the stems
            import splice as SPLICE
            info = {**info, 'world': SPLICE.merge_audio(stems, self.splice_segs, self.total, raw, self.fps)}
        self.master_wav = os.path.join(self.work, 'master.wav')
        self.loudnorm(raw, self.master_wav, lufs, tp)
        self.video = os.path.join(self.work, 'video.mp4')
        sh(['ffmpeg', '-y', '-loglevel', 'error', '-i', self.picture, '-i', self.master_wav, '-map', '0:v', '-map', '1:a', '-c:v', 'copy',
            '-c:a', 'aac', '-b:a', '384k', '-ar', '48000', '-ac', '2', '-movflags', '+faststart', '-shortest', self.video])
        self.report['music'] = info
        if getattr(self, 'splice_rec', None):
            import splice as SPLICE
            self.splice_rec['audio'] = {**info['world'], 'stems_sha256': {k: SPLICE.sha_file(p) for k, p in SPLICE.stem_files(stems).items()},
                                        'mix_raw_sha256': SPLICE.sha_file(raw), 'master_wav_sha256': SPLICE.sha_file(self.master_wav)}
            self.splice_rec['video'] = {'file': os.path.relpath(self.video, ROOT), 'sha256': SPLICE.sha_file(self.video)}
            json.dump(self.splice_rec, open(os.path.join(self.out, 'splice.json'), 'w'), indent=1, ensure_ascii=False)
        return {**info, 'video': os.path.relpath(self.video, ROOT), 'sha256': sha(open(self.video, 'rb').read()), 'mb': round(os.path.getsize(self.video) / 1e6, 2)}

    # ---- parts
    def do_parts(self):
        T, cuts = self.total, sorted({s['t0'] for s in self.tl['shots']} - {0.0})
        pick = []
        for target in (T / 3, 2 * T / 3):
            c = min(cuts, key=lambda x: abs(x - target)) if cuts else target
            if c not in pick and 0 < c < T:
                pick.append(c)
        bounds = [0.0] + sorted(pick) + [T]
        parts = []
        for i in range(len(bounds) - 1):
            p = os.path.join(self.work, f"{self.S['episode']}-part{i + 1}-720p.mp4")
            sh(['ffmpeg', '-y', '-loglevel', 'error', '-ss', str(bounds[i]), '-to', str(bounds[i + 1]), '-i', self.video, '-vf', 'scale=1280:720',
                '-c:v', 'libx264', '-preset', 'fast', '-b:v', '5M', '-maxrate', '6M', '-bufsize', '10M', '-c:a', 'aac', '-b:a', '192k', p])
            parts.append({'file': os.path.relpath(p, ROOT), 'from': bounds[i], 'to': bounds[i + 1], 'mb': round(os.path.getsize(p) / 1e6, 2)})
        self.parts = parts
        return {'parts': parts}

    # ---- artefacts (world): camera, data-sound events, checks page
    def do_artefacts(self):
        import artefacts as ART
        import episode_page as EPG
        by = {w['id']: w for w in self.S['world']}
        segs = [{'id': g['id'], 'mp4': g['mp4'], 't0': g['t0'], 'f0': g['f0'], 'f1': g['f1'],
                 'spine': json.load(open(os.path.join(self.root, by[g['id']]['dir'], 'spine.json')))} for g in self.splice_segs]
        out = os.path.join(self.root, 'out')
        rep = ART.write(out, self.total, self.fps, segs)
        rep['page'] = EPG.write_episode(self.root, self.S, self.tl, os.path.join(self.root, self.S['claims']), os.path.join(self.work, 'page', 'index.html'), self.fps)
        rep['page'].pop('json', None)
        return rep

    def world_short(self, S, a, b, g):
        """Short [a, b) inside world segment g (splice_segs entry): world/shorts.py."""
        import shorts as WS
        L = round(b - a, 4)
        w = next(x for x in self.S['world'] if x['id'] == g['id'])
        pic = os.path.join(self.work, f"{S['id']}-world.mp4")
        cws = [{'id': c['id'], 'text': c['text']} for c in self.counterweights]
        st = WS.render_world(os.path.join(self.root, w['dir']), a - g['t0'], b - g['t0'], pic, S.get('hook'), cws, self.workers,
                             cache=os.path.join(self.work, 'world-shorts-cache', g['id']), vs=float(S.get('scale', WS.VS_DEFAULT)))
        end = [{'id': S['id'] + '-end', 'template': 'endcard', 't0': 0.0, 't1': 1.5, 'p': {'next': S.get('end', ''), 'at': 0}}]
        segs, st2 = self.render(S['id'] + '-end', end, 'v', 1.5, hook=S.get('hook'), res=1080)
        endp = os.path.join(self.work, f"{S['id']}-end.mp4")
        self.concat(segs, endp)
        wav = os.path.join(self.work, f"{S['id']}.wav")
        au = WS.short_audio(self.master_wav, a, L, 1.5, wav)
        out = os.path.join(self.work, f"{S['id']}.mp4")
        WS.assemble(pic, endp, wav, out, self.fps)
        f0 = round(L * self.fps)
        endlogs = [{**x, 'f': x['f'] + f0} for gg in segs for x in json.load(open(gg['out'] + '.log.json'))['logs']]
        logs = WS.frame_logs(json.load(open(pic.replace('.mp4', '.log.json'))), a - g['t0'], self.fps, endlogs)
        json.dump(logs, open(os.path.join(self.work, f"{S['id']}-frame-log.json"), 'w'))
        return {'world': g['id'], 'render_world': {k: st.get(k) for k in ('wall_s', 'film_s', 'rendered', 'cached')}, 'endcard': st2, 'audio': au}

    # ---- shorts
    def do_shorts(self):
        res = []
        for S in self.S.get('shorts') or []:
            sc = next(s for s in self.S['scenes'] if any(x['id'] == SPEC.ANCHOR.match(S['from'])['sid'] for x in self.tl['sentences'] if x['scene'] == s['id']))
            off = next(x['start'] for x in self.tl['scenes'] if x['id'] == sc['id'])
            R = Resolver(self.voices[sc['id']], self.script)
            a = round(round((R.word_time(S['from']) + off) * self.fps) / self.fps, 4)
            b = round(round((R.word_time(S['to']) + off + 0.4) * self.fps) / self.fps, 4)
            L = round(b - a, 4)
            import shorts as WS
            g = WS.seg_for(getattr(self, 'splice_segs', None), a, b)
            if g:   # D-010: the span is a world segment → re-render it vertical from the segment's scene
                info = self.world_short(S, a, b, g)
                out = os.path.join(self.work, f"{S['id']}.mp4")
                res.append({'id': S['id'], 'file': os.path.relpath(out, ROOT), 'from': a, 'to': b, 'duration': round(probe_dur(out), 3), **info})
                continue
            shots = []  # a shot entered mid-way keeps its own clock (lead) and length (dur): same picture as the master at that moment
            for s in self.tl['shots']:
                if s['t1'] > a and s['t0'] < b:
                    shots.append({'id': s['id'] + '-v', 'template': s['template'], 't0': round(max(s['t0'], a) - a, 4), 't1': round(min(s['t1'], b) - a, 4),
                                  'lead': round(max(0.0, a - s['t0']), 4), 'dur': round(s['t1'] - s['t0'], 4), 'p': s['p']})
            shots.append({'id': S['id'] + '-end', 'template': 'endcard', 't0': L, 't1': round(L + 1.5, 4), 'p': {'next': S.get('end', ''), 'at': 0}})
            segs, st = self.render(S['id'], shots, 'v', L + 1.5, hook=S.get('hook'), res=1080)   # Shorts are 1080×1920 (SH01) whatever `res`
            pic = os.path.join(self.work, f"{S['id']}-picture.mp4")
            self.concat(segs, pic)
            out = os.path.join(self.work, f"{S['id']}.mp4")
            wav = os.path.join(self.work, f"{S['id']}.wav")
            WS.short_audio(self.master_wav, a, L, 1.5, wav)   # −14 LUFS / −1.5 dBTP per Short (SH03, SH04)
            sh(['ffmpeg', '-y', '-loglevel', 'error', '-i', pic, '-i', wav, '-map', '0:v', '-map', '1:a',
                '-c:v', 'copy', '-c:a', 'aac', '-b:a', '320k', '-ar', '48000', '-ac', '2', '-t', str(L + 1.5), out])
            logs = []
            for g in segs:
                t0 = next(s['t0'] for s in shots if s['id'] == g['shot'])
                logs += [{**x, 'f': x['f'] + round(t0 * self.fps), 'shot': g['shot']} for x in json.load(open(g['out'] + '.log.json'))['logs']]
            json.dump(logs, open(os.path.join(self.work, f"{S['id']}-frame-log.json"), 'w'))
            res.append({'id': S['id'], 'file': os.path.relpath(out, ROOT), 'from': a, 'to': b, 'duration': round(probe_dur(out), 3), **st})
        self.shorts = res
        return {'shorts': res}


def main():
    argv = sys.argv[1:]
    B = Build(argv[0], argv)
    t = time.time()
    B.step('spec', B.do_spec)
    B.load_inputs()
    B.step('voice', B.do_voice)
    B.step('resolve', B.do_resolve)
    if B.S.get('world'):
        B.step('world', B.do_world)
    B.step('render', B.do_render)
    if B.S.get('world'):
        B.step('splice', B.do_splice)   # F-5: đoạn thế giới vào master (hình); tiếng ghép trong mix
    B.step('mix', B.do_mix)
    if B.S.get('world'):
        B.step('artefacts', B.do_artefacts)   # out/camera.json, out/sonify-events.json, out/page.json (+ work/factory/page/index.html)
    B.step('parts', B.do_parts)
    B.step('shorts', B.do_shorts)
    import qc as QC
    B.step('qc', lambda: QC.run(B))
    B.report['total_seconds'] = round(time.time() - t, 2)
    json.dump(B.report, open(os.path.join(B.out, 'build-report.json'), 'w'), indent=1, ensure_ascii=False)
    print(f"build: {B.report['total_seconds']} s → {os.path.relpath(B.out, ROOT)}")


if __name__ == '__main__':
    main()
