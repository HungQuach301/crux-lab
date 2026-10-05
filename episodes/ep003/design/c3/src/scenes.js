// Tập 3 · C3 style frames (một hướng: nền, màu E2, phông, ngữ pháp chuyển động của thư viện hình v1).
// Ký hiệu mới của tập: CHUỖI BILL vs CỔNG ×2 (KEY-1, KEY-3), DÒNG THỜI GIAN GIẢ ĐỊNH (KEY-2), ĐÀN CHẤM VỀ ĐÍCH
// (KEY-4, KEY-5, KEY-7), BÓNG GIÁ (KEY-6). Luật màu (một vai một màu, không thêm màu):
//   accent  = T-bill (chuỗi bill, chấm kết quả lăn T-bill)       ink-muted = cổng ×2 (mức cố định, KHÔNG BAO GIỜ di chuyển)
//   warn    = vượt ×2 (chấm nằm phải cổng) + huy hiệu ILLUSTRATIVE  costlier  = phần sức mua bị mất (chỉ là vật, không là chữ)
//   ink     = Dana, cột "gấp đôi", 17 tháng bảo đảm THẬT (đặc + viền)  sọc chéo ink-muted = giả định "IF today's guarantee had existed"
// Mọi số trên hình đi qua CL(claimId). Không quét ngược ở cuối nhịp; nhịp kết ở trạng thái kết luận, giữ yên ≥ 1 s.
import { C, W, H, CL, DATA, text, badge, line, rect, srect, roundRect, clamp, lin, ease, easeIn, easeOut, back, mix, inout, rgba, measureText } from './engine.js';

const WIN = DATA.windows, NW = WIN.length;
const CLD = (id) => { const c = DATA.claims[id]; CL(id); return c; };
const year = (id) => CLD(id).year;

// ---------- shared marks ----------
function hatch(ctx, x, y, w, h, a = 1, gap = 18, color = C.muted, lw = 3) {
  if (a <= 0 || w <= 0 || h <= 0) return;
  ctx.save(); ctx.beginPath(); ctx.rect(x, y, w, h); ctx.clip(); ctx.globalAlpha = a; ctx.strokeStyle = color; ctx.lineWidth = lw;
  ctx.beginPath(); for (let k = -h; k < w + h; k += gap) { ctx.moveTo(x + k, y + h); ctx.lineTo(x + k + h, y); } ctx.stroke(); ctx.restore();
}
// fixed label of the episode: every pre-May-2005 result carries it
function ifLabel(ctx, a = 1, x = 96, y = 122) {
  if (a <= 0) return;
  hatch(ctx, x, y - 40, 48, 48, a, 12, C.muted, 3); srect(ctx, x, y - 40, 48, 48, C.muted, 2, a);
  text(ctx, CLD('ctx_hypothetical').display, x + 68, y, 'note', { color: C.ink, alpha: a, group: 'iflab' });
}
// ---------- C3 vòng 2 (ý đồ v2, §6.6): nhãn đối trọng / nhãn nghĩa — chỉ chữ, không thêm vật, không thêm số ngoài claim ----------
export const R2 = new URLSearchParams(location.search).get('r') === '2';
function r2label(ctx, s, x, y, t, t0, o = {}) { // ≥ 1 s cho mỗi 3 từ: hiện từ t0 tới hết nhịp
  if (!R2) return;
  text(ctx, s, x, y, o.tier || 'label', { weight: 700, color: o.color || C.ink, plate: o.plate === undefined ? C.surface : o.plate, alpha: ease(t, t0, t0 + 0.4), align: o.align, group: 'r2' + y });
}
function gateV(ctx, x, y0, y1, a = 1, lw = 10) { if (a > 0) line(ctx, [[x, y0], [x, y1]], C.muted, lw, { alpha: a, cap: 'butt' }); }
function dot(ctx, x, y, r, fill, a = 1, ringC = null) {
  if (a <= 0) return; ctx.save(); ctx.globalAlpha = a; ctx.beginPath(); ctx.arc(x, y, r, 0, 7); ctx.fillStyle = fill; ctx.fill();
  if (ringC) { ctx.lineWidth = 3; ctx.strokeStyle = ringC; ctx.beginPath(); ctx.arc(x, y, r + 4, 0, 7); ctx.stroke(); }
  ctx.restore();
}
function arrowR(ctx, x0, x1, y, color, a = 1, lw = 5) {
  if (a <= 0) return; line(ctx, [[x0, y], [x1, y]], color, lw, { alpha: a });
  line(ctx, [[x1 - 18, y - 14], [x1, y], [x1 - 18, y + 14]], color, lw, { alpha: a });
}

