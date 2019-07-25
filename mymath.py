def gcd(x,y):
    while not y == 0:
        tmp = y
        y = x%y
        x = tmp
    return x

def lcm(x,y):
    return (x * y) // gcd(x,y)

import math
def primes(x):
    if x < 2:
        return []
    ps = [i for i in range(x)]
    ps[1] = 0
    for p in ps:
        if p > math.sqrt(x): break
        if p == 0: continue
        for np in range(2 * p, x, p):
            ps[np] = 0
    return [p for p in ps if p != 0]


def prime_factors(ps, x):
    pfs = []
    for p in ps:
        i = 0
        while x % p == 0:
            x = x // p
            i += 1
        if i != 0:
            pfs.append((p,i))
    return pfs
