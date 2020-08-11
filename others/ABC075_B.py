import io
import sys
_INPUT="""\
    6 6
#####.
#.#.##
####.#
.#..#.
#.##..
#.#...
"""
sys.stdin=io.StringIO(_INPUT)
h,w=map(int,input().split())
sl=[]
for i in range(h):
    s=input()
    sl.append(s)
ans=[[0]*w for i in range(h)]
for i in range(h):
    for j in range(w):
        if sl[i][j]==".":
            if i==0:
                if j==0:
                    if sl[0][1]=="#":
                        ans[i][j]+=1
                    if sl[1][0]=="#":
                        ans[i][j]+=1
                    if sl[1][1]=="#":
                        ans[i][j]+=1
                    
                elif j==w-1:
                    if sl[0][w-2]=="#":
                        ans[i][j]+=1
                    if sl[1][w-1]=="#":
                        ans[i][j]+=1
                    if sl[1][w-2]=="#":
                        ans[i][j]+=1
                else:
                    if sl[i][j-1]=="#":
                        ans[i][j]+=1
                    if sl[i][j+1]=="#":
                        ans[i][j]+=1
                    if sl[i+1][j-1]=="#":
                        ans[i][j]+=1
                    if sl[i+1][j]=="#":
                        ans[i][j]+=1
                    if sl[i+1][j+1]=="#":
                        ans[i][j]+=1

            elif i==h-1:
                if j==0:
                    if sl[h-2][0]=="#":
                        ans[i][j]+=1
                    if sl[h-1][1]=="#":
                        ans[i][j]+=1
                    if sl[h-2][1]=="#":
                        ans[i][j]+=1
                elif j==w-1:
                    if sl[h-1][w-2]=="#":
                        ans[i][j]+=1
                    if sl[h-2][w-1]=="#":
                        ans[i][j]+=1
                    if sl[h-2][w-2]=="#":
                        ans[i][j]+=1
                else:
                    if sl[h-1][j-1]=="#":
                        ans[i][j]+=1
                    if sl[h-1][j+1]=="#":
                        ans[i][j]+=1
                    if sl[h-2][j-1]=="#":
                        ans[i][j]+=1
                    if sl[h-2][j]=="#":
                        ans[i][j]+=1
                    if sl[h-2][j+1]=="#":
                        ans[i][j]+=1
            elif i!=0 and j==0:
                if sl[i-1][j]=="#":
                    ans[i][j]+=1
                if sl[i+1][j]=="#":
                    ans[i][j]+=1
                if sl[i][j+1]=="#":
                    ans[i][j]+=1
                if sl[i-1][j+1]=="#":
                    ans[i][j]+=1
                if sl[i+1][j+1]=="#":
                    ans[i][j]+=1
            elif i!=0 and j==w-1:
                if sl[i-1][j]=="#":
                    ans[i][j]+=1
                if sl[i+1][j]=="#":
                    ans[i][j]+=1
                if sl[i][j-1]=="#":
                    ans[i][j]+=1
                if sl[i-1][j-1]=="#":
                    ans[i][j]+=1
                if sl[i+1][j-1]=="#":
                    ans[i][j]+=1 
            else:
                if sl[i-1][j]=="#":
                    ans[i][j]+=1
                if sl[i-1][j-1]=="#":
                    ans[i][j]+=1
                if sl[i-1][j+1]=="#":
                    ans[i][j]+=1
                if sl[i][j-1]=="#":
                    ans[i][j]+=1
                if sl[i][j+1]=="#":
                    ans[i][j]+=1
                if sl[i+1][j-1]=="#":
                    ans[i][j]+=1
                if sl[i+1][j]=="#":
                    ans[i][j]+=1
                if sl[i+1][j+1]=="#":
                    ans[i][j]+=1
        else:
            ans[i][j]="#"
for i in range(h):
    for j in range(w):
        print(ans[i][j],end="")
    print()  