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

def mod_comb(a,b,mod):
    #print(a,b)
    if a-b < b: return mod_comb(a,a-b,mod)
    ans_mul = 1
    ans_div = 1
    for i in range(b):
        ans_mul *= a-i
        ans_div *= i+1
        ans_mul %= mod
        ans_div %= mod
    return (ans_mul * modpow(ans_div, mod-2, mod)) % mod

def modpow(a,b,mod):
    if b == 0: return 1
    if b % 2 == 0:
        h = modpow(a, b//2, mod)
        return (h * h) % mod
    else:
        return (a * modpow(a, b-1, mod)) % mod

# 上限をm、果物の種類をn（振ったさいころの数）、総和をt
def upper_limited_dup_comb(n: int, m: int, t: int) -> int:
    ans = 0
    for k in range((t-n) // m + 1 ):
        #print(k)
        ans += (-1)**k * comb(n,k) * dup_comb(n,t-n-m*k)
        #ans %= 10**9 + 7
    return ans

def comb(n,k):
    ans = 1
    div = 1
    for i in range(k):
        ans *= n-i
        div *= i+1
    #print("conb:", n, k, ans // div)
    return (ans // div) # % (10**9 + 7)

def dup_comb(n,r):
    return comb(n+r-1, r)
