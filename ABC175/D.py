import io
import sys
_INPUT="""\
3 3
3 1 2
-1000 -2000 -3000
"""
sys.stdin=io.StringIO(_INPUT)
n,k=map(int,input().split())
p=list(map(int,input().split()))
c=list(map(int,input().split()))

#コマがマスiにあればコマをPiに移動させる
#このときスコアに+Cpiされる
maxn=-10**15
for i in range(n):
    #si=0
    ck=k
    ans=0
    koma=i
    if k>=n:
        ck=k%n
        kaisu=(k-(k%n))//n
        #kaisu=k//n
        sump=sum(p)
        ans+=sump*kaisu
    else:
        ck=k

    while ck>=1:
        koma=p[koma]-1
        ans+=c[koma]
        maxn=max(maxn,ans)
        ck-=1
print(maxn)
'''
for i in range(n):
    ans=0
    maxn=-10**15
    for j in range(k):
        z=p[i]-1
        ans+=c[z]
        maxn=max(maxn,ans)
        lm[i]=maxn
print(lm)
'''