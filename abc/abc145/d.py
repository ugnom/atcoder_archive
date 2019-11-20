import math
words = lambda t : list(map(t, input().split()))
x,y = words(int)

MOD = 10**9+7

def modpow(a,b,mod):
    if b == 0: return 1
    if b % 2 == 0:
        h = modpow(a, b//2, mod)
        return (h * h) % mod
    else:
        return (a * modpow(a, b-1, mod)) % mod

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


if (x+y) % 3 != 0:
    print(0)
elif x < (x+y)//3 or y < (x+y)//3:
    print(0)
else:
    k = (x + y) // 3
    #print(k, k, y-k)
    ans = mod_comb(k,y-k,MOD)
    print(ans)
