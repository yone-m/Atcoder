a,b,c,d,e,f=map(int,input().split())

al=[]
al.append(a)
al.append(b)
al.append(c)
al.append(d)
al.append(e)
al.append(f)

for i in range(0,5):
    for j in range(i+1,6):
        if al[i]>al[j]:
            k=al[j]
            al[j]=al[i]
            al[i]=k
print(al[3])

