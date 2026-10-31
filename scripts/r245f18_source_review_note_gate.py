#!/usr/bin/env python3
"""R245F18 independent source-review note provenance gate.
Input: R245F17 source workbench HTML. Output: isolated R245F18 candidate.
Does not modify the production entry, frozen source, SVG, or user storage.
"""
from pathlib import Path
import sys
src=Path(sys.argv[1]); dst=Path(sys.argv[2]); s=src.read_text()
def patch(old,new):
 global s
 assert s.count(old)==1,(s.count(old),old[:60])
 s=s.replace(old,new,1)
patch('R245F17 来源验证并发原子性工作台','R245F18 来源审阅意见验证门禁工作台')
patch("提出禁止编辑标记", "提出禁止编辑标记") if False else None
patch("$('decision').disabled=!activeCase;$('notes').disabled=!activeCase;}","$('decision').disabled=!activeCase||!sourceReviewReady();$('notes').disabled=!activeCase||!sourceReviewReady();$('export').disabled=!sourceReviewReady();$('import').disabled=!sourceReviewReady();}")
patch("function saveCurrent(){if(!activeCase)return;","function sourceReviewReady(){return imageReady&&sourceVerified&&registryVerified}\nfunction saveCurrent(){if(!activeCase||!sourceReviewReady())return false;")
patch("function exportNotes(){saveCurrent();","function exportNotes(){if(!sourceReviewReady()){message('原始JPEG和注册表尚未校验，拒绝导出来源审阅意见');return false}saveCurrent();")
patch("imageReady=false;sourceVerified=false;registryVerified=false;\n if(tracePointerId","imageReady=false;sourceVerified=false;registryVerified=false;\n showLists(); // Disable note editing and discard unverified draft text.\n if(tracePointerId")
patch("registryVerified=true;sourceVerified=true;imageReady=true;evidenceError=null;","registryVerified=true;sourceVerified=true;imageReady=true;evidenceError=null;\n  showLists();")
patch("imageReady=false;sourceVerified=false;registryVerified=false;\n  evidenceError=String(err.message||err);","imageReady=false;sourceVerified=false;registryVerified=false;\n  showLists();\n  evidenceError=String(err.message||err);")
patch("imageReady=false;sourceVerified=false;registryVerified=false;\n  evidenceError='自动读取受限：'","imageReady=false;sourceVerified=false;registryVerified=false;\n  showLists();\n  evidenceError='自动读取受限：'")
dst.parent.mkdir(parents=True,exist_ok=True);dst.write_text(s)
print(dst)
