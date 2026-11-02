/* Root T03 isolated, unapproved geometry transaction core V2. No storage or production DOM.
 * R245F71: compare-and-swap revision, immutable journal and deterministic replay.
 * FNV32 is an accidental-drift checksum, NOT a cryptographic source or identity certification. */
window.GlyphSpaceT03RegistryV2=(()=>{'use strict';
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
  const normalized=Object.fromEntries(shape.map(k=>[k,k==='anchor'?g[k]:round(g[k])]));
  if(normalized.width<=0||normalized.height<=0||normalized.x<0||normalized.y<0||
     normalized.x+normalized.width>100||normalized.y+normalized.height>100)fail('rounded geometry outside 100x100');
  return Object.freeze(normalized);
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
  if(!placeholder&&(!exact(r.paintedBBox,['x','y','width','height'])||!Object.values(r.paintedBBox).every(finite)||
    r.paintedBBox.width<=0||r.paintedBBox.height<=0||r.paintedBBox.x<0||r.paintedBBox.y<0||
    r.paintedBBox.x+r.paintedBBox.width>100.001||r.paintedBBox.y+r.paintedBBox.height>100.001))fail('invalid source painted bbox');
  return Object.freeze({...r,geometry:geometry(r.geometry),paintedBBox:placeholder?null:Object.freeze({...r.paintedBBox})});
 }
 const freezeDeep=x=>{if(x&&typeof x==='object'){Object.values(x).forEach(freezeDeep);Object.freeze(x)}return x};
 const checksum=x=>{const s=JSON.stringify(x);let h=2166136261;for(let i=0;i<s.length;i++){h=Math.imul(h^s.charCodeAt(i),16777619)}return (h>>>0).toString(16).padStart(8,'0')};
 function fromCatalog(catalog){
  if(!isRecord(catalog)||catalog.schemaVersion!=='T03-isolated-draft-1'||catalog.coordinateSystem!=='0 0 100 100'||catalog.sourceCertified!==false||catalog.permanentIDsApproved!==0||!Array.isArray(catalog.records)||catalog.records.length!==151)fail('invalid draft catalog');
  const initial=catalog.records.map(record),byId=new Map(initial.map(r=>[r.candidateInstanceId,r]));
  if(byId.size!==151||new Set(initial.map(r=>r.legacyInstanceId)).size!==151||new Set(initial.map(r=>r.key)).size!==25)fail('draft identity coverage mismatch');
  let rows=byId,order=initial.map(r=>r.candidateInstanceId),revision=0;
  const baseChecksum=checksum(initial),journal=[];
  const get=id=>rows.get(id)||null;
  const list=()=>Object.freeze(order.map(id=>rows.get(id)));
  const exportDraft=()=>Object.freeze({schemaVersion:'T03-isolated-registry-1',coordinateSystem:'0 0 100 100',sourceCertified:false,permanentIDsApproved:0,revision,records:list()});
  function apply(ops,expectedRevision,commit){
   if(!Number.isSafeInteger(expectedRevision)||expectedRevision!==revision)fail('stale or missing expectedRevision');
   if(!Array.isArray(ops)||ops.length===0||ops.length>151)fail('invalid transaction');
   const next=new Map(rows),nextOrder=[...order],touched=new Set(),canonicalOps=[];
   for(const op of ops){
    if(!isRecord(op)||!['move','reorder','insert','remove'].includes(op.type)||typeof op.id!=='string')fail('invalid operation');
    if(touched.has(op.id))fail('duplicate operation target');touched.add(op.id);
    if(op.type==='insert'){
     if(!exact(op,['type','id','record'])||op.id!==op.record?.candidateInstanceId||next.has(op.id))fail('invalid insert operation');
     const inserted=record(op.record);
     if(inserted.legacyInstanceId!==null)fail('cannot insert a fabricated legacy source');
     next.set(op.id,inserted);nextOrder.push(op.id);
     canonicalOps.push(freezeDeep({type:'insert',id:op.id,record:{...inserted,geometry:{...inserted.geometry}}}));
    }else if(op.type==='remove'){
     if(!exact(op,['type','id'])||!next.has(op.id)||next.get(op.id).legacyInstanceId!==null)fail('cannot remove legacy source');
     next.delete(op.id);nextOrder.splice(nextOrder.indexOf(op.id),1);
     canonicalOps.push(Object.freeze({type:'remove',id:op.id}));
    }else if(!next.has(op.id))fail('unknown operation target');
    else if(op.type==='move'){
     if(!exact(op,['type','id','geometry']))fail('invalid move operation');
     const before=next.get(op.id),updated=geometry(op.geometry);
     next.set(op.id,Object.freeze({...before,geometry:updated}));
     canonicalOps.push(freezeDeep({type:'move',id:op.id,geometry:{...updated}}));
    }else{
     if(!exact(op,['type','id','before']))fail('invalid reorder operation');
     if(op.before!==null&&(typeof op.before!=='string'||!next.has(op.before)||op.before===op.id))fail('invalid reorder reference');
     nextOrder.splice(nextOrder.indexOf(op.id),1);
     const at=op.before===null?nextOrder.length:nextOrder.indexOf(op.before);
     if(at<0)fail('missing reorder reference');nextOrder.splice(at,0,op.id);
     canonicalOps.push(Object.freeze({type:'reorder',id:op.id,before:op.before}));
    }
   }
   if(nextOrder.length!==next.size||new Set(nextOrder).size!==next.size)fail('identity set changed');
   const nextRecords=nextOrder.map(id=>next.get(id));
   const nextChecksum=checksum(nextRecords);
   if(commit){
    rows=next;order=nextOrder;revision++;
    journal.push(freezeDeep({expectedRevision,revision,ops:canonicalOps,postChecksumFNV32:nextChecksum}));
    return exportDraft();
   }
   return freezeDeep({expectedRevision,nextRevision:revision+1,postChecksumFNV32:nextChecksum,records:nextRecords});
  }
  const transact=(ops,expectedRevision)=>apply(ops,expectedRevision,true);
  const preview=(ops,expectedRevision)=>apply(ops,expectedRevision,false);
  const exportJournal=()=>freezeDeep({schemaVersion:'T03-isolated-journal-1',coordinateSystem:'0 0 100 100',
   sourceCertified:false,permanentIDsApproved:0,baseChecksumFNV32:baseChecksum,
   revision,entries:journal.map(e=>({expectedRevision:e.expectedRevision,revision:e.revision,
    ops:e.ops.map(o=>JSON.parse(JSON.stringify(o))),postChecksumFNV32:e.postChecksumFNV32}))});
  return Object.freeze({get,list,exportDraft,transact,preview,exportJournal,getRevision:()=>revision});
 }
 function replayJournal(catalog,log){
  if(!exact(log,['schemaVersion','coordinateSystem','sourceCertified','permanentIDsApproved','baseChecksumFNV32','revision','entries'])||
     log.schemaVersion!=='T03-isolated-journal-1'||log.coordinateSystem!=='0 0 100 100'||
     log.sourceCertified!==false||log.permanentIDsApproved!==0||!Array.isArray(log.entries)||
     !Number.isSafeInteger(log.revision)||log.revision!==log.entries.length)fail('invalid journal schema');
  const reg=fromCatalog(catalog);
  if(log.baseChecksumFNV32!==reg.exportJournal().baseChecksumFNV32)fail('journal baseline mismatch');
  for(const e of log.entries){
   if(!exact(e,['expectedRevision','revision','ops','postChecksumFNV32'])||e.expectedRevision!==reg.getRevision()||e.revision!==e.expectedRevision+1||
      typeof e.postChecksumFNV32!=='string')fail('journal entry mismatch');
   reg.transact(e.ops,e.expectedRevision);
   const produced=reg.exportJournal().entries.at(-1);
   if(produced.postChecksumFNV32!==e.postChecksumFNV32)fail('journal post-state mismatch');
  }
  return reg;
 }
 return Object.freeze({fromCatalog,replayJournal});
})();
