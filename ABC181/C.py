import itertools
import sys
n=int(input())

xl=[]
yl=[]
for i in range(n):
    x,y=map(int,input().split())
    xl.append(x)
    yl.append(y)

listN=list(itertools.combinations(list(range(n)),3))

for a in listN:
    if (xl[a[2]]-xl[a[1]])*(yl[a[0]]-yl[a[1]])==(yl[a[2]]-yl[a[1]])*(xl[a[0]]-xl[a[1]]):
        print("Yes")
        sys.exit()
print("No")
