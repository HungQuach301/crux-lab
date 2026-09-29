// S15 · The bill barely shrinks. Kết hợp: H3 three rows, Walt's bar shrinking from Nora's length: loan (a lot),
// bill (a little), monthly savings (a lot) -> H1 Walt's yard: $68 bundles stack very slowly to the ream + hatched
// slab; level at month 75. (Deviation from the C3 table "H1": the three-way size comparison is a scale reading -> H3.)
import { THREE, C, W, H, DATA, CL, text, chrome, line, rect, srect, mark, ease, easeOut, mix } from './engine.js';
import { monthRuler, PL } from './common.js';
import { makeYard } from './yard.js';
export const uses3d = true;

export function build(ctx0) {
  const { T, camera } = ctx0;
  const tG = T.a('grow'), tB = T.a('bills'), tSh = T.a('share'), tS = T.a('sav'), t68 = T.a('b68'), tSt = T.a('stack'), t75 = T.a('m75');
  const S = DATA.small, M = DATA.median;
  const rows = [
    { lab: 'Loan', w: S.loan / M.loan, t: tG, vw: CL('loan_small'), vn: CL('loan_median') },
    { lab: 'Loan costs', w: S.cost / M.cost, t: tB, vw: CL('cost_small'), vn: CL('cost_median') },
    { lab: 'Monthly savings', w: S.sav / M.sav, t: tS, vw: CL('sav_small'), vn: CL('sav_median') },
  ];
  const BX = 560, BL = 1000;
  function bars(ctx, t) {
    text(ctx, 'Walt compared with Nora', 96, 128, 'head');
    text(ctx, "Nora's bar = full length", 96, 190, 'note', { color: C.muted });
    rows.forEach((r, i) => {
      const y = 330 + i * 230, a = easeOut(t, r.t - 0.3, r.t + 0.2);
      if (a <= 0) return;
      text(ctx, r.lab, 96, y + 40, 'label', { alpha: a });
      rect(ctx, BX, y - 50, BL, 44, C.positive, 0.35 * a); mark(ctx, 'nora', BX - 30, y - 28, 14, a);
      text(ctx, r.vn, BX + BL + 20, y - 14, 'label', { color: C.positive, alpha: a });
      const k = mix(1, r.w, ease(t, r.t + 0.4, r.t + 1.8));
      rect(ctx, BX, y + 10, BL * k, 60, C.warn, 0.95 * a); mark(ctx, 'walt', BX - 30, y + 40, 16, a);
      text(ctx, r.vw, BX + BL * k + 20, y + 58, 'number', { alpha: easeOut(t, r.t + 1.6, r.t + 2.0) });
    });
    text(ctx, 'the bill barely shrinks', BX + BL * rows[1].w + 330, 330 + 230 + 58, 'label', { color: C.warn, alpha: easeOut(t, tB + 2.0, tB + 2.4) * (1 - ease(t, tSh - 0.3, tSh)) });
    text(ctx, 'his bill = ' + CL('share_walt') + ' of his loan', BX, 330 + 230 + 136, 'label', { color: C.warn, alpha: easeOut(t, tSh, tSh + 0.4) });
    text(ctx, 'savings shrink with the loan', 96, 960, 'caption', { alpha: easeOut(t, t68, t68 + 0.4), plate: PL });
    chrome(ctx, { illus: 1, source: 'Walt, Nora: illustrative. Same offer: ' + CL('r_old') + ' → ' + CL('r_today') + '.' });
  }
  // ---- H1: Walt's slow stack ----
  const Y = makeYard(ctx0, { who: ['walt'], K: 2.5 / 5200, months: 76, data: { walt: DATA.small80 } });
  const w = Y.out.walt;
  const month = (t) => Math.min(75, 75 * ease(t, tSt + 0.4, t75 + 0.2));
  function update(t) {
    const k = ease(t, tSt, T.dur);
    camera.position.set(w.x + 0.9, mix(2.6, 2.5, k), mix(10.0, 9.4, k)); camera.lookAt(w.x + 0.8, 1.45, w.Z - 1.0);
    Y.update('walt', { houseGrow: 1, reamIn: 1, month: month(t), owedOn: 1, colOn: 1, laser: 1, lit: 0.6 });
  }
  function yard(ctx, t, P) {
    const m = month(t);
    text(ctx, CL('sav_small') + ' a month, against a ' + CL('cost_small') + ' bill', 96, 128, 'head', { shadow: true });
    text(ctx, 'Break-even: month ' + CL('be_bal_small'), 96, 214, 'number', { color: C.positive, alpha: easeOut(t, t75 + 0.2, t75 + 0.6), shadow: true });
    const pr = P(new THREE.Vector3(w.x - w.FW / 2, 0.9, w.Z + w.FD / 2)), pc = P(new THREE.Vector3(w.xs + w.FW / 2, 0.5, w.Z + w.FD / 2));
    text(ctx, 'loan costs', pr.x - 24, pr.y - 30, 'label', { align: 'right', shadow: true });
    text(ctx, '+ still owed', pr.x - 24, pr.y + 26, 'label', { align: 'right', color: '#FF8A8E', shadow: true });
    text(ctx, '+' + CL('sav_small') + ' a month', pc.x + 24, pc.y, 'label', { color: '#8FE0B5', shadow: true });
    monthRuler(ctx, { x0: 330, x1: 1590, y: 930, max: 80, m, numbered: [[75, CL('be_bal_small'), easeOut(t, t75, t75 + 0.3), C.positive]] });
    chrome(ctx, { illus: 1 });
  }
  return {
    mode: (t) => (t >= tSt ? '3d' : '2d'), update,
    overlay: (ctx, t, P, m) => (m === '3d' ? yard(ctx, t, P) : bars(ctx, t)),
    stripTimes: [tG + 2.0, tB + 2.2, tSh + 1.0, t68 + 1.2, mix(tSt, t75, 0.6), T.dur - 0.2],
  };
}
