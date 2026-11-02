#!/usr/bin/env python3
"""R245F69 Root T03 isolated candidate patch; never edits production HTML."""
from pathlib import Path
import hashlib
import sys

root = Path(sys.argv[1]).resolve()
source = root / "v036_r245f68/R245F68_T03_normalized_geometry_draft_candidate.html"
target = root / "v036_r245f69/R245F69_T03_readonly_geometry_state_candidate.html"
raw = source.read_bytes()
assert hashlib.sha256(raw).hexdigest() == "9042d19a74d14357027fdbc039ec6f2ae7c71659696fffc9556c3f05e83ea6b5"
s = raw.decode("utf-8")
changes = [
    ("reset,nodes,keys,offsets,placements,getRevision:()=>geometryRevision",
     "reset,nodes,keys,offsets:Object.freeze({has:id=>offsets.has(id),get:id=>offsets.has(id)?Object.freeze([...offsets.get(id)]):undefined}),placements:Object.freeze({has:id=>placements.has(id),get:id=>placements.get(id)}),getOptical:(id)=>Object.freeze([...(offsets.get(id)||[0,0])]),getRevision:()=>geometryRevision"),
    ("preview.offsets.get(legacyInstanceId)||[0,0]", "preview.getOptical(legacyInstanceId)"),
]
for old, new in changes:
    assert s.count(old) == 1, old
    s = s.replace(old, new)
target.parent.mkdir(parents=True, exist_ok=True)
target.write_text(s, encoding="utf-8")
assert hashlib.sha256(target.read_bytes()).hexdigest() == "741676db7966c0255adf1415236afb4b6af19f45656f1b782f0fb70bc438d7f0"
print("R245F69 candidate SHA verified; production HTML unchanged")
