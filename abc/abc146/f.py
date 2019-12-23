words = lambda t : list(map(t, input().split()))

n,m = words(int)
s = input()

dp = [0]*n
dp2 = [0]*n
for i in range(1,n):
    for j in range(m,0,-1):
        print(i,j,s[i-j])
        if i >= j and s[i-j] == "0":
            print(i,j)
            if dp[i] == 0 or dp[i] > dp[i-1]+1:
                dp[i] = dp[i-j] + 1
                dp2[i] = i-j

print(dp)
print(dp2)
cur = n-1
ans = []
while cur != 0:
    ans.append(dp2[cur])
    cur = dp2[cur]
ans = reversed(ans)
ans = list(map(lambda x: str(x+1),ans))
print(" ".join(ans))
