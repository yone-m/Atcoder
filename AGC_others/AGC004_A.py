import io
import sys
_INPUT="""\
    999999989 999999993 999999991
"""
sys.stdin=io.StringIO(_INPUT)
a,b,c=map(int,input().split())

def block(a,b,c):
    blocksum=a*b*c
    if a%2==0 or b%2==0 or c%2==0:
        print(0)
        return
    else:
        if a!=1:
            print(blocksum-2*(a//2)*b*c)
            return
        elif b!=1:
            print(blocksum-2*(b//2)*a*c)
            return
        elif c!=1:
            print(blocksum-2*(c//2)*a*b)
            return
        else:
            print(1)
            return
block(a,b,c)