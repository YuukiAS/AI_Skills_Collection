#!/usr/bin/env python3
"""V6, derived from the V5 D2/ELK -> SVG pipeline; PNG uses Chromium.

Canonical labels and topology stay in the D2 source. ELK lays out the forward
flow; SVG post-processing implements the frozen role-card/connection spec.
Fonts, Playwright, browser profiles and diagnostics live only in .cache/.
"""
from __future__ import annotations
import asyncio,base64,heapq,io,json,math,os,re,subprocess,sys
from dataclasses import dataclass,field
from pathlib import Path
from lxml import etree as ET
from fontTools.ttLib import TTFont
from fontTools import subset

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
RES=ROOT/'.cache/assurance-diagram'
CACHE=RES/'v6'
NAME='ASSURANCE_PROCESS_V6_20261110'
NS='http://www.w3.org/2000/svg'
FONT='Noto Sans SC'
PALETTE={'high':('#3730A3','#FFFFFF'),'general':('#C7D2FE','#1E1B4B'),
 'exec_high':('#0F766E','#FFFFFF'),'exec_general':('#99F6E4','#134E4A'),
 'user':('#FCD34D','#78350F')}
STYLES={'normal':('#4B5563',2,''),'optional':('#4B5563',2,'6 4'),
 'back':('#DC2626',3,''),'proposal':('#EA580C',2,''),
 'revision':('#7C3AED',2.5,''),'evidence':('#9CA3AF',1.5,'2 4')}

@dataclass
class Node:
 key:str;label:str;kind:str;w:float;h:float;x:float=0;y:float=0
 @property
 def box(self):return (self.x,self.y,self.x+self.w,self.y+self.h)
 @property
 def cx(self):return self.x+self.w/2
 @property
 def cy(self):return self.y+self.h/2

@dataclass
class Edge:
 source:str;target:str;kind:str;label:str='';points:list=field(default_factory=list)


def parse():
 text=(HERE/f'{NAME}.d2').read_text();nodes={};edges=[]
 for line in text.splitlines():
  m=re.match(r'([\w.]+): ("(?:\\.|[^"\\])*") \{class: (\w+); width: ([\d.]+); height: ([\d.]+)',line)
  if m:
   key,label,kind,w,h=m.groups();nodes[key]=Node(key,json.loads(label),kind,float(w),float(h))
  m=re.match(r'([\w.]+) -> ([\w.]+):(?: ("(?:\\.|[^"\\])*"))? \{class: (\w+)\}',line)
  if m:
   a,b,label,kind=m.groups();edges.append(Edge(a,b,kind,json.loads(label) if label else ''))
 assert len(nodes)==28 and len(edges)==43,(len(nodes),len(edges))
 return text,nodes,edges


