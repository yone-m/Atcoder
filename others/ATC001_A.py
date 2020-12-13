import io
import sys

h,w=map(int,input().split())
a=[list(input()) for i in range(h)]

for i in range(h):
    for j in range(w):
        if a[i][j]=="s":
            sx,sy=i,j
        if a[i][j]=="g":
            gx,gy=i,j

todo=[[sx,sy]]
seen=[[0 for i in range(w)] for j in range(h)]
seen[sx][sy]=1

dx_dy=[[1,0],[0,1],[-1,0],[0,-1]]

while todo:
    #要素を取りだす（LIFO）
    x,y=todo.pop()

    #取りだした位置からいける4つの方向について調査
    for i in range(4):
        nx,ny=x+dx_dy[i][0],y+dx_dy[i][1]
        #nxとnyがともに区画内で、その位置が壁でもなく、
        #まだ訪れていない場合にseen[nx][ny]=1にして、todoに追加
        if 0<=nx<h and 0<=ny<w and seen[nx][ny]==0 and a[nx][ny]!="#":
            seen[nx][ny]=1
            todo.append([nx,ny])

    #もしゴールの座標が1になればYesを表示
    if seen[gx][gy]==1:
        print("Yes")
        sys.exit()

print("No")