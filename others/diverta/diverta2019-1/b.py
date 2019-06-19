words = lambda t : list(map(t, input().split()))
r,g,b,n = words(int)

ans = 0
for i in range(n // r + 1):
    for j in range((n-(i*r)) // g + 1):
        #print(i, j)
        if (n - (i*r) - (j*g)) % b == 0:
            ans += 1

print(ans)
