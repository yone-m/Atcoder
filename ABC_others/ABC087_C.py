import io
import sys
_INPUT="""\
    5
    3 2 2 4 1
    1 2 2 2 1
"""
sys.stdin=io.StringIO(_INPUT)

N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

ans=0
for i in range(N):
    sumn=sum(A[:i+1])+sum(B[i:])
    ans=max(sumn,ans)
print(ans)

