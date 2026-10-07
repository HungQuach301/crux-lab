"""B+1 · tập KHÔNG khai voice_overrides: mã cũ (main) và mã mới cho cùng khoá, cùng take, cùng file — giống hệt. API khoá.
  python3 moc-v/b1/b1_identical.py <voice_old.py> <episode_dir> <out.json>
Ca kiểm: bản sao Tập 5 (chỉ đọc nhánh ep005) với khoá voice_overrides BỊ BỎ (nhánh moc-v chưa có tập nào lưu take của nhà máy)."""
import hashlib, importlib.util, json, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'toolkit/factory')); sys.modules['requests'] = None
import yaml  # noqa: E402
import voice as NEW  # noqa: E402
spec = importlib.util.spec_from_file_location('voice_old', sys.argv[1]); OLD = importlib.util.module_from_spec(spec); spec.loader.exec_module(OLD); OLD.ROOT = ROOT
import re
EP = sys.argv[2]; Y = yaml.safe_load(open(os.path.join(EP, 'episode.yaml'))); Y.pop('voice_overrides', None)   # tập "không khai báo"
LINE = re.compile(r'^(S\d\d)\.(\d+)\s+(?:\{(\w+)\}\s+)?(.+?)\s*<!--')
script = {}
for ln in open(os.path.join(EP, 'story/script.md'), encoding='utf-8'):
    m = LINE.match(ln)
    if m: script[f'{m.group(1)}.{m.group(2)}'] = {'id': f'{m.group(1)}.{m.group(2)}', 'scene': m.group(1), 'text': m.group(4).strip()}
Y['scenes'] = [{'id': sc} for sc in sorted({s['scene'] for s in script.values()})]
rep = {}
for sc in Y['scenes']:
    sents = [s for s in script.values() if s['scene'] == sc['id']]
    w = os.path.join(ROOT, 'moc-v/work/b1-wav-id')
    a = OLD.voice_scene(Y['voice'], sents, os.path.join(EP, 'voice-takes'), w)
    b = NEW.voice_scene(NEW.scene_cfg(Y['voice'], Y.get('voice_overrides'), sc['id']), sents, os.path.join(EP, 'voice-takes'), w)
    strip = lambda v: {k: v[k] for k in ('mp3', 'key', 'duration', 'sentences', 'words', 'chars', 'take')}
    rep[sc['id']] = {'identical': strip(a) == strip(b), 'take': os.path.basename(b['mp3'])}
out = {'scenes': len(rep), 'identical': sum(v['identical'] for v in rep.values()), 'detail': rep}
json.dump(out, open(sys.argv[3], 'w'), indent=1); print(out['scenes'], 'scenes, identical:', out['identical'])
