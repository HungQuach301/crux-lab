const ROOT = 'file:///home/user/crux-lab';
export async function resolve(spec, ctx, next) {
  if (spec === 'three') return { url: new URL('./three-wrap.mjs', import.meta.url).href  /* three thật, WebGLRenderer giả */, shortCircuit: true };
  if (spec.startsWith('/toolkit/') || spec.startsWith('/episodes/')) return { url: ROOT + spec, shortCircuit: true };
  return next(spec, ctx);
}
