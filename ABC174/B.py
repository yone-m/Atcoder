import io
import sys
_INPUT="""\
    20 100000
14309 -32939
-56855 100340
151364 25430
103789 -113141
147404 -136977
-37006 -30929
188810 -49557
13419 70401
-88280 165170
-196399 137941
-176527 -61904
46659 115261
-153551 114185
98784 -6820
94111 -86268
-30401 61477
-55056 7872
5901 -163796
138819 -185986
-69848 -96669
"""
sys.stdin=io.StringIO(_INPUT)

import math
a,b=map(int,input().split())
xl=[]
yl=[]
for i in range(a):
    x,y=map(int,input().split())
    xl.append(x)
    yl.append(y)

cnt=0
for i in range(a):
    if math.sqrt(xl[i]**2+yl[i]**2)<=b:
        cnt+=1
print(cnt)