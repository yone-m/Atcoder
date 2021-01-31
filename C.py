import collections

n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)

c=collections.Counter(a)

cnt=0
ll=[0,0]
for k,v in c.items():
    if v>=4:
        cnt+=1
        ll.insert(0,k)
        if cnt>=2:
            break
        ll.insert(1,k)
        break
    elif v>=2:
        cnt+=1
        ll.insert(0,k)
        if cnt>=2:
            break

print(ll[0]*ll[1])