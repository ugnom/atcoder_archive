words = lambda t : list(map(t, input().split()))
n,m = words(int)

ss = [True] * (n+1)
dp = [0] * (n+1)
MOD = 1000000007


for i in range(m):
    k = int(input())
    ss[k] = False

dp[0] = 1
if ss[1]:
    dp[1] = 1
else:
    dp[1] = 0

for i in range(2,n+1):
    if ss[i]:
        dp[i] = (dp[i-1] + dp[i-2]) % MOD
    else:
        dp[i] = 0

#print(dp)
print(dp[n])
