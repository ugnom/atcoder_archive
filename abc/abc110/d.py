if __name__ == '__main__':
    words = lambda t : list(map(t, input().split()))
    n,m = words(int)

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
