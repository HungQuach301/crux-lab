'use strict';
// F2 · Break-even moves from month 24 to month 30. Claims: cost_median $5,124, sav_median $221 (ILL.), be_simple_median 24 (ILL.),
// gap24 $1,133 (ILL.), be_bal_median 30 (ILL.). Quote card: CFPB (public domain), consumerfinance.gov, retrieved 2026-09-29.
(function () {
  const { desk, clamp, lerp, ease, easeOut, back, seg, el, box, text, svg, sv, penPrep, pen, loopPath, highlighter, hl, stamp, camAt, setCam, dof, lift, C } = window.K;
  const S = {};
  const DUR = 10.0;
  const BILL = 5123.53, SAV = 221.30, GAP24 = 1132.95, BE = 30;
  const GAP30 = BE * SAV - BILL; // the gap that makes month 30 the crossing (drawing convention, see README)
  const gap = (m) => (m <= 24 ? GAP24 * m / 24 : GAP24 + (GAP30 - GAP24) * (m - 24) / 6);
  // month m is written at time tm(m)
  const tm = (m) => (m <= 24 ? 2.5 + 2.6 * Math.pow(m / 24, 0.85) : 6.9 + (m - 24) * 0.3);
  const cam = [
    [0.0, { x: 720, y: 1060, z: 0.84, tilt: 22, roll: -1.5 }],
    [1.2, { x: 740, y: 1000, z: 0.94, tilt: 21, roll: -1.0 }],
    [2.4, { x: 2180, y: 800, z: 0.60, tilt: 18, roll: 0.5 }],
    [5.3, { x: 2200, y: 790, z: 0.61, tilt: 18, roll: 0.5 }],
    [6.3, { x: 2250, y: 760, z: 0.64, tilt: 17, roll: 0.8 }],
    [8.9, { x: 2230, y: 790, z: 0.62, tilt: 17, roll: 0.6 }],
    [10.0, { x: 2240, y: 790, z: 0.635, tilt: 17, roll: 0.6 }],
  ];

  function build() {
    // --- Closing Disclosure page (reconstructed after the CFPB model form; Nora's figures)
    const P = box(desk, 'paper', 100, 120, 1150, 1400);
    S.P = { e: P, x: 100, y: 120, w: 1150, h: 1400 };
    text(P, 'Closing Disclosure', 60, 50, 60, { w: 700 });
    text(P, 'Nora · refinance · the loan-costs page', 60, 128, 28, { color: C.grid });
    stamp(P, 760, 64, 26, -4);
    box(P, 'abs', 60, 220, 1030, 64, { background: C.bg });
    text(P, 'Loan Costs', 80, 232, 36, { w: 700, color: C.ink });
    const rows = ['A. Origination Charges', 'B. Services Borrower Did Not Shop For', 'C. Services Borrower Did Shop For'];
    rows.forEach((r, i) => {
      const y = 320 + i * 170;
      text(P, r, 70, y, 34, { w: 700 });
      for (let k = 0; k < 2; k++) {
        box(P, 'abs', 110, y + 58 + k * 44, 520 - k * 120, 16, { background: C.grid, opacity: .25, borderRadius: '8px' });
        box(P, 'abs', 900, y + 58 + k * 44, 150, 16, { background: C.grid, opacity: .25, borderRadius: '8px' });
      }
    });
    box(P, 'abs', 60, 830, 1030, 3, { background: C.bg });
    text(P, 'D. TOTAL LOAN COSTS (A + B + C)', 70, 872, 38, { w: 700 });
    S.dHl = highlighter(P, 760, 856, 330, 88, C.warn);
    S.cost = text(P, '$5,124', 1070, 860, 70, { w: 700, align: 'right' });
    text(P, 'paid at closing · nominal $', 70, 930, 28, { color: C.grid });
    text(P, 'Layout after the CFPB model Closing Disclosure. Loan costs: 2025 median,', 70, 1270, 24, { color: C.grid });
    text(P, 'CFPB HMDA. Borrower and other figures are illustrative.', 70, 1302, 24, { color: C.grid });

    // --- reconstructed citation card (public-domain CFPB text, set in our own type)
    const Q = box(desk, 'abs', 560, 1130, 760, 300, { background: C.surface, borderRadius: '6px', boxShadow: '0 20px 40px rgba(0,0,0,.6)' });
    S.Q = { e: Q, x: 560, y: 1130, w: 760, h: 300 };
    box(Q, 'abs', 0, 0, 10, 300, { background: C.accent, borderRadius: '6px 0 0 6px' });
    el('div', Q, 't', { left: '44px', top: '34px', width: '680px', whiteSpace: 'normal', fontSize: '34px', lineHeight: '1.3', color: C.ink, fontWeight: 600 },
      '“A Closing Disclosure is a five-page form that provides final details about the mortgage loan you have selected.”');
    text(Q, '— CFPB, consumerfinance.gov · “What is a Closing Disclosure?”', 44, 236, 24, { color: C.muted });

    // --- ledger: saved each month
    const Lg = box(desk, 'paper lined', 1350, 150, 620, 1300);
    S.Lg = { e: Lg, x: 1350, y: 150, w: 620, h: 1300 };
    text(Lg, 'Saved each month', 40, 40, 44, { w: 700 });
    box(Lg, 'abs', 40, 104, 30, 30, { background: C.positive, borderRadius: '50%' });
    text(Lg, 'Nora', 84, 102, 30, { color: C.grid });
    stamp(Lg, 330, 98, 22, -3);
    const clip = box(Lg, 'abs', 0, 170, 620, 1110, { overflow: 'hidden' });
    S.list = box(clip, 'abs', 0, 0, 620, 3000);
    S.rows = [];
    let y = 0;
    for (let m = 1; m <= BE; m++) {
      const r = box(S.list, 'abs', 0, y, 620, 64);
      text(r, '+ $221', 150, 10, 40, { w: 700, color: C.bg });
      const tick = box(r, 'abs', 50, 18, 28, 28, { background: C.positive, borderRadius: '50%' });
      S.rows.push({ e: r, m, y });
      y += 64;
      if (m === 24) {
        S.slipY = y;
        y += 150;
      }
    }
    S.slip = box(S.list, 'abs', 20, S.slipY + 12, 580, 124, { background: C.ink, border: `5px solid ${C.negative}`, borderRadius: '6px', boxShadow: '0 14px 28px rgba(0,0,0,.35)' });
    text(S.slip, 'balance +$1,133', 30, 18, 52, { w: 700, color: C.negative });
    text(S.slip, 'owed at month 24 vs. the old loan', 32, 82, 24, { color: C.grid });
    stamp(S.slip, 430, -26, 18, 3);

    // --- graph paper: cumulative savings vs. the bill
    const Gp = box(desk, 'paper grid', 2070, 150, 1120, 1300);
    S.Gp = { e: Gp, x: 2070, y: 150, w: 1120, h: 1300 };
    text(Gp, 'Savings pile up against the bill', 60, 40, 44, { w: 700 });
    const X0 = 90, W = 960, BASE = 1010, H = 800, MMAX = 32, VMAX = 7200;
    const X = (m) => X0 + m / MMAX * W, Yv = (v) => BASE - v / VMAX * H;
    S.X = X; S.Yv = Yv;
    const g = svg(Gp, 0, 0, 1120, 1300);
    sv(g, 'line', { x1: X0, y1: BASE, x2: X0 + W, y2: BASE, stroke: C.bg, 'stroke-width': 4 }); // zero baseline
    S.band = sv(g, 'path', { fill: 'url(#hatch)', stroke: C.negative, 'stroke-width': 3 });
    S.cols = [];
    for (let m = 1; m <= BE; m++) {
      const c = sv(g, 'rect', { x: X(m) - 12.5, y: Yv(m * SAV), width: 25, height: BASE - Yv(m * SAV), fill: C.positive, opacity: 0 });
      S.cols.push(c);
    }
    // hidden part: balance gap on top of the bill (red hatch)
    const defs = sv(g, 'defs', {});
    const pat = sv(defs, 'pattern', { id: 'hatch', width: 16, height: 16, patternUnits: 'userSpaceOnUse', patternTransform: 'rotate(45)' });
    sv(pat, 'rect', { width: 16, height: 16, fill: C.negative, opacity: .22 });
    sv(pat, 'rect', { width: 6, height: 16, fill: C.negative, opacity: .85 });
    S.bandTop = (mEnd) => {
      let d = `M${X(0)},${Yv(BILL)}`;
      for (let m = 0; m <= mEnd + 1e-9; m += 0.5) d += ` L${X(m)},${Yv(BILL + gap(m))}`;
      d += ` L${X(mEnd)},${Yv(BILL)} Z`;
      return d;
    };
    S.bill = penPrep(sv(g, 'line', { x1: X0, y1: Yv(BILL), x2: X0 + W, y2: Yv(BILL), stroke: C.bg, 'stroke-width': 7, 'stroke-linecap': 'round' }));
    S.billLbl = text(Gp, 'loan costs $5,124', X0 + 10, Yv(BILL) + 16, 48, { w: 700 });
    S.bandLbl = text(Gp, '+ balance gap', X0 + 10, Yv(BILL + GAP30) - 76, 44, { w: 700, color: C.negative });
    // month markers
    S.m24 = text(Gp, '24', X(24), BASE + 14, 60, { w: 700, align: 'center' });
    text(Gp, 'months after refinancing →', X0, BASE + 30, 32, { w: 600, color: C.grid });
    S.m30 = text(Gp, '30', X(30), BASE + 14, 60, { w: 700, align: 'center', color: C.bg });
    S.loop24 = penPrep(sv(g, 'path', { d: loopPath(X(24), Yv(BILL), 50, 44, 3), fill: 'none', stroke: C.accent, 'stroke-width': 6, 'stroke-linecap': 'round' }));
    S.strike24 = penPrep(sv(g, 'path', { d: `M${X(24) - 46},${BASE + 58} L${X(24) + 46},${BASE + 42}`, stroke: C.negative, 'stroke-width': 9, 'stroke-linecap': 'round', fill: 'none' }));
    S.loop30 = penPrep(sv(g, 'path', { d: loopPath(X(30), Yv(BILL + gap(30)), 54, 48, 7), fill: 'none', stroke: C.accent, 'stroke-width': 7, 'stroke-linecap': 'round' }));
    S.loopM30 = penPrep(sv(g, 'path', { d: loopPath(X(30), BASE + 48, 56, 46, 9), fill: 'none', stroke: C.accent, 'stroke-width': 6, 'stroke-linecap': 'round' }));
    S.gStamp = stamp(Gp, 760, 44, 24, 3);
    text(Gp, 'each column: total saved by that month · nominal $', 60, 1200, 26, { color: C.grid });

    // flying copy of the $5,124 (lifted off the form)
    S.fly = text(desk, '$5,124', 0, 0, 70, { w: 700, color: C.bg, style: { background: C.warn, padding: '4px 14px', borderRadius: '6px', boxShadow: '0 30px 40px rgba(0,0,0,.45)' } });
    S.items = [S.P, S.Q, S.Lg, S.Gp];
  }

  function update(t) {
    setCam(camAt(cam, t));
    hl(S.dHl, seg(t, 0.6, 1.1));
    // lift the number and carry it to the bill line
    const pf = ease(seg(t, 1.3, 2.3));
    const a = { x: 100 + 800, y: 120 + 856 }, b = { x: 2070 + 90 + 330, y: 150 + S.Yv(BILL) - 76 };
    S.fly.style.left = lerp(a.x, b.x, pf) + 'px';
    S.fly.style.top = lerp(a.y, b.y, pf) + 'px';
    const z = Math.sin(pf * Math.PI) * 160 + 20;
    S.fly.style.transform = `translateZ(${z}px) rotate(${lerp(0, -3, Math.sin(pf * Math.PI))}deg)`;
    S.fly.style.opacity = t > 1.3 && t < 2.45 ? 1 : 0;
    pen(S.bill, seg(t, 2.2, 2.6));
    S.billLbl.style.opacity = easeOut(seg(t, 2.3, 2.6));
    // ledger rows and columns
    let n = 0;
    for (let m = 1; m <= BE; m++) if (t >= tm(m)) n = m;
    S.rows.forEach((r) => { r.e.style.opacity = r.m <= n ? 1 : 0; });
    S.cols.forEach((c, i) => { c.setAttribute('opacity', i < n ? (i === n - 1 ? 0.95 : 0.8) : 0); });
    // slip enters between month 24 and 25
    const ps = back(seg(t, 5.6, 6.2));
    S.slip.style.opacity = t > 5.6 ? 1 : 0;
    S.slip.style.transform = `translate(${lerp(640, 0, ps)}px, ${lerp(-60, 0, ps)}px) rotate(${lerp(6, -1.5, ps)}deg)`;
    // rows after the slip appear below it (the slip pushes the list)
    const lastY = n >= 25 ? S.rows[n - 1].y + 64 : (t > 5.6 ? S.slipY + 150 : (n ? S.rows[n - 1].y + 64 : 0));
    S.list.style.transform = `translateY(${-Math.max(0, lastY - 1040)}px)`;
    // hidden part raises the bill
    const pb = ease(seg(t, 6.0, 6.7));
    const mEnd = t < 6.9 ? 24 * pb : Math.min(BE, 24 + (t - 6.9) / 0.3);
    S.band.setAttribute('d', S.bandTop(Math.max(0.01, mEnd)));
    S.band.style.opacity = t > 6.0 ? 1 : 0;
    S.bandLbl.style.opacity = easeOut(seg(t, 6.3, 6.7));
    // month 24 (simple division), then crossed out; month 30
    S.m24.style.opacity = t > tm(24) ? 1 : 0;
    pen(S.loop24, seg(t, tm(24), tm(24) + 0.35) * (t < 6.0 ? 1 : 1 - seg(t, 6.0, 6.3)));
    S.loop24.style.opacity = t > tm(24) && t < 6.3 ? 1 : 0;
    pen(S.strike24, seg(t, 6.4, 6.7));
    S.m24.style.color = t > 6.4 ? C.grid : C.bg;
    S.m30.style.opacity = t > tm(30) ? 1 : 0;
    pen(S.loop30, seg(t, tm(30), tm(30) + 0.35));
    pen(S.loopM30, seg(t, tm(30) + 0.2, tm(30) + 0.6));
    S.gStamp.style.opacity = t > 2.4 ? 1 : 0;
    dof(S.items, 5);
  }
  window.SCENE = { dur: DUR, build, update };
})();
