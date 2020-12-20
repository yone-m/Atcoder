t=int(input())
nl=[]
sl=[]
kl=[]
for i in range(t):
    n,s,k=map(int,input().split())
    nl.append(n)
    sl.append(s)
    kl.append(k)

def fn(rrr,mmm):
    n=len(rrr)
    r0=0
    m0=1

    for i in range(n):
        r1=rrr[i]%mmm[i]
        