def layout(text,nodes):
 # Keep V5 placement exactly; only the four requested routing/tag edits change.
 text=(HERE/'ASSURANCE_PROCESS_V5_20261110.d2').read_text()
 lines=[l for l in text.splitlines() if not (' -> ' in l and any('class: '+k in l for k in ['back','proposal','revision','evidence']))]
 forward=CACHE/'forward-layout.d2';forward.write_text('\n'.join(lines)+'\n')
 raw=CACHE/'layout.svg';fonts=[]
 for kind,name in [('regular','Regular'),('bold','Semibold'),('semibold','Semibold'),('italic','Regular')]:
  fonts += ['--font-'+kind,str(RES/f'fonts/NotoSansSC-{name}.ttf')]
 subprocess.run([str(RES/'tools/d2-v0.9.0/bin/d2'),'--layout=elk','--scale','1','--pad','24',
                 '--elk-nodeNodeBetweenLayers','64','--elk-edgeNodeBetweenLayers','16',
                 *fonts,str(forward),str(raw)],check=True)
 r=ET.parse(str(raw)).getroot()
 def group(key):
  code=base64.b64encode(key.encode()).decode()
  return next(g for g in r.findall('.//{*}g') if code in g.get('class','').split())
 frames={}
 for key in ['design','delivery','design.gates']:
  a=group(key).find('.//{*}rect');frames[key]=[float(a.get(k)) for k in ['x','y','width','height']]
 for key,n in nodes.items():
  g=group(key);a=g.find('.//{*}rect')
  if a is not None:n.x,n.y,n.w,n.h=(float(a.get(k)) for k in ['x','y','width','height'])
  else:
   t=g.find('{*}text');n.x=float(t.get('x'))-n.w/2
   if n.kind=='decision':
    vals=list(map(float,re.findall(r'-?\d+(?:\.\d+)?',g.find('.//{*}path').get('d'))))
    n.x,n.y=min(vals[::2]),min(vals[1::2])
   else:
    d=g.find('.//{*}path').get('d');n.y=float(re.match(r'M\s+[-\d.]+\s+([-\d.]+)',d)[1])
 def reorder(keys):
  old=sorted(nodes[k].box for k in keys);lo=old[0][0];hi=max(b[2] for b in old)
  gap=(hi-lo-sum(nodes[k].w for k in keys))/(len(keys)-1);x=lo
  for key in keys:nodes[key].x=x;x+=nodes[key].w+gap
 reorder(['design.a','design.b','design.reality'])
 reorder(['design.gates.'+k for k in ['structure','questions','cold','retell']])
 # Keep ELK's columns, then align the shared-width role cards and routing buses.
 cx=frames['design'][2]/2
 for k in ['owner','grill','merge']:nodes['design.'+k].x=cx-nodes['design.'+k].w/2
 for keys in [['design.a','design.b','design.reality'],['design.gates.'+k for k in ['structure','questions','cold','retell']]]:
  lo=min(nodes[k].x for k in keys);hi=max(nodes[k].x+nodes[k].w for k in keys)
  for k in keys:nodes[k].x+=cx-(lo+hi)/2
 gate=frames['design.gates'];gate[1]=nodes['design.merge'].y+nodes['design.merge'].h+64
 for k,n in nodes.items():
  if k.startswith('design.gates.'):n.y=gate[1]+110
 gate[3]=234
 nodes['design.pass'].x=cx-nodes['design.pass'].w/2;nodes['design.pass'].y=gate[1]+gate[3]+80
 nodes['design.user'].x=24
 nodes['design.approve'].x=cx-nodes['design.approve'].w/2;nodes['design.approve'].y=nodes['design.pass'].y+nodes['design.pass'].h+64
 target_bottom=nodes['design.approve'].y+nodes['design.approve'].h
 delivery=frames['delivery'];delivery[0]=frames['design'][2]+450;delivery[2]=1260
 dc=delivery[0]+delivery[2]/2
 layers=[['owner'],['implement'],['validator'],['pass'],['professional','judge'],['sign'],['accept'],['done']]
 # More space above the parallel checks carries the positive-flow label and fork.
 heights=sum(max(nodes['delivery.'+k].h for k in ks) for ks in layers)
 gap=(target_bottom-56-50-heights-60)/7
 assert gap>=48,gap
 y=50
 for ks in layers:
  for k in ks:
   n=nodes['delivery.'+k];n.x=dc-n.w/2;n.y=y
   if k=='professional':n.x-=270
   if k=='judge':n.x+=270
  y+=max(nodes['delivery.'+k].h for k in ks)+gap+(60 if ks==['pass'] else 0)+(24 if ks==['sign'] else 0)
 doc=nodes['handoff.contract'];doc.x=frames['design'][2]+60;doc.y=(target_bottom-doc.h)/2
 for key in ['design','delivery']:frames[key][3]=target_bottom+24
 def point(k,x,y):n=nodes[k];n.x=x;n.y=y;n.w=n.h=0
 by=gate[1]+gate[3]+24
 point('design.gate_left',nodes['design.gates.questions'].cx,by)
 point('design.gate_right',nodes['design.gates.cold'].cx,by)
 point('design.gate_join',cx,by)
 point('delivery.check_join',dc,nodes['delivery.pass'].y-32)
 point('delivery.sign_split',dc,nodes['delivery.sign'].y+nodes['delivery.sign'].h+56)

 return frames


def inflate(b,m):return (b[0]-m,b[1]-m,b[2]+m,b[3]+m)

def overlap(a,b):return a[0]<b[2] and a[2]>b[0] and a[1]<b[3] and a[3]>b[1]

def seg_box(a,b,box,margin=0):
 box=inflate(box,margin)
 if abs(a[1]-b[1])<.01:return box[1]<a[1]<box[3] and max(a[0],b[0])>box[0] and min(a[0],b[0])<box[2]
 return box[0]<a[0]<box[2] and max(a[1],b[1])>box[1] and min(a[1],b[1])<box[3]

def segments(points):return list(zip(points,points[1:]))

def simplify(points):
 out=[]
 for p in points:
  if out and p==out[-1]:continue
  if len(out)>1 and ((out[-2][0]==out[-1][0]==p[0]) or (out[-2][1]==out[-1][1]==p[1])):out[-1]=p
  else:out.append(p)
 return out


def port(n,side,f=.5):
 if side=='top':
  y=n.y+(abs(f-.5)*n.h if n.kind=='decision' else 0)
  return (n.x+n.w*f,y),(n.x+n.w*f,n.y-16)
 if side=='bottom':
  y=n.y+n.h-(abs(f-.5)*n.h if n.kind=='decision' else 0)
  return (n.x+n.w*f,y),(n.x+n.w*f,n.y+n.h+16)
 if side=='left':return (n.x,n.y+n.h*f),(n.x-16,n.y+n.h*f)
 return (n.x+n.w,n.y+n.h*f),(n.x+n.w+16,n.y+n.h*f)


