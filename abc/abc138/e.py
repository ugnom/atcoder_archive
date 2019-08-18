words = lambda t : list(map(t, input().split()))
s = input()
t = input()

dict = {}
for i in range(len(s)):
    c = s[i]
    if c not in dict:
        dict[c] = []
    dict[c].append(i)

for k,v in dict.items():
    dict[k] = sorted(v)

#print(dict)

from bisect import bisect_right
def find_min_t(cur, c):
    k = bisect_right(dict[c], cur)
    if k >= len(dict[c]):
        return dict[c][0]
    else:
        return dict[c][k]

cur = -1
ans = 0
succeed = True
for c in t:
    if c not in dict:
        succeed = False
        break
    i = find_min_t(cur, c)
    #print(c, i, cur)
    if i <= cur:
        ans += len(s)
    cur = i

if succeed:
    print(ans + cur + 1)
else:
    print(-1)
