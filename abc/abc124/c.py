import numpy as np
words = lambda t : list(map(t, input().split()))

s = input()

bres = 0
wres = 0
for i in range(len(s)):
    if i % 2 == 0:
        if s[i] == '0':
            bres += 1
        else:
            wres += 1
    else:
        if s[i] == '0':
            wres += 1
        else:
            bres += 1

print(min(bres,wres))
