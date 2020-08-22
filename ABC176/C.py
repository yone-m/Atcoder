import io
import sys
_INPUT="""\
5
3 3 3 3 3
"""
sys.stdin=io.StringIO(_INPUT)
n=int(input())
a=list(map(int,input().split()))

maxh=a[0]
ans=0
for i in range(1,n):
    if maxh<a[i]:
        maxh=a[i]
    else:
        ans+=maxh-a[i]

print(ans)
