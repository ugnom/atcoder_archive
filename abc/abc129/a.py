#import numpy as np
words = lambda t : list(map(t, input().split()))
pqr = words(int)

pqr.sort()
print(pqr[0] + pqr[1])
