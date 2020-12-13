n=int(input())
a=list(map(int,input().split()))

for i in range(n):
    a[i]%=(10**9+7)

b=[0]*(n-1)
suma=sum(a)
sumb=suma
for i in range(n-1):
    sumb=sumb-a[i]
    b[i]=sumb%(10**9+7)

num=0
for i in range(n-1):
    num+=(a[i]*b[i])%(10**9+7)
num%=(10**9+7)
print(num)