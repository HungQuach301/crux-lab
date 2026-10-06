"""Run every machine rule (genre-spec/data-explainer.md [MÁY]) on a project root and write <root>/out/checks/report.json and report.md.

    python3 checks/py/run.py <root> [--contract <episode contract.json>] [--only F01,A01] [--list] [--baseline <previous report.json> | --first]

The episode contract defaults to <root>/contract.json (checks/CONTRACT.md §Episode contract).

REG (regression gate): every rule that PASSed in the checker's report of the previous version of the episode (--baseline, a
report the checking session keeps outside the builder's tree) and is comparable (same definition) must still PASS. --first
declares the first version (nothing to compare). Neither given: REG is MISSING.

Status: PASS | FAIL | MISSING (a contract artifact is absent: counts as not passed) | ERROR (rule crashed: counts as not passed).
`near` lists every metric within 5% of its threshold (brief §0: report metrics that only just meet a threshold), by rule, metric and tier.

Tier (K3, py/tiers.py): the episode verdict is TRƯỢT when a BLOCK (CHẶN) rule does not pass; else CHỜ GIẢI THÍCH when a MAJOR (CHÍNH) rule does
not pass and out/explanations.json has no explanation for it (≥ 8 words); else ĐẠT. A REFERENCE (THAM KHẢO) rule only reports its measurements."""
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(__file__))
import common  # noqa: E402
import r_file, r_audio, r_content, r_rhythm, r_visual, r_page, r_sound, r_voice, r_short  # noqa: E402,F401
import tiers  # noqa: E402

ORDER = ['F', 'A', 'S', 'R', 'V', 'C', 'P', 'T', 'L']

# Rules whose measurement K1 changed at the first crux-lab lock, by the lock of the rule set they changed from. A baseline report made under
# that lock carries no per-rule fingerprint, so REG compares its rules by threshold text and leaves these out (their old verdicts measured
# something else). Rules removed at that lock: V06 (3D rack focus), V07 (motion blur 8x).
CHANGED_SINCE = {'0478df7377b754137071e202c2ff396d7deba94293823cabf5f18932c411c612':
                 ['A14', 'A15', 'R03', 'V01', 'V05', 'A10', 'C04', 'C03', 'C07', 'C01', 'C12', 'V02', 'V03', 'V08', 'V11', 'C14', 'C13', 'S11', 'V10']}
REG_META = {'id': 'REG', 'section': 'CH §5, §4 khâu 3 (cổng hồi quy)', 'engine': 'py',
            'measure': 'baseline = the checker\'s report of the previous version of the episode (--baseline). A rule is comparable when it is in both reports and its '
                       'definition is unchanged: same fingerprint (sha256 of measure + threshold), or, for a baseline without fingerprints, the same threshold text and '
                       'not in CHANGED_SINCE[baseline lock]. Regression = comparable rule PASS in the baseline and not PASS now (FAIL, MISSING or ERROR). K3: only a '
                       'regression of a BLOCK (CHẶN) rule counts; regressions of MAJOR and REFERENCE rules are listed with their tier',
            'threshold': '0 regressions of BLOCK rules (a --first run has nothing to compare and passes; no baseline and no --first = MISSING)'}
REG_META['fingerprint'] = common.fingerprint(REG_META['measure'], REG_META['threshold'])


def key(fn):
    rid = fn.rid
    head = rid.rstrip('0123456789')
    return (ORDER.index(rid[0]), head, int(rid[len(head):]))   # K3.8: SH01… (Shorts) after the S rules


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
            reg.append({'rule': r['id'], 'tier': tiers.tier(r['id']), 'was': 'PASS', 'now': r['status'],
                        'failing': [f"{m['name']} = {m['value']}" for m in r.get('metrics', []) if not m['pass']][:4]})
    blocking = [x for x in reg if x['tier'] == tiers.BLOCK]
    return common.verdict('REG', [common.metric('comparable rules', len(comp), '>=', 1), common.metric('regressions of BLOCK rules', len(blocking), '<=', 0)],
                          details=[{'baselineLock': baseline.get('lock'), 'baselineRoot': baseline.get('root'), 'comparable': comp, 'notComparable': incomp,
                                    'improved': [i for i in comp if base[i]['status'] != 'PASS' and next(r for r in res if r['id'] == i)['status'] == 'PASS']}, *reg])


def registry():
    return [{**m, 'tier': tiers.tier(m['id']), 'tierReason': tiers.TIERS[m['id']][1]} for m in [fn.meta for fn in sorted(common.RULES, key=key)] + [REG_META]]


EXPLAIN_MIN_WORDS = 8


def explanations(root):
    """out/explanations.json of the builder: {"<rule>": "why it does not pass and why the episode can still go"} or {"explanations": [{rule, text}]}."""
    p = os.path.join(root, 'out', 'explanations.json')
    if not os.path.exists(p):
        return {}
    d = json.load(open(p, encoding='utf-8'))
    if isinstance(d.get('explanations'), list):
        d = {e.get('rule'): e.get('text') for e in d['explanations'] if isinstance(e, dict)}
    return {k: v for k, v in d.items() if isinstance(v, str) and len(v.split()) >= EXPLAIN_MIN_WORDS}


