/* R245F73: isolated Node VM fault-injection; no browser, storage or production writes. */
'use strict';
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
const source=fs.readFileSync(__dirname+'/r245f73_t03_live_three_view_bridge_v2.js','utf8');
let assertions=0;
function ok(v,msg){assert.ok(v,msg);assertions++}
function eq(a,b,msg){assert.deepEqual(a,b,msg);assertions++}
async function scenario(opts={}){
  const ids=['M-root-00','M-root-01'];
  const candidates=['wb06/M/legacy-00','wb06/M/legacy-01'];
  const base=ids.map((id,i)=>({id,candidateInstanceId:candidates[i],legacyInstanceId:id,
    sourceCertified:false,permanentIdApproved:false,geometry:{x:10+i*20,y:20,width:8,height:9,anchor:'ink-center',ox:0,oy:0}}));
  const rows=new Map(base.map(r=>[r.candidateInstanceId,structuredClone(r)]));
  const live=new Map(ids.map(id=>[id,{ox:0,oy:0}]));
  let pRev=0,rRev=0,setCalls=0,transacts=0;
  const P={getRevision:()=>pRev,setOptical(id,ox,oy){
    setCalls++;if(!live.has(id))throw Error('unknown');
    if(opts.failRollback && id==='M-root-01' && ox===0 && oy===0)throw Error('rollback failure');
    live.set(id,{ox,oy});pRev++;
    if(opts.failAfterMutation && id==='M-root-01' && ox===2 && oy===1)throw Error('setter mutated then threw');
  }};
  const reg={getRevision:()=>rRev,get:id=>rows.get(id),exportDraft:()=>({revision:rRev}),
    exportJournal:()=>({entries:transacts}),
    preview:(ops,expected)=>{eq(expected,rRev,'preview CAS');return {nextRevision:rRev+1}},
    transact:(ops,expected)=>{eq(expected,rRev,'commit CAS');transacts++;rRev++;
      for(const op of ops)rows.get(op.id).geometry=op.geometry;
      return {revision:opts.badCommitResult?rRev+1:rRev};
    }};
  const G={exportAll:async()=>({records:base}),snapshot:async id=>{
    const r=base.find(r=>r.id===id),l=live.get(id);
    return {geometry:{...r.geometry,x:r.geometry.x+l.ox,y:r.geometry.y+l.oy,ox:l.ox,oy:l.oy}};
  }};
  const R={fromCatalog:()=>reg};
  const win={GlyphSpaceT03Preview:P,GlyphSpaceT03Geometry:G,
    GlyphSpaceT03RegistryV2:R,GlyphSpaceT03Paint:{validate:id=>{ok(ids.includes(id),'paint validated')}}};
  vm.runInNewContext(source,{window:win,Error,Number,Math,Object,Array,Set,String});
  const bridge=await win.GlyphSpaceT03LiveBridgeV2.create();
  return {bridge,live,rows,base,getRevision:()=>rRev,getSetCalls:()=>setCalls,getTransacts:()=>transacts};
}
const batch=[{id:'wb06/M/legacy-00',ox:1,oy:0},{id:'wb06/M/legacy-01',ox:2,oy:1}];
(async()=>{
  {
    const x=await scenario();
    const r=await x.bridge.applyOptical(batch,0);
    eq(r.revision,1,'successful commit');eq(x.getRevision(),1,'registry revision');
    eq(x.live.get('M-root-00'),{ox:1,oy:0},'first applied');
    eq(x.live.get('M-root-01'),{ox:2,oy:1},'second applied');
    eq(x.getTransacts(),1,'single commit');
  }
  {
    const x=await scenario({failAfterMutation:true});
    await assert.rejects(x.bridge.applyOptical(batch,0),/setter mutated then threw/);assertions++;
    eq(x.live.get('M-root-00'),{ox:0,oy:0},'first rollback');
    eq(x.live.get('M-root-01'),{ox:0,oy:0},'partial setter rollback');
    eq(x.getRevision(),0,'no registry commit');
    eq(x.getTransacts(),0,'no journal commit');
    const r=await x.bridge.applyOptical([{id:'wb06/M/legacy-00',ox:1,oy:0}],0);
    eq(r.revision,1,'bridge usable after complete rollback');
  }
  {
    const x=await scenario({failAfterMutation:true,failRollback:true});
    await assert.rejects(x.bridge.applyOptical(batch,0),/rollback incomplete; bridge poisoned/);assertions++;
    const calls=x.getSetCalls();
    await assert.rejects(x.bridge.applyOptical([{id:'wb06/M/legacy-00',ox:1,oy:0}],0),/bridge poisoned/);assertions++;
    eq(x.getSetCalls(),calls,'poisoned bridge blocks subsequent writes');
    eq(x.getRevision(),0,'no registry commit after rollback failure');
  }
  {
    const x=await scenario({badCommitResult:true});
    await assert.rejects(x.bridge.applyOptical([{id:'wb06/M/legacy-00',ox:1,oy:0}],0),/registry already committed; bridge poisoned/);assertions++;
    eq(x.getRevision(),1,'registry committed');
    eq(x.live.get('M-root-00'),{ox:1,oy:0},'do not rollback DOM after committed registry');
    await assert.rejects(x.bridge.applyOptical([{id:'wb06/M/legacy-00',ox:2,oy:0}],1),/bridge poisoned/);assertions++;
  }
  {
    const x=await scenario();
    await assert.rejects(x.bridge.applyOptical([{id:'wb06/M/legacy-00',ox:7,oy:0}],0),/invalid or duplicate/);assertions++;
    eq(x.getSetCalls(),0,'invalid input no DOM writes');
  }
  console.log('R245F73 PASS assertions='+assertions+' scenarios=5; isolated Node VM only');
})().catch(e=>{console.error(e);process.exitCode=1});