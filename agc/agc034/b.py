import numpy as np
words = lambda t : list(map(t, input().split()))

str = input()
s = [c for c in str]
total = 0
i = 0
preva = 0
while i < len(s):
    #print("i:", i ,s[i:], preva)
    cnta = preva
    preva = 0
    cntbc = 0
    if s[i] == 'A':

        while i < len(s):
            #print(j, s[j])
            if s[i] == 'A':
                cnta += 1
                i+=1
            else:
                break
        while i < len(s) - 1:
            #print(k, s[k], s[k+1])
            if s[i] == 'B' and s[i+1] == 'C':
                cntbc += 1
                i += 2
            else:
                break
        if cnta > 0 and cntbc > 0:
            total += cnta * cntbc
            preva = cnta
        else:
            preva = 0
    else:
        i += 1
print(total)
