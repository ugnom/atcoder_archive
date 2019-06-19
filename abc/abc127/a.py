import numpy as np
words = lambda t : list(map(t, input().split()))
a,b = words(int)

if a >= 13:
    print(b)
elif a >= 6:
    print(b//2)
else:
    print(0)
