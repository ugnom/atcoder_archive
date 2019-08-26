words = lambda t : list(map(t, input().split()))
m,d = words(int)

def is_mday(m,d1,d10):
    if d1 >= 2 and d10 >= 2 and m == d1 * d10:
        return True
    else:
        return False

ans = 0
for m0 in range(1,m+1):
    for d0 in range(1,d+1):
        d1 = d0 % 10
        d10 = d0 // 10
        if is_mday(m0,d1,d10):
            ans += 1

print(ans)
