import re

s=input()
a=[]
for i in range(len(s)):
    if s[i].isupper():
        a.append(i)

w=[]
for j in range(0,len(a),2):
    w.append(s[a[j]:a[j+1]+1])

w.sort(key=str.lower)

print("".join(w))