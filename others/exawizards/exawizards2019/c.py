def getIndex(c):
    return ord(c) - 65


n,q = map(int,input().split())
s = input()

mins = [0]*26
curs = [0]*26
maxs = [0]*26
for _ in range(q):
    t,d = input().split()
    i = getIndex(t)
    if d == 'L':
        curs[i] -= 1
        mins[i] = min(mins[i], curs[i])
    else:
        curs[i] += 1
        maxs[i] = max(maxs[i], curs[i])

rem = 0
for i in range(n):
    mi = mins[getIndex(s[i])] + i
    ma = maxs[getIndex(s[i])] + i
    if 0 <= mi and ma < n:
        rem += 1

print(rem)
