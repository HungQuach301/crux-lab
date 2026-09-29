'use strict';
// F3 · Walt and Anjali. Claims: loan_small $115,000, cost_small $3,667, sav_small $68, cut36_small 1.12 (Walt);
// loan_large $655,000, cost_large $5,514, sav_large $387, cut36_large 0.32 / cut36_large_words (Anjali); hold36 36; oct2023; s10 1.
(function () {
  const { desk, clamp, lerp, ease, easeOut, back, seg, el, box, text, svg, sv, penPrep, pen, loopPath, highlighter, hl, stamp, camAt, setCam, dof, lift, C } = window.K;
  const S = {};
  const DUR = 9.5;
  const P = {
    walt: { name: 'Walt', col: C.warn, shape: 'tri', vals: [115000, 3667.05, 67.87], txt: ['$115,000', '$3,667', '$68'], cut: 1.12, cutTxt: '1.12' },
    anjali: { name: 'Anjali', col: C.negative, shape: 'sq', vals: [655000, 5513.97, 386.54], txt: ['$655,000', '$5,514', '$387'], cut: 0.32, cutTxt: '0.32' },
  };
  const ROWS = ['Loan', 'Loan costs', 'Saves per month'];
  const CAP = ['very different', 'about the same', 'very different'];
  const BEAT = [1.2, 3.0, 4.8]; // highlight start of each row
  const cam = [
    [0.0, { x: 1350, y: 520, z: 0.56, tilt: 21, roll: -1.0 }],
    [1.1, { x: 1300, y: 900, z: 0.455, tilt: 18, roll: -0.5 }],
    [2.9, { x: 1260, y: 910, z: 0.46, tilt: 18, roll: -0.3 }],
    [4.7, { x: 1360, y: 910, z: 0.46, tilt: 18, roll: 0 }],
    [6.5, { x: 1480, y: 910, z: 0.46, tilt: 18, roll: 0.3 }],
    [7.5, { x: 2140, y: 930, z: 0.455, tilt: 17, roll: 0.6 }],
    [9.5, { x: 2160, y: 930, z: 0.465, tilt: 17, roll: 0.6 }],
  ];
  function marker(parent, shape, x, y, s, col) {
    const g = svg(parent, x - s / 2, y - s / 2, s, s);
    if (shape === 'tri') sv(g, 'polygon', { points: `${s / 2},2 ${s - 2},${s - 2} 2,${s - 2}`, fill: col });
    else sv(g, 'rect', { x: 3, y: 3, width: s - 6, height: s - 6, fill: col });
    return g;
  }

  function build() {
    S.items = []; S.hls = []; S.flies = []; S.bars = []; S.caps = [];
    // --- the two loan files
    [['walt', 200], ['anjali', 1450]].forEach(([k, x]) => {
      const p = P[k];
      const F = box(desk, 'folder', x, 100, 1050, 820);
      S.items.push({ e: F, x, y: 100, w: 1050, h: 820 });
      box(F, 'abs', 40, -46, 460, 60, { background: '#9aa4b2', borderRadius: '8px 8px 0 0' });
      text(F, p.name.toUpperCase() + ' · MORTGAGE FILE', 64, -34, 26, { w: 700, color: C.bg });
      const Pp = box(F, 'paper', 30, 34, 990, 760);
      text(Pp, p.name, 50, 36, 70, { w: 700 });
      marker(Pp, p.shape, 50 + (k === 'walt' ? 190 : 250), 78, 50, p.col);
      stamp(Pp, 620, 52, 26, -4);
      text(Pp, 'Borrowed October 2023 · refinance offer', 50, 130, 30, { color: C.grid });
      ROWS.forEach((r, i) => {
        const y = 230 + i * 170;
        box(Pp, 'abs', 50, y - 20, 890, 3, { background: C.grid, opacity: .6 });
        text(Pp, r, 50, y + 30, 38, { w: 600, color: C.grid });
        const h = highlighter(Pp, 470, y + 6, 480, 110, p.col);
        S.hls.push({ e: h, i });
        text(Pp, p.txt[i], 940, y + 12, 88, { w: 700, align: 'right' });
      });
      text(Pp, 'nominal $', 50, 720, 22, { color: C.grid });
      p.fileX = x + 30; p.fileY = 100 + 34;
    });

    // --- chart strip: each row pulled out as a pair of bars (own scale per pair, zero baseline)
    const St = box(desk, 'paper grid', 200, 980, 2300, 740);
    S.items.push({ e: St, x: 200, y: 980, w: 2300, h: 740 });
    const BASE = 520, HMAX = 330, BW = 170;
    ROWS.forEach((r, i) => {
      const cx = 60 + i * 760;
      text(St, r, cx, 40, 46, { w: 700 });
      const g = svg(St, cx, 0, 700, 800);
      sv(g, 'line', { x1: 0, y1: BASE, x2: 640, y2: BASE, stroke: C.bg, 'stroke-width': 4 });
      const max = Math.max(P.walt.vals[i], P.anjali.vals[i]);
      [['walt', 110], ['anjali', 370]].forEach(([k, bx]) => {
        const p = P[k];
        const h = p.vals[i] / max * HMAX;
        const rect = sv(g, 'rect', { x: bx, y: BASE, width: BW, height: 0, fill: p.col });
        const lbl = text(St, p.txt[i], cx + bx + BW / 2, BASE - h - 78, 58, { w: 700, align: 'center' });
        lbl.style.opacity = 0;
        marker(St, p.shape, cx + bx + BW / 2, BASE + 44, 42, p.col);
        S.bars.push({ rect, h, lbl, i, k, BASE });
        // flying copy from the file row to the bar label
        const fx = p.fileX + 940, fy = p.fileY + 230 + i * 170 + 12;
        const f = text(desk, p.txt[i], 0, 0, 88, { w: 700, color: C.bg, style: { background: p.col, padding: '2px 12px', borderRadius: '6px', boxShadow: '0 30px 40px rgba(0,0,0,.45)' } });
        f.style.opacity = 0;
        S.flies.push({ e: f, i, a: { x: fx - 400, y: fy }, b: { x: 200 + cx + bx + BW / 2 - 170, y: 980 + BASE - h - 88 } });
      });
      S.caps.push(text(St, CAP[i], cx + 320, BASE + 84, 48, { w: 700, align: 'center', color: i === 1 ? C.bg : C.grid }));
    });
    text(St, 'each pair on its own scale · nominal $', 60, 680, 26, { color: C.grid });

    // --- ruler: rate cut needed to get the fees back within 36 months
    const R = box(desk, 'paper', 2620, 100, 780, 1700);
    S.items.push({ e: R, x: 2620, y: 100, w: 780, h: 1700 });
    text(R, 'Rate cut needed', 50, 40, 60, { w: 700 });
    text(R, 'to get the fees back within 36 months', 50, 116, 32, { color: C.grid });
    stamp(R, 440, 170, 24, -3);
    const Z0 = 1540, PT = 1000; // y of zero, px per point
    const g = svg(R, 0, 0, 780, 1700);
    sv(g, 'line', { x1: 200, y1: Z0, x2: 200, y2: Z0 - 1.25 * PT, stroke: C.bg, 'stroke-width': 6 });
    for (let v = 0; v <= 1.25 + 1e-9; v += 0.125) {
      const major = Math.abs(v * 4 - Math.round(v * 4)) < 1e-6;
      sv(g, 'line', { x1: 200, y1: Z0 - v * PT, x2: major ? 250 : 228, y2: Z0 - v * PT, stroke: C.bg, 'stroke-width': major ? 5 : 3 });
    }
    sv(g, 'line', { x1: 120, y1: Z0 - PT, x2: 740, y2: Z0 - PT, stroke: C.grid, 'stroke-width': 3, 'stroke-dasharray': '12 10' });
    text(R, '1 point', 520, Z0 - PT + 14, 40, { w: 600, color: C.grid });
    text(R, 'no cut', 40, Z0 - 22, 30, { color: C.grid });
    S.rm = ['walt', 'anjali'].map((k) => {
      const p = P[k];
      const m = marker(R, p.shape, 200, Z0, 64, p.col);
      const lb = box(R, 'abs', 270, 0, 480, 160);
      text(lb, p.cutTxt, 0, 0, 88, { w: 700, color: C.bg });
      text(lb, p.name + (k === 'anjali' ? ' · about a third of a point' : ' · more than a full point'), 4, 98, 30, { w: 600, color: C.grid });
      lb.style.opacity = 0;
      return { m, lb, target: Z0 - p.cut * PT, Z0 };
    });
  }

  function update(t) {
    setCam(camAt(cam, t));
    S.hls.forEach((h) => hl(h.e, seg(t, BEAT[h.i], BEAT[h.i] + 0.35)));
    S.flies.forEach((f) => {
      const t0 = BEAT[f.i] + 0.35, p = ease(seg(t, t0, t0 + 0.75));
      f.e.style.left = lerp(f.a.x, f.b.x, p) + 'px';
      f.e.style.top = lerp(f.a.y, f.b.y, p) + 'px';
      f.e.style.transform = `translateZ(${Math.sin(p * Math.PI) * 220 + 10}px) scale(${lerp(1, 0.66, p)})`;
      f.e.style.opacity = t > t0 && t < t0 + 0.8 ? 1 : 0;
    });
    S.bars.forEach((b) => {
      const t0 = BEAT[b.i] + 1.0, p = back(seg(t, t0, t0 + 0.55));
      const h = Math.max(0, b.h * p);
      b.rect.setAttribute('y', b.BASE - h); b.rect.setAttribute('height', h);
      b.lbl.style.opacity = t > BEAT[b.i] + 1.1 ? 1 : 0;
    });
    S.caps.forEach((c, i) => { c.style.opacity = easeOut(seg(t, BEAT[i] + 1.5, BEAT[i] + 1.8)); });
    S.rm.forEach((r, j) => {
      const t0 = 7.3 + j * 0.35, p = back(seg(t, t0, t0 + 0.8));
      r.m.style.top = (lerp(r.Z0, r.target, p) - 32) + 'px';
      r.lb.style.top = (r.target - 60) + 'px';
      r.lb.style.opacity = easeOut(seg(t, t0 + 0.7, t0 + 1.0));
    });
    dof(S.items, 5);
  }
  window.SCENE = { dur: DUR, build, update };
})();
