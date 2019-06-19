words = lambda t : list(map(t, input().split()))
n = int(input())
v = words(int)
c = words(int)

ans = 0
for vi,ci in zip(v,c):
    ans = ans + max(0, vi-ci)

print(ans)
