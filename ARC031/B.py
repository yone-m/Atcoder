import sys

a=[list(input()) for i in range(10)]

todo=[[0,0]]
seen=[[0 for _ in range(10)]for _ in range(10)]
seen[0][0]=1

dx_dy=[[1,0],[0,1],[-1,0],[0,-1]]

circle=0
change=0
for i in range(10):
    for j in range(10):
        if a[i][j]=="o":
            #〇の個数
            circle+=1

for i in range(10):
    for j in range(10):
        x,y=todo.pop()
        addcount=0
        #もし座標が〇だったら
        if a[x][y]=="o":
            for k in range(4):
                nx=x+dx_dy[k][0]
                ny=y+dx_dy[k][1]
                
                if 0<=nx<=9 and 0<=ny<=9 and a[nx][ny]=="o" and seen[nx][ny]==0:
                    seen[nx][ny]=1
                    todo.append([nx,ny])
                    addcount+=1

                if sum(seen)==circle:
                    print("YES")
                    sys.exit()

                if addcount==0:

                    
        
        


