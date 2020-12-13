n,q=map(int,input().split())
a=list(map(int,input().split()))

tl=[]
xl=[]
yl=[]
for i in range(q):
    t,x,y=map(int,input().split())
    tl.append(t)
    xl.append(x)
    yl.append(y)


ql=[]
for i in range(q):
    if tl[i]==1:
        a[xl[i]]=a[xl[i]]^yl[i]
    else:
        suma=a[0]
        for i in range(1,n):
            suma=suma^a[i]
        ql.append(suma^a[yl[i]])

for i in q:
    print(i)
