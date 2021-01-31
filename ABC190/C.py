import collections

n,m=map(int,input().split())
#al=[]
#bl=[]
cl=[]
dl=[]
sl=[]
ssl=[]
for i in range(m):
    a,b=map(int,input().split())
    #al.append(a)
    #bl.append(b)
    sl.append(a)
    sl.append(b)
    ssl.append([a,b])
k=int(input())
cdl=[]
for i in range(k):
    c,d=map(int,input().split())
    cl.append(c)
    dl.append(d)
    cdl.append([c,d])

setsl=set(sl)
ans=0
for i in range(2**k):
    nsl=set()
    for j in range(k):
        if ((i>>j)&1):
            nsl.add(cdl[j][0])
        else:
            nsl.add(cdl[j][1])
    cnt=0
    for x in range(m):
        if ssl[x][0] in nsl and ssl[x][1] in nsl:
            cnt+=1
    
    ans=max(ans,cnt)

print(ans)