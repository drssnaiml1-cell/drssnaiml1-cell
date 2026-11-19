import sys, math
W,H=1200,600
esc=lambda t:t.replace("&","&amp;").replace("'","&#39;")
# eye-friendly palette: sky, aqua, lavender, gold on deep navy
C={"sky":("#FFB866","#FF9933"),"aqua":("#FFFFFF","#CBD5E1"),"lav":("#5EE38A","#138808"),"gold":("#8FA8FF","#2B4BD6")}  # saffron, white, India green, Ashoka Chakra blue
stats=[("08","Ph.D. Research Scholars","doctoral supervision","sky",8),
       ("38","Int'l Postdoctoral Scholars","NYUST (YunTech) · NKUST, Taiwan","aqua",38),
       ("10","National Postdoctoral Scholars","India","lav",10),
       ("56","Scholars Mentored","in total","gold",56)]
rows=[[("Agentic AI","sky"),("AI","sky"),("AGI","sky"),("ASI","sky"),("Machine Learning","aqua"),("Deep Learning","aqua"),("NLP","aqua")],
      [("Reinforcement Learning","aqua"),("Graph ML","aqua"),("Quantum ML","lav"),("Post-Quantum Security","lav"),("IoT & Cybersecurity","lav")],
      [("Precision Healthcare","gold"),("Medical Imaging","gold"),("Autonomous Systems","gold"),("Precision Agriculture","gold")]]
F='"Segoe UI",Inter,Helvetica,Arial,sans-serif'
o=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Research supervision: 8 Ph.D. research scholars, 38 international postdoctoral scholars, 10 national postdoctoral scholars, 56 scholars mentored. Research areas: '+esc(", ".join(t for r in rows for t,_ in r))+'">','<defs>',
'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#081427"/><stop offset=".55" stop-color="#0D1F3C"/><stop offset="1" stop-color="#132A4F"/></linearGradient>',
'<linearGradient id="card" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".09"/><stop offset="1" stop-color="#FFFFFF" stop-opacity=".02"/></linearGradient>',
'<linearGradient id="shine" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0"/><stop offset=".5" stop-color="#FFFFFF" stop-opacity=".18"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></linearGradient>',
'<linearGradient id="bar" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FF9933"/><stop offset=".33" stop-color="#FF9933"/><stop offset=".34" stop-color="#FFFFFF"/><stop offset=".66" stop-color="#FFFFFF"/><stop offset=".67" stop-color="#138808"/><stop offset="1" stop-color="#138808"/></linearGradient>',
'<filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="60"/></filter>',
'<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>',
f'<clipPath id="clip"><rect width="{W}" height="{H}" rx="20"/></clipPath>']
for k,(a,b) in C.items():
    o.append(f'<linearGradient id="g{k}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient>')
