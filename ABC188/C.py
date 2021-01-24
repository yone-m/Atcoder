n=int(input())

a=list(map(int,input().split()))

la=int(len(a)/2)

max1=max(a[:la])
max2=max(a[la:])

min1=min(max1,max2)

for i in range(2**n):
    if a[i]==min1:
        print(i+1)

