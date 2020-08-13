import io
import sys
_INPUT="""\
    1 10
"""
sys.stdin=io.StringIO(_INPUT)
n,k=map(int,input().split())

numk=k
for _ in range(2,n+1):
    numk=numk*(k-1)
print(numk)