// ---------- Dana (ILLUSTRATIVE): faceless ink figure, envelope "Later" ----------
function dana(ctx, cx, base, s = 1, a = 1, look = 0) {
  if (a <= 0) return;
  ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = C.ink;
  ctx.beginPath(); ctx.moveTo(cx - 120 * s, base); ctx.lineTo(cx - 120 * s, base - 140 * s);
  ctx.bezierCurveTo(cx - 120 * s, base - 230 * s, cx - 70 * s, base - 262 * s, cx, base - 262 * s);
  ctx.bezierCurveTo(cx + 70 * s, base - 262 * s, cx + 120 * s, base - 230 * s, cx + 120 * s, base - 140 * s);
  ctx.lineTo(cx + 120 * s, base); ctx.closePath(); ctx.fill();
  ctx.beginPath(); ctx.arc(cx + look * 14 * s, base - 345 * s, 64 * s, 0, 7); ctx.fill();
  ctx.restore();
}
function envelope(ctx, x, y, a = 1) {
  if (a <= 0) return;
  ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = C.surface; ctx.strokeStyle = C.ink; ctx.lineWidth = 4;
  roundRect(ctx, x, y, 210, 128, 10); ctx.fill(); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(x + 4, y + 6); ctx.lineTo(x + 105, y + 66); ctx.lineTo(x + 206, y + 6); ctx.stroke(); ctx.restore();
  text(ctx, 'Later', x + 105, y + 112, 'note', { align: 'center', weight: 700, alpha: a });
}

// ---------- the two paths (KEY-1, KEY-3) ----------
const P = { x0: 560, x1: 1540, yBond: 400, yBill: 720, linkH: 64 };
const linkX = (k) => P.x0 + (P.x1 - P.x0) * k / 80;
function chain(ctx, n, a = 1, o = {}) { // n links visible (0..80); link o.cur (default 0) lit in accent = where the money is now
  if (a <= 0) return;
  const lw = (P.x1 - P.x0) / 80;
  for (let k = 0; k < Math.min(80, Math.ceil(n)); k++) {
    const f = clamp(n - k), x = linkX(k), y = P.yBill - P.linkH / 2;
    const lit = k === (o.cur ?? 0);
    ctx.save(); ctx.globalAlpha = a * f;
    roundRect(ctx, x + 1.5, y, lw - 3, P.linkH, 4);
    if (lit) { ctx.fillStyle = C.accent; ctx.fill(); } else { ctx.strokeStyle = C.muted; ctx.lineWidth = 2; ctx.stroke(); }
    ctx.restore();
  }
}
function bondBar(ctx, f, a = 1, o = {}) { // single bar from x0 toward the gate at year 20; f = 0..1 drawn
  if (a <= 0) return;
  const h = 64, y = P.yBond - h / 2, x1 = mix(P.x0, P.x1, f);
  srect(ctx, P.x0, y, P.x1 - P.x0, h, C.muted, 3, a * 0.5, [10, 10]);
  rect(ctx, P.x0, y, x1 - P.x0, h, C.ink, a * (o.fillA ?? 0.85));
}
function gateAt(ctx, x, y, a = 1, lab = true) {
  if (a <= 0) return;
  gateV(ctx, x, y - 92, y + 92, a, 12);
  if (lab) text(ctx, CLD('ctx_guarantee').display, x + 28, y + 26, 'number', { color: C.ink, alpha: a, group: 'gate' });
}

