n=int(input())

sl=set()
sl2=set()
for i in range(n):
    s=input()

    if s[0]=='!':
        sl2.add(s[1:])
    else:
        sl.add(s)
    
ns=sl & sl2
if len(ns)>0:
    print(ns.pop())
else:
    print("satisfiable")