words = lambda t : list(map(t, input().split()))
n,t = words(int)
xys = []
for i in range(n):
    x,y = words(int)
    xys.append((x,y))

xys.sort()
dp = [[0]*(t+1) for i in range(n)]

def show(dp):
  for row in dp:
      print(row)

for i in range(n):
    for j in range(1,t+1):
        dp[i][j] = dp[i-1][j]
        if xys[i][0] <= j:
            dp[i][j] = max(dp[i][j], xys[i][1] + dp[i-1][j-xys[i][0]])

#show(dp)
ans = xys[0][1]
for i in range(1,n):
    ans = max(ans, dp[i-1][t-1]+xys[i][1])

print(ans)
