#!/usr/bin/env python3
"""Rebuild F75 isolated source-pixel/segment guard from the untouched R245 workbench.
No production file or user storage is accessed. Source identity remains unapproved.
"""
from pathlib import Path
import hashlib
ROOT=Path(__file__).resolve().parent.parent
SOURCE=ROOT/'v036_round245/R245_source_case_bound_stroke_review_workbench.html'
DEST=ROOT/'v036_r245f75/R245F75_M_shadow_segment_ownership_workbench.html'
s=SOURCE.read_text(encoding='utf-8')
needle="function traceOverlay(){if(!imageReady)return;"
helper=r'''// R245F75: M04/06/07/08 are unapproved; context pixels/segments may not cross another exact M crop.
function traceF75OtherExactCrops(caseId,obs){
 const match=/^review-only\/M\/shadow-2008-M-vis-(04|06|07|08)$/.exec(caseId||'');
 if(!match)return null;
 if(!obs||obs.sourceObservationId!=='M-candidate:2008-M-vis-'+match[1])return false;
 return keyMap.get('M').observations.filter(o=>
  /^M-candidate:2008-M-vis-/.test(o.sourceObservationId)&&o.sourceObservationId!==obs.sourceObservationId)
  .map(o=>o.nativeRect);
}
function traceF75PointInside(p,r){return p[0]>=r[0]&&p[0]<=r[0]+r[2]&&p[1]>=r[1]&&p[1]<=r[1]+r[3]}
function traceF75SegmentHitsRect(a,b,r){
 // Closed rectangle, Liang-Barsky clipping: even a crossing without a sampled point is forbidden.
 let lo=0,hi=1;const dx=b[0]-a[0],dy=b[1]-a[1];
 const ps=[-dx,dx,-dy,dy],qs=[a[0]-r[0],r[0]+r[2]-a[0],a[1]-r[1],r[1]+r[3]-a[1]];
 for(let i=0;i<4;i++){
  if(ps[i]===0){if(qs[i]<0)return false;continue}
  const t=qs[i]/ps[i];if(ps[i]<0)lo=Math.max(lo,t);else hi=Math.min(hi,t);
  if(lo>hi)return false;
 }
 return true;
}
function traceF75OwnershipClean(caseId,obs,points){
 const rects=traceF75OtherExactCrops(caseId,obs);
 if(rects===null)return true;
 if(rects===false)return false;
 for(const p of points)if(rects.some(r=>traceF75PointInside(p,r)))return false;
 for(let i=1;i<points.length;i++)if(rects.some(r=>traceF75SegmentHitsRect(points[i-1],points[i],r)))return false;
 return true;
}
'''
assert s.count(needle)==1
s=s.replace(needle,helper+needle)
old="if(!traceValidPoint(x,y,obs))return false;const point=[Math.round(x*100)/100,Math.round(y*100)/100];traceDraft.push({obs,xy:point});"
new="if(!traceValidPoint(x,y,obs))return false;const point=[Math.round(x*100)/100,Math.round(y*100)/100];if(!traceValidPoint(point[0],point[1],obs)||!traceF75OwnershipClean(activeCase,obs,[...traceDraft.map(p=>p.xy),point])){traceDraft=[];draw();traceStatus('跨候选精确来源框的像素或笔画已隔离，当前草案取消');return false}traceDraft.push({obs,xy:point});"
assert s.count(old)==1;s=s.replace(old,new)
old="if(!pts.every(p=>traceValidPoint(p[0],p[1],obs))){traceStatus('来源裁框范围异常，拒绝');return false}"
new="if(!pts.every(p=>traceValidPoint(p[0],p[1],obs))||!traceF75OwnershipClean(activeCase,obs,pts)){traceDraft=[];draw();traceStatus('来源裁框/跨候选笔画归属异常，拒绝');return false}"
assert s.count(old)==1;s=s.replace(old,new)
old="traceValidPoint(p[0],p[1],obs))))throw Error('笔画坐标/来源SHA无效：'+id);"
new="traceValidPoint(p[0],p[1],obs)))||!traceF75OwnershipClean(id,obs,s.points))throw Error('笔画坐标/来源SHA/跨候选笔画归属无效：'+id);"
assert s.count(old)==1;s=s.replace(old,new)
assert s.count('function traceF75OwnershipClean(')==1
DEST.write_text(s,encoding='utf-8')
print({'output':str(DEST),'bytes':DEST.stat().st_size,'sha256':hashlib.sha256(DEST.read_bytes()).hexdigest()})
