"""C5 Tập 2 · luồng A: out/voice/takes.json (checks/CONTRACT.md: {takes:[{id, raw, final, model?, voiceId?, provider?}], voice}).

    python3 episodes/ep002/audio_src/takes.py [--checks <copy of origin/main checks>/py]

Lời cuối = các take C2 (review-c2/takes, review-c2/table-read.json `use`): Eric (cjVigY5qzO86Huf0OWal), eleven_v3, mặc định, seed 1, MỖI CẢNH MỘT
LẦN GỌI, thẻ cảm xúc thưa của kịch bản (G-015 · chọn). Mỗi take được kiểm:
  (1) chữ gửi TTS (meta .json của take) == chữ cảnh dựng lại từ story/script.md v5 bằng chính story/table_read.py (rows + scene_text); ghi SHA-1/SHA-256;
  (2) giọng/mô hình/thiết lập: voice, model, voice_settings=None, speed=None (không thẻ ngắt: kịch bản không có);
  (3) ASR (faster-whisper small.en, chữ ASR đã lưu ở table-read.json) so từ khoá bằng key_words/match_keys của BẢN SAO checks (origin/main, khoá K3.6).
Sinh lại chỉ khi từ khoá thiếu VÌ GIỌNG (xem `regen` trong kết quả: quyết định và lý do ghi vào takes.json; số ký tự EL mỗi lần gọi ghi ở `elChars`).
raw = file TTS như trả về; final = cùng file (ghép chỉ có gain, không giãn; S10: 2,0 s lặng chèn sau S10.1 theo timing.json `inserted`, không giãn).
"""
import hashlib
import importlib.util
import json
import os
import sys

EP = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ARGS = sys.argv[1:]
CK = ARGS[ARGS.index('--checks') + 1] if '--checks' in ARGS else os.path.join(EP, '..', '..', 'checks', 'py')

