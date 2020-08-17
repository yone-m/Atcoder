import io
import sys
_INPUT="""\
RRS
"""
sys.stdin=io.StringIO(_INPUT)
s=input()

cntr=0
for i in range(3):
    if s[i]=="R":
        cntr+=1
    if cntr==0 or cntr==1:
        ans=cntr
    elif cntr==2:
        if s[1]=="R":
            ans=2
        else:
            ans=1
    else:
        ans=3
print(ans)