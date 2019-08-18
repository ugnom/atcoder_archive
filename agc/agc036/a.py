words = lambda t : list(map(t, input().split()))
s = input()
ans = 0
prev = "#"
i = 0
while i < len(s)-1:
    ans += 1
    if s[i] == prev:
        prev = s[i] + s[i+1]
        i += 2
    else:
        prev = s[i]
        i += 1
if i == len(s) - 1 and prev != s[i]:
    ans += 1

print(ans)
