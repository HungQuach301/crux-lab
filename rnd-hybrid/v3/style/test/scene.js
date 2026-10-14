import { drawFigure } from '/rnd-hybrid/v3/style/figure1930.js';
export async function boot(res) {
  const W = Math.round(res * 16 / 9), H = res, c = document.createElement('canvas'); c.width = W; c.height = H; const g = c.getContext('2d');
  return { canvas: c, frame: () => { g.fillStyle = '#EDE4CF'; g.fillRect(0, 0, W, H); g.save(); g.scale(W / 1920, H / 1080);
    const specs = [{ sex: 'm', era: 'today', coat: '#4C6E9E', skin: 'tan', expr: 'happy', style: 'paper' }, { sex: 'f', era: 'today', coat: '#9E5A4C', skin: 'dark', expr: 'happy', style: 'paper' },
      { sex: 'm', expr: 'happy', pose: { L: 'down', R: 'write' }, style: 'engrave' }, { sex: 'm', expr: 'anxious', pose: { L: 'chin', R: 'down' }, style: 'engrave' }, { sex: 'm', expr: 'relieved', style: 'engrave' }];
    specs.forEach((o, i) => { g.save(); g.translate(200 + i * 380, 1000); g.scale(1.15, 1.15); drawFigure(g, o); g.restore(); });
    g.restore(); return { violations: [] }; } };
}
