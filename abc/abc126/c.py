import numpy as np
words = lambda t : list(map(t, input().split()))

n, k = words(int)

ans = 0
for i in range(1,n+1):
    if i < k:
        t = (1/n) * (1/2)**(np.ceil(np.log2(k/i)))
    else:
        t = (1/n)
    #print(i, t)
    ans += t

print(ans)
