import io
import sys
_INPUT="""\
3
1
2
4
"""
sys.stdin=io.StringIO(_INPUT)
n=int(input())
al=[]
for i in range(n):
    a=int(input())
    al.append(a)
sal=sum(al)

minsum=sal
for i in range(2**n):
    sumn=0
    sumn2=0
    for j in range(n):
        if ((i>>j)&1):
            sumn+=al[j]
        else:
            sumn2+=al[j]
    if minsum>=abs(sumn-sumn2):
        minsum=abs(sumn-sumn2)
        maxn=max(sumn2,sumn)
print(maxn)