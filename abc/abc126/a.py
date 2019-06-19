import numpy as np
words = lambda t : list(map(t, input().split()))

n,k = words(int)
str = input()

c = str[k-1]
ans = str[:k-1] + c.lower() + str[k:]
print(ans)
