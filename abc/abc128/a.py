import numpy as np
words = lambda t : list(map(t, input().split()))
a,p = words(int)

p = p + a*3
pie = p // 2
print(pie)
