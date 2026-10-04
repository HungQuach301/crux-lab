"""topics-r2 control topic cards: OpenAI gpt-5.5, reasoning medium, no tools, no data (topics-r2/DESIGN.md).

Adapted from topics-r2/control/gen_control.py for the five-field card (cardcheck v2). One call per pillar; wall-clock ceiling 10 minutes per call (SIGALRM). Cards that fail the template check are dropped
and the same prompt is called again (at most 3 calls per pillar in total); passing cards are kept in order until the
pillar has its quota. Nobody edits words; only cardcheck.normalize() punctuation.

Resumable: a pillar with topics-r2/control/out/<pillar>.json is skipped. Network errors retry 2/4/8/16 s.
Raw request + response of every call are saved verbatim in topics-r2/control/raw/.
Usage: python3 topics-r2/control/gen_control.py
"""
import json, os, re, signal, sys, time
import requests

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'tools'))
import cardcheck  # noqa: E402

MODEL = 'gpt-5.5'
CALL_SECONDS = 600
MAX_CALLS = 3
PILLARS = [('debt', 2), ('retire', 2), ('tax', 2)]
BRIEF_MD = open(os.path.join(HERE, '..', 'BRIEF.md')).read()
BRIEF = re.search(r'```BRIEF\n(.*?)\n```', BRIEF_MD, re.S).group(1)
EXCLUDE = re.search(r'```EXCLUDE\n(.*?)\n```', BRIEF_MD, re.S).group(1)
PILLAR_TEXT = dict(re.findall(r'- `(\w+)` → "([^"]+)"', BRIEF_MD))
ROLE = ('You are a well-read American who follows US personal-finance news. You have about ten minutes to think. '
        'Do not look anything up; use only what you already know.')
SCHEMA = {'type': 'object', 'additionalProperties': False, 'required': ['cards'], 'properties': {'cards': {
    'type': 'array', 'items': {'type': 'object', 'additionalProperties': False, 'required': list(cardcheck.FIELDS),
                               'properties': {f: {'type': 'string'} for f in cardcheck.FIELDS}}}}}


class Timeout(Exception):
    pass


def _alarm(signum, frame):
    raise Timeout()


def call(body):
    for i, wait in enumerate([2, 4, 8, 16, None]):
        signal.signal(signal.SIGALRM, _alarm)
        signal.alarm(CALL_SECONDS)
        t0 = time.time()
        try:
            r = requests.post('https://api.openai.com/v1/responses', json=body, timeout=(30, CALL_SECONDS))
            signal.alarm(0)
            if r.status_code >= 500 or r.status_code == 429:
                raise requests.ConnectionError(f'HTTP {r.status_code}')
            return r, time.time() - t0
        except Timeout:
            print(f'  call exceeded {CALL_SECONDS}s wall clock', flush=True)
            return None, time.time() - t0
        except (requests.ConnectionError, requests.Timeout) as e:
            signal.alarm(0)
            if wait is None:
                raise
            print(f'  network error ({e}); retry in {wait}s', flush=True)
            time.sleep(wait)


def main():
    os.makedirs(os.path.join(HERE, 'raw'), exist_ok=True)
    os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
    for pillar, n in PILLARS:
        out = os.path.join(HERE, 'out', f'{pillar}.json')
        if os.path.exists(out):
            print(f'[{pillar}] done, skip', flush=True)
            continue
        prompt = BRIEF.replace('{pillar}', PILLAR_TEXT[pillar]).replace('{n}', str(n)) + '\n\n' + EXCLUDE
        kept, attempts = [], []
        for k in range(1, MAX_CALLS + 1):
            if len(kept) >= n:
                break
            body = {'model': MODEL, 'instructions': ROLE, 'input': prompt, 'reasoning': {'effort': 'medium'},
                    'max_output_tokens': 6000, 'tools': [], 'store': False,
                    'text': {'format': {'type': 'json_schema', 'name': 'cards', 'schema': SCHEMA, 'strict': True}}}
            print(f'[{pillar}] call {k}/{MAX_CALLS} ...', flush=True)
            r, secs = call(body)
            rawp = os.path.join(HERE, 'raw', f'{pillar}-call{k}.json')
            rec = {'request': body, 'seconds': round(secs, 1), 'status': None if r is None else r.status_code,
                   'response': None if r is None else r.json(), 'timedOut': r is None}
            json.dump(rec, open(rawp, 'w'), indent=1, ensure_ascii=False)
            att = {'call': k, 'raw': os.path.relpath(rawp, HERE), 'seconds': rec['seconds'], 'cards': []}
            if r is not None and r.status_code == 200:
                resp = r.json()
                text = ''.join(c.get('text', '') for o in resp.get('output', []) if o.get('type') == 'message'
                               for c in o.get('content', []) if c.get('type') == 'output_text')
                att['model'] = resp.get('model')
                att['usage'] = resp.get('usage')
                att['status'] = resp.get('status')
                try:
                    cards = json.loads(text)['cards']
                except Exception as e:
                    cards = []
                    att['parseError'] = str(e)
                for c in cards:
                    norm = cardcheck.normalize_card(c)
                    viol = cardcheck.check(norm)
                    dup = any(norm['decision'] == x['card']['decision'] for x in kept)
                    ok = not viol and not dup and len(kept) < n
                    att['cards'].append({'original': c, 'normalized': norm, 'violations': viol, 'duplicate': dup,
                                         'kept': ok})
                    if ok:
                        kept.append({'card': norm, 'call': k})
            else:
                att['error'] = 'timeout' if r is None else r.text[:500]
            attempts.append(att)
            print(f'[{pillar}] call {k}: {sum(c["kept"] for c in att["cards"])} kept, total {len(kept)}/{n}, '
                  f'{att["seconds"]}s', flush=True)
        json.dump({'pillar': pillar, 'quota': n, 'model': MODEL, 'role': ROLE, 'prompt': prompt,
                   'kept': kept, 'attempts': attempts, 'complete': len(kept) >= n},
                  open(out, 'w'), indent=1, ensure_ascii=False)
        print(f'[{pillar}] wrote {out} ({len(kept)}/{n})', flush=True)


if __name__ == '__main__':
    main()
