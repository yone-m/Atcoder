n=int(input())
h=list(map(int,input().split()))

dp=[10**9]*(n)

dp[0]=0
dp[1]=abs(h[0]-h[1])

for i in range(2,n):
    c1=abs(h[i-1]-h[i])+dp[i-1]
    c2=abs(h[i-2]-h[i])+dp[i-2]
    dp[i]=min(c1,c2)

print(dp[n-1])