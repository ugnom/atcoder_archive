words = lambda t : list(map(t, input().split()))
a,b = words(int)

def gcd(x,y):
    while not y == 0:
        tmp = y
        y = x%y
        x = tmp
    return x

import math
def num_prime_factors(n):
    cnt = 0
    m = int(math.sqrt(n)) + 1
    for num in range(2,m):
        if n % num == 0:
            cnt += 1
            while n % num == 0:
                n //= num
    if not n == 1:
        cnt += 1
    return cnt

g = gcd(a,b)
cnt = num_prime_factors(g)
print(cnt+1)