// ---------- KEY-1: one saver, two paths ----------
export const KEY1 = {
  duration: 10, stripTimes: [0.6, 2.2, 3.8, 5.4, 7.2, 9.3],
  draw(ctx, t) {
    const aD = ease(t, 0, 0.5);
    dana(ctx, 250, 1010, 1.3, aD, ease(t, 6.6, 7.4));
    envelope(ctx, 145, 860, ease(t, 0.3, 0.8));
    badge(ctx, undefined, undefined, aD);
    // the bill path: money hops from bill to bill (chain grows left to right = time)
    const nLinks = 80 * easeIn(t, 1.0, 4.6) ** 0.85;
    const cur = t > 1.0 && t < 4.7 ? Math.min(79, Math.floor(nLinks)) : 0;
    chain(ctx, nLinks, ease(t, 0.9, 1.2), { cur });
    if (t > 1.0 && t < 4.7) dot(ctx, linkX(cur) + 6, P.yBill - P.linkH / 2 - 26, 13, C.accent, 1);
    arrowR(ctx, 420, P.x0 - 24, P.yBill, C.muted, ease(t, 0.9, 1.3));
    text(ctx, CL('bill_term_months') + '-month T-bills, one after another', P.x0, P.yBill + 104, 'label', { alpha: ease(t, 1.2, 1.7) });
    text(ctx, CL('bills_per_horizon') + ' bills', P.x1, P.yBill - 70, 'label', { align: 'right', color: C.muted, alpha: ease(t, 4.4, 4.9) });
    // the bond path: one bar to a fixed gate ×2 at year 20
    const fB = ease(t, 4.8, 7.4);
    bondBar(ctx, fB, ease(t, 4.6, 5.0));
    arrowR(ctx, 420, P.x0 - 24, P.yBond, C.muted, ease(t, 4.6, 5.0));
    gateAt(ctx, P.x1, P.yBond, ease(t, 4.7, 5.1));
    text(ctx, 'Savings bond: guaranteed', P.x0, P.yBond - 70, 'label', { alpha: ease(t, 4.9, 5.4) });
    text(ctx, 'at year ' + CL('horizon_years'), P.x1 + 28, P.yBond + 104, 'note', { color: C.muted, alpha: ease(t, 5.2, 5.7) });
    // time axis
    const aT = ease(t, 1.0, 1.5);
    line(ctx, [[P.x0, 880], [P.x1, 880]], C.grid, 4, { alpha: aT });
    text(ctx, 'today', P.x0, 950, 'note', { color: C.muted, alpha: aT });
    text(ctx, CL('horizon_years') + ' years', P.x1, 950, 'note', { color: C.muted, align: 'right', alpha: aT });
    // the question, held at the end (no path highlighted)
    text(ctx, 'Which path ends with more?', P.x0, 210, 'head', { alpha: ease(t, 7.8, 8.4) });
    r2label(ctx, 'Not a pick. Two rules, side by side.', P.x0, 1046, t, 4.0);
  },
};

// ---------- KEY-2: the what-if timeline ----------
const TL = { x0: 160, x1: 1760, y: 560, h: 150 };
const gIdx = WIN.findIndex((w) => w.s >= DATA.claims.guarantee_from.value.slice(0, 7));
const tx = (i) => TL.x0 + (TL.x1 - TL.x0) * i / NW;
export const KEY2 = {
  duration: 10, stripTimes: [0.8, 2.3, 3.8, 5.3, 7.0, 9.3],
  draw(ctx, t) {
    text(ctx, 'Every start month we replay', 160, 230, 'caption', { alpha: ease(t, 0.1, 0.6) });
    const n = NW * ease(t, 0.4, 2.6);
    // one tick per start month, drawn left to right
    for (let i = 0; i < Math.min(NW, n); i++) {
      const real = i >= gIdx, x = tx(i);
      const lit = real ? ease(t, 5.6, 6.2) : 0;
      rect(ctx, x, TL.y - TL.h / 2, Math.max(1.2, tx(1) - tx(0) - 0.4), TL.h, real ? (lit > 0.5 ? C.ink : C.accent) : C.accent, real ? mix(0.55, 1, lit) : 0.55);
    }
    text(ctx, year('first_start'), TL.x0, TL.y + TL.h / 2 + 90, 'label', { color: C.muted, alpha: ease(t, 0.6, 1.0) });
    text(ctx, year('last_start'), TL.x1, TL.y + TL.h / 2 + 90, 'label', { color: C.muted, align: 'right', alpha: ease(t, 2.4, 2.8) });
    // hatched wash over everything before May 2005
    const hx1 = tx(gIdx) - 3, fH = ease(t, 3.0, 4.6);
    hatch(ctx, TL.x0, TL.y - TL.h / 2 - 20, (hx1 - TL.x0) * fH, TL.h + 40, 0.9, 22, C.ink, 4);
    srect(ctx, TL.x0, TL.y - TL.h / 2 - 20, (hx1 - TL.x0) * fH, TL.h + 40, C.ink, 3, ease(t, 3.0, 3.4));
    const aIf = ease(t, 4.2, 4.8);
    text(ctx, CLD('ctx_hypothetical').display, 200, TL.y - TL.h / 2 - 56, 'caption', { weight: 700, alpha: aIf });
    text(ctx, CL('starts_hypothetical') + ' start months: what-if', 200, TL.y + TL.h / 2 + 170, 'label', { color: C.ink, alpha: ease(t, 4.6, 5.1) });
    // the short real stretch, outlined
    const aR = ease(t, 5.6, 6.2), rx = tx(gIdx), rw = tx(NW) - rx;
    srect(ctx, rx - 8, TL.y - TL.h / 2 - 28, rw + 16, TL.h + 56, C.ink, 5, aR);
    line(ctx, [[rx + rw / 2, TL.y - TL.h / 2 - 34], [rx + rw / 2, 330]], C.ink, 4, { alpha: aR });
    text(ctx, 'REAL guarantee: ' + CL('starts_with_guarantee') + ' months', TL.x1, 310, 'label', { align: 'right', weight: 700, alpha: aR });
    text(ctx, 'from ' + CLD('guarantee_from').display, TL.x1, 250, 'note', { align: 'right', color: C.muted, alpha: ease(t, 6.0, 6.5) });
    // the label moves to its fixed corner and stays (as it will on every pre-2005 result)
    ifLabel(ctx, ease(t, 7.6, 8.2));
    r2label(ctx, 'Not a pick. What history did.', 160, 1000, t, 4.0);
  },
};

