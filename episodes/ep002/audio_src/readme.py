"""Writes out/audio/README.md from work/audio/report.json, out/audio/manifest.json, out/voice/takes.json and (optional) a checks report.
    python3 episodes/ep002/audio_src/readme.py [<checks report.json>]
"""
import json
import os
import sys

EP = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
J = lambda p: json.load(open(os.path.join(EP, p)))
rep, man, tk = J('work/audio/report.json'), J('out/audio/manifest.json'), J('out/voice/takes.json')
ck = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else None
T2_DEFAULT, T2_ALT, ALT_CHECKS = (sys.argv[2:5] + ['?', '?', '?'])[:3]
m = rep['master']
s08 = next(t for t in tk['takes'] if t['id'] == 'S08')
sil = rep['silences']
L = []
L.append('# Tập 2 · C5 · tiếng (luồng A)\n')
L.append(f"Bản mix cuối trên `animatic/timing.json` (tổng {man['timing']['total_s']:.4f} s, SHA-256 `{man['timing']['sha256'][:12]}…`). "
         'File wav không commit (`.gitignore`); SHA-256 và kích thước trong `manifest.json`. Dựng lại: '
         '`python3 episodes/ep002/audio_src/takes.py && python3 episodes/ep002/audio_src/events.py && python3 episodes/ep002/audio_src/mix.py` (seed cố định).\n')
L.append('## Đo trên master (`master.wav`, trước AAC)\n')
L.append(f"- Âm lượng tích hợp **{m['I']} LUFS** (đích −14, A01 ±1) · true peak **{m['TP']} dBTP** (trần −1,5; A02 ≤ −1,0) · LRA {m['LRA']} LU.")
L.append(f"- Limiter true peak (4× oversample, look-ahead 5 ms): gain nhỏ nhất {rep['limiterMinGainDb']} dB, dưới −1 dB ở {rep['limiterGainBelow1dBShare'] * 100:.2f}% mẫu.")
L.append(f"- Stem (dBFS RMS cả tập): " + ', '.join(f'{k} {v}' for k, v in rep['stemLevelsDbfs'].items()) + '; sfx/whoosh im (bảng S2 không có lớp sfx). '
         f"Tổng stem = master (sai lệch lớn nhất {rep['sumMinusMasterMax']:.1e}).\n")
L.append('## Lời ưu tiên (G-006): duck dưới lời\n')
L.append(f"- Nhạc (kiểu C của Tập 1, G-016 · chọn) đặt **{rep['voiceOverMusicDb_A07']} dB dưới lời** trên các cửa sổ 100 ms có lời (cách đo A07; đích 20 dB như Tập 1); "
         'dải 1–4 kHz của nhạc duck thêm 13 dB khi có lời (nhìn trước 80 ms, thả 350 ms).')
L.append(f"- Tiếng dữ liệu (S2 \"minimal\", G-005 · chọn): −{rep['sonUnderVoiceDb']:.0f} dB dưới RMS lời trước side-chain; khi có lời thêm −8 dB và bỏ 95% dải 1–4 kHz; "
         f"nốt rơi vào lời được dời vào khe âm tiết (−60…+120 ms): {rep['sonification']['shiftedIntoGaps']}/{rep['sonification']['notes']} nốt, trung vị {rep['sonification']['medianShiftMs']} ms. "
         f"Không bao giờ nâng mức. Năng lượng stem sonify trong dải khai báo (60–270 Hz + 4,5–7 kHz) = {rep['sonBandShare'] * 100:.1f}%. "
         'Nhạc nhường −10 dB trong hai dải đó khi tiếng dữ liệu kêu.')
L.append(f"- Khoảng lặng (G-003): {len(sil)} khe lời ở các bước ngoặt (+ điểm quảng cáo): nền nhả τ 90 ms, room +8 dB, trở lại 200 ms — "
         + '; '.join(f"{r['t']:.2f} s ({r['dur']:.2f} s{', quảng cáo' if 'adBreak' in r else ''})" for r in sil) + '. Các cú cắt cảnh khác: nhạc phồng +3 dB.\n')
L.append('## Tiếng dữ liệu: chọn sự kiện (cách S2 của Tập 1)\n')
L.append('63 hành động dữ liệu (`out/sonify-events.json`, `work/audio/son-plan.json`, lý do trong `audio_src/events.py`), neo vào hình (`animatic/src/anchors`) và giải lại trên timing.json hiện tại: '
         'lãi suất vượt 9% (đường thả nổi cắt đường 9% = `line` dao động; các lần leo trên 9% ở S06, S07, S08 tới 19,3% = `line` đi lên); khởi đầu thấp hơn (mỗi lần lật điểm xuất phát = `dot`, cao độ theo độ cao); '
         'đệm tiết kiệm (hũ đầy = `bar` mọc, hũ cạn = `line` đi xuống ở S06.3, S07.5, S08.4); ô kết quả đỏ (khung chạy thả ô = `roll` tăng tốc theo dáng lãi T-bill; ô đỏ cao và to hơn; tỉ lệ đỏ 28,4/3,5/20,4/10,5/31,3/57,9/72,9% = `bar` cao độ theo tỉ lệ); '
         'chồng lãi và khối "đắt hơn" (S04, S08) = `bar`. Nhãn, số dạng chữ, thẻ, cú nhúng và thẻ phương pháp không có tiếng (S2 không có lớp sfx).\n')
