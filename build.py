from PIL import Image,ImageDraw,ImageFont
import os,hashlib
S=4; W=1024; BG=(245,240,230); INK=(25,28,31); RED=(164,55,42); MUTED=(91,88,80)
root=os.path.dirname(__file__); serif='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'; sans='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; sansb='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def F(n,b=0,ser=0): return ImageFont.truetype(serif if ser else (sansb if b else sans),n*S)
im=Image.new('RGB',(W*S,W*S),BG); d=ImageDraw.Draw(im)
def t(x,y,s,n=11,c=INK,b=0,ser=0,anchor=None): d.text((x*S,y*S),s,font=F(n,b,ser),fill=c,anchor=anchor)
def p(x,y,s,n=10,m=55,lead=13,c=INK,b=0):
 line=''; yy=y
 last=None
 for w in s.split():
  if len(line)+len(w)+1>m: t(x,yy,line,n,c,b); yy+=lead; line=w
  else: line=(line+' '+w).strip()
 if line:t(x,yy,line,n,c,b); last=yy
 return last
def audit_text_overflow(last_baseline,font_size,panel_bottom):
 # PIL's rendered glyphs occupy the baseline row through baseline + font height.
 assert last_baseline + font_size <= panel_bottom, f'text overflow: {last_baseline}+{font_size}>{panel_bottom}'
def B(r,fill=(248,245,237),out=INK): x,y,w,h=r; d.rectangle((x*S,y*S,(x+w)*S,(y+h)*S),fill=fill,outline=out,width=S)
# One row per distinct source story. Preliminary Myanmar (line 10) and summit
# (line 9) reports are covered by their completed outcomes (lines 17 and 29).
# Source citations refer to story-list-42.md, not to the printed story numbers.
REGISTRY=[
 ('Shenzhen peace declaration', 29, 'Shenzhen'), # story-list-42.md:29
 ('Myanmar ICJ genocide ruling', 17, 'Myanmar'), # story-list-42.md:17
 ('Gaza operation', 23, 'Gaza'), # story-list-42.md:23
 ('Iran dirty-bomb denial', 21, 'Iran'), # story-list-42.md:21
 ('Crimean Bridge attack', 24, 'Russia'), # story-list-42.md:24
 ('Yongbyon enrichment', 27, 'Korea'), # story-list-42.md:27
 ('Japan–Russia talks', 26, 'Japan'), # story-list-42.md:26
 ('Iran fires on Kuwait', 20, 'Kuwait'), # story-list-42.md:20
 ('Riyadh PIF Tower attack', 22, 'Riyadh'), # story-list-42.md:22
 ('PNG Rio Tinto fund', 34, 'PNG'), # story-list-42.md:34
 ('Fiji drought disaster', 42, 'Fiji'), # story-list-42.md:42
 ('Haiti plot conviction', 49, 'Haiti'), # story-list-42.md:49
 ('Begich Alaska seat', 38, 'US'), # story-list-42.md:38
 ('GTA VI Metacritic 99', 6, None), # story-list-42.md:6
 ('UN/ICC reform', 30, None), # story-list-42.md:30
 ('Take-Two shares', 7, None), # story-list-42.md:7
 ('Iran dirty-bomb threat', 19, None), # story-list-42.md:19
 ('APEC Outlook', 31, None), # story-list-42.md:31
 ('Greenland deal', 32, None), # story-list-42.md:32
 ('COP31', 33, None), # story-list-42.md:33
 ('Gas Husky sinking', 36, None), # story-list-42.md:36
 ('Markets Nikkei', 13, None), # story-list-42.md:13
 ('Markets BTC / WTI', 14, None), # story-list-42.md:14
 ('Cyclone Akvan', 12, None), # story-list-42.md:12
 ('Putin response', 25, None), # story-list-42.md:25
 ('South Korea dialogue', 28, None), # story-list-42.md:28
 ('Gaza aid plan', 39, None), # story-list-42.md:39
 ('Indonesia asset bill', 40, None), # story-list-42.md:40
 ('Serbia speaker', 45, None), # story-list-42.md:45
 ('Venezuelan TPS', 37, None), # story-list-42.md:37
 ('Malaysia UNHCR', 43, None), # story-list-42.md:43
 ('US–Philippines loan', 44, None), # story-list-42.md:44
 ('Saudi weather', 46, None), # story-list-42.md:46
 ('Nassau storm alert', 47, None), # story-list-42.md:47
 ('Voyager 1', 11, None), # story-list-42.md:11
 ('Save the Children', 41, None), # story-list-42.md:41
 ('Bangladesh shutdown', 35, None), # story-list-42.md:35
 ('Iran war after Jan 1 2027', 18, None), # story-list-42.md:18
 ('Anthropic IPO', 8, None), # story-list-42.md:8
 ('Prince Harry', 48, None), # story-list-42.md:48
 ]
