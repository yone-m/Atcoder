import io
import sys
_INPUT="""\
1000 1234000
"""
sys.stdin=io.StringIO(_INPUT)
n,y=map(int,input().split())
def money(n,y):
    for i in range(n+1):
        if y-10000*i<0:
            continue
        for j in range(n-i+1):
            if y-10000*i-5000*j<0:
                continue
            k=n-i-j
            if 10000*i+5000*j+1000*k==y:
                print(i,j,k)
                return
    print("-1 -1 -1")
money(n,y)