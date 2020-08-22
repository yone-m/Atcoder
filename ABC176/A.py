import io
import sys
_INPUT="""\
20 12 6
"""
sys.stdin=io.StringIO(_INPUT)
#n=int(input())
#a=list(map(int,input().split()))
n,x,t=map(int,input().split())
loop=n//x
ama=n%x
if ama==0:
    print(t*loop)

else:
    print(t*(loop+1))
