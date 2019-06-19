import sys
import numpy as np
n,k = map(int,input().split())
h = np.array(list(map(int,sys.stdin.readline().split())))

dp = np.zeros(n, dtype=int)
dp[0] = 0
for i in range(1,n):
    x = max(i-k, 0)
    #dp[i] = min(d + abs(h[i]-hd) for d, hd in zip(dp[x:i], h[x:i]))
    dp[i] = (dp[x:i] + abs(h[i] - h[x:i])).min()
print(dp[-1])
