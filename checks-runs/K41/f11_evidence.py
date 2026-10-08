"""K4.1 (chờ chủ dự án) — bằng chứng A10 + A16: F11 cũ (khai báo M3 + RELEASE_FILES) và F11 mới (danh sách của nhà máy) trên Tập 3–5.
Bản trong git không có media (video, stem, work/factory: .gitignore) → mỗi tệp thiếu được xếp: có trong git / bị .gitignore (giao ở bản C5, không vào git) /
thiếu thật. Tập 4, Tập 5: kết quả F11 trên gốc thật đã lưu (out/checks/report.json, run-c5c) để so.
  python3 checks-runs/K41/f11_evidence.py > checks-runs/K41/F11-evidence.md"""
import json, os, subprocess, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'checks', 'py'))
sys.path.insert(0, os.path.join(ROOT, 'checks-runs', 'K40'))
import common, run, r_file, retro  # noqa: E401,E402


def ignored(rel):
    return subprocess.run(['git', 'check-ignore', '-q', rel], cwd=ROOT).returncode == 0


print('# F11 cũ / mới trên Tập 3–5 (K4.1, chờ chủ dự án)\n')
for ep in ('ep003', 'ep004', 'ep005'):
    d, cache = retro.build(ep)
    ctx = common.Ctx(d, cache=cache)
    r = common.safe(run.common.RULES[[f.rid for f in common.RULES].index('F11')], ctx)
    det = r['details'][0] if r['details'] else {}
    print(f"## {ep}: chế độ {'nhà máy' if det.get('source') == 'factory' else 'khai báo M3 (K2)'} — {r['status']}\n")
    miss = det.get('notDelivered', [])
    for m in miss:
        rel = m if m.startswith('episodes/') else f'episodes/{ep}/{m.replace(".*", ".flac")}'
        print(f"- thiếu trong git: `{m}` — {'.gitignore (media/work, giao ở bản C5)' if ignored(rel) else 'KHÔNG bị .gitignore: thiếu thật'}")
    if det.get('declaredNotMadeByFactory'):
        print(f"- hợp đồng khai mà nhà máy không làm (chỉ báo, không đòi): {', '.join(det['declaredNotMadeByFactory'])}")
    if det.get('notDeclared'):
        print(f"- RELEASE_FILES chưa khai: {', '.join(det['notDeclared'])}")
    print()
