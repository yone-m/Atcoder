a,b,c=map(int,input().split())

if a-b>=1:
    print("Takahashi")
elif b-a>=1:
    print("Aoki")
else:
    if c==0:
        print("Aoki") 
    else:
        print("Takahashi")
