words = lambda t : list(map(t, input().split()))
a,b = words(int)

cur = 1
ans = 0
while True:
    if cur >= b:
        break
    cur -= 1
    cur += a
    ans += 1
print(ans)