class Router:
 def __init__(self,boxes,bounds):self.boxes=[inflate(b,8) for b in boxes];self.bounds=bounds;self.used=[]
 def parallel(self,a,b):
  horizontal=abs(a[1]-b[1])<.001
  for c,d in self.used:
   if (abs(c[1]-d[1])<.001)!=horizontal:continue
   if horizontal:
    if abs(a[1]-c[1])<15.9 and min(max(a[0],b[0]),max(c[0],d[0]))-max(min(a[0],b[0]),min(c[0],d[0]))>.1:return True
   elif abs(a[0]-c[0])<15.9 and min(max(a[1],b[1]),max(c[1],d[1]))-max(min(a[1],b[1]),min(c[1],d[1]))>.1:return True
  return False
 def route(self,start,end):
  xmin,ymin,xmax,ymax=self.bounds
  xs={start[0],end[0],xmin,xmax};ys={start[1],end[1],ymin,ymax}
  xs.update(range(math.floor(xmin/16)*16,math.ceil(xmax/16)*16+1,16));ys.update(range(math.floor(ymin/16)*16,math.ceil(ymax/16)*16+1,16))
  for l,t,r,b in self.boxes:
   xs.update([l-8,r+8]);ys.update([t-8,b+8])
  for a,b in self.used:
   if a[0]==b[0]:xs.update([a[0]-16,a[0]+16])
   else:ys.update([a[1]-16,a[1]+16])
  xs=sorted(x for x in xs if xmin<=x<=xmax);ys=sorted(y for y in ys if ymin<=y<=ymax)
  si,sj=xs.index(start[0]),ys.index(start[1]);ti,tj=xs.index(end[0]),ys.index(end[1])
  origin=(si,sj,0);q=[(0,0,origin)];dist={origin:0};parent={};tested={}
  while q:
   _,cost,state=heapq.heappop(q)
   if cost!=dist.get(state):continue
   i,j,axis=state
   if (i,j)==(ti,tj):
    out=[]
    while state!=origin:out.append((xs[state[0]],ys[state[1]]));state=parent[state]
    return simplify([start]+list(reversed(out)))
   a=(xs[i],ys[j])
   for ni,nj,na in [(i-1,j,1),(i+1,j,1),(i,j-1,2),(i,j+1,2)]:
    if not(0<=ni<len(xs) and 0<=nj<len(ys)):continue
    b=(xs[ni],ys[nj]);key=tuple(sorted((a,b)))
    if key not in tested:tested[key]=not any(seg_box(a,b,box) for box in self.boxes) and not self.parallel(a,b)
    if not tested[key]:continue
    cross=sum(1 for c,d in self.used if ((a[1]==b[1] and c[0]==d[0] and min(a[0],b[0])<=c[0]<=max(a[0],b[0]) and min(c[1],d[1])<=a[1]<=max(c[1],d[1])) or (a[0]==b[0] and c[1]==d[1] and min(a[1],b[1])<=c[1]<=max(a[1],b[1]) and min(c[0],d[0])<=a[0]<=max(c[0],d[0]))))
    if cross:continue
    nc=cost+abs(a[0]-b[0])+abs(a[1]-b[1])+(18 if axis and axis!=na else 0)+cross*45
    nxt=(ni,nj,na)
    if nc<dist.get(nxt,float('inf')):
     dist[nxt]=nc;parent[nxt]=state;heapq.heappush(q,(nc+abs(b[0]-end[0])+abs(b[1]-end[1]),nc,nxt))
  raise RuntimeError(f'No compliant orthogonal route: {start} -> {end}')
 def add(self,points):self.used.extend(segments(points))


def rounded(points,radius=8):
 out=[f'M {points[0][0]:g} {points[0][1]:g}']
 for i in range(1,len(points)-1):
  a,p,b=points[i-1],points[i],points[i+1];r=min(radius,(abs(p[0]-a[0])+abs(p[1]-a[1]))/2,(abs(b[0]-p[0])+abs(b[1]-p[1]))/2)
  if not r:continue
  before=(p[0]+(a[0]-p[0])*r/(abs(a[0]-p[0])+abs(a[1]-p[1])),p[1]+(a[1]-p[1])*r/(abs(a[0]-p[0])+abs(a[1]-p[1])))
  after=(p[0]+(b[0]-p[0])*r/(abs(b[0]-p[0])+abs(b[1]-p[1])),p[1]+(b[1]-p[1])*r/(abs(b[0]-p[0])+abs(b[1]-p[1])))
  out += [f'L {before[0]:g} {before[1]:g}',f'Q {p[0]:g} {p[1]:g} {after[0]:g} {after[1]:g}']
 out.append(f'L {points[-1][0]:g} {points[-1][1]:g}');return ' '.join(out)

