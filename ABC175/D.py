import io
import sys
_INPUT="""\
10 58
9 1 6 7 8 4 3 2 10 5
695279662 988782657 -119067776 382975538 -151885171 -177220596 -169777795 37619092 389386780 980092719
"""
sys.stdin=io.StringIO(_INPUT)
import collections
#コマがマスiにあればコマをPiに移動させる
#このときスコアに+Cpiされる
def sugoroku():
    n,k=map(int,input().split())
    p=list(map(int,input().split()))
    c=list(map(int,input().split()))
    maxn=-10**15

    ll=[]
    l=[]
    for i in range(n):
        l.append(i)
        koma=i
        for j in range(n-1):
            koma=p[koma]-1
            l.append(koma)
            c=collections.Counter(l)
            if len(c)!=j+1:
                l=set(l)
                ll.append(l)




    if k<=n:
        for i in range(n):
            ans=0
            koma=p[i]-1
            ans+=c[koma]
            for _ in range(1,k):
                koma=p[koma]-1
                ans+=c[koma]
                maxn=max(ans,maxn)
            maxn=max(ans,maxn)
        print(maxn)
        return

    else:
        suml=sum(c)
        if suml>0:
            ck=k%n
            loop=k//n
            if ck!=0:
                for i in range(n):
                    ans=0
                    koma=p[i]-1
                    ans+=c[koma]
                    for _ in range(ck-1):    
                        koma=p[koma]-1
                        ans+=c[koma]
                        maxn=max(ans,maxn)
                nmaxn=loop*suml+maxn
                print(nmaxn)
                return
            else:
                print(loop*suml)
                return
        else: 
            for i in range(n):
                ans=0
                koma=p[i]-1
                ans+=c[koma]
                for _ in range(1,n):
                    koma=p[koma]-1
                    ans+=c[koma]
                    maxn=max(ans,maxn)
                maxn=max(ans,maxn)
            print(maxn)
            return
sugoroku()