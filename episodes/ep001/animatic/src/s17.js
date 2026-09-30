// S17 · Anjali (signed SF5, Anjali side). H1 yard: Anjali's big house rises right of Nora's; same offer; her bill
// ($5,514) beside Nora's ($5,124); $387 bundles pass ream + slab at month 18; +$5,250 after 3 years -> H3 ruler:
// her square stops at about a third of a point (Walt 1.12 and Nora 0.5 shown for reference).
import { THREE, C, W, H, DATA, CL, text, chrome, line, rect, mark, measure, ease, easeOut, back, mix, clamp, basisNote, BASIS } from './engine.js';
import { monthRuler, cutRuler, PL } from './common.js';
import { makeYard } from './yard.js';
export const uses3d = true;

export function build(ctx0) {
  const { T, camera } = ctx0;
  const tA = T.a('anj'), tSm = T.a('same'), tL = T.a('loan'), tLi = T.a('limit'), tB = T.a('bill'), tS = T.a('stack'), tAh = T.a('ahead'), tTh = T.a('third');
  const Y = makeYard(ctx0, { who: ['nora', 'anjali'], K: 2.6 / 14000, months: 36 });
  const a = Y.out.anjali, n = Y.out.nora;
  const month = (t) => 36 * ease(t, tS, tAh - 0.3);
  const t18 = tS + (tAh - 0.3 - tS) * (DATA.large.be / 36);
  function update(t) {
    const k = ease(t, 0, tTh);
    camera.position.set(mix(3.0, 3.5, k), mix(3.6, 3.3, k), mix(13.6, 12.6, k)); camera.lookAt(3.6, 1.05, -1.4);
    Y.update('nora', { houseGrow: 1, reamIn: 1, colOn: 0, lit: 0.4 });
    Y.update('anjali', { houseGrow: back(t, tA, tA + 0.8), reamIn: easeOut(t, tB, tB + 0.5), month: month(t), owedOn: t > tS ? 1 : 0, colOn: 1, laser: ease(t, tS, tS + 0.3), lit: 0.6 });
  }
  function yard(ctx, t, P) {
    text(ctx, 'Same month, same rate, same cut', 96, 128, 'head', { alpha: easeOut(t, tSm, tSm + 0.4), shadow: true });
    text(ctx, CL('oct2023') + ' · ' + CL('r_old') + ' → ' + CL('r_today'), 96, 196, 'label', { alpha: easeOut(t, tSm, tSm + 0.4), shadow: true });
    const top = (o) => o.house.userData.h + o.house.userData.roof + 0.25;
    const pa = P(new THREE.Vector3(a.house.position.x, top(a), a.house.position.z)), pn = P(new THREE.Vector3(n.house.position.x, top(n), n.house.position.z));
    const lab = (who, s, p, al) => { const wd = measure(ctx, s, 'label'); mark(ctx, who, p.x - wd / 2 - 26, p.y - 14, 16, al); text(ctx, s, p.x - wd / 2, p.y, 'label', { alpha: al, shadow: true }); };
    lab('anjali', 'Anjali · ' + CL('loan_large') + ' loan', pa, easeOut(t, tL, tL + 0.4));
    text(ctx, 'Anjali', pa.x, pa.y, 'label', { align: 'center', alpha: easeOut(t, tA + 0.5, tA + 0.9) * (1 - easeOut(t, tL, tL + 0.4)), shadow: true });
    lab('nora', 'Nora · ' + CL('loan_median') + ' loan', pn, 1);
    basisNote(ctx, pn.x, pn.y + 50, { align: 'center', color: C.ink, shadow: true }); // C5 S09
    text(ctx, 'under the conforming limit (the ceiling for standard loans)', W - 96, 330, 'note', { align: 'right', plate: PL, alpha: easeOut(t, tLi, tLi + 0.4) * (1 - ease(t, tS, tS + 0.4)), shadow: true });
    const ra = P(new THREE.Vector3(a.x, a.rh, a.Z)), rn = P(new THREE.Vector3(n.x, n.rh, n.Z));
    const aB = easeOut(t, tB + 0.4, tB + 0.8) * (1 - ease(t, tS, tS + 0.3));
    text(ctx, 'bill ' + CL('cost_large'), ra.x, ra.y - 30, 'label', { align: 'center', alpha: aB, plate: PL });
    text(ctx, 'bill ' + CL('cost_median'), rn.x, rn.y - 30, 'label', { align: 'center', alpha: easeOut(t, tB + 0.4, tB + 0.8), plate: PL });
    basisNote(ctx, (ra.x + rn.x) / 2, Math.min(ra.y, rn.y) - 84, { align: 'center', color: C.ink, alpha: easeOut(t, tB + 0.4, tB + 0.8), plate: PL }); // C5 S09
    const pc = P(new THREE.Vector3(a.xs + a.FW / 2, 0.4, a.Z + a.FD / 2));
    text(ctx, '+' + CL('sav_large') + ' a month', Math.min(pc.x + 20, 1824 - measure(ctx, '+' + CL('sav_large') + ' a month', 'label')), pc.y, 'label', { color: '#8FE0B5', alpha: easeOut(t, tS, tS + 0.4), shadow: true });
    basisNote(ctx, Math.min(pc.x + 20, 1824 - measure(ctx, BASIS, 'note')), pc.y + 54, { color: C.ink, alpha: easeOut(t, tS, tS + 0.4), shadow: true }); // C5 S09
    const pt = P(new THREE.Vector3(a.x - a.FW / 2, a.rh, a.Z));
    const a18 = easeOut(t, t18, t18 + 0.3) * (1 - ease(t, tAh - 0.4, tAh - 0.1));
    text(ctx, 'paid back: month ' + CL('be_bal_large'), pt.x - 20, pt.y, 'label', { align: 'right', color: C.positive, alpha: a18, plate: PL });
    const aAh = easeOut(t, tAh, tAh + 0.4);
    text(ctx, CL('net36_large') + ' ahead', pt.x - 20, pt.y - 20, 'number', { align: 'right', color: C.positive, alpha: aAh, plate: PL });
    text(ctx, 'after ' + CL('y3') + ' years', pt.x - 20, pt.y + 44, 'label', { align: 'right', alpha: aAh, plate: PL });
    monthRuler(ctx, { y: 912, max: 36, m: month(t), alpha: easeOut(t, tS - 0.3, tS), numbered: [[18, CL('be_bal_large'), easeOut(t, t18, t18 + 0.3), C.positive], [36, CL('y3') + ' years', easeOut(t, tAh - 0.3, tAh), C.ink]] });
    chrome(ctx, { illus: 1, source: 'Anjali, Nora: illustrative. Bills: ' + CL('y2025') + ' medians (HMDA, US home-loan records).', plate: true });
  }
  function ruler(ctx, t) {
    text(ctx, 'Rate cut needed to pay back within ' + CL('y3') + ' years', 96, 128, 'head');
    text(ctx, 'point = one percentage point of the rate', 96, 190, 'note', { color: C.muted });
    const xOf = cutRuler(ctx, { x0: 300, x1: 1620, y: 560, max: 1.25, label: false });
    mark(ctx, 'walt', xOf(1.12), 560, 20, 0.6); text(ctx, 'Walt ' + CL('cut36_small'), xOf(1.12), 640, 'note', { align: 'center', color: C.muted });
    mark(ctx, 'nora', xOf(0.5), 560, 18, 0.6); text(ctx, 'Nora ' + CL('cut36_median'), xOf(0.5), 640, 'note', { align: 'center', color: C.muted });
    const xa = mix(xOf(1.25), xOf(DATA.cuts.large), easeOut(t, tTh, tTh + 1.4));
    mark(ctx, 'anjali', xa, 560, 24);
    const aT = easeOut(t, tTh + 1.2, tTh + 1.6);
    text(ctx, 'about a third', xOf(DATA.cuts.large), 430, 'number', { align: 'center', alpha: aT });
    text(ctx, 'of a point', xOf(DATA.cuts.large), 500, 'label', { align: 'center', alpha: aT });
    text(ctx, 'Anjali', xOf(DATA.cuts.large), 640, 'note', { align: 'center', alpha: aT });
    chrome(ctx, { illus: 1, source: 'Anjali: ' + CL('cut36_large_words') + ' (illustrative).' });
  }
  return {
    mode: (t) => (t >= tTh ? '2d' : '3d'), update,
    overlay: (ctx, t, P, m) => (m === '3d' ? yard(ctx, t, P) : ruler(ctx, t)),
    stripTimes: [tA + 1.4, tLi + 1.0, tB + 1.4, t18 + 0.4, tAh + 1.0, T.dur - 0.2],
  };
}