class Metrics:
 def __init__(self):
  self.fonts={w:TTFont(RES/f'fonts/NotoSansSC-{name}.ttf') for w,name in [(400,'Regular'),(600,'Semibold')]}
 def width(self,s,size,weight=400):
  f=self.fonts[weight];c=f.getBestCmap();h=f['hmtx'].metrics
  return sum(h[c.get(ord(a),'.notdef')][0] for a in s)*size/f['head'].unitsPerEm
 def wrap(self,s,size,width,weight=400):
  if self.width(s,size,weight)<=width:return [s]
  candidates=[i for i in range(1,len(s)) if self.width(s[:i],size,weight)<=width and self.width(s[i:],size,weight)<=width]
  if not candidates:raise RuntimeError(f'Cannot fit in two lines: {s}')
  preferred=[i for i in candidates if s[i-1] in '；，、 ']
  i=min(preferred or candidates,key=lambda i:abs(self.width(s[:i],size,weight)-self.width(s[i:],size,weight)))
  return [s[:i].strip(),s[i:].strip()]


def route_edges(nodes,edges,frames,m):
 doc=nodes['handoff.contract'];callout=(doc.cx-180,-230,doc.cx+180,-83)
 titleboxes=[(x+16,y+12,x+24+m.width('Design Assurance · 设计到冻结' if k=='design' else 'Delivery Assurance · 冻结到交付',20,600),y+40) for k,(x,y,w,h) in frames.items() if k in ['design','delivery']]
 x,y,w,h=frames['design.gates'];titleboxes.append((x+12,y+8,x+20+m.width('冻结关卡 · 四项都必跑',16,600),y+36))
 def get(k):return nodes[k if '.' in k else 'delivery.'+k]
 def put(a,b,kind,sa,ta,mid):
  a=a if '.' in a else 'delivery.'+a;b=b if '.' in b else 'delivery.'+b
  e=next(e for e in edges if e.source==a and e.target==b and e.kind==kind)
  p=port(nodes[a],*sa)[0];q=port(nodes[b],*ta)[0];e.points=simplify([p,*mid(p,q),q])
  for u,v in segments(e.points):
   assert u[0]==v[0] or u[1]==v[1],(a,b,u,v)
   for key,n in nodes.items():
    if key not in (a,b) and n.kind!='junction':assert not seg_box(u,v,n.box,3),(a,b,key,u,v)
   for box in titleboxes:assert not seg_box(u,v,box,2),(a,b,'title',u,v)
 def lane(x):return lambda p,q:[(x,p[1]),(x,q[1])]
 D=get('design.owner');I=get('implement');O=get('owner');P=get('professional');J=get('judge');Z=get('done');dc=I.cx;L=I.x;R=I.x+I.w
 put('owner','design.owner','back',('top',.95),('top',.8),lambda p,q:[(p[0],-64),(q[0],-64)])
 put('owner','design.owner','proposal',('top',.75),('right',.3),lambda p,q:[(p[0],-24),(D.x+D.w+32,-24),(D.x+D.w+32,q[1])])
 put('design.owner','handoff.contract','revision',('right',.8),('left',.2),lane(frames['design'][2]+16))
 put('design.owner','design.merge','back',('left',.55),('left',.2),lane(24))
 put('design.pass','design.merge','back',('left',.5),('left',.75),lane(24))
 put('design.approve','handoff.contract','normal',('right',.5),('left',.75),lane(frames['design'][2]+40))
 put('handoff.contract','owner','normal',('right',.65),('left',.3),lane(frames['delivery'][0]-24))
 put('owner','implement','normal',('bottom',.5),('top',.5),lambda p,q:[])
 put('implement','validator','optional',('bottom',.5),('top',.5),lambda p,q:[])
 put('validator','check_join','optional',('bottom',.5),('top',.5),lambda p,q:[])
 put('implement','check_join','normal',('bottom',.85),('right',.5),lambda p,q:[(p[0],p[1]+24),(R+24,p[1]+24),(R+24,q[1])])
 put('check_join','pass','normal',('bottom',.5),('top',.5),lambda p,q:[])
 put('validator','owner','proposal',('left',.2),('bottom',.2),lambda p,q:[(L-64,p[1]),(L-64,q[1]+24),(q[0],q[1]+24)])
 put('pass','implement','back',('right',.5),('right',.5),lane(R+56))
 for k in ['professional','judge']:
  put('pass',k,'optional',('bottom',.25 if k=='professional' else .75),('top',.5),lambda p,q:[(p[0],p[1]+40),(q[0],p[1]+40)])
 put('pass','sign','normal',('bottom',.5),('top',.5),lambda p,q:[])
 # X4 evidence now rises inside the left edge and enters X1's lower-left side.
 put('professional','owner','evidence',('left',.5),('left',.8),lane(frames['delivery'][0]+24))
 put('judge','owner','evidence',('right',.5),('right',.8),lane(J.x+J.w+48))
 put('sign','sign_split','normal',('bottom',.5),('top',.5),lambda p,q:[])
 put('sign_split','accept','optional',('bottom',.5),('top',.5),lambda p,q:[])
 put('sign_split','done','normal',('right',.5),('right',.5),lambda p,q:[(R+24,p[1]),(R+24,q[1])])
 put('accept','done','optional',('bottom',.5),('top',.5),lambda p,q:[])
 put('design.user','design.owner','normal',('bottom',.5),('top',.3),lambda p,q:[(p[0],p[1]+32),(q[0],p[1]+32)])
 put('design.owner','design.grill','normal',('bottom',.5),('top',.5),lambda p,q:[])
 for parent,keys,kinds,join in [
  ('design.grill',['design.a','design.b','design.reality'],['normal','optional','optional'],'design.merge'),
  ('design.merge',['design.gates.'+k for k in ['structure','questions','cold','retell']],['normal']*4,'design.gate_join')]:
  for i,(key,kind) in enumerate(zip(keys,kinds)):
   f=.2+.6*i/(len(keys)-1);outer=i in [0,len(keys)-1]
   yy=frames['design.gates'][1]+(56 if outer else 80) if parent=='design.merge' else get(parent).y+get(parent).h+(24 if outer else 48)
   put(parent,key,kind,('bottom',f),('top',.5),lambda p,q,yy=yy:[(p[0],yy),(q[0],yy)])
   if parent=='design.grill':
    yy=get(join).y-(24 if outer else 48)
    put(key,join,kind,('bottom',.5),('top',f),lambda p,q,yy=yy:[(p[0],yy),(q[0],yy)])
   else:
    target='design.gate_left' if i<2 else 'design.gate_right'
    put(key,target,kind,('bottom',.5),('left' if i<2 else 'right',.5),lambda p,q:[(p[0],q[1])])
 for k in ['left','right']:put('design.gate_'+k,'design.gate_join','normal',('right' if k=='left' else 'left',.5),('left' if k=='left' else 'right',.5),lambda p,q:[])
 put('design.gate_join','design.pass','normal',('bottom',.5),('top',.5),lambda p,q:[])
 put('design.pass','design.approve','normal',('bottom',.5),('top',.5),lambda p,q:[])
 assert all(e.points for e in edges)
 return callout,titleboxes


