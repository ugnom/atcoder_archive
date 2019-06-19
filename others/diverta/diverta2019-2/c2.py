words = lambda t : list(map(t, input().split()))
n = int(input())
a = words(int)
n = len(a)
b = a.copy()
map(abs, b)
a.sort()
b.sort()
score = -1 * b[0]
for i in range(1,n):
    score += a[i]
for i in range(n//2,n):
    score += a[i]
print(score)
if n % 2 == 0:
    print(a[-1], a[0])
    ttl = a[-1] - a[0]
    for i in range(1,n//2):
        print(a[i], ttl)
        ttl = a[i] - ttl
        print(a[-1*(i+1)], ttl)
        ttl = a[-1*(i+1)] - ttl
else:
    print(a[0], a[-1])
    ttl = a[0] - a[-1]
    for i in range(1,n//2):
        print(a[-1*(i+1)], ttl)
        ttl = a[-1*(i+1)] - ttl
        print(a[i], ttl)
        ttl = a[i] - ttl
    print(a[n//2], ttl)
