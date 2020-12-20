h,w=map(int,input().split())

a = [list(map(int,input().split())) for i in range(h)]

minb=100
for i in range(h):
    for j in range(w):
        minb=min(minb,a[i][j])
sumb=0
for i in range(h):
    for j in range(w):
        if minb<a[i][j]:
            sumb+=a[i][j]-minb

print(sumb)



