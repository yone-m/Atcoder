import itertools

n=int(input())

xl=[]
yl=[]
for i in range(n):
    a,b=map(int,input().split())
    xl.append(a)
    yl.append(b)

listN=list(itertools.combinations(list(range(n)),2))

ans=0
for a in listN:
    if (yl[a[0]]-yl[a[1]])/(xl[a[0]]-xl[a[1]])<=1 and -1<=(yl[a[0]]-yl[a[1]])/(xl[a[0]]-xl[a[1]]):
        ans+=1
print(ans)