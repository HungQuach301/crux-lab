// S20 · The question that stays with you. H1: Nora's house at dusk; a time marker walks along the path under it
// (flat year ruler); at year 3 a cash stack rises in front: +$1,039 ahead; at year 7 it has grown to +$8,093; the
// marker keeps walking off the frame with no more marks; an outline house "your home?" appears beside hers.
import { THREE, C, W, H, DATA, CL, text, chrome, line, rect, dot, mark, ease, easeOut, back, mix, house, outlineHouse, box, mat, pm } from './engine.js';
import { outdoors, shadowAll, cashMats, PL } from './common.js';
export const uses3d = true;

export function build({ scene, camera, renderer, T }) {
  const tS = T.a('stay'), t3 = T.a('y3'), t7 = T.a('y7'), tF = T.a('fast'), tTh = T.a('there'), tQ = T.a('q');
  outdoors(scene, renderer, { sky: '#161E2C', trees: 12 });
  const nh = shadowAll(house({ w: 3.2, d: 2.6, h: 1.9, roof: 1.3, wall: '#C9BBA4', roofCol: '#3B3F48', lit: 2.2 })); nh.position.set(-1.2, 0, -3.0); scene.add(nh);
  const out = outlineHouse({ w: 3.0, d: 2.4, h: 1.8, roof: 1.2, color: '#F2F4F7' }); out.position.set(4.4, 0, -3.0); scene.add(out);
  // cash stack in front of the house: height = Nora's position (dollars) once positive; one scale
  const pos = DATA.pos96, K = 2.4 / 8500;
  const cm = cashMats();
  const stack = new THREE.Mesh(new THREE.BoxGeometry(1.3, 1, 0.9), cm); stack.castShadow = stack.receiveShadow = true; scene.add(stack);
  // month shown: walks 0 -> 36 by "three years", -> 84 by "seven", then beyond (no marks)
  const month = (t) => t < tS ? 0 : t < t3 ? 36 * ease(t, tS, t3) : t < t7 ? 36 + 48 * ease(t, t3 + 0.6, t7) : 84 + 60 * ease(t, tTh, T.dur);
  const at = (m) => { const a = Math.min(95, Math.floor(m)), b = Math.min(96, a + 1); return mix(pos[a], pos[b], Math.min(1, m - a)); };
  function update(t) {
    const k = ease(t, 0, T.dur);
    camera.position.set(mix(0.6, 1.2, k), mix(3.0, 3.4, k), mix(10.5, 12.2, k)); camera.lookAt(0.8, 1.2, -1.5);
    const m = Math.min(96, month(t)), v = Math.max(0, at(m)), h = Math.max(0.001, v * K);
    stack.visible = v > 1; stack.scale.y = h; stack.position.set(1.4, h / 2, 0.6);
    out.userData.mat.opacity = easeOut(t, tQ, tQ + 0.8); out.visible = t > tQ;
  }
  function overlay(ctx, t, P) {
    const m = month(t);
    text(ctx, 'The number only you know: how long you stay', 96, 128, 'head', { alpha: easeOut(t, 0.2, 0.6), shadow: true });
    // flat year ruler: 0..8 years visible; only 3 and 7 numbered; the marker walks on and off the frame
    const RX0 = 260, RX1 = 1700, RY = 960, rx = (mm) => RX0 + (mm / 96) * (RX1 - RX0);
    ctx.save(); ctx.fillStyle = C.grid; ctx.fillRect(RX0, RY, RX1 - RX0, 4); ctx.restore();
    for (let y = 1; y <= 8; y++) rect(ctx, rx(y * 12) - 3, RY - 18, 6, 18, C.grid, 1);
    text(ctx, 'years in the home →', RX0, RY + 58, 'note', { color: C.muted });
    const a3 = easeOut(t, t3 - 0.2, t3 + 0.2), a7 = easeOut(t, t7 - 0.2, t7 + 0.2);
    text(ctx, CL('y3') + ' years', rx(36), RY + 58, 'label', { align: 'center', alpha: a3 });
    text(ctx, CL('y7') + ' years', rx(84), RY + 58, 'label', { align: 'center', alpha: a7 });
    const xm = rx(m);
    if (t > tS) { mark(ctx, 'nora', xm, RY - 34, 18); line(ctx, [[RX0, RY + 2], [Math.min(xm, RX1 + 300), RY + 2]], C.positive, 6); }
    // what the same offer comes to
    const ps = P(new THREE.Vector3(2.2, 0.6, 0.6));
    text(ctx, '+' + CL('net36_median') + ' ahead', ps.x + 20, ps.y - 40, 'number', { color: C.positive, alpha: a3 * (1 - ease(t, t7 - 0.3, t7)), plate: PL });
    text(ctx, 'if she sells after ' + CL('y3') + ' years', ps.x + 20, ps.y + 20, 'label', { alpha: a3 * (1 - ease(t, t7 - 0.3, t7)), plate: PL });
    text(ctx, '+' + CL('net84_median') + ' ahead', ps.x + 20, ps.y - 40, 'number', { color: C.positive, alpha: a7, plate: PL });
    text(ctx, 'if she stays ' + CL('y7') + ' years', ps.x + 20, ps.y + 20, 'label', { alpha: a7, plate: PL });
    text(ctx, 'rate cut: how fast the fees come back', 96, 196, 'label', { color: C.muted, alpha: easeOut(t, tF, tF + 0.4), shadow: true });
    text(ctx, 'your stay: whether you are still there', 96, 250, 'label', { color: C.ink, alpha: easeOut(t, tTh, tTh + 0.4), shadow: true });
    const po = P(new THREE.Vector3(4.4, 3.4, -3.0));
    text(ctx, 'your home?', po.x, po.y, 'label', { align: 'center', alpha: easeOut(t, tQ + 0.5, tQ + 0.9), shadow: true });
    text(ctx, 'How long do you picture yourself in your home?', W / 2, 860, 'caption', { align: 'center', alpha: easeOut(t, tQ + 0.2, tQ + 0.6), plate: PL, sent: true });
    chrome(ctx, { illus: 1 });
  }
  return { update, overlay, stripTimes: [tS + 0.8, t3 + 0.6, t7 + 0.8, tF + 1.2, tTh + 1.6, T.dur - 0.2], hardTime: t7 + 1.0 };
}
