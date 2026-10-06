// Tập 4 · ký hiệu mới N1 "inflation shadow" (beats.md B08 · KEY-3, cảnh S08). Nạp qua custom_symbols của episode.yaml.
// Nghĩa: một số tiền cố định (trần $500,000, ink-muted liền, đứng yên) so với chính số tiền đó giữ sức mua (đường ĐỨT cùng màu, nâng theo
// CPI-U hằng tháng từ tháng 5/1997 tới tháng 8/2026 → "≈ $1,046,000 (Aug 2026 dollars)"). Cùng màu vì nó LÀ cái trần, tính lại;
// đứt để không đọc thành dữ liệu giá nhà. Chú thích "consumer prices, not house prices" luôn hiện khi bóng hiện; S08.4 phóng to 2 s.
// Trục giá trị từ 0. Mọi số đi qua claim ({claimId}); đường CPI vẽ từ DATA.cpi (data/CPIAUCNS.csv, cùng nguồn với model.py).
// p: at (đường trần vẽ vào), noteAt (nhãn "never adjusted"), at0/at1 (bóng chạy trái→phải), labelAt, footAt, bigAt (phóng chú thích).
import { ease, easeOut, lin, mix } from '/toolkit/factory/lib/engine.js';

const at = (p, k, def = 0) => (typeof p[k] === 'number' ? p[k] : def);
const fade = (t, a0) => ease(t, a0, a0 + 0.4);

export const n1 = { draw(E, t, p) {
  const cpi = E.data.cpi, cap = E.data.cap, base = cpi[0][1], n = cpi.length;
  const capC = E.C.cap || E.C.muted;
  const x0 = E.SAFE.x0 + 120, x1 = E.SAFE.x1 - 60, y0 = 300, y1 = 850;            // y1 = giá trị 0
  const vmax = cap * cpi[n - 1][1] / base * 1.12;
  const X = (i) => mix(x0, x1, i / (n - 1)), Y = (v) => mix(y1, y0, v / vmax);
  const a0 = at(p, 'at');
  // khung: tiêu đề, trục 0, mốc thời gian (tháng hiệu lực là claim; đầu phải không ghi năm)
  E.text(p.title || 'Joint tax-free cap on a home-sale gain', E.SAFE.x0 + 24, E.SAFE.y0 + 70, 'caption', { alpha: fade(t, a0), group: 'n1-title' });
  E.line([[x0, y1], [x1, y1]], E.C.grid, 4, fade(t, a0));
  E.text('0', x0 - 24, y1 + 16, 'note', { align: 'right', color: E.C.muted, alpha: fade(t, a0), group: 'n1-0' });
  E.text(`{${p.startClaim || 'exclusion_effective_month'}}`, x0, y1 + 56, 'note', { color: E.C.muted, alpha: fade(t, a0), group: 'n1-x0' });
  E.text(p.endLabel || 'today', x1, y1 + 56, 'note', { align: 'right', color: E.C.muted, alpha: fade(t, a0), group: 'n1-x1' });
  // trần: liền, ink-muted 10 px, vẽ vào rồi đứng yên
  const kc = easeOut(t, a0, a0 + 1.2);
  E.line([[x0, Y(cap)], [mix(x0, x1, kc), Y(cap)]], capC, 10, 1);
  E.text(`{${p.cap || 'excl_joint_limit_usd'}} cap`, x0 + 24, Y(cap) + 70, 'label', { alpha: fade(t, a0 + 0.3), group: 'n1-cap' });
  const na = at(p, 'noteAt', a0 + 1.5);
  E.text('a plain dollar amount, never adjusted', x0 + 24, Y(cap) + 132, 'note', { color: E.C.muted, alpha: fade(t, na), group: 'n1-never' });
  // bóng lạm phát: đứt, cùng màu, chạy theo CPI-U hằng tháng
  const s0 = at(p, 'at0', a0 + 3), s1 = at(p, 'at1', s0 + 4), k = lin(t, s0, s1);
  if (t >= s0) {
    const m = Math.max(2, Math.ceil(k * n)), pts = [];
    for (let i = 0; i < m; i++) pts.push([X(i), Y(cap * cpi[i][1] / base)]);
    E.line(pts, capC, 6, 1, [22, 16]);
    const [hx, hy] = pts[pts.length - 1];
    E.dot(hx, hy, 9, E.C.bg, 1, capC);
    E.historical();
  }
  const la = at(p, 'labelAt', s1);
  E.text(`{${p.shadow || 'excl_joint_1997_in_now'}}`, x1, Y(cap * cpi[n - 1][1] / base) - 40, 'number', { align: 'right', alpha: fade(t, la), group: 'n1-shadow' });
  E.text(`{${p.cap || 'excl_joint_limit_usd'}} kept up with consumer prices`, x1, Y(cap * cpi[n - 1][1] / base) + 50, 'note',
    { align: 'right', color: E.C.muted, alpha: fade(t, la + 0.3), group: 'n1-shadow2' });
  // chú thích: hiện cùng bóng, S08.4 phóng 48 → 64 px trong 2 s rồi về
  const fa = at(p, 'footAt', s0), ba = at(p, 'bigAt', 1e9);
  const big = ease(t, ba, ba + 0.4) * (1 - ease(t, ba + 2, ba + 2.4));
  E.text(p.foot || 'consumer prices (CPI-U), not house prices', x0 - 120 + 24, 962, mix(48, 64, big),
    { weight: big > 0.5 ? 700 : 600, color: big > 0.5 ? E.C.ink : E.C.muted, alpha: fade(t, fa), group: 'n1-foot' });
} };