# V5 label coordinates retained except for the requested revision notice.
PINNED_LABELS=[{'text': '是', 'box': [743.5, 1294.0, 771.5, 1318.0], 'kind': 'normal', 'amber': False, 'edge': 'design.pass->design.approve'}, {'text': '是', 'box': [1153.75, 1342.0, 1181.75, 1366.0], 'kind': 'normal', 'amber': False, 'edge': 'design.approve->handoff.contract'}, {'text': '否：补缺口', 'box': [316.75, 1204.0, 392.75, 1228.0], 'kind': 'back', 'amber': False, 'edge': 'design.pass->design.merge'}, {'text': '大改：重新过关卡', 'box': [217.75, 235.0, 329.75, 259.0], 'kind': 'back', 'amber': False, 'edge': 'design.owner->design.merge'}, {'text': '动手前、完成后都告知用户', 'box': [18.92500000000001, 235.0, 178.925, 259.0], 'kind': 'back', 'amber': True, 'edge': 'design.owner->design.merge'}, {'text': '小修订：新版本，只重跑结构检查', 'box': [1115.25, 260.0, 1311.25, 284.0], 'kind': 'revision', 'amber': False, 'edge': 'design.owner->handoff.contract'}, {'text': '动手前、完成后都告知用户', 'box': [1299.0, 304, 1459, 328], 'kind': 'revision', 'amber': True, 'edge': 'design.owner->handoff.contract'}, {'text': '按条件', 'box': [2557.0, 347.71428571428567, 2609.0, 371.71428571428567], 'kind': 'optional', 'amber': False, 'edge': 'delivery.implement->delivery.validator'}, {'text': '只交证据', 'box': [3001.0, 471.2857142857143, 3065.0, 495.2857142857143], 'kind': 'evidence', 'amber': False, 'edge': 'delivery.judge->delivery.owner'}, {'text': '验收器提案', 'box': [2283.0, 331.6, 2359.0, 355.6], 'kind': 'proposal', 'amber': False, 'edge': 'delivery.validator->delivery.owner'}, {'text': '否，属实现问题：返修', 'box': [2823.0, 430.2857142857143, 2959.0, 454.2857142857143], 'kind': 'back', 'amber': False, 'edge': 'delivery.pass->delivery.implement'}, {'text': '验收器提案；D1 决定是否采纳', 'box': [985.5, 98.0, 1163.104, 122.0], 'kind': 'proposal', 'amber': False, 'edge': 'delivery.owner->design.owner'}, {'text': '是', 'box': [2557.0, 1047.7142857142858, 2585.0, 1071.7142857142858], 'kind': 'normal', 'amber': False, 'edge': 'delivery.sign->delivery.sign_split'}]

