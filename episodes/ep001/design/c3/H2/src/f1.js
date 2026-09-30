'use strict';
// F1 · Cold open: the missed window. Claims: low2026, low2026_date, low2026_since, oct2023, r_old, sav_low2026_median (ILL.),
// seven, r_today, anchor_date, first7_since, term30. Weekly rates come from the local FRED file at render time (not in repo).
(function () {
  const { desk, clamp, lerp, ease, easeOut, back, seg, el, box, text, svg, sv, penPrep, pen, loopPath, highlighter, hl, stamp, camAt, setCam, dof, lift, C } = window.K;
  let S = {};
  const DUR = 9.0;
  const cam = [
    [0.0, { x: 880, y: 580, z: 0.74, tilt: 26, roll: -2.2 }],
    [0.4, { x: 880, y: 580, z: 0.74, tilt: 26, roll: -2.2 }],
    [1.9, { x: 900, y: 820, z: 0.98, tilt: 23, roll: -1.2 }],
    [2.9, { x: 910, y: 850, z: 1.02, tilt: 22, roll: -1.0 }],
    [4.1, { x: 2130, y: 720, z: 1.00, tilt: 20, roll: 1.0 }],
    [4.7, { x: 2130, y: 720, z: 1.00, tilt: 20, roll: 1.0 }],
    [5.7, { x: 1380, y: 640, z: 0.64, tilt: 17, roll: 0 }],
    [6.9, { x: 1400, y: 640, z: 0.65, tilt: 17, roll: 0 }],
    [7.9, { x: 1660, y: 640, z: 0.64, tilt: 16, roll: 0.4 }],
    [9.0, { x: 1680, y: 645, z: 0.66, tilt: 16, roll: 0.5 }],
  ];

  function build(D) {
    const wk = D.weekly.filter((r) => r[0] >= '2025-01-01' && r[0] <= '2026-09-24');
    const t0 = Date.parse(wk[0][0]), t1 = Date.parse(wk[wk.length - 1][0]);
    const CW = 1380, CH = 540, y0 = 5.75, y1 = 7.35;
    const X = (d) => (Date.parse(d) - t0) / (t1 - t0) * CW;
    const Y = (r) => CH - (r - y0) / (y1 - y0) * CH;

    // --- sheet A: the printed data sheet
    const A = box(desk, 'paper', 120, 140, 1500, 1060);
    S.A = { e: A, x: 120, y: 140, w: 1500, h: 1060 };
    text(A, '30-year fixed mortgage rate, US · weekly average', 60, 48, 46, { w: 700 });
    text(A, 'Freddie Mac Primary Mortgage Market Survey', 60, 108, 28, { color: C.grid });
    const g = svg(A, 60, 170, CW, CH);
    sv(g, 'line', { x1: 0, y1: CH, x2: CW, y2: CH, stroke: C.grid, 'stroke-width': 2 });
    sv(g, 'line', { x1: 0, y1: Y(7), x2: CW, y2: Y(7), stroke: C.grid, 'stroke-width': 2, 'stroke-dasharray': '10 10' });
    S.sevenLbl = text(A, '7%', 60 + 90, 170 + Y(7) - 44, 34, { w: 700, color: C.grid });
    // window band: weeks at least 1 point below Nora's rate (<= 6.62) — green highlighter under the line
    // longest contiguous run of weeks <= 6.62 (the 2025-26 window), split at the low
    let runs = [], cur = [];
    wk.forEach((r) => { if (+r[1] <= 6.62) cur.push(r); else { if (cur.length) runs.push(cur); cur = []; } });
    if (cur.length) runs.push(cur);
    const win = runs.sort((a, b) => b.length - a.length)[0];
    const iw = win.findIndex((r) => r[0] === '2026-02-26');
    const P_ = (arr) => 'M' + arr.map((r) => X(r[0]).toFixed(1) + ',' + Y(+r[1]).toFixed(1)).join(' L');
    const wa = { fill: 'none', stroke: C.positive, 'stroke-width': 34, 'stroke-linecap': 'round', 'stroke-linejoin': 'round', opacity: .45 };
    S.winA = penPrep(sv(g, 'path', Object.assign({ d: P_(win.slice(0, iw + 1)) }, wa)));
    S.winB = penPrep(sv(g, 'path', Object.assign({ d: P_(win.slice(iw)) }, wa)));
    const path = 'M' + wk.map((r) => X(r[0]).toFixed(1) + ',' + Y(+r[1]).toFixed(1)).join(' L');
    S.line = sv(g, 'path', { d: path, fill: 'none', stroke: C.accent, 'stroke-width': 7, 'stroke-linejoin': 'round', 'stroke-linecap': 'round' });
    S.lineL = S.line.getTotalLength();
    // length at which the low / end sit
    const iLow = wk.findIndex((r) => r[0] === '2026-02-26');
    const sub = sv(g, 'path', { d: 'M' + wk.slice(0, iLow + 1).map((r) => X(r[0]).toFixed(1) + ',' + Y(+r[1]).toFixed(1)).join(' L'), fill: 'none', stroke: 'none' });
    S.lowFrac = sub.getTotalLength() / S.lineL;
    S.line.style.strokeDasharray = S.lineL + ' ' + S.lineL;
    S.pen = sv(g, 'circle', { r: 11, fill: C.bg });
    S.pts = wk.map((r) => [X(r[0]), Y(+r[1])]);
    S.sub = S.line;
    const lx = X('2026-02-26'), ly = Y(5.98);
    S.lowDot = sv(g, 'circle', { cx: lx, cy: ly, r: 12, fill: C.accent, stroke: C.ink, 'stroke-width': 4 });
    S.lowLoop = penPrep(sv(g, 'path', { d: loopPath(lx, ly, 70, 52, 2), fill: 'none', stroke: C.accent, 'stroke-width': 6, 'stroke-linecap': 'round' }));
    // end point + Jan 2025 point (first time above 7% since)
    const ex = X('2026-09-24'), ey = Y(7.03);
    const jx = X('2025-01-16'), jy = Y(7.04);
    S.endDot = sv(g, 'circle', { cx: ex, cy: ey, r: 13, fill: C.accent, stroke: C.ink, 'stroke-width': 4 });
    S.janDot = sv(g, 'circle', { cx: jx, cy: jy, r: 11, fill: C.ink, stroke: C.accent, 'stroke-width': 5 });
    S.arc = penPrep(sv(g, 'path', { d: `M${jx + 8},${jy - 16} C ${jx + 300},${Y(7) - 70} ${ex - 300},${Y(7) - 70} ${ex - 8},${ey - 18}`, fill: 'none', stroke: C.accent, 'stroke-width': 4, 'stroke-dasharray': '2 12', 'stroke-linecap': 'round' }));
    S.arc.setAttribute('stroke-dasharray', S.arc._L + ' ' + S.arc._L);
    S.endLbl = box(A, 'abs', 60 + CW - 700, 170 + Y(6.30), 700, 200);
    text(S.endLbl, '7.03%', 700, 0, 100, { w: 700, align: 'right', color: C.bg });
    text(S.endLbl, 'week ending', 700, 110, 30, { w: 600, align: 'right', color: C.bg });
    text(S.endLbl, 'September 24, 2026', 700, 146, 30, { w: 600, align: 'right', color: C.bg });
    S.endLoop = penPrep(sv(g, 'path', { d: loopPath(ex, ey, 44, 38, 5), fill: 'none', stroke: C.accent, 'stroke-width': 6, 'stroke-linecap': 'round' }));
    S.janLbl = text(A, 'first time above 7% since January 2025', 60 + CW - 760, 170 + Y(7) - 116, 32, { w: 700, color: C.accent });

    // table fragment under the chart: only the claim row is in focus
    const T = box(A, 'abs', 60, 760, 1380, 250);
    text(T, 'Week ending', 0, 0, 24, { w: 600, color: C.grid });
    text(T, 'Rate', 560, 0, 24, { w: 600, color: C.grid, align: 'right' });
    const rows = [['2026-02-12', ''], ['2026-02-19', ''], ['2026-02-26', 'LOW'], ['2026-03-05', ''], ['2026-03-12', '']];
    rows.forEach((r, i) => {
      const y = 38 + i * 42;
      const v = wk.find((w) => w[0] === r[0]);
      if (r[1] === 'LOW') {
        S.rowHl = highlighter(T, -12, y - 6, 600, 44, C.accent);
        text(T, 'February 26, 2026', 0, y, 32, { w: 700 });
        text(T, '5.98%', 560, y, 32, { w: 700, align: 'right' });
        S.rowNote = text(T, '← lowest since September 2022', 610, y, 32, { w: 700, color: C.accent });
      } else {
        const d = new Date(r[0] + 'T12:00:00Z');
        text(T, d.toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric', timeZone: 'UTC' }), 0, y, 30, { cls: 'blurred', color: C.grid });
        text(T, (+v[1]).toFixed(2) + '%', 560, y, 30, { cls: 'blurred', color: C.grid, align: 'right' });
      }
    });
    text(A, 'Source: Freddie Mac via FRED · fred.stlouisfed.org/series/MORTGAGE30US', 60, 1012, 22, { color: C.grid });

    // --- Nora's file (folder + sheet)
    const F = box(desk, 'folder', 1760, 200, 800, 960);
    S.F = { e: F, x: 1760, y: 200, w: 800, h: 960 };
    box(F, 'abs', 40, -46, 440, 60, { background: '#9aa4b2', borderRadius: '8px 8px 0 0' });
    text(F, 'NORA · MORTGAGE FILE', 64, -34, 26, { w: 700, color: C.bg });
    const P = box(F, 'paper', 30, 34, 740, 890);
    text(P, 'Borrower', 50, 50, 26, { color: C.grid });
    text(P, 'Nora', 50, 84, 54, { w: 700 });
    stamp(P, 330, 70, 26, -5);
    box(P, 'abs', 50, 170, 640, 3, { background: C.grid });
    text(P, 'Borrowed', 50, 200, 26, { color: C.grid });
    text(P, 'October 2023', 50, 234, 44, { w: 600 });
    text(P, 'Rate · 30-year fixed', 50, 312, 26, { color: C.grid });
    text(P, '7.62%', 50, 344, 104, { w: 700 });
    box(P, 'abs', 190, 100, 34, 34, { background: C.positive, borderRadius: '50%' }); // Nora marker (circle)

    // the slip: what refinancing at the low would have saved
    const L = box(desk, 'paper lined', 1830, 740, 700, 330);
    S.L = { e: L, x: 1830, y: 740, w: 700, h: 330 };
    text(L, 'Refinance at the February low (5.98%):', 36, 36, 30, { w: 600 });
    S.slipHl = highlighter(L, 24, 112, 620, 100, C.positive);
    S.slipNum = text(L, '−$459 / month', 40, 114, 80, { w: 700 });
    text(L, 'payment, nominal $', 40, 230, 24, { color: C.grid });
    S.slipStamp = stamp(L, 390, 236, 22, 4);
    const ls = svg(L, 0, 0, 700, 330);
    S.strike1 = penPrep(sv(ls, 'path', { d: 'M20,176 C 180,150 420,190 610,148', fill: 'none', stroke: C.negative, 'stroke-width': 11, 'stroke-linecap': 'round' }));
    S.strike2 = penPrep(sv(ls, 'path', { d: 'M28,196 C 220,172 430,206 600,170', fill: 'none', stroke: C.negative, 'stroke-width': 8, 'stroke-linecap': 'round' }));
    S.items = [S.A, S.F, S.L];
    S.g = g;
  }

  function update(t) {
    setCam(camAt(cam, t));
    // line prints: to the low 0.3–1.9 s, then the rest 4.9–6.7 s
    const p1 = ease(seg(t, 0.3, 1.9)) * S.lowFrac;
    const p2 = seg(t, 4.9, 6.7);
    const frac = p2 > 0 ? S.lowFrac + (1 - S.lowFrac) * easeOut(p2) : p1;
    S.line.style.strokeDashoffset = S.lineL * (1 - frac);
    const pt = S.line.getPointAtLength(S.lineL * frac);
    S.pen.setAttribute('cx', pt.x); S.pen.setAttribute('cy', pt.y);
    S.pen.style.opacity = (t > 0.25 && t < 1.95) || (t > 4.85 && t < 6.75) ? 1 : 0;
    S.lowDot.style.opacity = t > 1.9 ? 1 : 0;
    pen(S.lowLoop, seg(t, 1.9, 2.5));
    hl(S.rowHl, seg(t, 2.0, 2.4));
    S.rowNote.style.opacity = easeOut(seg(t, 2.3, 2.6));
    pen(S.winA, seg(t, 2.5, 3.1));
    pen(S.winB, easeOut(seg(t, 4.95, 6.0)));
    // slip arrives on Nora's file
    const sp = back(seg(t, 3.2, 3.9));
    lift(S.L.e, 60 * (1 - seg(t, 3.9, 4.3)) + 12, lerp(8, -3, sp), lerp(700, 0, sp), lerp(-120, 0, sp));
    S.L.e.style.opacity = t > 3.2 ? 1 : 0;
    hl(S.slipHl, seg(t, 3.9, 4.3));
    // rise past 7%: end label + 'since January 2025'
    S.endDot.style.opacity = t > 6.7 ? 1 : 0;
    pen(S.endLoop, seg(t, 6.7, 7.1));
    S.endLbl.style.opacity = easeOut(seg(t, 6.6, 6.95));
    S.sevenLbl.style.color = t > 6.3 ? C.accent : C.grid;
    S.janDot.style.opacity = easeOut(seg(t, 6.9, 7.1));
    pen(S.arc, seg(t, 6.95, 7.5));
    S.janLbl.style.opacity = easeOut(seg(t, 7.2, 7.5));
    // the missed saving is crossed out
    pen(S.strike1, seg(t, 7.7, 8.05));
    pen(S.strike2, seg(t, 7.95, 8.25));
    S.slipNum.style.opacity = 1 - 0.35 * seg(t, 8.0, 8.4);
    dof(S.items, 5);
  }
  window.SCENE = { dur: DUR, build, update };
})();
