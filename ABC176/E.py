import io
import sys
_INPUT="""\
5 5 10
2 5
4 3
2 3
5 5
2 2
5 4
5 3
5 1
3 5
1 4
"""
sys.stdin=io.StringIO(_INPUT)
h,w,m=map(int,input().split())
import collections
h2l=[]
w2l=[]
for i in range(m):
    h2,w2=map(int,input().split())
    h2l.append(h2)
    w2l.append(w2)

ch=collections.Counter(h2l)
cw=collections.Counter(w2l)

ans=0
chcnt=1
cwcnt=1
chl=[]
cwl=[]
chl.append(ch.most_common()[0][0])
cwl.append(cw.most_common()[0][0])
for i in range(len(ch)-1):
    if ch.most_common()[i][1]==ch.most_common()[i+1][1]:
        chl.append(ch.most_common()[i+1][0])
        chcnt+=1
    else:
        break
for i in range(len(cw)-1):
    if cw.most_common()[i][1]==cw.most_common()[i+1][1]:
        cwl.append(cw.most_common()[i+1][0])
        cwcnt+=1
    else:
        break

for i in range(chcnt):
    for j in range(cwcnt):
        ansx=ch.most_common()[i][0]
        ansy=cw.most_common()[j][0]
        ansh=ch.most_common()[i][1]
        answ=cw.most_common()[j][1]
        for k in range(m):
            if ansx==h2l[k] and ansy==w2l[k]:
                ans=0
                break
            ans=ansh+answ

print(ans if ans>0 else ansh+answ-1)

