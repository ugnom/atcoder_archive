
words = lambda t : list(map(t, input().split()))
n,m = words(int)
s = words(int)
t = words(int)
MOD = 10**9 + 7

dp = [[0] * (m+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = 1
for i in range(m+1):
    dp[0][i] = 1

for i in range(1,n+1):
    for j in range(1,m+1):
#        for k in range(n+1):
#            print(dp[k])
#        print("")
        if s[i-1] == t[j-1]:
            dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % MOD
        else:
            dp[i][j] = (dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]) % MOD

#for k in range(n+1):
#    print(dp[k])


print(dp[-1][-1])
