words = lambda t : list(map(t, input().split()))
n = int(input())
a = set()
c = "#"
ans = True
for _ in range(n):
    s = input()
    if (c != "#" and c != s[0]) or (s in a):
        ans = False
        break
    a.add(s)
    c = s[-1]
if ans:
    print("Yes")
else:
    print("No")