// ---------- the finish-line swarm (KEY-4, KEY-5) ----------
const SW = { x0: 200, x1: 1480, m0: 1.0, m1: 4.8, bin: 0.04 };
const mx = (m) => SW.x0 + (m - SW.m0) / (SW.m1 - SW.m0) * (SW.x1 - SW.x0);
const GX = mx(2);
const ERA = (s) => (s < '1950' ? 0 : s < '1990' ? 1 : 2);
// positions: full swarm stacked up from a baseline; era rows stacked symmetric about each row's centre
const full = [], rows = [];
{
  const cnt = {}, cntE = [{}, {}, {}];
  WIN.forEach((w, i) => {
    const b = Math.floor((w.roll - SW.m0) / SW.bin), xb = mx(SW.m0 + (b + 0.5) * SW.bin);
    const k = cnt[b] = (cnt[b] || 0) + 1; full[i] = [xb, k];
    const e = ERA(w.s), ke = cntE[e][b] = (cntE[e][b] || 0) + 1; rows[i] = [xb, e, ke];
  });
}
const FULL = { base: 900, step: 10.5, r: 5 };
const ROWY = [430, 680, 930], ROWSTEP = 5.2;
const fullXY = (i) => [full[i][0], FULL.base - (full[i][1] - 0.5) * FULL.step];
const rowXY = (i) => { const [x, e, k] = rows[i]; return [x, ROWY[e] - 6 - (k - 0.5) * ROWSTEP]; };
function swarmAxis(ctx, base, a = 1) {
  if (a <= 0) return;
  line(ctx, [[SW.x0, base], [SW.x1, base]], C.grid, 4, { alpha: a });
}
const dropT = (i) => 1.2 + 3.0 * i / NW; // chronological rain
function eraText(ctx, e) { return e === 0 ? year('early_from') + '–' + year('early_to') : e === 1 ? year('mid_from') + '–' + year('mid_to') : year('since_1990_from') + '–' + year('last_start'); }

