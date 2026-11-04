// Isolated T03 adapter: stages all views before mutation; not a production integration.
import {makeGlyphFrame} from './geometry.mjs';
export function stageThreeViews(entries) {
  if (!Array.isArray(entries) || entries.length !== 3) throw new RangeError('exactly three views required');
  const ids = new Set();
  return Object.freeze(entries.map(({id, inkBBox, anchor, optical}) => {
    if (typeof id !== 'string' || !id || ids.has(id)) throw new TypeError('invalid/duplicate view ID');
    ids.add(id);
    const frame = makeGlyphFrame({inkBBox,anchor,optical});
    return Object.freeze({id,frame});
  }));
}
export function mapThreeViewPointer(staged, id, screenPoint, screenToLogical) {
  if (!Array.isArray(staged) || staged.length !== 3) throw new TypeError('unstaged views');
  const item=staged.find(v=>v.id===id);
  if (!item) throw new RangeError('unknown view');
  if (typeof screenToLogical !== 'function') throw new TypeError('missing mapping');
  return item.frame.toSource(screenToLogical(screenPoint));
}
