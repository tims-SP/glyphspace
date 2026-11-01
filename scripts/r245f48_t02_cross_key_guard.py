#!/usr/bin/env python3
"""R245F48 isolated T02 source-identity negative gate; never certifies glyphs."""
import json,sys
from pathlib import Path
SOURCE=Path(__file__).resolve().parent.parent/'docs/evidence/v036-r245f48-source-ROI-hashes.json'

def validate(data,proposals=()):
    assert data['round']=='R245F48'
    assert data['rootTaskIds']==['T01','T02']
    assert len(data['rows'])==9
    assert not any(data[k] for k in ('officialSameSourceProven','licenseVerified','sourceCertified','formalAccepted'))
    assert data['approvedPermanentIds']==0 and not data['K3IndependentOccurrenceConfirmed']
    byid={x['observation']:x for x in data['rows']}
    assert len(byid)==9 and len({tuple(x['cropXYXY']) for x in data['rows']})==9
    forbidden={frozenset(x) for x in data['crossKeyNoAutoAliasPairs']}
    assert len(forbidden)==8
    for row in data['rows']:
        assert len(row['nativeRGBSHA256'])==64
    assigned={}
    for p in proposals:
        if p.get('approved') or p.get('productionBindable'):
            raise ValueError('unverified proposal cannot be approved')
        obs=p['observations'];assert all(x in byid for x in obs)
        ref=p.get('referenceShapeId')
        if ref is not None:
            for a in obs:
                for b in assigned.get(ref,[]):
                    if frozenset((a,b)) in forbidden:raise ValueError('cross-proposal alias forbidden')
            for i,a in enumerate(obs):
                for b in obs[i+1:]:
                    if frozenset((a,b)) in forbidden:raise ValueError('same-proposal alias forbidden')
            assigned.setdefault(ref,[]).extend(obs)
    return True

if __name__=='__main__':
    data=json.loads(SOURCE.read_text());assert validate(data)
    try:validate(data,[{'observations':['M-vis-04'],'referenceShapeId':'INVALID'},{'observations':['legacy:L:6'],'referenceShapeId':'INVALID'}]);raise AssertionError('failed open')
    except ValueError:pass
    print('PASS R245F48 T02 cross-key source identity gate; not certified')
