// Tập 4 · G2 (b) — N2 (design/c3/n2.js, không đổi) + chế độ 'line': mẫu thư viện V3 `line` cộng nhãn nghĩa (§6.6, chỉ nhãn).
// Không thêm vật, không đổi màu: đường lãi, vạch trần, màu warn trên trần là của mẫu `line`; ở đây chỉ dời nhãn trần, hạ tiêu đề
// (để huy hiệu ILLUSTRATIVE ở đỉnh, không bị đẩy xuống đè đoạn cuối đường), thêm 2 mốc quý (beats.md B06 "two quarter markers") và
// một dòng đối trọng đứng suốt shot. Mọi số qua claim ({claimId}).
// p (ngoài tham số của `line`): levelSide 'left' (nhãn trần đầu trái vạch; tiêu đề hạ 16 px) · marks [{claim, text}] (mốc tại quý =
// value của claim, hiện khi đường tới quý đó) · note {text, x, y} (đối trọng đứng từ đầu shot).
// Chế độ 'bars': mẫu thư viện `bars` + dòng đơn vị p.unit trên tiêu đề (B09/B10: thanh là LÃI, trần là trên lãi).
// Shorts (E.V): giữ nguyên bố cục dọc của thư viện (bản vá C5); 'line' không thêm nhãn, 'bars' dùng p.titleV (tiêu đề ngắn có đơn vị) nếu có.
import { n2 as base } from '/episodes/ep004/design/c3/n2.js';
import { line as LINE, bars as BARS } from '/toolkit/factory/lib/templates.js';
import { ease, lin, mix } from '/toolkit/factory/lib/engine.js';

const at = (p, k, def = 0) => (typeof p[k] === 'number' ? p[k] : def);
const fade = (t, a0) => ease(t, a0, a0 + 0.4);
const num = (E, id) => { const v = E.claims[id].value; return typeof v === 'number' ? v : parseFloat(String(v).replace(/[^\d.-]/g, '')); };

function lineG2(E, t, p) {
  if (E.V) return LINE.draw(E, t, p);
  const left = p.levelSide === 'left';
  LINE.draw(E, t, left ? { ...p, title: undefined, levelAt: 1e9 } : p); // left: vạch + nhãn trần vẽ lại dưới đây
  const b = { x0: E.SAFE.x0 + 24, x1: E.SAFE.x1 - 24, y0: E.SAFE.y0 + 150, y1: E.SAFE.y1 - 110 };
  const S = p.series.split('.').reduce((o, k) => o?.[k], E.data), ys = S.map((r) => +r.y);
  const lvl = num(E, p.level), ymax = Math.max(...ys, lvl) * 1.1;
  const X = (i) => mix(b.x0 + 60, b.x1, i / (S.length - 1)), Y = (v) => mix(b.y1, b.y0, v / ymax);
  const a0 = at(p, 'at0'), a1 = at(p, 'at1', a0 + 4);
  if (p.note) E.text(p.note.text, p.note.x, p.note.y, 'note', { weight: 700, color: E.C.ink, plate: E.C.surface, group: 'g2-note' });
  if (left) {
    const la = at(p, 'levelAt', a0);
    if (p.title) E.text(p.title, b.x0, b.y0 - 24, 'caption', { alpha: fade(t, a0) });
    E.line([[b.x0 + 60, Y(lvl)], [b.x1, Y(lvl)]], E.C.muted, 6, fade(t, la));
    E.text(p.levelLabel || `{${p.level}}`, b.x0 + 60, Y(lvl) - 18, 'label', { color: E.C.ink, plate: E.C.surface, alpha: fade(t, la), group: 'lvl' });
  }
  (p.marks || []).forEach((m, j) => {
    const q = String(E.claims[m.claim].value).slice(0, 7), i = S.findIndex((r) => String(r.x).slice(0, 7) === q);
    if (i < 0) throw new Error('mark ' + m.claim + ': quarter ' + q + ' not in ' + p.series);
    const ta = a0 + (a1 - a0) * (i + 1) / S.length, a = fade(t, ta), x = X(i), y = Y(lvl), dy = 24 + 56 * j;
    if (a <= 0.01) return;
    E.line([[x, y], [x, y - dy - 4]], E.C.muted, 3, a);
    E.dot(x, y, 8, E.C.ink, a);
    E.text(m.text, x - 30, y - dy, 'note', { align: 'right', weight: 700, color: E.C.ink, alpha: a, group: 'g2-mark' + j });
  });
}

function barsG2(E, t, p) {
  if (E.V) return BARS.draw(E, t, p.titleV ? { ...p, title: p.titleV } : p); // Shorts: một tiêu đề ngắn có đơn vị (p.titleV)
  BARS.draw(E, t, p);
  if (p.unit) E.text(p.unit, E.SAFE.x0 + 24, E.SAFE.y0 + 56, 'note', { weight: 700, alpha: fade(t, at(p, 'at')), group: 'g2-unit' });
}

export const n2 = { draw(E, t, p, d, s) {
  return p.mode === 'line' ? lineG2(E, t, p) : p.mode === 'bars' ? barsG2(E, t, p) : base.draw(E, t, p, d, s); } };
