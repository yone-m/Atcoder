import io
import sys
_INPUT="""\
    999983
"""
sys.stdin=io.StringIO(_INPUT)
N=int(input())

def waru(N):
    if N%2==0 or N%5==0:
        print("-1")
        return
    
    i=1
    while(i<1000000000):
        if 7*(10**i-1)%(9*N)==0:
            print(i)
            return
        i+=1
    
    print("-1")
waru(N)