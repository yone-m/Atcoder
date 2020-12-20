n=int(input())
a=list(map(int,input().split()))

sa=sorted(a,reverse=True)

ans=0
sumo=sum(sa)-sa[0]
for i in range(n-1):
    suma=sa[i]*(n-i-1)
    ans+=abs(suma-sumo)
    sumo-=sa[i+1]

print(ans)