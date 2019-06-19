import numpy as np
words = lambda t : list(map(t, input().split()))
n,m = words(int)

l = 0
r = n+1

for i in range(m):
    li,ri = words(int)
    l = max(l,li)
    r = min(r,ri)

print(max(0, r - l + 1))
