#!/usr/bin/env python3
"""Apply the R245F14 Root T03 precommit inkBBox guard to an isolated R245F13 HTML candidate.

Never edit the frozen V0.35 production entry. Source/target must differ.
The cumulative R245F14 ZIP contains the complete generated candidate and Chromium QA.
"""
import argparse
from pathlib import Path

OLD_APPLY = "function applyCoords(raw){if(!validCoords(raw))return false;for(const [key,points] of Object.entries(raw))ROOT_COORDS[key]=points.map(x=>[...x]);return true}"
NEW_APPLY = """function applyCoords(raw){
 if(!validCoords(raw))return false;
 const projected=coordSnapshot();
 for(const [key,points] of Object.entries(raw))projected[key]=points.map(x=>[...x]);
 if(window.GlyphSpaceR245F12?.validateSnapshot){
  try{window.GlyphSpaceR245F12.validateSnapshot(projected)}
  catch(e){window.__r245f14LastRejected=String(e);return false}
 }
 for(const [key,points] of Object.entries(raw))ROOT_COORDS[key]=points.map(x=>[...x]);
 return true
}"""
OLD_SET = "function setCalibValue(dimension,value){const key=byId('refKey').value||'G';ROOT_COORDS[key][calibRootIndex][dimension]=value;saveCoords();synchronizeCoords();refreshCalibInputs();updateQualitySummary()}"
NEW_SET = """function setCalibValue(dimension,value){
 const key=byId('refKey').value||'G';
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
OLD_API = "window.GlyphSpaceR245F12=Object.freeze({inspect(){"
NEW_API = """window.GlyphSpaceR245F12=Object.freeze({
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

def main():
    p=argparse.ArgumentParser()
    p.add_argument("source",type=Path)
    p.add_argument("target",type=Path)
    a=p.parse_args()
    if a.source.resolve()==a.target.resolve():
        p.error("refuse in-place edit")
    text=a.source.read_text(encoding="utf-8")
    for old,new in [(OLD_APPLY,NEW_APPLY),(OLD_SET,NEW_SET),(OLD_API,NEW_API)]:
        if text.count(old)!=1:
            raise ValueError("patch anchor missing or ambiguous: "+old[:50])
        text=text.replace(old,new)
    a.target.parent.mkdir(parents=True,exist_ok=True)
    a.target.write_text(text,encoding="utf-8")

if __name__=="__main__":
    main()
