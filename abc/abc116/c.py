n = int(input())
a = list(map(int, input().split()))

ans = 0
cur = 0
for ai in a:
    if ai < cur:
        cur = ai
    else:
        ans += ai - cur
        cur = ai

print(ans)
