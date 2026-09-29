// The break-even table (signed SF3), shared by S09 and S10. One dollar scale K for every object:
// ream = loan costs; column = one $221 bundle per month; two paper stacks = balance paid off since refinancing (old loan
// if kept / new loan); hatched slab = the difference (still owed on the new loan vs the old one), lifted onto the ream.
// The caller passes a state function st(t) -> { month, billGrow, level, paidOn, paidMonth, owedGrow, owedMove, ... }.
import { THREE, C, W, H, DATA, CL, text, strike, ease, easeOut, mix, box, mat, pm, paperEdgeTex, owedTex } from './engine.js';
import { kitchen, bundleColumn, ream, letter, monthRuler } from './common.js';

export function makeTable({ scene, camera, renderer }) {
  const M = DATA.median;
  kitchen(scene, renderer, { w: 18, d: 8, key: 110 });
  const K = 2.35 / 11000, FW = 1.25, FD = 0.95;
  const X = { bill: -1.25, sav: -3.3, old: 1.3, nw: 2.8 };
  const at = (arr, m) => { const a = Math.floor(m), b = Math.min(arr.length - 1, a + 1); return mix(arr[a], arr[b], m - a); };
  const R = ream(scene, { dollars: M.cost, K, FW, FD, label: CL('cost_median'), big: 136 });
  const billH = R.userData.h;
  const col = bundleColumn(scene, { n: 30, dollars: M.sav, K, FW, FD, x: X.sav });
  const stackMat = (c) => { const t = paperEdgeTex(); t.repeat.set(1, 6); return new THREE.MeshStandardMaterial({ map: t, color: c, roughness: 0.9 }); };
  const oldS = box(FW * 0.9, 1, FD * 0.9, stackMat('#E4E6EA')); scene.add(oldS);
  const newS = box(FW * 0.9, 1, FD * 0.9, stackMat('#86A9F2')); scene.add(newS);
  const ot = owedTex(); ot.repeat.set(2, 1);
  const owed = box(FW * 0.9 + 0.02, 1, FD * 0.9 + 0.02, new THREE.MeshStandardMaterial({ map: ot, roughness: 0.85 })); scene.add(owed);
  const ghost = new THREE.LineSegments(new THREE.EdgesGeometry(new THREE.BoxGeometry(FW * 0.9, 1, FD * 0.9)), new THREE.LineDashedMaterial({ color: C.negative, dashSize: 0.06, gapSize: 0.05 })); scene.add(ghost);
  const laser = new THREE.Mesh(new THREE.BoxGeometry(2.3, 0.02, 0.02), new THREE.MeshBasicMaterial({ color: '#FFFFFF', transparent: true, opacity: 0 })); scene.add(laser);
  const Lt = letter(scene, { rows: [{ label: 'Your rate now', value: CL('r_old') }, { label: 'New rate', value: CL('r_today') }, { label: 'Loan costs', value: CL('cost_median') }], width: 1.6 });
  Lt.mesh.position.set(-5.6, 0.02, 0.9); Lt.mesh.rotation.y = 0.18;

  function owedState(s) {
    const m = s.month, g = at(M.gap, Math.max(0, m)) * K;
    const newTop = at(M.newPaid, s.paidMonth) * K;
    const from = new THREE.Vector3(X.nw, newTop + g / 2, 0), to = new THREE.Vector3(X.bill, billH + g / 2, 0);
    const p = from.clone().lerp(to, s.owedMove); p.y += Math.sin(s.owedMove * Math.PI) * 1.0;
    return { g, p, newTop };
  }
  function update(t, s) {
    const lc = s.letterCam || 0, LPp = Lt.mesh.position;
    camera.position.set(mix(mix(-0.2, -0.25, s.cam), LPp.x + 0.9, lc), mix(mix(2.4, 2.3, s.cam), 3.0, lc), mix(mix(8.7, 8.3, s.cam), LPp.z + 2.2, lc));
    camera.lookAt(mix(-0.25, LPp.x + 0.8, lc), mix(1.12, 0, lc), mix(0, LPp.z + 0.1, lc));
    R.visible = s.billGrow > 0; R.scale.y = Math.max(0.001, s.billGrow); R.position.set(X.bill, billH * s.billGrow / 2, 0);
    col.update(t, s.landT);
    const ho = Math.max(0.001, at(M.oldPaid, s.paidMonth) * K), hn = Math.max(0.001, at(M.newPaid, s.paidMonth) * K);
    oldS.visible = newS.visible = s.paidOn > 0;
    oldS.scale.set(1, ho, 1); oldS.position.set(X.old, ho / 2, 0); newS.scale.set(1, hn, 1); newS.position.set(X.nw, hn / 2, 0);
    oldS.material.opacity = newS.material.opacity = s.paidOn;
    const o = owedState(s);
    owed.visible = s.owedGrow > 0; owed.scale.y = Math.max(0.001, o.g * (s.owedMove > 0 ? 1 : s.owedGrow)); owed.position.copy(o.p);
    if (s.owedMove <= 0) owed.position.y = o.newTop + o.g * s.owedGrow / 2;
    owed.rotation.z = Math.sin(s.owedMove * Math.PI) * 0.15;
    ghost.visible = s.owedMove > 0.05; ghost.scale.y = Math.max(0.001, o.g); ghost.position.set(X.nw, o.newTop + o.g / 2, 0); ghost.computeLineDistances();
    const lvl = billH + (s.owedMove >= 1 ? o.g : 0);
    laser.position.set((X.bill + X.sav) / 2, lvl + 0.012, FD / 2 + 0.03); laser.scale.x = 1.35;
    laser.material.opacity = s.level * (s.owedMove > 0 && s.owedMove < 1 ? 0 : 1);
    laser.material.color.set(s.done ? C.positive : s.owedMove >= 1 ? C.negative : '#FFFFFF');
    Lt.set([0, 0, s.letterHl || 0]); Lt.mesh.visible = s.letter > 0;
  }
  function overlay(ctx, t, P, s) {
    const o = owedState(s);
    const pb0 = P(new THREE.Vector3(X.bill, 0, FD / 2)), ps0 = P(new THREE.Vector3(X.sav, 0, FD / 2));
    text(ctx, 'loan costs', pb0.x, pb0.y + 54, 'label', { align: 'center', alpha: s.billGrow * ease(1 - (s.letterCam || 0), 0.9, 1), shadow: true });
    text(ctx, '+' + CL('sav_median') + ' a month', ps0.x, ps0.y + 54, 'label', { align: 'center', color: '#8FE0B5', alpha: s.savLabel, shadow: true });
    const pst = P(new THREE.Vector3((X.old + X.nw) / 2, at(M.oldPaid, s.paidMonth) * K, 0));
    text(ctx, 'balance paid off', pst.x, Math.min(pst.y - 90, 690), 'label', { align: 'center', alpha: s.paidOn, shadow: true });
    text(ctx, 'since refinancing', pst.x, Math.min(pst.y - 40, 740), 'note', { align: 'center', color: C.ink, alpha: s.paidOn, shadow: true });
    const po = P(new THREE.Vector3(X.old, 0, FD / 2)), pn = P(new THREE.Vector3(X.nw, 0, FD / 2));
    text(ctx, 'old loan', po.x, po.y + 54, 'label', { align: 'center', color: C.ink, alpha: s.paidOn, shadow: true });
    text(ctx, 'new loan', pn.x, pn.y + 54, 'label', { align: 'center', color: '#B9CFFA', alpha: s.paidOn, shadow: true });
    if (s.paidQ > 0) { const pq = P(new THREE.Vector3(X.nw, 0.9, 0)); text(ctx, '?', pq.x, pq.y, 'number', { align: 'center', color: '#FF8A8E', alpha: s.paidQ, shadow: true }); }
    const aO = s.owedLabel;
    text(ctx, CL('gap24') + ' still owed', 96, 268, 'number', { color: '#FF8A8E', alpha: aO, plate: 'rgba(14,17,22,0.85)' });
    text(ctx, 'on the new loan vs the old one', 96, 334, 'label', { alpha: aO, plate: 'rgba(14,17,22,0.85)' });
    const pr = P(new THREE.Vector3(X.bill, billH + o.g, 0));
    text(ctx, '+ ' + CL('gap24') + ' still owed', pr.x, pr.y - 40, 'label', { align: 'center', color: '#FF8A8E', alpha: s.onBill * (1 - s.done), shadow: true });
    text(ctx, 'loan costs', pr.x, pr.y - 92, 'label', { align: 'center', color: C.ink, alpha: s.done, shadow: true });
    text(ctx, '+ still owed', pr.x, pr.y - 40, 'label', { align: 'center', color: '#FF8A8E', alpha: s.done, shadow: true });
    const rx = monthRuler(ctx, { m: s.month, max: 36, late: 24, alpha: s.ruler, numbered: [
      [24, CL('be_simple_median'), s.n24, s.strike24 > 0 ? C.muted : C.ink], [30, CL('be_bal_median'), s.done, C.positive]] });
    if (s.strike24 > 0) strike(ctx, rx(24) - 36, 912 + 42, rx(24) + 36, C.negative, s.strike24, 6);
  }
  return { update, overlay, K, billH, X };
}
