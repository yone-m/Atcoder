n=int(input())
al=[]
for i in range(n):
    a=int(input())
    al.append(a)

for j in range(1,n):
    if al[j-1]==al[j]:
        print("stay")
    else:
        if al[j-1]>al[j]:
            s="down"
        else:
            s="up"
        print(s+" "+str(abs(al[j-1]-al[j])))