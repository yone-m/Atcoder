n=int(input())
al=[]
bl=[]
sl=[]
for i in range(n):
    a,b=map(int,input().split())
    al.append(a)
    bl.append(b)
    sl.append([a,b])

sl.sort(key=lambda x:x[1])

t=0
import sys
for i in range(n):
    t+=sl[i][0]
    if t>sl[i][1]:
        print("No")
        sys.exit()
    
print("Yes")