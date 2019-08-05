words = lambda t : list(map(t, input().split()))
n = int(input())
ans = 0
for i in range(1,n+1):
    k = i
    d = 0
    while k != 0:
        d += 1
        k = k // 10
    if d % 2 == 1:
        ans += 1
print(ans)
