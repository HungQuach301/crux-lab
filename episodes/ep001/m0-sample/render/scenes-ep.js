'use strict';
// A-M0 sample scene: the weekly 30-year rate (MORTGAGE30US) draws from 1971; the peak lands on the spoken "18.63%".
(function () {
  const { B, K } = window.SCENES;
  const { D, C, clamp, smooth, easeOut, back, fade, S, Tx, L1, claim, env } = K;
  const M = D.model;
  const N = M.series.length;
  const iPeak = M.series.findIndex((r) => r[0] === M.peak[0]);
  const x0 = 260, x1 = 1660, yb = 880, yt = 280;
  const X = (i) => x0 + (x1 - x0) * i / (N - 1), Y = (v) => yb - (yb - yt) * v / 20;
  const cue = (w) => D.cues['m0.1|' + w];
  window.CAMS.CAM['m0-rates'] = { f: 35, base: { z: -260 }, moves: [[0.6, 1.4, { z: 260 }]] };

  B['m0-rates'] = (L, sc, H) => {
    const items = []; env(items, 'm0', { glow: 0.06, floor: 0.6 });
    const t71 = H.local(cue('1971')), tPk = H.local(cue('18.63%')), t81 = H.local(cue('1981')), t30 = H.local(cue('30')), tHold = tPk + 1.0, tEnd = tHold + 2.4;
    // progress: 1971 -> the peak while the sentence builds to "18.63%", a 1 s hold, then the long fall to 2026 (eased)
    const i = L < tPk ? iPeak * smooth((L - t71) / (tPk - t71)) : iPeak + (N - 1 - iPeak) * smooth((L - tHold) / (tEnd - tHold)); // holds 1 s on the peak (breathing room after the number)
    const n = Math.max(1, Math.round(i));
    const pts = M.series.slice(0, n + 1).map((r, k) => [X(k), Y(r[1])]);
    items.push(S('m0-axis', 'polyline', { panel: 'm0', chart: 'rates', z: 0, pts: [[x0, yb + 12], [x1, yb + 12]], stroke: C.muted, lw: 2, meta: { role: 'axis', panel: 'm0', chart: 'rates' } }));
    if (L >= t71 - 1 / 60) items.push(S('m0-rate', 'polyline', { panel: 'm0', chart: 'rates', z: 0, pts, stroke: C.rate, lw: 4, curve: true, meta: { role: 'series', panel: 'm0', chart: 'rates', series: 'rate', shape: 'solid', label: 'm0-lab' } }));
    const a = H.P(x0, yb + 12, 0), b = H.P(x1, yb + 12, 0);
    items.push(Tx('m0-a0', '1971', a[0], a[1] + 44, 30, C['text-dim'], { sharp: true, role: 'axis-label', anchor: 'rates', chart: 'rates', year: 1971, align: 'center', claims: [claim('y1971')], alpha: L >= t71 - 1 / 60 ? 1 : 0 }));
    items.push(Tx('m0-a1', '2026', b[0], b[1] + 44, 30, C['text-dim'], { sharp: true, role: 'axis-label', anchor: 'rates', chart: 'rates', year: 2026, align: 'center', claims: [claim('y2026')], alpha: L >= t71 - 1 / 60 ? 1 : 0 })); // both anchors while the line is on screen (C04)
    const lab = H.P(x0 + 10, 740, 0);
    items.push(Tx('m0-lab', 'weekly average', lab[0], lab[1], 28, C['text-dim'], { sharp: true, series: 'rate', alpha: fade(L, t71 + 0.3, 0.3) }));
    // the peak: dot + value on the spoken number, the year on "1981"
    const pk = H.P(X(iPeak), Y(M.peak[1]), 0);
    if (L >= tPk - 1 / 60) {
      items.push(S('m0-peak', 'circle', { panel: 'm0', chart: 'rates', z: 0, c: [X(iPeak), Y(M.peak[1])], r: 11 * back((L - tPk + 1 / 60) / 0.3), fill: C.warn, meta: { role: 'mark', panel: 'm0', chart: 'rates', series: 'rate' } }));
      items.push(Tx('m0-peak-l', '18.63%', pk[0] + 26, pk[1] - 20, 48, C.text, { sharp: true, weight: 700, level: 2, claims: [claim('peak')] }));
    }
    items.push(Tx('m0-peak-y', 'in 1981', pk[0] + 28, pk[1] + 26, 30, C['text-dim'], { sharp: true, claims: [claim('y1981')], alpha: L >= t81 - 1 / 60 ? 1 : 0 }));
    items.push(L1('m0-l1', '30-year fixed rate', 1280, 360, 60, clamp((L - t30 + 0.05) / 0.1), { sharp: true, claims: [claim('term30')] }));
    return items;
  };
})();
