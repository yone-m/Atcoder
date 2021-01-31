import math
n=int(input())

#n(a+l)/2=Nより、n*(a+l)=2N
#(l-a+1)(a+l)=2N
cnt=0

sq=int(math.sqrt(2*n))

for i in range(1,sq+1):
    if (2*n)%i==0:
        if i%2==1 and i!=(2*n//i):
            cnt+=1
        elif (2*n//i)%2==1 and i!=(2*n//i):
            cnt+=1

print(cnt*2)