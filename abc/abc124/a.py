import numpy as np
words = lambda t : np.array(list(map(t, input().split())))
a,b = words(int)

m = max(a,b)

if a == b:
    print(a*2)
else:
    print(max(a,b) + (max(a,b)-1))
