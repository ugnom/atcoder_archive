words = lambda t : list(map(t, input().split()))
n = int(input())
s = input()
prev = s[0]
ans = 1
for c in s:
    if prev != c:
        ans += 1
        prev = c

print(ans)
