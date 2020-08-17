import io
import sys
_INPUT="""\
2
1 1
"""
sys.stdin=io.StringIO(_INPUT)
n=int(input())
l=list(map(int,input().split()))
l=sorted(l)

cnt=0
for i in range(n):
    for j in range(i+1,n):
        if l[i]==l[j]:
            continue
        else:
            for k in range(j+1,n):
                if l[j]==l[k]:
                    continue
                else:
                    if l[i]+l[j]>l[k] and l[j]+l[k]>l[i] and l[k]+l[i]>l[j]:
                        cnt+=1
print(cnt)