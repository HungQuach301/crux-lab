"""Tốc độ đọc thật và tỉ lệ thời lượng/từ theo tập (lessons T6-5; mở rộng từ tongket-t5/measure_pace.py). Chạy sau mỗi tập:
    python3 toolkit/usage/measure_pace.py ep004 ep005 ep006
Hằng trong check_script.py (WPS_SPEECH, WPS_TOTAL) lấy theo TẬP CUỐI cùng giọng/model/speed; lệch > 2 % so với hằng đang dùng → sửa mẫu
playbook/templates/check_script.py và ghi một dòng vào lessons."""
import json, os, re, statistics as st, sys

def words(s):
    return len(re.sub(r'\[[^\]]*\]', '', s or '').split())

for ep in sys.argv[1:] or ['ep005', 'ep006']:
    S = json.load(open(f'episodes/{ep}/out/script.json'))['sentences']
    spoken = sum(words(x['spoken']) for x in S)
    speech = sum(x['end'] - x['start'] for x in S)
    total = max(json.load(open(t))['total'] for t in (f'episodes/{ep}/out/factory/timeline.json',
                f'episodes/{ep}/out/timeline.json') if os.path.exists(t))
    per = {}
    for x in S:
        a = per.setdefault(x['scene'], [0, 0.0]); a[0] += words(x['spoken']); a[1] += x['end'] - x['start']
    r = [w / d for w, d in per.values() if d > 0]
    print(f'{ep}: từ nói {spoken} · giây lời {speech:.1f} · tổng {total:.1f} · '
          f'đọc {spoken/speech:.2f} từ/s · thời lượng {spoken/total:.2f} từ/s · ngoài lời {total/speech-1:.0%} · '
          f'theo cảnh {min(r):.2f}–{max(r):.2f} (trung vị {st.median(r):.2f}, độ lệch chuẩn {st.pstdev(r):.2f})')
