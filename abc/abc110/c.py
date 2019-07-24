words = lambda t : list(map(t, input().split()))
s = input()
t = input()

dst = {}
dts = {}
a = "abcdefghijklmnopqrstuvwxyz"
for c in a:
    dst[c] = "-"
    dts[c] = "-"

ans = True
for i in range(len(s)):
    if dst[s[i]] == "-":
        dst[s[i]] = t[i]
    elif dst[s[i]] == t[i]:
        continue
    else:
        ans = False
        break
if ans == True:
    for i in range(len(s)):
        if dts[t[i]] == "-":
            dts[t[i]] = s[i]
        elif dts[t[i]] == s[i]:
            continue
        else:
            ans = False
            break

if ans:
    print("Yes")
else:
    print("No")
