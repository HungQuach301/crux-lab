"""R&D v3 · ĐỌC MÙ TẮT TIẾNG: 2 "người" × 2 lượt, qua toolkit/blind/headless.sh (headless, chỉ công cụ Read, chạy từ thư mục trống,
0 agent con). Khoá: CONSOLE_API_KEY truyền vào biến môi trường ANTHROPIC_API_KEY của tiến trình con — KHÔNG in, KHÔNG ghi ra tệp.
"Người" A = model sonnet, "người" B = model opus (hai mô hình đọc khác nhau; đây là CHẨN ĐOÁN, không phải người thật, không phải cổng).
Mỗi lượt là một phiên mới (không nhớ lượt trước). Vật liệu: tờ khung 19 ô + 5 dải 6 khung (không lời, không kịch bản).
  python3 rnd-hybrid/v3/blind/run.py   → rnd-hybrid/v3/blind/raw/<người>-<lượt>.json + cost.json
Trần chi: dừng nếu tổng cost_usd ≥ 2,5 $ (trần cứng bước 2: 3 $)."""
import json, os, subprocess, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
HERE = os.path.dirname(os.path.abspath(__file__)); RAW = os.path.join(HERE, 'raw'); os.makedirs(RAW, exist_ok=True)
MAT = os.path.join(ROOT, 'rnd-hybrid', 'v3', 'blind', 'material')
sheet = os.path.join(MAT, 'to-khung.png'); strips = sorted(os.path.join(MAT, f) for f in os.listdir(MAT) if f.startswith('strip-'))
tmpl = open(os.path.join(HERE, 'prompt.tmpl')).read().replace('{SHEET}', sheet).replace('{STRIPS}', '\n'.join(f'   {i + 1}. {p}' for i, p in enumerate(strips)))
pfile = os.path.join(RAW, 'prompt.txt'); open(pfile, 'w').write(tmpl)
key = os.environ.get('CONSOLE_API_KEY')
if not key: sys.exit('thiếu CONSOLE_API_KEY (headless chỉ dùng khoá Console)')
env = {k: v for k, v in os.environ.items() if k not in ('ANTHROPIC_API_KEY', 'CLAUDE_CODE_OAUTH_TOKEN')}; env['ANTHROPIC_API_KEY'] = key
total = 0.0; runs = []
for who, model in (('A', 'sonnet'), ('B', 'opus')):
    for k in (1, 2):
        out = os.path.join(RAW, f'{who}-{k}.json')
        if os.path.exists(out): d = json.load(open(out))
        else:
            r = subprocess.run(['bash', os.path.join(ROOT, 'toolkit', 'blind', 'headless.sh'), pfile, out, '--read', '--model', model], env=env, capture_output=True, text=True, timeout=900)
            if r.returncode or not os.path.exists(out): print('lỗi lượt', who, k, r.stderr[-800:].replace(key, '***')); sys.exit(1)
            d = json.load(open(out))
        total += d.get('cost_usd') or 0; runs.append({'who': who, 'model': model, 'pass': k, 'cost_usd': d.get('cost_usd'), 'turns': d.get('turns')})
        print(who, k, model, 'cost', d.get('cost_usd'), 'tổng', round(total, 3))
        if total >= 2.5: print('DỪNG: chạm ngưỡng chi 2,5 $'); break
    if total >= 2.5: break
json.dump({'runs': runs, 'total_usd': round(total, 4)}, open(os.path.join(RAW, 'cost.json'), 'w'), indent=1)
