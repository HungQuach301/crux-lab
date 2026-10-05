"""Trích nguyên văn câu trả lời của người đọc từ bản ghi agent (lệnh SubagentHandback), kiểm mỗi người đọc mở đúng 1 file của mình.
    python3 episodes/ep003/review-c4/extract.py MAP.json TASKDIR OUT.json   (MAP: {hex: agentId})"""
import json, sys
M, T, out = json.load(open(sys.argv[1])), sys.argv[2], {}
for h, a in M.items():
    reads = []
    for ln in open(f'{T}/{a}.output'):
        try:
            e = json.loads(ln)
        except ValueError:
            continue
        if e.get('type') != 'assistant':
            continue
        for c in (e.get('message') or {}).get('content', []):
            if c.get('type') == 'tool_use' and c['name'] == 'Read':
                reads.append(c['input'].get('file_path', ''))
            if c.get('type') == 'tool_use' and c['name'] == 'SubagentHandback':
                out[h] = max((v for v in c['input'].values() if isinstance(v, str)), key=len)
    assert len(reads) == 1 and h in reads[0], (h, reads)
json.dump(out, open(sys.argv[3], 'w'), indent=1, ensure_ascii=False)
print(len(out), 'answers')
