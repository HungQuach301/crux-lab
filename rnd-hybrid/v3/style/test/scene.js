import { bankFacade } from '/rnd-hybrid/v3/style/street2d.js';
export async function boot(res) {
  const c = document.createElement('canvas'); c.width = 1920; c.height = 1080; const g = c.getContext('2d');
  return { canvas: c, frame: () => { g.fillStyle = '#334'; g.fillRect(0, 0, 1920, 1080); g.save(); g.scale(1080 / 1540, 1080 / 1540); bankFacade(g, 1870, 1540, { style: 'paper', columns: false }); g.restore(); return { violations: [] }; } };
}
