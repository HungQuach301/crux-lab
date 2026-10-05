"""Tập 3 · C4 (REVIEWER ý đồ C4, CHẶN 1): `packets.py packet` luôn chèn trường `scale` với định nghĩa khuyên CŨ ("tự rút một lời khuyên hay phán
'X an toàn/tốt hơn'"). Bộ đo câu khuyên mới (chủ dự án, C3) chỉ tính hành động hướng tới người xem. Script này thay `scale` của gói người chấm
bằng đúng câu `rules` của rubric đang dùng (không thêm, không bớt) và in SHA-256 gói sau khi thay. Chạy ngay sau `packets.py packet`, trước khi giao người chấm.
    python3 episodes/ep003/review-c4/fix_packet.py PACKET.json RUBRIC.json"""
import hashlib, json, sys
pk, rub = json.load(open(sys.argv[1])), json.load(open(sys.argv[2]))
pk['scale'] = rub['rules']
json.dump(pk, open(sys.argv[1], 'w'), indent=1, ensure_ascii=False)
print('scale := rubric.rules;', hashlib.sha256(open(sys.argv[1], 'rb').read()).hexdigest())
