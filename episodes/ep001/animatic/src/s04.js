// S04 · Nora. H1: Nora's house at dusk, moving boxes land on the porch and the lights come on; her loan file fills in
// line by line (flat card, labels >= label tier): loan $375,000, rate 7.62%, October 2023; stamp "Dollars of the day".
import { THREE, C, W, H, DATA, CL, text, chrome, mark, ease, easeOut, back, mix, box, mat, house, rgba, roundRect, nb } from './engine.js';
import { outdoors, shadowAll, card, PL } from './common.js';
export const uses3d = true;

export function build({ scene, camera, renderer, T }) {
  const tH = T.a('house'), tB = T.a('built'), tM = T.a('moved'), tLn = T.a('loan'), tR = T.a('rate'), tDl = T.a('dollars');
  outdoors(scene, renderer, { sky: '#1A2233', trees: 10 });
  const nh = shadowAll(house({ w: 3.4, d: 2.8, h: 2.0, roof: 1.35, wall: '#C9BBA4', roofCol: '#3B3F48', lit: 0 }));
  nh.position.set(-2.2, 0, -2.2); scene.add(nh);
  const boxM = mat('#B08A5C', { roughness: 0.95 });
  const boxes = [[-3.2, 0.3, -0.35, 0.6], [-2.55, 0.25, -0.3, 0.5], [-3.0, 0.72, -0.4, 0.45], [-1.2, 0.28, -0.25, 0.55]].map(([x, y, z, s], i) => {
    const b = box(s, s * 0.8, s, boxM); b.position.set(x, y, z); b.userData = { y, s, t0: tM + i * 0.25 }; b.visible = false; scene.add(b); return b;
  });
  const porchLight = new THREE.PointLight('#FFC477', 0, 6, 2); porchLight.position.set(-2.2, 1.6, -0.2); scene.add(porchLight);
  function update(t) {
    const k = ease(t, tH, T.dur);
    camera.position.set(mix(1.4, 0.6, k), mix(3.0, 2.6, k), mix(10.5, 8.6, k)); camera.lookAt(mix(0.6, 0.2, k), 1.2, -1.2);
    boxes.forEach((b) => { const d = easeOut(t, b.userData.t0, b.userData.t0 + 0.45); b.visible = t > b.userData.t0; b.position.y = b.userData.y + (1 - d) * 2.2; b.rotation.y = (1 - d) * 0.6; });
    const on = ease(t, tM + 0.9, tM + 1.4); nh.userData.winMat.emissiveIntensity = 2.6 * on; porchLight.intensity = 5 * on;
  }
  function overlay(ctx, t, P) {
    const pn = P(new THREE.Vector3(-2.2, 0, -0.6));
    const aN = easeOut(t, tH, tH + 0.4);
    mark(ctx, 'nora', pn.x - 70, pn.y + 70, 18, aN); text(ctx, "Nora's first home", pn.x - 42, pn.y + 86, 'label', { alpha: aN, shadow: true });
    text(ctx, 'Nora is illustrative:', 96, 128, 'head', { alpha: aN, shadow: true });
    text(ctx, 'built from typical figures', 96, 196, 'label', { alpha: easeOut(t, tB, tB + 0.4), shadow: true });
    // the loan file (flat card), rows fill in
    const cx = 1150, cy = 260, cw = 660, ch = 560, aC = easeOut(t, tM - 0.4, tM + 0.2);
    card(ctx, cx, cy, cw, ch, aC);
    text(ctx, "NORA'S LOAN", cx + 36, cy + 66, 'label', { color: '#FFFFFF', alpha: aC });
    const row = (y, k, v, tt) => {
      const a = easeOut(t, tt, tt + 0.4) * aC; if (a <= 0) return;
      text(ctx, k, cx + 36, y, 'note', { color: '#4B5563', alpha: a });
      // the whole value slides in from the right (never a partial number)
      text(ctx, v, cx + cw - 36 + 60 * (1 - easeOut(t, tt, tt + 0.5)), y + 70, 'number', { color: '#20242C', align: 'right', alpha: a });
    };
    row(cy + 170, nb('Loan, in dollars of the day', 'Loan'), CL('loan_median'), tLn); // C5 S09: basis next to the $
    row(cy + 330, 'Rate', CL('r_old'), tR);
    text(ctx, 'Signed ' + CL('oct2023'), cx + 36, cy + 510, 'label', { color: '#20242C', alpha: easeOut(t, tR + 0.5, tR + 0.9) * aC });
    // stamp: dollars of the day
    const aS = easeOut(t, tDl, tDl + 0.25), sc = mix(1.5, 1, easeOut(t, tDl, tDl + 0.3));
    if (aS > 0) {
      ctx.save(); ctx.translate(cx + cw / 2, cy + ch + 90); ctx.rotate(-0.06); ctx.scale(sc, sc);
      ctx.globalAlpha = aS; ctx.strokeStyle = C.warn; ctx.lineWidth = 6; roundRect(ctx, -300, -52, 600, 104, 12); ctx.stroke(); ctx.restore();
      text(ctx, 'Dollars of the day', cx + cw / 2, cy + ch + 86, 'label', { align: 'center', color: C.warn, alpha: aS });
      text(ctx, 'not adjusted for inflation', cx + cw / 2, cy + ch + 196, 'note', { align: 'center', color: C.ink, alpha: aS, shadow: true });
    }
    chrome(ctx, { illus: aN });
  }
  return { update, overlay, stripTimes: [tH + 1.0, tB + 1.0, tM + 1.6, tLn + 1.2, tR + 1.4, T.dur - 0.2] };
}
