// S16 · If Walt sells after three years. Kết hợp: H1 Walt's yard at 3 years: 36 bundles of $68 still short of the
// ream + hatched slab ($1,777 short) -> H3 rate-cut ruler: Walt's triangle slides past the 1-point line to 1.12;
// Nora's 0.5 beside it (smaller house -> bigger cut); two rows: the bill barely shrinks, savings shrink.
import { THREE, C, W, H, DATA, CL, text, chrome, line, rect, mark, ease, easeOut, back, mix, inout , withObj } from './engine.js';
import { monthRuler, cutRuler, houseIcon, PL } from './common.js';
import { makeYard } from './yard.js';
export const uses3d = true;

export function build(ctx0) {
  const { T, camera } = ctx0;
  const tSe = T.a('sell'), tSh = T.a('short'), tC = T.a('cut'), tM = T.a('more'), tWy = T.a('why'), tF = T.a('fees'), tS = T.a('savings');
  const Y = makeYard(ctx0, { who: ['walt'], K: 2.2 / 4300, months: 36 });
  const w = Y.out.walt;
  const month = (t) => 36 * ease(t, tSe, tSh - 0.3);
  function update(t) {
    camera.position.set(w.x + 0.8, 2.3, mix(8.2, 7.8, ease(t, 0, tC))); camera.lookAt(w.x + 0.7, 1.1, w.Z - 1.0);
    Y.update('walt', { houseGrow: 1, reamIn: 1, month: month(t), owedOn: 1, colOn: 1, laser: 1, laserRed: t > tSh - 0.3, lit: 0.6 });
  }
  function yard(ctx, t, P) {
    text(ctx, 'If Walt sells after ' + CL('y3') + ' years', 96, 128, 'head', { shadow: true });
    const top = P(new THREE.Vector3((w.x + w.xs) / 2, w.rh + w.gapAt(36) * Y.K, w.Z));
    const aS = easeOut(t, tSh, tSh + 0.4);
    text(ctx, CL('net36_small') + ' short', 1250, 420, 'number', { color: '#FF8A8E', alpha: aS, plate: PL });
    text(ctx, 'after ' + CL('y3') + ' years, savings still', 1250, 490, 'label', { alpha: aS, plate: PL });
    text(ctx, 'below loan costs', 1250, 546, 'label', { alpha: aS, plate: PL });
    text(ctx, '+ extra owed', 1250, 602, 'label', { alpha: aS, plate: PL });
    const pr = P(new THREE.Vector3(w.x - w.FW / 2, 0.7, w.Z + w.FD / 2)), pc = P(new THREE.Vector3(w.xs + w.FW / 2, 0.3, w.Z + w.FD / 2));
    text(ctx, 'loan costs', pr.x - 24, pr.y - 30, 'label', { align: 'right', shadow: true });
    text(ctx, '+ extra owed', pr.x - 24, pr.y + 26, 'label', { align: 'right', color: '#FF8A8E', shadow: true });
    text(ctx, '+' + CL('sav_small') + ' a month', pc.x + 24, pc.y, 'label', { color: '#8FE0B5', shadow: true });
    monthRuler(ctx, { y: 930, max: 36, m: month(t), numbered: [[36, CL('y3') + ' years', easeOut(t, tSh - 0.3, tSh), C.ink]] });
    chrome(ctx, { illus: 1 });
  }
  function ruler(ctx, t) {
    text(ctx, 'Rate cut needed to pay back within ' + CL('y3') + ' years', 96, 128, 'head');
    text(ctx, 'point = one percentage point of the rate', 96, 190, 'note', { color: C.muted });
    const xOf = cutRuler(ctx, { x0: 300, x1: 1620, y: 600, max: 1.25, label: false });
    const fl = t > tM && t < tM + 1.6 ? 0.5 + 0.5 * Math.cos((t - tM) * 12) : 1;
    line(ctx, [[xOf(1), 450], [xOf(1), 630]], C.warn, 6, { dash: [14, 10], alpha: easeOut(t, tM, tM + 0.2) * fl });
    const aM = easeOut(t, tM, tM + 0.6);
    rect(ctx, xOf(1), 585, (xOf(1.12) - xOf(1)) * aM, 30, C.warn, 0.9);
    text(ctx, 'more than the 1-point line', xOf(1.06), 690, 'label', { align: 'center', color: C.warn, alpha: easeOut(t, tM + 0.5, tM + 0.9) * (1 - ease(t, tWy, tWy + 0.3)) });
    const xw = mix(xOf(0), xOf(1.12), easeOut(t, tC, tC + 1.6));
    mark(ctx, 'walt', xw, 600, 24);
    text(ctx, CL('cut36_small') + ' points', xOf(1.12) + 40, 540, 'number', { align: 'center', alpha: easeOut(t, tC + 1.4, tC + 1.8) });
    // why: smaller house -> bigger cut
    const aY = easeOut(t, tWy, tWy + 0.5);
    mark(ctx, 'nora', xOf(0.5), 600, 20, aY);
    text(ctx, CL('cut36_median') + ' point', xOf(0.5), 550, 'label', { align: 'center', color: C.positive, alpha: aY });
    houseIcon(ctx, xOf(1.12), 760, Math.sqrt(DATA.small.loan / DATA.median.loan) * 0.95, '#C9BBA4', aY, false);
    houseIcon(ctx, xOf(0.5), 760, 0.95, '#C9BBA4', aY, false);
    text(ctx, 'Walt ' + CL('loan_small'), xOf(1.12), 810, 'note', { align: 'center', alpha: aY });
    text(ctx, 'Nora ' + CL('loan_median'), xOf(0.5), 810, 'note', { align: 'center', alpha: aY });
    text(ctx, 'Smaller loan, bigger cut needed', W / 2, 330, 'caption', { align: 'center', color: C.warn, alpha: aY, plate: PL });
    // the two reasons
    const row = (y, lab, vw, vn, fw, a) => {
      if (a <= 0) return;
      text(ctx, lab, 96, y + 44, 'label', { alpha: a });
      withObj({ role: 'bar', chart: 's16-' + lab, value: fw * a, full: a >= 1, orient: 'h', char: 'small' }, () => rect(ctx, 620, y, 600 * fw * a, 28, C.warn, 0.95));
      withObj({ role: 'bar', chart: 's16-' + lab, value: a, full: a >= 1, orient: 'h', char: 'median' }, () => rect(ctx, 620, y + 34, 600 * a, 28, C.positive, 0.5));
      mark(ctx, 'walt', 596, y + 14, 12, a); mark(ctx, 'nora', 596, y + 48, 11, a);
      text(ctx, 'Walt ' + vw, 620 + 600 * fw + 16, y + 22, 'note', { alpha: a }); text(ctx, 'Nora ' + vn, 1236, y + 64, 'note', { color: C.positive, alpha: a });
    };
    row(860, 'Bill: barely shrinks', CL('cost_small'), CL('cost_median'), DATA.small.cost / DATA.median.cost, easeOut(t, tF, tF + 0.5));
    row(952, 'Savings: shrink', CL('sav_small'), CL('sav_median'), DATA.small.sav / DATA.median.sav, easeOut(t, tS, tS + 0.5));
    chrome(ctx, { illus: 1 });
  }
  return {
    mode: (t) => (t >= tC ? '2d' : '3d'), update,
    overlay: (ctx, t, P, m) => (m === '3d' ? yard(ctx, t, P) : ruler(ctx, t)),
    stripTimes: [tSe + 1.4, tSh + 1.0, tC + 2.0, tM + 1.8, tWy + 1.2, T.dur - 0.2],
  };
}
