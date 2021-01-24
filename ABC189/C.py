n=int(input())
a=list(map(int,input().split()))

ans=0
for i in range(n):
    sums=0
    j=i
    while a[i]<=a[j]:
        sums+=a[i]
        j+=1
        if j>=n:
            break
    k=i
    while a[i]<=a[k]:
        sums+=a[i]
        k-=1
        if k<0:
            break
    sums-=a[i]
    ans=max(ans,sums)

print(ans)