import sys
s=input()

if len(s)==1 and s=='8':
    print("Yes")

if len(s)==2:
    ints=int(s)
    ints2=int(s[1]+s[0])

    if ints%8==0 or ints2%8==0:
        print("Yes")

if len(s)>=3:
    ll=[]
    for i in range(126):
        ll.append(8*i)

    for a in ll:
        stra=str(a).format
        cnt=0
        for j in range(3):
            if stra[j] in s:
                cnt+=1
                s.remove(stra[j])
            else:
                break
            if cnt==3:
                print("Yes")
                sys.exit()
print("No")
