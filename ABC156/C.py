n=int(input())
a=list(map(int,input().split()))

sa=sum(a)

av=round(sa/n)
ans=0
for x in a:
    ans+=(av-x)**2

print(ans)