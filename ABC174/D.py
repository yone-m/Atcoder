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
cnt=0

if A[0]=="W" and A[1]=="R":
    A[0]="R"
    cnt+=1

for i in range(1,N-2):
    if A[i]=="W" and A[i+1]=="R":
        if A[i-1]=="W":
            A[i+1]="W"
        else:
            A[i]="R"
        cnt+=1

if A[N-2]=="W" and A[N-1]=="R":
    A[N-1]=="W"
    cnt+=1

print(cnt)