STORIES=[r[0] for r in REGISTRY]
N=len(STORIES)
STORY_NUM={name:f'{i+1:02d}' for i,name in enumerate(STORIES)}
assert 28 <= N <= 42 and len(set(STORIES)) == N
assert len({r[1] for r in REGISTRY}) == N, 'duplicate source story'
assert all(6 <= r[1] <= 49 for r in REGISTRY)
# When available, validate citations against the authority itself; no external
# file is required to reproduce the standalone repository image.
source_path=os.path.join(root,'..','..','story-list-42.md')
if os.path.exists(source_path):
 import re
 source_lines=open(source_path).read().splitlines()
 assert all(re.match(r'^\d+\. ',source_lines[line-1]) for _,line,_ in REGISTRY)
 assert {r[1] for r in REGISTRY} == (set(range(6,15)) | set(range(17,50))) - {9,10}

DISPLAYED=[]
def numbered(section,names,text):
 # Check the actual string handed to the drawing routine against its story IDs.
 import re
 expected=[STORY_NUM[name] for name in names]
 actual=re.findall(r'(?<![\w])\d{2}(?!\d)',text.split(' | ')[0])
 assert actual == expected, (section,names,text,expected)
 DISPLAYED.append((section,tuple(names),tuple(actual)))
 return text.replace(' | ',' ')
def num(*names): return ' · '.join(STORY_NUM[n] for n in names)
def heading(section,names,label):
 return numbered(section,names,num(*names)+' · | '+label)
