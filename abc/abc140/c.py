words = lambda t : list(map(t, input().split()))
n = input()
b = words(int)

ans = b[0]
prev = 0
for i in range(1,len(b)):
    ans += min(b[i], b[i-1])
ans += b[-1]

print(ans)
