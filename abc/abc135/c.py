words = lambda t : list(map(t, input().split()))
n = int(input())
a = words(int)
b = words(int)

ttl = 0
for i in range(n):
    if a[i] >= b[i]:
        ttl += b[i]
        a[i] -= b[i]
    else:
        ttl += min(a[i]+a[i+1],b[i])
        a[i+1] = max(0, a[i+1] - (b[i] - a[i]))
    #print(a)
print(ttl)
