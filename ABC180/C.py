import math
n=int(input())

ll=[]
ll2=[]
intn=int(math.sqrt(n))
for i in range(1,intn+1):
    if n%i==0:
        ll.append(i)
        if n//i!=i:
            ll2.append(n//i)

for a in ll:
    print(a)
for b in ll2[::-1]:
    print(b)
