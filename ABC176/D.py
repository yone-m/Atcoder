import io
import sys
_INPUT="""\
"""
sys.stdin=io.StringIO(_INPUT)
h,w=map(int,input().split())
ch,cw=map(int,input().split())
dh,dw=map(int,input().split())
ls=[]
for i in range(h):
    s=input()
    ls.append(s)

    
