#!/usr/bin/env python3
"""Đóng gói và chấm kiểm mù theo `playbook/quality-framework.md` v2 §5.

Bốn lệnh, đúng thứ tự một lượt kiểm:

  deal   — chia mẫu cho người đọc: mỗi (mẫu, người đọc thứ k) một thư mục tên hex 8 ký tự chứa đúng một file
           cùng tên hex; ghi khoá giải mã (KEY.json, nằm NGOÀI thư mục người đọc) và prompts.json
           (hex → đường dẫn + câu hỏi cố định) cho phiên điều phối giao agent.
  packet — từ câu trả lời (answers.json {hex: "nguyên văn"}) dựng gói cho người chấm độc lập mù tập:
           nhãn R01… trộn ngẫu nhiên, mỗi nhãn chỉ có câu trả lời + rubric "đúng nghĩa" / "chỉ tả hình";
           không tên tập, không tên mẫu, không biết mẫu nào là đối chứng. Khoá nhãn ghi riêng.
  tally  — gộp điểm người chấm (scores.json {Rxx: {score: 1|0.5|0, advice_stated: bool, advice_inferred: bool, caution_only: bool, quote, why}};
           bản chấm cũ chỉ có `advice` vẫn đọc được: advice = advice_stated) → bảng theo mẫu,
           áp luật dừng sớm và luật câu khuyên, tính cổng (chỉ nhịp loại "image" của bộ ứng viên).
  next   — liệt kê mẫu cần người đọc thứ 3 (sau khi tally báo NEED_3RD) để chạy `deal --slots 3 --only …`.

Luật (ghi trong ý đồ trước khi chạy; mặc định khớp quality-framework v2):
  * Một người đọc "đúng" khi score == 1 VÀ không có câu khuyên. 0,5 ghi lại để tham khảo, tính là "không đúng".
  * Câu khuyên (K4.1, checks-appeal A9 + A21 — chờ chủ dự án duyệt): ba cờ, người chấm trích câu người đọc làm căn cứ (`quote`).
      advice_stated   — video (hình, chữ trên hình, lời) NÊU hoặc ngụ ý một hành động tài chính: mua / bán / giữ / chờ / khoá / chọn hay tránh
                        một sản phẩm. TÍNH: nhịp có ≥ 1 advice_stated → TRƯỢT ngay.
      advice_inferred — người đọc TỰ SUY hành động từ dữ liệu khi bị hỏi câu 4 (và/hoặc câu 5 nói là kết luận của mình, hoặc ghi
                        "the video doesn't state …"). BÁO, không chặn; đếm ở bảng.
      caution_only    — chỉ thận trọng chung (tự kiểm số của mình, hỏi chuyên gia / bên cho vay / chuyên gia thuế). Không tính (A9).
  * Dừng sớm: 2 người đầu cùng kết quả → xong (2/2 đạt, 0/2 trượt); lệch → gọi người thứ 3; đạt khi ≥ 2/3 đúng.
  * Cổng: tỉ lệ nhịp "image" của bộ ứng viên đạt ≥ --threshold. Nhịp "illustration" và bộ đối chứng chỉ báo cáo.

Manifest (JSON):
  {"question": "…câu hỏi cố định, tiếng Anh…",
   "candidate_set": "ep003",
   "samples": [{"id": "KEY-1", "set": "ep003", "kind": "image", "file": "path/KEY-1.png"},
               {"id": "S05",  "set": "ep001", "kind": "image", "file": "…"}]}
Rubric (JSON): {"rules": "…", "items": {"KEY-1": {"meaning": "…", "description_only": "…"}, …}}
  (khoá theo id mẫu; mẫu đối chứng dùng id riêng, ví dụ "ctrl:S05").
"""
import argparse, hashlib, json, os, random, secrets, shutil, sys

RNG = random.SystemRandom()


def _load(p, default=None):
    if default is not None and not os.path.exists(p):
        return default
    with open(p, encoding='utf-8') as f:
        return json.load(f)


