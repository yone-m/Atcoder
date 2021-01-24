n,k=map(int,input().split())
h=list(map(int,input().split()))

dp=[10**9]*n
dp[0]=0
dp[1]=abs(h[0]-h[1])

for i in range(2,n):
    for j in range(1,k+1):
        if i-j<0:
            break
        c=dp[i-j]+abs(h[i-j]-h[i])
        dp[i]=min(dp[i],c)

print(dp[n-1])
