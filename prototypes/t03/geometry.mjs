// Isolated T03 geometry kernel. Not wired to the frozen V0.35 entry.
const finite = n => typeof n === 'number' && Number.isFinite(n);
function point(p) {
  if (!p || !finite(p.x) || !finite(p.y)) throw new TypeError('invalid point');
  return {x:p.x,y:p.y};
}
export function normalizeInkBBox(box) {
  if (!box || ![box.x,box.y,box.width,box.height].every(finite) ||
      box.width <= 0 || box.height <= 0) throw new RangeError('invalid inkBBox');
  return Object.freeze({x:box.x,y:box.y,width:box.width,height:box.height});
}
export function makeGlyphFrame({inkBBox,anchor, optical={x:0,y:0}}) {
  const b=normalizeInkBBox(inkBBox), a=point(anchor), o=point(optical);
  // 100x100 logical glyph space; anchor and optical offsets are logical units.
  const scale=100/Math.max(b.width,b.height);
  const center={x:b.x+b.width/2,y:b.y+b.height/2};
  const toLogical=p=>{
    p=point(p);
    return {x:50+(p.x-center.x)*scale+(50-a.x)+o.x,
            y:50+(p.y-center.y)*scale+(50-a.y)+o.y};
  };
  const toSource=p=>{
    p=point(p);
    return {x:center.x+(p.x-50-(50-a.x)-o.x)/scale,
            y:center.y+(p.y-50-(50-a.y)-o.y)/scale};
  };
  return Object.freeze({inkBBox:b,anchor:a,optical:o,scale,toLogical,toSource});
}
export function invertAffine(matrix, p) {
  if (!matrix || ![matrix.a,matrix.b,matrix.c,matrix.d,matrix.e,matrix.f].every(finite))
    throw new TypeError('invalid affine');
  p=point(p);
  const {a,b,c,d,e,f}=matrix, det=a*d-b*c;
  if (!finite(det)||Math.abs(det)<1e-12) throw new RangeError('singular affine');
  return {x:(d*(p.x-e)-c*(p.y-f))/det,
          y:(-b*(p.x-e)+a*(p.y-f))/det};
}
