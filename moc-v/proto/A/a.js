// Mốc V · Hướng A — "vật thể thật 2D" (G-012a): nhà của Rosa & Frank đứng trên CHỒNG TIỀN (cao ∝ đô la), trần $500,000 là XÀ THÉP,
// thời gian là LỊCH XÉ; khu phố nhiều nhà "SOLD" = nhiều giao dịch. Cùng trục xương sống và thang đô la với hướng C; khác ngôn ngữ hình.
import { C, clamp, lin, ease, easeOut, easeBack, mix, rgba, loadAll, makeCtx, chrome, person, house, roundRect } from '../lib2d.js';

const S = await loadAll();
const { cue, interp, gain, at, CL, spine } = S;
const canvas = document.getElementById('c');
const K = makeCtx(canvas), { ctx, text } = K;
const X = (yr) => 420 + (yr - 2000) / 26.5 * 1300;
const Y = (v) => 900 - v / 800000 * 640;
const qx = (q) => X(S.qYear(q));
const dataEv = spine.events.filter((e) => e.kind === 'data');
const BILL = '#5E8C6A', BILL2 = '#4C7558', STRAP = '#E9E3D3';

function camAt(t) {
  const k = [[0, 330, 640, 2.1], [11.8, 330, 640, 2.1], [15.3, 1000, 560, 1], [56.4, 1000, 560, 1], [59.4, 1360, 560, 1.3], [62.9, 1360, 560, 1.3], [64.6, 1000, 560, 1], [99, 1000, 560, 1]];
  let i = 1; while (i < k.length - 1 && t > k[i][0]) i++;
  const [a, ...p] = k[i - 1], [b, ...q] = k[i], x = ease(t, a, b);
  return { cx: mix(p[0], q[0], x), cy: mix(p[1], q[1], x), z: mix(p[2], q[2], x) };
}

// chồng tiền: từ $lo đến $hi, mỗi bó $50,000; tô 'over' phần trên $500,000
function stack(x, lo, hi, w, o = {}) {
  const step = 50000;
  for (let v = lo; v < hi - 1; v += step) {
    const v2 = Math.min(hi, v + step), y1 = Y(v), y2 = Y(v2), over = o.over && v >= 500000 - 1, paid = o.paid && v < 200000 - 1;
    ctx.fillStyle = paid ? rgba(C.cushion, o.paidA ?? 1) : over ? C.warn : (Math.round(v / step) % 2 ? BILL : BILL2);
    if (paid && (o.paidA ?? 1) < 1) { ctx.fillStyle = (Math.round(v / step) % 2 ? BILL : BILL2); ctx.fillRect(x - w / 2, y2, w, y1 - y2); ctx.fillStyle = rgba(C.cushion, o.paidA); }
    ctx.fillRect(x - w / 2, y2 + 1, w, y1 - y2 - 2);
    ctx.fillStyle = rgba(STRAP, 0.85); ctx.fillRect(x - 5, y2 + 1, 10, y1 - y2 - 2);
  }
}

function beam(y, x0, x1, glow = 0) {
  ctx.fillStyle = '#59616E'; ctx.fillRect(x0, y - 9, x1 - x0, 18);
  ctx.fillStyle = '#8B94A3'; ctx.fillRect(x0, y - 9, x1 - x0, 4);
  ctx.fillStyle = '#3A404A'; for (let x = x0 + 20; x < x1; x += 60) { ctx.beginPath(); ctx.arc(x, y + 2, 3, 0, 7); ctx.fill(); }
  if (glow > 0) { ctx.fillStyle = rgba(C.warn, 0.5 * glow); ctx.fillRect(x0, y - 12, x1 - x0, 24); }
}

