// Mốc V · Hướng C — "hình học liên tục": một khung đồ thị duy nhất, máy quay di chuyển, KHÔNG cắt cứng, KHÔNG thẻ chữ toàn màn hình.
// Biểu đồ là nhân vật: nhà nhỏ cưỡi đầu đường; phép trừ $200,000 là cả đường trượt xuống; số bay từ đầu đường lên làm số hero.
import { C, clamp, lin, ease, easeOut, easeBack, mix, rgba, loadAll, makeCtx, chrome, person, house, roundRect } from '../lib2d.js';

const S = await loadAll();
const { cue, interp, gain, value, at, CL, spine } = S;
const canvas = document.getElementById('c');
const K = makeCtx(canvas), { ctx, text } = K;

// thế giới: x theo năm, y theo đô la
const X = (yr) => 300 + (yr - 2000) / 26.5 * 1400;
const Y = (v) => 880 - v / 800000 * 640;
const qx = (q) => X(S.qYear(q));
const dataEv = spine.events.filter((e) => e.kind === 'data');
const popT = spine.events.filter((e) => e.kind === 'tick' && e.pop !== undefined).map((e) => e.t);   // mỗi nhà SOLD bật = một tick âm

function camAt(t) {
  const keys = [[0, 330, 650, 2.2], [11.8, 330, 650, 2.2], [15.3, 1000, 560, 1], [56.4, 1000, 560, 1], [59.4, 1340, 560, 1.15],
    [62.9, 1340, 560, 1.15], [64.6, 1000, 560, 1], [99, 1000, 560, 1]];
  let i = 1; while (i < keys.length - 1 && t > keys[i][0]) i++;
  const [a, ...p] = keys[i - 1], [b, ...q] = keys[i], x = ease(t, a, b);
  return { cx: mix(p[0], q[0], x), cy: mix(p[1], q[1], x), z: mix(p[2], q[2], x) };
}

