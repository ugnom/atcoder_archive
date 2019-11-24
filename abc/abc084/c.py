n = int(input())
xs = []
for i in range(n-1):
    c,s,f = list(map(int,input().split()))
    xs.append((c,s,f))

for i in range(n):
    cur = 0
    #print(i, "---------")
    for j in range(i,n-1):
        c,s,f = xs[j]
        if cur <= s:
            cur = s
        else:
            if cur % f != 0:
                cur = ((cur // f) + 1) * f
        cur += c
        #print(cur)
    print(cur)
