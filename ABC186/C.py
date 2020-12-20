n=int(input())

ans=0

for i in range(n+1):
    nowans=0
    sn=str(i)
    for j in range(len(sn)):
        if sn[j]=='7':
            ans+=1
            nowans=1
            break
    
    if nowans==0:
        oc=oct(i)
        soc=str(oc)
        for k in range(2,len(soc)):
            if soc[k]=='7':
                ans+=1
                break

print(n-ans)