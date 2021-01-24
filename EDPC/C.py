n=int(input())
al=[]
bl=[]
cl=[]
for i in range(n):
    a,b,c=map(int,input().split())
    al.append(a)
    bl.append(b)
    cl.append(c)

dp=[[(-1)]*3 for _ in range(n)]
dp[0][0]=al[0]
dp[0][1]=bl[0]
dp[0][2]=cl[0]

for i in range(1,n):
    a1=dp[i-1][1]+al[i]
    a2=dp[i-1][2]+al[i]
    dp[i][0]=max(a1,a2)

    b1=dp[i-1][0]+bl[i]
    b2=dp[i-1][2]+bl[i]
    dp[i][1]=max(b1,b2)

    c1=dp[i-1][0]+cl[i]
    c2=dp[i-1][1]+cl[i]
    dp[i][2]=max(c1,c2)

print(max(dp[n-1]))