rects=[(24,22,976,84),(24,120,976,42),(24,174,312,139),(356,174,312,139),(688,174,312,139),(24,328,640,190),(680,328,320,190)]+[(24+(i%4)*245,536+(i//4)*53,235,48) for i in range(12)]+[(24,696,976,122),(24,830,310,108),(350,830,650,108)]
for i,a in enumerate(rects):
 for b in rects[i+1:]:
  if a[0]<b[0]+b[2] and b[0]<a[0]+a[2] and a[1]<b[1]+b[3] and b[1]<a[1]+a[3]: raise RuntimeError(f'layout overlap {a} {b}')
t(24,25,'THE WORLD IN ONE DAY',12,RED,1); t(24,42,'Thursday 19 November 2026',62,INK,1,1); t(998,32,'FREY / DAILY BRIEF',10,MUTED,1,anchor='ra'); d.line((24*S,106*S,1000*S,106*S),fill=INK,width=2*S)
for i,(a,b) in enumerate([(str(N),'stories'),('6','regions'),('+0.36%','Nikkei'),('$63k','BTC'),('$82','WTI'),('+7.5%','Take-Two')]):
 x=24+i*162; B((x,120,150,42),(239,232,216),(173,165,150)); t(x+7,126,a,17,RED,1); t(x+7,148,b,9,MUTED,1)
heroes=[('DIPLOMACY','Trump · Xi · Putin','90-minute Shenzhen peace declaration; UN, ICC reform, nuclear counterproliferation.',(38,87,119)),('JUSTICE','ICJ: Myanmar liable','Myanmar genocide ruling, 9–6; restitution and investigations ordered.',RED),('GTA VI','Metacritic 99','GTA VI scores 99; Take-Two rises 7.5% on the cultural market story.',(205,151,49))]
for i,(k,h,s,col) in enumerate(heroes):
 x=24+i*332; B((x,174,312,139)); d.rectangle((x*S,174*S,(x+312)*S,232*S),fill=col)
 # Recognisable geometric scenes, kept entirely inside the illustration band.
 if i==0: # diplomacy: skyline, lit windows, and three flag bands
  d.rectangle(((x+28)*S,205*S,(x+284)*S,232*S),fill=(25,42,52))
  for bx,bh in [(42,18),(72,28),(105,22),(145,34),(185,24),(224,30),(258,20)]:
   d.rectangle(((x+bx)*S,(232-bh)*S,(x+bx+22)*S,232*S),fill=(18,31,39))
   for wy in range(210,229,8): d.rectangle(((x+bx+5)*S,wy*S,(x+bx+9)*S,(wy+3)*S),fill=(244,197,83))
  for j,fc in enumerate([(210,58,55),(244,197,83),(235,235,220)]): d.rectangle(((x+30)*S,(181+j*6)*S,(x+282)*S,(186+j*6)*S),fill=fc)
 elif i==1: # justice: courthouse columns and scales
  d.polygon([(x+48,196),(x+156,180),(x+264,196)],fill=(246,226,183))
  d.rectangle(((x+48)*S,196*S,(x+264)*S,201*S),fill=(246,226,183))
  for cx in [65,98,131,164,197,230]: d.rectangle(((x+cx)*S,201*S,(x+cx+13)*S,229*S),fill=(246,226,183))
  d.rectangle(((x+45)*S,229*S,(x+267)*S,232*S),fill=(246,226,183)); d.line(((x+156)*S,198*S,(x+156)*S,226*S),fill=INK,width=2*S)
  d.line(((x+130)*S,205*S,(x+182)*S,205*S),fill=INK,width=2*S); d.line(((x+130)*S,205*S,(x+124)*S,217*S),fill=INK,width=2*S); d.line(((x+182)*S,205*S,(x+188)*S,217*S),fill=INK,width=2*S)
  d.ellipse(((x+115)*S,215*S,(x+137)*S,221*S),fill=(246,226,183)); d.ellipse(((x+175)*S,215*S,(x+197)*S,221*S),fill=(246,226,183))
 else: # GTA VI: neon sunset, skyline, and palms
  d.rectangle(((x+20)*S,180*S,(x+292)*S,204*S),fill=(245,115,78)); d.ellipse(((x+125)*S,185*S,(x+187)*S,232*S),fill=(255,208,93))
  d.polygon([(x+20,223),(x+55,210),(x+80,222),(x+112,202),(x+145,222),(x+180,207),(x+214,222),(x+246,198),(x+292,220),(x+292,232),(x+20,232)],fill=(47,34,67))
  for px in [48,78,108,140,175,210,245]: d.rectangle(((x+px)*S,224*S,(x+px+12)*S,232*S),fill=(28,22,45))
  for px in [35,268]:
   d.rectangle(((x+px)*S,198*S,(x+px+4)*S,232*S),fill=(28,50,45)); d.ellipse(((x+px-16)*S,190*S,(x+px+18)*S,204*S),fill=(28,50,45)); d.ellipse(((x+px-12)*S,185*S,(x+px+24)*S,200*S),fill=(28,50,45))
 t(x+10,238,heading('hero', [('Shenzhen peace declaration','UN/ICC reform'),('Myanmar ICJ genocide ruling',),('GTA VI Metacritic 99','Take-Two shares')][i],k),10,(80,75,65),1); t(x+10,251,h,22,INK,1); last=p(x+10,278,s,11,42,13,INK,1); audit_text_overflow(last,11,313)
B((24,328,640,190),(239,235,225)); t(36,340,'THE DAY, IN SEQUENCE',12,RED,1)
timeline=[
 ('OVERNIGHT',('Myanmar ICJ genocide ruling','Gaza operation','Iran dirty-bomb denial','Iran dirty-bomb threat'),'{0} ICJ rules Myanmar genocide; {1} Gaza; {2} / {3} Iran updates.'),
 ('MORNING',('APEC Outlook','Greenland deal'),'{0} APEC adopts Shenzhen Outlook; {1} Greenland deal passes 109–0.'),
 ('MIDDAY',('Shenzhen peace declaration','Japan–Russia talks'),'{0} peace declaration; {1} Japan and Russia communicate.'),
 ('AFTERNOON',('COP31','Gas Husky sinking'),'{0} COP31 finance unresolved; {1} LPG tanker sinks off Bulgaria.'),
 ('EVENING',('Markets Nikkei','Markets BTC / WTI','Cyclone Akvan'),'{0} · {1} markets close higher; {2} cyclone alerts widen.')]
for i,(a,names,template) in enumerate(timeline):
 text=template.format(*(STORY_NUM[n] for n in names))
 numbered('timeline',names,text)
 assert 126+d.textlength(text,font=F(10))/S < 664
 t(38,364+i*29,a,9,RED,1); t(126,364+i*29,text,10)

B((680,328,320,190),(221,231,222)); t(692,340,'13 PIN WORLD MAP',12,RED,1); t(692,352,'red numbers mark stories 1–13',8,INK,1)
def project(lon,lat): return (700+(lon+180)*188/360, 355+(90-lat)*120/180)
land=[ [(-168,72),(-140,70),(-125,55),(-100,50),(-80,25),(-92,15),(-110,20),(-120,35),(-145,45)], [(-80,12),(-65,8),(-55,-5),(-65,-30),(-75,-55),(-50,-55),(-35,-20),(-45,5)], [(-10,35),(10,35),(35,30),(55,15),(45,5),(20,0),(5,10)], [(-18,15),(5,35),(30,30),(45,10),(35,-10),(20,-35),(0,-35),(-15,-5)], [(35,35),(60,40),(90,55),(125,50),(145,35),(130,20),(105,10),(80,15),(55,5)], [(70,5),(95,10),(115,0),(130,-10),(120,-25),(100,-5)], [(130,-10),(155,-15),(150,-35),(130,-40)], [(40,72),(80,75),(120,70),(150,60),(170,65),(160,75)], [(-55,75),(-30,80),(-20,65),(-40,60)], [(140,-5),(155,-10),(155,-25),(145,-20)]]
for poly in land: d.polygon([tuple(v*S for v in project(*pt)) for pt in poly],fill=(113,145,112))
pins=[(114,22.5,'Shenzhen'),(96.2,19.7,'Myanmar'),(-77,38.9,'US'),(34.5,31.5,'Gaza'),(37.6,55.7,'Russia'),(139.7,35.7,'Japan'),(127,37.5,'Korea'),(51.4,35.7,'Iran'),(48,29.4,'Kuwait'),(46.7,24.6,'Riyadh'),(147,-9.5,'PNG'),(178.4,-18.1,'Fiji'),(-72.3,18.5,'Haiti')]
mapped=[r for r in REGISTRY if r[2] is not None]
assert len(pins)==len(mapped)==13
PLACE_STORY={r[2]:r[0] for r in mapped}
assert set(PLACE_STORY)=={p[2] for p in pins}
pin_xy=[]
for i,(lon,lat,name) in enumerate(pins,1):
 x,y=project(lon,lat); pin_xy.append((x,y)); d.ellipse(((x-4)*S,(y-4)*S,(x+4)*S,(y+4)*S),fill=RED)
# Place labels around each real dot, enforcing label-to-label and label-to-dot clearance.
label_boxes=[]
MIN_GAP=16
def overlaps(a,b,gap=MIN_GAP): return a[0] < b[2]+gap and b[0] < a[2]+gap and a[1] < b[3]+gap and b[1] < a[3]+gap
# Wide deterministic candidate field: labels may fan into the open ocean, with long leaders.
candidate_xy=[(x,y) for y in range(366,492,4) for x in range(692,866,4)]
for i,(x,y) in enumerate(pin_xy,1):
 name=PLACE_STORY[pins[i-1][2]]; label=numbered('map pin',(name,),STORY_NUM[name]); bb=d.textbbox((0,0),label,font=F(8,1)); tw=bb[2]-bb[0]; th=bb[3]-bb[1]; chosen=None
 for lx,ly in sorted(candidate_xy,key=lambda q:(q[0]-x)**2+(q[1]-y)**2):
  if lx+tw/S>875 or ly < 366 or ly+th/S>498: continue
  box=(lx,ly,lx+tw/S,ly+th/S)
  if any(overlaps(box,old) for old in label_boxes): continue
  if any(j != i and box[0] < px+4+MIN_GAP and px-4-MIN_GAP < box[2] and box[1] < py+4+MIN_GAP and py-4-MIN_GAP < box[3] for j,(px,py) in enumerate(pin_xy,1)): continue
  chosen=(lx,ly,box); break
 assert chosen, f'label collision placement failed for pin {i}'
 lx,ly,box=chosen; label_boxes.append(box); d.line((x*S,y*S,lx*S,ly*S),fill=INK,width=S); t(lx,ly,label,8,INK,1)
assert all(not overlaps(a,b,MIN_GAP) for n,a in enumerate(label_boxes) for b in label_boxes[n+1:])
legend=[numbered('map legend',(name,),STORY_NUM[name]+' | '+place) for name,line,place in mapped]
assert legend == [STORY_NUM[PLACE_STORY[place]]+' '+place for _,_,place in mapped]
legend_y=366; legend_lead=10; legend_font=7
legend_height=(len(legend)-1)*legend_lead+legend_font
assert legend_y+legend_height <= 498
for j,item in enumerate(legend):
 assert 883+d.textlength(item,font=F(legend_font))/S <= 1000
 t(883,legend_y+j*legend_lead,item,legend_font)
regions='Asia-Pacific 6 · Middle East 4 · Americas 2 · Europe 1'
assert d.textlength(regions,font=F(7))/S <= 296
region_y=504
assert region_y+7 <= 518 and 352+8 < legend_y
assert legend_y+legend_height < region_y
assert 692+d.textlength('red numbers mark stories 1–13',font=F(8,1))/S <= 1000
t(692,region_y,regions,7)

cards=[
 (heading('card',('Iran dirty-bomb denial', 'Iran fires on Kuwait'),'Iran / Gulf'),'Iran fires on Kuwait; Tehran denies a dirty-bomb plot.'),
 (heading('card',('Crimean Bridge attack', 'Putin response'),'Ukraine / Russia'),'Crimean Bridge attacked for third time; Putin vows response.'),
 (heading('card',('Yongbyon enrichment', 'South Korea dialogue'),'Korea'),'IAEA says Yongbyon enrichment expands; Seoul calls for dialogue.'),
 (heading('card',('Gaza operation', 'Gaza aid plan'),'Gaza'),'Israel operation after evacuation orders; aid plan scores 4/26.'),
 (heading('card',('UN/ICC reform', 'APEC Outlook'),'Trade / AI'),'APEC Outlook covers trade, data and AI risks.'),
 (heading('card',('COP31',),'Climate'),'COP31 phaseout language, finance and 2035 target unresolved.'),
 (heading('card',('Fiji drought disaster', 'Cyclone Akvan'),'Asia–Pacific'),'Fiji disaster over drought; Akvan landfall forecast.'),
 (heading('card',('Indonesia asset bill', 'Serbia speaker'),'Institutions'),'Indonesia asset bill; Serbia elects Cupic 140–97.'),
 (heading('card',('Venezuelan TPS', 'Malaysia UNHCR'),'Migration'),'US asks court to block Venezuelan TPS; Malaysia UNHCR pause.'),
 (heading('card',('PNG Rio Tinto fund', 'US–Philippines loan'),'Economy'),'Rio Tinto $250m PNG fund; Philippines loan exceeds $2bn.'),
 (heading('card',('Saudi weather', 'Nassau storm alert'),'Weather'),'Saudi warnings through 24 Nov; Nassau storm alert.'),
 (heading('card',('Begich Alaska seat', 'Haiti plot conviction'),'US / Caribbean'),'Begich retains Alaska seat; pastor convicted in Haiti plot.'),
]
for i,(h,s) in enumerate(cards):
 x=24+(i%4)*245; y=536+(i//4)*53; B((x,y,235,48))
 # Added story IDs must not run into the unchanged status tag.
 title_size=13
 available=219-d.textlength('REPORTED',font=F(8,1))/S-6
 while d.textlength(h,font=F(title_size,1))/S > available: title_size-=1
 assert title_size >= 9
 t(x+8,y+6,h,title_size,INK,1); t(x+227,y+7,'REPORTED',8,RED,1,anchor='ra')
 last=p(x+8,y+25,s,10,34,12); audit_text_overflow(last,10,y+48)

B((24,696,976,122),(235,230,217)); t(36,708,'BRIEFS · THE REST OF THE FILE',11,RED,1)
briefs=[
 (heading('brief',('Voyager 1',),'VOYAGER 1'),'one light-day from Earth'),
 (heading('brief',('Save the Children',),'SAVE THE CHILDREN'),'589m children in conflict zones'),
 (heading('brief',('Riyadh PIF Tower attack',),'RIYADH'),'Houthi missile damages PIF Tower'),
 (heading('brief',('Bangladesh shutdown',),'BANGLADESH'),'shutdown and political violence'),
 (heading('brief',('Gas Husky sinking',),'BULGARIA'),'Gas Husky sinks with 3,400t LPG'),
 (heading('brief',('Iran war after Jan 1 2027',),'IRAN'),'war may continue after Jan 1, 2027'),
 (heading('brief',('Gaza aid plan',),'GAZA'),'peace-plan implementation 4/26'),
 (heading('brief',('Markets Nikkei',),'TOKYO'),'Nikkei 59,238 (+0.36%)'),
 (heading('brief',('Markets BTC / WTI',),'MARKETS'),'BTC ~$63k · WTI ~$82'),
 (heading('brief',('Anthropic IPO',),'SAN FRANCISCO'),'Anthropic IPO $83'),
 (heading('brief',('US–Philippines loan',),'US'),'loan package exceeds $2bn'),
 (heading('brief',('Prince Harry',),'LONDON'),'Prince Harry ready to re-enlist'),
]
for j,(city,rest) in enumerate(briefs):
 x=36+(j//6)*480; y=731+(j%6)*9; t(x,y,city,9,INK,1); t(x+len(city)*5.8+7,y,'— '+rest,9,INK,0)
t(36,789,'MARKETS',10,RED,1); t(108,789,'Nikkei 59,238 +0.36% · BTC ~$63k · WTI ~$82 · Take-Two +7.5% · Anthropic IPO $83',10,INK,1)
B((24,830,310,108)); t(36,842,'DATE CHECK',11,RED,1); p(36,862,f'TRUE · Thursday · ICJ ruling 19 Nov · APEC Outlook adopted · {N} stories · 6 regions · 13 pins',10,42,14)
B((350,830,650,108)); t(362,842,'SOURCES',11,RED,1); p(362,862,'Just Security · AppiSToS · Open Chronicle · Bangladesh Chronicle · BBC · Breitbart · NYT · Faithful Herald · Metacritic · IAEA',10,88,14,MUTED)
# Cross-check every recorded draw, require coverage, and independently inspect
# number/place relationships for both the legend and geographic labels.
assert {name for _,names,_ in DISPLAYED for name in names} == set(STORIES)
for section,names,labels in DISPLAYED:
 assert labels == tuple(STORY_NUM[name] for name in names), (section,names,labels)
for section in ('map legend','map pin'):
 actual={names[0]:labels[0] for sec,names,labels in DISPLAYED if sec==section}
 assert actual == {name:STORY_NUM[name] for name,_,_ in mapped}
NUMBERING_AUDIT=[(STORY_NUM[name],name,line,sorted({sec for sec,names,_ in DISPLAYED if name in names})) for name,line,_ in REGISTRY]
print('PASS: rectangle, hero text overflow, 16px label collision, numbering, legend/caption bounds')
out=os.path.join(root,'entry.png'); im.resize((1024,1024),Image.Resampling.LANCZOS).save(out,optimize=True); data=open(out,'rb').read(); assert len(data)<=1048576 and Image.open(out).getpixel((0,0))==BG; print(hashlib.sha256(data).hexdigest(),len(data))
