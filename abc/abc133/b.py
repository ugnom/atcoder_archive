import numpy as np

words = lambda t : list(map(t, input().split()))
n,d = words(int)

a = []
for i in range(n):
    k = words(int)
    a.append(k)

def dist(x,y):
    ttl = 0
    for x1,y1 in zip(x,y):
        ttl += (abs(x1 - y1))**2
    return np.sqrt(ttl)

ans = 0
for i in range(n-1):
    for j in range(i+1,n):
        ds = dist(a[i], a[j])
        #print(i, j, a[i], a[j], ds)
        if ds == round(ds):
            ans += 1

print(ans)
