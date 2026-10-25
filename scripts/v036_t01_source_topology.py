#!/usr/bin/env python3
"""R116 source-only ink connectivity. Descriptive evidence, never certification."""
from collections import deque
import hashlib
from PIL import Image
OLD_SIZE=(1536,1086)
M_BOXES={'M-vis-01':(992,585,24,24),'M-vis-02':(1045,585,21,23),
'M-vis-03':(993,615,21,25),'M-vis-04':(1017,623,14,13),
'M-vis-05':(993,645,18,22),'M-vis-06':(1012,652,12,15),
'M-vis-07':(1027,653,12,14),'M-vis-08':(1040,653,12,15)}
THRESHOLDS=(96,128,144,160,176)
PAIRS=(('M-vis-03','M-vis-04'),('M-vis-05','M-vis-06'),('M-vis-07','M-vis-08'))
def scale_box(box,dims):
 x,y,w,h=box;sx,sy=dims[0]/OLD_SIZE[0],dims[1]/OLD_SIZE[1]
 a,b,c,d=round(x*sx),round(y*sy),round((x+w)*sx),round((y+h)*sy)
 if not (0<=a<c<=dims[0] and 0<=b<d<=dims[1]):raise ValueError('ROI outside source')
 return (a,b,c,d)
def contains(box,x,y):
 return box[0]<=x<box[2] and box[1]<=y<box[3]
def components(im,roi,threshold):
 x0,y0,x1,y1=roi
 if not(0<=x0<x1<=im.width and 0<=y0<y1<=im.height):raise ValueError('bad ROI')
 gray=im.crop(roi).convert('L');w,h=gray.size;data=gray.tobytes();seen=bytearray(w*h);out=[]
 for i in range(w*h):
  if seen[i] or data[i]>=threshold:continue
  seen[i]=1;queue=deque([i]);coords=[]
  while queue:
   q=queue.popleft();yy,xx=divmod(q,w);coords.append((xx+x0,yy+y0))
   for dy in (-1,0,1):
    ny=yy+dy
    if ny<0 or ny>=h:continue
    for dx in (-1,0,1):
     nx=xx+dx
     if (dx==0 and dy==0) or nx<0 or nx>=w:continue
     ni=ny*w+nx
     if not seen[ni] and data[ni]<threshold:
      seen[ni]=1;queue.append(ni)
  out.append(coords)
 return out
def edge_crossings(im,threshold=160):
 dims=im.size;old=scale_box(M_BOXES['M-vis-02'],dims);extension=scale_box((1066,585,5,23),dims)
 margin=round(4*dims[0]/OLD_SIZE[0]);ym=round(4*dims[1]/OLD_SIZE[1])
 roi=(old[0]-margin,old[1]-ym,extension[2]+margin,old[3]+ym)
 crossing=0;connected_ink=0;unconnected_ink=0;total_extension=0
 for comp in components(im,roi,threshold):
  orig=any(contains(old,*pt) for pt in comp);ext=sum(contains(extension,*pt) for pt in comp)
  total_extension+=ext
  if ext:
   if orig:crossing+=1;connected_ink+=ext
   else:unconnected_ink+=ext
 return {'threshold':threshold,'oldROI':list(old),'extensionROI':list(extension),
 'extensionInk':total_extension,'extensionConnectedToOld':connected_ink,
 'extensionUnconnected':unconnected_ink,'crossingComponents':crossing}
def pair_connectivity(im,a,b,threshold):
 ra=scale_box(M_BOXES[a],im.size);rb=scale_box(M_BOXES[b],im.size)
 margin=max(1,round(3*im.width/OLD_SIZE[0]))
 roi=(max(0,min(ra[0],rb[0])-margin),max(0,min(ra[1],rb[1])-margin),
 min(im.width,max(ra[2],rb[2])+margin),min(im.height,max(ra[3],rb[3])+margin))
 shared=0;total_a=0;total_b=0
 for comp in components(im,roi,threshold):
  ca=sum(contains(ra,*p) for p in comp);cb=sum(contains(rb,*p) for p in comp)
  total_a+=ca;total_b+=cb
  if ca and cb:shared+=1
 return {'pair':[a,b],'threshold':threshold,'componentIntersectsBoth':shared,
 'darkInA':total_a,'darkInB':total_b,
 'rectanglesOverlap':not (ra[2]<=rb[0] or rb[2]<=ra[0] or ra[3]<=rb[1] or rb[3]<=ra[1])}
def audit(im):
 return {'dimensions':list(im.size),'sourceRGBSHA256':hashlib.sha256(im.convert('RGB').tobytes()).hexdigest(),
 'thresholds':list(THRESHOLDS),'edge':[edge_crossings(im,t) for t in THRESHOLDS],
 'pairs':[pair_connectivity(im,a,b,t) for a,b in PAIRS for t in THRESHOLDS],
 'sourceCertified':False,'approvedCrop':False,'approvedPermanentIDs':0,
 'copyrightCleared':False,'confirmedMissingRootCount':None}
