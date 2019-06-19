import numpy as np
words = lambda t : list(map(t, input().split()))

n = int(input())
cs = []
for i in range(n):
    s,p = input().split()
    cs.append((s,(-1) * int(p),i+1))

cs = sorted(cs)
for (s,p,i) in cs:
    print(i)
