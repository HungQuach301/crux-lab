// S14 · Walt. H1 yard: Walt's smaller house rises beside Nora's (volume = loan); the same letter slides to Walt;
// his bill ($3,667) drops in beside Nora's ($5,124) on one dollar scale; a level line shows how little lower it is.
import { THREE, C, W, H, DATA, CL, text, chrome, mark, ease, easeOut, back, mix, measure, basisNote, BASIS } from './engine.js';
import { letter, PL } from './common.js';
import { makeYard } from './yard.js';
export const uses3d = true;

export function build(ctx0) {
  const { T, scene, camera } = ctx0;
  const tW = T.a('walt'), tL = T.a('loan'), tS = T.a('same'), tLe = T.a('letter'), tB = T.a('bill'), tF = T.a('far'), tLi = T.a('little');
  const Y = makeYard(ctx0, { who: ['walt', 'nora'], K: 1.4 / 6000 });
  const Lt = letter(scene, { rows: [{ label: 'Your rate now', value: CL('r_old') }, { label: 'New rate', value: CL('r_today') }, { label: 'Loan costs', value: CL('cost_small') }], width: 1.8 });
  const lvl = new THREE.Mesh(new THREE.BoxGeometry(1, 0.02, 0.02), new THREE.MeshBasicMaterial({ color: '#FFFFFF', transparent: true, opacity: 0 })); scene.add(lvl);
  const w = Y.out.walt, n = Y.out.nora;
  function update(t) {
    const k = ease(t, 0, T.dur);
    camera.position.set(mix(-1.8, -2.2, k), mix(3.3, 3.1, k), mix(12.5, 11.6, k)); camera.lookAt(-2.4, 1.3, -1.2);
    Y.update('nora', { houseGrow: 1, reamIn: easeOut(t, tB - 0.2, tB + 0.3), colOn: 0, lit: 0.6 });
    Y.update('walt', { houseGrow: back(t, tW, tW + 0.7), reamIn: easeOut(t, tB, tB + 0.5), colOn: 0, lit: 0.6 });
    const la = easeOut(t, tLe, tLe + 0.9);
    Lt.mesh.position.set(mix(-12, -2.6, la), 0.02, 2.4); Lt.mesh.rotation.y = 0.1 + (1 - la) * 0.4; Lt.mesh.visible = t > tLe;
    Lt.set([0, ease(t, tLe + 0.8, tLe + 1.2), ease(t, tB, tB + 0.4)]);
    lvl.position.set((w.x + n.x) / 2, n.rh + 0.012, w.Z + 0.43); lvl.scale.x = Math.abs(n.x - w.x) + 1.0; lvl.material.opacity = ease(t, tLi, tLi + 0.4);
  }
  function overlay(ctx, t, P) {
    const top = (o) => o.house.userData.h + o.house.userData.roof + 0.25;
    const pw = P(new THREE.Vector3(w.house.position.x, top(w), w.house.position.z)), pn = P(new THREE.Vector3(n.house.position.x, top(n), n.house.position.z));
    const aW = easeOut(t, tW + 0.4, tW + 0.8);
    const lab = (who, name, loanS, p, a, al) => { const s = name + ' · ' + loanS, wd = measure(ctx, s, 'label'); mark(ctx, who, p.x - wd / 2 - 26, p.y - 14, 16, a); text(ctx, s, p.x - wd / 2, p.y, 'label', { alpha: a, shadow: true, color: al }); };
    lab('walt', 'Walt', CL('loan_small') + ' loan', { x: pw.x, y: pw.y + 0 }, aW * easeOut(t, tL, tL + 0.4) + 0.001, t > tF ? C.warn : C.ink);
    text(ctx, 'Walt', pw.x, pw.y, 'label', { align: 'center', alpha: aW * (1 - easeOut(t, tL, tL + 0.4)), shadow: true });
    lab('nora', 'Nora', CL('loan_median') + ' loan', { x: pn.x, y: pn.y }, easeOut(t, tL, tL + 0.4), C.ink);
    text(ctx, 'Walt: illustrative, built from typical figures', 96, 196, 'label', { alpha: aW * (1 - ease(t, tLe, tLe + 0.3)), shadow: true });
    text(ctx, 'Both borrowed ' + CL('oct2023') + ' at ' + CL('r_old'), 96, 128, 'head', { alpha: easeOut(t, tS, tS + 0.4) * (1 - ease(t, tLe, tLe + 0.3)), shadow: true });
    text(ctx, 'Same offer: ' + CL('r_old') + ' → ' + CL('r_today'), 96, 128, 'head', { alpha: easeOut(t, tLe, tLe + 0.4), shadow: true });
    const rw = P(new THREE.Vector3(w.x, w.rh, w.Z)), rn = P(new THREE.Vector3(n.x, n.rh, n.Z));
    const aB = easeOut(t, tB + 0.4, tB + 0.8);
    text(ctx, 'bill ' + CL('cost_small'), rw.x, rw.y - 30, 'label', { align: 'center', alpha: aB, plate: PL });
    text(ctx, 'bill ' + CL('cost_median'), rn.x, rn.y - 30, 'label', { align: 'center', alpha: aB, plate: PL });
    basisNote(ctx, W / 2, 470, { align: 'center', color: C.ink, alpha: easeOut(t, tL, tL + 0.4), plate: PL }); // C5 S09: amounts are dollars of the day
    text(ctx, 'far smaller loan', W / 2, 900, 'caption', { align: 'center', color: C.warn, alpha: easeOut(t, tF, tF + 0.4) * (1 - ease(t, tLi, tLi + 0.3)), plate: PL });
    text(ctx, 'only a little smaller bill', W / 2, 900, 'caption', { align: 'center', alpha: easeOut(t, tLi, tLi + 0.4), plate: PL });
    chrome(ctx, { illus: 1, source: 'Walt, Nora: illustrative. Bills: ' + CL('y2025') + ' medians (HMDA, US home-loan records).', plate: true });
  }
  return { update, overlay, stripTimes: [tW + 1.0, tL + 1.4, tLe + 1.4, tB + 1.2, tF + 0.8, T.dur - 0.2] };
}
