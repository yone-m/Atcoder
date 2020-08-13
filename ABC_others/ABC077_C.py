n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
al=sorted(a)
bl=sorted(b)
cl=sorted(c)
abl=[0]*n
bcl=[0]*n
i=n-1
for j in range(n-1,-1,-1):
    while al[i]>=bl[j]:
        i-=1
        if i==-1:
            break
    if i==-1:
        abl[j]=0
    else:
        abl[j]=i+1
k=0
for j in range(n):
    while cl[k]<=bl[j]:
        k+=1
        if k==n:
            break
    if k==n:
        bcl[j]=0
    else:
        bcl[j]=(n-k)
ans=0
for s in range(n):
    ans+=abl[s]*bcl[s]
print(ans)