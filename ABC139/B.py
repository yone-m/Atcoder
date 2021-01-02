a,b=map(int,input().split())

s=a
cnt=1
if b==1:
    cnt=0
while s<b:
    s+=a-1
    cnt+=1

print(cnt)