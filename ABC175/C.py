import io
import sys
_INPUT="""\
10 1 2
"""
sys.stdin=io.StringIO(_INPUT)
x,k,d=map(int,input().split())

def counta(x,k,d):
    #xcnt=0
    x=abs(x)
    if d<2*x:
        ans=x//d
        #amari=x%d
        if ans>k:
            print(abs(x-k*d))
            return
        k=k-ans
        x=x-ans*d
        if k%2==0:
            print(x)
            return
        else:
            print(abs(x-d))
            return
    else:
        if k%2==0:
            print(x)
            return
        else:
            print(abs(x-d))
            return
counta(x,k,d)