def chips(nodes,edges,callout,titleboxes,m):
 out=[dict(c) for c in PINNED_LABELS];allsegs=[(a,b,STYLES[e.kind][1]) for e in edges for a,b in segments(e.points)]
 obstacles=[inflate(n.box,8) for n in nodes.values()]+[inflate(callout,8)]+[inflate(b,8) for b in titleboxes]
 def distance(a,b,box):
  if a[1]==b[1]:
   dx=max(box[0]-max(a[0],b[0]),min(a[0],b[0])-box[2],0);dy=max(box[1]-a[1],a[1]-box[3],0)
  else:dx=max(box[0]-a[0],a[0]-box[2],0);dy=max(box[1]-max(a[1],b[1]),min(a[1],b[1])-box[3],0)
  return math.hypot(dx,dy)
 def place(e,text,amber=False):
  w=m.width(text,12)+16;h=24
  ss=sorted(segments(e.points),key=lambda z:-(abs(z[0][0]-z[1][0])+abs(z[0][1]-z[1][1])))
  for extra in ([0] if len(text)<=10 else [0,8,16,28,44,64]):
   for a,b in ss:
    horizontal=a[1]==b[1]
    for frac in [.5,.3,.7,.15,.85]:
     cx=a[0]+(b[0]-a[0])*frac;cy=a[1]+(b[1]-a[1])*frac
     for side in ([-1] if horizontal or (e.kind=='evidence' and e.source!='delivery.professional') else [1]):
      x=cx-w/2+(0 if horizontal else side*(w/2+10+extra));y=cy-h/2+(side*(h/2+10+extra) if horizontal else 0)
      box=(x,y,x+w,y+h)
      if y< -210 or y+h>max(n.y+n.h for n in nodes.values())+24:continue
      if any(overlap(box,o) for o in obstacles):continue
      if any(overlap(inflate(box,8),c['box']) for c in out):continue
      if any(distance(a,b,box)<8+lw/2-.01 for a,b,lw in allsegs):continue
      out.append({'text':text,'box':box,'kind':e.kind,'amber':amber,'edge':f'{e.source}->{e.target}'});return
  raise RuntimeError(f'No label position: {text}')
 for e in sorted(edges,key=lambda e:0 if e.source=='delivery.pass' and e.target=='delivery.sign' else 1):
  if any(c['edge']==e.source+'->'+e.target and not c['amber'] for c in out):continue
  if e.label and not (e.kind=='back' and e.source=='delivery.owner' and e.target=='design.owner'):place(e,e.label)
  if e.source=='design.owner' and e.kind in ['back','revision'] and not any(c['edge']==e.source+'->'+e.target and c['amber'] for c in out):place(e,'动手前、完成后都告知用户',True)
 return out


