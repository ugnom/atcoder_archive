words = lambda t : list(map(t, input().split()))

MOD = 10**9 + 7

l = list(input())

dp1 = [0]*(len(l)) #equal
dp2 = [0]*(len(l)) #less than

dp1[0] = 2
dp2[0] = 1
for i in range(1,len(l)):
    if l[i] == '1':
        dp1[i] = (dp1[i-1] * 2) % MOD
        dp2[i] = (dp2[i-1] * 3 + dp1[i-1]) % MOD
    else:
        dp1[i] = dp1[i-1]
        dp2[i] = (dp2[i-1] * 3) % MOD

#print(dp1,dp2)

print((dp1[-1] + dp2[-1])%MOD)