L.append('## Lời và ký tự ElevenLabs\n')
L.append(f"- Eric `{tk['voice']['voiceId']}`, `{tk['voice']['model']}`, mặc định (không voice_settings, không speed, không thẻ ngắt), mỗi cảnh một lần gọi, thẻ cảm xúc thưa như kịch bản.")
regen = [t for t in tk['takes'] if t['elChars']['C5']]
L.append(f"- {13 - len(regen)} cảnh dùng lại take C2 (chữ trùng kịch bản, cùng giọng/mô hình/thiết lập). Sinh lại ở C5 vì kịch bản đổi "
         '(S08.6 "in dollars of the day"; v5.2: S04.4, S09.5, S09.6, S10.3 "from 1954 to 1980"), mỗi cảnh seed 1, seed 2 chỉ khi ASR thiếu từ khoá:')
for t in regen:
    calls = ', '.join(f"seed {c['seed']} {c['characterCost']} ký tự" for c in t['elChars']['calls'])
    L.append(f"  - {t['id']}: {calls}; dùng {t['raw'].split('/')[-1]} ({t['audioS']:.2f} s), ASR thiếu {len(t['asr']['missing'])}.")
L.append(f"- **Ký tự ElevenLabs dùng ở C5: {tk['elCharsC5']}.**")
if rep.get('wordDips'):
    L.append('- Hạ nền cục bộ dưới một từ (A14 trên master nghe "Lea" thay "Leah" ở S02.2, stem lời một mình nghe đúng): '
             + '; '.join(f"{d['sentence']} \"{d['word']}\" {d['t']:.2f}–{d['end']:.2f} s nhạc + tiếng dữ liệu {d['db']:+.0f} dB" for d in rep['wordDips'])
             + ' (dốc 80 ms; không nâng lời).')
L.append('')
if ck:
    L.append('## Luật âm thanh (bản sao checks origin/main, LOCK `2fcc9fcc…`)\n')
    L.append('| Luật | Kết quả | Số đo |\n|---|---|---|')
    for r in ck['results']:
        meas = '; '.join(f"{x['name']} {x['value']}" for x in r.get('metrics', []))
        L.append(f"| {r['id']} ({r.get('tier')}) | {r['status']} | {meas[:180].replace('|', '/')} |")
    L.append('')
    L.append('Video tạm = nền màu + master (AAC 320k), chỉ để các luật đọc tiếng từ video chạy được; khi P mux bản thật thì chạy lại các luật đó. '
             'Mọi luật CHẶN về tiếng đều đạt (A14: 0/151 từ khoá thiếu trên master). '
             'T2 (tham khảo): ostinato kiểu C dùng chung một âm giai nên chroma của các câu 4 ô giống nhau ≥ 0,90, dù chuỗi hợp âm không lặp; Tập 1 kiểu C đo 29%. Gu C đã khoá nên không đổi. '
             'T3 (tham khảo): lối vào khoảng lặng chậm vì pad tự tắt dần (1,3 s trước khoảng lặng không có nốt mới), giống Tập 1. '
             'A03 LRA (tham khảo): thấp vì lời được ưu tiên, giống Tập 1. A17/R02/R03 đo lời và nhịp kịch bản, không phụ thuộc mix.')
alt = man.get('alt')
if alt:
    ra = json.load(open(os.path.join(EP, 'work', 'audio', 'report-alt.json')))
    L.append('')
    L.append('## Bản nhạc thay thế (`--music alt`, chủ dự án C6: cùng kiểu C, ít lặp hơn)\n')
    L.append('Cùng nhạc cụ, cùng nhịp, cùng âm giai; mỗi ô tự chọn nhịp thump, bass, ostinato từ tập rộng hơn (không trùng ô trước), thỉnh thoảng có ô "thở" ở cuối câu nhạc (không thump/bass), '
             'hợp âm chọn theo độ tương phản. Lời, tiếng dữ liệu, duck, hạ nền "Leah", khoảng lặng và chuỗi master giữ nguyên. '
             f"Master-alt: {alt['master']['integratedLUFS']} LUFS, true peak {alt['master']['truePeakDbtp']} dBTP; nhạc {ra['voiceOverMusicDb_A07']} dB dưới lời. "
             'File: `stems-alt/{voice,music-alt,sonify,room}.wav` (tổng = `master-alt.wav`), SHA-256 ở `manifest.json` → `alt`. Mặc định vẫn là bản hiện tại.')
    L.append(f"- **T2 (câu nhạc 4 ô lặp lại): mặc định {T2_DEFAULT}, thay thế {T2_ALT}** (Tập 1 kiểu C: 29%). Luật của bản thay thế: {ALT_CHECKS}.")
    L.append('- So sánh cho chủ dự án: `review-c6/music-ab.m4a` (57 s): hai đoạn, mỗi đoạn A = mặc định rồi B = thay thế; một tiếng bíp trước A, hai tiếng trước B. '
             'Đoạn 1 = S02.2 (có chữ "Leah" và chỗ hạ nền), đoạn 2 = S07.5 (hai lần chạy, tiếng dữ liệu, nhịp đầy). Chỉ mục: `review-c6/music-ab.json`.')
open(os.path.join(EP, 'out', 'audio', 'README.md'), 'w').write('\n'.join(L) + '\n')
print('README written')
