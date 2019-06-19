import numpy as np
words = lambda t : list(map(t, input().split()))

n,a,b,c,d = words(int)
s = input()

def verify(x,y):
    posa = x
    res = True
    while posa < y:
        #print(posa,y)
        if (posa+1 == y or posa+2 == y) and s[y] == '.':
            break
        if s[posa+1] == '#' and s[posa+2] == '#':
            res = False
            break
        if s[posa+2] == '.':
            posa += 2
        elif s[posa+1] == '.':
            posa += 1
    return res

#print(c,d)
if c < d:
    if verify(a-1,c-1) and verify(b-1,d-1):
        print("Yes")
    else:
        print("No")
else:
    if verify(a-1,c-1) and verify(b-1,d-1):
        res2 = False
        for i in range(b-1,d):
            if s[i] == '.' and s[i-1] == '.' and s[i+1] == '.':
                res2 = True
                break
        if res2:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