o.append('</defs>')
o.append(f'''<style>
.h{{font:700 13px {F};fill:#FFB866;letter-spacing:4px}}
.n{{font:800 34px {F}}}
.t{{font:700 16px {F};fill:#F1F5F9}}
.s{{font:500 12.5px {F};fill:#94A3B8}}
.p{{font:600 14.5px {F};fill:#E2E8F0}}
.up{{animation:up .9s cubic-bezier(.2,.8,.2,1) backwards}}
@keyframes up{{from{{opacity:0;transform:translateY(22px)}}to{{opacity:1;transform:none}}}}
.ring{{animation:draw 2.2s cubic-bezier(.3,.7,.2,1) backwards}}
@keyframes draw{{from{{stroke-dashoffset:239}}}}
.sh{{animation:sh 6s ease-in-out infinite}}
@keyframes sh{{0%,55%{{transform:translateX(-320px)}}85%,100%{{transform:translateX(320px)}}}}
.blob1{{animation:d1 18s ease-in-out infinite}}.blob2{{animation:d2 22s ease-in-out infinite}}.blob3{{animation:d1 26s ease-in-out infinite reverse}}
@keyframes d1{{0%,100%{{transform:translate(0,0)}}50%{{transform:translate(160px,60px)}}}}
@keyframes d2{{0%,100%{{transform:translate(0,0)}}50%{{transform:translate(-180px,-40px)}}}}
.chip{{animation:pop .6s cubic-bezier(.3,1.5,.5,1) backwards}}
@keyframes pop{{from{{opacity:0;transform:scale(.6)}}to{{opacity:1;transform:none}}}}
.fl{{animation:fl 5s ease-in-out infinite}}@keyframes fl{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-3px)}}}}
.bd{{animation:bd 4s ease-in-out infinite}}@keyframes bd{{0%,100%{{stroke-opacity:.35}}50%{{stroke-opacity:.95}}}}
.tw{{animation:tw 3s ease-in-out infinite}}@keyframes tw{{0%,100%{{opacity:.15}}50%{{opacity:.9}}}}
.glint{{animation:gl 4s ease-in-out infinite}}@keyframes gl{{to{{transform:translateX(1400px)}}}}
.pu{{animation:pu 2.4s ease-in-out infinite}}@keyframes pu{{0%,100%{{opacity:.5;r:4px}}50%{{opacity:1;r:6px}}}}
.chip,.chk{{transform-box:fill-box;transform-origin:center}}
.chk{{animation:spin 40s linear infinite}}@keyframes spin{{to{{transform:rotate(360deg)}}}}
</style>''')
o.append('<g clip-path="url(#clip)">')
o.append(f'<rect width="{W}" height="{H}" fill="url(#bg)"/>')
o.append('<circle class="blob1" cx="180" cy="120" r="170" fill="#FF9933" opacity=".20" filter="url(#blur)"/>')
o.append('<circle class="blob2" cx="1020" cy="140" r="170" fill="#138808" opacity=".24" filter="url(#blur)"/>')
o.append('<circle class="blob3" cx="620" cy="520" r="200" fill="#2B4BD6" opacity=".22" filter="url(#blur)"/>')
cx0,cy0,RR=W/2,470,150
sp="".join(f'<line x1="{cx0}" y1="{cy0}" x2="{cx0+RR*math.cos(math.radians(a*15)):.1f}" y2="{cy0+RR*math.sin(math.radians(a*15)):.1f}"/>' for a in range(24))
o.append(f'<g class="chk" opacity=".07" stroke="#8FA8FF" fill="none"><circle cx="{cx0}" cy="{cy0}" r="{RR}" stroke-width="6"/><circle cx="{cx0}" cy="{cy0}" r="16" fill="#8FA8FF"/><g stroke-width="2.5">{sp}</g></g>')
import random; random.seed(7)
for i in range(26):
    x,y=random.randint(20,1180),random.randint(20,580)
    o.append(f'<circle class="tw" style="animation-delay:{random.random()*3:.2f}s" cx="{x}" cy="{y}" r="{random.choice([1,1.2,1.6])}" fill="#E2E8F0"/>')
