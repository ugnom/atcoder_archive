words = lambda t : list(map(t, input().split()))
s = input()

p = []
i = 0
while i < len(s):
    # s[i] == 'R'
    r = 0
    l = 0
    while s[i] == 'R':
        r += 1
        i += 1
    while i < len(s) and s[i] == 'L':
        l += 1
        i += 1
    p.append((r,l))
#print(p)


ans = []
for r,l in p:
    nr = ((r+1) // 2) + l // 2
    nl = r // 2 + ((l+1) // 2)
    st = ([0] * (r-1)) + [nr] + [nl] + ([0] * (l-1))
    ans += st
print(" ".join(map(str,ans)))
