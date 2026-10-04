"""Episode 2 (C5, stream D): rights ledger out/rights.json and visual-asset manifest out/visual-assets.json (checks K3.1, rule F12;
RIGHTS.md at the repo root, rows for Tập 2 drafted in RIGHTS-ep002.md).

    python3 episodes/ep002/preprod/rights_c5.py

Quotes are copied from files, never typed: Inter OFL 1.1 from toolkit/render/fonts/LICENSE-Inter-OFL-1.1.txt; ElevenLabs terms from the verbatim
capture of Episode 1 (episodes/ep001/work/c5/elevenlabs-terms.json, same account, same voice, same model, paid Creator plan confirmed by the
owner 2026-09-30); FRED terms from data/sources.json; federal rules from data/context.json. The render page of Episode 2 is canvas 2D only (no
three.js, no image, no texture): the only visual asset it loads is the Inter font. The audio generator path is stream A's code (audio_src/):
F12 fails honestly while a named generator does not exist.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.normpath(os.path.join(HERE, '..'))
REPO = os.path.normpath(os.path.join(EP, '..', '..'))
EL = json.load(open(os.path.join(REPO, 'episodes', 'ep001', 'work', 'c5', 'elevenlabs-terms.json'), encoding='utf-8'))
PAID_PLAN_CONFIRMED = True  # chủ dự án xác nhận 30/09/2026: gói trả phí Creator (RIGHTS.md V-ERIC)
# stream A (C5): mix / music / sonification code. The first existing path wins; none = the planned path (F12 then names it missing).
AUDIO_GEN = next((p for p in ('audio_src/mix.py', 'work/audio/src/mix.py', 'audio_src/events.py') if os.path.exists(os.path.join(EP, p))), 'audio_src/mix.py')
SON_GEN = 'audio_src/events.py' if os.path.exists(os.path.join(EP, 'audio_src/events.py')) else AUDIO_GEN


def para(text, start):
    i = text.index(start)
    j = text.find('\n\n', i)
    return re.sub(r'\s*\n\s*', ' ', text[i:j if j > 0 else None]).strip()


def main():
    ofl = open(os.path.join(REPO, 'toolkit', 'render', 'fonts', 'LICENSE-Inter-OFL-1.1.txt'), encoding='utf-8').read()
    inter_copy = ofl.split('\n')[0].split(' Inter-Italic')[0].strip()
    inter_quote = inter_copy + ' — ' + para(ofl, 'This Font Software is licensed') + ' … ' + para(ofl, 'Permission is hereby granted') + \
        ' … ' + para(ofl, '1) Neither the Font Software') + ' … ' + para(ofl, '2) Original or Modified Versions')
    src = json.load(open(os.path.join(EP, 'data', 'sources.json'), encoding='utf-8'))['files']
    tb3 = next(f for f in src if f['series'] == 'TB3MS')
    dtb3 = next(f for f in src if f['series'] == 'DTB3')
    ctx = {c['claimId']: c for c in json.load(open(os.path.join(EP, 'data', 'context.json'), encoding='utf-8'))['claims']}
    takes = json.load(open(os.path.join(EP, 'out', 'voice', 'takes.json'), encoding='utf-8')) if os.path.exists(os.path.join(EP, 'out', 'voice', 'takes.json')) else {}
    voice = takes.get('voice') or {}
    assets = [
        {'name': 'Voice "Eric" (ElevenLabs)', 'kind': 'voice', 'stems': ['voice'], 'visuals': [],
         'origin': f'ElevenLabs text-to-speech, premade voice "Eric" (voice_id {voice.get("voiceId", "cjVigY5qzO86Huf0OWal")}), model {voice.get("model", "eleven_v3")}, '
                   'paid plan (Creator, owner-confirmed 2026-09-30); takes: out/voice/takes.json (stream A)',
         'licence': 'ElevenLabs Terms of Service (Last Updated 31 March 2026), commercial use for Paid Users (§(c)(ii)); verbatim quotes in '
                    'episodes/ep001/work/c5/elevenlabs-terms.json (same account and plan as Episode 1)',
         'thirdParty': True, 'terms': {'quote': EL['terms']['quotes'][0] + ' — ' + EL['terms']['quotes'][1] + ' — Billing: ' + EL['billing']['quotes'][0],
                                          'url': EL['terms']['url'], 'version': EL['terms']['version'], 'urls': [EL['terms']['url'], EL['billing']['url']]},
         'commercial': True if PAID_PLAN_CONFIRMED else None, 'rightsRow': 'V-ERIC'},
        {'name': 'Music, sound design and room tone (generated)', 'kind': 'music', 'stems': ['music', 'sfx', 'whoosh', 'room'], 'visuals': [],
         'origin': 'synthesised in code for this episode by stream A (numpy; music C, G-016; no samples, no loops, no third-party audio)',
         'licence': 'own work of the project', 'thirdParty': False, 'generator': AUDIO_GEN, 'rightsRow': 'A-MUSIC-2'},
        {'name': 'Data sonification (generated, palette S2)', 'kind': 'sonification', 'stems': ['sonify'], 'visuals': [],
         'origin': 'synthesised in code from the picture\'s data events (out/sonify-events.json, audio_src/events.py; palette S2 as Tập 1, G-005)',
         'licence': 'own work of the project', 'thirdParty': False, 'generator': SON_GEN, 'rightsRow': 'A-MUSIC-2'},
        {'name': 'Inter', 'kind': 'font', 'stems': [], 'visuals': ['Inter'],
         'origin': 'Inter 400/600/700 latin woff2 (toolkit/render/fonts/, = npm @fontsource/inter 5.3.0, byte-identical); the render page '
                   '(animatic/src/page.html) loads them with @font-face from /fonts/',
         'licence': 'SIL Open Font License 1.1', 'thirdParty': True, 'commercial': True,
         'terms': {'quote': inter_quote, 'url': 'https://unpkg.com/@fontsource/inter@5.3.0/LICENSE'},
         'source': {'url': 'https://www.npmjs.com/package/@fontsource/inter/v/5.3.0', 'repo': 'https://github.com/rsms/inter'},
         'licenceFile': 'toolkit/render/fonts/LICENSE-Inter-OFL-1.1.txt', 'rightsRow': 'F-INTER'},
        {'name': 'TB3MS (3-month Treasury bill, Board of Governors H.15 via FRED)', 'kind': 'data', 'stems': [], 'visuals': [],
         'origin': f'{tb3["what"]}; downloaded {tb3["downloaded"]} (data/sources.json, sha256 {tb3["sha256"][:12]}…); drawn by project code (the ridge, every replay)',
         'licence': 'public domain, citation requested (FRED series page)', 'thirdParty': True, 'publicDomain': True,
         'source': {'url': tb3['seriesPage']},
         'pdBasis': f'FRED series page notes for TB3MS: "{tb3["terms"]["quote"]}" — {tb3["terms"]["url"]} (Board of Governors of the Federal Reserve System, H.15)',
         'attribution': 'Source: Board of Governors of the Federal Reserve System (US), 3-Month Treasury Bill Secondary Market Rate, via FRED, Federal Reserve Bank of St. Louis',
         'rightsRow': 'D-FRED-TB3MS'},
        {'name': 'DTB3 (daily 3-month Treasury bill, cross-check only)', 'kind': 'data', 'stems': [], 'visuals': [],
         'origin': f'{dtb3["what"]}; downloaded {dtb3["downloaded"]}; not shown, cross-check of TB3MS only (S04)',
         'licence': 'public domain, citation requested (FRED series page)', 'thirdParty': True, 'publicDomain': True,
         'source': {'url': dtb3['seriesPage']}, 'pdBasis': f'FRED series page notes for DTB3: "{dtb3["terms"]["quote"]}" — {dtb3["terms"]["url"]}',
         'rightsRow': 'D-FRED-DTB3'},
        {'name': 'Federal student loan rules (eCFR 34 CFR 685, Federal Register 2026-01912, FSA)', 'kind': 'data', 'stems': [], 'visuals': [],
         'origin': 'policy facts shown as text in S01-S02 and the description (data/context.json: ' + ', '.join(sorted(ctx)) + '); no document image is shown',
         'licence': 'public domain (US federal government works)', 'thirdParty': True, 'publicDomain': True,
         'source': {'url': ctx['ctx_plus_end']['source']['url'], 'urls': sorted({c['source']['url'] for c in ctx.values()})},
         'pdBasis': '17 U.S.C. §105: copyright protection is not available for any work of the United States Government (eCFR, Federal Register, '
                    'Federal Student Aid are federal publications); facts are quoted with their citation',
         'rightsRow': 'D-POLICY-2'},
    ]
    json.dump({'about': 'Rights ledger of Episode 2 (checks/CONTRACT.md out/rights.json, K3.1). One entry per sounding stem group and per visual asset '
                        '(out/visual-assets.json + contract.json rights.visual), plus data used on screen. Generated by preprod/rights_c5.py; RIGHTS.md is the '
                        'human ledger (Tập 2 rows: RIGHTS-ep002.md).',
               'assets': assets}, open(os.path.join(EP, 'out', 'rights.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    manifest = {
        'about': 'Visual assets of the Episode 2 build (K3.1): every picture file and font the render page loads. The page (animatic/src/page.html + '
                 'design/c3/final/src engines) draws everything in canvas 2D from project code and data; it loads no image, PDF, 3D model or texture '
                 'file (no three.js in this episode). Fonts are matched by family (document.fonts).',
        'assets': [{'name': 'Inter', 'kind': 'font', 'family': 'Inter',
                    'paths': ['fonts/inter-latin-400-normal.woff2', 'fonts/inter-latin-600-normal.woff2', 'fonts/inter-latin-700-normal.woff2',
                              '../../toolkit/render/fonts/inter-latin-*-normal.woff2']}],
        'generated': [],
        'note': 'thumbnails (C6) are added here with their generator when they exist',
    }
    json.dump(manifest, open(os.path.join(EP, 'out', 'visual-assets.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print('rights.json:', len(assets), 'assets; audio generator', AUDIO_GEN, os.path.exists(os.path.join(EP, AUDIO_GEN)), '; sonify', SON_GEN)


if __name__ == '__main__':
    main()
