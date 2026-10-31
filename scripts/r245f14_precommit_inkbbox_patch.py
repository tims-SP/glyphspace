#!/usr/bin/env python3
"""Root T03 isolated candidate: reject ink-out-of-bounds edits BEFORE changing UI state/storage.

Applies only to the named R245F13 candidate, producing R245F14. Never edits V0.35.
"""
from pathlib import Path
import argparse

OLD_APPLY="function applyCoords(raw){if(!validCoords(raw))return false;for(const [key,points] of Object.entries(raw))ROOT_COORDS[key]=points.map(x=>[...x]);return true}"
NEW_APPLY="""function applyCoords(raw){
 if(!validCoords(raw))return false;
 // R245F14: an import must be checked against the *complete* projected geometry
 // before changing ROOT_COORDS. Partial legacy patches retain their old semantics.
 const projected=coordSnapshot();
 for(const [key,points] of Object.entries(raw))projected[key]=points.map(x=>[...x]);
 if(window.GlyphSpaceR245F12?.validateSnapshot){
  try{window.GlyphSpaceR245F12.validateSnapshot(projected)}
  catch(e){window.__r245f14LastRejected=String(e);return false}
 }
 for(const [key,points] of Object.entries(raw))ROOT_COORDS[key]=points.map(x=>[...x]);
 return true
}"""
OLD_SET="function setCalibValue(dimension,value){const key=byId('refKey').value||'G';ROOT_COORDS[key][calibRootIndex][dimension]=value;saveCoords();synchronizeCoords();refreshCalibInputs();updateQualitySummary()}"
NEW_SET="""function setCalibValue(dimension,value){
 const key=byId('refKey').value||'G',before=ROOT_COORDS[key][calibRootIndex][dimension];
 // R245F14: the legacy editor used to save, repaint, and only then discover
 // an inkBBox violation. Keep the previous committed geometry/storage intact.
 if(window.GlyphSpaceR245F12?.validateSnapshot){
  const projected=coordSnapshot();projected[key][calibRootIndex][dimension]=value;
  try{window.GlyphSpaceR245F12.validateSnapshot(projected)}
  catch(e){
   window.__r245f14LastRejected=String(e);
   refreshCalibInputs();
   byId('calibAudit').textContent='校准未保存：轮廓越出键帽100×100边界；原位置已保留。';
   return false;
  }
 }
 ROOT_COORDS[key][calibRootIndex][dimension]=value;
 saveCoords();synchronizeCoords();refreshCalibInputs();updateQualitySummary();
 return true;
}"""
OLD_API="window.GlyphSpaceR245F12=Object.freeze({inspect(){"
NEW_API="""window.GlyphSpaceR245F12=Object.freeze({
 validateSnapshot(data){
  if(!data||typeof data!=='object'||Array.isArray(data))throw Error('invalid coordinate snapshot');
  try{
   for(const id of ids){
    const r=CATALOG[id],points=data[r.key],idx=Number(r.legacySlot.split(':')[1]);
    if(!Array.isArray(points)||!Array.isArray(points[idx])||points[idx].length!==3)throw Error('incomplete coordinate snapshot: '+id);
    targetFor(r,...points[idx]);
   }
  }catch(e){window.__r245f12LastError=null;throw e}
  return true;
 },
 inspect(){"""

def patch(source):
    for before,after in [(OLD_APPLY,NEW_APPLY),(OLD_SET,NEW_SET),(OLD_API,NEW_API)]:
        n=source.count(before)
        if n!=1:raise ValueError(f'expected exactly one patch anchor, got {n}: {before[:55]}')
        source=source.replace(before,after)
    return source

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('source',type=Path);a.add_argument('target',type=Path);args=a.parse_args()
    if args.source.resolve()==args.target.resolve():raise ValueError('refuse in-place edit')
    args.target.parent.mkdir(parents=True,exist_ok=True)
    args.target.write_text(patch(args.source.read_text()),encoding='utf-8')
    print(args.target)
