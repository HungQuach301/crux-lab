// KEY-5 (S04.1-S04.2, S11.4-S11.6): the same loan replayed at every start month. The 10-year frame lands on the far
// left of the ridge; the ridge top inside it lights up as the track and Leah's bead rides it once; a blank tile drops
// straight down into the tray beneath. Then the frame steps right one month per notch, faster and faster; ghost
// outlines of earlier stops (24, 48, 72 months back) show neighbouring frames overlapping; every stop drops a tile.
import { source, THREE, C, DATA, CL, text, badge, ease, easeOut, back, mix, clamp } from './engine.js';
import { xOf, KY, RIDGE, Z } from './world.js';
import { history, NS } from './hist.js';

const DUR = 10.0;
const tk = (k) => (k === 0 ? 2.9 : k <= 4 ? 2.9 + 0.5 * k : 4.9 + 3.7 * Math.pow((k - 4) / (NS - 5), 0.55));
export function build({ scene, camera, renderer }) {
  renderer.toneMappingExposure = 1.0;
  const Hs = history(scene, { ghosts: 1 });
  const kAt = (t) => { let lo = 0, hi = NS - 1; if (t < tk(0)) return 0; while (lo < hi) { const m = (lo + hi + 1) >> 1; if (tk(m) <= t) lo = m; else hi = m - 1; } return lo; };
  function update(t) {
    const k = kAt(t);
    // smooth slide for the first slow notches
    const kk = k >= 1 && k <= 4 ? (k - 1) + ease(t, tk(k), tk(k) + 0.3) : k;
    const land = easeOut(t, 0.0, 0.9);
    Hs.placeFrame(kk, { alpha: land, lift: (1 - land) * 2.5, bm: t < 3.0 ? mix(0, 119, ease(t, 1.5, 2.7)) : 0, wireUpto: ease(t, 0.9, 1.5),
      litUpto: t < 3.0 ? mix(0, 119, ease(t, 1.5, 2.7)) : -1, bracketA: ease(t, 0.9, 1.3) });
    Hs.ghosts.forEach((g, i) => { const kg = k - 24 * (i + 1); if (kg < 0 || t < tk(1)) { g.visible = false; return; } g.visible = true; g.position.x = xOf(kg); g.position.y = 0; g.userData.alpha(0.5 - i * 0.14); });
    Hs.TR.userData.update((j) => {
      const td = tk(j) + (j === 0 ? 0.1 : 0.05); if (t < td) return { y: null };
      const fall = j === 0 ? 0.45 : j <= 4 ? 0.35 : 0.22;
      return { y: (1 - easeOut(t, td, td + fall)) * 1.9, kind: 'blank' };
    }, -1);
    const c = ease(t, 0, DUR);
    camera.fov = 42; camera.position.set(mix(-0.3, 0.0, c), mix(6.6, 6.4, c), mix(13.4, 12.9, c)); camera.lookAt(mix(-0.25, 0.0, c), 0.7, -0.4); camera.updateProjectionMatrix();
  }
  function overlay(ctx, t, proj) {
    const pa = proj(new THREE.Vector3(xOf(0), 3.9, Z.ridge1));
    text(ctx, CL('first_start'), Math.max(40, pa.x - 20), pa.y - 18, 'label', { alpha: Math.min(ease(t, 0.9, 1.3), 1 - ease(t, 4.6, 4.9)) });
    text(ctx, CL('term'), 640, 668, 'label', { align: 'center', color: C.muted, alpha: Math.min(ease(t, 1.0, 1.4), 1 - ease(t, 4.6, 4.9)) });
    const pz = proj(new THREE.Vector3(xOf(NS - 1), 3.9, Z.ridge1));
    text(ctx, CL('last_start'), pz.x - 30, pz.y - 18, 'label', { align: 'right', alpha: ease(t, 8.6, 8.9) });
    badge(ctx, 1);
    source(ctx, 'tl');
  }
  return { duration: DUR, stripTimes: [0.5, 1.9, 3.1, 4.6, 6.6, 9.8], update, overlay };
}
