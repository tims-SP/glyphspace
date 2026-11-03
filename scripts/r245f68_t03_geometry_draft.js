// R245F68 Root T03: read-only normalized geometry draft.
// Embed after GlyphSpaceT03Preview, GlyphSpaceT03Paint and GlyphSpaceT03Binding.
// This module is isolated and must not be loaded by production V0.35.
window.GlyphSpaceT03Geometry=(()=>{'use strict';
 const preview=window.GlyphSpaceT03Preview,paint=window.GlyphSpaceT03Paint,binding=window.GlyphSpaceT03Binding;
 const round=n=>Math.round(n*10000)/10000;
 const assert=(condition,why)=>{if(!condition)throw Error('T03 geometry draft: '+why)};
 async function snapshot(legacyInstanceId){
  const identity=binding.resolveLegacy(legacyInstanceId);
  assert(identity.role==='legacy_visual'&&identity.approvalStatus==='planning_only','unapproved or nonvisual identity');
  const revision=preview.getRevision();
  const m=await paint.measure(legacyInstanceId,400);
  assert(preview.getRevision()===revision,'concurrent geometry mutation');
  const placement=preview.getPlacement(legacyInstanceId),optical=preview.offsets.get(legacyInstanceId)||[0,0];
  const b=m.paintedBBox,dx=(placement?.dx||0)+optical[0],dy=(placement?.dy||0)+optical[1];
  const x=round(b.x+dx),y=round(b.y+dy),width=round(b.width),height=round(b.height);
  assert([x,y,width,height,...optical].every(Number.isFinite)&&width>0&&height>0,'invalid painted bbox');
  assert(x>=-0.001&&y>=-0.001&&x+width<=100.001&&y+height<=100.001,'ink outside 100x100');
  assert(preview.getRevision()===revision,'stale geometry draft');
  const geometry=Object.freeze({x,y,width,height,anchor:placement?.anchor||'ink-center',ox:optical[0],oy:optical[1]});
  return Object.freeze({candidateInstanceId:identity.candidateInstanceId,legacyInstanceId,key:identity.key,
    referenceShapeId:null,assetId:null,geometry,paintedBBox:Object.freeze({...b}),
    inkBBoxCertified:false,sourceCertified:false,permanentIdApproved:false,status:'planning_only'});
 }
 async function exportAll(){
  const revision=preview.getRevision();
  const ids=binding.all().filter(r=>r.role==='legacy_visual').map(r=>r.legacyInstanceId).sort();
  assert(ids.length===151&&new Set(ids).size===151,'151 unique legacy visual instances required');
  const records=[];
  for(const id of ids){
   assert(preview.getRevision()===revision,'concurrent export mutation');
   records.push(await snapshot(id));
  }
  assert(preview.getRevision()===revision,'concurrent export mutation');
  assert(new Set(records.map(r=>r.candidateInstanceId)).size===151,'candidate identity collision');
  return Object.freeze({schemaVersion:'T03-isolated-draft-1',coordinateSystem:'0 0 100 100',
    inkBBoxMethod:'chromium-alpha-raster-16of255',sourceCertified:false,permanentIDsApproved:0,
    records:Object.freeze(records)});
 }
 return Object.freeze({snapshot,exportAll});
})();