# animated top bar
o.append('<rect width="1200" height="6" fill="url(#bar)"/><rect class="glint" x="-200" width="200" height="6" fill="url(#shine)"/>')
o.append(f'<circle class="pu" cx="{W/2-150}" cy="40" r="4" fill="#FF9933"/><text x="{W/2}" y="45" text-anchor="middle" class="h">RESEARCH SUPERVISION</text><circle class="pu" style="animation-delay:1.2s" cx="{W/2+150}" cy="40" r="4" fill="#5EE38A"/>')
cw,gap,ch=264,24,196; x0=(W-(4*cw+3*gap))/2; y0=68
R=38; circ=2*math.pi*R
for i,(n,t,s,k,v) in enumerate(stats):
    x=x0+i*(cw+gap); cx=x+cw/2; a=C[k][0]
    frac=v/56; off=circ*(1-frac)
    o.append(f'<g class="up" style="animation-delay:{.1+i*.15:.2f}s"><g class="fl" style="animation-delay:{i*.7:.1f}s">')
    o.append(f'<rect x="{x}" y="{y0}" width="{cw}" height="{ch}" rx="18" fill="url(#card)"/>')
    o.append(f'<rect x="{x}" y="{y0}" width="{cw}" height="{ch}" rx="18" fill="none" stroke="url(#g{k})" stroke-width="1.6" class="bd" style="animation-delay:{i*.8:.1f}s"/>')
    o.append(f'<svg x="{x}" y="{y0}" width="{cw}" height="{ch}"><rect class="sh" style="animation-delay:{i*.9:.1f}s" x="-40" y="-20" width="120" height="{ch+40}" fill="url(#shine)" transform="skewX(-18)"/></svg>')
    o.append(f'<circle cx="{cx}" cy="{y0+62}" r="{R}" fill="none" stroke="#FFFFFF" stroke-opacity=".08" stroke-width="7"/>')
    cy=y0+62; o.append(f'<path class="ring" style="animation-delay:{.4+i*.2:.2f}s;stroke-dasharray:{circ:.1f};stroke-dashoffset:{off:.1f}" d="M{cx} {cy-R} a{R} {R} 0 1 1 0 {2*R} a{R} {R} 0 1 1 0 {-2*R}" fill="none" stroke="url(#g{k})" stroke-width="7" stroke-linecap="round" filter="url(#glow)"/>')
    o.append(f'<text x="{cx}" y="{y0+74}" text-anchor="middle" class="n" fill="url(#g{k})">{n}</text>')
    o.append(f'<text x="{cx}" y="{y0+136}" text-anchor="middle" class="t">{esc(t)}</text>')
    o.append(f'<text x="{cx}" y="{y0+160}" text-anchor="middle" class="s">{esc(s)}</text>')
    o.append(f'<rect x="{cx-18}" y="{y0+174}" width="36" height="3" rx="1.5" fill="url(#g{k})"/>')
    o.append('</g></g>')
o.append(f'<text x="{W/2}" y="325" text-anchor="middle" class="h">RESEARCH AREAS</text>')
# legend
leg=[("AI Foundations","sky"),("Learning Systems","aqua"),("Quantum & Security","lav"),("Applied AI","gold")]
lw=[len(t)*7+40 for t,_ in leg]; lx=(W-sum(lw))/2
for (t,k),w in zip(leg,lw):
    o.append(f'<circle cx="{lx+6}" cy="347" r="5" fill="url(#g{k})"/><text x="{lx+18}" y="351" class="s">{esc(t)}</text>'); lx+=w
y=372; idx=0
for r in rows:
    ws=[max(len(t)*8.9+48,78) for t,_ in r]; tot=sum(ws)+14*(len(r)-1); x=(W-tot)/2
    for (t,k),w in zip(r,ws):
        a,b=C[k]; idx+=1
        o.append(f'<g class="chip" style="animation-delay:{.9+idx*.07:.2f}s"><g class="fl" style="animation-delay:{idx*.33%5:.2f}s">')
        o.append(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="42" rx="21" fill="{b}" fill-opacity=".16"/>')
        o.append(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="42" rx="21" fill="none" stroke="url(#g{k})" stroke-width="1.3" class="bd" style="animation-delay:{idx*.25%4:.2f}s"/>')
        o.append(f'<circle cx="{x+18:.1f}" cy="{y+21}" r="4" fill="{a}"/>')
        o.append(f'<text x="{x+w/2+7:.1f}" y="{y+26}" text-anchor="middle" class="p">{esc(t)}</text></g></g>')
        x+=w+14
    y+=62
o.append('</g>')
o.append(f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="20" fill="none" stroke="#FFFFFF" stroke-opacity=".08"/>')
o.append('</svg>')
open(sys.argv[1],'w').write("\n".join(o))
