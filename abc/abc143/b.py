words = lambda t : list(map(t, input().split()))
n = int(input())
d = words(int)

ttl = 0
for i in range(n-1):
    for j in range(i+1,n):
        ttl += d[i] * d[j]

print(ttl)
