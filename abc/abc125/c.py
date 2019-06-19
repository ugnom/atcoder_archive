import math

words = lambda t : list(map(t, input().split()))


def gcd (a,b):
    if a > b:
        t = b
        b = a
        b = t
    v = b
    while (a % b != 0):
        t = a % b
        a = b
        b = t
        v = b
    return v


n = int(input())
a = words(int)

if n == 2:
    print(max(a[0],a[1]))

else:
    cgcdm1 = max(gcd(a[0],a[1]),gcd(a[1],a[2]),gcd(a[2],a[0]))
    allgcd = gcd(a[0],gcd(a[1],a[2]))

    for i in range(3,len(a)):
        cgcdm1 = max(gcd(cgcdm1,a[i]),allgcd)
        allgcd = gcd(allgcd, a[i])

    print(cgcdm1)


def gcd (a,b):
    if a > b:
        t = b
        b = a
        b = t
    v = b
    while (a % b != 0):
        t = a % b
        a = b
        b = t
        v = b
    return v
