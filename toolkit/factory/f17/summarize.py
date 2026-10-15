"""F-17 · gom số đo của cine_check.js thành bảng cho REPORT (T4–T9).
  python3 toolkit/factory/f17/summarize.py <cine.json>… > out.md     (mỗi tệp: một cảnh; luật màu = cine_color.judge)
T6 viền: ΔL* (viền bật − tắt) trung bình ở điểm ảnh xa đèn (n·đèn ≤ 0) / gần đèn (n·đèn > 0,2) — đích xa ≤ 0,5 và ≤ 10 % gần (shot nào có người).
T7 màu thân: ΔE2000 trung bình sRGB thân người trước/sau lớp. T8 vệt DOF: max theo cột của ΔL* trong dải 1–6 px trên đầu, F-17 vs fragment v4.
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'world', 'cine'))
import cine_color as CC  # noqa: E402


def main(paths):
    out = {}
    print('| cảnh | mẫu | nhóm màu dữ liệu | ΔE2000 max | luật màu | viền xa đèn ΔL* (max mẫu) | lõi xa đèn ΔL* (max, chẩn đoán) | gần đèn ΔL* (min mẫu) | xa/gần max | thân ΔE2000 (max) | vệt DOF F-17 / v4 (max ΔL*) | mái trơn / vân (khung-mái) |')
    print('|---|---|---|---|---|---|---|---|---|---|---|---|')
    for p in paths:
        d = json.load(open(p)); j = CC.judge(d); name = os.path.basename(p).split('.')[0]
        rims = [c for s in d['samples'] if s.get('rim') for c in s['rim']['chars'] if c.get('nFar', 0) >= 200 and c.get('nNear', 0) >= 200]
        far = max((c['farDL'] for c in rims), default=None); near = min((c['nearDL'] for c in rims), default=None)
        core = max((c.get('farCoreDL', 0) for c in rims), default=None); ratio = max((c['farDL'] / c['nearDL'] for c in rims if c['nearDL'] > 0), default=None)
        de_body = max((CC.de2000(CC.srgb_to_lab(c['base']), CC.srgb_to_lab(c['cine'])) for c in rims), default=None)
        st = [s['streak'] for s in d['samples'] if s.get('streak')]
        sf, sv = (max(x['maxFixed'] for x in st), max(x['maxV4'] for x in st)) if st else (None, None)
        f = lambda v, k=2: '—' if v is None else f'{v:.{k}f}'  # noqa: E731
        r = d.get('roof', {})
        print(f"| {name} | {j['samples']} | {j['groups']} | {f(j['max_dE'])} | **{j['level']}** | {f(far)} | {f(core)} | {f(near)} | {f(ratio)} | {f(de_body, 1)} | "
              f"{f(sf, 1)} / {f(sv, 1)} | {r.get('roofPlain', 0)} / {r.get('roofTex', 0)} |")
        out[name] = {'color': {k: j[k] for k in ('level', 'samples', 'groups', 'max_dE', 'block')}, 'rim_far_max': far, 'rim_far_core_max': core, 'rim_near_min': near, 'rim_far_near_ratio_max': ratio,
                     'body_dE_max': de_body, 'streak_fixed_max': sf, 'streak_v4_max': sv, 'roof': r}
    json.dump(out, open(os.environ.get('F17_SUMMARY', os.devnull), 'w'), indent=1, ensure_ascii=False)


if __name__ == '__main__':
    main(sys.argv[1:])
