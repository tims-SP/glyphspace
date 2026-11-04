import assert from 'node:assert/strict';
import {stageThreeViews,mapThreeViewPointer} from './three-view.mjs';
const inputs=['keyboard','focus','mini'].map((id,i)=>({id,inkBBox:{x:i*10,y:0,width:20,height:40},anchor:{x:50,y:50},optical:{x:i,y:-i}}));
const staged=stageThreeViews(inputs);
let checks=0;
for(let i=0;i<3;i++) {
 const p={x:15+i*10,y:20};
 const logical=staged[i].frame.toLogical(p);
 const recovered=mapThreeViewPointer(staged,inputs[i].id,logical,x=>x);
 assert.ok(Math.abs(recovered.x-p.x)<1e-9);checks++;
 assert.ok(Math.abs(recovered.y-p.y)<1e-9);checks++;
}
for(const bad of [inputs.slice(0,2),[inputs[0],inputs[0],inputs[2]],[inputs[0],{...inputs[1],anchor:{x:NaN,y:0}},inputs[2]]]) {assert.throws(()=>stageThreeViews(bad));checks++;}
assert.throws(()=>mapThreeViewPointer(staged,'missing',{x:0,y:0},x=>x));checks++;
assert.throws(()=>mapThreeViewPointer(staged,'keyboard',{x:0,y:0},null));checks++;
console.log('PASS isolated T03 three-view adapter assertions:',checks);
