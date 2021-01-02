import itertools

n,k=map(int,input().split())
T=[list(map(int,input().split())) for _ in range(n)]

#numsに1~N-1までの数字を入れる
nums = list(range(1,n))
ans = 0
#numsの組み合わせを順番に取りだす
for index in itertools.permutations(nums):
    #1番最初に0を入れる(長さがnになる)
	index = [0]+list(index)
	ti = 0
	for i in range(n):
        #最後にn-1→0に帰る必要がある
		ti+=T[index[i]][index[(i+1)%n]]
	if ti==k:
		ans+=1

print(ans)