# Quyết định sinh lại (đọc ASR trước khi gọi API; không gọi khi thiếu từ khoá không do giọng)
REGEN = {
    'S09': {'decision': 'keep seed 1 (no regeneration)',
            'why': 'ASR heard both years: "of the 1954 -1980 starts" (x2); the locked number parser reads the hyphen as a minus sign (num:-1980), so '
                   '"1980" counts as missing although the voice says "nineteen eighty". Seed 2 (C2) gave the identical ASR text; a seed-3 take of the same '
                   'text would not change the hyphenated form ("nineteen fifty-four-to-nineteen eighty", from the script\'s "1954-to-1980") and would move '
                   'S09 under the rendered picture. Cause = text form, not voice: listed for P-ep002 (C5 plan: A14 "1954-to-1980").'},
}


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main():
    sys.argv = [sys.argv[0]]
    tr = load('table_read', os.path.join(EP, 'story', 'table_read.py'))
    sys.path.insert(0, CK)
    for k in [k for k in sys.modules if k.startswith('r_')]:
        del sys.modules[k]
    import r_audio
    rs = tr.rows()
    keys = r_audio.key_words([{'text': r['text']} for r in rs])
    res = json.load(open(os.path.join(EP, 'review-c2', 'table-read.json')))
    tm = json.load(open(os.environ.get('EP2_TIMING') or os.path.join(EP, 'animatic', 'timing.json')))
    at = {s['id']: s for s in tm['scenes']}
    script_sha = hashlib.sha256(open(os.path.join(EP, 'story', 'script.md'), 'rb').read()).hexdigest()
    takes, models, voices, problems = [], set(), set(), []
    for sc in sorted({r['scene'] for r in rs}):
        text = tr.scene_text([r for r in rs if r['scene'] == sc])
        e = res['scenes'][sc]
        use = e['use']
        meta = json.load(open(os.path.join(EP, 'review-c2', 'takes', use[:-4] + '.json')))
        ok_text = meta['text'] == text == e['text']
        ok_set = meta['model'] == tr.MODEL and meta['voice'] == tr.VOICE and meta.get('voice_settings') is None and meta.get('speed') is None
        tk = next(t for t in e['takes'] if t['file'] == use)
        K = [k for r, kk in zip(rs, keys) if r['scene'] == sc for k in kk]
        miss = r_audio.match_keys(K, [{'w': w} for w in tk['asr'].split()])
        if not ok_text or not ok_set:
            problems.append(sc)
        models.add(meta['model'])
        voices.add(meta['voice'])
        rel = f'review-c2/takes/{use}'
        s = at[sc]
        row = {'id': sc, 'raw': rel, 'final': rel, 'model': meta['model'], 'voiceId': meta['voice'], 'provider': 'elevenlabs', 'seed': meta['seed'],
               'voiceSettings': meta.get('voice_settings'), 'speed': meta.get('speed'),
               'textSha1': hashlib.sha1(text.encode()).hexdigest(), 'textMatchesScriptV5': ok_text, 'tags': [r['tag'] for r in rs if r['scene'] == sc and r['tag']],
               'sentences': [r['id'] for r in rs if r['scene'] == sc], 'startInNarration': s['start'], 'audioS': s['audio_s'],
               'inserted': s.get('inserted') or [],
               'source': ('C5 regeneration (script change: ' + e['regenerated'] + '), same voice, model, settings') if e.get('regenerated') else
                         'C2 take reused (same voice, model, settings, v5 text)',
               'asr': {'keyWords': len(K), 'missing': miss, 'by': 'faster-whisper small.en (review-c2/table-read.json), match_keys of checks origin/main K3.6'},
               'elChars': {'C5': sum(t['characterCost'] for t in e['takes']) if e.get('regenerated') else 0,
                           'calls': [{'file': t['file'], 'seed': t['seed'], 'characterCost': t['characterCost'], 'len': t['len'],
                                      'when': 'C5' if e.get('regenerated') else 'C2'} for t in e['takes']]}}
        if miss:
            row['regen'] = REGEN.get(sc, {'decision': 'REGENERATE NEEDED', 'why': 'key words missing'})
        takes.append(row)
        print(sc, use, 'text', ok_text, 'settings', ok_set, 'missing', miss)
    assert not problems, problems
    assert len(models) == 1 and len(voices) == 1, (models, voices)
    c5 = sum(t['elChars']['C5'] for t in takes)
    regen = [t['id'] for t in takes if t['elChars']['C5']]
    out = {'_about': 'Narration of Tập 2 C5 (script v5): one eleven_v3 take per scene, Eric, default settings (no voice_settings, no speed, no break tags), '
                     'sparse emotion tags as written in the script. Every take text verified identical to the current script; C2 table-read takes reused '
                     f'(same voice/model/settings) except {regen or "none"}, regenerated in C5 after a script change (EL characters used in C5: {c5}). raw = final: the voice track '
                     '(audio_src/mix.py) places each take at its scene start of animatic/timing.json with gain only, no stretch; the only edit is the 2.0 s '
                     'silence timing.json inserts after S10.1 (owner C4 Q3a). Generated by audio_src/takes.py.',
           'script': {'path': 'story/script.md', 'sha256': script_sha, 'version': 'v5'},
           'takes': takes,
           'elCharsC5': c5, 'regeneratedC5': regen, 'elCharsC2Total': res.get('chars'),
           'voice': {'provider': 'elevenlabs', 'voiceId': voices.pop(), 'model': models.pop(), 'name': 'Eric (premade)',
                     'settings': 'default (no voice_settings, no speed)', 'endpoint': 'text-to-speech/{voice}/stream/with-timestamps, mp3_44100_128'}}
    os.makedirs(os.path.join(EP, 'out', 'voice'), exist_ok=True)
    json.dump(out, open(os.path.join(EP, 'out', 'voice', 'takes.json'), 'w'), indent=1, ensure_ascii=False)
    print(len(takes), 'takes ->', 'out/voice/takes.json')


if __name__ == '__main__':
    main()
