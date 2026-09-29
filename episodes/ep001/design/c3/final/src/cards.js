'use strict';
// Title cards (1 s each) for review-c3/contract.mp4, drawn with the same tokens and Inter. Writes ../work/card-*.png
//   NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node cards.js
const fs = require('fs'), path = require('path');
const { chromium } = require('playwright');
const FIN = path.resolve(__dirname, '..'), REPO = path.resolve(FIN, '../../../../..');
const TOK = JSON.parse(fs.readFileSync(path.join(FIN, 'tokens.json'), 'utf8'));
const CARDS = [
  ['card-0', 'Episode 1 · C3 visual contract', 'Direction D: H1 real objects + H3 geometry of money', 'Six motion style frames, no sound, in story order'],
  ['card-SF1', '1 / 6 · Cold open: the missed window', 'S01 · H3 chart → H1 kitchen → H3 chart', ''],
  ['card-SF2', '2 / 6 · The letter, and the promise', 'S02 · H1 kitchen table, model houses', ''],
  ['card-SF3', '3 / 6 · Break-even moves from 24 to 30', 'S09–S10 · H1 objects on one dollar scale', ''],
  ['card-SF4', '4 / 6 · A quarter point: never', 'S11 · H3 chart', ''],
  ['card-SF5', '5 / 6 · Walt and Anjali', 'S14–S17 · H1 houses, fees, savings', ''],
  ['card-SF6', '6 / 6 · The three-mark ruler', 'S18 · H3, the viewer places their own loan', ''],
];
const font = (w) => `@font-face{font-family:Inter;font-weight:${w};src:url(data:font/woff2;base64,${fs.readFileSync(path.join(REPO, 'toolkit/render/fonts', `inter-latin-${w}-normal.woff2`)).toString('base64')}) format('woff2')}`;
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  await p.setContent(`<style>${font(400)}${font(600)}${font(700)}body{margin:0}</style><canvas id=c width=1920 height=1080></canvas>`);
  await p.evaluate(async () => { for (const w of [400, 600, 700]) await document.fonts.load(`${w} 48px Inter`); });
  for (const [name, a, s, n] of CARDS) {
    const url = await p.evaluate(([a, s, n, C]) => {
      const g = document.getElementById('c').getContext('2d');
      g.fillStyle = C.bg; g.fillRect(0, 0, 1920, 1080);
      g.fillStyle = C.warn; g.fillRect(96, 420, 12, 200);
      g.fillStyle = C.ink; g.font = '700 88px Inter'; g.fillText(a, 140, 500);
      g.fillStyle = C['ink-muted']; g.font = '600 56px Inter'; g.fillText(s, 140, 590);
      if (n) { g.font = '400 48px Inter'; g.fillText(n, 140, 670); }
      g.font = '400 48px Inter'; g.fillText('Crux · Episode 1', 96, 1030);
      return document.getElementById('c').toDataURL('image/png');
    }, [a, s, n, TOK.color]);
    fs.mkdirSync(path.join(FIN, 'work'), { recursive: true });
    fs.writeFileSync(path.join(FIN, 'work', name + '.png'), Buffer.from(url.split(',')[1], 'base64'));
  }
  await b.close();
})();
