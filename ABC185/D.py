import sys

n,m=map(int,input().split())

#0~m-1
a=list(map(int,input().split()))
a=sorted(a)

if m==0:
    print(1)
    sys.exit()
if m==n:
    print(0)
    sys.exit()

b=[]
if a[0]!=1:
    b.append(a[0]-1)

for i in range(m-1):
    if (a[i+1]-a[i]-1)!=0:
        b.append(a[i+1]-a[i]-1)

if a[m-1]!=n:
    b.append(n-a[m-1])

minb=min(b)

ans=0
for i in b:
    if i%minb==0:
        ans+=i/minb
    else:
        ans+=i//minb+1

print(int(ans))