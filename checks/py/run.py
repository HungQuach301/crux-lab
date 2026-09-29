"""Run every machine rule (genre-spec/data-explainer.md [MÁY]) on a project root and write <root>/out/checks/report.json and report.md.

    python3 checks/py/run.py <root> [--contract <episode contract.json>] [--only F01,A01] [--list] [--baseline <previous report.json> | --first]

The episode contract defaults to <root>/contract.json (checks/CONTRACT.md §Episode contract).

REG (regression gate): every rule that PASSed in the checker's report of the previous version of the episode (--baseline, a
report the checking session keeps outside the builder's tree) and is comparable (same definition) must still PASS. --first
declares the first version (nothing to compare). Neither given: REG is MISSING.

Status: PASS | FAIL | MISSING (a contract artifact is absent: counts as not passed) | ERROR (rule crashed: counts as not passed).
`near` lists every metric within 5% of its threshold (brief §0: report metrics that only just meet a threshold)."""
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(__file__))
import common  # noqa: E402
import r_file, r_audio, r_content, r_rhythm, r_visual, r_page, r_sound  # noqa: E402,F401

ORDER = ['F', 'A', 'S', 'R', 'V', 'C', 'P', 'T', 'L']

# Rules whose measurement K1 changed at the first crux-lab lock, by the lock of the rule set they changed from. A baseline report made under
# that lock carries no per-rule fingerprint, so REG compares its rules by threshold text and leaves these out (their old verdicts measured
# something else). Rules removed at that lock: V06 (3D rack focus), V07 (motion blur 8x).
CHANGED_SINCE = {'0478df7377b754137071e202c2ff396d7deba94293823cabf5f18932c411c612':
                 ['A14', 'A15', 'R03', 'V01', 'V05', 'A10', 'C04', 'C03', 'C07', 'C01', 'C12', 'V02', 'V03', 'V08', 'V11', 'C14', 'C13', 'S11', 'V10']}
REG_META = {'id': 'REG', 'section': 'CH §5, §4 khâu 3 (cổng hồi quy)', 'engine': 'py',
            'measure': 'baseline = the checker\'s report of the previous version of the episode (--baseline). A rule is comparable when it is in both reports and its '
                       'definition is unchanged: same fingerprint (sha256 of measure + threshold), or, for a baseline without fingerprints, the same threshold text and '
                       'not in CHANGED_SINCE[baseline lock]. Regression = comparable rule PASS in the baseline and not PASS now (FAIL, MISSING or ERROR)',
            'threshold': '0 regressions (a --first run has nothing to compare and passes; no baseline and no --first = MISSING)'}
REG_META['fingerprint'] = common.fingerprint(REG_META['measure'], REG_META['threshold'])


def key(fn):
    rid = fn.rid
    return (ORDER.index(rid[0]), int(rid[1:]))


def regression(res, baseline, first=False):
    """REG verdict from this run's results and the baseline report (dict) or first=True."""
    if baseline is None:
        if first:
            return common.Result('REG', 'PASS', [common.metric('regressions', 0, '<=', 0)], note='first version: nothing to compare')
        return common.Result('REG', 'MISSING', note='no baseline report (--baseline <previous report.json>) and not declared --first')
    changed = set(CHANGED_SINCE.get(baseline.get('lock') or '', []))
    base = {r['id']: r for r in baseline.get('results', [])}
    comp, incomp, reg = [], [], []
    for r in res:
        b = base.get(r['id'])
        if b is None or r['id'] == 'REG':
            continue
        if b.get('fingerprint'):
            same = b['fingerprint'] == r.get('fingerprint')
        else:
            same = b.get('threshold') == r.get('threshold') and r['id'] not in changed
        if not same:
            incomp.append(r['id'])
            continue
        comp.append(r['id'])
        if b['status'] == 'PASS' and r['status'] != 'PASS':
            reg.append({'rule': r['id'], 'was': 'PASS', 'now': r['status'], 'failing': [f"{m['name']} = {m['value']}" for m in r.get('metrics', []) if not m['pass']][:4]})
    return common.verdict('REG', [common.metric('comparable rules', len(comp), '>=', 1), common.metric('regressions', len(reg), '<=', 0)],
                          details=[{'baselineLock': baseline.get('lock'), 'baselineRoot': baseline.get('root'), 'comparable': comp, 'notComparable': incomp,
                                    'improved': [i for i in comp if base[i]['status'] != 'PASS' and next(r for r in res if r['id'] == i)['status'] == 'PASS']}, *reg])


