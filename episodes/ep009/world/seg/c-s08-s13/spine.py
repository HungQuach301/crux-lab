"""Tập 9 · ĐOẠN C = S08–S13 (chương 3 "The lights go out", hồi 2 phần 1). Lời + giờ = timeline nhà máy (kit.Seg).
B11 (S08.1): thẻ thuê N2 trên cửa Nina lật ra giá trị, dấu "assumption" → câu hỏi hồi 2 (S08.2) trên phố. B12 (S09.1–S09.2, thế giới): hai nhà mẫu — vốn
người mua (cọc LIT) lớn hơn đống cổ phiếu → cửa sổ sáng; đống lớn hơn → cửa tối. B13 (S09.3–S09.4): phố nhìn cao, 307 nhà, đầu/cuối; lô trống của Nina qua
cuối phố. B14 (S10): khối 1990s hiện, phần lớn sáng; nhà đầu tiên tối nhất. B15 (S11): 16 tháng quanh March 1999 ($1 ra dưới $1) vẫn sáng. B16 (S12):
2002–2007 tối hết; 6 bóng sáng (bản tiền mặt) tắt nốt. B17 (S13): nhà June 2006 nhấc lên: bóng chồng tiền mặt, rồi đống cổ phiếu cao hơn."""
import os, sys
HERE = globals().get('HERE_OVERRIDE') or os.path.dirname(os.path.abspath(__file__)); W9 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W9)
import kit as K
SV = K.SV
S = K.Seg(['S08', 'S09', 'S10', 'S11', 'S12', 'S13'])
B = [
 ('c0', 'S08.1', 'chart', 'Tiền thuê là giả định: thẻ 5% trên cửa Nina.', 'thẻ lật ra 5%, dấu "assumption".', {'tag': '@S08.1:tag', 'five': '@S08.1:five'}, ['xu'], 0.4, 'rõ', 'CHUYỂN CHẾ ĐỘ → thế giới'),
 ('c1', 'S08.2', 'world', 'Câu hỏi hồi 2: với cổ phiếu, bao nhiêu nhà còn sáng?', 'phố nhìn ngang, chưa sáng.', {'street': '@S08.2:street'}, [], 0.45, 'tò mò', 'lia máy'),
 ('c2', 'S09.1', 'world', 'Sáng = vốn người mua (sau phí bán) lớn hơn đống người thuê.', 'nhà mẫu 1: cọc vốn cao hơn đống; cửa sổ sáng.', {'lit': '@S09.1:lit', 'equity': '@S09.1:equity'}, ['tinh'], 0.45, 'rõ', '—'),
 ('c3', 'S09.2', 'world', 'Đống lớn hơn → cửa tối.', 'nhà mẫu 2: đống cao hơn; cửa tối.', {'dark': '@S09.2:dark'}, ['bịch'], 0.45, 'rõ', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('c4', 'S09.3', 'chart', '307 nhà, January 1991 → July 2016.', 'phố nhìn cao: nhà mọc trái → phải.', {'three': '@S09.3:houses', 'july': '@S09.3:July'}, ['gõ gỗ'], 0.45, 'rõ', '—'),
 ('c5', 'S09.4', 'chart', 'Tháng của Nina chưa có trên phố.', 'lô trống qua cuối phố, Nina + đèn.', {'nina': '@S09.4:Nina'}, [], 0.4, 'ấm', '—'),
 ('c6', 'S10.1', 'chart', 'Thập niên 1990: phần lớn sáng, khoảng 2/3.', 'khối 1990s hiện, đa số sáng.', {'most': '@S10.1:About', 'two': '@S10.1:two'}, ['tinh ×n'], 0.5, 'ấm', '—'),
 ('c7', 'S10.2', 'chart', 'Nhà tối nhất là nhà đầu tiên, January 1991.', 'nhà đầu tiên chớp, tối.', {'darkest': '@S10.2:darkest', 'first': '@S10.2:first'}, ['bịch'], 0.55, 'ngạc nhiên', '—'),
 ('c8', 'S10.3', 'chart', 'Người thuê đầu tiên đón trọn đợt cổ phiếu tăng.', 'giữ.', {'boom': '@S10.3:boom'}, [], 0.5, 'rõ', '—'),
 ('c9', 'S11.1', 'chart', 'Vài năm sau thị trường đứng yên.', 'khối 1999 sáng dần.', {'stalled': '@S11.1:stalled'}, [], 0.5, 'chậm', '—'),
 ('c10', 'S11.2', 'chart', 'Quanh March 1999, $1 cổ phiếu ra dưới $1 sau 10 năm.', '16 nhà quanh 1999 viền sáng.', {'short': '@S11.2:short', 'less': '@S11.2:less'}, ['tinh ×16'], 0.55, 'ngạc nhiên', '—'),
 ('c11', 'S11.3', 'chart', 'Những nhà đó vẫn sáng.', 'giữ sáng.', {'lit': '@S11.3:lit'}, [], 0.5, 'rõ', '—'),
 ('c12', 'S12.1', 'chart', 'Rồi phố tối, tối mãi.', '2000–2007 hiện: tối.', {'dark': '@S12.1:dark'}, ['chuỗi bịch'], 0.62, 'lạnh', '—'),
 ('c13', 'S12.2', 'chart', '2002–2007: người mua không hơn ở tháng nào.', 'khối 72 nhà tối hết.', {'none': '@S12.2:none'}, [], 0.68, 'lạnh', '—'),
 ('c14', 'S12.3', 'chart', 'Với tiền mặt có 6 nhà sáng; với cổ phiếu cũng tắt.', '6 bóng sáng (tiền mặt) tắt.', {'cash': '@S12.3:cash', 'out': '@S12.3:out'}, ['tắt ×6'], 0.66, 'lạnh', '—'),
 ('c15', 'S12.4', 'chart', 'Người mua đỉnh giá nhà; người thuê mua cổ phiếu qua đợt rơi.', 'giữ.', {'peak': '@S12.4:peak'}, [], 0.6, 'lạnh', 'đẩy máy'),
 ('c16', 'S13.1', 'chart', 'June 2006: nhà tối nhất lần trước (tiền mặt).', 'nhà June 2006 nhấc lên; bóng chồng tiền mặt.', {'june': '@S13.1:Last', 'cash': '@S13.1:cash'}, ['giấy'], 0.6, 'lạnh', '—'),
 ('c17', 'S13.2', 'chart', 'Với cổ phiếu kém hơn $250k.', 'đống cổ phiếu cao hơn bóng tiền mặt.', {'stocks': '@S13.2:stocks', 'quarter': '@S13.2:quarter'}, ['giấy dồn'], 0.66, 'nặng', '—'),
 ('c18', 'S13.3', 'chart', 'Nhà tối càng tối.', 'cửa tối thêm.', {'darker': '@S13.3:darker'}, ['bịch'], 0.6, 'nặng', '—'),
]
beats = SV.beats_from(B, S.A, S.lines)
cue = {b['id']: b['cues'] for b in beats}
moves = K.moves_of([
    ('m_w1', 'mode', 'cTag', 'wSide', cue['c0']['five'], cue['c1']['street'], 1.3, 'câu hỏi hồi 2: về phố (thế giới)', 'whoosh_mode', {}),
    ('m_demo', 'pan', 'wSide', 'wDemo', cue['c1']['street'], cue['c2']['lit'], 1.4, 'luật đèn trên hai nhà mẫu cạnh phố', 'whoosh_soft', {}),
    ('m_c1', 'mode', 'wDemo', 'cStreet', cue['c3']['dark'], cue['c4']['three'], 1.2, 'đếm cả phố: nhìn cao, số chỉ ở đồ thị', 'whoosh_mode', {}),
    ('m_n', 'pan', 'cStreet', 'cLot', cue['c4']['july'], cue['c5']['nina'], 1.3, 'tháng của Nina: lô trống qua cuối phố', 'whoosh_soft', {}),
    ('m_s', 'pan', 'cLot', 'cStreet', cue['c5']['nina'], cue['c6']['most'], 1.3, 'đi dọc phố từ 1991', 'whoosh_soft', {}),
    K.reframe(S, beats, 'm_r1', 'push', 'cStreet', 'cStreet~', 'S12.1:Then', 'phố tối: lại gần khối giữa phố'),
    ('m_06', 'pan', 'cStreet~', 'c2006', cue['c15']['peak'], cue['c16']['june'], 1.4, 'một nhà: June 2006 nhấc khỏi phố', 'whoosh_soft', {}),
])
ev = [{'t': cue['c0']['five'], 'kind': 'tick', 'v': 0.5}, {'t': cue['c2']['lit'], 'kind': 'data', 'v': 0.7}, {'t': cue['c3']['dark'], 'kind': 'data', 'v': 0.2},
      {'t': cue['c4']['three'], 'kind': 'rise', 'dur': 1.8}, {'t': cue['c6']['most'], 'kind': 'rise', 'dur': 1.6}, {'t': cue['c7']['first'], 'kind': 'data', 'v': 0.15},
      {'t': cue['c10']['less'], 'kind': 'data', 'v': 0.6}, {'t': cue['c12']['dark'], 'kind': 'rise', 'dur': 1.8}, {'t': cue['c13']['none'], 'kind': 'data', 'v': 0.1},
      {'t': cue['c14']['out'], 'kind': 'data', 'v': 0.2}, {'t': cue['c16']['cash'], 'kind': 'data', 'v': 0.35}, {'t': cue['c17']['quarter'], 'kind': 'data', 'v': 0.15},
      {'t': cue['c18']['darker'], 'kind': 'tick', 'v': 0.3}]
K.finish(HERE, S, 'ep009 · C = S08–S13 (chương 3, hồi 2 phần 1)', beats, moves, ev,
         {'chapter': [cue['c0']['tag'] - 1.2 if cue['c0']['tag'] > 1.5 else 0.3, 'The lights go out']},
         {'c0.five': 'rent tag: 5% of the price a year · July 2026 · assumption', 'c4.three': '307 start months', 'c4.july': 'January 1991 → July 2016',
          'c6.two': '1990s: about 2 in 3 lit', 'c7.first': 'darkest: January 1991', 'c10.less': '16 start months: $1 ended below $1 · all 16 stay lit',
          'c13.none': '2002 to 2007: none of 72', 'c14.cash': 'with cash: 6 of 72', 'c16.cash': 'June 2006 · with cash: $82,385 behind',
          'c17.quarter': 'with stocks: $261,689 behind'},
         [f"{b['id']}.{c}" for b in beats for c in b['cues']])
