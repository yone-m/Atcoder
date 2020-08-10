import io
import sys
_INPUT="""\
   8
WRWWRWRR
"""
sys.stdin=io.StringIO(_INPUT)

N=int(input())
s=input()
A=[]
for i in range(N):
    A.append(s[i])

cntW=0
for i in range(N):
    if A[i]=="W":
        cntW+=1
cntR=N-cntW

changeW=0
changeR=0
for i in range(cntR):
    if A[i]=="W":
        changeW+=1
for i in range(cntR,N):
    if A[i]=="R":
        changeR+=1

if changeR==changeW:
    ans=changeW
else:
    #minN=min(changeW,changeR)
    maxN=max(changeR,changeW)
    ans=maxN
print(ans)