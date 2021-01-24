import sys
from decimal import Decimal
n,x=map(int,input().split())

vl=[]
pl=[]
for i in range(n):
    v,p=map(int,input().split())
    vl.append(v)
    pl.append(p)

suma=0
for i in range(n):
    suma+=vl[i]*pl[i]*Decimal("0.01")
    if suma>x:
        print(i+1)
        sys.exit()

print(-1)