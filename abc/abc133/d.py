words = lambda t : list(map(t, input().split()))
n = int(input())
a = words(int)

a1 = 0
for i in range(n):
    if i % 2 == 0:
        a1 += a[i]
    else:
        a1 -= a[i]

a1 = a1 // 2

ans = []
ans.append(a1*2)
prevans = a1
for i in range(n-1):
    curans = a[i] - prevans
    ans.append(curans*2)
    prevans = curans

print(" ".join(map(str, ans)))
