words = lambda t : list(map(t, input().split()))
n = int(input())
s, t = words(str)
ans = ""
for i in range(n):
    ans += s[i] + t[i]
print(ans)
