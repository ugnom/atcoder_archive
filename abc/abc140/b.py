words = lambda t : list(map(t, input().split()))
n = input()
a = words(int)
b = words(int)
c = words(int)

prev = -20
ans = 0
for aa in a:
    ans += b[aa-1]
    if prev == aa-2:
        ans += c[aa-2]
    prev = aa-1

print(ans)
