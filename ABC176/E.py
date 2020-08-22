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
'''
ansh=ch.most_common()[0][1]
answ=cw.most_common()[0][1]
ansx=ch.most_common()[0][0]
ansy=cw.most_common()[0][0]
ans=ansh+answ

nexth=ch.most_common()[0][1]+ch.most_common()[1][1]
nextw=cw.most_common()[0][1]+cw.most_common()[1][1]
'''
chcnt=0
cwcnt=0
for i in range(len(ch)-1):
    if ch.most_common()[i][1]==ch.most_common()[i+1][1]:
        chcnt+=1
for i in range(len(cw)-1):
    if cw.most_common()[i][1]==cw.most_common()[i+1][1]:
        cwcnt+=1
num=0
ansh=ch.most_common()[0][1]
ansx=ch.most_common()[0][0]
answ=cw.most_common()[0][1]
ansy=cw.most_common()[0][0]
ans=ansh+answ
point=1

i=0
j=0
for i in range(chcnt):
    for j in range(cwcnt):
        ansh=ch.most_common()[i][1]
        ansx=ch.most_common()[i][0]
        answ=cw.most_common()[j][1]
        ansy=cw.most_common()[j][0]
        ans=ansh+answ
        for k in range(m):
            if h2l[k]==ansx and w2l[k]==ansy:
                ans-=1
        num=max(num,ans)
num=max(num,ans)
'''
while(point==1):
    for i in range(1,h-1):
        out=0
        if ansh!=ch.most_common()[i-1][1]:
            out+=1
            ansh=ch.most_common()[i-1][1]
            ansx=ch.most_common()[i-1][0]
        else:
            ansh=ch.most_common()[i][1]
            ansx=ch.most_common()[i][0]

        for j in range(1,w-1):
            if cw.most_common()[j][1]!=ch.most_common()[i-1][1]:
                out+=1
                answ=cw.most_common()[j-1][1]
                ansy=cw.most_common()[j-1][0]
                if out>=2:
                    point=0
            else:
                answ=cw.most_common()[j][1]
                ansy=cw.most_common()[j][0]
            ans=ansh+answ
            if h2l[i]==ansx and w2l[j]==ansy:
                ans-=1
            num=max(ans,num)
'''
print(num)
