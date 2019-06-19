import math

words = lambda t : list(map(t, input().split()))
n = words(int)
xs = []
total = 0
for _ in range(n):
    tmp = int(input())
    xs.append(tmp)
    total += tmp

dp = [[0] * n for i in range(total)]
for i in range(1,total):
    for j in range(1,n):
        for k in range(1,n)
            dp[i][j] += dp[i-1][]