export const KEY4 = {
  duration: 12, stripTimes: [0.8, 3.0, 5.0, 6.9, 8.8, 11.3],
  draw(ctx, t) {
    ifLabel(ctx, ease(t, 0.0, 0.4));
    text(ctx, 'Each dot: one ' + CL('horizon_years') + '-year roll of T-bills', 96, 200, 'label', { color: C.muted, alpha: inout(t, 0.2, 0.7, 6.4, 6.9) });
    const sp = ease(t, 6.6, 8.4); // split into eras
    swarmAxis(ctx, FULL.base + 14, 1 - sp);
    gateV(ctx, GX, mix(300, 250, sp), mix(FULL.base + 40, ROWY[2] + 20, sp), ease(t, 0.3, 0.8), 10);
    text(ctx, CLD('ctx_guarantee').display + ' (the bond)', GX, 282, 'label', { align: 'center', weight: 700, alpha: ease(t, 0.4, 0.9) * (1 - sp) });
    for (let i = 0; i < NW; i++) {
      const td = dropT(i); if (t < td) continue;
      const f = easeOut(t, td, td + 0.35);
      const [fx, fy] = fullXY(i), [rx, ry] = rowXY(i);
      const x = mix(fx, rx, sp), y = mix(mix(150, fy, f), ry, sp);
      const right = WIN[i].roll > 2, colr = ease(t, 4.6, 5.2);
      dot(ctx, x, y, mix(FULL.r, 3.4, sp), right && colr > 0.5 ? C.warn : C.accent, f * (right ? 1 : 0.9));
    }
    // extremes labelled
    const aE = inout(t, 4.3, 4.7, 6.3, 6.6);
    text(ctx, CL('min_tbill_multiple_20y'), SW.x0, FULL.base + 84, 'label', { alpha: aE });
    text(ctx, CL('max_tbill_multiple_20y'), SW.x1 + 20, FULL.base + 84, 'label', { align: 'right', alpha: aE });
    text(ctx, 'times the money after ' + CL('horizon_years') + ' years', (SW.x0 + SW.x1) / 2, FULL.base + 84, 'note', { align: 'center', color: C.muted, alpha: aE });
    // the overall share, then three era rows each with its own number
    const a1 = inout(t, 5.0, 5.5, 6.4, 6.8);
    if (a1 > 0) { const w = text(ctx, CL('share_tbills_above_double_pct'), 900, 380, 'hero', { color: C.warn, alpha: a1, group: 'all' }).x1; text(ctx, 'beat ' + CLD('ctx_guarantee').display, w + 30, 370, 'caption', { alpha: a1, group: 'all' }); }
    text(ctx, CL('share_tbills_above_double_pct') + ' overall', 1824, 122, 'label', { align: 'right', color: C.warn, alpha: ease(t, 6.4, 6.9) });
    const aR = ease(t, 8.0, 8.6);
    const shares = ['share_above_double_1934_1949_pct', 'share_above_double_1950_1989_pct', 'share_tbills_above_double_starts_since_1990_pct'];
    r2label(ctx, 'Not a pick. What history did.', 200, 1046, t, 4.8);
    for (let e = 0; e < 3; e++) {
      line(ctx, [[SW.x0, ROWY[e]], [SW.x1, ROWY[e]]], C.grid, 3, { alpha: aR }); text(ctx, eraText(ctx, e), SW.x1 + 40, ROWY[e] - 140, 'note', { color: C.muted, alpha: aR, group: 'era' + e });
      const ae = ease(t, 8.6 + 0.5 * e, 9.0 + 0.5 * e);
      text(ctx, CL(shares[e]), SW.x1 + 40, ROWY[e] - 50, 'number', { color: e === 1 ? C.warn : C.ink, alpha: ae, group: 'n' + e });
      text(ctx, 'beat ' + CLD('ctx_guarantee').display, SW.x1 + 40, ROWY[e] + 6, 'note', { color: C.muted, alpha: ae, group: 'n' + e });
    }
  },
};

// ---------- KEY-5: the only real-guarantee starts ----------
export const KEY5 = {
  duration: 10, stripTimes: [0.6, 2.2, 3.8, 5.4, 7.2, 9.3],
  draw(ctx, t) {
    ifLabel(ctx, 1 - ease(t, 2.0, 2.6) * 0.0);
    gateV(ctx, GX, 250, ROWY[2] + 20, 1, 10);
    text(ctx, CLD('ctx_guarantee').display + ' (the bond)', GX, 230, 'label', { align: 'center', weight: 700 });
    for (let e = 0; e < 3; e++) line(ctx, [[SW.x0, ROWY[e]], [SW.x1, ROWY[e]]], C.grid, 3, { alpha: e === 2 ? 1 : mix(1, 0.04, ease(t, 0.8, 2.0)) });
    const fo = ease(t, 0.8, 2.0); // other rows fade back
    const rl = ease(t, 2.0, 3.2); // real ones light up
    for (let i = 0; i < NW; i++) {
      const [x, y] = rowXY(i), e = ERA(WIN[i].s), real = i >= gIdx;
      if (real) continue;
      dot(ctx, x, y, 3.4, WIN[i].roll > 2 ? C.warn : C.accent, e === 2 ? mix(0.9, 0.6, fo) : mix(0.9, 0.0, fo));
    }
    for (let i = gIdx; i < NW; i++) { // 17 real-guarantee starts: solid ink + ring, pulled up into one tight cluster
      const [x, y] = rowXY(i), k = i - gIdx;
      const cx = mx(WIN[i].roll), cy = 700 - (k % 6) * 0 - 0;
      const px = mix(x, cx + ((k % 3) - 1) * 24, ease(t, 3.4, 4.6)), py = mix(y, 640 + (Math.floor(k / 3) - 2.5) * 24, ease(t, 3.4, 4.6));
      dot(ctx, px, py, mix(3.4, 8, rl), rl > 0.5 ? C.ink : C.accent, 1, rl > 0.5 ? C.ink : null);
    }
    for (let e = 0; e < 3; e++) text(ctx, eraText(ctx, e), SW.x1 + 40, ROWY[e] - 140, 'note', { color: C.muted, alpha: e === 2 ? 1 : mix(1, 0.35, fo), group: 'era' + e });
    const aR = ease(t, 3.0, 3.5);
    text(ctx, 'REAL guarantee', 620, 600, 'caption', { weight: 700, alpha: aR });
    text(ctx, 'none of ' + CL('starts_with_guarantee') + ' beat ' + CLD('ctx_guarantee').display, 620, 670, 'label', { alpha: ease(t, 4.8, 5.3) });
    text(ctx, CL('min_multiple_guarantee_starts') + ' to ' + CL('max_multiple_guarantee_starts'), 620, 730, 'note', { color: C.ink, alpha: ease(t, 5.4, 5.9) });
    // tag on the cluster + overall share stays in the corner
    const aS = ease(t, 6.4, 6.9);
    text(ctx, 'small sample · one era', 620, 500, 'label', { color: C.bg, weight: 700, plate: C.ink, alpha: aS });
    const aO = ease(t, 0.2, 0.6);
    text(ctx, CL('share_tbills_above_double_pct') + (R2 ? ' of all rolls beat ' + CLD('ctx_guarantee').display : ' overall'), 1824, 122, 'label', { align: 'right', color: C.warn, alpha: aO });
    r2label(ctx, 'Not a pick. What history did.', 200, 1046, t, 4.0);
  },
};

