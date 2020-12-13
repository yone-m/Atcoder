from scipy.special import comb
l=int(input())
a=comb(l-1, 11, exact=True)
print(a)