n,m=map(int,input().split())

a=list(map(int,input().split()))
b=list(map(int,input().split()))

ans=0
ans2=0
if n==m:
    for i in range(n):
        if a[i]!=b[i] and a[i]<=n:
            ans+=1
    