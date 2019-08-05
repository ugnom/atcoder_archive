words = lambda t : list(map(t, input().split()))
n,k = words(int)
xs = words(int)

def divisor (x):
    ans = []
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            ans.append(i)
            if i != x // i:
                ans.append(x//i)
    ans.sort()
    return list(reversed(ans))

s = sum(xs)
#print(s)
ds = divisor(s)
ans = 1
#print(ds)
for d in ds:
    ms = []
    for x in xs:
        ms.append(x%d)
    ms.sort()
    #print(d,ms)
    f = 0
    f_ttl = ms[f]
    b = len(ms)-1
    b_ttl = d - ms[b]
    while f != b:
        if f_ttl >= b_ttl:
            b -= 1
            b_ttl += d - ms[b]
        else:
            f += 1
            f_ttl += ms[f]
    if k >= f_ttl:
        ans = d
        break
print(ans)