// ---------- KEY-6: the price shadow ----------
const W66 = WIN.findIndex((w) => w.s === DATA.claims.worst_real_start.value.slice(0, 7));
const CPI = new Map(DATA.cpi);
const addM = (s, n) => { let y = +s.slice(0, 4), m = +s.slice(5, 7) - 1 + n; y += Math.floor(m / 12); m = ((m % 12) + 12) % 12; return `${y}-${String(m + 1).padStart(2, '0')}`; };
export const KEY6 = {
  duration: 12, stripTimes: [0.7, 2.6, 4.4, 6.2, 8.4, 11.3],
  draw(ctx, t) {
    // left: one start (the worst), dollars bar vs price shadow, both from the same base
    const s0 = WIN[W66].s, B = 930, U = 150, BX = 330, BW = 150;
    const k = Math.round(240 * ease(t, 0.8, 4.6));
    const shadow = CPI.get(addM(s0, k)) / CPI.get(s0), dollars = Math.pow(2, k / 240);
    const aL = ease(t, 0.0, 0.4);
    line(ctx, [[BX - 60, B], [BX + 2 * BW + 100, B]], C.grid, 4, { alpha: aL });
    // shadow: what the original money bought, priced in each year's dollars
    ctx.save(); ctx.globalAlpha = aL; ctx.fillStyle = rgba(C.muted, 0.18); ctx.fillRect(BX + 40, B - shadow * U, BW, shadow * U); ctx.restore();
    srect(ctx, BX + 40, B - shadow * U, BW, shadow * U, C.muted, 4, aL, [14, 10]);
    // the doubled dollars, in front, slightly left
    rect(ctx, BX - 20, B - dollars * U, BW, dollars * U, C.ink, aL);
    // the shortfall: the part of the shadow the doubled stack can't reach
    const aG = ease(t, 4.8, 5.4);
    if (shadow > dollars) rect(ctx, BX + 40 + BW - 26, B - shadow * U, 26, (shadow - dollars) * U, C.costlier, aG);
    text(ctx, CLD('ctx_guarantee').display + ' dollars', BX - 44, B - dollars * U + 44, 'label', { align: 'right', alpha: ease(t, 1.0, 1.5), group: 'bar' });
    text(ctx, 'what the original', BX + 40 + BW + 22, B - shadow * U + 36, 'note', { color: C.ink, alpha: ease(t, 1.2, 1.7), group: 'sh' });
    text(ctx, 'money bought', BX + 40 + BW + 22, B - shadow * U + 90, 'note', { color: C.ink, alpha: ease(t, 1.2, 1.7), group: 'sh' });
    text(ctx, 'start ' + CLD('worst_real_start').display, BX - 20, B + 64, 'note', { color: C.muted, alpha: aL });
    const aW = ease(t, 5.0, 5.6);
    text(ctx, CLD('ctx_guarantee').display + ' bought ' + CL('worst_real_value_double_pct'), 96, 200, 'caption', { weight: 700, alpha: aW, group: 'w' });
    text(ctx, 'of what the original bought', 96, 262, 'note', { alpha: aW, group: 'w' });
    // right: every start, buying power of the double vs the original (line = kept up)
    const RX0 = 960, RX1 = 1800, RB = 640, RU = 300, nr = ease(t, 6.0, 9.0);
    const real = WIN.filter((w) => w.real != null);
    const aRt = ease(t, 5.8, 6.3);
    for (let i = 0; i < real.length * nr; i++) {
      const w = real[i], x = RX0 + (RX1 - RX0) * i / real.length, v = w.real - 1;
      rect(ctx, x, v >= 0 ? RB - v * RU : RB, Math.max(1, (RX1 - RX0) / real.length), Math.abs(v) * RU, v >= 0 ? C.ink : C.costlier, aRt * (v >= 0 ? 0.8 : 1));
    }
    line(ctx, [[RX0, RB], [RX1, RB]], C.muted, 5, { alpha: aRt, cap: 'butt' });
    text(ctx, 'kept up with prices', RX0, RB - 170, 'note', { color: C.ink, alpha: ease(t, 6.4, 6.9) });
    text(ctx, 'fell behind', RX0, RB + 190, 'note', { color: C.ink, alpha: ease(t, 6.4, 6.9) });
    text(ctx, year('first_start'), RX0, RB + 280, 'note', { color: C.muted, alpha: aRt });
    text(ctx, year('last_start'), RX1, RB + 280, 'note', { color: C.muted, align: 'right', alpha: aRt });
    text(ctx, 'each bar: one start, ' + CLD('ctx_guarantee').display + ' after ' + CL('horizon_years') + ' years', RX0, 262, 'note', { color: C.muted, alpha: aRt });
    const aN = ease(t, 9.4, 10.0);
    const w = text(ctx, CL('share_double_beat_prices_pct'), RX0, 190, 'number', { alpha: aN, group: 'n' }).x1;
    text(ctx, 'of starts kept up', w + 24, 186, 'label', { alpha: aN, group: 'n' });
    if (R2) ifLabel(ctx, 1); else ifLabel(ctx, 1, 960, 1040);
    r2label(ctx, 'Not a pick. What history did.', 960, 1046, t, 5.0);
  },
};