function frame(t) {
  const b = cue, cam = camAt(t);
  ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.fillStyle = C.bg; ctx.fillRect(0, 0, 1920, 1080);
  const W2S = (x, y) => [960 + (x - cam.cx) * cam.z, 540 + (y - cam.cy) * cam.z];
  const world = () => ctx.setTransform(cam.z, 0, 0, cam.z, 960 - cam.cx * cam.z, 540 - cam.cy * cam.z);
  const screen = () => ctx.setTransform(1, 0, 0, 1, 0, 0);

  // ---- trục (vào khi máy quay lùi ra, b1 → b2)
  const axA = ease(t, 13.6, 15.4) * (1 - 0.6 * ease(t, 63.2, 64.4)) * (1 - ease(t, 56.4, 57.4) + ease(t, 62.9, 64.2));
  if (axA > 0) {
    world(); ctx.globalAlpha = axA; ctx.strokeStyle = C.grid; ctx.lineWidth = 2 / cam.z;
    ctx.beginPath(); ctx.moveTo(X(2000), Y(0)); ctx.lineTo(X(2026.5), Y(0)); ctx.stroke();
    for (let yr = 2000; yr <= 2025; yr += 5) { ctx.beginPath(); ctx.moveTo(X(yr), Y(0)); ctx.lineTo(X(yr), Y(0) + 12); ctx.stroke(); }
    ctx.globalAlpha = 1; screen();
    for (let yr = 2000; yr <= 2025; yr += 5) { const [sx, sy] = W2S(X(yr), Y(0)); text(String(yr), sx, sy + 56, 40, { w: 400, color: C.muted, align: 'center', alpha: axA }); }
  }

  // ---- b1: nhiều nhà nhỏ = nhiều giao dịch → gom về một điểm (trung bình)
  const manyA = t >= popT[0] - 0.1 ? 1 : 0, gather = ease(t, b.b1.avg - 0.2, b.b1.avg + 0.7);
  if (manyA > 0 && gather < 1) {
    world();
    for (let k = 0; k < popT.length; k++) {
      const r = Math.sin(k * 12.9898) * 43758.5453, fr = r - Math.floor(r), r2 = Math.sin(k * 78.233) * 12345.678, fr2 = r2 - Math.floor(r2);
      const hx = 140 + fr * 600, hy = 600 + fr2 * 240, appear = lin(t, popT[k] - 0.05, popT[k] + 0.12);
      if (appear <= 0) continue;
      const x = mix(hx, X(2000), gather), y = mix(hy, Y(200000), gather);
      house(ctx, x, y, 34 * (1 - 0.6 * gather), { alpha: appear * (1 - gather), wall: C.muted, roof: '#5F6B7A', win: '#C9D2DD' });
    }
    screen();
  }

  // ---- đường GIÁ TRỊ (b2) rồi trượt xuống thành đường LÃI (b4)
  const qDraw = interp(spine.draw, t);
  const slide = ease(t, b.b4.less, b.b4.less + 1.6);          // 0 → 1: trừ $200,000
  const off = 200000 * (1 - slide);                                  // đường = lãi + off
  const lineOn = t >= b.b2.draw0 - 0.1;
  const qRide = t >= b.b5.t0 ? interp(spine.ride, t) : -1;
  if (lineOn) {
    world();
    const qEnd = Math.min(105, qDraw);
    // b4: dải $200,000 đã trả (cushion), co lại khi đường trượt
    const bandA = ease(t, b.b4.less - 0.1, b.b4.less + 0.3) * (1 - ease(t, b.b4.less + 1.6, b.b4.less + 2.4));
    if (bandA > 0) {
      ctx.fillStyle = rgba(C.cushion, 0.35 * bandA);
      ctx.fillRect(X(2000), Y(200000 * (1 - slide)), X(2026.5) - X(2000), Y(0) - Y(200000 * (1 - slide)));
    }
    // khoảng dưới vạch (b5)
    const gapA = ease(t, b.b5.under - 0.6, b.b5.under + 0.3) * (1 - ease(t, b.b6.t0, b.b6.t0 + 0.6));
    const capOn = t >= b.b3.cap;
    const isGain = slide > 0.5;
    const col = isGain ? C.ink : C.accent;
    const dim = !capOn || isGain ? 1 : t < b.b4.grow - 0.2 ? mix(1, 0.22, ease(t, b.b3.cap + 0.3, b.b3.cap + 0.9)) : mix(0.22, 1, ease(t, b.b4.grow - 0.2, b.b4.grow + 0.4));   // lượt đạo diễn: đường GIÁ TRỊ mờ khi đặt cạnh trần (tránh đọc nhầm 'giá nhà vượt trần')
    ctx.lineJoin = 'round'; ctx.lineCap = 'round';
    // nét chính
    ctx.beginPath();
    for (let q = 0; q <= qEnd; q += 0.25) { const x = qx(q), y = Y(at(gain, q) + off); q === 0 ? ctx.moveTo(x, y) : ctx.lineTo(x, y); }
    ctx.strokeStyle = rgba(col, (qRide >= 0 ? 0.42 : 1) * dim); ctx.lineWidth = 6 / Math.max(1, cam.z * 0.8); ctx.stroke();
    if (gapA > 0 && qRide >= 0) {
      ctx.beginPath(); ctx.moveTo(qx(0), Y(500000));
      for (let q = 0; q <= qRide; q += 0.25) ctx.lineTo(qx(q), Y(Math.min(500000, at(gain, q))));
      ctx.lineTo(qx(qRide), Y(500000)); ctx.closePath(); ctx.fillStyle = rgba(C.muted, 0.16 * gapA); ctx.fill();
    }
    // phần đã đi qua (b5–b8): sáng; đoạn trên vạch = warn
    if (qRide >= 0) {
      for (let q = 0; q < qRide; q += 0.25) {
        const q2 = Math.min(qRide, q + 0.25), g1 = at(gain, q), g2 = at(gain, q2), over = (g1 + g2) / 2 > 500000;
        ctx.beginPath(); ctx.moveTo(qx(q), Y(g1)); ctx.lineTo(qx(q2), Y(g2));
        ctx.strokeStyle = over ? C.warn : C.ink; ctx.lineWidth = over ? 10 : 6; ctx.stroke();
      }
    }
    screen();
    // nhãn đường
    const labA = ease(t, b.b2.draw0 + 0.6, b.b2.draw0 + 1.4) * (1 - ease(t, b.b4.less + 0.2, b.b4.less + 0.8));
    if (labA > 0) { const [sx, sy] = W2S(qx(Math.min(qEnd, 64)), Y(at(gain, Math.min(qEnd, 64)) + off)); text('home value', sx - 20, sy - 34, 48, { color: C.accent, align: 'right', alpha: labA * dim }); }
    const lab2 = ease(t, b.b4.paid - 0.3, b.b4.paid + 0.4) * (1 - ease(t, 63.2, 64.0));
    if (lab2 > 0) { const [sx, sy] = W2S(qx(70), Y(at(gain, 70))); text('gain on paper', sx + 24, sy + 64, 48, { color: C.ink, alpha: lab2 }); }
  }

  // ---- vạch trần (b3): rơi xuống, khoá, đứng yên suốt đoạn
  if (t >= b.b3.cap - 0.05) {
    const drop = easeBack(t, b.b3.cap, b.b3.cap + 0.35);
    const yv = mix(Y(820000) - 200, Y(500000), drop);
    world(); ctx.strokeStyle = C.muted; ctx.lineWidth = 6 / Math.max(1, cam.z * 0.8);
    ctx.beginPath(); ctx.moveTo(X(2000) - 40, yv); ctx.lineTo(X(2026.5) + 20, yv); ctx.stroke();
    // "same in every quarter": nhịp chạy dọc vạch
    const sweep = lin(t, b.b3.flat, b.b3.flat + 1.4);
    if (sweep > 0 && sweep < 1) for (let yr = 2000; yr <= 2026; yr += 1) {
      const d = Math.abs((yr - 2000) / 26 - sweep); if (d < 0.08) { ctx.fillStyle = rgba(C.ink, 1 - d / 0.08); ctx.fillRect(X(yr) - 3, yv - 14, 6, 28); }
    }
    screen();
    const [lx, ly] = W2S(X(2000), Y(500000));
    text(`${CL('excl_joint_limit_usd')} cap`, Math.max(110, lx), ly - 22, 48, { w: 700, color: C.muted, alpha: ease(t, b.b3.lbl - 0.1, b.b3.lbl + 0.3) * (1 - 0.5 * ease(t, 63.2, 64)) });
  }

  // ---- con trỏ: nhà nhỏ cưỡi đường (b2 đường giá trị, b5–b8 đường lãi); nhấp sáng ở mỗi nốt âm dữ liệu
  const heroA = 1 - ease(t, 62.9, 63.6);
  {
    let hx, hy, w;
    if (t < b.b2.draw0) {                                            // b0–b1: nhà của Rosa & Frank (lớn), về điểm đầu
      hx = X(2000); hy = Y(200000); w = 120;
    } else if (qRide < 0) { const rw = ease(t, b.b5.t0 - 0.75, b.b5.t0 + 0.15), q = Math.min(105, qDraw) * (1 - rw); /* tua về 2000 dọc đường lãi */ hx = qx(q); hy = Y(at(gain, q) + off); w = mix(120, 56, ease(t, b.b2.draw0, b.b2.draw0 + 0.8)); }
    else { hx = qx(qRide); hy = Y(at(gain, qRide)); w = 56; }
    const unknown = ease(t, b.b1.blur, b.b1.blur + 0.6) * (1 - ease(t, b.b1.avg + 0.4, b.b1.avg + 1.0));
    world();
    let pulse = 0; for (const e of dataEv) if (t >= e.t && t < e.t + 0.18) pulse = Math.max(pulse, 1 - (t - e.t) / 0.18);
    if (pulse > 0 && t > b.b2.draw0) { ctx.fillStyle = rgba(qRide >= 0 && at(gain, qRide) > 500000 ? C.warn : C.ink, 0.35 * pulse); ctx.beginPath(); ctx.arc(hx, hy, 18 + 14 * pulse, 0, 7); ctx.fill(); }
    if (unknown > 0.02) {
      ctx.save(); ctx.globalAlpha = heroA; ctx.setLineDash([10, 8]); ctx.strokeStyle = C.muted; ctx.lineWidth = 3;
      const h = w * 0.62, r = w * 0.42; ctx.beginPath(); ctx.moveTo(hx - w / 2, hy); ctx.lineTo(hx - w / 2, hy - h); ctx.lineTo(hx - w * 0.6, hy - h); ctx.lineTo(hx, hy - h - r);
      ctx.lineTo(hx + w * 0.6, hy - h); ctx.lineTo(hx + w / 2, hy - h); ctx.lineTo(hx + w / 2, hy); ctx.closePath(); ctx.globalAlpha = heroA * unknown; ctx.stroke(); ctx.restore();
      ctx.globalAlpha = heroA * unknown; ctx.font = '700 60px Inter'; ctx.fillStyle = C.muted; ctx.textAlign = 'center'; ctx.fillText('?', hx, hy - 18); ctx.globalAlpha = 1; ctx.textAlign = 'left';
    }
    const bump = t >= b.b10.past ? Math.sin(Math.PI * lin(t, b.b10.past, b.b10.past + 0.35)) * 14 : 0;
    house(ctx, hx, hy - bump, w, { alpha: heroA * (1 - unknown) });
    const back = ease(t, b.b9.t0, b.b9.t0 + 0.8) * heroA;   // Rosa & Frank trở lại cạnh nhà khi lời nói về lãi của họ
    if (back > 0 && qRide >= 0) { ctx.globalAlpha = back; person(ctx, hx - 62, hy, 0.2, C.ink, { hair: true }); person(ctx, hx - 44, hy, 0.22, C.ink); ctx.globalAlpha = 1; }
    const upA = ease(t, b.b1.rise - 0.1, b.b1.rise + 0.3) * (1 - ease(t, b.b1.many - 0.5, b.b1.many));
    if (upA > 0) { ctx.fillStyle = rgba(C.accent, upA); const ux = hx + w * 0.8, uy = hy - w * 0.4 - 30 * ease(t, b.b1.rise, b.b1.rise + 1.2); ctx.beginPath(); ctx.moveTo(ux, uy - 34); ctx.lineTo(ux - 18, uy - 8); ctx.lineTo(ux + 18, uy - 8); ctx.closePath(); ctx.fill(); ctx.fillRect(ux - 6, uy - 10, 12, 34); }
    // b0: Rosa & Frank
    const pA = 1 - ease(t, b.b1.blur - 0.2, b.b1.blur + 0.6);
    if (pA > 0) { ctx.globalAlpha = pA; person(ctx, X(2000) - 120, Y(200000), 0.42, C.ink, { hair: true }); person(ctx, X(2000) - 82, Y(200000), 0.46, C.ink); ctx.globalAlpha = 1; }
    screen();
    if (pA > 0) { const [sx, sy] = W2S(X(2000) - 100, Y(200000)); text('Rosa & Frank · Phoenix', sx, sy + 70, 48, { align: 'center', alpha: pA * ease(t, 0.5, 1.0) }); }
    // b0: dấu hỏi giữa mái và vạch gợi trần
    const qA = ease(t, b.b0.cap_hint, b.b0.cap_hint + 0.5) * (1 - ease(t, b.b1.blur, b.b1.blur + 0.5));
    if (qA > 0) {
      world(); ctx.setLineDash([16, 12]); ctx.strokeStyle = rgba(C.muted, qA); ctx.lineWidth = 3; ctx.beginPath(); ctx.moveTo(X(2000) - 260, Y(500000)); ctx.lineTo(X(2000) + 400, Y(500000)); ctx.stroke(); ctx.setLineDash([]);
      screen(); const [sx, sy] = W2S(X(2000) + 10, mix(Y(200000) - 130, Y(500000) + 40, 0.5));
      text('?', sx, sy + ease(t, b.b0.q - 0.2, b.b0.q + 0.2) * -6, 120, { w: 700, color: C.warn, align: 'center', alpha: qA * ease(t, b.b0.q - 0.3, b.b0.q) });
      text('the cap', W2S(X(2000) + 400, 0)[0], W2S(0, Y(500000))[1] - 20, 44, { color: C.muted, align: 'right', alpha: qA });
    }
  }

  // ---- b2: năm chạy theo đầu đường
  if (t >= b.b2.draw0 && t < b.b3.cap + 0.4) {
    const q = Math.min(105, qDraw), [sx, sy] = W2S(qx(q), Y(at(gain, q) + off));
    const yr = Math.floor(S.qYear(q)); const a = 1 - ease(t, b.b3.cap, b.b3.cap + 0.4);
    text(q >= 105 ? CL('sale_quarter') : String(yr), sx + 40, sy - 40, 54, { w: 700, color: C.accent, alpha: a });
  }

  // ---- b4: "gain on paper = ?" (lời 'gain') → khối $200,000 (lời 'two hundred thousand') → lớn theo chỉ số ('grown') → trừ ('less')
  const qA2 = ease(t, b.b4.gain - 0.1, b.b4.gain + 0.3) * (1 - ease(t, b.b4.less, b.b4.less + 0.4));
  if (qA2 > 0) { const [sx, sy] = W2S(X(2016), Y(70000)); text('their gain on paper = ?', sx, sy, 56, { w: 700, color: C.ink, align: 'center', alpha: qA2 }); }
  const paidA = ease(t, b.b4.two - 0.1, b.b4.two + 0.3) * (1 - ease(t, b.b4.less + 1.6, b.b4.less + 2.4));
  if (paidA > 0) {
    world(); ctx.fillStyle = rgba(C.cushion, 0.9 * paidA); ctx.fillRect(X(2000) - 34, Y(200000 * (1 - slide)), 22, Y(0) - Y(200000 * (1 - slide))); screen();
    const [sx, sy] = W2S(X(2000) + 10, Y(200000 * (1 - slide)));
    text(t < b.b4.less ? CL('illustrative_price_200k_usd') : `− ${CL('illustrative_price_200k_usd')} paid`, sx + 10, sy - 18, 48, { w: 700, color: C.cushion, alpha: paidA });
  }
  const grA = ease(t, b.b4.grow - 0.1, b.b4.grow + 0.3) * (1 - ease(t, b.b4.less, b.b4.less + 0.4));
  if (grA > 0) { const [sx, sy] = W2S(qx(105), Y(gain[105] + 200000)); text(`${CL('illustrative_price_200k_usd')}, grown with the index`, sx - 30, sy - 40, 48, { w: 700, color: C.accent, align: 'right', alpha: grA }); }

  // ---- b5: ngoặc "well under the line"
  const brA = ease(t, b.b5.under - 0.1, b.b5.under + 0.3) * (1 - ease(t, b.b6.t0, b.b6.t0 + 0.5));
  if (brA > 0 && qRide >= 0) {
    const [x0, y0] = W2S(qx(qRide) + 34, Y(500000)), [, y1] = W2S(0, Y(Math.max(0, at(gain, qRide))));
    ctx.strokeStyle = rgba(C.cushion, brA); ctx.lineWidth = 5; ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(x0 + 16, y0); ctx.lineTo(x0 + 16, y1); ctx.lineTo(x0, y1); ctx.stroke();
    text('well under', x0 + 30, (y0 + y1) / 2 + 16, 48, { w: 700, color: C.cushion, alpha: brA });
  }

  // ---- b6/b8: mốc vượt
  // mốc giữ đến hết nhịp kết luận (luật thư viện: nhịp kết ở trạng thái kết luận): "Over" trái điểm cắt, "Stayed over" phải trên đoạn vượt
  const crossQ = 88 + (500000 - gain[88]) / (gain[89] - gain[88]);
  const keep = 1 - ease(t, b.b9.fly - 0.4, b.b9.fly);
  if (t >= b.b6.cross - 0.05) {
    const a = ease(t, b.b6.cross - 0.05, b.b6.cross + 0.25) * keep;
    const fl = 1 - lin(t, b.b6.cross, b.b6.cross + 0.6);
    world();
    if (fl > 0) { ctx.strokeStyle = rgba(C.warn, fl); ctx.lineWidth = 4; ctx.beginPath(); ctx.arc(qx(crossQ), Y(500000), 20 + 70 * (1 - fl), 0, 7); ctx.stroke();
      for (let k = 0; k < 10; k++) { const an = k * Math.PI / 5, r0 = 26 + 50 * (1 - fl), r1 = r0 + 34; ctx.beginPath(); ctx.moveTo(qx(crossQ) + r0 * Math.cos(an), Y(500000) + r0 * Math.sin(an)); ctx.lineTo(qx(crossQ) + r1 * Math.cos(an), Y(500000) + r1 * Math.sin(an)); ctx.stroke(); } }
    ctx.fillStyle = rgba(C.warn, a); ctx.beginPath(); ctx.arc(qx(crossQ), Y(500000), 9, 0, 7); ctx.fill(); screen();
    const [sx, sy] = W2S(qx(crossQ), Y(500000));
    text(`Over: ${CL('cross_quarter_at_200k_phoenix')}`, sx - 26, sy - 26, 48, { w: 700, color: C.warn, align: 'right', alpha: a });
  }
  if (t >= b.b8.lbl - 0.1) {
    const a = ease(t, b.b8.lbl - 0.1, b.b8.lbl + 0.3) * keep, [sx, sy] = W2S(qx(93), Y(500000));
    world(); ctx.fillStyle = rgba(C.warn, a); ctx.beginPath(); ctx.arc(qx(93), Y(500000), 9, 0, 7); ctx.fill(); screen();
    text(`Stayed over since ${CL('stay_quarter_at_200k_phoenix')}`, 1824, sy - 140, 48, { w: 700, color: C.warn, align: 'right', alpha: a });
  }

  // ---- b9: số bay từ đầu đường lên làm số hero (gọi lại câu mở đầu)
  if (t >= b.b9.fly - 0.05) {
    const [tx, ty] = W2S(qx(105), Y(gain[105])), f = easeOut(t, b.b9.fly, b.b9.land), arc = Math.sin(Math.PI * f) * 80;
    const x = mix(tx + 20, 960, f), y = mix(ty - 30, 210, f) - arc, px = mix(56, 120, f);
    const out = 1 - ease(t, 62.9, 63.5);
    text(CL('gain_at_200k_phoenix'), x, y, px, { w: 700, color: C.ink, align: f > 0.5 ? 'center' : 'left', alpha: out });
    text('gain on paper · the number from the opening', 960, 290, 48, { color: C.muted, align: 'center', alpha: ease(t, b.b9.land, b.b9.land + 0.4) * out });
  }
  // ---- b10: phần vượt trần
  if (t >= b.b10.past - 0.1) {
    const a = ease(t, b.b10.past - 0.1, b.b10.past + 0.25) * (1 - ease(t, 63.2, 63.9));
    const [x0, y0] = W2S(qx(105) + 26, Y(500000)), [, y1] = W2S(0, Y(gain[105]));
    ctx.strokeStyle = rgba(C.warn, a); ctx.lineWidth = 6; ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(x0 + 18, y0); ctx.lineTo(x0 + 18, y1); ctx.lineTo(x0, y1); ctx.stroke();
    text('past the cap', x0 + 34, (y0 + y1) / 2 + 16, 48, { w: 700, color: C.warn, alpha: a });
  }

  // ---- b11: giá ×3,8 — hai cột giá (chiều cao ∝ chỉ số), nhà ở đỉnh
  if (t >= 63.0) {
    const a = ease(t, 63.2, 64.0), g = S.data.claims.growth_phoenix.value, grow = ease(t, 63.8, b.b11.x + 0.05);
    const base = 900, h0 = 120, x0 = 700, x1 = 1220, cw = 150;
    ctx.globalAlpha = a; ctx.fillStyle = rgba(C.bg, a); ctx.fillRect(0, 0, 1920, 1080); ctx.globalAlpha = 1;
    ctx.fillStyle = rgba(C.accent, 0.85 * a); ctx.fillRect(x0 - cw / 2, base - h0, cw, h0);
    const h1 = mix(h0, h0 * g, grow); ctx.fillRect(x1 - cw / 2, base - h1, cw, h1);
    ctx.globalAlpha = a; house(ctx, x0, base - h0, 110); house(ctx, x1, base - h1, 110); ctx.globalAlpha = 1;
    text(String(CL('buy_year')), x0, base + 56, 48, { color: C.muted, align: 'center', alpha: a });
    text(CL('sale_quarter'), x1, base + 56, 48, { color: C.muted, align: 'center', alpha: a });
    text(CL('growth_phoenix'), x1 + 130, base - h1 + 40, 120, { w: 700, color: C.accent, alpha: ease(t, b.b11.x, b.b11.x + 0.4) });
    text('Phoenix-area prices since 2000', 960, 190, 56, { w: 600, align: 'center', alpha: ease(t, 63.2, 63.8) });
  }

  // ---- lớp bắt buộc: huy hiệu nhỏ
  screen();
  chrome(K, { illus: true, hist: t >= b.b1.avg, src: t >= b.b1.src,
    cw: t >= b.b10.past ? 'A measurement, not a tax bill or a next step' : t >= b.b4.gain ? 'A home that rose like the Phoenix average' : null,
    cwA: t >= b.b10.past ? ease(t, b.b10.past, b.b10.past + 0.4) : ease(t, b.b4.gain, b.b4.gain + 0.4) });
}

window.APP = { canvas, frame };
window.READY = true;
