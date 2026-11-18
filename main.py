# tiny-chess-01 @newton — PST-ordered captures, deterministic, <4KB
import json,os,sys,urllib.request,urllib.error
E=os.environ.get("MAKEFUN_ENV_URL")or sys.exit("MAKEFUN_ENV_URL unset")
V={"p":1,"n":3,"b":3,"r":5,"q":9,"k":100}
# central control + development bias (index 0=a8 ... 63=h1 for white tables; black mirrored)
C=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,2,2,2,2,1,1,1,2,3,4,4,3,2,1,1,2,4,5,5,4,2,1,1,2,3,4,4,3,2,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0]
def post(p,b):
 r=urllib.request.Request(E+p,data=json.dumps(b).encode(),headers={"content-type":"application/json"})
 try:
  with urllib.request.urlopen(r)as x:return json.load(x)
 except urllib.error.HTTPError as e:sys.exit("%s:%s"%(p,e.code))
def board(fen):
 B={};r=0
 for row in fen.split()[0].split("/"):
  f=0
  for c in row:
   if c.isdigit():f+=int(c)
   else:B["abcdefgh"[f]+str(8-r)]=c;f+=1
  r+=1
 return B
def idx(s):return ord(s[0])-97+(8-int(s[1]))*8
def choose(fen,legal):
 B=board(fen);side=fen.split()[1]
 def rank(m):
  fr,to=m[:2],m[2:4]
  mover=B[fr];mv=mover.lower()
  victim=B.get(to)
  if victim is None and mv=="p" and fr[0]!=to[0]:victim="p"  # ep
  taken=V[victim.lower()]if victim else 0
  promo=V[m[4]]if len(m)>4 else 0
  # prefer captures, then central to-square, then cheaper mover
  cent=C[idx(to)if mover.isupper()else 63-idx(to)]
  return(-taken-promo*2,-cent,V[mv],m)
 return min(legal,key=rank)
while 1:
 g=post("/game",{})
 if g["status"]=="done":break
 while g["status"]=="your_move":
  g=post("/move",{"game":g["game"],"move":choose(g["fen"],g["legal_moves"])})
 print("game",g.get("game"),g.get("outcome"),file=sys.stderr)
print("done",g.get("wins"),g.get("draws"),g.get("losses"),file=sys.stderr)
