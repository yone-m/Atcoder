import sys

n,m,t=map(int,input().split())

al=[]
bl=[]
for i in range(m):
    a,b=map(int,input().split())
    al.append(a)
    bl.append(b)

nokori=n-al[0]

if nokori<=0:
    print("No")
    sys.exit()

for i in range(m-1):
    nokori+=bl[i]-al[i]
    nokori=min(n,nokori)
    nokori-=al[i+1]-bl[i]
    if nokori<=0:
        print("No")
        sys.exit()

nokori+=bl[m-1]-al[m-1]
nokori=min(n,nokori)

nokori-=t-bl[m-1]
if nokori<=0:
    print("No")
    sys.exit()

print("Yes")