def episode_verdict(res, expl):
    """Tier summary and the episode verdict: only BLOCK fails; MAJOR not passing needs an explanation; REFERENCE is measurement only."""
    summ = {}
    for t in (tiers.BLOCK, tiers.MAJOR, tiers.REFERENCE):
        rs = [r for r in res if r['tier'] == t]
        summ[t] = {'label': tiers.LABEL[t], 'rules': len(rs), 'pass': sum(1 for r in rs if r['status'] == 'PASS'),
                   'notPass': [f"{r['id']} {r['status']}" for r in rs if r['status'] != 'PASS']}
    unexplained = [r['id'] for r in res if r['tier'] == tiers.MAJOR and r['status'] != 'PASS' and r['id'] not in expl]
    summ[tiers.MAJOR]['explained'] = {r['id']: expl[r['id']] for r in res if r['tier'] == tiers.MAJOR and r['status'] != 'PASS' and r['id'] in expl}
    summ[tiers.MAJOR]['unexplained'] = unexplained
    if summ[tiers.BLOCK]['notPass']:
        v = 'TRƯỢT'
    elif unexplained:
        v = 'CHỜ GIẢI THÍCH'
    else:
        v = 'ĐẠT'
    return v, summ


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
        r['tier'] = tiers.tier(fn.rid)
        r['seconds'] = round(time.time() - t0, 1)
        res.append(r)
        print(f"{r['id']:4} {r['status']:7} {r['seconds']:6}s  " + '; '.join(f"{m['name']}={m['value']}" for m in r['metrics'] if not m['pass'])[:200] + (('  ' + r['note']) if r.get('note') else ''), flush=True)
    if not only or 'REG' in only:
        bl = args[args.index('--baseline') + 1] if '--baseline' in args else os.environ.get('K_BASELINE')
        r = regression(res, json.load(open(bl)) if bl else None, first='--first' in args)
        r.update(section=REG_META['section'], threshold=REG_META['threshold'], fingerprint=REG_META['fingerprint'], tier=tiers.tier('REG'), seconds=0.0)
        if bl:
            r['baseline'] = os.path.abspath(bl)
        res.append(r)
        print(f"{r['id']:4} {r['status']:7}  " + '; '.join(f"{m['name']}={m['value']}" for m in r['metrics'] if not m['pass']) + (('  ' + r['note']) if r.get('note') else ''), flush=True)
    near = [{'rule': r['id'], 'tier': r['tier'], **m} for r in res for m in r['metrics'] if m.get('near')]
    verdict_, summ = episode_verdict(res, explanations(ctx.root))
    counts = {s: sum(1 for r in res if r['status'] == s) for s in ('PASS', 'FAIL', 'MISSING', 'ERROR')}
    lock = open(os.path.join(os.path.dirname(__file__), '..', 'LOCK')).read().strip() if os.path.exists(os.path.join(os.path.dirname(__file__), '..', 'LOCK')) else None
    vsha = common.sha256_file(ctx.path('out/video.mp4')) if ctx.has('out/video.mp4') else None
    out = {'root': ctx.root, 'contract': ctx.contract_path or ctx.path('contract.json'), 'lock': lock, 'video_sha256': vsha, 'episode': verdict_, 'tiers': summ,
           'counts': counts, 'near': near, 'results': res}
    os.makedirs(ctx.path('out/checks'), exist_ok=True)
    name = 'report' if not only else 'report-partial'
    json.dump(out, open(ctx.path(f'out/checks/{name}.json'), 'w'), indent=1, ensure_ascii=False, default=str)
    with open(ctx.path(f'out/checks/{name}.md'), 'w') as f:
        f.write(f"# checks/ report\n\nroot: `{ctx.root}`  \nlock: `{lock}`  \nmaster SHA-256: `{vsha}`  \n{counts}\n\n"
                f"**Tập: {verdict_}** (chỉ luật CHẶN làm trượt tập; luật CHÍNH không đạt cần bên dựng giải thích; luật THAM KHẢO chỉ báo số đo)\n\n"
                "| cấp | luật | đạt | không đạt |\n|---|---|---|---|\n")
        for t, x in summ.items():
            f.write(f"| {x['label']} | {x['rules']} | {x['pass']} | {', '.join(x['notPass']) or '—'} |\n")
        if summ[tiers.MAJOR]['unexplained']:
            f.write(f"\nCHÍNH không đạt, chưa có giải thích trong `out/explanations.json`: {', '.join(summ[tiers.MAJOR]['unexplained'])}\n")
        f.write('\n## Chỉ số trong ±5% quanh ngưỡng\n\n' + ('\n'.join(f"- {n['rule']} ({tiers.LABEL[n['tier']]}) · {n['name']} = {n['value']} (ngưỡng {n['op']} {n['threshold']}, "
                                                                     f"{'đạt' if n['pass'] else 'không đạt'})" for n in near) or 'không có') + '\n')
        f.write("\n| rule | tier | § | status | failing metrics |\n|---|---|---|---|---|\n")
        for r in res:
            bad = '; '.join(f"{m['name']} = {m['value']} (need {m['op']} {m['threshold']})" for m in r['metrics'] if not m['pass'])
            f.write(f"| {r['id']} | {tiers.LABEL[r['tier']]} | {r['section']} | {r['status']} | {bad or r.get('note') or ''} |\n")
    for n in near:
        print(f"near {n['rule']} ({tiers.LABEL[n['tier']]}) {n['name']} = {n['value']} (threshold {n['op']} {n['threshold']})")
    print(json.dumps(counts), 'episode:', verdict_)


if __name__ == '__main__':
    main()
