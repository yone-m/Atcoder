import sys
n,s,d=map(int,input().split())

xl=[]
for i in range(n):
    x,y=map(int,input().split())
    xl.append([x,y])

for i in range(n):
    if xl[i][0]<s and xl[i][1]>d:
        print("Yes")
        sys.exit()

print("No")