def registry():
    return [fn.meta for fn in sorted(common.RULES, key=key)] + [REG_META]


def main():
    args = sys.argv[1:]
    if '--list' in args:
        print(json.dumps(registry(), indent=1, ensure_ascii=False))
        return
    root = args[0]
    only = set(args[args.index('--only') + 1].split(',')) if '--only' in args else None
    ctx = common.Ctx(root, contract=args[args.index('--contract') + 1] if '--contract' in args else None)
    if only:
        only.discard('')
    res = []
    for fn in sorted(common.RULES, key=key):
        if only and fn.rid not in only:
            continue
        t0 = time.time()
        r = common.safe(fn, ctx)
        r['section'] = fn.meta['section']
        r['threshold'] = fn.meta['threshold']
        r['fingerprint'] = fn.meta['fingerprint']
        r['seconds'] = round(time.time() - t0, 1)
        res.append(r)
        print(f"{r['id']:4} {r['status']:7} {r['seconds']:6}s  " + '; '.join(f"{m['name']}={m['value']}" for m in r['metrics'] if not m['pass'])[:200] + (('  ' + r['note']) if r.get('note') else ''), flush=True)
    if not only or 'REG' in only:
        bl = args[args.index('--baseline') + 1] if '--baseline' in args else os.environ.get('K_BASELINE')
        r = regression(res, json.load(open(bl)) if bl else None, first='--first' in args)
        r.update(section=REG_META['section'], threshold=REG_META['threshold'], fingerprint=REG_META['fingerprint'], seconds=0.0)
        if bl:
            r['baseline'] = os.path.abspath(bl)
        res.append(r)
        print(f"{r['id']:4} {r['status']:7}  " + '; '.join(f"{m['name']}={m['value']}" for m in r['metrics'] if not m['pass']) + (('  ' + r['note']) if r.get('note') else ''), flush=True)
    near = [{'rule': r['id'], **m} for r in res for m in r['metrics'] if m.get('near')]
    counts = {s: sum(1 for r in res if r['status'] == s) for s in ('PASS', 'FAIL', 'MISSING', 'ERROR')}
    lock = open(os.path.join(os.path.dirname(__file__), '..', 'LOCK')).read().strip() if os.path.exists(os.path.join(os.path.dirname(__file__), '..', 'LOCK')) else None
    vsha = common.sha256_file(ctx.path('out/video.mp4')) if ctx.has('out/video.mp4') else None
    out = {'root': ctx.root, 'contract': ctx.contract_path or ctx.path('contract.json'), 'lock': lock, 'video_sha256': vsha, 'counts': counts, 'near': near, 'results': res}
    os.makedirs(ctx.path('out/checks'), exist_ok=True)
    name = 'report' if not only else 'report-partial'
    json.dump(out, open(ctx.path(f'out/checks/{name}.json'), 'w'), indent=1, ensure_ascii=False, default=str)
    with open(ctx.path(f'out/checks/{name}.md'), 'w') as f:
        f.write(f"# checks/ report\n\nroot: `{ctx.root}`  \nlock: `{lock}`  \nmaster SHA-256: `{vsha}`  \n{counts}\n\n| rule | § | status | failing metrics |\n|---|---|---|---|\n")
        for r in res:
            bad = '; '.join(f"{m['name']} = {m['value']} (need {m['op']} {m['threshold']})" for m in r['metrics'] if not m['pass'])
            f.write(f"| {r['id']} | {r['section']} | {r['status']} | {bad or r.get('note') or ''} |\n")
        if near:
            f.write('\n## Metrics within 5% of a threshold\n\n' + '\n'.join(f"- {n['rule']} {n['name']} = {n['value']} (threshold {n['op']} {n['threshold']})" for n in near) + '\n')
    print(json.dumps(counts))


if __name__ == '__main__':
    main()
