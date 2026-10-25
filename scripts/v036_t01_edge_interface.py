#!/usr/bin/env python3
"""R117 source-only strict seam topology. Pixel connectivity != stroke ownership."""
from PIL import Image
from v036_t01_source_topology import M_BOXES,THRESHOLDS,PAIRS,scale_box,components,contains,edge_crossings,pair_connectivity

def seam(im,left,right,t):
    if left[2]!=right[0]: raise ValueError("nonadjacent seam")
    lo=max(left[1],right[1]);hi=min(left[3],right[3])
    g=im.convert("L");x=left[2]-1;y=right[0]
    pairs=[(a,b) for a in range(lo,hi) if g.getpixel((x,a))<t
           for b in range(max(lo,a-1),min(hi,a+2)) if g.getpixel((y,b))<t]
    return {"contacts":len(pairs),"distinctRows":len(set(a for a,b in pairs)|set(b for a,b in pairs))}

def shared(im,roi,a,b,t):
    return [(sum(contains(a,*p) for p in c),sum(contains(b,*p) for p in c))
            for c in components(im,roi,t)
            if any(contains(a,*p) for p in c) and any(contains(b,*p) for p in c)]

def edge(im,t):
    a=scale_box(M_BOXES["M-vis-02"],im.size)
    b=scale_box((1066,585,5,23),im.size)
    box=(min(a[0],b[0]),min(a[1],b[1]),max(a[2],b[2]),max(a[3],b[3]))
    strict=shared(im,box,a,b,t)
    broad=edge_crossings(im,t)
    count=sum(n for _,n in strict)
    return {"threshold":t,"strictConnectedExtensionInk":count,
            "contextConnectedExtensionInk":broad["extensionConnectedToOld"],
            "contextOnlyExtensionInk":broad["extensionConnectedToOld"]-count,
            "directSeam":seam(im,a,b,t),"approvedCrop":False}

def pair(im,n1,n2,t):
    a=scale_box(M_BOXES[n1],im.size);b=scale_box(M_BOXES[n2],im.size)
    l,r=sorted((a,b),key=lambda z:z[0])
    y0=max(l[1],r[1]);y1=min(l[3],r[3])
    s=shared(im,(l[0],y0,r[2],y1),a,b,t) if y1>y0 else []
    return {"pair":[n1,n2],"threshold":t,"gapPixels":r[0]-l[2],
            "contextSharedComponents":pair_connectivity(im,n1,n2,t)["componentIntersectsBoth"],
            "strictSharedComponents":len(s),
            "directSeam":seam(im,l,r,t) if l[2]==r[0] else None,
            "approvedIdentity":False}

def audit(im):
    return {"dimensions":list(im.size),"thresholds":list(THRESHOLDS),
            "edge":[edge(im,t) for t in THRESHOLDS],
            "pairs":[pair(im,a,b,t) for a,b in PAIRS for t in THRESHOLDS],
            "sourceCertified":False,"certifiedKeys":0,"approvedPermanentIDs":0,
            "approvedCrop":False,"confirmedMissingRootCount":None,
            "license":"not-established","registration":"proportional-only"}
