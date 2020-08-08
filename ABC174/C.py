import io
import sys
_INPUT="""\
    999983
"""
sys.stdin=io.StringIO(_INPUT)
N=int(input())

def waru(N):
    if N%2==0:
        print("-1")
        return

    i=1
    while i<10:
        l=["7"]*i
        num="".join(l)
        num=int(num)
        if num%N==0:
            print(i)
            return
    print("-1")
waru(N)