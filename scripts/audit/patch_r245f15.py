from pathlib import Path
import sys
root=Path(sys.argv[1])
old=(root/'v036_r245f14/R245F14_T03_precommit_ink_bounds_candidate.html').read_text()
needle='function setCalibValue(dimension,value){'
assert old.count(needle)==1
start=old.index(needle)
end=old.index('function exportCoords()',start)
replacement='''// R245F15: preflight the *live* three-view SVG DOM before touching coordinates,
// and only persist after a successful full post-commit inspection. This prevents
// a legitimate coordinate edit from saving over an already-tampered SVG scene.
function commitCalibTransaction(patch){
 const previous=coordSnapshot();let mutated=false;
 try{
  if(window.GlyphSpaceR245F12?.inspect)window.GlyphSpaceR245F12.inspect();
  if(!applyCoords(patch))throw Error(window.__r245f14LastRejected||'invalid coordinate patch');
  mutated=true;
  synchronizeCoords();
  if(window.GlyphSpaceR245F12?.inspect)window.GlyphSpaceR245F12.inspect();
  saveCoords();refreshCalibInputs();updateQualitySummary();
  window.__r245f15LastRejected=null;
  return true;
 }catch(e){
  if(mutated){
   for(const [key,points] of Object.entries(previous))ROOT_COORDS[key]=points.map(p=>[...p]);
   try{synchronizeCoords()}catch(_rollbackError){}
  }
  window.__r245f14LastRejected=String(e);
  window.__r245f15LastRejected=String(e);
  refreshCalibInputs();
  byId('calibAudit').textContent='校准未保存：轮廓越出边界或三视图字形状态异常；原位置已保留。';
  return false;
 }
}
function setCalibValue(dimension,value){
 const key=byId('refKey').value||'G',points=ROOT_COORDS[key].map(p=>[...p]);
 points[calibRootIndex][dimension]=value;
 return commitCalibTransaction({[key]:points});
}
'''
new=old[:start]+replacement+old[end:]
old_reset="byId('calibKeyReset').onclick=()=>{ROOT_COORDS[key.value]=COORD_DEFAULTS[key.value].map(a=>[...a]);saveCoords();synchronizeCoords();refreshCalibInputs();updateQualitySummary();toast('此键坐标已恢复初始复刻值')};"
new_reset="byId('calibKeyReset').onclick=()=>{if(commitCalibTransaction({[key.value]:COORD_DEFAULTS[key.value].map(a=>[...a])}))toast('此键坐标已恢复初始复刻值');else toast('重置未保存：三视图状态异常')};"
assert new.count(old_reset)==1
new=new.replace(old_reset,new_reset)
old_import="if(obj.format!=='wubi06-geometry-v1'||!applyCoords(obj.coords))throw Error('文件格式、字根数量或坐标范围不正确');saveCoords();synchronizeCoords();refreshCalibInputs();updateQualitySummary();toast('字根坐标补丁已导入');"
new_import="if(obj.format!=='wubi06-geometry-v1'||!commitCalibTransaction(obj.coords))throw Error('文件格式、轮廓或三视图状态不正确');toast('字根坐标补丁已导入');"
assert new.count(old_import)==1
new=new.replace(old_import,new_import)
out=root/'v036_r245f15/R245F15_T03_live_DOM_preflight_candidate.html'
out.parent.mkdir(exist_ok=True)
out.write_text(new)
print(out, len(new), 'old',len(old))