def draw(nodes,edges,frames,callout,labels,m):
 root=ET.Element('svg',nsmap={None:NS});defs=ET.SubElement(root,'defs')
 def elem(tag,parent=root,**kw):return ET.SubElement(parent,tag,**{k.replace('_','-'):str(v) for k,v in kw.items()})
 def text(s,x,y,size=13,weight=400,color='#374151',anchor='middle',parent=root,**kw):
  e=elem('text',parent,x=x,y=y,font_size=size,font_weight=weight,fill=color,text_anchor=anchor,dominant_baseline='central',**kw);e.text=s;return e
 def multiline(lines,x,y,lh=20,**kw):
  for i,s in enumerate(lines):text(s,x,y+(i-(len(lines)-1)/2)*lh,**kw)
 for key in ['design','delivery']:
  x,y,w,h=frames[key];elem('rect',x=x,y=y,width=w,height=h,rx=16,fill='#F5F7FF' if key=='design' else '#F0FDFA',stroke='#D1D5DB',stroke_width=1)
  text('Design Assurance · 设计到冻结' if key=='design' else 'Delivery Assurance · 冻结到交付',x+16,y+26,size=20,weight=600,anchor='start',data_part='container-title')
 x,y,w,h=frames['design.gates'];elem('rect',x=x,y=y,width=w,height=h,rx=10,fill='#F9FAFB',stroke='#D1D5DB',stroke_width=1,stroke_dasharray='6 4')
 text('冻结关卡 · 四项都必跑',x+12,y+22,size=16,weight=600,anchor='start',data_part='gate-title')
 for kind,(color,width,dash) in STYLES.items():
  length=width*4+4;half=width*1.5+2
  mark=elem('marker',defs,id='arrow-'+kind,markerWidth=length,markerHeight=half*2,refX=length,refY=half,orient='auto',markerUnits='userSpaceOnUse')
  elem('path',mark,d=f'M 0 0 L {length:g} {half:g} L 0 {half*2:g} Z',fill=color)
 for e in edges:
  color,width,dash=STYLES[e.kind];kw={'stroke_dasharray':dash} if dash else {}
  elem('path',d=rounded(e.points),fill='none',stroke=color,stroke_width=width,**({'marker_end':f'url(#arrow-{e.kind})'} if nodes[e.target].kind!='junction' else {}),data_edge=f'{e.source}->{e.target}',data_kind=e.kind,**kw)
 optional={'design.b','design.reality','delivery.validator','delivery.professional','delivery.judge','delivery.accept'}
 for key,n in nodes.items():
  group=elem('g',data_node=key,data_kind=n.kind)
  if n.kind in PALETTE:
   color,ink=PALETTE[n.kind];header,body=n.label.split('\n',1)
   clip=elem('clipPath',defs,id='clip-'+key.replace('.','-'));elem('rect',clip,x=n.x,y=n.y,width=n.w,height=n.h,rx=10)
   inside=elem('g',group,clip_path='url(#clip-'+key.replace('.','-')+')')
   elem('rect',inside,x=n.x,y=n.y,width=n.w,height=n.h,fill='#FFFFFF')
   elem('rect',inside,x=n.x,y=n.y,width=n.w,height=48,fill=color)
   elem('line',group,x1=n.x,y1=n.y+48,x2=n.x+n.w,y2=n.y+48,stroke='#D1D5DB',stroke_width=1)
   elem('rect',group,x=n.x,y=n.y,width=n.w,height=n.h,rx=10,fill='none',stroke='#D1D5DB',stroke_width=1.5 if key in optional else 1,**({'stroke_dasharray':'6 4'} if key in optional else {}))
   multiline(m.wrap(header,16,n.w-24,600),n.cx,n.y+24,lh=20,size=16,weight=600,color=ink,parent=group,data_part='header')
   multiline(body.split('\n') if '\n' in body else m.wrap(body,13,n.w-24),n.cx,n.y+74,lh=19,size=13,weight=400,parent=group,data_part='body')
  elif n.kind=='decision':
   elem('path',group,d=f'M {n.cx:g} {n.y:g} L {n.x+n.w:g} {n.cy:g} L {n.cx:g} {n.y+n.h:g} L {n.x:g} {n.cy:g} Z',fill='#FFFFFF',stroke='#D1D5DB',stroke_width=1)
   text(n.label,n.cx,n.cy,size=16,weight=600,parent=group)
  elif n.kind=='artifact':
   f=20;elem('path',group,d=f'M {n.x:g} {n.y:g} H {n.x+n.w-f:g} L {n.x+n.w:g} {n.y+f:g} V {n.y+n.h:g} H {n.x:g} Z M {n.x+n.w-f:g} {n.y:g} V {n.y+f:g} H {n.x+n.w:g}',fill='#FFFFFF',stroke='#D1D5DB',stroke_width=1)
   lines=n.label.split('\n');text(lines[0],n.cx,n.y+(28 if len(lines)>1 else n.h/2),size=16,weight=600,parent=group)
   for i,s in enumerate(lines[1:]):
    assert m.width(s,13)<n.w-24,(s,n.w)
    text(s,n.x+16,n.y+65+i*26,anchor='start',parent=group)
 for c in labels:
  x,y,r,b=c['box'];group=elem('g',data_label=c['text']);elem('rect',group,x=x,y=y,width=r-x,height=b-y,rx=6,fill='#FEF3C7' if c['amber'] else '#FFFFFF')
  text(c['text'],(x+r)/2,(y+b)/2,size=12,color='#92400E' if c['amber'] else STYLES[c['kind']][0],parent=group)
 l,t,r,b=callout;elem('rect',x=l,y=t,width=r-l,height=b-t,rx=6,fill='#FFFFFF',stroke='#DC2626',stroke_width=1)
 text('退回请求',l+14,t+20,size=14,weight=600,color='#991B1B',anchor='start')
 for i,s in enumerate(['合同矛盾或缺决定','新事实推翻设计','必需验收方法做不到，且无等价方法','需要改变完成标准','需要只有用户能做的决定']):text('• '+s,l+14,t+46+i*21,size=13,weight=400,color='#991B1B',anchor='start')
 elem('path',d=f'M {(l+r)/2:g} {b:g} V -64',stroke='#DC2626',stroke_width=3,fill='none')
 left=min(-100,min(c['box'][0] for c in labels)-16);right=max(frames['delivery'][0]+frames['delivery'][2]+112,max(c['box'][2] for c in labels)+16)
 ly=max(v[1]+v[3] for k,v in frames.items() if k in ['design','delivery'])+32
 cell=(right-left)/10
 models=['Claude / GPT Pro','GPT 极高','GPT Work 极高','Codex 高','']
 names=['规划端·专业','规划端·普通','执行端·专业','执行端·普通','用户']
 for i,((key,(color,ink)),name,model) in enumerate(zip(PALETTE.items(),names,models)):
  x=left+cell*i+8;elem('rect',x=x,y=ly,width=cell-16,height=30,rx=6,fill=color)
  text(name,x+(cell-16)/2,ly+15,size=13,weight=600,color=ink)
  if model:text(model,x+(cell-16)/2,ly+47,size=12)
 cell=(right-left)/12
 meanings=['正常流程（必跑）','正常流程（可选）','退回或补缺口','验收器提案（建议权）','修订后的新版本','交回证据，不转移负责权']
 for i,((kind,(color,width,dash)),meaning) in enumerate(zip(STYLES.items(),meanings)):
  x=left+(right-left)/2+cell*i+8;elem('path',d=f'M {x:g} {ly+15:g} H {x+cell-30:g}',fill='none',stroke=color,stroke_width=width,marker_end=f'url(#arrow-{kind})',**({'stroke_dasharray':dash} if dash else {}))
  text(meaning,x+(cell-16)/2,ly+47,size=12,color=color)
 ymin=t-16;ymax=ly+72;W=math.ceil(right-left);H=math.ceil(ymax-ymin)
 root.set('viewBox',f'{left:g} {ymin:g} {W} {H}');root.set('width',str(W));root.set('height',str(H));root.set('style','background:white')
 chars=''.join(e.text or '' for e in root.findall('.//text'))
 css=[]
 for weight,font in m.fonts.items():
  missing=set(map(ord,chars))-set(font.getBestCmap());assert not missing,missing
  f=TTFont(RES/f'fonts/NotoSansSC-{"Regular" if weight==400 else "Semibold"}.ttf');o=subset.Options();o.flavor='woff';sub=subset.Subsetter(options=o);sub.populate(text=chars);sub.subset(f);f.flavor='woff';buf=io.BytesIO();f.save(buf)
  css.append('@font-face{font-family:"Noto Sans SC";font-style:normal;font-weight:'+str(weight)+';src:url(data:font/woff;base64,'+base64.b64encode(buf.getvalue()).decode()+') format("woff");}')
 style=elem('style',defs);style.text=''.join(css)+'text{font-family:"Noto Sans SC";font-synthesis:none;}'
 path=HERE/f'{NAME}.svg';ET.ElementTree(root).write(str(path),encoding='utf-8',xml_declaration=True)
 return W,H