function calendar(x, y, label, flip, a) { // lịch xé để bàn (màn hình)
  if (a <= 0) return;
  ctx.save(); ctx.globalAlpha = a;
  ctx.fillStyle = '#E9E3D3'; roundRect(ctx, x, y, 300, 170, 12); ctx.fill();
  ctx.fillStyle = C.costlier; roundRect(ctx, x, y, 300, 44, 12); ctx.fill(); ctx.fillRect(x, y + 30, 300, 14);
  ctx.fillStyle = '#2A303B'; for (const dx of [60, 240]) { ctx.beginPath(); ctx.arc(x + dx, y + 8, 7, 0, 7); ctx.fill(); }
  ctx.font = '700 60px Inter'; ctx.fillStyle = '#1B1F26'; ctx.textAlign = 'center'; ctx.fillText(label, x + 150, y + 130);
  if (flip > 0) { // tờ cũ bay lên
    ctx.globalAlpha = a * (1 - flip); ctx.translate(x + 115, y + 44 - 90 * flip); ctx.rotate(-0.5 * flip);
    ctx.fillStyle = '#E9E3D3'; ctx.fillRect(-115, 0, 230, 126);
  }
  ctx.restore();
}

function frame(t) {
  const b = cue, cam = camAt(t);
  ctx.setTransform(1, 0, 0, 1, 0, 0);
  const g = ctx.createLinearGradient(0, 0, 0, 1080); g.addColorStop(0, '#121722'); g.addColorStop(1, C.bg); ctx.fillStyle = g; ctx.fillRect(0, 0, 1920, 1080);
  const W2S = (x, y) => [960 + (x - cam.cx) * cam.z, 540 + (y - cam.cy) * cam.z];
  const world = () => ctx.setTransform(cam.z, 0, 0, cam.z, 960 - cam.cx * cam.z, 540 - cam.cy * cam.z);
  const screen = () => ctx.setTransform(1, 0, 0, 1, 0, 0);
  // mặt đất
  world(); ctx.fillStyle = '#161B24'; ctx.fillRect(-400, Y(0), 3000, 400); ctx.fillStyle = C.grid; ctx.fillRect(-400, Y(0), 3000, 3); screen();

  // b1: khu phố — nhiều nhà, biển SOLD bật lên (nhiều giao dịch), giá gom về một (trung bình)
  const manyA = lin(t, b.b1.many - 4.6, b.b1.many - 1.0), gather = ease(t, b.b1.avg - 0.2, b.b1.avg + 0.8);
  if (manyA > 0 && gather < 1) {
    world();
    for (let k = 0; k < 10; k++) {
      const hx = k < 4 ? 80 + k * 66 : 520 + (k - 4) * 70, s = 44 + (k % 3) * 8, ap = lin(manyA, k / 12, k / 12 + 0.12);
      if (ap <= 0) continue;
      house(ctx, hx, Y(0), s, { alpha: ap * (1 - gather), wall: '#B8BFCA', roof: '#5F6B7A', win: '#C9D2DD' });
      const sold = lin(manyA, k / 12 + 0.1, k / 12 + 0.2);
      if (sold > 0) { // biển SOLD; khi gom: thẻ giá bay về nhà của Rosa & Frank
        const fx = mix(hx + s * 0.5, X(2000), gather), fy = mix(Y(0) - s * 1.25, Y(200000) - 40, gather);
        ctx.globalAlpha = sold * (1 - gather * 0.9); ctx.fillStyle = C.costlier; ctx.fillRect(fx - 26, fy - 14, 52, 24);
        ctx.fillStyle = '#fff'; ctx.font = '700 19px Inter'; ctx.textAlign = 'center'; ctx.fillText('SOLD', fx, fy + 5); ctx.textAlign = 'left'; ctx.globalAlpha = 1;
      }
    }
    screen();
    const [sx, sy] = W2S(420, Y(0)); text('many sales → one average', sx, sy + 70, 48, { color: C.muted, align: 'center', alpha: ease(t, b.b1.many - 0.4, b.b1.many) * (1 - gather) });
  }

  // lịch xé (thời gian): từ b2
  const qDraw = interp(spine.draw, t), qRide = t >= b.b5.t0 ? interp(spine.ride, t) : -1;
  const qNow = qRide >= 0 ? qRide : Math.min(105, qDraw);
  const calA = ease(t, b.b2.draw0 - 0.6, b.b2.draw0) * (1 - ease(t, b.b9.fly - 0.6, b.b9.fly));
  if (calA > 0) {
    const yrF = S.qYear(qNow) - 0.125, yr = Math.floor(yrF), flip = qNow >= 105 ? 0 : clamp((yrF - yr) * 4 - 3, 0, 1) * 0;
    const swap = Math.abs(t - (b.b5.t0 + 0.15)) < 0.4 ? 1 - Math.abs(t - (b.b5.t0 + 0.15)) / 0.4 : 0;
    calendar(110, 150, qNow >= 104.5 ? CL('sale_quarter') : String(yr), flip, calA * (1 - 0.6 * swap));
  }

  // trần: xà thép rơi xuống (b3), đứng yên
  const slide = ease(t, b.b4.less, b.b4.less + 1.6), off = 200000 * (1 - slide);
  if (t >= b.b3.cap - 0.05) {
    const drop = easeBack(t, b.b3.cap, b.b3.cap + 0.35), yv = mix(Y(820000) - 260, Y(500000), drop);
    let glow = 0; if (t >= b.b6.cross) glow = Math.max(1 - lin(t, b.b6.cross, b.b6.cross + 0.8), qRide >= 0 && at(gain, qRide) > 500000 ? 0.35 : 0);
    if (t >= b.b10.past - 0.1) glow = Math.max(glow, 0.6 * ease(t, b.b10.past - 0.1, b.b10.past + 0.2));
    world(); beam(yv, X(2000) - 60, X(2026.5) + 40, glow);
    const sweep = lin(t, b.b3.flat, b.b3.flat + 1.4);
    if (sweep > 0 && sweep < 1) { ctx.fillStyle = rgba(C.ink, 0.9); const x = mix(X(2000) - 60, X(2026.5) + 40, sweep); ctx.fillRect(x - 30, yv - 9, 60, 18); }
    screen();
    const [lx, ly] = W2S(X(2000) - 60, Y(500000));
    text(`${CL('excl_joint_limit_usd')} cap`, Math.max(110, lx), ly - 26, 48, { w: 700, color: C.ink, plate: '#3A404A', alpha: ease(t, b.b3.lbl - 0.1, b.b3.lbl + 0.3) * (1 - 0.6 * ease(t, 63.2, 64)) });
  }

  // vệt lịch sử (đỉnh chồng tiền theo thời gian)
  const trailA = 1 - 0.7 * ease(t, 62.9, 63.6);
  if (t >= b.b2.draw0) {
    world(); ctx.lineJoin = 'round'; const isGain = slide > 0.5, qEnd = Math.min(105, qDraw);
    ctx.beginPath(); for (let q = 0; q <= qEnd; q += 0.25) { const x = qx(q), y = Y(at(gain, q) + off); q === 0 ? ctx.moveTo(x, y) : ctx.lineTo(x, y); }
    ctx.strokeStyle = rgba(isGain ? C.ink : C.accent, (qRide >= 0 ? 0.3 : 0.75) * trailA); ctx.lineWidth = 4; ctx.stroke();
    if (qRide >= 0) for (let q = 0; q < qRide; q += 0.25) {
      const q2 = Math.min(qRide, q + 0.25), g1 = at(gain, q), g2 = at(gain, q2);
      ctx.beginPath(); ctx.moveTo(qx(q), Y(g1)); ctx.lineTo(qx(q2), Y(g2)); ctx.strokeStyle = rgba((g1 + g2) / 2 > 500000 ? C.warn : C.ink, trailA); ctx.lineWidth = 5; ctx.stroke();
    }
    screen();
    const labA = ease(t, b.b2.draw0 + 0.6, b.b2.draw0 + 1.4) * (1 - ease(t, b.b4.less + 0.2, b.b4.less + 0.8));
    if (labA > 0) { const ql = Math.max(4, Math.min(qEnd - 16, 52)); const [sx, sy] = W2S(qx(ql), Y(at(gain, ql) + off)); text('home value', sx, sy - 30, 48, { color: C.accent, align: 'center', alpha: labA }); }
    const lab2 = ease(t, b.b4.paid - 0.3, b.b4.paid + 0.4) * (1 - ease(t, 63.2, 64));
    if (lab2 > 0) { const [sx, sy] = W2S(qx(58), Y(at(gain, 58))); text('gain on paper', sx + 24, sy + 64, 48, { alpha: lab2 }); }
  }

  // nhân vật chính: NHÀ trên CHỒNG TIỀN
  const heroA = 1 - ease(t, 62.9, 63.5);
  const swapA = t >= b.b5.t0 - 0.5 && t < b.b5.t0 + 0.6 ? Math.abs(lin(t, b.b5.t0 - 0.5, b.b5.t0 + 0.6) * 2 - 1) : 1; // nhà về đầu 2000 (mờ ra, hiện lại)
  {
    let hx, top, lo, w, hw;
    if (t < b.b2.draw0) { hx = X(2000); lo = 0; top = 200000; w = 70; hw = 130; }
    else { const q = qNow; hx = qx(q); top = (qRide >= 0 ? at(gain, q) : at(gain, q) + off); lo = qRide >= 0 ? 0 : -200000 * slide; w = 58; hw = mix(130, 84, ease(t, b.b2.draw0, b.b2.draw0 + 0.8)); }
    const fog = ease(t, b.b1.blur, b.b1.blur + 0.6) * (1 - ease(t, b.b1.avg + 0.3, b.b1.avg + 1.0));
    world(); ctx.globalAlpha = heroA * swapA;
    const paidHi = ease(t, b.b4.grow - 0.3, b.b4.grow + 0.3);
    // b4: phần $200,000 đã trả trượt ra trái rồi chồng hạ xuống
    if (t < b.b2.draw0) stack(hx, 0, 200000, w);
    else if (qRide < 0) {
      const val = at(gain, qNow) + 200000;
      ctx.save(); ctx.translate(-260 * slide, 0); ctx.globalAlpha = heroA * swapA * (1 - 0.8 * slide); stack(hx, 0, 200000, w, { paid: paidHi > 0, paidA: paidHi }); ctx.restore();
      ctx.save(); ctx.translate(0, (Y(0) - Y(200000)) * slide); stack(hx, 200000, val, w); ctx.restore();
      ctx.globalAlpha = heroA * swapA;
    } else stack(hx, 0, Math.max(0, top), w, { over: true });
    let pulse = 0; for (const e of dataEv) if (t >= e.t && t < e.t + 0.18) pulse = Math.max(pulse, 1 - (t - e.t) / 0.18);
    const roofY = t < b.b2.draw0 ? Y(200000) : Y(Math.max(0, top));
    if (pulse > 0 && t > b.b2.draw0) { ctx.fillStyle = rgba(qRide >= 0 && top > 500000 ? C.warn : C.ink, 0.25 * pulse); ctx.beginPath(); ctx.arc(hx, roofY - hw * 0.4, hw * 0.6 + 10 * pulse, 0, 7); ctx.fill(); }
    house(ctx, hx, roofY, hw);
    if (fog > 0) { for (let k = 0; k < 7; k++) { ctx.fillStyle = rgba('#AEB6C2', 0.22 * fog); ctx.beginPath(); ctx.arc(hx - 70 + k * 24, roofY - 50 - (k % 3) * 18, 46, 0, 7); ctx.fill(); }
      ctx.font = '700 64px Inter'; ctx.fillStyle = rgba(C.ink, fog); ctx.textAlign = 'center'; ctx.fillText('?', hx, roofY - 34); ctx.textAlign = 'left'; }
    ctx.globalAlpha = 1;
    const pA = 1 - ease(t, b.b1.blur - 0.2, b.b1.blur + 0.6);
    if (pA > 0) { ctx.globalAlpha = pA; person(ctx, X(2000) - 150, Y(0), 0.62, '#E9C9A8', { hair: true }); person(ctx, X(2000) - 100, Y(0), 0.68, '#C9D6E8'); ctx.globalAlpha = 1; }
    screen();
    if (pA > 0) { const [sx, sy] = W2S(X(2000) - 125, Y(0)); text('Rosa & Frank · Phoenix', sx, sy + 64, 48, { align: 'center', alpha: pA * ease(t, 0.5, 1) }); }
    // b0: thẻ giá $200,000 trên nhà; dấu hỏi dưới xà gợi ý
    const tagA = ease(t, 0.6, 1.2) * (1 - ease(t, b.b1.blur, b.b1.blur + 0.4));
    if (tagA > 0) { const [sx, sy] = W2S(X(2000) + 80, Y(200000) - 60); text(`paid ${CL('illustrative_price_200k_usd')} in ${CL('buy_year')}`, sx + 10, sy, 48, { w: 700, plate: '#E9E3D3', color: '#1B1F26', alpha: tagA }); }
    const qA = ease(t, b.b0.cap_hint, b.b0.cap_hint + 0.5) * (1 - ease(t, b.b1.blur, b.b1.blur + 0.5));
    if (qA > 0) {
      world(); ctx.globalAlpha = qA * 0.6; beam(Y(500000), X(2000) - 300, X(2000) + 420); ctx.globalAlpha = 1; screen();
      const [sx, sy] = W2S(X(2000) + 60, Y(500000));
      text('?', sx, sy + 110, 120, { w: 700, color: C.warn, align: 'center', alpha: qA * ease(t, b.b0.q - 0.3, b.b0.q) });
      text('the tax-free cap', sx + 100, sy - 30, 48, { color: C.muted, alpha: qA });
    }
  }

  // b4: nhãn phần đã trả + phép trừ
  const paidA = ease(t, b.b4.grow - 0.3, b.b4.grow + 0.3) * (1 - ease(t, b.b4.less + 1.6, b.b4.less + 2.3));
  if (paidA > 0) {
    const [sx, sy] = W2S(qx(105) - 260 * slide - 40, Y(100000));
    text(`${slide > 0.02 ? '− ' : ''}${CL('illustrative_price_200k_usd')} paid`, sx, sy + 16, 48, { w: 700, color: C.cushion, align: 'right', alpha: paidA });
    const arA = ease(t, b.b4.less, b.b4.less + 0.3) * (1 - ease(t, b.b4.less + 1.8, b.b4.less + 2.3));
    if (false) { const [ax, ay] = W2S(qx(105) - 60, Y(330000)); text(`− ${CL('illustrative_price_200k_usd')}`, ax, ay, 56, { w: 700, color: C.cushion, align: 'right', alpha: arA }); }
  }

  // b6/b8 mốc
  const tag = (q, s, a) => { const [sx, sy] = W2S(qx(q), Y(500000)); text(s, sx, sy - 120, 48, { w: 700, color: '#1B1F26', plate: C.warn, align: 'center', alpha: a }); };
  if (t >= b.b6.cross - 0.05) tag(89, `Over: ${CL('cross_quarter_at_200k_phoenix')}`, ease(t, b.b6.cross - 0.05, b.b6.cross + 0.25) * (1 - ease(t, b.b8.lbl - 0.2, b.b8.lbl + 0.2)));
  if (t >= b.b8.lbl - 0.1) tag(93, `Stayed over since ${CL('stay_quarter_at_200k_phoenix')}`, ease(t, b.b8.lbl - 0.1, b.b8.lbl + 0.3) * (1 - ease(t, b.b9.fly - 0.4, b.b9.fly)));

  // b9: thẻ giá bay lên thành số hero
  if (t >= b.b9.fly - 0.05) {
    const [tx, ty] = W2S(qx(105), Y(gain[105]) - 90), f = easeOut(t, b.b9.fly, b.b9.land), arc = Math.sin(Math.PI * f) * 80, out = 1 - ease(t, 62.9, 63.5);
    text(CL('gain_at_200k_phoenix'), mix(tx, 960, f), mix(ty, 230, f) - arc, mix(56, 120, f), { w: 700, color: '#1B1F26', plate: '#E9E3D3', align: 'center', alpha: out });
    text('gain on paper · the number from the opening', 960, 310, 48, { color: C.muted, align: 'center', alpha: ease(t, b.b9.land, b.b9.land + 0.4) * out });
  }
  if (t >= b.b10.past - 0.1) {
    const a = ease(t, b.b10.past - 0.1, b.b10.past + 0.25) * (1 - ease(t, 63.2, 63.9));
    const [x0, y0] = W2S(qx(105) + 44, Y(500000)), [, y1] = W2S(0, Y(gain[105]));
    ctx.strokeStyle = rgba(C.warn, a); ctx.lineWidth = 6; ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(x0 + 18, y0); ctx.lineTo(x0 + 18, y1); ctx.lineTo(x0, y1); ctx.stroke();
    text('past the cap', x0 + 34, (y0 + y1) / 2 + 16, 48, { w: 700, color: C.warn, alpha: a });
  }

  // b11: hai nhà trên hai chồng tiền, cao ∝ chỉ số giá (×3,8)
  if (t >= 63.0) {
    const a = ease(t, 63.2, 64.0), gr = S.data.claims.growth_phoenix.value, grow = ease(t, b.b11.x - 0.3, b.b11.x + 0.9);
    ctx.fillStyle = rgba(C.bg, 0.88 * a); ctx.fillRect(0, 0, 1920, 1080);
    const base = 900, h0 = 120, h1 = mix(h0, h0 * gr, grow);
    for (const [x, h] of [[700, h0], [1220, h1]]) {
      ctx.globalAlpha = a; const n = Math.max(1, Math.round(h / 30));
      for (let i = 0; i < n; i++) { ctx.fillStyle = i % 2 ? BILL : BILL2; ctx.fillRect(x - 75, base - (i + 1) * h / n + 1, 150, h / n - 2); ctx.fillStyle = rgba(STRAP, 0.85); ctx.fillRect(x - 6, base - (i + 1) * h / n + 1, 12, h / n - 2); }
      house(ctx, x, base - h, 130); ctx.globalAlpha = 1;
    }
    calendar(585, 920 - 0, String(CL('buy_year')), 0, 0); // (lịch nhỏ không dùng: nhãn năm dưới cột)
    text(String(CL('buy_year')), 700, base + 56, 48, { color: C.muted, align: 'center', alpha: a });
    text(CL('sale_quarter'), 1220, base + 56, 48, { color: C.muted, align: 'center', alpha: a });
    text(CL('growth_phoenix'), 1360, base - h1 + 60, 120, { w: 700, color: C.accent, alpha: ease(t, b.b11.x, b.b11.x + 0.4) });
    text('Phoenix-area prices since 2000', 960, 150, 56, { align: 'center', alpha: ease(t, b.b11.x - 0.2, b.b11.x + 0.4) });
  }

  screen();
  chrome(K, { illus: true, hist: t >= b.b1.avg, src: t >= b.b1.src && t < 63.2 || t >= 64,
    cw: t >= b.b10.past ? 'A measurement, not a tax bill or a next step' : t >= b.b4.gain ? 'A home that rose like the Phoenix average' : null,
    cwA: t >= b.b10.past ? ease(t, b.b10.past, b.b10.past + 0.4) : ease(t, b.b4.gain, b.b4.gain + 0.4) });
}

window.APP = { canvas, frame };
window.READY = true;
