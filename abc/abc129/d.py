#import numpy as np
words = lambda t : list(map(t, input().split()))



h,w = words(int)
wq = [0] * w

grid = []
for i in range(h):
    grid.append(list(input()))

ans = 0
for i in range(h):
    j = 0
    while j < w:
        #print(i,j, grid[i][j])
        if grid[i][j] == '#':
            wq[j] = 0
            j+=1
            continue
        k = 0
        while j+k < w:
            if grid[i][j+k] == '.':
                k += 1
            else:
                break
        #print(i,j,k)
        if k + h > ans:
            for x in range(j,j+k):
                vplus = 0
                if not wq[x] == 0:
                    vplus = wq[x]
                else:
                    for vi in range(i-1,-1,-1):
                        if grid[vi][x] == '#':
                            break
                        else:
                            vplus += 1
                    for vi in range(i+1,h):
                        if grid[vi][x] == '#':
                            break
                        else:
                            vplus += 1
                ans = max(ans, vplus+k)
                wq[x] = vplus
        j += k
print(ans)
