#!/usr/bin/env python3
"""R173 SHA-pinned highres overlap pixel diagnostics; no source redistribution or certification."""
import hashlib,io,json,urllib.parse,urllib.request,zipfile
from pathlib import Path
import cv2,numpy as np
from PIL import Image
DATA_SHA='1300d30b60f4d308dd7a8c17fcacf528a42f950f6122589e8c42fd2eb5f83310'
ZIP_SHA='fb7a9984a84be12a71d71dc86088b8859762ca97cb9a3db173b4a8adaf0b9707'
JPEG_SHA='47c5d53f6cf57ac67c957c6510a3e2696072c3ce63e73024ed025367f31c600e'
ZIP_NAME='第三代五笔字型（新世纪版）简体字根键位图高清版(官方).zip'
ENTRY='zgjwt_jt_3508x2480.jpg'
def sha(b):return hashlib.sha256(b).hexdigest()
def load_pairs(path):
    raw=Path(path).read_bytes()
    if sha(raw)!=DATA_SHA:raise ValueError('R172 coordinate SHA drift')
    d=json.loads(raw)
    if (d['sourceRound']!=172 or d['sourceHighresSHA256']!=JPEG_SHA or
        d['sourceReferenceSHA256']!='df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49' or
        d['license']!='unconfirmed' or len(d['pairs'])!=41):raise ValueError('source metadata drift')
    seen=set()
    for p in d['pairs']:
        if p['a']==p['b'] or p['k'] not in 'ABCDEFGH IJKLMNOPQRSTUVWX'.replace(' ',''):raise ValueError('invalid identity')
        for key in ('ra','rb'):
            x0,y0,x1,y1=p[key]
            if not (0<=x0<x1<=3508 and 0<=y0<y1<=2480):raise ValueError('invalid ROI')
        a,b=p['ra'],p['rb']
        if min(a[2],b[2])<=max(a[0],b[0]) or min(a[3],b[3])<=max(a[1],b[1]):raise ValueError('no overlap')
        pair=tuple(sorted((p['a'],p['b'])))
        if pair in seen:raise ValueError('duplicate pair')
        seen.add(pair)
    return d
def fetch_highres():
    url='https://raw.githubusercontent.com/06wb/06wb.github.io/master/Tutorials/'+urllib.parse.quote(ZIP_NAME)
    req=urllib.request.Request(url,headers={'User-Agent':'glyphspace-r173-source-only'})
    with urllib.request.urlopen(req,timeout=60) as r:blob=r.read(2000000)
    if len(blob)!=996823 or sha(blob)!=ZIP_SHA:raise ValueError('ZIP hash mismatch')
    with zipfile.ZipFile(io.BytesIO(blob)) as z:
        if z.namelist()!=[ENTRY]:raise ValueError('ZIP member drift')
        raw=z.read(ENTRY)
    if len(raw)!=1348865 or sha(raw)!=JPEG_SHA:raise ValueError('JPEG hash mismatch')
    with Image.open(io.BytesIO(raw)) as im:
        if im.size!=(3508,2480):raise ValueError('JPEG dimension drift')
        return np.asarray(im.convert('RGB')).copy()
def audit(rgb,data,thresholds=(100,160,210)):
    if rgb.shape!=(2480,3508,3) or rgb.dtype!=np.uint8:raise ValueError('image dimensions/dtype')
    if tuple(thresholds)!=(100,160,210):raise ValueError('threshold drift')
    rows=[]
    for p in data['pairs']:
        ax0,ay0,ax1,ay1=p['ra'];bx0,by0,bx1,by1=p['rb']
        x0=min(ax0,bx0);y0=min(ay0,by0);x1=max(ax1,bx1);y1=max(ay1,by1)
        gray=cv2.cvtColor(rgb[y0:y1,x0:x1],cv2.COLOR_RGB2GRAY)
        h,w=gray.shape
        am=np.zeros((h,w),dtype=bool);bm=am.copy()
        am[ay0-y0:ay1-y0,ax0-x0:ax1-x0]=True
        bm[by0-y0:by1-y0,bx0-x0:bx1-x0]=True
        overlap=am&bm;exact=bool(np.array_equal(am,bm))
        item={'key':p['k'],'a':p['a'],'b':p['b'],'introducedByMargin':p['new'],
              'exactSameEnvelope':exact,'overlapPixels':int(overlap.sum()),'thresholds':{}}
        for th in thresholds:
            ink=gray<th;ovink=ink&overlap
            bridge=touchA=touchB=0
            if ink.any() and not exact:
                n,lab,_,_=cv2.connectedComponentsWithStats(ink.astype(np.uint8),8)
                if n>1:
                    labels=np.arange(1,n)
                    ov=np.isin(labels,np.unique(lab[ovink]))
                    aa=np.isin(labels,np.unique(lab[ink&am&~bm]))
                    bb=np.isin(labels,np.unique(lab[ink&bm&~am]))
                    bridge=int(np.count_nonzero(ov&aa&bb))
                    touchA=int(np.count_nonzero(ov&aa))
                    touchB=int(np.count_nonzero(ov&bb))
            item['thresholds'][str(th)]={'overlapDarkPixels':int(ovink.sum()),
                'exclusiveADarkPixels':int((ink&am&~bm).sum()),
                'exclusiveBDarkPixels':int((ink&bm&~am).sum()),
                'bridgingComponents':bridge,'overlapComponentsTouchA':touchA,'overlapComponentsTouchB':touchB}
        rows.append(item)
    return {'round':173,'sourceJPEG_SHA256':JPEG_SHA,'sourceDimensions':[3508,2480],
            'sourceROI_SHA256':DATA_SHA,'pairs':rows,
            'summary':{'pairs':len(rows),'exactSameEnvelope':sum(x['exactSameEnvelope'] for x in rows),
              'introducedByMargin':sum(x['introducedByMargin'] for x in rows),
              'thresholds':{str(th):{'pairsWithDarkOverlap':sum(x['thresholds'][str(th)]['overlapDarkPixels']>0 for x in rows),
                'pairsWithBridgingComponents':sum(x['thresholds'][str(th)]['bridgingComponents']>0 for x in rows)} for th in thresholds}},
            'license':'unconfirmed','sourceCertifiedKeys':0,'approvedPermanentIDs':0,
            'trueMissingRootCount':None,'formalAccepted':False,'thirdPartyImageRepublished':False}
if __name__=='__main__':
    data=load_pairs(Path(__file__).with_name('v036_r173_41_overlap_rois.json'))
    result=audit(fetch_highres(),data)
    assert result['summary']['pairs']==41 and result['summary']['introducedByMargin']==20
    print('R173_SUMMARY='+json.dumps({k:v for k,v in result.items() if k!='pairs'},ensure_ascii=False,separators=(',',':')))
    for i,row in enumerate(result['pairs']):print('R173_PAIR='+json.dumps({'i':i,**row},ensure_ascii=False,separators=(',',':')))
