// KEY-3 (S05.2-S05.4): the frame sweeps every start month. Its own rail lights amber where the ridge rises above it
// (= the variable rate went above 9% in that replay); a long rail along the foot of the ridge keeps one segment per start
// month and stays amber for those (574 of 753). At the same time a tile drops into the tray beneath each start: tall
// red = costlier in total (107), flat grey = not. Amber (rails) and red (tiles) never share an object.
// End: rail nearly all amber; trays only flecked red; left tray clearly redder; the worst start (April 1977) is a
// double-height red block with a dark ring that pulses once.
import { source, THREE, C, DATA, CL, text, numWords, badge, ease, easeOut, mix, lin } from './engine.js';
import { xOf, rail, Z, TILE } from './world.js';
import { history, NS } from './hist.js';

const DUR = 10.0, S0 = 0.5, S1 = 5.6;
export function build({ scene, camera, renderer }) {
  const Hs = history(scene);
  const LR = rail(scene, NS, { r: 0.04 });
  const kAt = (t) => (t < S0 ? 0 : Math.min(NS - 1, (NS - 1) * Math.pow(lin(t, S0, S1), 1.25)));
  const tStart = (j) => S0 + (S1 - S0) * Math.pow(j / (NS - 1), 1 / 1.25);
  function update(t) {
    const k = kAt(t), fa = 1 - ease(t, S1 + 0.1, S1 + 0.6);
    Hs.placeFrame(Math.floor(k), { alpha: fa, bm: 0, litUpto: 119, bracketA: 0 });
    Hs.B.visible = fa > 0.3; Hs.WIRE.visible = fa > 0.3;
    LR.userData.place(xOf(0), xOf(NS - 1) + 0.02, 0.11, Z.longRail, (j) => (DATA.above[j] && tStart(j) <= t ? 1 : 0));
    const pulse = Math.sin(Math.PI * lin(t, 8.4, 9.4));
    Hs.TR.userData.update((j) => {
      const td = tStart(j) + 0.05; if (t < td) return { y: null };
      return { y: (1 - easeOut(t, td, td + 0.25)) * 1.6, kind: DATA.costlier['1.5'][j] ? 'red' : 'grey' };
    }, DATA.worstIdx, pulse);
    camera.fov = 42; camera.position.set(0, 6.4, 12.9); camera.lookAt(0, 0.7, -0.4); camera.updateProjectionMatrix();
  }
  function overlay(ctx, t, proj) {
    numWords(ctx, CL('share_rate_above_fixed'), 'rate above 9% at some point', 60, 150, { alpha: Math.min(ease(t, 5.6, 6.0), 1 - ease(t, 8.3, 8.6)), numColor: C.ink });
    numWords(ctx, CL('share_all'), 'cost more in total', 640, 640, { align: 'center', alpha: Math.min(ease(t, 7.0, 7.4), 1 - ease(t, 8.2, 8.5)) });
    const pl = proj(new THREE.Vector3((xOf(0) + xOf(323)) / 2, 0, 0.12 + 12 * TILE.pitch + 0.2));
    const pr = proj(new THREE.Vector3((xOf(324) + xOf(752)) / 2, 0, 0.12 + 12 * TILE.pitch + 0.2));
    numWords(ctx, CL('share_early'), 'starts 1954–1980', pl.x, 650, { align: 'center', alpha: ease(t, 8.5, 8.9) });
    numWords(ctx, CL('share_late'), 'starts 1981 on', pr.x, 650, { align: 'center', alpha: ease(t, 8.5, 8.9) });
    badge(ctx, 1);
    source(ctx, 'br');
  }
  return { duration: DUR, stripTimes: [0.4, 2.0, 3.8, 5.8, 7.4, 9.6], update, overlay };
}
