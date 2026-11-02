/* R245F73 — isolated T03 bridge with partial-setter rollback. No storage, network, or production writes. */
window.GlyphSpaceT03LiveBridgeV2=(()=>{'use strict';
  const fail=(message)=>{throw Error('T03 bridge: '+message)};
  const hasOwn=(o,k)=>Object.prototype.hasOwnProperty.call(o,k);
  const exact=(o,fields)=>o!==null&&typeof o==='object'&&!Array.isArray(o)&&
    Object.keys(o).length===fields.length&&fields.every(k=>hasOwn(o,k));
  const round=n=>Number(n.toFixed(4));
  async function create(){
    const P=window.GlyphSpaceT03Preview,G=window.GlyphSpaceT03Geometry,R=window.GlyphSpaceT03RegistryV2;
    if(!P||!G||!R)fail('missing isolated T03 dependencies');
    const catalog=await G.exportAll();
    const reg=R.fromCatalog(catalog);
    let previewRevision=P.getRevision(),busy=false,poisoned=false;
    const exportDraft=()=>reg.exportDraft();
    const exportJournal=()=>reg.exportJournal();
    const applyOptical=async(changes,expectedRevision)=>{
      if(poisoned)fail('bridge poisoned after incomplete rollback; recreate isolated bridge');
      if(busy)fail('concurrent bridge transaction');
      busy=true;
      try{
        if(!Number.isSafeInteger(expectedRevision)||expectedRevision!==reg.getRevision())fail('stale registry revision');
        if(previewRevision!==P.getRevision())fail('external preview mutation');
        if(!Array.isArray(changes)||changes.length<1||changes.length>151)fail('invalid change batch');
        const seen=new Set(),ops=[],old=[];
        for(const c of changes){
          if(!exact(c,['id','ox','oy'])||typeof c.id!=='string'||!Number.isFinite(c.ox)||!Number.isFinite(c.oy)||
             Math.abs(c.ox)>4||Math.abs(c.oy)>4||seen.has(c.id))fail('invalid or duplicate optical change');
          seen.add(c.id);
          const r=reg.get(c.id);
          if(!r||r.legacyInstanceId===null||r.sourceCertified||r.permanentIdApproved)fail('non-legacy or certified target');
          const g=r.geometry;
          const next={...g,x:round(g.x+c.ox-g.ox),y:round(g.y+c.oy-g.oy),ox:round(c.ox),oy:round(c.oy)};
          ops.push({type:'move',id:c.id,geometry:next});
          old.push({id:r.legacyInstanceId,ox:g.ox,oy:g.oy});
          window.GlyphSpaceT03Paint.validate(r.legacyInstanceId);
        }
        // Validate the complete registry transaction before touching any SVG node.
        const planned=reg.preview(ops,expectedRevision);
        const applied=[];
        let committed=false;
        try{
          for(let i=0;i<changes.length;i++){
            const r=reg.get(changes[i].id);
            // Record rollback obligation BEFORE setter: it may mutate DOM then throw.
            applied.push(old[i]);
            P.setOptical(r.legacyInstanceId,changes[i].ox,changes[i].oy);
          }
          // Read back actual raster-derived geometry; no fabricated ink certification.
          for(let i=0;i<changes.length;i++){
            const r=reg.get(changes[i].id),actual=await G.snapshot(r.legacyInstanceId),want=ops[i].geometry;
            if(['x','y','width','height','ox','oy','anchor'].some(k=>actual.geometry[k]!==want[k]))
              fail('live SVG geometry diverged from planned draft');
          }
          if(reg.getRevision()!==expectedRevision)fail('registry revision changed');
          const result=reg.transact(ops,expectedRevision);
          committed=true;
          if(result.revision!==planned.nextRevision)fail('unexpected committed revision');
          previewRevision=P.getRevision();
          return result;
        }catch(e){
          if(committed){poisoned=true;fail('registry already committed; bridge poisoned: '+String(e))}
          const errors=[];
          for(const x of applied.reverse())try{P.setOptical(x.id,x.ox,x.oy)}catch(rollbackError){errors.push(String(rollbackError))}
          if(errors.length){poisoned=true;fail('rollback incomplete; bridge poisoned: '+errors.join('; '))}
          previewRevision=P.getRevision();
          throw e;
        }
      }finally{busy=false}
    };
    return Object.freeze({applyOptical,exportDraft,exportJournal,getRevision:()=>reg.getRevision(),
      sourceCertified:false,permanentIDsApproved:0});
  }
  return Object.freeze({create});
})();