def _dump(obj, p):
    os.makedirs(os.path.dirname(os.path.abspath(p)), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(obj, f, indent=1, ensure_ascii=False)
        f.write('\n')


def _sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


# ---------------------------------------------------------------- deal
def deal(manifest, outdir, keyfile, slots, only=None, base=None):
    m = _load(manifest)
    base = base or os.path.dirname(os.path.abspath(manifest))
    cand = m['candidate_set']
    key = _load(keyfile, {'_': 'GIẢI MÃ — không đưa cho người đọc hay người chấm.', 'question': m['question'],
                          'candidate_set': cand, 'items': {}})
    if key['question'] != m['question']:
        sys.exit('câu hỏi khác lượt trước: câu hỏi phải cố định cho mọi người đọc')
    taken = {(v['set'], v['id'], v['slot']) for v in key['items'].values()}
    jobs = []
    for s in m['samples']:
        if only and s['id'] not in only and f"{s['set']}/{s['id']}" not in only:
            continue
        for k in slots:
            if (s['set'], s['id'], k) in taken:
                sys.exit(f"đã chia {s['set']}/{s['id']} cho người đọc {k}")
            jobs.append((s, k))
    RNG.shuffle(jobs)
    os.makedirs(outdir, exist_ok=True)
    prompts = _load(os.path.join(outdir, 'prompts.json'), {})
    for s, k in jobs:
        h = secrets.token_hex(4)
        while h in key['items'] or os.path.exists(os.path.join(outdir, h)):
            h = secrets.token_hex(4)
        src = s['file'] if os.path.isabs(s['file']) else os.path.join(base, s['file'])
        ext = os.path.splitext(src)[1]
        os.makedirs(os.path.join(outdir, h))
        dst = os.path.join(outdir, h, h + ext)
        shutil.copyfile(src, dst)
        key['items'][h] = {'id': s['id'], 'set': s['set'], 'kind': s.get('kind', 'image'), 'slot': k,
                           'sha256': _sha(dst)}
        prompts[h] = {'path': os.path.abspath(dst), 'prompt': f"{m['question']}\n\nThe file to read: {os.path.abspath(dst)}"}
    _dump(key, keyfile)
    # prompts.json nằm ở gốc outdir, ngoài mọi thư mục hex: agent người đọc chỉ được trỏ vào thư mục của mình
    _dump(prompts, os.path.join(outdir, 'prompts.json'))
    return [h for h, v in key['items'].items() if v['slot'] in slots
            and (not only or v['id'] in only or f"{v['set']}/{v['id']}" in only)]


# ---------------------------------------------------------------- packet
def packet(keyfile, answersfile, rubricfile, packetfile, rubrickeyfile):
    key, ans, rub = _load(keyfile), _load(answersfile), _load(rubricfile)
    cand = key['candidate_set']
    old = _load(rubrickeyfile, {})
    done = set(old.values())
    hexes = [h for h in key['items'] if h in ans and h not in done]
    missing = [h for h in key['items'] if h not in ans]
    if missing:
        print(f'chưa có câu trả lời: {len(missing)} mẫu (bỏ qua trong gói này)', file=sys.stderr)
    RNG.shuffle(hexes)
    start = len(old)
    pk = {'rules': rub['rules'], 'scale': 'score: 1 = đủ phần ĐÚNG NGHĨA; 0.5 = một phần nghĩa; 0 = chỉ tả hình hoặc nghĩa khác. '
          'advice_stated: true khi câu trả lời cho thấy CHÍNH VIDEO (hình, chữ trên hình, lời) nêu hay ngụ ý một hành động tài chính '
          '(mua, bán, giữ, chờ, khoá, chọn/tránh một sản phẩm), kể cả phán "X an toàn/tốt hơn" mà người đọc gán cho video. '
          'advice_inferred: true khi người đọc TỰ SUY hành động đó từ dữ liệu (câu 4/5: "my own conclusion", "the video doesn\'t say …"). '
          'caution_only: true khi chỉ có thận trọng chung (tự kiểm số của mình, hỏi chuyên gia/bên cho vay) — không tính là khuyên. '
          'quote: trích nguyên văn câu của người đọc làm căn cứ cho cờ (rỗng nếu không cờ nào).',
          'return': '{"Rxx": {"score": 1|0.5|0, "advice_stated": true|false, "advice_inferred": true|false, "caution_only": true|false, '
                    '"quote": "…", "why": "≤ 15 từ"}}', 'items': {}}
    rk = dict(old)
    for i, h in enumerate(hexes, start + 1):
        it = key['items'][h]
        rid = it['id'] if it['set'] == cand else f"ctrl:{it['id']}"
        if rid not in rub['items']:
            sys.exit(f'rubric thiếu mục {rid}')
        lab = f'R{i:02d}'
        r = rub['items'][rid]
        pk['items'][lab] = {'answer': ans[h], 'meaning': r['meaning'], 'description_only': r['description_only']}
        rk[lab] = h
    _dump(pk, packetfile)
    _dump(rk, rubrickeyfile)
    return list(pk['items'])


# ---------------------------------------------------------------- tally
def beat_status(readers):
    """readers: [(score, advice), …] theo thứ tự đọc. Trả (trạng thái, số đúng, số câu khuyên)."""
    ok = [s == 1 and not a for s, a in readers]
    adv = sum(1 for _, a in readers if a)
    n_ok = sum(ok)
    if adv:
        return 'FAIL', n_ok, adv
    if len(readers) < 2:
        return 'NEED_MORE', n_ok, adv
    if len(readers) == 2:
        return ('PASS' if ok[0] else 'FAIL') if ok[0] == ok[1] else 'NEED_3RD', n_ok, adv
    return ('PASS' if n_ok >= 2 else 'FAIL'), n_ok, adv


MIN_IMAGE_SHARE = 0.6  # nhịp loại 1 ≥ 60% số nhịp then chốt (quality-framework v2 §5.8)


def check_classes(key, classesfile):
    """Bảng phân loại đã báo qua issue ({id: "image"|"illustration"}): manifest phải khớp, loại 1 ≥ 60%."""
    cl = _load(classesfile)
    cand = key['candidate_set']
    bad = sorted({v['id'] for v in key['items'].values() if v['set'] == cand and cl.get(v['id']) != v.get('kind')})
    if bad:
        sys.exit(f'loại nhịp trong manifest lệch bảng phân loại đã báo: {", ".join(bad)}')
    share = sum(k == 'image' for k in cl.values()) / len(cl)
    if share < MIN_IMAGE_SHARE:
        sys.exit(f'nhịp loại 1 chỉ {share:.0%} < {MIN_IMAGE_SHARE:.0%} số nhịp then chốt')
    return {'file': os.path.basename(classesfile), 'sha256': _sha(classesfile), 'image_share': round(share, 3)}


def tally(keyfile, rubrickeyfile, scoresfile, threshold=0.8, classesfile=None):
    """Chỉ cho kiểm theo nhịp ở C3, C4 (≤ 3 người đọc mỗi mẫu). C1, C2 đếm theo ý đồ của cổng."""
    key, rk, sc = _load(keyfile), _load(rubrickeyfile), _load(scoresfile)
    cand = key['candidate_set']
    if any(v['slot'] > 3 for v in key['items'].values()):
        sys.exit('tally chỉ dùng cho kiểm theo nhịp (≤ 3 người đọc); C1/C2 đếm theo ý đồ của cổng')
    classes = check_classes(key, classesfile) if classesfile else None
    per = {}
    for lab, h in rk.items():
        if lab not in sc:
            continue
        it = key['items'][h]
        v = sc[lab]
        if v['score'] not in (0, 0.5, 1):
            sys.exit(f'{lab}: điểm không hợp lệ {v["score"]}')
        stated = bool(v['advice_stated']) if 'advice_stated' in v else bool(v.get('advice'))   # bản chấm cũ: advice = stated
        d = per.setdefault((it['set'], it['id']), {'kind': it.get('kind', 'image'), 'r': [], 'inferred': 0})
        d['r'].append((it['slot'], v['score'], stated, v.get('why', '')))
        d['inferred'] += bool(v.get('advice_inferred')) and not stated
    rows = []
    for (st, sid), d in sorted(per.items(), key=lambda x: (x[0][0] != cand, x[0])):
        rs = sorted(d['r'])
        status, n_ok, adv = beat_status([(s, a) for _, s, a, _ in rs])
        rows.append({'set': st, 'id': sid, 'kind': d['kind'], 'scores': [s for _, s, _, _ in rs], 'readers': len(rs),
                     'correct': n_ok, 'advice': adv, 'advice_inferred': d['inferred'], 'status': status, 'why': [w for *_, w in rs]})
    gate = [r for r in rows if r['set'] == cand and r['kind'] == 'image']
    # câu khuyên ở BẤT KỲ nhịp nào của bộ ứng viên (kể cả loại 2) làm cổng trượt
    advice_beats = [r['id'] for r in rows if r['set'] == cand and r['advice']]
    pending = [r['id'] for r in gate if r['status'] not in ('PASS', 'FAIL')]
    n_pass = sum(r['status'] == 'PASS' for r in gate)
    res = {'candidate_set': cand, 'threshold': threshold, 'rows': rows, 'gate_beats': len(gate), 'gate_pass': n_pass,
           'pending': pending, 'advice_beats': advice_beats, 'classes': classes}
    if gate and not pending:
        share = n_pass / len(gate)
        res['share'] = round(share, 3)
        res['verdict'] = 'PASS' if share >= threshold and not advice_beats else 'FAIL'
        res['near_threshold'] = abs(share - threshold) <= 0.05  # chống Goodhart: ±5% quanh ngưỡng phải nêu tên
    else:
        res['verdict'] = 'PENDING'
    return res


def markdown(res):
    L = ['| Bộ | Mẫu | Loại | Điểm theo thứ tự đọc | Đúng | Câu khuyên | Kết quả |', '|---|---|---|---|---|---|---|']
    for r in res['rows']:
        L.append(f"| {r['set']} | {r['id']} | {r['kind']} | {' · '.join(str(s) for s in r['scores'])} | "
                 f"{r['correct']}/{r['readers']} | {r['advice']} | {r['status']} |")
    if res['verdict'] == 'PENDING':
        L.append(f"\n**Chưa xong:** cần người đọc thêm cho {', '.join(res['pending']) or '—'}.")
    else:
        near = ' — **trong ±5% quanh ngưỡng**' if res['near_threshold'] else ''
        adv = f"; câu khuyên ở {', '.join(res['advice_beats'])}" if res['advice_beats'] else ''
        L.append(f"\n**Cổng ({res['candidate_set']}, nhịp loại image): {res['gate_pass']}/{res['gate_beats']} = "
                 f"{res['share']:.0%}; ngưỡng {res['threshold']:.0%}{adv} → {res['verdict']}{near}.**")
    if res.get('classes'):
        c = res['classes']
        L.append(f"Bảng phân loại `{c['file']}` SHA-256 `{c['sha256'][:12]}…`, loại 1 = {c['image_share']:.0%}.")
    return '\n'.join(L)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    d = sub.add_parser('deal')
    d.add_argument('manifest'); d.add_argument('--out', required=True); d.add_argument('--key', required=True)
    d.add_argument('--slots', default='1,2'); d.add_argument('--only', default='', help='id hoặc set/id, cách nhau dấu phẩy')
    p = sub.add_parser('packet')
    p.add_argument('--key', required=True); p.add_argument('--answers', required=True)
    p.add_argument('--rubric', required=True); p.add_argument('--packet', required=True)
    p.add_argument('--rubric-key', required=True)
    t = sub.add_parser('tally')
    t.add_argument('--key', required=True); t.add_argument('--rubric-key', required=True)
    t.add_argument('--scores', required=True); t.add_argument('--threshold', type=float, default=0.8)
    t.add_argument('--json'); t.add_argument('--md'); t.add_argument('--classes', help='bảng phân loại nhịp đã báo')
    n = sub.add_parser('next')
    n.add_argument('--key', required=True); n.add_argument('--rubric-key', required=True)
    n.add_argument('--scores', required=True)
    a = ap.parse_args(argv)
    if a.cmd == 'deal':
        hs = deal(a.manifest, a.out, a.key, [int(x) for x in a.slots.split(',')],
                  [x for x in a.only.split(',') if x] or None)
        print(f'{len(hs)} mẫu đã chia; prompts: {os.path.join(a.out, "prompts.json")}')
    elif a.cmd == 'packet':
        print('nhãn:', ' '.join(packet(a.key, a.answers, a.rubric, a.packet, a.rubric_key)))
    elif a.cmd == 'tally':
        res = tally(a.key, a.rubric_key, a.scores, a.threshold, a.classes)
        if a.json:
            _dump(res, a.json)
        md = markdown(res)
        if a.md:
            open(a.md, 'w', encoding='utf-8').write(md + '\n')
        print(md)
    elif a.cmd == 'next':
        res = tally(a.key, a.rubric_key, a.scores)
        need = [f"{r['set']}/{r['id']}" for r in res['rows'] if r['status'] == 'NEED_3RD']
        print(','.join(need))


if __name__ == '__main__':
    main()
