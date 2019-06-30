words = lambda t : list(map(t, input().split()))
n = int(input())
a = words(int)

ans = 0
for i in range(n-2):
    if (a[i] < a[i+1] and a[i+1] < a[i+2]) or a[i] > a[i+1] and a[i+1] > a[i+2]:
        ans += 1

print(ans)
