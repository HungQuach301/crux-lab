"""Episode 1 (C5, stream D): rights ledger out/rights.json and visual-asset manifest out/visual-assets.json (checks K3.1, rule F12;
RIGHTS.md at the repo root; playbook/quality-framework.md §8).

    python3 episodes/ep001/preprod/rights_c5.py

Quotes are copied from files, never typed: Inter OFL 1.1 from toolkit/render/fonts/LICENSE-Inter-OFL-1.1.txt (the LICENSE of the npm
package @fontsource/inter 5.3.0, whose three latin woff2 files are byte-identical to toolkit/render/fonts/*.woff2), three.js MIT from the
installed package, FRED from data/sources.json, CFPB (HMDA) from data/hmda-sources.json. The ElevenLabs terms could not be fetched
(elevenlabs.io blocked by the session proxy): the entry carries "PENDING-OWNER-PASTE" and commercial = null, so F12 fails honestly until
the owner pastes the verbatim sentence and its URL and sets commercial = true.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.normpath(os.path.join(HERE, '..'))
REPO = os.path.normpath(os.path.join(EP, '..', '..'))
PENDING = 'PENDING-OWNER-PASTE'
AUDIO_GEN = 'work/audio/src/mix.py'   # stream A's mix/music/sonification code (C5); resolved from the episode root


def para(text, start):
    """The paragraph of `text` that starts with `start`, joined into one line (verbatim words, line breaks -> spaces)."""
    i = text.index(start)
    j = text.find('\n\n', i)
    return re.sub(r'\s*\n\s*', ' ', text[i:j if j > 0 else None]).strip()


def main():
    ofl = open(os.path.join(REPO, 'toolkit', 'render', 'fonts', 'LICENSE-Inter-OFL-1.1.txt'), encoding='utf-8').read()
    inter_copy = ofl.split('\n')[0].split(' Inter-Italic')[0].strip()           # "Copyright 2016 The Inter Project Authors (https://github.com/rsms/inter)"
    inter_quote = inter_copy + ' — ' + para(ofl, 'This Font Software is licensed') + ' … ' + para(ofl, 'Permission is hereby granted') + \
        ' … ' + para(ofl, '1) Neither the Font Software') + ' … ' + para(ofl, '2) Original or Modified Versions')
    three_dir = os.environ.get('THREE_DIR')
    mit = None
    for d in ([os.path.dirname(three_dir)] if three_dir else []) + [os.path.join(REPO, 'node_modules', 'three')]:
        p = os.path.join(d, 'LICENSE')
        if os.path.exists(p):
            mit = open(p, encoding='utf-8').read()
    three_quote = (para(mit, 'Copyright') + ' — ' + para(mit, 'Permission is hereby granted')) if mit else \
        'Copyright © 2010-2026 three.js authors — Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:'
    fred = json.load(open(os.path.join(EP, 'data', 'sources.json')))['files']
    fred_terms = next((f.get('terms') for f in fred if f.get('series') == 'MORTGAGE30US'), None) or {}
    hmda = json.load(open(os.path.join(EP, 'data', 'hmda-sources.json')))['terms']

    assets = [
        {'name': 'Voice "Eric" (ElevenLabs)', 'kind': 'voice', 'stems': ['voice'], 'visuals': [],
         'origin': 'ElevenLabs text-to-speech, premade voice "Eric" (voice_id cjVigY5qzO86Huf0OWal), model eleven_v3, paid plan; takes: out/voice/takes.json',
         'licence': 'ElevenLabs Terms of Service, commercial licence of paid plans (verbatim quote pending: elevenlabs.io is blocked by the session proxy)',
         'thirdParty': True, 'terms': {'quote': PENDING, 'url': PENDING}, 'commercial': None,
         'pending': 'owner pastes the verbatim sentence granting commercial use (Terms of Use / billing page) and its URL, then sets commercial = true (RIGHTS.md V-ERIC)',
         'rightsRow': 'V-ERIC'},
        {'name': 'Music, sound design and room tone (generated)', 'kind': 'music', 'stems': ['music', 'sfx', 'whoosh', 'room'], 'visuals': [],
         'origin': 'synthesised in code for this episode (numpy; no samples, no loops, no third-party audio)', 'licence': 'own work of the project',
         'thirdParty': False, 'generator': AUDIO_GEN, 'rightsRow': 'A-MUSIC'},
        {'name': 'Data sonification (generated, palette S2)', 'kind': 'sonification', 'stems': ['sonify'], 'visuals': [],
         'origin': 'synthesised in code from the page\'s data events (work/audio/son-plan.json, out/sonify-events.json)', 'licence': 'own work of the project',
         'thirdParty': False, 'generator': AUDIO_GEN, 'rightsRow': 'A-MUSIC'},
        {'name': 'Inter', 'kind': 'font', 'stems': [], 'visuals': ['Inter'],
         'origin': 'Inter 400/600/700 latin woff2 (toolkit/render/fonts/), from the npm package @fontsource/inter 5.3.0 (byte-identical files); the render page loads them with @font-face',
         'licence': 'SIL Open Font License 1.1', 'thirdParty': True, 'commercial': True,
         'terms': {'quote': inter_quote, 'url': 'https://unpkg.com/@fontsource/inter@5.3.0/LICENSE'},
         'source': {'url': 'https://www.npmjs.com/package/@fontsource/inter/v/5.3.0', 'repo': 'https://github.com/rsms/inter'},
         'licenceFile': 'toolkit/render/fonts/LICENSE-Inter-OFL-1.1.txt', 'rightsRow': 'F-INTER'},
        {'name': 'three.js', 'kind': 'code', 'stems': [], 'visuals': [],
         'origin': 'three.js 0.186.1 (npm "three"), the WebGL library of the render page (H1 scenes); code, not a picture: every 3D object and texture is built by project code',
         'licence': 'MIT', 'thirdParty': True, 'commercial': True, 'terms': {'quote': three_quote, 'url': 'https://unpkg.com/three@0.186.1/LICENSE'},
         'source': {'url': 'https://www.npmjs.com/package/three/v/0.186.1'}},
        {'name': 'MORTGAGE30US (Freddie Mac PMMS via FRED)', 'kind': 'data', 'stems': [], 'visuals': [],
         'origin': 'weekly 30-year fixed rate, Freddie Mac Primary Mortgage Market Survey, downloaded from FRED (data/sources.json); drawn by project code',
         'licence': 'FRED terms of use: citation required; attribution "Source: Freddie Mac via FRED"', 'thirdParty': True, 'commercial': True,
         'terms': {'quote': 'you may use these data series with proper attribution of the source and acknowledgment that you obtained the data from FRED',
                   'url': 'https://fred.stlouisfed.org/legal/'},
         'seriesNotes': {'quote': (fred_terms.get('quote') or '')[:400], 'url': fred_terms.get('url')},
         'attribution': 'Source: Freddie Mac via FRED', 'rightsRow': 'D-FRED-1'},
        {'name': 'HMDA 2018-2025 (CFPB)', 'kind': 'data', 'stems': [], 'visuals': [],
         'origin': 'Home Mortgage Disclosure Act loan-level data, ffiec.cfpb.gov (data/hmda-sources.json); medians computed by project code',
         'licence': 'public domain (US federal government work)', 'thirdParty': True, 'publicDomain': True,
         'source': {'url': 'https://ffiec.cfpb.gov/data-browser/'},
         'pdBasis': hmda['quote'] + ' — ' + hmda['url'] + ' (17 U.S.C. §105: works of the US government are not subject to copyright)',
         'attribution': 'Source: CFPB HMDA', 'rightsRow': 'D-HMDA'},
    ]
    json.dump({'about': 'Rights ledger of Episode 1 (checks/CONTRACT.md out/rights.json, K3.1). One entry per sounding stem group and per visual asset '
                        '(out/visual-assets.json), plus code and data used on screen. Generated by preprod/rights_c5.py; RIGHTS.md is the human ledger.',
               'assets': assets}, open(os.path.join(EP, 'out', 'rights.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    manifest = {
        'about': 'Visual assets of the build (K3.1): every picture file and font the render page loads. The page draws everything else in code '
                 '(canvas 2D, three.js geometry, CanvasTexture from project code); it loads no image, PDF, 3D model or texture file. '
                 'Fonts are matched by family (document.fonts).',
        'assets': [{'name': 'Inter', 'kind': 'font', 'family': 'Inter', 'paths': ['../../toolkit/render/fonts/inter-latin-400-normal.woff2',
                                                                             '../../toolkit/render/fonts/inter-latin-600-normal.woff2',
                                                                             '../../toolkit/render/fonts/inter-latin-700-normal.woff2']}],
        'generated': [{'glob': 'out/package/thumb-*.png', 'generator': 'preprod/thumbs_c5.js'}],
    }
    json.dump(manifest, open(os.path.join(EP, 'out', 'visual-assets.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print('rights.json:', len(assets), 'assets; visual-assets.json:', len(manifest['assets']), 'visuals; Inter quote', len(inter_quote), 'chars')


if __name__ == '__main__':
    main()
