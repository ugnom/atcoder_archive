import math

words = lambda t : list(map(t, input().split()))
n = int(input())
d = {}

for i in range(n):
    str = "".join(sorted(input()))
    if str not in d:
        d[str] = 1
    else:
        d[str] += 1

ans = 0
for k,v in d.items():
    #print(k,v)
    if v != 1:
        ans += (v) * (v-1) // 2

print(ans)
