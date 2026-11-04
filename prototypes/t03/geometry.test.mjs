import assert from 'node:assert/strict';
import {makeGlyphFrame,normalizeInkBBox,invertAffine} from './geometry.mjs';
let checks=0;
const ok=(a,b)=>{assert.ok(Math.abs(a-b)<1e-9,`${a} != ${b}`);checks++};
for(const box of [{x:12,y:23,width:20,height:40},{x:-9,y:4,width:120,height:15}])
 for(const anchor of [{x:50,y:50},{x:20,y:80}])
  for(const optical of [{x:0,y:0},{x:2.5,y:-3}]) {
   const frame=makeGlyphFrame({inkBBox:box,anchor,optical});
   for(const p of [{x:box.x,y:box.y},{x:box.x+box.width,y:box.y+box.height},{x:0,y:0}]) {
    const restored=frame.toSource(frame.toLogical(p));
    ok(restored.x,p.x);ok(restored.y,p.y);
   }
  }
const matrix={a:2,b:0.5,c:-1,d:3,e:9,f:-4}, p={x:7,y:-3};
const screen={x:matrix.a*p.x+matrix.c*p.y+matrix.e,y:matrix.b*p.x+matrix.d*p.y+matrix.f};
const restored=invertAffine(matrix,screen);ok(restored.x,p.x);ok(restored.y,p.y);
for(const bad of [{x:0,y:0,width:0,height:1},{x:0,y:0,width:1,height:NaN}]) {
 assert.throws(()=>normalizeInkBBox(bad));checks++;
}
assert.throws(()=>invertAffine({a:1,b:2,c:2,d:4,e:0,f:0},{x:0,y:0}));checks++;
assert.throws(()=>makeGlyphFrame({inkBBox:{x:0,y:0,width:1,height:1},anchor:{x:NaN,y:0}}));checks++;
console.log('PASS isolated T03 geometry assertions:',checks);