// ---------- KEY-7: the line on the bill-rate scale ----------
const RS = { x0: 200, x1: 1760, r0: 0, r1: 8.0, base: 760 };
const rxs = (r) => RS.x0 + (r - RS.r0) / (RS.r1 - RS.r0) * (RS.x1 - RS.x0);
const AV = [];
{ const cnt = {}; WIN.forEach((w, i) => { const b = Math.floor(w.avg / 0.1); const k = cnt[b] = (cnt[b] || 0) + 1; AV[i] = [rxs((b + 0.5) * 0.1), k]; }); }
// visiting order of the swinging marker: a deterministic shuffle, so it lands on both sides
const ORDER = [...Array(NW).keys()].map((i) => [((i * 7919) % NW), i]).sort((a, b) => a[0] - b[0]).map((p) => p[1]);
const RANK = []; ORDER.forEach((i, r) => { RANK[i] = r; });
export const KEY7 = {
  duration: 12, stripTimes: [0.8, 2.6, 4.4, 6.4, 8.6, 11.3],
  draw(ctx, t) {
    const aA = ease(t, 0.1, 0.5), BE = rxs(DATA.breakeven), MN = rxs(DATA.claims.mean_tb3ms_all_pct.value);
    line(ctx, [[RS.x0, RS.base], [RS.x1, RS.base]], C.grid, 4, { alpha: aA });
    text(ctx, 'average T-bill rate over ' + CL('horizon_years') + ' years', (RS.x0 + RS.x1) / 2, RS.base + 160, 'note', { align: 'center', color: C.muted, alpha: aA });
    // the line (gate) and the long-run average just under it
    gateV(ctx, BE, 400, RS.base + 20, ease(t, 0.6, 1.1), 10);
    text(ctx, CL('steady_breakeven_tb3ms_pct') + ' = ' + CLD('ctx_guarantee').display + ' in ' + CL('horizon_years') + ' years', BE + 24, 420, 'label', { weight: 700, alpha: ease(t, 1.0, 1.5) });
    text(ctx, 'on the bill-rate scale', BE + 24, 476, 'note', { color: C.muted, alpha: ease(t, 1.2, 1.7) });
    const aM = ease(t, 1.8, 2.3);
    line(ctx, [[MN, RS.base], [MN, RS.base + 52]], C.ink, 5, { alpha: aM });
    text(ctx, CL('mean_tb3ms_all_pct') + ' average since ' + year('first_start'), MN - 12, RS.base + 96, 'note', { align: 'right', alpha: aM });
    // every 20-year average lands as a dot; the marker swings to both sides
    const n = NW * easeIn(t, 3.0, 8.6);
    const cur = Math.min(NW - 1, Math.floor(n));
    for (let i = 0; i < NW; i++) {
      if (RANK[i] > n) continue;
      const [x, k] = AV[i]; const right = WIN[i].avg > DATA.breakeven;
      dot(ctx, x, RS.base - 14 - (k - 0.5) * 8, 4, right ? C.warn : C.accent, 0.95);
    }
    if (t > 3.0 && t < 8.8) { const i = ORDER[cur]; const x = AV[i][0]; line(ctx, [[x, 520], [x, RS.base - 4]], C.ink, 4, { alpha: 0.9 }); dot(ctx, x, 520, 14, C.ink, 1); }
    const aS = ease(t, 4.0, 4.6);
    text(ctx, 'roll beat ' + CLD('ctx_guarantee').display, RS.x1, 290, 'caption', { align: 'right', color: C.warn, alpha: aS });
    text(ctx, 'roll fell short', RS.x0, 290, 'caption', { color: C.accent, alpha: aS });
    text(ctx, 'each dot: one start, the average of its ' + CL('bills_per_horizon') + ' bills', RS.x0, 190, 'note', { color: C.muted, alpha: ease(t, 3.0, 3.5) });
    // today's single month, fading: it is not the 20-year average
    const aT = inout(t, 9.0, 9.5, 10.6, 11.4) * 0.9 + ease(t, 10.6, 11.4) * 0.35;
    const TX = rxs(DATA.claims.tb3ms_latest_pct.value);
    dot(ctx, TX, RS.base + 40, 10, C.accent, aT, C.ink);
    text(ctx, 'one month: ' + CL('tb3ms_latest_pct'), TX + 30, RS.base + 56, 'note', { alpha: aT });
    ifLabel(ctx, 1);
    r2label(ctx, 'Beat ' + CLD('ctx_guarantee').display + ' = average right of the line', 1824, 122, t, 3.4, { align: 'right', tier: 'note', plate: C.bg });
    r2label(ctx, 'What the roll must do. Not a pick.', 200, 1046, t, 4.6);
  },
};

