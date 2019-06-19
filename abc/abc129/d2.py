import numpy as np
words = lambda t : list(map(t, input().split()))

h,w = words(int)
wq = [0] * w

grid = []
grid.append(np.array([False] * (w+2)))
for i in range(h):
    k = np.array(['#'] + list(input()) + ['#'])
    grid.append(k=='.')

grid.append(np.array([False] * (w+2)))
np.array(grid)

l = np.zeros((h+2,w+2),dtype=int)
r = np.zeros((h+2,w+2),dtype=int)
u = np.zeros((h+2,w+2),dtype=int)
d = np.zeros((h+2,w+2),dtype=int)

for i in range(h+2):
    print(grid[i])



for i in range(1,h+1):
    for j in range(1,w+1):
        l[i][j] = (l[i][j-1]+1) * grid[i][j]
        u[i][j] = (u[i-1][j]+1) * grid[i][j]

for i in range(h,0,-1):
    for j in range(w,0,-1):
        r[i][j] = (r[i][j+1]+1) * grid[i][j]
        d[i][j] = (d[i+1][j]+1) * grid[i][j]


print((l+r+u+d).max()-3)
