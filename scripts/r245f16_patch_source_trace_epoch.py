#!/usr/bin/env python3
"""Apply the R245F16 async trace import epoch guard to the R245F4 fork workbench.

Requires the verified cumulative ZIP extraction containing
v036_r245f4/R245F4_source_epoch_atomic_notes_workbench.html.
Does not touch production index.html or user storage.
"""
from pathlib import Path
import sys
root=Path(sys.argv[1]).resolve()
src=root/"v036_r245f4/R245F4_source_epoch_atomic_notes_workbench.html"
dst=root/"v036_r245f16/R245F16_source_epoch_atomic_trace_workbench.html"
old="$('traceImport').addEventListener('change',async e=>{const file=e.target.files[0];e.target.value='';if(!file||file.size>1048576){traceStatus('拒绝超过1MB的导入文件');return}try{traceImportData(JSON.parse(await file.text()))}catch(err){traceStatus('拒绝导入：'+err.message)}});"
new="""// R245F16: bind async trace import to the source verification epoch.
async function traceImportFile(file){
 const importEpoch=evidenceEpoch;
 if(!imageReady||!sourceVerified||!registryVerified)throw Error('原始来源字节尚未校验');
 if(!file||file.size>1048576)throw Error('文件不存在或超过1MB');
 const raw=await file.text();
 if(importEpoch!==evidenceEpoch||!imageReady||!sourceVerified||!registryVerified)
  throw Error('描记导入期间来源验证状态已变化，拒绝过期结果');
 const parsed=JSON.parse(raw);
 if(importEpoch!==evidenceEpoch||!imageReady||!sourceVerified||!registryVerified)
  throw Error('描记导入期间来源验证状态已变化，拒绝过期结果');
 return traceImportData(parsed);
}
$('traceImport').addEventListener('change',async e=>{
 const file=e.target.files[0];e.target.value='';
 try{await traceImportFile(file)}catch(err){traceStatus('拒绝导入：'+err.message)}
});"""
s=src.read_text(encoding="utf-8")
assert s.count(old)==1, "parent source differs"
dst.parent.mkdir(parents=True,exist_ok=True)
dst.write_text(s.replace(old,new),encoding="utf-8")
print(dst)
