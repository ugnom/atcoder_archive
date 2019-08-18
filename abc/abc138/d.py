import sys

sys.setrecursionlimit(10**6 + 1000)


words = lambda t : list(map(t, input().split()))
n,q = words(int)
par = [0] * n
for i in range(n-1):
    a,b = words(int)
    par[b-1] = a-1

points = [0] * n
for i in range(q):
    p,x = words(int)
    points[p-1] += x

ans = [0] * n
ans[0] = points[0]
for i in range(1,n):
    ans[i] = ans[par[i]] + points[i]


print(" ".join(map(str,ans)))
