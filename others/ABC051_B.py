import io
import sys
_INPUT="""\
2 2
"""
sys.stdin=io.StringIO(_INPUT)
a,b=map(int,input().split())
#x,y,z<=a
#x+y+z=b
#0<=b<=3a
ans=0
for x in range(a+1):
    #y+z=b-x
    minn=min(a,b-x)
    for y in range(minn+1):
        z=b-x-y
        if 0<=z and z<=a:
            ans+=1
print(ans)
