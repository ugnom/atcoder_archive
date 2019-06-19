def getIndex(c):
    return ord(c) - 65


n,q = map(int,input().split())
s = input()

qs = []
for _ in range(q):
    (t,d) = input().split()
    qs.append((t,d))

qs.reverse()

l = 0
lt = 0
lfound = False
rflag = False
lprev = '1'
for (t,d) in qs:
    #print(l,lt,t,d)
    if s[0] == t and d == 'L':
        lfound = True
    if lfound == False:
        continue
    if l >= n:
        break
    if t == s[l]:
        if d == 'L':
            lprev = s[l]
            lt += 1
            l += 1
            rflag = False
    elif t == lprev:
        if d == 'R':
            rflag = True

if rflag :
    lt -= 1

#print("----------")
r = n-1
rt = 0
rfound = False
lflag = False
rprev = '1'
for (t,d) in qs:
    #print(r,rt,t,d)
    if s[n-1] == t and d == 'R':
        rfound = True
    if rfound == False:
        continue
    if r < 0:
        break
    if t == s[r]:
        if d == 'R':
            rprev = s[r]
            rt += 1
            r -= 1
            lflag = False
    elif t == rprev :
        if d == 'L':
            lflag = True
if lflag :
    rt -= 1

print(max(0, n - (lt+rt)))
