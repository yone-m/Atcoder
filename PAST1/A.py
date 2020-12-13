import re

s=input()

if re.match(r'[0-9]{3}',s)!=None:
    ints=int(s)
    print(2*ints)
else:
    print("error")
