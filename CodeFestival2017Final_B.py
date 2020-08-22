import io
import sys
_INPUT="""\
"""
sys.stdin=io.StringIO(_INPUT)
s=input()
def kaibun(s):
    ls=len(s)

    if ls==0:
        print("YES")
        return
    ca,cb,cc=0,0,0
    l=[]
    for i in range(ls):
        if s[i]=="a":
            ca+=1
            l.append(ca)
        if s[i]=="b":
            cb+=1
            l.append(cb)
        if s[i]=="c":
            cc+=1
            l.append(cc)
    cnt=0
    for j in l:
        if j==0:
            cnt+=1
    if cnt==2:
        print("NO")
        return

    elif cnt==1:
        if ls==2:
            print("YES")
            return
        else:
            print("NO")
            return
    
    else:
        cnt=0
        for j in l:
            if j>=0:
                cnt+=1


