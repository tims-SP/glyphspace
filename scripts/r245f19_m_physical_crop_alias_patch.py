from pathlib import Path
src=Path(__file__).resolve().parents[1]/'v036_r245f18/R245F18_verified_source_review_note_gate_workbench.html'
dst=Path(__file__).with_name('R245F19_M_shared_physical_crop_review_candidate.html')
s=src.read_text(encoding='utf-8')
old='''function traceForeignCrops(obs){
 if(!obs)return [];
 const key=keys.find(k=>k.observations.includes(obs));
 return key?key.observations.filter(o=>o.sourceObservationId!==obs.sourceObservationId):[];
}'''
new='''// R245F19 Root T01/T02: explicit same-physical-crop M source aliases, NOT shape identity.
const M_PHYSICAL_CROP_PAIRS=Object.freeze([
 ['M-candidate:2008-M-vis-01','legacy:M:0'],
 ['M-candidate:2008-M-vis-02','legacy:M:1'],
 ['M-candidate:2008-M-vis-03','legacy:M:2'],
 ['M-candidate:2008-M-vis-05','legacy:M:3']
]);
function traceSameMPhysicalCrop(a,b){
 if(!a||!b)return false;
 const idA=a.sourceObservationId,idB=b.sourceObservationId;
 if(!M_PHYSICAL_CROP_PAIRS.some(pair=>pair.includes(idA)&&pair.includes(idB)&&idA!==idB))return false;
 return a.nativeRect.length===4&&b.nativeRect.length===4&&
  a.nativeRect.every((v,i)=>v===b.nativeRect[i])&&a.rgbSHA256===b.rgbSHA256;
}
function traceForeignCrops(obs){
 if(!obs)return [];
 const key=keys.find(k=>k.observations.includes(obs));
 return key?key.observations.filter(o=>o.sourceObservationId!==obs.sourceObservationId&&!traceSameMPhysicalCrop(obs,o)):[];
}'''
assert s.count(old)==1
s=s.replace(old,new)
dst.parent.mkdir(parents=True,exist_ok=True)
dst.write_text(s,encoding='utf-8')
