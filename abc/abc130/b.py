words = lambda t : list(map(t, input().split()))
n,x = words(int)
a = words(int)

ans = 1
prev = 0
for i in range(len(a)):
    prev += a[i]
    if prev > x:
        break
    else:
        ans += 1
print(ans)
