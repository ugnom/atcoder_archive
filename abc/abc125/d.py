words = lambda t : list(map(t, input().split()))
n = int(input())
a = words(int)

negcnt = 0
zcnt = 0
for k in a:
    if k < 0:
        negcnt += 1
    elif k == 0:
        zcnt += 1

ans = 0
if (negcnt + zcnt) % 2 == 0:
    for k in a:
        ans += abs(k)
    print(ans)
else:
    negmin = (10**9+1)
    for k in a:
        if abs(k) < negmin:
            negmin = abs(k)
    for k in a:
        ans += abs(k)
    #print(ans,negmin)
    print(ans - 2*negmin)
