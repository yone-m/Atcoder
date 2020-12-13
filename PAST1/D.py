import collections as col

n=int(input())
a=[]
for i in range(n):
    s=int(input())
    a.append(s)

al=sorted(a)
c=col.Counter(al)
num=c.most_common()[0][1]

if num==1:
    print("Correct")
else:
    wnum=c.most_common()[0][0]
    for j in range(1,n):
        if c[j]==0:
            cnum=j
            break
        else:
            cnum=n
    print(wnum,cnum)