async def screenshot(W,H):
 sys.path.insert(0,str(RES/'v3/python'))
 from playwright.async_api import async_playwright
 env=dict(os.environ);env.update({'XDG_CACHE_HOME':str(CACHE/'chromium-cache'),'XDG_CONFIG_HOME':str(CACHE/'chromium-config')})
 async with async_playwright() as p:
  context=await p.chromium.launch_persistent_context(str(CACHE/'chromium-profile'),executable_path='/usr/bin/chromium-browser',headless=True,viewport={'width':W,'height':H},device_scale_factor=2,env=env,args=['--no-sandbox','--disable-dev-shm-usage','--disable-gpu','--disk-cache-dir='+str(CACHE/'chromium-disk-cache')])
  page=await context.new_page();await page.goto((HERE/f'{NAME}.svg').as_uri());await page.evaluate('document.fonts.ready')
  result=await page.evaluate('''() => ({regular:document.fonts.check('400 13px "Noto Sans SC"'),semibold:document.fonts.check('600 16px "Noto Sans SC"'),width:innerWidth,height:innerHeight,dpr:devicePixelRatio})''')
  assert result['regular'] and result['semibold'],result
  await page.screenshot(path=str(HERE/f'{NAME}.png'),full_page=False,timeout=30000)
  result['browser']=context.browser.version if context.browser else 'Chromium persistent context';result['renderer']='Chromium / Playwright';await context.close();return result


def main():
 CACHE.mkdir(parents=True,exist_ok=True);text,nodes,edges=parse();frames=layout(text,nodes);m=Metrics()
 callout,titleboxes=route_edges(nodes,edges,frames,m);labels=chips(nodes,edges,callout,titleboxes,m);W,H=draw(nodes,edges,frames,callout,labels,m)
 evidence={'browser':None,'size':[W,H],'frames':frames,'callout':callout,'nodes':{k:{'box':n.box,'label':n.label,'kind':n.kind} for k,n in nodes.items()},'edges':[{'source':e.source,'target':e.target,'kind':e.kind,'points':e.points} for e in edges],'labels':labels}
 (CACHE/'render-evidence.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
 browser=asyncio.run(screenshot(W,H));evidence['browser']=browser
 (CACHE/'render-evidence.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n');print('Rendered',W,H,browser,flush=True)

if __name__=='__main__':main()
