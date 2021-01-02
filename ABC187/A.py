a,b=map(int,input().split())

sa=str(a)
sb=str(b)
la=len(sa)
lb=len(sb)

ansa=0
ansb=0
for i in range(la):
    ansa+=int(sa[i])
for i in range(lb):
    ansb+=int(sb[i])

print(max(ansb,ansa))