// ---------- KEY-3 (type 2): today's single bill rate is not the doubling line ----------
export const KEY3 = {
  duration: 8, stripTimes: [0.5, 1.8, 3.1, 4.4, 5.8, 7.4],
  draw(ctx, t) {
    chain(ctx, 80, 1);
    text(ctx, CL('tb3ms_latest_pct') + ' · ' + CLD('tb3ms_latest_month').display, P.x0, P.yBill - 56, 'label', { alpha: 1 });
    bondBar(ctx, 1, 0.6, { fillA: 0.5 }); gateAt(ctx, P.x1, P.yBond, 1, true);
    const sl = ease(t, 1.0, 2.4);
    // the first link slides up toward the gate, stops halfway, and a "≠" appears
    const lx = mix(P.x0, 1080, sl), ly = mix(P.yBill, 620, sl);
    rect(ctx, lx, ly - P.linkH / 2, (P.x1 - P.x0) / 80 * 3, P.linkH, C.accent, sl > 0 ? 1 : 0);
    const aN = ease(t, 2.8, 3.3);
    text(ctx, '≠', 1220, 650, 'hero', { align: 'center', alpha: aN });
    text(ctx, 'measured differently', 1300, 600, 'label', { alpha: ease(t, 3.4, 3.9) });
    text(ctx, 'one month, not ' + CL('horizon_years') + ' years', 1300, 666, 'label', { alpha: ease(t, 4.4, 4.9) });
    text(ctx, '?', (P.x0 + P.x1) / 2, P.yBill + 150, 'number', { align: 'center', color: C.muted, alpha: ease(t, 5.4, 6.0) });
    r2label(ctx, 'Not a pick. Not a forecast.', P.x0, 1046, t, 3.2);
  },
};
