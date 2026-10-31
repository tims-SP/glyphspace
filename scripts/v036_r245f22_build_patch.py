#!/usr/bin/env python3
"""R245F22: prevent pending source-review JSON imports overwriting local edits.

Edits only an isolated candidate; never changes V0.35, historical SVGs, or storage.
"""
from pathlib import Path
import sys
if len(sys.argv)!=2: raise SystemExit("usage: python scripts/v036_r245f22_build_patch.py /path/to/restored_parent")
BASE=Path(sys.argv[1]).resolve()
old=BASE/'v036_r245f21/R245F21_EK_source_epoch_atomic_workbench.html'
new=BASE/'v036_r245f22/R245F22_EK_edit_revision_atomic_workbench.html'
new.parent.mkdir(parents=True,exist_ok=True)
s=old.read_text()
repls=[
 ('let importRequest=0;', 'let importRequest=0;\n// Every local edit invalidates pending asynchronous imports, independently of source epochs.\nlet editRevision=0;'),
 ("state.points.push([...p]);draw();return true", "state.points.push([...p]);++editRevision;draw();return true"),
 ("state.drafts[state.active].strokes.push({points:state.points.map(p=>[...p])});state.points=[]", "state.drafts[state.active].strokes.push({points:state.points.map(p=>[...p])});++editRevision;state.points=[]"),
 ("state.drafts=next;state.points=[];state.drawing=false;ui();return true", "state.drafts=next;++editRevision;state.points=[];state.drawing=false;ui();return true"),
 ("state.drafts[state.active].strokes.pop();ui()", "state.drafts[state.active].strokes.pop();++editRevision;ui()"),
 ("state.drafts[state.active]={note:'',strokes:[]};ui()", "state.drafts[state.active]={note:'',strokes:[]};++editRevision;ui()"),
 ("if(state.verified)state.drafts[state.active].note=e.target.value", "if(state.verified){state.drafts[state.active].note=e.target.value;++editRevision}"),
 ("const epoch=state.epoch,request=++importRequest;const raw=await f.text();if(epoch!==state.epoch||request!==importRequest||!state.verified)throw Error('stale import/source verification');", "const epoch=state.epoch,revision=editRevision,request=++importRequest;const raw=await f.text();if(epoch!==state.epoch||revision!==editRevision||request!==importRequest||!state.verified)throw Error('stale import/source verification or newer local edits');"),
 ("state.drafts=Object.fromEntries(groups.map(g=>[g.groupId,{strokes:[],note:''}]));ui()", "state.drafts=Object.fromEntries(groups.map(g=>[g.groupId,{strokes:[],note:''}]));++editRevision;ui()"),
]
for before,after in repls:
 c=s.count(before)
 if c!=1:raise RuntimeError(f'expected 1 occurrence, got {c}: {before}')
 s=s.replace(before,after)
new.write_text(s)
print(new)
