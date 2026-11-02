/* Root T03 isolated, unapproved geometry transaction core. Never writes storage or production DOM. */
window.GlyphSpaceT03Registry=(()=>{'use strict';
 const FAIL='T03 draft registry: ';
 const fail=message=>{throw Error(FAIL+message)};
 const anchors=new Set(['ink-center','ink-top-left','ink-bottom-left']);
 const round=x=>Math.round(x*10000)/10000;
 const shape=Object.freeze(['x','y','width','height','anchor','ox','oy']);
 const own=(o,k)=>Object.prototype.hasOwnProperty.call(o,k);
 const finite=x=>typeof x==='number'&&Number.isFinite(x);
 const isRecord=x=>x!==null&&typeof x==='object'&&!Array.isArray(x);
 const exact=(o,keys)=>isRecord(o)&&Object.keys(o).length===keys.length&&keys.every(k=>own(o,k));
 function geometry(g){
  if(!exact(g,shape))fail('geometry shape mismatch');
  if(!anchors.has(g.anchor)||!['x','y','width','height','ox','oy'].every(k=>finite(g[k])))fail('invalid geometry values');
  if(g.width<=0||g.height<=0||g.x<0||g.y<0||g.x+g.width>100.001||g.y+g.height>100.001)fail('outside 100x100');
  if(Math.abs(g.ox)>4||Math.abs(g.oy)>4)fail('optical correction exceeds draft bound');
  return Object.freeze(Object.fromEntries(shape.map(k=>[k,k==='anchor'?g[k]:round(g[k])])));
 }
 const rowKeys=Object.freeze(['candidateInstanceId','legacyInstanceId','key','referenceShapeId','assetId','geometry','paintedBBox','inkBBoxCertified','sourceCertified','permanentIdApproved','status']);
 function record(r){
  if(!exact(r,rowKeys))fail('record shape mismatch');
  if(typeof r.candidateInstanceId!=='string'||!/^([A-Z])$/.test(r.key))fail('invalid candidate identity');
  const placeholder=/^draft-only\/[A-Z]\/[a-z0-9-]{3,48}$/.test(r.candidateInstanceId);
  const legacy=/^wb06\/[A-Z]\/legacy-\d\d$/.test(r.candidateInstanceId);
  if(!placeholder&&!legacy)fail('invalid draft namespace');
  if(r.candidateInstanceId.split('/')[1]!==r.key)fail('candidate key mismatch');
  if(placeholder){if(r.legacyInstanceId!==null||r.paintedBBox!==null)fail('draft placeholder must not claim legacy glyph or ink');}
  else if(typeof r.legacyInstanceId!=='string'||!/^[A-Z]-root-\d\d$/.test(r.legacyInstanceId)||r.legacyInstanceId[0]!==r.key)fail('invalid legacy binding');
  if(r.referenceShapeId!==null||r.assetId!==null||r.inkBBoxCertified!==false||r.sourceCertified!==false||r.permanentIdApproved!==false||r.status!=='planning_only')fail('unapproved certification or source');
  if(!placeholder&&(!exact(r.paintedBBox,['x','y','width','height'])||!Object.values(r.paintedBBox).every(finite)||r.paintedBBox.width<=0||r.paintedBBox.height<=0))fail('invalid source painted bbox');
  return Object.freeze({...r,geometry:geometry(r.geometry),paintedBBox:placeholder?null:Object.freeze({...r.paintedBBox})});
 }
 function fromCatalog(catalog){
  if(!isRecord(catalog)||catalog.schemaVersion!=='T03-isolated-draft-1'||catalog.coordinateSystem!=='0 0 100 100'||catalog.sourceCertified!==false||catalog.permanentIDsApproved!==0||!Array.isArray(catalog.records)||catalog.records.length!==151)fail('invalid draft catalog');
  const initial=catalog.records.map(record),byId=new Map(initial.map(r=>[r.candidateInstanceId,r]));
  if(byId.size!==151||new Set(initial.map(r=>r.legacyInstanceId)).size!==151||new Set(initial.map(r=>r.key)).size!==25)fail('draft identity coverage mismatch');
  let rows=byId,order=initial.map(r=>r.candidateInstanceId),revision=0;
  const get=id=>rows.get(id)||null;
  const list=()=>Object.freeze(order.map(id=>rows.get(id)));
  const exportDraft=()=>Object.freeze({schemaVersion:'T03-isolated-registry-1',coordinateSystem:'0 0 100 100',sourceCertified:false,permanentIDsApproved:0,revision,records:list()});
  function transact(ops){
   if(!Array.isArray(ops)||ops.length===0||ops.length>151)fail('invalid transaction');
   const next=new Map(rows),nextOrder=[...order],touched=new Set();
   for(const op of ops){
    if(!isRecord(op)||!['move','reorder','insert','remove'].includes(op.type)||typeof op.id!=='string')fail('invalid operation');
    if(touched.has(op.id))fail('duplicate operation target');touched.add(op.id);
    if(op.type==='insert'){
     if(!exact(op,['type','id','record'])||op.id!==op.record?.candidateInstanceId||next.has(op.id))fail('invalid insert operation');
     const inserted=record(op.record);
     if(inserted.legacyInstanceId!==null)fail('cannot insert a fabricated legacy source');
     next.set(op.id,inserted);nextOrder.push(op.id);
    }else if(op.type==='remove'){
     if(!exact(op,['type','id'])||!next.has(op.id)||next.get(op.id).legacyInstanceId!==null)fail('cannot remove legacy source');
     next.delete(op.id);nextOrder.splice(nextOrder.indexOf(op.id),1);
    }else if(!next.has(op.id))fail('unknown operation target');
    else if(op.type==='move'){
     if(!exact(op,['type','id','geometry']))fail('invalid move operation');
     const before=next.get(op.id),updated=geometry(op.geometry);
     next.set(op.id,Object.freeze({...before,geometry:updated}));
    }else{
     if(!exact(op,['type','id','before']))fail('invalid reorder operation');
     if(op.before!==null&&(typeof op.before!=='string'||!next.has(op.before)||op.before===op.id))fail('invalid reorder reference');
     nextOrder.splice(nextOrder.indexOf(op.id),1);
     const at=op.before===null?nextOrder.length:nextOrder.indexOf(op.before);
     if(at<0)fail('missing reorder reference');nextOrder.splice(at,0,op.id);
    }
   }
   if(nextOrder.length!==next.size||new Set(nextOrder).size!==next.size)fail('identity set changed');
   rows=next;order=nextOrder;revision++;
   return exportDraft();
  }
  return Object.freeze({get,list,exportDraft,transact,getRevision:()=>revision});
 }
 return Object.freeze({fromCatalog});
})();
