#!/usr/bin/env python3
"""Reproduce the R245F21 E/K source epoch fix from the R245F20 ZIP candidate.
Usage: python3 scripts/r245f21_source_epoch_patch.py OLD.html NEW.html
This changes only an isolated review workbench, never production index.html.
"""
import sys
from pathlib import Path
old, new = map(Path, sys.argv[1:3])
s = old.read_text(encoding="utf-8")
patches = [
 ("let view={left:0,top:0,scale:1};",
  "let view={left:0,top:0,scale:1};\nlet importRequest=0;"),
 ("async function verifySource(bytes){const epoch=++state.epoch;invalidate();const buffer=",
  "async function verifySource(bytes,sourceEpoch=null){const epoch=sourceEpoch===null?++state.epoch:sourceEpoch;if(epoch!==state.epoch)return false;invalidate();const buffer="),
 ("$('source').addEventListener('change',async e=>{try{const f=e.target.files[0];if(f)await verifySource(new Uint8Array(await f.arrayBuffer()))}catch(err){invalidate();status('来源加载失败：'+err.message)}});",
  "$('source').addEventListener('change',async e=>{const epoch=++state.epoch;invalidate();status('正在读取原图');try{const f=e.target.files[0];if(!f){status('未选择原图');return}const bytes=new Uint8Array(await f.arrayBuffer());if(epoch!==state.epoch)return;await verifySource(bytes,epoch)}catch(err){if(epoch!==state.epoch)return;++state.epoch;invalidate();status('来源加载失败：'+err.message)}});"),
 ("$('import').addEventListener('change',async e=>{try{const f=e.target.files[0];if(f){importData(JSON.parse(await f.text()));status('已导入未归属草案；没有批准任何ID')}}catch(err){status('导入拒绝：'+err.message)}});",
  "async function importFile(f){if(!state.verified)throw Error('source JPEG not verified');const epoch=state.epoch,request=++importRequest;const raw=await f.text();if(epoch!==state.epoch||request!==importRequest||!state.verified)throw Error('stale import/source verification');return importData(JSON.parse(raw))}\n$('import').addEventListener('change',async e=>{const f=e.target.files[0];if(!f)return;const epoch=state.epoch;try{await importFile(f);if(epoch===state.epoch)status('已导入未归属草案；没有批准任何ID')}catch(err){if(epoch===state.epoch)status('导入拒绝：'+err.message)}});"),
 ("verifySource,setGroup,addPoint,finish,documentData,importData,clear:",
  "verifySource,setGroup,addPoint,finish,documentData,importData,importFile,clear:"),
]
for before, after in patches:
    assert s.count(before) == 1, "R245F20 source changed; refusing patch"
    s = s.replace(before, after)
new.write_text(s, encoding="utf-8")
print("Patched isolated candidate:", new)
