import numpy as np
words = lambda t : list(map(t, input().split()))
n,m = words(int)
a = words(int)
cb = []
for i in range(m):
    b,c = words(int)
    cb.append((c,b))

a.sort()
cb = list(reversed(sorted(cb)))

#print(a)
#print(cb)

ind_a = 0
end = False
for (c,b) in cb:
    for i in range(b):
        if ind_a >= n:
            end = True
            break
        if a[ind_a] < c:
            a[ind_a] = c
            ind_a += 1
        else:
            end = True
            break
    if end:
        break

print(sum(a))
