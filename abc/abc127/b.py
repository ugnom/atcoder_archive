import numpy as np
words = lambda t : list(map(t, input().split()))
r,d,x1 = words(int)

cur = x1
for i in range(10):
    cur = r * cur - d
    print(cur)
