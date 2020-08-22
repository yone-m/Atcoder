import io
import sys
_INPUT="""\
123456789
"""
sys.stdin=io.StringIO(_INPUT)
n=input()

ln=len(n)
sum=0
for i in range(ln):
    a=int(n[i])
    sum+=a

if sum%9==0:
    print("Yes")
else:
    print("No")